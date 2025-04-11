from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from .forms import RegistroForm, RecuperarContrasenaForm
from django.contrib.auth import login

def home(request):
    return render(request, "home.html")

def sobrenosotros(request):
    return render(request, "sobrenosotro.html")

def inicioSesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('nombre_de_la_url_principal')  # Cambia esto por tu URL de redirección
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, "inicioSesion.html")

    
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Guardar el formulario en la base de datos
            form.save()
            messages.success(request, 'Registro exitoso.')
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def planes(request):
    return render(request, "planes.html")

def programas(request):
    return render(request, "programas.html")



def profesores(request):
    return render(request, "profesore.html")

def recuperar_contrasena(request):
    if request.method == 'POST':
        form = RecuperarContrasenaForm(request.POST)
        if form.is_valid():
            # Implementar lógica para enviar correo de recuperación
            # email = form.cleaned_data['email']
            # enviar_correo_recuperacion(email)
            messages.success(request, 'Se han enviado instrucciones a tu correo electrónico.')
            return redirect('inicioSesion')
    else:
        form = RecuperarContrasenaForm()
    return render(request, "recuperar_contrasena.html", {'form': form})
