# test_checkout.py
import unittest
from flask_testing import TestCase
from app import app, db, User, Product, CartItem
from werkzeug.security import generate_password_hash
import stripe

class CheckoutTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['STRIPE_PUBLIC_KEY'] = 'your_stripe_public_key'
        app.config['STRIPE_SECRET_KEY'] = 'your_stripe_secret_key'
        return app

    def setUp(self):
        db.create_all()
        # Create a test user
        hashed_password = generate_password_hash('password')
        test_user = User(username='testuser', email='testuser@example.com', password_hash=hashed_password)
        db.session.add(test_user)
        db.session.commit()

        # Create a test product
        test_product = Product(name='Test Product', description='Test Description', price=10.0, image_url='test.jpg')
        db.session.add(test_product)
        db.session.commit()

        # Add product to cart
        cart_item = CartItem(user_id=test_user.id, product_id=test_product.id, quantity=1)
        db.session.add(cart_item)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_checkout(self):
        with self.client:
            # Log in the test user
            self.client.post('/login', data=dict(
                username='testuser',
                password='password'
            ), follow_redirects=True)

            # Mock Stripe API
            stripe.Customer.create = lambda **kwargs: type('obj', (object,), {'id': 'test_customer_id'})
            stripe.Charge.create = lambda **kwargs: type('obj', (object,), {'id': 'test_charge_id'})

            # Perform checkout
            response = self.client.post('/checkout', data=dict(
                stripeToken='test_token'
            ), follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Payment successful!', response.data)

            # Check if cart is empty
            cart_items = CartItem.query.filter_by(user_id=1).all()
            self.assertEqual(len(cart_items), 0)

if __name__ == '__main__':
    unittest.main()