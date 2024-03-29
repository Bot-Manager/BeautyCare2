from django.db import models
from django.utils.text import slugify
# Create your models here.


class Servicios(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    categoria = models.ForeignKey('Categoria' , on_delete=models.SET_NULL , null=True)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='servicios/')
    slug = models.SlugField(blank=True , null=True)


    def save(self , *args , **kwargs):
        if not self.slug and self.nombre:
            self.slug = slugify(self.nombre)
        super(Servicios , self).save(*args , **kwargs)


    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'




    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=25)


    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre