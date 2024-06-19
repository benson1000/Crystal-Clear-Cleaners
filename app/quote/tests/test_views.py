from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from quote.models import Quote


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

    def test_quote_view_post_valid_form(self):
        url = reverse('quote:quote_view')
        response = self.client.post(url, self.quote_data)

        # Check if form submission redirects to success page
        self.assertRedirects(response, reverse('quote:success_page'))

        # Check if a Quote object was created in the database
        self.assertEqual(Quote.objects.count(), 1)

        # Check if the email was sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Service Quote Received')
        self.assertIn('Dear Test User,', mail.outbox[0].body)
        self.assertIn('Thank you for contacting us.', mail.outbox[0].body)

    def test_quote_view_post_invalid_form(self):
        invalid_data = self.quote_data.copy()
        invalid_data['email'] = 'invalid_email'
        url = reverse('quote:quote_view')
        response = self.client.post(url, invalid_data)

        # Check if form submission stays on the same page
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'email',
                             'Enter a valid email address.')
