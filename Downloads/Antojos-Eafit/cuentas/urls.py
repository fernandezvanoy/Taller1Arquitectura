from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UsuarioViewSet, logout_view


router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('registro/', views.registro_view, name='registro_view'),
    path('logout/', logout_view, name='logout'),
    path('api/', include(router.urls)),
] 
