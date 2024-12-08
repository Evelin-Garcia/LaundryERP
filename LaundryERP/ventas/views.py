from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Venta
from .forms import VentaForm
from ordenes.models import OrdenDeServicio
from django.contrib.auth.decorators import login_required, user_passes_test


# Listar todas las ventas
@login_required
def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/listar_ventas.html', {'ventas': ventas})


# Registrar una nueva venta
def registrar_ventas(request, orden_id=None):
    orden = None
    if orden_id:
        orden = get_object_or_404(OrdenDeServicio, id=orden_id)

        # Verificar si la orden ya tiene una venta registrada
        if Venta.objects.filter(orden_servicio=orden).exists():
            messages.error(request, "Esta orden ya tiene una venta registrada.")
            return redirect('ordenes:listar_ordenes')

    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            if orden:
                venta.orden_servicio = orden
                venta.monto_total = orden.calcular_total()
            venta.save()
            messages.success(request, 'Venta registrada exitosamente.')
            return redirect('ventas:listar_ventas')
    else:
        form = VentaForm(initial={'orden_servicio': orden} if orden else None)

    return render(request, 'ventas/registrar_ventas.html', {'form': form, 'orden': orden})

# Ver detalles de una venta
def detalle_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    return render(request, 'ventas/detalle_venta.html', {'venta': venta})

# Actualizar una venta existente
def actualizar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venta actualizada exitosamente.')
            return redirect('ventas:listar_ventas')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'ventas/actualizar_venta.html', {'form': form, 'venta': venta})

# Eliminar una venta
def eliminar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        venta.delete()
        messages.success(request, 'Venta eliminada exitosamente.')
        return redirect('ventas:listar_ventas')
    return render(request, 'ventas/eliminar_venta.html', {'venta': venta})

def agregar_venta_desde_orden(request, orden_id):
    # Obtener la orden de servicio
    orden = get_object_or_404(OrdenDeServicio, id=orden_id)

    if orden.estatus != "Completada":
        messages.error(request, "Solo las órdenes completadas pueden registrarse como ventas.")
        return redirect('ordenes:listar_ordenes')

    # Redirigir al formulario de registro de ventas
    return redirect('ventas:registrar_ventas_desde_orden', orden_id=orden.id)
