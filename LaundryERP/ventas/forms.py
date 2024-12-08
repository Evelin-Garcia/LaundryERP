from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['orden_servicio', 'monto_total', 'metodo_pago']
        widgets = {
            'orden_servicio': forms.Select(attrs={'class': 'form-select'}),
            'monto_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'metodo_pago': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'orden_servicio': 'Orden de Servicio',
            'monto_total': 'Monto Total',
            'metodo_pago': 'Método de Pago',
            
        }
