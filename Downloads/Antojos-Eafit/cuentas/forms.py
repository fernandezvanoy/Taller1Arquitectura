from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Usuario
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["correo_institucional", "nombre_completo", "numero_celular", "password1", "password2"] 

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["password1"]) 
        if commit:
            usuario.save()
        return usuario  
    
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'})
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].help_text = ""  
        self.fields["password2"].help_text = ""
        self.fields["password1"].widget.attrs.update({"placeholder": "Ingrese su contraseña"})
        self.fields["password2"].widget.attrs.update({"placeholder": "Repita su contraseña"})
        self.fields["nombre_completo"].widget.attrs.update({"placeholder": "Ingrese su nombre completo"})
        self.fields["correo_institucional"].widget.attrs.update({"placeholder": "Ingrese su correo institucional"})
        self.fields["numero_celular"].widget.attrs.update({"placeholder": "Ingrese su numero de celular"})

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Correo Institucional") 
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput())
