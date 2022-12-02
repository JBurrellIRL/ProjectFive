from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Allows the site admin to manage customer profiles in the admin panel"""
    list_display = (
        'user',
        'default_phone_number',
        'default_street_address1',
        'default_postcode',
    )
