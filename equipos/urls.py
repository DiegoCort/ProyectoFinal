from django.urls import path
from .views import (
    EquipoListView, EquipoCreateView, EquipoUpdateView, EquipoDeleteView,
    lista_equipos, nuevo_equipo, editar_equipo, eliminar_equipo
)

app_name = "equipos"

urlpatterns = [
    path("", EquipoListView.as_view(), name="lista"),
    path("nuevo/", EquipoCreateView.as_view(), name="nuevo"),
    path("editar/<int:pk>/", EquipoUpdateView.as_view(), name="editar"),
    path("eliminar/<int:pk>/", EquipoDeleteView.as_view(), name="eliminar"),
    
    # Rutas basadas en funciones
    path("lista_equipos/", lista_equipos, name="lista_equipos"),
    path("nuevo_equipo/", nuevo_equipo, name="nuevo_equipo"),
    path("editar_equipo/<int:equipo_id>/", editar_equipo, name="editar_equipo"),
    path("eliminar_equipo/<int:equipo_id>/", eliminar_equipo, name="eliminar_equipo"),
]
