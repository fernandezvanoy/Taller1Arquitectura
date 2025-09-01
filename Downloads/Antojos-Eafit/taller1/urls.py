
from django.contrib import admin
from django.urls import path,include
from cuentas import views as cuentas_views
from taller1 import views as taller1_views
from negocios import views as negocios_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', taller1_views.inicio, name='inicio'),
    path('', include('cuentas.urls')),
    path('admin/', admin.site.urls),
    path('', include('negocios.urls')),
    path('', include('RegistroEmprendedores.urls')),
    path('', include('guia.urls')),
]

#if settings.DEBUG:
 #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)