from django.contrib import admin

# Register your models here.

from .models import Galerias , Categoria


admin.site.register(Galerias)
admin.site.register(Categoria)