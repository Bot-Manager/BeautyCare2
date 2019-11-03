from django import forms
from .models import Reservas


class ReservaServicioForm(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = '__all__'
