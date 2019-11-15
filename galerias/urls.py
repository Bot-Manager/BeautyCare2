
from django.urls import path 
from . import views

app_name = 'galerias'

urlpatterns = [
    path('',views.lista_galeria , name='lista_galeria'),
   
]
