"""Checkout app urls"""
from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success/', views.SuccessView.as_view(),
         name='success'),
    path('cancel/', views.CancelView.as_view(),
         name='cancel'),
]
