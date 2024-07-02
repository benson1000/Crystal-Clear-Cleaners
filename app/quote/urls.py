from django.urls import path
from . import views

app_name = 'quote'

urlpatterns = [
    # Define the URL pattern for the quote view
    path('', views.quote_view, name='quote'),
]
