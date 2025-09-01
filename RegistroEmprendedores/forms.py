from django import forms
from .models import Entrepreneur, Product

class EntrepreneurForm(forms.ModelForm):
    class Meta:
        model = Entrepreneur
        fields = [
            'business_name', 'location', 'description', 'lunes_inicio', 'lunes_fin',
            'martes_inicio', 'martes_fin', 'miercoles_inicio', 'miercoles_fin',
            'jueves_inicio', 'jueves_fin', 'viernes_inicio', 'viernes_fin',
            'contact_info', 'logo'
        ]
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'location': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 3}),
            'lunes_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'lunes_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'martes_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'martes_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'miercoles_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'miercoles_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'jueves_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'jueves_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'viernes_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'viernes_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-sm'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm'}),
        }

class ProductForm(forms.ModelForm):
    # Field to handle the file upload in the form
    image_file = forms.FileField(required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'image_file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
