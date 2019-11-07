from django.db import models
from servicios.models import Servicios


# Create your models here.

class Reservas(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    servicio = models.ForeignKey(Servicios , on_delete=models.SET_NULL , null=True)


    def __str__(self):
        return self.nombre
    