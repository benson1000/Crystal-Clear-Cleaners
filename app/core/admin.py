from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from core.models import CustomUser

# Register your models here.


class CustomUserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
                                       'is_superuser', 'groups',
                                       'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'name', 'is_staff')
    search_fields = ('email', 'name')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
