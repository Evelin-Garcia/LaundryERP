from django.contrib import admin
from .models import Venta

class VentaAdmin(admin.ModelAdmin):
    list_display = ('orden_servicio', 'monto_total', 'fecha_venta', 'metodo_pago', 'pago_realizado')
    search_fields = ('orden_servicio__id', 'metodo_pago')
    list_filter = ('metodo_pago', 'pago_realizado')
    list_per_page = 10

admin.site.register(Venta, VentaAdmin)
