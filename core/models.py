from django.db import models

# Create your models here.

class registroUsuarios(models.Model):
    nickname = models.CharField(max_length=16, verbose_name="usuario")
    nombre = models.CharField(max_length=16, verbose_name="nombre del usuario")
    apellidoPaterno = models.CharField(max_length=16, verbose_name="apellido paterno del ususario")
    apellidoMaterno = models.CharField(max_length=16, verbose_name="apellido materno del usuario")
    contrasena = models.CharField(max_length=12, verbose_name="contraseña del usuario")
    correo = models.CharField(max_length=40, verbose_name="correo del usuario")
    telefono = models.IntegerField(verbose_name="telefono del usuario")
    nombreMascota = models.CharField(max_length=16, verbose_name="nombre de la mascota")
    edadMascota = models.IntegerField(verbose_name="edad de la mascota")

    def __str__(self):
        return self.nickname

