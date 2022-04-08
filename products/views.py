from django.contrib import messages
from django.db.models import Q
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
)
from django.views.generic import (
    ListView,
    # CreateView,
)
from .models import Category, Product


class ProductListView(ListView):
    """Display a list of products"""
    model = Product
    template_name = "products/all_products.html"

    def get(self, *args, **kwargs):
        """Override default get function"""
        products = Product.objects.all()
        categories = None
        query = None

        if 'category' in self.request.GET:
            categories = self.request.GET['category'].lower().split(',')
            print(f'Categories passed in the url: {categories}')
            products = products.filter(category__category_name__in=categories)
            categories = Category.objects.filter(category_name__in=categories)
            print(f'Object:{categories}')
        
        if 'q' in self.request.GET:
            query = self.request.GET['q']
            if not query:
                messages.error(self.request,
                "Type in what you want to search for")
                return redirect(reverse('products:products'))

            queries = Q(product_name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

        context = {
            'product_list': products,
            'search_term': query,
            'current_categories': categories,
        }
        return render(self.request, self.template_name, context)


class CategoriesListView(ListView):
    """Display a list of categories"""
    model = Product
    template_name = "products/all_products.html"
