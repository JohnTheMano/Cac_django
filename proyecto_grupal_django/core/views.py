from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from datetime import datetime
from .forms import  NuevoAuto
from .models import Vendedor, Vehiculo, Comprador, Transaccion
from .forms import AltaVendedorModelForm, AltaCompradoModelForm
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
#from django.views.generic.list import ListView
from django.urls import reverse_lazy



# Create your views here.
def index(request):
    #if request.method == "GET":
        return render(request, "core/index.html")

def nosotros(request):
    return render(request,'core/nosotros.html')


def nombre_usuario(request,usuario):
    return HttpResponse(
       f"""<h1>Bienvenido: {usuario}!</h1>"""
    )


def vehiculos_todos(request):
     
   
    vehiculos = [
        {'nombre': 'Renault Sandero Stepway', 'año': 2020},
        {'nombre': 'Peugeot 208', 'año': 2021},
       {'nombre': 'Volkswagen Tuareg', 'año': 2021},
       {'nombre': 'Mitsubishi Colt', 'año': 2023},
        {'nombre': 'Ford ka', 'año': 2023}]

 
    context = {
           'listado_vehiculos': vehiculos
            
         }

    return render(request, 'core/vehiculos_listado.html', context)

def vehiculos_anio(request, anio):
     
   
    vehiculos = [
        {'nombre': 'Renault Sandero Stepway', 'año': 2020},
        {'nombre': 'Peugeot 208', 'año': 2021},
        {'nombre': 'Volkswagen Tuareg', 'año': 2021},
        {'nombre': 'Mitsubishi Colt', 'año': 2023},
        {'nombre': 'Ford ka', 'año': 2023}]

   
    vehiculos_filtrados = []

    
    for vehiculo in vehiculos:
        
        if vehiculo.get('año') == int(anio):
            
            vehiculos_filtrados.append(vehiculo)

    context = {
        'listado_vehiculos': vehiculos_filtrados,
        'anio_parametro': anio
    }

    return render(request, 'core/vehiculos_listado.html', context)
    
def vehiculos_estado(request,estado):
    return HttpResponse(
       f"""<h1>Estado del vehículo: {estado}</h1>"""
    )

def vehiculos_ficha(request):
     context = {
          'nombre_vehículo': 'Sandero Stepway',
          'marca':'Renault',
          'anio':'2020',
          'entrega_inmediata':False,
     }
     return render( request ,'core/oferta_del_dia.html',context )
 
def registrar_venta(request):
    
    if request.method == "POST":
    # Creo la instancia del formulario con los datos cargados en pantalla
        formulario =  NuevoAuto(request.POST)
    # Valido y proceso los datos.
        if formulario.is_valid():
            print(formulario.cleaned_data)
            print(messages.info(request,"Consulta enviada con exito"))
            print(messages.get_messages(request))
            #dar de alta info
            return redirect(reverse("registrar_auto"))
            
    else:
    # Creo el formulario vacío con los valores por defecto
        formulario =  NuevoAuto()
    
    context = {
        'venta_form' : formulario
    }
    
    return render( request ,'core/vende_tu_auto.html',context )

#------Vendedor----------------------
class VendedorCreateView(CreateView):
    model = Vendedor
    form_class = AltaVendedorModelForm
    template_name='core/alta_vendedor.html'
    success_url='vendedores_listado'
    
    #fields = '__all__'
    
    
class VendedorListView(ListView):
    model = Vendedor
    context_object_name = 'listado_vendedor'
    template_name='core/vendedor_listado.html'
    #queryset= Vendedor.objects.filter(tipo_vendedor= "Persona")
    
class VendedorDeleteView(DeleteView):
    model = Vendedor
    #el nombre de la plantilla es por defecto de django
    template_name = 'core/vendedor_confirm_delete.html' 
    success_url = reverse_lazy('vendedores_listado')
    
class VendedorUpdateView(UpdateView):
    pass


#-------------------COMPRADOR--------------------
class CompradorCreateView(CreateView):
    model = Comprador
    form_class = AltaCompradoModelForm
    template_name='core/alta_Comprador.html'
    success_url='compradores_listado'
    
class CompradorListView(ListView):
    model = Comprador
    context_object_name = 'listado_comprador'
    template_name='core/comprador_listado.html'
    #queryset= Vendedor.objects.filter(tipo_vendedor= "Persona")

    
class CompradorDeleteView(DeleteView):
    model = Comprador
    #el nombre de la plantilla es por defecto de django
    template_name = 'core/comprador_confirm_delete.html' 
    success_url = reverse_lazy('compradores_listado')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#listview Vehiculos
"""
class VehiculosListView(ListView):
    
    vehiculos = [
        {'nombre': 'Renault Sandero Stepway', 'año': 2020},
        {'nombre': 'Peugeot 208', 'año': 2021},
        {'nombre': 'Volkswagen Tuareg', 'año': 2021},
        {'nombre': 'Mitsubishi Colt', 'año': 2023},
        {'nombre': 'Ford ka', 'año': 2023}]

 
    context = {
            'listado_vehiculos': vehiculos
            
        }

    

    model= Vehiculo
    template_name='core/vehiculos_listado.html'
    context_object_name = 'listado_vehiculos'
    success_url='vehiculos'
       
   
"""