from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class ImagenCarrusel(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to="carrusel/")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo if self.titulo else "Imagen sin titulo"



class UsuarioManager(BaseUserManager):
    def create_user(self, correo_institucional, password=None, **extra_fields):
        if not correo_institucional:
            raise ValueError("El usuario debe tener un correo institucional")

        extra_fields.setdefault("numero_celular", None)  
        usuario = self.model(
            correo_institucional=self.normalize_email(correo_institucional), 
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo_institucional, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("numero_celular", "")  
        return self.create_user(correo_institucional, password, **extra_fields)

class Usuario(AbstractBaseUser): 
    correo_institucional = models.EmailField(unique=True)
    numero_celular = models.CharField(max_length=15, blank=True, null=True)
    nombre_completo = models.CharField(max_length=150, unique=True, default="")  

    objects = UsuarioManager()

    USERNAME_FIELD = "correo_institucional"
    REQUIRED_FIELDS = ["nombre_completo"]  
