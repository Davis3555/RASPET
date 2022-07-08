from unicodedata import name
from django.urls import URLPattern, path
from .views import acercaNosotros, crearCuenta, form_apoderado, form_del_mascota, home, index, acercaNosotros, comoFunciona, home, insertarMascota, productos, repuestos,  terminosCondiciones, encuentraMascota,form_mod_mascota

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
    path('ingresar-mascota/', insertarMascota, name="ingresar-mascota"),
    path('modificar-mascota/', form_mod_mascota, name="modificar-mascota"),
    path('eliminar-mascota/', form_del_mascota, name="form-del-mascota"),
    path('agregar-apoderado/', form_apoderado, name="crear-apoderado"),
    path('eliminar-mascota/<id>', form_del_mascota, name="eliminar-mascota"),
]