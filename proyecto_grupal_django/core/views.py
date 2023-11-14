from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
# from .forms import  NuevoAuto
from .models import Vendedor, Vehiculo, Comprador, Transaccion,Reporte
from .forms import AltaVendedorModelForm, AltaCompradoModelForm, AltaVehiculoModelForm
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
#from django.views.generic.list import ListView
from django.urls import reverse_lazy



# Create your views here.
def index(request):
    #if request.method == "GET":
        return render(request, "core/index.html")

def nosotros(request):
    return render(request,'core/nosotros.html')

def reportes(request):
    return render(request,'core/reportes.html')


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
    
class VendedorDeleteView(UserPassesTestMixin, DeleteView):
    model = Vendedor
    #el nombre de la plantilla es por defecto de django
    template_name = 'core/vendedor_confirm_delete.html' 
    success_url = reverse_lazy('vendedores_listado')

    def test_func(self):
        return self.request.user.groups.filter(name='administrativos').exists()
    

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

class CompradorUpdateView(UserPassesTestMixin, UpdateView):
    model = Comprador
    template_name='core/comprador_update.html'
    form_class = AltaCompradoModelForm
    success_url = reverse_lazy('compradores_listado')

    def test_func(self):
        return self.request.user.groups.filter(name='administrativos').exists()


class CompradorListView(LoginRequiredMixin, ListView):
    model = Comprador
    context_object_name = 'listado_comprador'
    template_name='core/comprador_listado.html'
    #queryset= Vendedor.objects.filter(tipo_vendedor= "Persona")

    
class CompradorDeleteView(UserPassesTestMixin, DeleteView):
    model = Comprador
    #el nombre de la plantilla es por defecto de django
    template_name = 'core/comprador_confirm_delete.html' 
    success_url = reverse_lazy('compradores_listado')

    def test_func(self):
        return self.request.user.groups.filter(name='administrativos').exists()

#-------------------------------VEHICULOS-------------------------
class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = AltaVehiculoModelForm
    template_name='core/alta_auto.html'
    success_url='vehiculos_listado'

class VehiculoUpdateView(UpdateView):
    model = Vehiculo
    # fields = [ 
    #     "anio", 
    #     "tipo",
    #     "precio",
    #     "descripcion",
    #     "vendedor",
    # ] 
    form_class = AltaVehiculoModelForm
    template_name = 'core/vehiculo_update.html' 
    success_url = reverse_lazy('vehiculos_listado')
    

class VehiculosListView(ListView):
    model = Vehiculo
    context_object_name = 'listado_vehiculos'
    template_name='core/vehiculos_listado.html'

class VehiculoDeleteView(UserPassesTestMixin, DeleteView):
    model = Vehiculo
    #el nombre de la plantilla es por defecto de django
    template_name = 'core/vehiculo_confirm_delete.html' 
    success_url = reverse_lazy('vehiculos_listado')

    def test_func(self):
        return self.request.user.groups.filter(name='administrativos').exists()
    
    # def handle_no_permission(self):
    #     return redirect('error')
    
class ReportesListView(ListView):
    model = Reporte
    context_object_name = 'reportes'
    template_name = 'core/reportes.html'

#-------------------------------REGISTRAR LA TRANSACCION-------------------------
def registrar_compra(request):
    pass


class ErrorView(DeleteView):
    template_name = 'error.html'

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