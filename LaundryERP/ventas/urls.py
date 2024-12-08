from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [

    path('listar/', views.listar_ventas, name='listar_ventas'),
    path('registrar/', views.registrar_ventas, name='registrar_ventas'),
    path('registrar/<int:orden_id>/', views.registrar_ventas, name='registrar_ventas_desde_orden'),
    path('detalle/<int:id>/', views.detalle_venta, name='detalle_venta'),
    path('actualizar/<int:id>/', views.actualizar_venta, name='actualizar_venta'),
    path('eliminar/<int:id>/', views.eliminar_venta, name='eliminar_venta'),
    path('agregar-desde-orden/<int:orden_id>/', views.agregar_venta_desde_orden, name='agregar_venta_desde_orden'),
]
