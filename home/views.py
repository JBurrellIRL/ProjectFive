from django.views import generic


class Home(generic.TemplateView):
    """View to display the site homepage"""
    template_name = "home/index.html"
