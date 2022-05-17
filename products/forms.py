"""Forms for Product view"""
from django import forms
from bootstrap_modal_forms.mixins import (
    PopRequestMixin,
    CreateUpdateAjaxMixin
)
from .models import (
    Product,
    Category,
    Color,
    Type,
    Size,
    Rating,
)


class CreateProductForm(forms.ModelForm):
    """Form to create new product."""

    class Meta:
        """Meta class specifying fields."""
        model = Product
        # fields = '__all__'
        exclude = ('slug',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names


class AddRatingForm(PopRequestMixin,
                    CreateUpdateAjaxMixin,
                    forms.ModelForm):
    """Form for adding product rating"""

    class Meta:
        """Specify model and form fields"""
        model = Rating
        fields = ('user', 'product', 'rating', 'comment')
        # fields = ('rating',)

        widgets = {
            'rating': forms.RadioSelect(),
            'comment': forms.Textarea(attrs={
                'lines':'5', 
                'max-width': '200px',
            })
        }
