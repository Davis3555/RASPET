from django.urls import URLPattern, path
from .views import acercaNosotros, crearCuenta, home, index, acercaNosotros, comoFunciona, home, insertarMascota, productos, repuestos,  terminosCondiciones, encuentraMascota

urlpatterns = [
    path('', index, name="index"),
    path('acerca-nosotros/', acercaNosotros, name="acerca-nosotros"),
    path('como-funciona/', comoFunciona, name="como-funciona"),
    path('productos/', productos, name="productos"),
    path('repuestos/', repuestos, name="repuestos"),
    path('terminos-condiciones/', terminosCondiciones, name="terminos-conidiciones"),
    path('encuentra-mascota/', encuentraMascota, name="encuentra-mascota"),
    path('crear-cuenta/', crearCuenta, name="crear-cuenta"),
    path('home', home, name="home"),
    path('ingresar-mascota/', insertarMascota, name="ingresar-mascota")

    
]