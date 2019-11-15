from django.shortcuts import render

# Create your views here.
from .models import Galerias ,Category


def lista_galeria(request):
    lista_galeria = Galerias.objects.all()
    categories =Category.objects.all()

    context = {
        'lista_galeria' : lista_galeria ,
        'categories' : categories ,
    }
    
    return render(request , 'Galerias/galeria.html' , context)
