from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.urls import reverse
from datetime import datetime
from .forms import  NuevoAuto
from .models import Vendedor, Vehiculo, Comprador, Transaccion
from .forms import AltaVendedorModelForm, AltaCompradoModelForm, AltaVehiculoModelForm, AltatransaccionModelForm
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
#from django.views.generic.list import ListView
from django.urls import reverse_lazy
from datetime import datetime
from django.db.models import Count



# Create your views here.
def mi_Vista(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request,user)
        #redireccionar pagina éxito
    else:
        return {f'Login Inváildo'}
        pass

# def logout_view(request):
#     logout(request)
#     #redireccionar a pagina éxito

def index(request):
    #if request.method == "GET":
        return render(request, "core/index.html")


# @permission_required('cac.puede_ver_lista',login_url='./core/login.html')




def nosotros(request):
    return render(request,'core/nosotros.html')

                
def nombre_usuario(request,usuario):
    return HttpResponse(
       f"""<h1>Bienvenido: {usuario}!</h1>"""
    )

def registro_exitoso(request):
    return render(request, 'core/registro_exitoso.html')

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
    vehiculos_filtrados = Vehiculo.objects.filter(anio=int(anio))
    

    context = {
        'vehiculos_filtrados': vehiculos_filtrados,
        'anio_parametro': anio,
        
    }

    return render(request, 'core/vehiculos_año.html', context)
    
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
    permission_required = ""
    model = Vendedor
    form_class = AltaVendedorModelForm
    template_name='core/alta_vendedor.html'
    success_url='registro_exitoso'
    
    #fields = '__all__'

class VendedorUpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = 'core.change_vendedor'
    model = Vendedor
    template_name='core/vendedor_update.html'
    form_class = AltaVendedorModelForm
    success_url = reverse_lazy('vendedores_listado')


    
class VendedorListView(PermissionRequiredMixin, ListView):
    permission_required = 'core.view_vendedor'
    model = Vendedor
    context_object_name = 'listado_vendedor'
    template_name='core/vendedor_listado.html'
    #queryset= Vendedor.objects.filter(tipo_vendedor= "Persona")
    
class VendedorDeleteView(PermissionRequiredMixin,DeleteView):
    permission_required =  'core.delete_vendedor'
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
    permission_required = 'core.add_comprador'
    model = Comprador
    form_class = AltaCompradoModelForm
    template_name='core/alta_Comprador.html'
    success_url='registro_exitoso'

class CompradorUpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = 'core.change_comprador'
    model = Comprador
    template_name='core/comprador_update.html'
    form_class = AltaCompradoModelForm
    success_url = reverse_lazy('compradores_listado')


class CompradorListView(PermissionRequiredMixin, ListView):
    permission_required = 'core.view_comprador'
    model = Comprador
    context_object_name = 'listado_comprador'
    template_name='core/comprador_listado.html'
    #queryset= Vendedor.objects.filter(tipo_vendedor= "Persona")

    
class CompradorDeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = 'core.delete_comprador'
    model = Comprador
    #el nombre de la plantilla es por defecto de django
    template_name = 'core/comprador_confirm_delete.html' 
    success_url = reverse_lazy('compradores_listado')

#-------------------------------VEHICULOS-------------------------
class VehiculoCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'core.add_vehiculo'
    model = Vehiculo
    form_class = AltaVehiculoModelForm
    template_name='core/alta_auto.html'
    success_url='vehiculos'

class VehiculosListView(ListView):
    model = Vehiculo
    context_object_name = 'vehiculos_listado'
    template_name='core/vehiculos_listado.html'
   
    

class VehiculoDeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = 'core.delete_vehiculo'
    model = Vehiculo
    #el nombre de la plantilla es por defecto de django
    template_name = 'core/vehiculo_confirm_delete.html' 
    success_url = reverse_lazy('vehiculos_listado')

class VehiculoUpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = 'core.change_vehiculo'
    model = Vehiculo
    fields = [ 
        "anio", 
        "tipo",
        "precio",
        "descripcion",
        "vendedor",
    ] 
    template_name = 'core/vehiculo_update.html' 
    success_url = reverse_lazy('vehiculos_listado')
#-------------------------------REGISTRAR LA TRANSACCION-------------------------

class TransaccionCreateView(CreateView):
    model = Transaccion
    form_class = AltatransaccionModelForm
    template_name='core/alta_transaccion.html'
    success_url = reverse_lazy('ventas_listado')

#------------otra opcion de regitrar transaccion-------------


