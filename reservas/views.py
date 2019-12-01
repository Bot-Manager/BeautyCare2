from .models import Reservas
from django.shortcuts import render
from .forms import ReservaServicioForm

from reservas.models import Reservas
# Create your views here.

def reserva_servicio(request):
    reserva_form = ReservaServicioForm(request.POST)

    if request.method == 'POST' :

        if reserva_form.is_valid():
            reserva_form.save()
    context = {'form' : reserva_form}

    return render(request , 'Reservas/reservas.html' , context)

def lista_reserva(request):
    lista_reserva = Reservas.objects.all()

    context = {
        'lista_reserva' : lista_reserva ,
        }

    return render(request , 'Reservas/lista_reservas.html' , context)