"""Profiles app urls"""
from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    # path('', views.profile, name='profile'),
     path('<int:pk>/', views.UserProfileDetails.as_view(),
         name='profile'),
     path('<int:pk>/update/', views.UpdateProfile.as_view(),
         name='update_profile'),
     path('<int:pk>/order_history/<slug:slug>/', views.PastOrderDetailView.as_view(),
         name='past_order'),
]