def comprar_vehiculo(request, vehiculo_id):
    # Obtén el vehículo y el comprador que deseas precargar
    vehiculo = Vehiculo.objects.get(pk=vehiculo_id)
    comprador = Comprador.objects.get(pk=1)  # Reemplaza con el ID del comprador deseado
    precio_vehiculo = vehiculo.precio
    metodo_pago='efectivo'
    estado_transaccion='Completada'
    

    if request.method == "POST":
        form = AltatransaccionModelForm(request.POST)
        if form.is_valid():
            # Crea la instancia de la transacción y guarda los datos
            transaccion = Transaccion(
                vendedor=vehiculo.vendedor,
                comprador=comprador,
                vehiculo=vehiculo,
                precio_transaccion=precio_vehiculo,
                metodo_pago=metodo_pago,
                estado_transaccion=estado_transaccion,
                observaciones='123op'
            )
            transaccion.save()
            return redirect('ventas_listado')  # Redirige a la lista de vehículos u otra página

    else:
        initial_data = {
            'vendedor': vehiculo.vendedor,
            'comprador': comprador,
            'vehiculo': vehiculo,
             'precio_transaccion':precio_vehiculo,
             'metodo_pago':metodo_pago,
             'estado_transaccion':estado_transaccion
             
        }
        form = AltatransaccionModelForm(initial=initial_data)

    context = {
        'form': form,
        'vehiculo': vehiculo,
        'comprador': comprador,
    }

    return render(request, 'core/alta_transaccion.html', context)

class VentasListView(PermissionRequiredMixin,ListView):
    permission_required = 'core.view_transaccion'
    model = Transaccion
    context_object_name = 'listado_ventas'
    template_name='core/ventas_listado.html'
    
#------------------------Reportes----------------------------------------
class ReportesView(PermissionRequiredMixin,View):
    permission_required = 'core.view_reporte'
    template_name = 'core/reportes.html'
    

    def get(self, request, *args, **kwargs):
        # Lógica para obtener los datos necesarios para los gráficos
        cantidad_vehiculos_0KM = Vehiculo.objects.filter(tipo='0KM').count()
        cantidad_vehiculos_usado = Vehiculo.objects.filter(tipo='Usado').count()
        transacciones_septiembre = Transaccion.objects.filter(
            fecha_transaccion__month=9,
            fecha_transaccion__year=datetime.now().year
        ).count()
        transacciones_octubre = Transaccion.objects.filter(
            fecha_transaccion__month=10,
            fecha_transaccion__year=datetime.now().year
        ).count()
        transacciones_noviembre = Transaccion.objects.filter(
            fecha_transaccion__month=11,
            fecha_transaccion__year=datetime.now().year
        ).count()
        transacciones_diciembre = Transaccion.objects.filter(
            fecha_transaccion__month=12,
            fecha_transaccion__year=datetime.now().year
        ).count()
        financiamientos_plazos = Vendedor.objects.filter(financiamiento_ofrecido='Financiamiento a Plazos').count()
        financiamientos_leasing = Vendedor.objects.filter(financiamiento_ofrecido='Leasing').count()
        financiamientos_contado = Vendedor.objects.filter(financiamiento_ofrecido='Pago al Contado').count()
        
        vendedores_mas_transacciones = Vendedor.objects.annotate(num_transacciones=Count('transaccion')).order_by('-num_transacciones')[:3]

        
        #cantidad_vehiculos_por_tipo = Vehiculo.objects.values('tipo')
        #cantidad_vendedores = Vendedor.objects.count()
        #cantidad_compradores = Comprador.objects.count()

        # Pasar los datos al contexto
        context = {
            'cantidad_vehiculos_0KM': cantidad_vehiculos_0KM ,
            'cantidad_vehiculos_usado': cantidad_vehiculos_usado,
            'transacciones_septiembre': transacciones_septiembre,
            'transacciones_octubre': transacciones_octubre,
            'transacciones_noviembre': transacciones_noviembre,
            'transacciones_diciembre': transacciones_diciembre,
            'financiamientos_plazos': financiamientos_plazos,
            'financiamientos_leasing': financiamientos_leasing,
            'financiamientos_contado': financiamientos_contado,
            'vendedores_mas_transacciones': vendedores_mas_transacciones,
            #'cantidad_vendedores': cantidad_vendedores,
            #'cantidad_compradores': cantidad_compradores,
            # Puedes agregar más datos según sea necesario
        }

        return render(request, self.template_name, context)
    
    
def oferta_dia(request):
   
    

    # Recupera el vehículo de la base de datos
    vehiculo_oferta = Vehiculo.objects.all().order_by('precio').first()
   
    context = {
        'vehiculo_oferta': vehiculo_oferta,
    }
    print(context)
    return render(request, 'core/oferta_del_dia.html', context)

def auto_Okm(request):
    vehiculos_0km= Vehiculo.objects.filter(tipo='0KM')
    context = {
        'vehiculos_0km': vehiculos_0km,
    }
    
    return render(request, 'core/0km.html', context)

def usados(request):
    vehiculos_usados= Vehiculo.objects.filter(tipo='Usado')
    context = {
        'vehiculos_usados': vehiculos_usados,
    }
    
    return render(request, 'core/usados.html', context)