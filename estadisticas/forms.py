from django import forms
from .models import EstadisticaJugador

class EstadisticaJugadorForm(forms.ModelForm):
    class Meta:
        model = EstadisticaJugador
        fields = ['jugador', 'partido', 'goles', 'asistencias', 'tarjetas_amarillas', 'tarjetas_rojas']
