from django import forms
from .models import Liga

class LigaForm(forms.ModelForm):
    class Meta:
        model = Liga
        fields = ['nombre']  # Ajusta según los campos de tu modelo
