from django.contrib import messages
from django.db.models import Q
from django.shortcuts import (
    render,
    redirect,
    reverse
)
from django.views.generic import (
    ListView,
    # CreateView,
)
from .models import Product


class ProductListView(ListView):
    """Display a list of products"""
    model = Product
    template_name = "products/all_products.html"

    def get(self, *args, **kwargs):
        """Override default get function"""
        products = Product.objects.all()
        query = None

        if 'q' in self.request.GET:
            query = self.request.GET['q']
            if not query:
                messages.error(self.request,
                "Type in what you want to search for")
                return redirect(reverse('products'))

            queries = Q(product_name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

        context = {
            'product_list': products,
            'search_term': query,
        }

        return render(self.request, self.template_name, context)


class CategoriesListView(ListView):
    """Display a list of categories"""
    model = Product
    template_name = "products/all_products.html"
