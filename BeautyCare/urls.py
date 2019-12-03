"""BeautyCare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static  
from reservas.views import lista_reserva 
from users import views as users_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/' , include('servicios.urls' , namespace='servicios')),
    path('reservas/' , include('reservas.urls' , namespace='reservas')),
    path('galerias/' , include('galerias.urls' , namespace='galerias')),
    path('listaReservas/' , lista_reserva),
    path('login/' , auth_views.LoginView.as_view(template_name='users/login.html') , name='login'),
    path('logout/' , auth_views.LogoutView.as_view(template_name='users/logout.html') , name='logout'),
    path('registro/' , users_views.registro , name='registro'),
    path('' , include('home.urls' , namespace='home')),
    path('perfil/' , users_views.perfil , name='perfil'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)