from django.contrib import admin
from .models import Empleado, Cliente

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rol')
    search_fields = ('usuario__username','rol', 'usuario__email')
    list_filter = ('rol',)
    list_per_page = 10
    
    def get_nombre(self, obj):
        return f"{obj.usuario.first_name} {obj.usuario.last_name}"
    get_nombre.short_description = 'Nombre'

    def get_correo(self, obj):
        return obj.usuario.email
    get_correo.short_description = 'Correo'

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'correo', 'direccion')
    search_fields = ('nombre', 'telefono', 'correo')
    list_filter = ('direccion',)
    list_per_page = 10

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Cliente, ClienteAdmin)

