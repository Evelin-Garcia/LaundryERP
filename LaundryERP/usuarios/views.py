from django.shortcuts import render, redirect
from .forms import ClienteForm, EmpleadoForm, LoginForm
from .models import Empleado, Cliente
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages


# Create your views here.
def login_empleado(request):
    form = LoginForm(data=request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        usuario = authenticate(username=username, password=password)
        
        if usuario is not None:
            login(request, usuario)
            messages.success(request, 'Inicio de Sesión exitoso')
            return redirect('index')  
        else:
            # Agregar mensaje de error si las credenciales no son válidas.
            form.add_error(None, "Usuario o contraseña incorrectos.")
    
    return render(request, 'usuarios/login.html', {'form': form})

def logout_empleado(request):
    logout(request)
    messages.success(request, 'Sesion cerrada con éxito')
    return redirect('usuarios:login')  

def is_admin(usuario):
    try:
        return hasattr(usuario, 'empleado') and usuario.empleado.rol == 'admin'
    except Empleado.DoesNotExist:
        return False  # Si no tiene un empleado asociado, no es administrador

@login_required
@user_passes_test(is_admin, login_url='/error')

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'usuarios/lista_empleados.html', {'empleados': empleados})


@login_required # solicita que el usuario este logeado
@user_passes_test(is_admin, login_url='/error')

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            # Guardamos el empleado (esto también guarda al usuario)
            form.save()
            return redirect('usuarios:lista_empleados')  
    else:
        form = EmpleadoForm()

    return render(request, 'usuarios/crear_empleado.html', {'form': form})


@login_required
@user_passes_test(is_admin, login_url='/error')
def index_cliente(request):
    if request.method == 'POST':
        form_cliente = ClienteForm(request.POST)
        if form_cliente.is_valid():
            form_cliente.save()
            return redirect('index')
    else:
        form_cliente = ClienteForm()
    return render(request, 'usuarios/registro_clientes.html', {'form': form_cliente})


@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()  # Obtiene todos los clientes
    return render(request, 'usuarios/lista_clientes.html', {'clientes': clientes})


