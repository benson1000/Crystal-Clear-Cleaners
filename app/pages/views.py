from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'pages/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'pages/about.html', context)


def services(request):
    context = {
        'title': 'Services'
    }
    return render(request, 'pages/services.html', context)


def contact(request):
    context = {
        'title': 'Contact'
    }
    return render(request, 'pages/contact.html', context)
