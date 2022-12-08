from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


def contact_view(request):
    """View to render contact form"""
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = "JBs Record Store Enquiry"
            body = {
                'name': contact_form.cleaned_data['name'],
                'email': contact_form.cleaned_data['email'],
                'subject': contact_form.cleaned_data['subject'],
                'message': contact_form.cleaned_data['message'],
                }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'jonathanbtest@gmail.com',
                                            ['jonathanbtest@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            contact_form.save()

        else:
            messages.error(
                request, "Error saving form. Please check your submission.")
            return redirect("contact")

        return redirect("success")

    contact_form = ContactForm()
    return render(request, "contact/contact.html", {
        'contact_form': contact_form})


def success(request):
    """View to render form success page"""
    return render(request, 'contact/success.html')
