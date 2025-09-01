from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["correo_institucional", "nombre_completo", "numero_celular", "password"]  # Campos actualizados
