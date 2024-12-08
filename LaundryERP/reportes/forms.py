from django import forms
from django.forms import DateInput
from usuarios.models import Cliente, Empleado
from ordenes.models import Prenda

class FiltroReporteForm(forms.Form):
    fecha_inicio = forms.DateField(widget=DateInput(attrs={'type': 'date'}), required=False)
    fecha_fin = forms.DateField(widget=DateInput(attrs={'type': 'date'}), required=False)
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=False, empty_label='Seleccionar Cliente')
    empleado = forms.ModelChoiceField(queryset=Empleado.objects.select_related('usuario').all(), required=False, empty_label='Seleccionar Empleado')
    prenda = forms.ModelChoiceField(queryset=Prenda.objects.all(),required=False,empty_label='Seleccionar Tipo de Prenda')      
    
class FiltroHistorialClienteForm(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=True, empty_label='Seleccionar Cliente')