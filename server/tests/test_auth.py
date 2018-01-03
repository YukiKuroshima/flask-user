import json
from server.tests.base import BaseTestCase


class TestAuth(BaseTestCase):
    """Tests for authentication routes"""

    def sign_up(self, email, pw, pw2, follow_redirects):
        return self.client.post(
                '/signup',
                data=dict(email=email, password=pw, confirm=pw2),
                follow_redirects=follow_redirects
                )

    def test_get_signup(self):
        """Ensure the GET /signup renders template."""
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('signup.html')
        self.assertIn(b'Sign Up', response.data)
        self.assertIn(b'action="/signup"', response.data)
        self.assertIn(b'<form', response.data)
        self.assertIn(b'method="POST"', response.data)
        self.assertIn(b'Password', response.data)
        self.assertIn(b'Repeat Password', response.data)
        self.assertIn(b'Email', response.data)
        self.assertIn(b'method="POST"', response.data)

    def test_post_signup(self):
        response = self.sign_up(
                email='yuuki@gmail.com',
                pw='mypassword',
                pw2='mypassword',
                follow_redirects=False
                )
        self.assertRedirects(
                response=response,
                location='/confirm'
                )

    def test_post_signup_template(self):
        response = self.sign_up(
                email='yuuki@gmail.com',
                pw='mypassword',
                pw2='mypassword',
                follow_redirects=True
                )
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('confirm.html')

    def test_post_signup_dup_email(self):
        self.sign_up(
                email='yuuki@gmail.com',
                pw='mypassword',
                pw2='mypassword',
                follow_redirects=True
                )
        response = self.sign_up(
                email='yuuki@gmail.com',
                pw='mypassword',
                pw2='mypassword',
                follow_redirects=True
                )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This email is taken', response.data)
