from django.shortcuts import render, redirect
from .forms import QuoteForm
from django.contrib import messages
from .tasks import send_quote_received_email

# Create your views here.

success_message = (
    'Thank you for contacting us, We will get back to you shortly. '
    'Kindly check your email.'
)


def quote_view(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            user_email = form.cleaned_data['email']
            form.save()
            # Call Celery task to send email asynchronously
            send_quote_received_email.delay(full_name, user_email)
            # Create an empty form and set the success message
            messages.success(request, success_message)
            return redirect('home')
    else:
        form = QuoteForm()
    return render(request, 'quote/quote_form.html', {'form': form})
