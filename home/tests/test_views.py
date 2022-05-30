"""Test profile views"""
from django.test import TestCase


class HomeTestCase(TestCase):
    """Test Home views"""

    def test_500_error_page(self):
        """Test """
        response = self.client.get('products/146580')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('home/500.html')
