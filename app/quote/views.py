from django.shortcuts import render, redirect
from .forms import QuoteForm

# Create your views here.

success_message = (
    'Thank you for contacting us, We will get back to you shortly. '
    'Kindly check your email.'
)


def success_page(request):
    return render(request, 'quote/success.html')


def quote_view(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = QuoteForm()
    return render(request, 'quote/quote_form.html', {'form': form})
