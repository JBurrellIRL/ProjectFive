from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        """Correct spelling in admin panel"""
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100, null=True, blank=True)
    release_year = models.CharField(max_length=10, null=True, blank=True)
    sku = models.CharField(
        max_length=254, null=False, blank=False, unique=True)
    description = models.TextField()
    condition = models.TextField()
    excerpt = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
