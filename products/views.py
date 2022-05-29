"""Views for products"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q, functions, Min, Avg
from django.shortcuts import (
    render,
    redirect,
    reverse,
)
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    TemplateView,
)
from bootstrap_modal_forms.generic import (
    BSModalDeleteView,
    BSModalCreateView,
)
from . import contexts
from .models import (
    Category,
    Product,
    Color,
    Size,
    Rating,
    Type,
)
from .forms import (
    CreateProductForm,
    AddRatingForm,
    CreateTypeForm,
    UpdateTypeForm,
    CreateColorForm,
    UpdateColorForm,
    CreateSizeForm,
    # UpdateSizeForm,
    CreateCategoryForm,
    # UpdateCategoryForm,
)


class ProductListView(ListView):
    """Display a list of products"""
    model = Product
    template_name = 'products/all_products.html'

    # code adapted from CI boutique_ado walkthrough project
    def get(self, *args, **kwargs):
        """Override the class view default 'get' function"""
        all_products = Product.objects.all()
        products = Product.objects.all()
        categories = None
        query = None
        sort = None
        direction = None
        colors = None
        sizes = None
        types = None

        if 'sort' in self.request.GET:
            sortkey = self.request.GET['sort']
            sort = sortkey
            print(sortkey)

            if sortkey == 'name-asc':
                sortkey = 'product_name'
                direction = 'asc'
                products = products.annotate(
                    lower_name=functions.Lower('product_name'))

            if sortkey == 'name-desc':
                sortkey = 'product_name'
                direction = 'desc'
                products = products.annotate(
                    lower_name=functions.Lower('product_name'))

            if sortkey == 'price-asc':
                sortkey = 'price'
                direction = 'asc'

            if sortkey == 'price-desc':
                sortkey = 'price'
                direction = 'desc'

            if 'direction' and direction == 'desc':
                sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        # filter by category
        if 'category' in self.request.GET:
            categories = self.request.GET['category'].split(',')
            products = products.filter(category__slug__in=categories)
            categories = Category.objects.filter(slug__in=categories)
        # filter by color
        if 'color' in self.request.GET:
            colors = self.request.GET['color'].split(',')
            products = products.filter(color__slug__in=colors)
            colors = Color.objects.filter(slug__in=colors)

        # filter by size
        if 'size' in self.request.GET:
            sizes = self.request.GET['size'].split(',')
            products = products.filter(size__slug__in=sizes)
            sizes = Size.objects.filter(slug__in=sizes)

        # filter by type
        if 'type' in self.request.GET:
            product_types = self.request.GET['type'].split(',')
            products = products.filter(
                product_type__slug__in=product_types)
            types = Type.objects.filter(slug__in=product_types)
            print(types)


        if 'q' in self.request.GET:
            query = self.request.GET['q']
            if not query:
                messages.error(self.request,
                               "Type in what you want to search for")
                return redirect(reverse('products:products'))

            queries = Q(product_name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

        current_sorting = f'{sort}-{direction}'
        sort_type = current_sorting.split('-')[0]
        sort_direction = current_sorting.split('-')[1]

        # All categories, sizes and colors for a div with filter
        category_list = Category.objects.all()
        color_list = Color.objects.all()
        size_list = Size.objects.all()

        context = {
            'all_products': all_products,
            'product_list': products,
            'search_term': query,
            'current_types': types,
            'current_categories': categories,
            'current_sorting': current_sorting,
            'current_colors': colors,
            'current_sizes': sizes,
            'sort_type': sort_type,
            'sort_direction': sort_direction,
            'category_list': category_list,
            'color_list': color_list,
            'size_list': size_list,
        }
        return render(self.request, self.template_name, context)


class ProductDetailView(DetailView):
    """Product details view"""
    model = Product
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        """Get products with same categories"""
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        product = Product.objects.get(pk=pk)
        product_cs = product.get_categories()
        print(f'Product categories: {product_cs}')
        products = Product.objects.exclude(pk=pk)
        similar_prod = []
        for product in products:
            c = product.get_categories()
            common = any(check in product_cs for check in c)
            if common:
                similar_prod.append(product)
        print(similar_prod)
        context['similar_prod'] = similar_prod
        return context


class CreateProductView(LoginRequiredMixin, CreateView):
    """Add new product"""
    form_class = CreateProductForm
    template_name = 'products/add_product.html'
    success_message = 'New product successfully added.'

    def get_success_url(self):
        """Get success url after creating product."""
        pk = self.object.pk
        return reverse_lazy('products:product_details', args=[pk])


class UpdateProductView(LoginRequiredMixin, UpdateView):
    """Update product"""

    form_class = CreateProductForm
    queryset = Product.objects.all()
    template_name = 'products/edit_product.html'
    success_message = 'Product successfully edited.'

    def get_success_url(self):
        """Get success url after updating product."""
        pk = self.object.pk
        return reverse_lazy('products:edit_product', args=[pk])


class DeleteProductView(LoginRequiredMixin, BSModalDeleteView):
    """Delete product"""
    model = Product
    template_name = 'products/delete.html'
    success_message = 'Product successfully deleted'
    success_url = reverse_lazy('products:products')


class RateProduct(LoginRequiredMixin, BSModalCreateView):
    """Rate the product"""
    form_class = AddRatingForm
    template_name = 'products/includes/add_rating.html'
    success_message = 'Rating successfully added.'

    def get(self, *args, **kwargs):
        """Overwrite default get method and pass inital data."""
        pk = self.kwargs.get('pk')
        product = Product.objects.get(pk=pk)
        initial_data = {
            'user': self.request.user,
            'product': product,
        }
        form = AddRatingForm(self.request.POST or None, initial=initial_data)
        context = {
            'form': form,
            'product': product,
        }
        return render(self.request, self.template_name, context)

    def get_success_url(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        return reverse_lazy('products:product_details', args=[pk])


# CRUD views for Type
class CreateTypeView(LoginRequiredMixin, BSModalCreateView):
    """Add new type"""
    form_class = CreateTypeForm
    template_name = 'products/create.html'
    success_message = 'New product type successfully added.'
    success_url = reverse_lazy('products:manage_products')


class AddType(CreateTypeView):
    "Add type while adding new product"
    success_url = reverse_lazy('products:add_product')


class UpdateTypeView(LoginRequiredMixin, UpdateView):
    """Update type"""

    form_class = UpdateTypeForm
    queryset = Type.objects.all()
    template_name = 'products/edit.html'
    success_message = 'Type successfully edited.'
    success_url = reverse_lazy('products:manage_products')


class DeleteTypeView(LoginRequiredMixin, BSModalDeleteView):
    """Delete type"""
    model = Type
    template_name = 'products/delete.html'
    success_message = 'Type successfully deleted'
    success_url = reverse_lazy('products:manage_products')


# CRUD views for Category
class CreateCategoryView(LoginRequiredMixin, BSModalCreateView):
    """Add new product"""
    form_class = CreateCategoryForm
    template_name = 'products/create.html'
    success_message = 'New category successfully added.'
    success_url = reverse_lazy('products:manage_products')


class AddCategory(CreateCategoryView):
    "Add category while adding new product"
    success_url = reverse_lazy('products:add_product')


class UpdateCategoryView(LoginRequiredMixin, UpdateView):
    """Update category"""

    form_class = CreateCategoryForm
    queryset = Category.objects.all()
    template_name = 'products/edit.html'
    success_message = 'Category successfully edited.'
    success_url = reverse_lazy('products:manage_products')


class DeleteCategoryView(LoginRequiredMixin, BSModalDeleteView):
    """Delete category"""
    model = Category
    template_name = 'products/delete.html'
    success_message = 'Category successfully deleted'
    success_url = reverse_lazy('products:manage_products')


# CRUD views for Color
class CreateColorView(LoginRequiredMixin, BSModalCreateView):
    """Add new color"""
    form_class = CreateColorForm
    template_name = 'products/create.html'
    success_message = 'New color successfully added.'
    success_url = reverse_lazy('products:manage_products')


class AddColor(CreateColorView):
    "Add color while adding new product"
    success_url = reverse_lazy('products:add_product')


class UpdateColorView(LoginRequiredMixin, UpdateView):
    """Update color"""

    form_class = UpdateColorForm
    queryset = Color.objects.all()
    template_name = 'products/edit.html'
    success_message = 'Color successfully edited.'
    success_url = reverse_lazy('products:manage_products')


class DeleteColorView(LoginRequiredMixin, BSModalDeleteView):
    """Delete color"""
    model = Color
    template_name = 'products/delete.html'
    success_message = 'Color successfully deleted'
    success_url = reverse_lazy('products:manage_products')


# CRUD views for Size
class CreateSizeView(LoginRequiredMixin, BSModalCreateView):
    """Add new size"""
    form_class = CreateSizeForm
    template_name = 'products/create.html'
    success_message = 'New size successfully added.'
    success_url = reverse_lazy('products:manage_products')


class AddSize(CreateSizeView):
    "Add category while adding new product"
    success_url = reverse_lazy('products:add_product')


class UpdateSizeView(LoginRequiredMixin, UpdateView):
    """Update size"""

    form_class = CreateSizeForm
    queryset = Size.objects.all()
    template_name = 'products/edit.html'
    success_message = 'Size successfully edited.'
    success_url = reverse_lazy('products:manage_products')


class DeleteSizeView(LoginRequiredMixin, BSModalDeleteView):
    """Delete size"""
    model = Size
    template_name = 'products/delete.html'
    success_message = 'Size successfully deleted'
    success_url = reverse_lazy('products:manage_products')


class ManageProductsView(LoginRequiredMixin, TemplateView):
    """
    Renders products and supporting models for Product Management
    page
    """
    template_name = 'products/manage_products.html'

    def get(self, *args, **kwargs):
        products = Product.objects.all()
        types = Type.objects.all()
        categories = Category.objects.all()
        colors = Color.objects.all()
        sizes = Size.objects.all()

        context = {
            'products': products,
            'types': types,
            'categories': categories,
            'colors': colors,
            'sizes': sizes,
        }
        return render(self.request, self.template_name, context)
