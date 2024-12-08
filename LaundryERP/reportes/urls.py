from django.urls import path
from . import views

app_name = 'reportes'

urlpatterns = [
    path('', views.index, name='index'),  # Página principal de reportes
    path('reporte_ventas/', views.reporte_ventas, name='reporte_ventas'),
    path('historial_ventas/', views.historial_ventas_cliente, name='historial_ventas'),
]
