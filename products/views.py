"""Views for products"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q, functions
from django.shortcuts import (
    render,
    redirect,
    reverse,
    # HttpResponse,
    # get_object_or_404,
)
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
)
from bootstrap_modal_forms.generic import (
    BSModalDeleteView,
    BSModalCreateView,
)
from .models import (
    Category,
    Product,
    Color,
    Size,
    Rating,
)
from .forms import (
    CreateProductForm,
    AddRatingForm,
)


class ProductListView(ListView):
    """Display a list of products"""
    model = Product
    template_name = 'products/all_products.html'

    # code adapted from CI boutique_ado walkthrough project
    def get(self, *args, **kwargs):
        """Override the class view default 'get' function"""
        products = Product.objects.all()
        categories = None
        query = None
        sort = None
        direction = None
        colors = None
        sizes = None

        if 'sort' in self.request.GET:
            sortkey = self.request.GET['sort']
            sort = sortkey
            print(sortkey)
            # if sortkey == 'rating':
            #     products = products.annotate(
            #         rating='rating'
            #     )

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
                direction = 'des'

            if sortkey == 'rating':
                sortkey = 'rating'
                direction = 'asc'
                # products = products.annotate(
                #     rating_int=int('products__rating'))

            if 'direction' and direction == 'desc':
                # if direction == 'desc':
                sortkey = f'-{sortkey}'

                products = products.order_by(sortkey)
                # print(products)

        # filter by category
        if 'category' in self.request.GET:
            categories = self.request.GET['category'].split(',')
            # print(f'Categories passed in the url: {categories}')
            products = products.filter(category__slug__in=categories)
            categories = Category.objects.filter(slug__in=categories)
            # print(f'Object:{categories}')
            # print(products)

        # filter by color
        if 'color' in self.request.GET:
            colors = self.request.GET['color'].split(',')
            # print(f'Colors passed in the url: {colors}')
            products = products.filter(color__slug__in=colors)
            colors = Color.objects.filter(slug__in=colors)
            # print(f'Object:{colors}')
            # print(products)

        # filter by size
        if 'size' in self.request.GET:
            sizes = self.request.GET['size'].split(',')
            # print(f'Colors passed in the url: {sizes}')
            products = products.filter(size__slug__in=sizes)
            sizes = Size.objects.filter(slug__in=sizes)
            # print(f'Object:{sizes}')
            # print(products)

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
            'product_list': products,
            'search_term': query,
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
    """Update product view"""

    form_class = CreateProductForm
    queryset = Product.objects.all()
    template_name = 'products/edit_product.html'

    success_message = 'Product successfully edited.'

    def get_success_url(self):
        """Get success url after updating product."""
        pk = self.object.pk
        return reverse_lazy('products:product_details', args=[pk])


class DeleteProductView(LoginRequiredMixin, BSModalDeleteView):
    """Delete prduct view"""
    model = Product
    template_name = 'products/product_delete.html'
    success_message = 'Product successfully deleted'
    success_url = reverse_lazy('products:products')


class AddRating(LoginRequiredMixin, BSModalCreateView):
    """Rate the product"""
    form_class = AddRatingForm
    template_name = 'products/includes/add_rating.html'
    success_message = 'Rating successfully added.'

    def get(self, *args, **kwargs):
    
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
        return render(self.request, 'products/includes/add_rating.html', context)

    def get_success_url(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        print(pk)
        return reverse_lazy('products:product_details', args=[pk])
