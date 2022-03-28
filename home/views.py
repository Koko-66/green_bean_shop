from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

# Create your views here.
class HomeView(TemplateView):
    """Render home view"""
    template_name = 'home/home.html'
