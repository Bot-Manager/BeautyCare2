from django.db import models


# Create your models here.

class Galerias(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=50)
    imagen = models.ImageField(upload_to='galerias/')
    categoria = models.ForeignKey('Categoria' , on_delete=models.SET_NULL , null=True)

    class Meta:
        verbose_name = 'galeria'
        verbose_name_plural = 'galerias'

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=25)


    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre