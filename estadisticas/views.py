from django.shortcuts import render, get_object_or_404, redirect
from .models import EstadisticaJugador
from .forms import EstadisticaJugadorForm

# Listar estadísticas
def listar_estadisticas(request):
    estadisticas = EstadisticaJugador.objects.all()
    return render(request, 'estadisticas/listar.html', {'estadisticas': estadisticas})

# Crear una nueva estadística
def crear_estadistica(request):
    if request.method == 'POST':
        form = EstadisticaJugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estadisticas')
    else:
        form = EstadisticaJugadorForm()
    return render(request, 'estadisticas/form.html', {'form': form})

# Editar una estadística existente
def editar_estadistica(request, pk):
    estadistica = get_object_or_404(EstadisticaJugador, pk=pk)
    if request.method == 'POST':
        form = EstadisticaJugadorForm(request.POST, instance=estadistica)
        if form.is_valid():
            form.save()
            return redirect('listar_estadisticas')
    else:
        form = EstadisticaJugadorForm(instance=estadistica)
    return render(request, 'estadisticas/form.html', {'form': form})

# Eliminar una estadística
def eliminar_estadistica(request, pk):
    estadistica = get_object_or_404(EstadisticaJugador, pk=pk)
    if request.method == 'POST':
        estadistica.delete()
        return redirect('listar_estadisticas')
    return render(request, 'estadisticas/eliminar.html', {'estadistica': estadistica})
