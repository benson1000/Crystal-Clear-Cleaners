from django.urls import path
from . import views

urlpatterns = [
    # Define the URL pattern for the quote view
    path('', views.quote_view, name='quote'),
    # Other URL patterns for the quote application
]
