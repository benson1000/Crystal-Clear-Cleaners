from .models import Quote
from django import forms


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['full_name', 'email', 'phone_number',
                  'location', 'service_description']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number.as_e164) != 12:
            raise forms.ValidationError("Please enter a valid",
                                        "Kenya phone number.")
        return phone_number
