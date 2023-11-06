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
    path('vehiculos/alta_comprador', views.CompradorCreateView.as_view(), name="alta_comprador"),
    #path('vehiculos/', views.VehiculosListView.as_view(), name='vehiculos_todos'),
    path('vehiculos/vendedores_listado', views.VendedorListView.as_view(), name="vendedores_listado"),
    path('vehiculos/compradores_listado', views.CompradorListView.as_view(), name="compradores_listado"),
    path('vendedor/delete/<int:pk>', views.VendedorDeleteView.as_view(), name='vendedor_eliminar'),
    path('comprador/delete/<int:pk>', views.CompradorDeleteView.as_view(), name='comprador_eliminar'),
    path('vendedor/update/<int:pk>', views.VendedorUpdateView.as_view(), name='vendedor_actualizar'),
    path('comprador/update/<int:pk>', views.CompradorUpdateView.as_view(), name='comprador_actualizar'),
    path('vehiculos/alta_auto/', views.VehiculoCreateView.as_view(), name="alta_auto"),
    path('vehiculos/alta_auto/vehiculos', views.VehiculosListView.as_view(), name="vehiculos_listado"),
    path('vehiculos/delete/<int:pk>', views.VehiculoDeleteView.as_view(), name='vehiculo_eliminar'),
    path('vehiculos/updatev/<int:pk>', views.VehiculoUpdateView.as_view(), name='vehiculo_update'),
    
    ]