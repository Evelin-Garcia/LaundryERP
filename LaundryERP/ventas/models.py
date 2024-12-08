from django.db import models
from ordenes.models import OrdenDeServicio

# Create your models here. Para las ventas y los métodos de pago.
class Venta(models.Model):
    orden_servicio = models.OneToOneField(OrdenDeServicio, on_delete=models.CASCADE, unique=True, related_name='venta')
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=20, choices=[ 
        ('efectivo', 'Efectivo'), 
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
        ])
    pago_realizado = models.BooleanField(default=False)  # Este campo indica si se realizó el pago
    
    def save(self, *args, **kwargs):
        # Calcular el monto total de la venta basado en la orden
        self.monto_total = self.orden_servicio.calcular_total()
        
        # Si el pago se ha realizado, cambiar el estatus de la orden a 'finalizado'
        if self.pago_realizado:
            self.orden_servicio.estatus = 'Completada'
            self.orden_servicio.save()

        # Guardar la venta después de haber realizado los cambios
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'Venta n° {self.id} - Total: ${self.monto_total}'
