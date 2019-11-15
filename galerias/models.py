from django.db import models
from django.utils.text import slugify
# Create your models here.


class Galerias(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=50)
    imagen = models.ImageField(upload_to='galerias/')
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null=True)



    class Meta:
        verbose_name = 'galeria'
        verbose_name_plural = 'galerias'

    def __str__(self):
        return self.nombre


class Category(models.Model):
    name = models.CharField(max_length=30)

    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name