from django.contrib import admin
from .models import Product, Category, Genre


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'artist',
        'category',
        'genre',
        'price',
        'status',
    )

    ordering = ('artist',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
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
