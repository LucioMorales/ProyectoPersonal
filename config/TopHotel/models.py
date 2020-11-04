from django.db import models

# Create your models here.

class Huesped(models.Model):
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    dni = models.IntegerField()
    telefono = models.IntegerField()

    def __str__(self):
        return "{}".format(self.nombre)

class Habitacion(models.Model):
    numero = models.IntegerField()
    piso = models.IntegerField()

    def __str__(self):
        return "{}".format(self.numero)