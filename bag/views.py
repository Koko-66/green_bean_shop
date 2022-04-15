from django.shortcuts import render
from django.views.generic import TemplateView


class ViewBag(TemplateView):
    """Render bag view."""
    template_name = 'bag/bag.html'
