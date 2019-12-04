from django.contrib import admin

# Register your models here.
from .models import Reservas


class Lista(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'telefono','fecha', 'hora', 'servicio']
    search_fields = ['nombre', 'email', 'telefono']
    list_filter = ('fecha', 'servicio')



admin.site.register(Reservas, Lista)