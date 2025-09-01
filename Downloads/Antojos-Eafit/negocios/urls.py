from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.categorias_view, name='categorias'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('entrepreneur/<int:pk>/', views.entrepreneur_detail, name='entrepreneur_detail'),
    path('categoria/<str:category_name>/', views.category_products, name='category_products'),

]