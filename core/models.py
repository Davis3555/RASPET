
from tkinter import CASCADE
from django.db import models


# Create your models here.

    

class apoderado(models.Model):
    rutApo = models.CharField(primary_key=True,max_length=15, verbose_name='Rut Apoderado')
    nombreApo =models.CharField(max_length=50, verbose_name='Nombre Apoderado')
    apellidoApo =models.CharField(max_length=50, verbose_name='Apellido Apoderado')
    telefonoAapo =models.IntegerField( verbose_name='Tefefono Apoderado')
    direccionApo =models.CharField(max_length=100, verbose_name='Direccion Apoderado')
    emailApo =models.CharField(max_length=50, verbose_name='Email Apoderado')
    def __str__(self):
        return self.nombreApo

opciones_sexo=[
    [0,"Macho"],
    [1,"Hembra"]
]

opciones_mascota=[
    [0,"Perros"],
    [1,"Gatos"],
    [2,"Aves"],
    [3,"Otros"]
]

class registroMascotas(models.Model):
    idChip = models.IntegerField(primary_key=True , verbose_name='Id del chip de tu mascota')
    nombreMascota = models.CharField(max_length=50, verbose_name='Nombre de tu mascota')
    edadMascota = models.IntegerField(verbose_name='Edad de tu mascota')
    sexo = models.IntegerField(choices=opciones_sexo)
    tipoMascota = models.IntegerField(choices=opciones_mascota)
    apoderado = models.ForeignKey(apoderado, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombreMascota