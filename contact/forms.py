from django import forms
from .models import Contact


# Create your forms here.
class ContactForm(forms.ModelForm):
    """Contact Form"""
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['name'].widget.attrs[
            'pattern'] = "([^\\s][A-z-\\s]+)"
        self.fields['subject'].widget.attrs[
            'pattern'] = "([^\\s][A-z-\\s]+)"
