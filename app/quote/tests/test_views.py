from django.test import TestCase, Client
from django.urls import reverse
from quote.models import Quote
from unittest.mock import patch


class QuoteViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.quote_data = {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '+254712345678',
            'location': 'Nairobi',
            'service_description': 'Test service description.',
        }

    def test_quote_view_get(self):
        url = reverse('quote:quote_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quote/quote_form.html')

    @patch('quote.tasks.send_quote_received_email.delay')
    def test_quote_view_post_valid_form(self, mock_send_quote_received_email):
        url = reverse('quote:quote_view')
        response = self.client.post(url, self.quote_data)

        # Check if form submission redirects to success page
        self.assertRedirects(response, reverse('home'))

        # Check if a Quote object was created in the database
        self.assertEqual(Quote.objects.count(), 1)

        # Check if the Celery task to send the email was called
        mock_send_quote_received_email.assert_called_once_with(
            'Test User', 'test@example.com'
            )

    def test_quote_view_post_invalid_form(self):
        invalid_data = self.quote_data.copy()
        invalid_data['email'] = 'invalid_email'
        url = reverse('quote:quote_view')
        response = self.client.post(url, invalid_data)

        # Check if form submission stays on the same page
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'email',
                             'Enter a valid email address.')
