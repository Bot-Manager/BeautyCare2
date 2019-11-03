

from django.urls import path
from . import views


app_name = 'servicios'


urlpatterns = [
    path('', views.lista_servicio , name='lista_servicio'),
    path('<slug:slug>' , views.detalle_servicio , name='detalle_servicio')
]
