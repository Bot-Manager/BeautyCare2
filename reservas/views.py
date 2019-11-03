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