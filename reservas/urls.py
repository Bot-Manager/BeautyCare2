
from django.urls import path
from . import views


app_name = 'reservas'


urlpatterns = [
    path('', views.reserva_servicio , name='reserva_servicio'),
    path('listaReservas/', views.lista_reserva , name='lista_reserva')
]
