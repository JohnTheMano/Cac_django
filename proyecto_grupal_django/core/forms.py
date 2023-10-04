from typing import Any
from django import forms 
from django.core.exceptions import ValidationError

class NuevoAuto(forms.Form):
    listadoMarcas = [
        ('opcion1', 'Chevrolet'),
        ('opcion2', 'Fiat'),
        ('opcion3', 'Toyota'),
    ]
    
    nombre = forms.CharField(
        label="Nombre de contacto",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control col-md-6'})
    )

    apellido = forms.CharField(
        label="Apellido de contacto",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control col-md-6 fondo_rojo'})
    )

    Mail = forms.EmailField(
        label="Mail",
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control col-md-6'})
    )

    Marca = forms.ChoiceField(
        choices=listadoMarcas,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control col-md-6'})
    )

    Modelo = forms.CharField(
        label="Modelo",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control col-md-6'})
    )

    Año = forms.IntegerField(
        label="Año",
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control col-md-2'})
    )

    Precio = forms.IntegerField(
        label="Precio",
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control col-md-6'})
    )
    
    
    def clean_año(self):
        año= self.cleaned_data["Año"]
        if año < 2005:
            raise ValidationError(("El modelo debe ser mayor a 2006 inclusive"))
        
        return año
    
    
    def clean_Precio(self):
        precio = self.cleaned_data["Precio"]
        if precio <= 0:
            raise ValidationError("El precio debe ser un número positivo")
        return precio
        