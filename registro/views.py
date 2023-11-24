from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  # Asegúrate de que el formulario CustomUserCreationForm esté importado correctamente desde la aplicación "modelo"
from modelo.models import CustomUser
from django.contrib import messages
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso!')
            return redirect('listar_usuarios')
        else:
            messages.error(request, 'Hubo un error en el registro.') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'registrar.html', {'form': form})

def listar_usuarios(request):
    usuarios = CustomUser.objects.all()
    print(usuarios)
    return render(request, 'listar_usuarios.html', {
        'usuarios': usuarios})