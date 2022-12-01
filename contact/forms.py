from django import forms
from .models import Contact


# Create your forms here.
class ContactForm(forms.ModelForm):
    """Contact Form"""
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
