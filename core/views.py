from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect, render
from django.http import Http404
from .models import registroMascotas
from core.forms import CustomUserCreationForm, mascotaForm


# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def acercaNosotros(request):
    return render(request, 'core/acercanosotros.html')

def comoFunciona(request):
    return render(request, 'core/comofunciona.html')

def productos(request):
    return render(request, 'core/productos.html')

def repuestos(request):
    return render(request, 'core/repuestos.html')

def terminosCondiciones(request):
    return render(request, 'core/terminos_condiciones.html')

def encuentraMascota(request):
    return render(request, 'core/encuentramascota.html')

def home(request):
    return render(request, 'core/home.html')

def crearCuenta(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user =authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password2"])
            login(request, user)
            return redirect(to=home)
        data["form"] =formulario
    return render(request, 'registration/crearcuenta.html', data)


def insertarMascota(request):
    pac=mascotaForm()  
    datos ={
        'form':pac
    }

    if request.method == 'POST':
        formulario = mascotaForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Mascota Agregada")
            return redirect(to="home")
        datos['form'] = pac

    return render(request, 'core/agregarmascota.html',datos)


