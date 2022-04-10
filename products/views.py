"""Views for products"""
from django.contrib import messages
from django.db.models import Q, functions
from django.shortcuts import (
    render,
    redirect,
    reverse,
)
from django.views.generic import (
    ListView,
    DetailView,
    # CreateView,
)
from .models import (
    Category,
    Product,
    Color,
    Size,
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

        if 'sort' in self.request.GET:
            sortkey = self.request.GET['sort']
            sort = sortkey
            if sortkey == 'product_name':
                sortkey = 'lower_name'
                products = products.annotate(
                    lower_name=functions.Lower('product_name'))

            # if sortkey == 'category':
            #     sortkey == 'category__category_name'
            #     print(f'sorted by category: {sortkey}')

            if 'direction' in self.request.GET:
                direction = self.request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

                products = products.order_by(sortkey)
                print(products)

        # filter by category
        if 'category' in self.request.GET:
            categories = self.request.GET['category'].split(',')
            print(f'Categories passed in the url: {categories}')
            products = products.filter(category__category_name__in=categories)
            categories = Category.objects.filter(category_name__in=categories)
            print(f'Object:{categories}')

        # filter by color
        if 'color' in self.request.GET:
            colors = self.request.GET['color'].split(',')
            print(f'Colors passed in the url: {colors}')
            products = products.filter(color__color__in=colors)
            colors = Color.objects.filter(color__in=colors)
            print(f'Object:{colors}')

        # filter by size
        if 'size' in self.request.GET:
            sizes = self.request.GET['size'].split(',')
            print(f'Colors passed in the url: {sizes}')
            products = products.filter(size__size_short__in=sizes)
            sizes = Size.objects.filter(size_short__in=sizes)
            print(f'Object:{sizes}')

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

        # # All categories, sizes and colors for a div with filter
        category_list = Category.objects.all()
        color_list = Color.objects.all()
        size_list = Size.objects.all()

        context = {
            'product_list': products,
            'search_term': query,
            'current_categories': categories,
            'current_sorting': current_sorting,
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
