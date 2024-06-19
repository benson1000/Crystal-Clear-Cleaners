from django.test import TestCase
from unittest.mock import patch
from quote.tasks import send_quote_received_email


class CeleryTasksTestCae(TestCase):

    @patch('quote.tasks.send_mail')
    def test_send_quote_received_email(self, mock_send_mail):
        full_name = "Test User"
        user_email = "test@example.com"

        send_quote_received_email(full_name, user_email)

        # Assert that the send_mail function was called once
        self.assertEqual(mock_send_mail.call_count, 1)

        # Assert the arguments passed to send_mail
        subject, message, sender_email, recipient_email = \
            mock_send_mail.call_args[0]
        self.assertEqual(subject, 'Service Quote Received')
        self.assertIn('Dear Test User,', message)
        self.assertIn('Thank you for contacting us.', message)
        self.assertEqual(sender_email, 'admin@crstalclearcleaners.com')
        self.assertEqual(recipient_email, ['test@example.com'])
