from django.urls import path
from . import views

app_name = 'ordenes'

urlpatterns = [
    path('listar/', views.listar_ordenes, name='listar_ordenes'),
    path('detalle/<int:pk>/', views.detalle_orden, name='detalle_orden'), 
    path('crear/', views.crear_orden, name='crear_orden'),
    path('actualizar/<int:pk>/', views.actualizar_orden, name='actualizar_orden'),
    path('eliminar/<int:pk>/', views.eliminar_orden, name='eliminar_orden'),
]
