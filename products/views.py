# from django.shortcuts import render
from django.views.generic import (
    ListView,
    # CreateView,
)
from .models import Product


class ProductListView(ListView):
    """Display a list of products"""
    model = Product
    template_name = "products/all_products.html"
    success_message = "Products displayed"