from django.urls import path
from . import views


urlpatterns = [
    path('all/', views.products, name='all_products'),
    path('create/', views.product, name='create_product'),
    path('<int:id>/', views.productById, name='product_by_id'),
]
