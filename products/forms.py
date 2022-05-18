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
                'lines': '5',
                'max-width': '200px',
            })
        }


class CreateTypeForm(PopRequestMixin,
                     CreateUpdateAjaxMixin,
                     forms.ModelForm):
    """Form to create new product type."""

    class Meta:
        """Meta class specifying fields."""
        model = Type
        # fields = '__all__'
        exclude = ('slug',)


class UpdateTypeForm(PopRequestMixin,
                     forms.ModelForm):
    """Form to create new product type."""

    class Meta:
        """Meta class specifying fields."""
        model = Type
        # fields = '__all__'
        exclude = ('slug',)


class CreateCategoryForm(PopRequestMixin,
                         CreateUpdateAjaxMixin,
                         forms.ModelForm):
    """Form to create new product type."""

    class Meta:
        """Meta class specifying fields."""
        model = Category
        # fields = '__all__'
        exclude = ('slug',)


class UpdateCategoryForm(PopRequestMixin,
                         forms.ModelForm):
    """Form to create new product type."""

    class Meta:
        """Meta class specifying fields."""
        model = Category
        # fields = '__all__'
        exclude = ('slug',)


class CreateSizeForm(PopRequestMixin,
                     CreateUpdateAjaxMixin,
                     forms.ModelForm):
    """Form to create new product type."""

    class Meta:
        """Meta class specifying fields."""
        model = Size
        # fields = '__all__'
        exclude = ('slug',)


class UpdateSizeForm(PopRequestMixin,
                     forms.ModelForm):
    """Form to create new product type."""

    class Meta:
        """Meta class specifying fields."""
        model = Size
        # fields = '__all__'
        exclude = ('slug',)


class CreateColorForm(PopRequestMixin,
                      CreateUpdateAjaxMixin,
                      forms.ModelForm):
    """Form to create new product type."""

    class Meta:
        """Meta class specifying fields."""
        model = Color
        exclude = ('slug',)


class UpdateColorForm(PopRequestMixin,
                      forms.ModelForm):
    """Form to create new product type."""

    class Meta:
        """Meta class specifying fields."""
        model = Color
        # fields = '__all__'
        exclude = ('slug',)
