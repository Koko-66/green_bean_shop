"""Urls for bag app"""
from django.urls import path
from bag import views


app_name = 'bag'
urlpatterns = [
    path('', views.ViewBag.as_view(), name='view_bag'),
    path('add/<int:pk>/', views.add_to_bag, name='add_to_bag')
]
