"""Urls for products app"""
from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='products'),
    path('product_details/<int:pk>/', views.ProductDetailView.as_view(),
         name='product_details'),
    path('add/', views.CreateProductView.as_view(), name='add_product'),
    path('product_details/<int:pk>/update/', views.UpdateProductView.as_view(),
         name='edit_product'),
    path('product_details/<int:pk>/delete/', views.DeleteProductView.as_view(),
         name='delete_product'),
    path('product_details/<int:pk>/add_rating/', views.AddRating.as_view(),
         name='add_rating'),
]
