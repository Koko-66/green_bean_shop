"""Forms for Product view"""
from django import forms
from .models import Product, Category, Color, Type


class CreateProductForm(forms.ModelForm):
    """Form to create new product."""

    class Meta:
        """Meta class specifying fields."""
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names
