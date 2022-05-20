"""Forms for Product view"""
from django import forms
from bootstrap_modal_forms.mixins import (
    PopRequestMixin,
    CreateUpdateAjaxMixin
)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    HTML,
    Field,
    Div,
    Row,
    Column
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

    # https://www.programcreek.com/python/example/60825/django.forms.CheckboxSelectMultiple
    # color = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=[(c.pk, c.color) for c in Color.objects.all()],
    # )

    # size = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=[(s.pk, s.size_short) for s in Size.objects.all()],
    # )

    # category = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=[(cat.pk, cat.friendly_name) for cat in Category.objects.all()]
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names

        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            Div('product_name', css_class="col-12 col-md-11 form-control\
                mb-3 bg-light"),
            Field('description', css_class="col-12 col-md-11\
                form-control mb-3 bg-light", rows="3", ),
            Div(Row(
                Column('product_type', css_class="col-12 col-md-11"),
                Column(HTML("""
                {% if not form.product_name.value %}
                    <div class="text-end"><span>
                    <a data-form-url="{% url 'products:add_type'%}"
                        class="create-new pointer" title="Add new product type"
                        aria-label="Add new product type">
                    <i class="fas fa-plus text-green pointer"></i></a>
                    </span></div>
                {% endif %}
                """),),
                ), css_class="form-control mb-3 bg-light",),
            Div(Row(
                Column('category', css_class='col-12 col-md-11'),
                Column(HTML("""
                    <div class="text-end">
                    <span class="clear_category text-green pointer"
                        title="Clear selection" aria-label="Clear selection">
                        <i class="fas fa-eraser"></i></span>
                    {% if not form.product_name.value %}<span>
                        <a data-form-url="{% url 'products:add_category'%}"
                        class="create-new text-green pointer" title="Add new product
                        type" aria-label="Add new product type">
                        <i class="fas fa-plus"></i></a></span>
                    {% endif %}</div>
                """),),
                ), css_class="form-control mb-3 bg-light",
            ),
            Div(Row(
                Column('color', css_class='col-12 col-md-11'),
                Column(HTML("""
                <div class="text-end">
                <span class="clear_color text-green pointer"
                    title="Clear selection" aria-label="Clear selection">
                <i class="fas fa-eraser cursor-pointer"></i></span>
                {% if not form.product_name.value %}<span>
                    <a data-form-url="{% url 'products:add_color'%}"
                    class="create-new text-green pointer" title="Add new color"
                    aria-label="Add new color">
                    <i class="fas fa-plus"></i></a></span>
                {% endif %}</div>
                """),),
                ), css_class="form-control mb-3 bg-light",
            ),
            Div(Row(
                Column('size', css_class='col-12 col-md-11'),
                Column(HTML("""
                <div class="text-end">
                <span class="clear_size text-green pointer" title="Clear selection"
                    aria-label="Clear selection">
                    <i class="fas fa-eraser"></i></span>
                {% if not form.product_name.value %}<span>
                    <a data-form-url="{% url 'products:add_size'%}"
                    class="create-new" title="Add new size"
                    aria-label="Add new product type">
                    <i class="fas fa-plus text-green pointer"></i></a></span>
                    {% endif %}</div>
                """),),
                ), css_class="form-control mb-3 bg-light",
            ),
            # 'category',
            # 'size',
            # 'color',
            Div(
                'price', css_class="w-25 text-smaller"),
            HTML("""
                {%if form.image.value %}
                    <div class="my-2">
                    <img src="{{ form.instance.image.url }}"
                    class="img-fluid" style="height: 150px;"></div>
                {% else %}
                    <p class="text-smaller"> No image</p>
                {% endif %}
                """),
            HTML('<div class="mb-5 text-smaller">{{ form.image }}</div>'),
        )


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
