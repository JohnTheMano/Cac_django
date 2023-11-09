from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from datetime import datetime
from .forms import  NuevoAuto
from .models import Vendedor, Vehiculo, Comprador, Transaccion
from .forms import AltaVendedorModelForm, AltaCompradoModelForm, AltaVehiculoModelForm, AltatransaccionModelForm
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

class VendedorUpdateView(UpdateView):
    model = Vendedor
    template_name='core/vendedor_update.html'
    form_class = AltaVendedorModelForm
    success_url = reverse_lazy('vendedores_listado')


    
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
    

""" 
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Excluye el objeto actual de la validación del campo 'dni'
        form.fields['dni'].queryset = Vendedor.objects.filter(pk=self.object.pk)
        return form
"""
    


#-------------------COMPRADOR--------------------
class CompradorCreateView(CreateView):
    model = Comprador
    form_class = AltaCompradoModelForm
    template_name='core/alta_Comprador.html'
    success_url='compradores_listado'

class CompradorUpdateView(UpdateView):
    model = Comprador
    form_class = AltaCompradoModelForm
    template_name='core/alta_Comprador.html'
    success_url = reverse_lazy('comprador_actualizar')


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

#-------------------------------VEHICULOS-------------------------
class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = AltaVehiculoModelForm
    template_name='core/alta_auto.html'
    success_url='vehiculos'

class VehiculosListView(ListView):
    model = Vehiculo
    context_object_name = 'listado_vehiculos'
    template_name='core/vehiculos_listado.html'

class VehiculoDeleteView(DeleteView):
    model = Vehiculo
    #el nombre de la plantilla es por defecto de django
    template_name = 'core/vehiculo_confirm_delete.html' 
    success_url = reverse_lazy('vehiculos_listado')

class VehiculoUpdateView(UpdateView):
    model = Vehiculo
    fields = [ 
        "anio", 
        "tipo",
        "precio",
    ] 
    template_name = 'core/vehiculo_update.html' 
    success_url = reverse_lazy('vehiculos_listado')
#-------------------------------REGISTRAR LA TRANSACCION-------------------------

class TransaccionCreateView(CreateView):
    model = Transaccion
    form_class = AltatransaccionModelForm
    template_name='core/alta_transaccion.html'
    success_url = reverse_lazy('vehiculos_listado')

#------------otra opcion de regitrar transaccion-------------
def comprar_vehiculo(request, vehiculo_id):
    # Obtén el vehículo y el comprador que deseas precargar
    vehiculo = Vehiculo.objects.get(pk=vehiculo_id)
    comprador = Comprador.objects.get(pk=1)  # Reemplaza con el ID del comprador deseado
    precio_vehiculo = vehiculo.precio
    

    if request.method == "POST":
        form = AltatransaccionModelForm(request.POST)
        if form.is_valid():
            # Crea la instancia de la transacción y guarda los datos
            transaccion = Transaccion(
                vendedor=vehiculo.vendedor,
                comprador=comprador,
                vehiculo=vehiculo,
                precio_transaccion=precio_vehiculo,
                metodo_pago='efectivo',
                estado_transaccion='Completada',
                observaciones='nada'
            )
            transaccion.save()
            return redirect('vehiculos_listado')  # Redirige a la lista de vehículos u otra página

    else:
        initial_data = {
            'vendedor': vehiculo.vendedor,
            'comprador': comprador,
            'vehiculo': vehiculo,
             'precio_transaccion':precio_vehiculo,
             'metodo_pago':'efectivo',
        }
        form = AltatransaccionModelForm(initial=initial_data)

    context = {
        'form': form,
        'vehiculo': vehiculo,
        'comprador': comprador,
    }

    return render(request, 'core/alta_transaccion.html', context)
"""
def registrar_compra(request):
    pass
    transaccion = Transaccion(
    vendedor=vendedor,
    comprador=comprador,
    vehiculo=vehiculo,
    fecha_transaccion=datetime.now(),
    precio_transaccion=formulario.cleaned_data['precio'],
    metodo_pago=formulario.cleaned_data['metodo_pago'],
    estado_transaccion='Completada',
    observaciones='observaciones',
)
    transaccion.save()
    
    """
    
"""
if request.method == "POST":
        formulario = NuevoAuto(request.POST)
        if formulario.is_valid():
            # Obtén o crea el vendedor, comprador y vehículo según sea necesario
            vendedor, _ = Vendedor.objects.get_or_create(nombre=formulario.cleaned_data['nombre_vendedor'], apellido=formulario.cleaned_data['apellido_vendedor'], dni=formulario.cleaned_data['dni_vendedor'])
            comprador, _ = Comprador.objects.get_or_create(nombre=formulario.cleaned_data['nombre_comprador'], apellido=formulario.cleaned_data['apellido_comprador'], dni=formulario.cleaned_data['dni_comprador'])
            vehiculo, _ = Vehiculo.objects.get_or_create(marca=formulario.cleaned_data['marca'], modelo=formulario.cleaned_data['modelo'], placa=formulario.cleaned_data['placa'])
            
            # Crea una nueva transacción de compra
            transaccion = Transaccion.objects.create(
                vendedor=vendedor,
                comprador=comprador,
                vehiculo=vehiculo,
                fecha_transaccion=datetime.now(),
                precio_transaccion=formulario.cleaned_data['precio'],  # Ajusta el campo del formulario correspondiente
                metodo_pago=formulario.cleaned_data['metodo_pago'],  # Ajusta el campo del formulario correspondiente
                estado_transaccion='Completada',  # Puedes ajustar el estado según sea necesario
                observaciones=formulario.cleaned_data['observaciones'],  # Ajusta el campo del formulario correspondiente
            )
            return redirect(reverse("registrar_auto"))
    else:
        formulario = NuevoAuto()

    context = {
        'venta_form': formulario
    }

    return render(request, 'core/vende_tu_auto.html', context)
"""
    
    
    
    
    
    
    
    
    
    
    
