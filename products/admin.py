"""Register product models in the admin"""
from django.contrib import admin
from .models import Type, Size, Color, Category, Product, Rating


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    """Register Type on admin"""
    list_display = ('id', 'product_type', 'type_code', 'slug')


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    """Register Size on admin"""
    list_display = ('id', 'size_long', 'size_short', 'slug')


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    """Register Color on admin"""
    list_display = ('id', 'color', 'color_code', 'slug')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Register Category on admin"""
    list_display = ('id', 'category_name', 'friendly_name', 'slug')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Register Rating on admin"""
    list_display = ('id', 'rating', 'user', 'product')
    list_filter = ['product']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Register Product on admin"""
    list_display = ('id', 'product_name', 'description', 'code', 'price')
    list_filter = ('product_name', 'category')
    search_fields = ['product_name', 'category']
