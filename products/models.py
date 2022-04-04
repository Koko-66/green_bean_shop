"""Models for products app"""
import random
from django.db import models
from cloudinary.models import CloudinaryField


class Type(models.Model):
    """Create instance of Type"""
    product_type = models.CharField(max_length=100)
    type_code = models.CharField(max_length=5)

    def __str__(self):
        """String method for type"""
        return self.pruduct_type


class Size(models.Model):
    """Create instance of Size"""
    size_short = models.CharField(max_length=25)  # e.g. 'M'
    size_long = models.CharField(max_length=50)  # e.g. 'Medium'

    def __str__(self):
        """String method for size"""
        return f'{self.size_long} ({self.size_short})'


class Color(models.Model):
    """Create instance of Color"""
    color = models.CharField(max_length=100)  # display color
    color_code = models.CharField(max_length=5)

    def __str__(self):
        """String method for color"""
        return self.color


class Category(models.Model):
    """Create instance of Category"""
    category_name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        """Meta options for Product model"""
        verbose_name_plural = "categories"

    def get_friendly_name(self):
        """Friendly name for product category"""
        return self.friendly_name

    def __str__(self):
        """String method for category"""
        return self.category_name


class Product(models.Model):
    """Create product instance"""
    product_name = models.CharField(max_length=300)
    description = models.TextField()
    code = models.CharField(
            max_length=8,
            blank=True,
            editable=False,
            unique=True,
        )
    image = CloudinaryField('image', default='No image provided', blank=True)
    categories = models.ManyToManyField(Category, related_name='categories')
    size = models.ManyToManyField(Size, related_name='sizes')
    color = models.ManyToManyField(Color, related_name='colors')
    price = models.FloatField(max_length=6, default=000.00)

    def get_sizes(self):
        """Get all sizes"""
        self.m2mfield.through.sizes.all()

    def get_colors(self):
        """Get all sizes"""
        self.m2mfield.through.colors.all()

    def get_categories(self):
        """Get list of categories to display in the template."""
        self.m2mfield.through.categories.all()
        # for category in self.category.all():
        #     categories = categories + category.name + ', '
        # return categories[:-2]

    def _generate_code(self):
        """Generate random number as SKU and check for uniqueness"""
        code = random.randint(10000, 99999)
        products = Product.objects.all()
        codes = [product.code for product in products]
        print(codes)

        while code in codes:
            new_code = random.randint(10000, 99999)
            code = new_code
            break
        # skus.append(sku)
        # print(skus)
        return code

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the sku number
        if it hasn't been set already.
        """
        if not self.code:
            self.code = self._generate_code()
        super().save(*args, **kwargs)

    def __str__(self):
        """String method for product"""
        return self.product_name
