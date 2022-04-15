"""Register profile model in the admin"""
from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Register UserProfile on admin"""
    list_display = ('pk', 'user')
