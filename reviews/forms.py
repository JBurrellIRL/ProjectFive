from django import forms
from .models import Reviews


class ReviewsForm(forms.ModelForm):
    """
    Creates form for customer reviews
    """
    image = forms.ImageField(label='Image')

    class Meta:
        model = Reviews
        fields = ("review_title", "body", "rating", "image")
