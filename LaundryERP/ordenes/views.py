from django.shortcuts import render, get_object_or_404, redirect
from .models import OrdenDeServicio, OrdenPrenda
from .forms import OrdenDeServicioForm, OrdenPrendaForm
from django.contrib import messages
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required, user_passes_test


# Listar órdenes
@login_required
def listar_ordenes(request):
    ordenes = OrdenDeServicio.objects.all()
    return render(request, 'ordenes/listar_ordenes.html', {'ordenes': ordenes})

# Crear una nueva orden
@login_required
def crear_orden(request):
    OrdenPrendaFormSet = modelformset_factory(OrdenPrenda, form=OrdenPrendaForm, extra=1, can_delete=True)
    
    if request.method == 'POST':
        form = OrdenDeServicioForm(request.POST)
        formset = OrdenPrendaFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            try:
                # Guarda la orden de servicio
                orden = form.save()
                prendas_validas = 0
                
                # Guarda las prendas asociadas
                for form in formset:
                    if form.cleaned_data:  # Verifica que no sea un formulario vacío
                        prenda = form.save(commit=False)
                        prenda.orden = orden
                        prenda.save()
                        prendas_validas += 1
                
                if prendas_validas > 0:
                    messages.success(request, 'Orden creada exitosamente.')
                else:
                    messages.warning(request, 'La orden fue creada, pero no se asociaron prendas.')
                
                return redirect('ordenes:listar_ordenes')
            except Exception as e:
                messages.error(request, f"Error al guardar la orden: {e}")
        else:
            print("Errores en el formulario principal:", form.errors)
            print("Errores en el formset:", [f.errors for f in formset])
            messages.error(request, 'Por favor, corrige los errores en los formularios.')
    
    else:
        form = OrdenDeServicioForm()
        formset = OrdenPrendaFormSet(queryset=OrdenPrenda.objects.none())
    
    return render(request, 'ordenes/crear_orden.html', {'form': form, 'formset': formset})

# Detalle de una orden
def detalle_orden(request, pk):
    orden = get_object_or_404(OrdenDeServicio, pk=pk)
    prendas = orden.ordenprenda_set.all()
    return render(request, 'ordenes/detalle_orden.html', {'orden': orden, 'prendas': prendas})


def actualizar_orden(request, pk):
    orden = get_object_or_404(OrdenDeServicio, pk=pk)
    prendas = OrdenPrenda.objects.filter(orden=orden)
    if request.method == 'POST':
        form = OrdenDeServicioForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            messages.success(request, f"La orden {orden.pk} se actualizó exitosamente.")
            return redirect('ordenes:listar_ordenes')
        else:
            messages.error(request, "Hubo un problema al actualizar la orden. Revisa los datos ingresados.")
    else:
        form = OrdenDeServicioForm(instance=orden)
    
    context={
       'form': form, 
       'orden': orden,
       'prendas': prendas,
    }
    
    return render(request, 'ordenes/actualizar_orden.html', context)


# Eliminar una orden
def eliminar_orden(request, pk):
    orden = get_object_or_404(OrdenDeServicio, pk=pk)
    if request.method == 'POST':
        orden.delete()
        messages.success(request, "La Orden ha sido eliminada exitosamente.")
        return redirect('ordenes:listar_ordenes')
    return render(request, 'ordenes/eliminar_orden.html', {'orden': orden})

