from django.test import TestCase
from django.test import Client
from quote.models import Quote
from django.core.exceptions import ValidationError


class QuoteModelTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.quote = Quote.objects.create(
            full_name="Test User",
            email="test@example.com",
            phone_number="+254712345678",
            location="Nairobi",
            service_description="Test service description",
        )

    def test_create_quote(self):
        """Test creating a quote"""
        self.assertTrue(isinstance(self.quote, Quote))
        self.assertEqual(self.quote.full_name, "Test User")
        self.assertEqual(self.quote.email, "test@example.com")
        self.assertEqual(self.quote.phone_number, "+254712345678")
        self.assertEqual(self.quote.location, "Nairobi")
        self.assertEqual(self.quote.service_description,
                         "Test service description")
        self.assertEqual(self.quote.created_at, self.quote.created_at)

    def test_quote_str_representation(self):
        """Test quote string representation"""
        self.assertEqual(str(self.quote), "Test service description")

    def test_invalid_email_raises_validation_error(self):
        """Test invalid email raises validation error"""
        invalid_data = self.quote_data.copy()
        invalid_data['email'] = 'invalid_email'
        with self.assertRaises(ValidationError):
            Quote.objects.create(**invalid_data)
