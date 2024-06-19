from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_quote_received_email(full_name, user_email):
    subject = 'Service Quote Received'
    message = (
        f'Dear {full_name}, \n\n'
        'Thank you for contacting us.'
        'We have received your service quote request. '
        'We will review your request and get back to you shortly.\n\n'
        'Kind regards,\n'
        'Crystal Clear Cleaners.'
    )
    sender_email = settings.EMAIL_HOST_USER
    recipient_email = [user_email]
    send_mail(subject, message, sender_email, recipient_email)
