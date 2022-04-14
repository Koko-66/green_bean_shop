"""User profile views"""
from django.shortcuts import render, Http404
from django.views.generic import (
    DetailView,
)
from .models import UserProfile


class UserProfileView(DetailView):
    """View user profile details"""
    model = UserProfile
    template_name = 'profiles/profile.html'

    
# def profile(request):
#     """ Display the user's profile. """

#     template = 'profiles/profile.html'
#     context = {}

#     return render(request, template, context)