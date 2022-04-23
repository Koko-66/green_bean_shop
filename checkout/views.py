"""Checkout app views"""
import stripe
from django.conf import settings

from django.views.decorators.http import require_POST
from django.contrib import messages
from django.shortcuts import (
    render,
    redirect,
    reverse,
)
from django.views.generic import TemplateView
from bag.contexts import bag_contents
from .forms import OrderForm


def checkout(request):
    """Render checkout template"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    # Prevent users accessing checkout by typing up the url.
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products:products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    # convert to integer to satisfy stripe's requirement
    stripe_total = round(total*100)
   
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        automatic_payment_methods={
                'enabled': True,
            },
    )
   
    form = OrderForm()
    DOMAIN = "https://8000-koko66-greenbeanshop-k725rwho1rk.ws-eu42.gitpod.io/"  # change in production
    success_url = DOMAIN + "checkout/success/",

    if not stripe_public_key:
        messages.warning(request, 'Stripe is missing public key. Please make sure it is set and valid.')
    template = 'checkout/checkout.html'
    context = {
        'order_form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'success_url': success_url,
    }

    return render(request, template, context)


class SuccessView(TemplateView):
    """Stripe success view"""
    template_name = "checkout/success.html"


class CancelView(TemplateView):
    """Stripe cancel view"""
    template_name = "checkout/cancel.html"
