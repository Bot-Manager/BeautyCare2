from django.db import models

# Create your models here.

class Reservas(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()


    def __str__(self):
        return self.nombre
    