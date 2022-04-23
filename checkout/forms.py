
"""Checkout form"""
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """Order form"""
    class Meta:
        """Specify fields to display in the form"""
        model = Order
        fields = ('full_name', 'email', 'street_address1',
                  'street_address2', 'town_or_city',
                  'postcode', 'county', 'country',
                  'phone_number')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Postal Code',
            'country': 'Country',
            'phone_number': 'Phone Number',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            if field != 'country':
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            else:
                self.fields[field].widget.attrs[
                    'class'] = 'stripe-style-input default-country'
            self.fields[field].label = False
