from django import forms
from .models import Reservas
from servicios.models import Servicios

class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)

class TimeInput(forms.TimeInput):
    input_type = "time"

class ReservaServicioForm(forms.ModelForm):
    
    class Meta: 
        model = Reservas
        fields = 'nombre','email','telefono','fecha','hora','servicio',

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fecha"].widget = DateInput()
        self.fields["hora"].widget = TimeInput()
        

