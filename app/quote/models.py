from django.db import models
from django.core.validators import MaxLengthValidator
from phonenumber_field.modelfields import PhoneNumberField  # type: ignore

# Create your models here.


class Quote(models.Model):
    LOCATION_CHOICES = [
        ('Nairobi', 'Nairobi'),
        ('Kiambu', 'Kiambu'),
        ('Machakos', 'Machakos'),
        ('Kajiado', 'Kajiado'),
    ]
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = PhoneNumberField(region='KE')
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    service_description = models.TextField(
        validators=[MaxLengthValidator(500)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_description
