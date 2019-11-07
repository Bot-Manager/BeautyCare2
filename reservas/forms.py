from django import forms
from .models import Reservas
from servicios.models import Servicios


class ReservaServicioForm(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = '__all__'
