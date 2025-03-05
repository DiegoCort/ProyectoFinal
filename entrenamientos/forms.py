from django import forms
from .models import Entrenamiento

class EntrenamientoForm(forms.ModelForm):
    class Meta:
        model = Entrenamiento
        fields = ["equipo", "entrenador", "fecha", "duracion", "objetivos"]
        widgets = {
            "fecha": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "duracion": forms.TimeInput(attrs={"type": "time"}),
        }
