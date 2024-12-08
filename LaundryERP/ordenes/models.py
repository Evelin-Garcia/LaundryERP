from django.db import models
from usuarios.models import Cliente, Empleado

# Create your models here. Definimos las órdenes, prendas y su relación.

class Prenda(models.Model):
    tipo_prenda =models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.tipo_prenda

class OrdenDeServicio(models.Model):
    
    ESTATUS = [ 
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Completada', 'Completada'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, limit_choices_to={'rol':'empleado'})
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estatus = models.CharField(max_length=20, choices=ESTATUS)
    prendas = models.ManyToManyField(Prenda, through='OrdenPrenda')
    
    def __str__(self):
        return f"Orden #{self.id} - {self.cliente.nombre}"
    
    def calcular_total(self): #Método para calcular el total de la orden basado en las prendas y su cantidad.
        total = sum(orden_prenda.prenda.precio * orden_prenda.cantidad for orden_prenda in self.ordenprenda_set.all())
        return total    

class OrdenPrenda(models.Model):
    orden = models.ForeignKey(OrdenDeServicio, on_delete=models.CASCADE)
    prenda = models.ForeignKey(Prenda, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.cantidad} x {self.prenda.tipo_prenda} (Orden n°{self.orden.id})'