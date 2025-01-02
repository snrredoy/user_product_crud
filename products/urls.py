from django.urls import path
from . import views

urlpatterns = [
    path('product/' , views.ProductList.as_view() , name='product'),
    path('product/<int:pk>/' , views.ProductDetail.as_view() , name='product-detail'),
    path('product-all/' , views.ProductListAll.as_view() , name='product-all'),
]