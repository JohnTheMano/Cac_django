from django.shortcuts import render
from django.http import HttpResponse

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
     context = {
         'listado_vehiculos': [
              'Renault Sandero Stepway 2020',
              'Peugeot 208 2021',
              'volkswagen Tuareg 2021',
              'mitsubishi Colt 2023']
    }   
     return render( request ,'core/vehiculos_listado.html',context)

def vehiculos_anio(request, anio):
    return HttpResponse(
       f"""<h1>Vehículos del año: {anio}</h1>"""
    )

def vehiculos_estado(request,estado):
    return HttpResponse(
       f"""<h1>Estado del vehículo: {estado}</h1>"""
    )

def vehiculos_ficha(request):
     context = {
          'nombre_vehículo': 'Sandero Stepway',
          'marca':'Renault',
          'anio':'2020',
          'entrega_inmediata':True,
     }
     return render( request ,'core/ficha_vehiculo.html',context )