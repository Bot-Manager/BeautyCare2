from django.contrib import admin

# Register your models here.

from .models import Servicios , Categoria



admin.site.register(Servicios)
admin.site.register(Categoria)