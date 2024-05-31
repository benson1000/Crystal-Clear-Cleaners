from .models import Quote
from django import forms


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['full_name', 'email', 'phone_number',
                  'location', 'service_description']

    widgets = {
        'full_name': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
        'email': forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}),
        'phone_number': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        'location': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Location'}),
        'service_description': forms.Textarea(
            attrs={'class': 'form-control',
                   'placeholder': 'Service Description'}),
        }
