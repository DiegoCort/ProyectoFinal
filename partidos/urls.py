from django.urls import path
from .views import listar_partidos, crear_partido, editar_partido, eliminar_partido

urlpatterns = [
    path("", listar_partidos, name="listar_partidos"),
    path("crear/", crear_partido, name="crear_partido"),
    path("editar/<int:partido_id>/", editar_partido, name="editar_partido"),
    path("eliminar/<int:partido_id>/", eliminar_partido, name="eliminar_partido"),
]
