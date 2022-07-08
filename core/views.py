from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect, render
from django.http import Http404
from .models import registroMascotas, apoderado
from core.forms import CustomUserCreationForm, apoderadoForm, mascotaForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import permission_required

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
    queryset = request.GET.get("buscar") 
    print(queryset)
    datos=registroMascotas.objects.all()
    page = request.GET.get('page',1)
    
    try:
        paginator =Paginator(datos,3)
        datos = paginator.page(page)
    except:
        raise Http404
    
    if queryset:
        
        datos = {
            
            'mascotas':registroMascotas.objects.filter(
            Q(idChip__icontains =queryset)|
            Q(nombreMascota__icontains=queryset)
            ).distinct(),
            'paginator': paginator
        
        }
    else:
        datos = {
            'mascotas': datos,
            'paginator': paginator
        }
    return render(request, 'core/home.html',datos)

def crearCuenta(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Usuario Creado")
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
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mascota Agregada")
            return redirect(to="home")
        datos['form'] = pac

    return render(request, 'core/agregarmascota.html',datos)


def form_mod_mascota(request, id):
    pac=registroMascotas.objects.get(idChip=id)
    datos ={
        'form': mascotaForm(instance=pac)
    }
    if request.method == 'POST':
        formulario = mascotaForm(data=request.POST,instance=pac)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Mascota modificada")
            return redirect(to="home")
        datos["form"] = formulario
    return render(request, 'core/modificarmascota.html', datos)


def form_del_mascota(request, id):
     pac=registroMascotas.objects.get(idChip=id)
     pac.delete()
     messages.success(request, "Mascota Eliminada")
     return redirect(to="home")


def form_apoderado(request):
    pac=apoderadoForm()

    datos ={
        'form':pac
    }

    if request.method == 'POST':
        formulario = apoderadoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Apoderado Agregado")
            return redirect(to="home")
        datos['form'] = pac

    return render(request, 'core/crearapoderado.html',datos)