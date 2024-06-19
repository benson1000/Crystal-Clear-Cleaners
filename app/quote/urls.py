from django.urls import path
from . import views

app_name = 'quote'

urlpatterns = [
    # Define the URL pattern for the quote view
    path('', views.quote_view, name='quote'),
    path('success/', views.success_page, name='success_page')
    # Other URL patterns for the quote application
]
