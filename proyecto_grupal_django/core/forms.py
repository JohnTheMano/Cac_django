from typing import Any
from django import forms 
from django.core.exceptions import ValidationError
from .models import Vendedor, Comprador, Transaccion



class NuevoAuto(forms.Form):
    listadoMarcas = [
        ('opcion1', 'Chevrolet'),
        ('opcion2', 'Fiat'),
        ('opcion3', 'Toyota'),
    ]

    nombre = forms.CharField(
        label="Nombre de contacto",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nombre de contacto'})
    )

    apellido = forms.CharField(
        label="Apellido de contacto",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Apellido de contacto'})
    )

    Mail = forms.EmailField(
        label="Mail",
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'name@example.com'})
    )

    Marca = forms.ChoiceField(
        choices=listadoMarcas,
        required=True,
        widget=forms.Select(attrs={'class': 'form-select form-select-sm', 'placeholder': 'Marca'})
    )

    Modelo = forms.CharField(
        label="Modelo",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Modelo'})
    )

    Año = forms.IntegerField(
        label="Año",
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Año'})
    )

    Precio = forms.IntegerField(
        label="Precio",
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Precio'})
    )

    def clean_Año(self):
        año = self.cleaned_data["Año"]
        if año < 2006:
            raise ValidationError("El año debe ser mayor o igual a 2006")
        return año

    def clean_Precio(self):
        precio = self.cleaned_data["Precio"]
        if precio <= 0:
            raise ValidationError("El precio debe ser un número positivo")
        return precio


class AltaVendedorModelForm(forms.ModelForm):
     class Meta:
        model = Vendedor
        #exclude = ['email']
        
        fields = '__all__'
      
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Email'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'DNI'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Teléfono'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ubicación'}),
            'financiamiento_ofrecido': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'licencia_vendedor': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Licencia de vendedor'}),
            'tipo_vendedor': forms.Select(attrs={'class': 'form-control form-control-sm'}),
        }
        
        
class AltaCompradoModelForm(forms.ModelForm):
     class Meta:
        model = Comprador
        #exclude = ['email']
        
        fields = '__all__'
      
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Email'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'DNI'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Teléfono'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ubicación'}),
            'tipo_comprador': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'preferencias_financiamiento': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'vehiculos_favoritos': forms.Select(attrs={'class': 'form-control form-control-sm', 'required': False}),
            
            
        }