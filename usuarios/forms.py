from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class UsuarioRegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rol']

class UsuarioEdicionForm(UserChangeForm):
    password = None  # Para que no pida cambiar la contraseña en la edición
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rol']
