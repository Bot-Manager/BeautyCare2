from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
from .forms import UserRegisterForm

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request , f'Cuenta creada por {username}! Ahora puedes loguearte')
            return redirect('http://127.0.0.1:8000/login')
    else:
        form = UserRegisterForm()
    return render(request , 'Users/Registro.html' , {'form': form})

