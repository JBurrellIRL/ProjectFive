from django.contrib import admin
from .models import Reviews

# Register your models here.

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'review_title',
        'name',
        'date',
        'rating',
        'approved',
    )
