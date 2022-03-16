from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.products, name='all_products'),
    path('product/', views.product, name='create_product'),
    path('product/<int:id>/', views.productById, name='product_by_id'),
]
