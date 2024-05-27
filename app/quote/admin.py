from django.contrib import admin
from .models import Quote


# Register your models here.
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number',
                    'location', 'service_description', 'created_at']

    list_filter = ['email', 'phone_number', 'location']
