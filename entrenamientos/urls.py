from django.urls import path
from .views import listar_entrenamientos, crear_entrenamiento, editar_entrenamiento, eliminar_entrenamiento

urlpatterns = [
    path('', listar_entrenamientos, name='listar_entrenamientos'),
    path('crear/', crear_entrenamiento, name='crear_entrenamiento'),
    path('editar/<int:entrenamiento_id>/', editar_entrenamiento, name='editar_entrenamiento'),
    path('eliminar/<int:entrenamiento_id>/', eliminar_entrenamiento, name='eliminar_entrenamiento'),
]
