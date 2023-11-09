from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ManyToManyField
from django.forms.models import ModelMultipleChoiceField
from django.http.request import HttpRequest

# Register your models here.
from core.models import Vehiculo, Vendedor, Comprador, Transaccion, Reporte


# class CacAdminSite(admin.AdminSite):
#     site_header = "Sistema de Administracion de Concesionario"
#     site_title = "sistema MAcua"
#     index_title = "administracion del Sitio"
#     empty_value_display = "vacio"


class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','anio','precio','descripcion')
    list_editable = ('anio','precio','descripcion')
    list_display_links = ['marca','modelo']
    search_fields = ['modelo']


# @sitio_admin.register(Comprador)
class CompradorAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido')

    def formfield_for_manytomany(self, db_field, request, **kwargs: Any):
        if db_field == 'vehiculo':
            kwargs["queryset"] = Vehiculo.objects.order_by('modelo')
        return super().formfield_for_manytomany(db_field, request, **kwargs)


# Register your models here.
# sitio_admin = CacAdminSite(name = 'cacadmin')
# sitio_admin.register(Vehiculo,VehiculoAdmin)
# sitio_admin.register(Vendedor)
# sitio_admin.register(Comprador,CompradorAdmin)
# sitio_admin.register(Transaccion)
# sitio_admin.register(Reporte)

admin.site.register(Vehiculo,VehiculoAdmin)
admin.site.register(Vendedor)
admin.site.register(Comprador,CompradorAdmin)
admin.site.register(Transaccion)
admin.site.register(Reporte)
