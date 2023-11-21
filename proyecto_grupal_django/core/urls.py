from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from .views import ReportesView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    
    path('nosotros/', views.nosotros , name='nosotros'),
    path('usuarios/<str:usuario>', views.nombre_usuario, name='nombre_usuario'),
    path('vehiculos/', views.vehiculos_todos, name='vehiculos_todos'),

    path('vehiculos/registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    re_path('vehiculos/anio/(?P<anio>[0-9]{4})/$', views.vehiculos_anio, name='vehiculos_anio'),
    path('vehiculos/disponibles', views.vehiculos_estado, {'estado': 'disponible'}, name="vehiculos_disponible"),
    path('vehiculos/vendidos', views.vehiculos_estado, {'estado': 'vendido'}, name="vehiculos_vendido"),
    path('vehiculos/ficha/', views.oferta_dia, name='ficha_vehiculo'),
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
    path('vehiculos/alta_transaccion', views.TransaccionCreateView.as_view(), name="alta_transaccion"),
    path('vehiculos/comprar_vehiculo/<int:vehiculo_id>/', views.comprar_vehiculo, name='comprar_vehiculo'),
    path('vehiculos/ventas_listado', views.VentasListView.as_view(), name="ventas_listado"),
    path('vehiculos/reportes',ReportesView.as_view() , name="reportes"),
    path('vehiculos/0km',views.auto_Okm , name="0km"),
    path('vehiculos/usados',views.usados , name="usados"),
    
    ] 