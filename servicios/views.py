from django.shortcuts import render

# Create your views here.
from .models import Servicios


def lista_servicio(request):
    lista_servicio = Servicios.objects.all()

    context = {'lista_servicio' : lista_servicio ,}

    return render(request , 'Servicios/lista.html' , context)


def detalle_servicio(request , slug):
    detalle_servicio = Servicios.objects.get(slug=slug)

    context = {'detalle_servicio' : detalle_servicio}

    return render(request , 'Servicios/detalle.html' , context)