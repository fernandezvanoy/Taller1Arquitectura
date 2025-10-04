from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_review, name='add_review'),
    path('product/<int:product_id>/', views.product_reviews, name='product_reviews'),
]
