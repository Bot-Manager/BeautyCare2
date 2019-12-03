from django.contrib import admin

# Register your models here
from .models import Nosotros , Pasion , Profesional


class Lista(admin.ModelAdmin):
    list_display = ['nombre', 'titulo' , 'descripcion', 'imagen']
    search_fields = ['nombre', 'imagen']
    list_filter = ['titulo']


class Lista_pasion(admin.ModelAdmin):
    list_display = ['titulo', 'contenido']
    search_fields = ['titulo']


admin.site.register(Nosotros)
admin.site.register(Pasion, Lista_pasion)
admin.site.register(Profesional, Lista)