from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import CustomUser

# Register your models here.


class UserAdmin(BaseUserAdmin):
    """Test the admin pass for users"""
    ordering = ['id']
    list_display = ['email', 'name']


admin.site.register(CustomUser, UserAdmin)
