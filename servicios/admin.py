from django.contrib import admin

# Register your models here.

from .models import Servicios , Categoria

class Lista(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion','categoria', 'precio']
    search_fields = ['nombre', 'categoria', 'precio']
    list_filter = ['nombre','categoria', 'precio']

admin.site.register(Servicios, Lista)
admin.site.register(Categoria)