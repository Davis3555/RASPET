from unicodedata import name
from django.urls import URLPattern, path
from .views import acercaNosotros, crearCuenta, index, acercaNosotros, comoFunciona, iniciarSesion, productos, repuestos, user001, terminosCondiciones, encuentraMascota

urlpatterns = [
    path('', index, name="index"),
    path('acerca-nosotros/', acercaNosotros, name="acerca-nosotros"),
    path('como-funciona/', comoFunciona, name="como-funciona"),
    path('productos/', productos, name="productos"),
    path('repuestos/', repuestos, name="repuestos"),
    path('user001/', user001, name="user001"),
    path('terminos-condiciones/', terminosCondiciones, name="terminos-conidiciones"),
    path('encuentra-mascota/', encuentraMascota, name="encuentra-mascota"),
    path('crear-cuenta/', crearCuenta, name="crear-cuenta"),
    path('inicia-sesion/', iniciarSesion, name="iniciar-sesion"),
]