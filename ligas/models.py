from django.db import models
from equipos.models import Equipo  # Importamos Equipo correctamente

class Liga(models.Model):
    nombre = models.CharField(max_length=100)
    equipos = models.ManyToManyField(Equipo, related_name="ligas")  # Relación M:M con equipos
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

