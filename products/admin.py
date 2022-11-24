from django.contrib import admin
from .models import Product, Format, Genre
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
    list_display = (
        'sku',
        'name',
        'artist',
        'format',
        'genre',
        'price',
        'status',
    )

    ordering = ('artist',)


@admin.register(Format)
class FormatAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
