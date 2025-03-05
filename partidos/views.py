from django.shortcuts import render, get_object_or_404, redirect
from .models import Partido
from .forms import PartidoForm

def listar_partidos(request):
    partidos = Partido.objects.all()
    return render(request, "partidos/listar.html", {"partidos": partidos})

def crear_partido(request):
    if request.method == "POST":
        form = PartidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_partidos")
    else:
        form = PartidoForm()
    return render(request, "partidos/form.html", {"form": form})

def editar_partido(request, partido_id):
    partido = get_object_or_404(Partido, id=partido_id)
    if request.method == "POST":
        form = PartidoForm(request.POST, instance=partido)
        if form.is_valid():
            form.save()
            return redirect("listar_partidos")
    else:
        form = PartidoForm(instance=partido)
    return render(request, "partidos/form.html", {"form": form})

def eliminar_partido(request, partido_id):
    partido = get_object_or_404(Partido, id=partido_id)
    if request.method == "POST":
        partido.delete()
        return redirect("listar_partidos")
    return render(request, "partidos/eliminar.html", {"partido": partido})
