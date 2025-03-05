from django.urls import path
from .views import lista_ligas, nueva_liga, editar_liga, eliminar_liga

urlpatterns = [
    path('', lista_ligas, name='lista_ligas'),  # Ruta base sin 'ligas/'
    path('nueva/', nueva_liga, name='nueva_liga'),
    path('editar/<int:liga_id>/', editar_liga, name='editar_liga'),
    path('eliminar/<int:liga_id>/', eliminar_liga, name='eliminar_liga'),
]
