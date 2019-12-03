from django.urls import path
from . import views

app_name = 'nosotros'


urlpatterns = [
    path('', views.nosotros_lista , name='nosotros_lista'),
    
]
