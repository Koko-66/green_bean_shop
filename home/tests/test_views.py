"""Test profile views"""
from django.test import TestCase
from django.http import HttpResponseServerError


class HomeTestCase(TestCase):
    """Test Home views"""

    def test_home_page(self):
        """Test homepage redering"""
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('index.html')

    def test_404_error_page(self):
        """Test 404 page"""
        template_name = '404.html'
        response = self.client.get('testurl/')
        self.assertTemplateUsed(template_name)

    
    def my_test_500_view(self):
        """Test 500 page."""
        return HttpResponseServerError()
