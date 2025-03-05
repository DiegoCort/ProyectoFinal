from django.shortcuts import render, redirect, get_object_or_404
from .models import Liga
from .forms import LigaForm

def lista_ligas(request):
    ligas = Liga.objects.all()
    return render(request, 'ligas/lista_ligas.html', {'ligas': ligas})

def nueva_liga(request):
    if request.method == 'POST':
        form = LigaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ligas')
    else:
        form = LigaForm()
    return render(request, 'ligas/nueva_liga.html', {'form': form})

def editar_liga(request, liga_id):
    liga = get_object_or_404(Liga, id=liga_id)  # Ahora sí reconoce get_object_or_404
    if request.method == "POST":
        form = LigaForm(request.POST, instance=liga)
        if form.is_valid():
            form.save()
            return redirect('lista_ligas')
    else:
        form = LigaForm(instance=liga)
    return render(request, 'ligas/editar_liga.html', {'form': form})

def eliminar_liga(request, liga_id):
    liga = get_object_or_404(Liga, id=liga_id)
    if request.method == "POST":
        liga.delete()
        return redirect('lista_ligas')
    return render(request, 'ligas/eliminar_liga.html', {'liga': liga})