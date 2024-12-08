from django import forms
from .models import Empleado, Cliente
from django.contrib.auth.models import User


class UsuarioEmpleadoForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        
class EmpleadoForm(forms.ModelForm):
    ROLES = [
        ('admin' , 'Administrador'),
        ('empleado' , 'Empleado'),
    ]
    # Capturar datos del usuario
    usuario = forms.ModelChoiceField(queryset=User.objects.all(), required=False)  # Campo para ingresar el nombre de usuario
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    # Capturar rol del empleado
    rol = forms.ChoiceField(choices=ROLES, initial='empleado')
        
    class Meta:
        model = Empleado
        fields = ['usuario','rol']
        
    def save(self, commit=True):
        # Si no se selecciona un usuario, crear uno nuevo
        usuario = self.cleaned_data['usuario']
        
        if not usuario:
            usuario = User.objects.create_user(
                username=self.cleaned_data['email'],  # Usamos el email como username
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                email=self.cleaned_data['email'],
                password=self.cleaned_data['password'],
            )

        # Crear el empleado asociado
        empleado = Empleado.objects.create(
            usuario=usuario,
            rol=self.cleaned_data['rol']
        )

        return empleado

class ClienteForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=15)
    correo  = forms.EmailField()
    direccion = forms.CharField(max_length=500)
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'correo', 'direccion']
        
        
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
