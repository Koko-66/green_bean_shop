"""Context processor for bag"""
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """Store bag contents"""

    bag_items = []
    total = 0
    product_count = 0
    free_delivery_threshold = settings.FREE_DELIVERY_THRESHOLD
    bag = request.session.get('bag', {})
    # Iterate through bag, update product_count and grab other data
    # If item has no size nor color
    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            # Handle products with color, no size
            if 'items_by_color' in item_data.keys():
                for color, quantity in item_data['items_by_color'].items():
                    product = get_object_or_404(Product, pk=item_id)
                    total += quantity * product.price
                    product_count += quantity
                    bag_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'color': color
                    })
            else:
                # Handle products with size, no color
                if isinstance(list(
                              item_data['items_by_size'].values())[0], int):
                    for size, quantity in item_data['items_by_size'].items():
                        product = get_object_or_404(Product, pk=item_id)
                        total += quantity * product.price
                        product_count += quantity
                        bag_items.append({
                            'item_id': item_id,
                            'quantity': quantity,
                            'product': product,
                            'size': size,
                        })
                else:
                    # Handle products with size and color
                    for size, colors in item_data['items_by_size'].items():
                        for color, quantity in colors[
                                'items_by_color'].items():
                            product = get_object_or_404(Product, pk=item_id)
                            total += quantity * product.price
                            product_count += quantity
                            bag_items.append({
                                'item_id': item_id,
                                'quantity': quantity,
                                'product': product,
                                'size': size,
                                'color': color
                            })

    if total < free_delivery_threshold:
        if total < 10:
            delivery = 2.99
        else:
            delivery = 4.99
        free_delivery_delta = round(free_delivery_threshold - total + 0.01, 2)
    else:
        delivery = 0
        free_delivery_delta = 0
    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_threshold': free_delivery_threshold,
        'free_delivery_delta': free_delivery_delta,
        'grand_total': grand_total,
    }

    return context
