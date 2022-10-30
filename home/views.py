from django.views import generic
from django.shortcuts import render


class Home(generic.TemplateView):
    """View to display the site homepage"""
    template_name = "home/index.html"


def privacy_view(request):
    """
    To display the Privacy page
    """
    return render(request, "home/privacy.html")


def terms_view(request):
    """
    To display the Terms & Conditions page
    """
    return render(request, "home/terms.html")


def faqs_view(request):
    """
    To display the Terms & Conditions page
    """
    return render(request, "home/faqs.html")
