"""Webhook handlers for integraton with Stripe"""
import json
import time
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from products.models import Product
from profiles.models import UserProfile
from .models import Order, OrderLineItem


# All functions adapted slightly from CI BoutiqueAdo walkthrough project
class StripeWhHandler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        customer_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt', {
                'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt', {
                'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        print(save_info)

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)
        name = intent.charges.data[0].billing_details
        # Replace empty strings from stripe data with None.
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != "AnonymousUser":
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.fullname = name
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_town_or_city = shipping_details.address.city
                profile.default_county = shipping_details.address.state
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_country = shipping_details.address.country
                profile.default_phone_number = shipping_details.phone
        # Check if the order already exists and if not create it in the webhook
        order_exists = False
        # Add a delay to prevent creating an order in the view and webhook as
        # well in cases when connection is slow
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    town_or_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    phone_number__iexact=shipping_details.phone,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            # Send confirmation email if created by the view
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} |\
                 SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    user_profile=profile,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
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
                                        order_line_item = OrderLineItem(
                                            order=order,
                                            product=product,
                                            quantity=quantity,
                                            product_color=color,
                                            product_size=size,
                                            )
                                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        # Send confirmation email if created by webhook handler
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} |\
                 SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
