"""Context processor for bag"""
from django.conf import settings


def bag_contents(request):
    """Store bag contents"""

    bag_items =[]
    total = 0
    product_count = 0
    free_delivery_threshold = settings.FREE_DELIVERY_THRESHOLD
    if total < free_delivery_threshold:
        if total < 10: 
            delivery = 2.99
        else:
            delivery = 4.99
        free_delivery_delta = free_delivery_threshold - total
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
