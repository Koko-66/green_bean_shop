"""Contexts with product ratings"""

from math import modf
from django.db.models import Avg
from products.models import Product, Rating


def get_ratings(request):
    """Get ratings for products"""
    products = Product.objects.all()
    avg_ratings = {}
    latest_product_ratings = {}
    older_product_ratings = {}

    for product in products:
        avg_rating = Rating.objects.filter(
            product__pk=product.pk).aggregate(Avg('rating'))['rating__avg']
        if avg_rating:
            avg_rating = round(avg_rating * 2) / 2
            avg_ratings[product] = avg_rating
            h_star, f_stars = modf(avg_rating)
            stars = []
            count = 0
            while count < f_stars:
                stars.append('star')
                count += 1
        latest_product_ratings[product] = Rating.objects.filter(product=product)[:3]
        older_product_ratings[product] = Rating.objects.filter(product=product)[4::]

    context = {
        'latest_product_ratings': latest_product_ratings,
        'older_product_ratings': older_product_ratings,
        'avg_rating': avg_rating,
        'avg_ratings': avg_ratings,
        'stars': stars,
        'h_star': h_star,
    }
    return context
