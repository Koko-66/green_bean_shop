"""Custom tags to use across application"""
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """Calculate subtotal per item"""
    return price * quantity
