"""Profiles app urls"""
from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('<int:pk>/', views.UserProfileView.as_view(), name='profile'),
    # path('', views.profile, name='profile'),

]