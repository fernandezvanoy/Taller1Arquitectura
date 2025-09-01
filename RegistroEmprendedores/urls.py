from django.urls import path,include
from .views import create_entrepreneur, success, entrepreneur_list, delete_entrepreneur, add_product
from . import views

urlpatterns = [
        path('crear-emprendedor/', create_entrepreneur, name='create_entrepreneur'),
        path('registro-exitoso/', success, name='success'),
        path('emprendedores/<int:pk>/productos/', views.view_products, name='view_products'),
        path('eliminar-emprendedor/<int:pk>/', delete_entrepreneur, name='delete_entrepreneur'),
        path('agregar-producto/<int:pk>/', add_product, name='add_product'),  # Ruta corregida
        path('producto-agregado/<int:pk>/', views.product_success, name='product_success'),
        path('editar-producto/<int:pk>/', views.edit_product, name='edit_product'),
        path('eliminar-producto/<int:pk>/', views.delete_product, name='delete_product'),
        path('emprendedores/', views.entrepreneur_list, name='entrepreneur_list'),

]