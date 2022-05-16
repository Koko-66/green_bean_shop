"""Models for products app"""
import random
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField


class Type(models.Model):
    """Create instance of Type"""
    product_type = models.CharField(max_length=100)
    type_code = models.CharField(max_length=5)
    slug = models. SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        """
        Override the save method to set the product_type as slug
        """
        self.slug = slugify(self.product_type)
        super().save(*args, **kwargs)

    def __str__(self):
        """String method for type"""
        return self.product_type


class Size(models.Model):
    """Create instance of Size"""
    size_short = models.CharField(max_length=25)  # e.g. 'M'
    size_long = models.CharField(max_length=50)  # e.g. 'Medium'
    slug = models. SlugField(max_length=25, unique=True)

    def save(self, *args, **kwargs):
        """
        Override the save method to set the size_short as slug
        """
        self.slug = slugify(self.size_short)
        super().save(*args, **kwargs)

    def __str__(self):
        """String method for size"""
        return f'{self.size_long} ({self.size_short})'


class Color(models.Model):
    """Create instance of Color"""
    color = models.CharField(max_length=100)  # display color
    color_code = models.CharField(max_length=5)
    slug = models. SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        """
        Override the save method to set the color as slug
        """
        self.slug = slugify(self.color)
        super().save(*args, **kwargs)

    # def color_lower(self):
    #     """Change color name to lowercase"""
    #     return self.color.lower()

    def __str__(self):
        """String method for color"""
        return self.color


class Category(models.Model):
    """Create instance of Category"""
    category_name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    slug = models. SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        """
        Override the save method to set the category_name as slug
        """
        self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

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
    product_type = models.ForeignKey(
        Type, null=True, on_delete=models.SET_NULL)
    image = CloudinaryField('image', blank=True)
    category = models.ManyToManyField(Category, related_name='categories')
    size = models.ManyToManyField(Size, blank=True, related_name='sizes')
    color = models.ManyToManyField(Color, blank=True, related_name='colors')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                blank=True, default=00.00)
    # rating = models.DecimalField(
        # max_digits=6, decimal_places=2, null=True, blank=True)

    def get_sizes(self):
        """Get all sizes for a product"""
        sizes = []
        for size in self.size.all():
            sizes.append(size)
        return sizes

    def get_colors(self):
        """Get all colors for a product"""
        colors = []
        for color in self.color.all():
            colors.append(color)
        return colors

    def get_categories(self):
        """Get list of categories for a product"""
        categories = []
        for category in self.category.all():
            categories.append(category)
        return categories

    def _generate_code(self):
        """Generate random number to use in the SKU and check for uniqueness"""
        code = random.randint(10000, 99999)
        products = Product.objects.all()
        codes = [product.code for product in products]
        # print(codes)

        while code in codes:
            new_code = random.randint(10000, 99999)
            code = new_code
            break
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


class Rating(models.Model):
    """Create instance of rating"""
    RATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rating')
    rating = models.IntegerField(default=0, choices=RATING)

    def __str__(self):
        """String method for rating"""
        return f'{self.product.product_name}_{self.rating}'
