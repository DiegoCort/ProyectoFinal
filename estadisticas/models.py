from django.db import models
from partidos.models import Partido
from usuarios.models import Usuario  # Asegúrate de que existe el modelo Usuario

class EstadisticaJugador(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, null=True, blank=True)
    jugador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="estadisticas")
    goles = models.PositiveIntegerField(default=0)
    asistencias = models.PositiveIntegerField(default=0)
    tarjetas_amarillas = models.PositiveIntegerField(default=0)
    tarjetas_rojas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.jugador} - {self.partido} | Goles: {self.goles}, Asistencias: {self.asistencias}"

