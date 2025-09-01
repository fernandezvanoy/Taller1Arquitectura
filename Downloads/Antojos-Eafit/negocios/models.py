from django.db import models
from RegistroEmprendedores.models import Product as REProduct

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
# Create your models here.
from django.db import models

class Entrepreneur(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Product(REProduct):
    """
    Proxy model para reutilizar el Product de la app RegistroEmprendedores
    sin duplicar tablas. Todas las consultas a negocios.Product apuntan
    a la misma tabla RegistroEmprendedores_product y datos existentes.
    """
    class Meta:
        proxy = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['name']  # opcional: ajusta el orden por defecto