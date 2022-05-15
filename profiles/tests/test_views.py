"""Test profile views"""
from django.test import TestCase
from django.contrib.auth.models import User
# from django.shortcuts import reverse
from profiles.models import UserProfile
from checkout.models import Order


class ProfileTestCase(TestCase):
    """Test Profile views"""

    @classmethod
    def setUpTestData(cls):
        """Set up instances of models for testing"""
        cls.user = User.objects.create_user(username='test',
                                            password='password')
        cls.profile = UserProfile.objects.update_or_create(user=cls.user)
        cls.order = Order.objects.create(order_number='797917hahhphap',
                                         user_profile=cls.profile[0],
                                         )

    def test_profile_detail_view(self):
        """Test profile detail view"""

        self.client.login(username='test', password='password')
        response = self.client.get(f'/profile/{self.user.pk}/')
        self.assertEqual(response.context['profile'], self.profile[0])

    def test_update_profile_view(self):
        """Test update profile view"""

        self.client.login(username='test', password='password')
        response = self.client.get(f'/profile/{self.user.pk}/update/')
        # print(response.context)
        self.assertEqual(response.context['on_profile_page'], True)

    def test_past_orders_view(self):
        """Test past orders view"""

        self.client.login(username='test', password='password')

        response = self.client.get(
            f'/{self.user.pk}/order_history/{self.order.slug}')
        self.assertTemplateUsed('checkout/success.html')

        # profile = UserProfile.objects.get(user=self.user)
        order = Order.objects.get(slug=self.order.slug)
        # self.assertEqual(self.profile[0], 'test')
        self.assertEqual(
            UserProfile.objects.get(user=self.user).user.username, 'test')
        self.assertEqual(
            Order.objects.get(slug=self.order.slug).slug, '797917HAHHPHAP')

        print(response.context)

        # self.assertEqual()
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.context['order'], self.order)
