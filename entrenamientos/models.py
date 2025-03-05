from django.db import models
from usuarios.models import Usuario
from equipos.models import Equipo

class Entrenamiento(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="entrenamientos")
    entrenador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="entrenamientos_dirigidos")
    fecha = models.DateTimeField()
    duracion = models.DurationField(help_text="Duración en horas y minutos")
    objetivos = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.equipo} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"
