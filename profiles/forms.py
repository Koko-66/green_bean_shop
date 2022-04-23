"""User profile form"""
from django import forms
from .models import UserProfile


# Code from CI Boutique Ado walkthrough project
class UserProfileForm(forms.ModelForm):
    """User profile form"""
    class Meta:
        """Exclude fields"""
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_postcode': 'Postal Code',
            'default_county': 'County or State',
            'default_country': 'County or State',
            'default_phone_number': 'Phone Number',
        }

        self.fields['default_street_address1'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs[
                    'class'] = "form-group form-text"
            else:
                self.fields[field].widget.attrs[
                    'class'] = "form-group form-text default-country"
            self.fields[field].label = False
