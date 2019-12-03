from django.shortcuts import render
from .models import Nosotros , Pasion , Profesional

# Create your views here.
def nosotros_lista(request):
    nosotros = Nosotros.objects.last()
    pasion = Pasion.objects.all()
    profesional = Profesional.objects.all()

    context = {
        'nosotros' : nosotros ,
        'pasion' : pasion ,
        'profesional' : profesional

    }

    return render(request , 'Nosotros/nosotros.html' , context)