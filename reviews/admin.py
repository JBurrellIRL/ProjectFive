from django.contrib import admin
from .models import Reviews

# Register your models here.


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Allows the site admin to manage reviews in the admin panel"""
    list_display = (
        'review_title',
        'date',
        'name',
        'rating',
        'approved',
    )
