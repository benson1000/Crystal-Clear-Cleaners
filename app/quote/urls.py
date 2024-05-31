from django.urls import path
from . import views

urlpatterns = [
    # Define the URL pattern for the quote view
    path('quote/', views.quote_view, name='quote'),
    path('success/', views.success_page, name='success_page')
    # Other URL patterns for the quote application
]
