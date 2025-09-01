from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib import messages
from .models import Usuario
from .forms import RegistroForm, LoginForm
from .serializers import UsuarioSerializer
from rest_framework import viewsets





def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data["username"]  # Django usa "username" para autenticación
            password = form.cleaned_data["password"]
            usuario = authenticate(request, correo_institucional=email, password=password)  

            if usuario is not None:
                auth_login(request, usuario)
                return redirect("inicio")
            else:
                messages.error(request, "Por favor, ingrese un correo o contraseña correcta.")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data["password1"])  # Hashear la contraseña
            usuario.save()
            auth_login(request, usuario)
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('inicio')


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
