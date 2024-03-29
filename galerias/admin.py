from django.contrib import admin

# Register your models here.

from .models import Galerias , Categoria

class Lista(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'imagen','categoria']
    search_fields = ['nombre', 'categoria']
    list_filter = ('nombre', 'categoria')




class Lista(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'imagen', 'categoria' ]
    search_fields = ['nombre']
    list_filter = ['categoria']

admin.site.register(Galerias,Lista)
admin.site.register(Categoria)