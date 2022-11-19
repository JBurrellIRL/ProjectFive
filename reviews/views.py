from django.shortcuts import render
from .models import Reviews


def reviews(request):
    """
    Renders the reviews page
    """
    reviews_list = (
        Reviews.objects.all().filter(approved=True).order_by("-date"))
    return render(
        request,
        "reviews/reviews.html", {"reviews_list": reviews_list})
