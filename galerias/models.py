from django.db import models

# Create your models here.


class Galerias(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=50)
    imagen = models.ImageField(upload_to='galerias/')