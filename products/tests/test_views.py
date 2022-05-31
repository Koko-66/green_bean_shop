"""Test product app views"""
from django.test import TestCase
from django.contrib.auth.models import User
# from django.shortcuts import reverse
from products.models import (
    Type,
    Size,
    Color,
    Category,
    Product
)


class ProductsTestCase(TestCase):
    """Test Profile views"""

    @classmethod
    def setUpTestData(cls):
        """Set up instances of models for testing"""
        cls.user = User.objects.create_user(username='test',
                                            password='password')
        cls.type1 = Type.objects.create(product_type='T-shirt',
                                        type_code='TS',
                                        slug='t-shirt')
        cls.type2 = Type.objects.create(product_type='bracelet',
                                        type_code='BRC',
                                        slug='bracelet')
        cls.size1 = Size.objects.create(size_short='M',
                                        size_long='Medium',
                                        slug='m')
        cls.size2 = Size.objects.create(size_short='L',
                                        size_long='Large',
                                        slug='l')
        cls.color1 = Color.objects.create(color='Red',
                                          color_code='RED',
                                          slug='red')
        cls.color2 = Color.objects.create(color='Green',
                                          color_code='GRN',
                                          slug='green')
        cls.category1 = Category.objects.create(category_name='new',
                                                friendly_name='New',
                                                slug='new')
        cls.category2 = Category.objects.create(category_name='test',
                                                friendly_name='Test',
                                                slug='test')

        cls.product1 = Product.objects.create(product_name='Test product1',
        #                                     product_type=cls.type1,
        #                                     size=cls.size1,
        #                                     color=cls.color1,
        #                                     category=cls.category1,
                                              price=22.99)

    def test_add_product_view_get_success_url(self):
        """Test get_success_url method in AddProductView"""

        response = self.client.get('add_product/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('products/add_product.html')

    def test_create_new_product(self):
        """Test view creating new product"""
        response = self.client.get('products/add/')
        self.assertEqual(response.status_code, 200)

        self.client.login(username='admin', password='password')
        data = {
            'product_name': 'Test product2',
            'description': 'Test description',
            'product_type': 'T-shirt',
            'category': 'new',
            'price': 23.99,
        }

        response = self.client.post('/products/add/', data=data)
        self.assertRedirects(
            response, '/accounts/login/?next=/products/add/')

    def test_update_product_view_get_success_url(self):
        """Test get_success_url method in AddProductView"""

        self.client.login(username='admin', password='password')
        response = self.client.get('product_details/1/update/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('products/edit_product.html')

        response = self.client.post(
            f'/products/product_details/{self.product1.pk}/update/')
        self.assertRedirects(
            response, f'/accounts/login/?next=/products/product_details/{self.product1.pk}/update/')
