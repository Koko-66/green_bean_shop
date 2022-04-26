"""Checkout app urls"""
from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
     path('', views.checkout, name='checkout'),
     path('success/<int:pk>/', views.checkout_success, name='success'),
     path('cancel/<int:pk>/', views.CancelView.as_view(), name='cancel'),
]
