from django.db import models

# Create your models here.

opciones_mascota=[
    [0,"Perros"],
    [1,"Gatos"],
    [2,"Aves"],
    [3,"Otros"]
]

class registroMascotas(models.Model):
    idChip = models.IntegerField(primary_key=True, verbose_name='Id del chip de tu mascota')
    nombreMascota = models.CharField(max_length=50, verbose_name='Nombre de tu mascota')
    edadMascota = models.IntegerField(verbose_name='Edad de tu mascota')
    tipoMascota = models.IntegerField(choices=opciones_mascota)

    def __str__(self):
        return self.nombreMascota
    

