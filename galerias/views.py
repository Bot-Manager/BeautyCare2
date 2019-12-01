from django.shortcuts import render

# Create your views here.
from .models import Galerias ,Categoria


def lista_galeria(request):
    lista_galeria = Galerias.objects.all()
    categorias = Categoria.objects.all()

    context = {
        'lista_galeria' : lista_galeria ,
        'categorias' : categorias ,
    }
    
    return render(request , 'Galerias/galeria.html' , context)
