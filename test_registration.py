# test_registration.py
import unittest
from flask_testing import TestCase
from app import app, db, User


class RegistrationTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_registration(self):
        with self.client:
            response = self.client.post('/register', data=dict(
                username='testuser',
                email='testuser@example.com',
                password='password'
            ), follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Registration successful. Please log in.', response.data)

            user = User.query.filter_by(username='testuser').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.email, 'testuser@example.com')


if __name__ == '__main__':
    unittest.main()