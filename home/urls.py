from django.urls import path
from . import views


urlpatterns = [
    path("", views.Home.as_view(), name='home'),
    path("privacy-policy/", views.privacy_view, name='privacy'),
    path("terms/", views.terms_view, name='terms'),
    path("faqs/", views.faqs_view, name='faqs'),

]
