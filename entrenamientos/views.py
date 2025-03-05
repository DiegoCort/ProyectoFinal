from django.shortcuts import render, get_object_or_404, redirect
from .models import Entrenamiento
from .forms import EntrenamientoForm

def listar_entrenamientos(request):
    entrenamientos = Entrenamiento.objects.all()
    return render(request, "entrenamientos/listar_entrenamientos.html", {"entrenamientos": entrenamientos})

def crear_entrenamiento(request):
    if request.method == "POST":
        form = EntrenamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_entrenamientos")
    else:
        form = EntrenamientoForm()
    return render(request, "entrenamientos/form_entrenamiento.html", {"form": form})

def editar_entrenamiento(request, pk):
    entrenamiento = get_object_or_404(Entrenamiento, pk=pk)
    if request.method == "POST":
        form = EntrenamientoForm(request.POST, instance=entrenamiento)
        if form.is_valid():
            form.save()
            return redirect("listar_entrenamientos")
    else:
        form = EntrenamientoForm(instance=entrenamiento)
    return render(request, "entrenamientos/form_entrenamiento.html", {"form": form})

def eliminar_entrenamiento(request, pk):
    entrenamiento = get_object_or_404(Entrenamiento, pk=pk)
    if request.method == "POST":
        entrenamiento.delete()
        return redirect("listar_entrenamientos")
    return render(request, "entrenamientos/confirmar_eliminar.html", {"entrenamiento": entrenamiento})
