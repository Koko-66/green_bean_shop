"""Checkout app views"""
import json
import stripe
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import (
    render,
    redirect,
    reverse,
)
from django.views.decorators.http import require_POST
from bag.contexts import bag_contents
from products.models import (
    Product,
    Color,
    Size,
)
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from .forms import OrderForm
from .models import Order, OrderLineItem


# Code from CI BoutiqueAdo walkthrough project
@require_POST
def cache_checkout_data(request):
    """"Store checkout data to pass to webhook"""

    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


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
            order = form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            # iterate through bag items and create OrderLinmItem for each
            for item_id, item_data in bag.items():
                try:
                    # Handle products without color or size
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        # Handle products with color, no size
                        if 'items_by_color' in item_data.keys():
                            for color, quantity in item_data[
                                    'items_by_color'].items():
                                color = Color.objects.get(slug=color)
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
                                    size = Size.objects.get(slug=size)
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
                                    size = Size.objects.get(slug=size)
                                    for color, quantity in colors[
                                            'items_by_color'].items():
                                        color = Color.objects.get(slug=color)
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

            return redirect(reverse('checkout:success',
                            args=[order.order_number]))
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

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'county': profile.default_county,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                    'phone_number': profile.default_phone_number,

                })
            except UserProfile.DoesNotExist:
                form = OrderForm()
        else:
            form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe is missing public key. Please make \
            sure it is set and valid.')

    template = 'checkout/checkout.html'

    context = {
        'order_form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """Stripe success view"""

    save_info = request.session.get('save_info')
    order = Order.objects.get(order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_town_or_city': order.town_or_city,
                'default_county': order.county,
                'default_postcode': order.postcode,
                'default_country': order.country,
                'default_phone_number': order.phone_number,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
