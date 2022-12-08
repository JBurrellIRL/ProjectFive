from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Reviews
from .forms import ReviewsForm
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def all_reviews(request):
    """
    Renders the reviews page
    """
    reviews_list = (
        Reviews.objects.all().filter(
            approved=True).order_by("-date"))
    return render(
        request,
        "reviews/reviews.html", {"reviews_list": reviews_list})


class AddReview(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Renders the Add Review page
    """

    model = Reviews
    form_class = ReviewsForm
    template_name = "reviews/add_review.html"
    success_message = "Your review was successfully added, \
        and is awaiting approval. Thanks!"

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class UpdateReview(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, UpdateView):

    def test_func(self):
        """
        This validates that only the reviewer or admin can edit their review.
        """
        if self.request.user.is_superuser:
            return True
        review = self.get_object()
        return review.name == self.request.user.username

    model = Reviews
    form_class = ReviewsForm
    template_name = "reviews/update_review.html"
    success_message = "Your review was successfully updated."


@login_required
def DeleteReview(request, review_id):
    """
    Delete User Review
    """
    reviews = get_object_or_404(Reviews, id=review_id)
    reviews.delete()
    messages.success(request, "Your review was deleted successfully.")
    return redirect("reviews")
