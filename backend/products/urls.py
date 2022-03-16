
from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.product_list_create_view_api),
    path('all/', views.product_list_create_view_api),
    path('<int:pk>/', views.product_details_view_api),
    path('<int:pk>/update/', views.product_update_view_api),
    path('<int:pk>/delete/', views.product_delete_view_api),
]
