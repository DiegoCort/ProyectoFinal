from django.contrib import admin
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "liga", "ciudad", "entrenador", "fundado_en")
    search_fields = ("nombre", "ciudad", "entrenador")
    list_filter = ("liga", "fundado_en")
