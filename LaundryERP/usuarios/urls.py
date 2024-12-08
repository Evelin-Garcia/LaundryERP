from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('emp/', views.lista_empleados, name='lista_empleados'),
    path('cli/', views.index_cliente, name='index_cliente'),
    path('lista/', views.lista_clientes, name='lista_clientes'),
    path('crear/', views.crear_empleado, name='crear_empleado'),
    path('cerrar_sesion/', views.logout_empleado, name='cerrar_sesion'),
    path('inicio_sesion/', views.login_empleado, name='login'),
]