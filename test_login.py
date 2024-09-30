# test_login.py
import unittest
from flask_testing import TestCase
from app import app, db, User
from werkzeug.security import generate_password_hash

class LoginTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()
        # Create a test user
        hashed_password = generate_password_hash('password')
        test_user = User(username='testuser', email='testuser@example.com', password_hash=hashed_password)
        db.session.add(test_user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login(self):
        with self.client:
            response = self.client.post('/login', data=dict(
                username='testuser',
                password='password'
            ), follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Logged in successfully.', response.data)

if __name__ == '__main__':
    unittest.main()