from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        """Correct spelling in admin panel"""
        verbose_name_plural = 'Formats'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Genre(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        """Correct spelling in admin panel"""
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """Model for store products"""

    status = ((0, "Draft"), (1, "Published"))
    
    """Custom class to overwrite default objects manager, to
    filter blog posts to only show published products"""

    class ProductManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=1)

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(
        'Genre', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100, null=True, blank=True)
    release_year = models.CharField(max_length=10, null=True, blank=True)
    sku = models.CharField(
        max_length=254, null=False, blank=False, unique=True)
    description = models.TextField()
    rating = models.DecimalField(
                                 max_digits=5,
                                 decimal_places=1,
                                 null=True,
                                 blank=True)
    condition = models.TextField()
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=status, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField(default=10)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    objects = models.Manager()
    productmanager = ProductManager()

    def __str__(self):
        return self.name
