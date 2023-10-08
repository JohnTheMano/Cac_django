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