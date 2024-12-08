from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Empleado(models.Model):
    ROLES = [
        ('admin', 'Administrador'),
        ('empleado', 'Empleado'),
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='empleado')
    rol = models.CharField(max_length=20, choices=ROLES, default='empleado')
    
    
    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    direccion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'