"""Contexts with product ratings"""

from math import modf
from django.db.models import Avg
from products.models import Product, Rating


def get_ratings(request):
    """Get ratings for products"""
    products = Product.objects.all()
    avg_ratings = {}
    star_ratings = {}
    latest_product_ratings = {}
    older_product_ratings = {}
    all_rev_users = {}

    for product in products:
        avg_rating = Rating.objects.filter(
            product__pk=product.pk).aggregate(Avg('rating'))['rating__avg']
        all_prod_ratings = Rating.objects.filter(product=product)
        # Make avarage rating and number of stars available to the application
        if avg_rating:
            avg_rating = round(avg_rating * 2) / 2
            avg_ratings[product] = avg_rating
            h_star, f_stars = modf(avg_rating)
            stars = []
            count = 0
            while count < f_stars:
                stars.append('star')
                count += 1
            if h_star:
                stars.append('h_star')
            star_ratings[product] = stars

            # Get list of users who rated the product
            users_rev = []
            for rating in all_prod_ratings:
                users_rev.append(rating.user)
                all_rev_users[product] = users_rev

        latest_product_ratings[product] = Rating.objects.filter(
            product=product)[:3]
        older_product_ratings[product] = Rating.objects.filter(
            product=product)[3::]

    context = {
        'latest_product_ratings': latest_product_ratings,
        'older_product_ratings': older_product_ratings,
        'avg_ratings': avg_ratings,
        'all_rev_users': all_rev_users,
        'star_ratings': star_ratings,
    }
    return context
