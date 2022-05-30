"""User profile views"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    DetailView,
    UpdateView,
)
from checkout.models import Order
from products.models import Rating
from .forms import UserProfileForm
from .models import UserProfile


class UserProfileDetails(LoginRequiredMixin, DetailView):
    """Display and update userprofile"""

    model = UserProfile
    template_name = 'profiles/profile.html'
    success_message = 'Profile successfully updated.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        user = self.request.user
        user_reviews = Rating.objects.filter(user=user)

        context['profile'] = UserProfile.objects.get(pk=pk)
        context['orders'] = Order.objects.all()
        context['on_profile_page'] = True
        context['user_reviews'] = user_reviews
        return context


class UpdateProfile(LoginRequiredMixin, UpdateView):
    """Display and update userprofile"""

    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profiles/update_profile.html'
    success_message = "Profile updated"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['on_profile_page'] = True
        return context


class PastOrderDetailView(LoginRequiredMixin, DetailView):
    """View details of past order"""
    model = Order
    template_name = 'checkout/success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        slug = self.kwargs.get('slug')
        profile = get_object_or_404(UserProfile, pk=pk)
        order = get_object_or_404(Order, slug=slug)

        context['profile'] = profile
        context['order'] = order
        context['from_profile'] = True
        return context
