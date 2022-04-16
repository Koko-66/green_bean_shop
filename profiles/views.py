"""User profile views"""
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
# from django.views.generic import (
#     DetailView,
# )
from profiles.forms import UserProfileForm
from .models import UserProfile

# Code from CI Boutique Ado walkthrough project
def profile(request):
    """Display the user's profile."""

    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated.')
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form
    }

    return render(request, template, context)