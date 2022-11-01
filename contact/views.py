from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages


def contact_view(request):
    """View to render contact form"""
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()

        else:
            messages.error(request, "Error saving form")

        return redirect("success")

    contact_form = ContactForm()
    contacts = Contact.objects.all()
    return render(request, "contact/contact.html", {
        'contact_form': contact_form})


def success(request):
    """View to render form success page"""
    return render(request, 'contact/success.html')