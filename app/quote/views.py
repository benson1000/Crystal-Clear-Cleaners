from django.shortcuts import render, redirect
from .forms import QuoteForm
from django.contrib import messages

# Create your views here.

success_message = (
    'Thank you for contacting us, We will get back to you shortly. '
    'Kindly check your email.'
)


def quote_view(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, success_message)
            return redirect('quote')
    else:
        form = QuoteForm()
    return render(request, 'quote/quote_form.html', {'form': form})
