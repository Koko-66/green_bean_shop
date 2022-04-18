"""Urls for bag app"""
from django.urls import path
from bag import views


app_name = 'bag'
urlpatterns = [
    path('', views.ViewBag.as_view(), name='view_bag'),
    path('add/<int:item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<int:item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove_item/<int:item_id>/', views.remove_item, name='remove_item'),
]
