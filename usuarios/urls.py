from django.urls import path
from .views import (
    registrar_usuario, listar_usuarios, editar_usuario, eliminar_usuario,
    iniciar_sesion, cerrar_sesion
)

urlpatterns = [
    path('', listar_usuarios, name='listar_usuarios'),
    path('registrar/', registrar_usuario, name='registrar_usuario'),
    path('listar/', listar_usuarios, name='listar_usuarios'),
    path('editar/<int:usuario_id>/', editar_usuario, name='editar_usuario'),
    path('eliminar/<int:usuario_id>/', eliminar_usuario, name='eliminar_usuario'),
    path('login/', iniciar_sesion, name='iniciar_sesion'),
    path('logout/', cerrar_sesion, name='cerrar_sesion'),
]
