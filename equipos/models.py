from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    liga = models.ForeignKey("ligas.Liga", on_delete=models.CASCADE, related_name="equipos_rel", default=1)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    entrenador = models.CharField(max_length=100, blank=True, null=True)
    fundado_en = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.liga.nombre})"
