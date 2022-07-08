
from django.urls import path
from rest_mascota.views import detalle_apoderado, detalle_mascota, lista_apoderado, lista_mascotas
from rest_mascota.viewslogin import login

urlpatterns = [
    path('lista-mascotas/', lista_mascotas, name="lista-mascotas"),
    path('lista-apoderados/', lista_apoderado, name="lista-apoderados"),

    path('detalle-mascotas/<id>',detalle_mascota, name="detalle-mascotas"),
    path('detalle-apoderados/<id>',detalle_apoderado, name="detalle-apoderados"),

    path('login-token',login, name="login_token"),


]
