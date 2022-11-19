from django import forms
from .models import Reviews


class ReviewsForm(forms.ModelForm):
    """
    Creates form for customer reviews
    """

    class Meta:
        model = Reviews
        fields = ("review_title", "body", "rating", "image")
