from django.urls import path
from . import views

urlpatterns = [
    path('guia_emprendedor/', views.guia_view, name='guia_emprendedor'),
]
