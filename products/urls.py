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
    path('product_details/<int:pk>/add_rating/', views.RateProduct.as_view(),
         name='add_rating'),
    # Type
    path('create_type/', views.CreateTypeView.as_view(),
         name='create_type'),
    path('add/add_type/', views.AddType.as_view(),
         name='add_type'),
    path('update_type/<int:pk>/', views.UpdateTypeView.as_view(),
         name='update_type'),
    path('delete_type/<int:pk>/', views.DeleteTypeView.as_view(),
         name='delete_type'),
    # Category
    path('create_category/', views.CreateCategoryView.as_view(),
         name='create_category'),
    path('add/add_category/', views.AddCategory.as_view(),
         name='add_category'),
    path('update_category/<int:pk>/', views.UpdateCategoryView.as_view(),
         name='update_category'),
    path('delete_category/<int:pk>/', views.DeleteCategoryView.as_view(),
         name='delete_category'),
    # Color
    path('create_color/', views.CreateColorView.as_view(),
         name='create_color'),
    path('add/add_color/', views.AddColor.as_view(),
         name='add_color'),
    path('update_color/<int:pk>/', views.UpdateColorView.as_view(),
         name='update_color'),
    path('delete_color/<int:pk>/', views.DeleteColorView.as_view(),
         name='delete_color'),
    # Size
    path('create_size/', views.CreateSizeView.as_view(),
         name='create_size'),
    path('add/add_size/', views.AddSize.as_view(),
         name='add_size'),
    path('update_size/<int:pk>/', views.UpdateSizeView.as_view(),
         name='update_size'),
    path('delete_size/<int:pk>/', views.DeleteSizeView.as_view(),
         name='delete_size'),

    path('manage_products', views.ManageProductsView.as_view(),
         name='manage_products')

]
