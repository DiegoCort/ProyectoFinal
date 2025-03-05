from django.urls import path
from .views import listar_estadisticas, crear_estadistica, editar_estadistica, eliminar_estadistica

urlpatterns = [
    path('', listar_estadisticas, name='listar_estadisticas'),
    path('crear/', crear_estadistica, name='crear_estadistica'),
    path('editar/<int:pk>/', editar_estadistica, name='editar_estadistica'),
    path('eliminar/<int:pk>/', eliminar_estadistica, name='eliminar_estadistica'),
]
