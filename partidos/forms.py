from django import forms
from .models import Partido

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ["equipo_local", "equipo_visitante", "fecha", "goles_local", "goles_visitante"]
