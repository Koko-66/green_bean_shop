"""Home app views"""
from django.shortcuts import render
from django.views.generic import TemplateView
# from django.contrib import messages


class HomeView(TemplateView):
    """Render home view"""
    template_name = 'home/index.html'


def error_404(request, exception):
    """Custom 404 error page"""
    return render(request, '404.html')


def error_500(request):
    """Custom 500 error page"""
    return render(request, '500.html')
