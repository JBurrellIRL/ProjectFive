from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """ Create Order Form, choose fields to display" """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
        # To set the required number
        self.fields['phone_number'].widget.attrs[
            'pattern'] = "[0-9]{8,20}"
        # To disallow whitespace in the name field
        self.fields['full_name'].widget.attrs[
            'pattern'] = "([^\\s][A-z-\\s]+)"
        self.fields['street_address1'].widget.attrs[
            'pattern'] = "([^\\s][A-z0-9-\\s]+)"
        self.fields['town_or_city'].widget.attrs[
            'pattern'] = "([^\\s][A-z-\\s]+)"
