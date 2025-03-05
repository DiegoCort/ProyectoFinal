from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Equipo
from .forms import EquipoForm

# Vista para listar equipos
class EquipoListView(ListView):
    model = Equipo
    template_name = "equipos/lista.html"
    context_object_name = "equipos"

# Vista para crear un equipo
class EquipoCreateView(CreateView):
    model = Equipo
    template_name = "equipos/formulario.html"
    fields = ["nombre", "liga"]
    success_url = reverse_lazy("equipos:lista")

# Vista para actualizar un equipo
class EquipoUpdateView(UpdateView):
    model = Equipo
    template_name = "equipos/formulario.html"
    fields = ["nombre", "liga"]
    success_url = reverse_lazy("equipos:lista")

# Vista para eliminar un equipo
class EquipoDeleteView(DeleteView):
    model = Equipo
    template_name = "equipos/confirmar_eliminar.html"
    success_url = reverse_lazy("equipos:lista")
    
def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos/lista_equipos.html', {'equipos': equipos})

def nuevo_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')
    else:
        form = EquipoForm()
    return render(request, 'equipos/nuevo_equipo.html', {'form': form})

# Editar equipo
def editar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'equipos/editar_equipo.html', {'form': form, 'equipo': equipo})

# Eliminar equipo
def eliminar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    if request.method == 'POST':
        equipo.delete()
        return redirect('lista_equipos')
    return render(request, 'equipos/eliminar_equipo.html', {'equipo': equipo})