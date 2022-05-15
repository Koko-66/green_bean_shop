"""Home app views"""
# from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
# from django.contrib import messages


class HomeView(TemplateView):
    """Render home view"""
    template_name = 'home/index.html'

def error_404(request, exception):
    return render(request, '404.html')