from django.shortcuts import (
    render,
    redirect,
    reverse
)
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """Render checkout template"""
    bag = request.session.get('bag', {})
    # Prevent users accessing checkout by typing up the url.
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products:products'))

    form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': form,
    }

    return render(request, template, context)
