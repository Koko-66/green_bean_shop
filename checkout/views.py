"""Checkout app views"""

import stripe
from django.conf import settings
# from django.views.decorators.http import require_POST
from django.contrib import messages
from django.shortcuts import (
    render,
    redirect,
    reverse,
    # get_object_or_404,
)
from django.views.generic import TemplateView
from bag.contexts import bag_contents
from products.models import Product
from .forms import OrderForm
from .models import Order, OrderLineItem


def checkout(request):
    """Render checkout template"""

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # print('Reached post')
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'phone_number': request.POST['phone_number'],
        }

        # Save form data to back end and process
        form = OrderForm(form_data)

        if form.is_valid():
            order = form.save()
            # iterate through bag items and create OrderLinmItem for each
            for item_id, item_data in bag.items():
                try:
                    # Handle products without color or size
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        # product = get_object_or_404(Product, pk=item_id)

                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        # Handle products with color, no size
                        if 'items_by_color' in item_data.keys():
                            # product = get_object_or_404(Product, pk=item_id)
                            for color, quantity in item_data[
                                    'items_by_color'].items():
                                order_line_item = OrderLineItem(
                                    order=order,
                                    product=product,
                                    quantity=quantity,
                                    product_color=color,
                                )
                                order_line_item.save()
                        else:
                            # Handle products with size, no color
                            if isinstance(list(item_data[
                                    'items_by_size'].values())[0], int):
                                for size, quantity in item_data[
                                        'items_by_size'].items():
                                    # product = get_object_or_404(
                                    #   Product, pk=item_id)
                                    order_line_item = OrderLineItem(
                                        order=order,
                                        product=product,
                                        quantity=quantity,
                                        product_size=size,
                                        )
                                    order_line_item.save()
                            else:
                                # Handle products with size and color
                                for size, colors in item_data[
                                        'items_by_size'].items():
                                    for color, quantity in colors[
                                            'items_by_color'].items():
                                        # product = get_object_or_404(
                                        #   Product, pk=item_id)
                                        order_line_item = OrderLineItem(
                                            order=order,
                                            product=product,
                                            quantity=quantity,
                                            product_color=color,
                                            product_size=size,
                                            )
                                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "We couldn't fine one or more of the products in your \
                        bag. Please contact our support team to discuss \
                        options."
                    ))
                    order.delete()
                    return redirect(reverse('bag:view_bag'))
            # Check if user wanted to save their info

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout:success', args=[order.pk]))
        else:
            messages.error(request, "Something went wrong. \
            Please double check the information you provided.")
    else:
        bag = request.session.get('bag', {})

        # Prevent users accessing checkout by typing up the url.
        if not bag:
            messages.error(request, "There's nothing in your bag at the \
                moment.")
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

    if not stripe_public_key:
        messages.warning(request, 'Stripe is missing public key. Please make \
            sure it is set and valid.')

    template = 'checkout/checkout.html'

    context = {
        'order_form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        # 'pk': order.pk,
    }

    return render(request, template, context)


def checkout_success(request, pk):
    """Stripe success view"""

    save_info = request.session.get('save_info')
    order = Order.objects.get(pk=pk)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order.order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


class CancelView(TemplateView):
    """Stripe cancel view"""

    template_name = 'checkout/cancel.html'
