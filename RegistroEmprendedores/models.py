from django.conf import settings
from django.db import models
from .models_base import TimeStampedModel # Cambio

class Entrepreneur(TimeStampedModel): # CAMBIO: Se hereda
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)  
    business_name = models.CharField(max_length=255)  
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    lunes_inicio = models.TimeField(blank=True, null=True)
    lunes_fin = models.TimeField(blank=True, null=True)
    martes_inicio = models.TimeField(blank=True, null=True)
    martes_fin = models.TimeField(blank=True, null=True)
    miercoles_inicio = models.TimeField(blank=True, null=True)
    miercoles_fin = models.TimeField(blank=True, null=True)
    jueves_inicio = models.TimeField(blank=True, null=True)
    jueves_fin = models.TimeField(blank=True, null=True)
    viernes_inicio = models.TimeField(blank=True, null=True)
    viernes_fin = models.TimeField(blank=True, null=True)
    contact_info = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.business_name

class Product(TimeStampedModel): # CAMBIO: Se hereda
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True) # Nuevo campo para URL de Cloudinary

    def __str__(self):
        return self.name