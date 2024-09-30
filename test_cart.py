# test_cart.py
import unittest
from flask_testing import TestCase
from app import app, db, User, Product, CartItem
from werkzeug.security import generate_password_hash

class CartTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()
        # Create a test user
        hashed_password = generate_password_hash('password')
        self.test_user = User(username='testuser', email='testuser@example.com', password_hash=hashed_password)
        db.session.add(self.test_user)
        db.session.commit()

        # Create a test product
        self.test_product = Product(name='Test Product', description='Test Description', price=10.0, image_url='test.jpg')
        db.session.add(self.test_product)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_to_cart(self):
        with self.client:
            # Log in the test user
            self.client.post('/login', data=dict(
                username='testuser',
                password='password'
            ), follow_redirects=True)

            # Add product to cart
            response = self.client.get(f'/add_to_cart/{self.test_product.id}', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Item added to cart.', response.data)

            # Check if product is in cart
            cart_item = CartItem.query.filter_by(user_id=self.test_user.id, product_id=self.test_product.id).first()
            self.assertIsNotNone(cart_item)
            self.assertEqual(cart_item.quantity, 1)

    def test_view_cart(self):
        with self.client:
            # Log in the test user
            self.client.post('/login', data=dict(
                username='testuser',
                password='password'
            ), follow_redirects=True)

            # Add product to cart
            self.client.get(f'/add_to_cart/{self.test_product.id}', follow_redirects=True)

            # View cart
            response = self.client.get('/cart', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Test Product', response.data)
            self.assertIn(b'10.0', response.data)

if __name__ == '__main__':
    unittest.main()