from django.contrib import admin
from .models import Prenda, OrdenDeServicio, OrdenPrenda

class PrendaAdmin(admin.ModelAdmin):
    list_display = ('tipo_prenda', 'precio', 'descripcion')
    search_fields = ('tipo_prenda',)
    list_filter = ('tipo_prenda',)

class OrdenDeServicioAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'empleado', 'fecha_creacion', 'estatus', 'calcular_total')
    search_fields = ('cliente__nombre', 'empleado__nombre', 'estatus')
    list_filter = ('estatus', 'empleado__rol')
    readonly_fields = ('fecha_creacion', 'calcular_total')  # Campos de solo lectura
    list_per_page = 10  # Paginación

    def calcular_total(self, obj):
        return obj.calcular_total()
    calcular_total.short_description = 'Total'

class OrdenPrendaAdmin(admin.ModelAdmin):
    list_display = ('orden', 'prenda', 'cantidad')
    search_fields = ('orden__id', 'prenda__tipo_prenda')

admin.site.register(Prenda, PrendaAdmin)
admin.site.register(OrdenDeServicio, OrdenDeServicioAdmin)
admin.site.register(OrdenPrenda, OrdenPrendaAdmin)

