"""Order model"""
from uuid import uuid4

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.template.defaultfilters import slugify
from django_countries.fields import CountryField

from products.models import Product, Color, Size
from profiles.models import UserProfile


class Order(models.Model):
    """Create instance of Order"""

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    # Used to prevent the part of webhook handler that checks if order already
    # exists in the databse from matching purchases with same items by the same
    # client, since these two values will be unique.
    slug = models.SlugField(max_length=32, unique=True)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        """Generate order number"""
        return uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            if self.order_total < 10:
                self.delivery_cost = settings.STANDARD_DELIVERY_LOWER
            else:
                self.delivery_cost = settings.STANDARD_DELIVERY_HIGHER
        else:
            self.delivery_cost = 0
        self.grand_total = float(self.order_total) + float(self.delivery_cost)
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the save method to set the order number
        if it hasn't been set already and set it as slug
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()

        self.slug = slugify(self.order_number).upper()

        super().save(*args, **kwargs)

    def __str__(self):
        """Return Order as string"""
        return self.order_number


class OrderLineItem(models.Model):
    """
    Create instance of line item in the order
    product of same size and color x quantity
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    product_size = models.ForeignKey(Size, null=True, blank=True,
                                     on_delete=models.CASCADE)
    product_color = models.ForeignKey(Color, null=True, blank=True,
                                      on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def generate_sku(self):
        """Generate SKU"""
        sku = f'{self.product.code}-{self.product.product_type.type_code}'
        if self.product_size:
            if self.product_color:
                sku = f'{sku}-{self.product_size.size_short}{self.product_color.color_code}'
            else:
                sku = f'{sku}-{self.roduct_size.size_short}'
        else:
            if self.product_color:
                sku = sku = f'{sku}-{self.product_color.color_code}'
            else:
                sku
        return sku

    def save(self, *args, **kwargs):
        """
        Override the save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.generate_sku()} on order {self.order.order_number}'
