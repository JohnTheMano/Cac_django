from django.contrib import admin

# Register your models here.
from core.models import Vehiculo, Vendedor, Comprador, Transaccion, Reporte

# Register your models here.
admin.site.register(Vehiculo)
admin.site.register(Vendedor)
admin.site.register(Comprador)
admin.site.register(Transaccion)
admin.site.register(Reporte)
