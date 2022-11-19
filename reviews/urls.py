from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path("", views.all_reviews, name="reviews"),
    path("add_review/", views.AddReview.as_view(), name="add_review"),
    path("update_review/<int:pk>", views.UpdateReview.as_view(),
         name="update_review"),
    path("delete_review/<int:review_id>", views.DeleteReview,
         name="delete_review"),
]