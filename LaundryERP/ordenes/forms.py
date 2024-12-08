from django import forms
from .models import OrdenDeServicio, OrdenPrenda
from usuarios.models import Empleado

class OrdenDeServicioForm(forms.ModelForm):
    class Meta:
        model = OrdenDeServicio
        fields = ['cliente', 'empleado', 'estatus']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['empleado'].queryset = Empleado.objects.filter(rol='empleado', usuario__isnull=False)

class OrdenPrendaForm(forms.ModelForm):
    class Meta:
        model = OrdenPrenda
        fields = ['prenda', 'cantidad']

