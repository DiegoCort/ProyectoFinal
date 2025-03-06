from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Usuario
from .forms import UsuarioRegistroForm, UsuarioEdicionForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])  # Encriptar contraseña
            user.save()
            return redirect('login')
    else:
        form = UsuarioRegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def listar_usuarios(request):
    if request.user.rol == 'administrador':
        usuarios = Usuario.objects.all()  # Admin puede ver todos los usuarios
    else:
        usuarios = Usuario.objects.filter(id=request.user.id)  # Solo ve su propio perfil

    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

@login_required
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        form = UsuarioEdicionForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioEdicionForm(instance=usuario)
    return render(request, 'usuarios/editar_usuario.html', {'form': form})

@login_required
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/eliminar_usuario.html', {'usuario': usuario})

def iniciar_sesion(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            # Redirigir según el rol
            if user.rol == 'futbolista':
                return redirect('vista_futbolista')
            elif user.rol == 'tecnico':
                return redirect('vista_tecnico')
            elif user.rol == 'organizador':
                return redirect('vista_organizador')
            elif user.rol == 'administrador':
                return redirect('admin:index')  # Redirige al panel de admin de Django
            
            return redirect('listar_usuarios')  # Redirección por defecto
        else:
            return render(request, 'usuarios/login.html', {'error': 'Usuario o contraseña incorrectos'})

    return render(request, 'usuarios/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar_sesion')

def es_futbolista(user):
    return user.rol == 'futbolista'

# Función que verifica si el usuario es técnico
def es_tecnico(user):
    return user.rol == 'tecnico'

# Vista solo accesible para futbolistas
@login_required
@user_passes_test(es_futbolista)
def vista_futbolista(request):
    return render(request, 'usuarios/futbolista.html')

# Vista solo accesible para técnicos
@login_required
@user_passes_test(es_tecnico)
def vista_tecnico(request):
    return render(request, 'usuarios/tecnico.html')
