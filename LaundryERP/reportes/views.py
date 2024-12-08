from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone
from ventas.models import Venta
from ordenes.models import OrdenDeServicio
from usuarios.models import Cliente
from .forms import FiltroReporteForm, FiltroHistorialClienteForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test



# Create your views here.
# Vista principal de reportes
@login_required
def index(request):
    return render(request, 'reportes/index.html')

#Reporte de ventas: filtra por fecha y cliente:

def reporte_ventas(request):
    # Valores predeterminados
    fecha_inicio = timezone.now().replace(year=timezone.now().year, month=1, day=1)
    fecha_fin = timezone.now()

    ventas = Venta.objects.select_related(
        'orden_servicio__cliente',
        'orden_servicio__empleado__usuario'
    ).prefetch_related('orden_servicio__prendas')

    # Procesar formulario
    form = FiltroReporteForm(request.GET or None)
    if form.is_valid():
        # Obtener datos del formulario
        fecha_inicio = form.cleaned_data.get('fecha_inicio') or fecha_inicio
        fecha_fin = form.cleaned_data.get('fecha_fin') or fecha_fin
        cliente = form.cleaned_data.get('cliente')
        empleado = form.cleaned_data.get('empleado')
        prenda = form.cleaned_data.get('prenda')

        # Aplicar filtros
        ventas = ventas.filter(fecha_venta__range=[fecha_inicio, fecha_fin])
        if cliente:
            ventas = ventas.filter(orden_servicio__cliente=cliente)
        if empleado:
            ventas = ventas.filter(orden_servicio__empleado=empleado)
        if prenda:
            ventas = ventas.filter(orden_servicio__prendas=prenda)

    # Calcular total
    total_ventas = ventas.aggregate(Sum('monto_total'))['monto_total__sum'] or 0

    # Mensaje para cuando no hay resultados
    mensaje = "No se encontraron ventas para los filtros seleccionados." if not ventas.exists() else None

    context = {
        'form': form,
        'ventas': ventas,
        'total_ventas': total_ventas,
        'mensaje': mensaje,
    }
    return render(request, 'reportes/reporte_ventas.html', context)



#Vista para el historial de ventas del cliente:
def historial_ventas_cliente(request):
    form = FiltroHistorialClienteForm(request.GET)
    ventas_cliente = None

    if 'cliente' in request.GET and request.GET['cliente']:
        try:
            cliente = Cliente.objects.get(id=request.GET['cliente'])
            
            # Filtrar las órdenes de servicio del cliente
            ordenes_cliente = OrdenDeServicio.objects.filter(cliente=cliente)
            # Filtrar las ventas relacionadas con esas órdenes
            ventas_cliente = Venta.objects.filter(orden_servicio__in=ordenes_cliente)
            
            # Verificar si hay alguna orden pendiente o en proceso
            ordenes_no_completadas = ordenes_cliente.filter(estatus__in=["Pendiente", "En Proceso"])
            
            if ordenes_no_completadas.exists():
                ordenes_no_completadas_list = ", ".join([str(orden.id) for orden in ordenes_no_completadas])
                messages.warning(
                    request, 
                    f"La(s) orden(es) de servicio n°: {ordenes_no_completadas_list}, asociada(s) a {cliente.nombre} aún no está(n) finalizada(s)."
                )
            else:
                messages.info(request, f"El cliente {cliente.nombre} tiene todas las órdenes completadas.")
                
        except Cliente.DoesNotExist:
            messages.error(request, "El cliente seleccionado no existe.")

    context = {
        'form': form,
        'ventas_cliente': ventas_cliente,
    }
    
    return render(request, 'reportes/historial_ventas_cliente.html', context)