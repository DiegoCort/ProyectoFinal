"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import redirect

def redirigir_a_login(request):
    return redirect('iniciar_sesion')  # Asegúrate de que 'iniciar_sesion' es el nombre correcto en tus URLs


urlpatterns = [
    path('', redirigir_a_login),
    path('admin/', admin.site.urls),
    path('ligas/', include('ligas.urls')),
    path("equipos/", include("equipos.urls")),
    path("partidos/", include("partidos.urls")),
    path('estadisticas/', include('estadisticas.urls')),
    path('entrenamientos/', include('entrenamientos.urls')),
    path('usuarios/', include('usuarios.urls')),
    
]
