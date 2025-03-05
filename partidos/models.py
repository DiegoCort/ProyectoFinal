from django.db import models
from ligas.models import Liga
from equipos.models import Equipo

class Partido(models.Model):
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="partidos_local")
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="partidos_visitante")
    fecha = models.DateTimeField()
    goles_local = models.IntegerField(null=True, blank=True)
    goles_visitante = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} - {self.fecha}"