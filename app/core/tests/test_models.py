from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfull(self):
        """Test crating a new user with an email is successfull"""
        email = 'test@email.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(email=email,
                                                    password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@EMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        # assertRaises means that next code must raise an error
        # in our application, that is not implemented yet, so test fails
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@email.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)