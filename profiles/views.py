"""User profile views"""
# from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    DetailView,
    UpdateView,
)
from checkout.models import Order
from .forms import UserProfileForm
from .models import UserProfile

# Code from CI Boutique Ado walkthrough project
# def profile(request):
#     """Display the user's profile."""

#     profile = get_object_or_404(UserProfile, user=request.user)
#     form = UserProfileForm(instance=profile)
    
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile updated.')
#     template = 'profiles/profile.html'
#     context = {
#         'profile': profile,
#         'form': form
#     }

#     return render(request, template, context)


class UserProfileDetails(DetailView):
    """Display and update userprofile"""

    model = UserProfile
    template_name = 'profiles/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['profile'] = UserProfile.objects.get(pk=pk)
        context['orders'] = Order.objects.all()
        context['on_profile_page'] = True
        return context


class UpdateProfile(UpdateView):
    """Display and update userprofile"""

    form_class = UserProfileForm
    template_name = 'profiles/update_profile.html'
    queryset = UserProfile.objects.all()
    # success_url = HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
    success_message = "Profile updated"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['on_profile_page'] = True
        return context


class PastOrderDetailView(DetailView):
    """View details of past order"""
    model = Order
    # success_message = f'Details of order placed on {order.date}.'
    template_name = 'checkout/success.html'

    def get(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        slug = self.kwargs.get('slug')
        profile = get_object_or_404(UserProfile, pk=pk)
        order = get_object_or_404(Order, slug=slug)

        context = {
            'profile': profile,
            'order': order,
            'from_profile': True
        }
        return render(self.request, self.template_name, context)

    # def get_context_data(self, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     context = super().get_context_data(**kwargs)
    #     context['profile'] = UserProfile.objects.get(pk=pk)
    #     context['from_profile'] = True
    #     return context
