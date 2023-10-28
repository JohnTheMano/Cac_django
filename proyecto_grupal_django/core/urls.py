from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros , name='nosotros'),
    path('usuarios/<str:usuario>', views.nombre_usuario, name='nombre_usuario'),
    path('vehiculos/', views.vehiculos_todos, name='vehiculos_todos'),
    
    re_path('vehiculos/anio/(?P<anio>[0-9]{4})/$', views.vehiculos_anio, name='vehiculos_anio'),
    path('vehiculos/disponibles', views.vehiculos_estado, {'estado': 'disponible'}, name="vehiculos_disponible"),
    path('vehiculos/vendidos', views.vehiculos_estado, {'estado': 'vendido'}, name="vehiculos_vendido"),
    path('vehiculos/ficha/', views.vehiculos_ficha, name='ficha_vehiculo'),
    path('vehiculos/auto/', views.registrar_venta, name='registrar_auto'),
    path('vehiculos/alta_vendedor', views.VendedorCreateView.as_view(), name="alta_vendedor"),
    #path('vehiculos/', views.VehiculosListView.as_view(), name='vehiculos_todos'),
    path('vehiculos/vendedores', views.VendedorListView.as_view(), name="vendedores_listado"),
    path('vendedor/delete/<int:pk>', views.VendedorDeleteView.as_view(), name='vendedor_eliminar'),
    
    ]