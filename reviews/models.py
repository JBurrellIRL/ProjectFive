from django.db import models
from django.urls import reverse

RATE_CHOICES = [
    (1, '1 - Awful'),
    (2, '2 - Poor'),
    (3, '3 - Average'),
    (4, '4 - Good'),
    (5, '5 - Excellent'),
]


class Reviews(models.Model):
    """
    Model for Reviews
    """

    class Meta:
        verbose_name_plural = "Reviews"

    review_title = models.CharField(max_length=100)
    name = models.CharField(max_length=20, null=True)
    image = models.ImageField(
                              upload_to="reviews_images/",
                              null=True,
                              blank=True)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(
        choices=RATE_CHOICES, null=True, blank=True)
    approved = models.BooleanField(default=False)
    body = models.TextField(null=True, blank=False, max_length=400)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("reviews")