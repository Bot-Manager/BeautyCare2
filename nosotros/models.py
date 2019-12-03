from django.db import models

# Create your models here.

class Nosotros(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()

    class Meta:
        verbose_name = 'nosotros'
        verbose_name_plural = 'nosotros'

    def __str__(self):
        return self.titulo



class Pasion(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()

    class Meta:
        verbose_name = 'pasion'
        verbose_name_plural = 'pasion'

    def __str__(self):
        return self.titulo



class Profesional(models.Model):
    nombre = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='profesional/')

    
    class Meta:
        verbose_name = 'profesional'
        verbose_name_plural = 'profesional'

    def __str__(self):
        return self.nombre