"""Urls for quiz app"""
from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='products'),
    ]
