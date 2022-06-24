from django.shortcuts import render

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

def user001(request):
    return render(request, 'core/user001.html')

def terminosCondiciones(request):
    return render(request, 'core/terminos_condiciones')

def encuentraMascota(request):
    return render(request, 'core/encuentramascota.html')

def crearCuenta(request):
    return render(request, 'registration/crearcuenta.html')

def iniciarSesion(request):
    return render(request, 'registration/iniciosesion.html')

