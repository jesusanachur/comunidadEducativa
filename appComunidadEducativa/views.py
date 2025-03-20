from django.shortcuts import render
from .forms import RegistroForm
from django.contrib import messages


def home(request):
    return render(request,"home.html")

def sobrenosotros(request):
    return render(request,"sobrenosotro.html")

def inicioSesion (request):
    return render(request,"inicioSesion.html")

def planes(request):
    return render(request,"planes.html")

def programas(request):
    return render(request,"programas.html")

  
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            return render(request, 'registro.html', {'form': form})
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})
   
def profesores(request):
    return render(request,"profesore.html")

def recuperar_contrasena(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Aquí iría la lógica para enviar el correo de recuperación
        # Por ahora, solo mostramos un mensaje de confirmación
        messages.success(request, 'Se han enviado instrucciones de recuperación a tu correo electrónico.')
        return redirect('inicioSesion')
    return render(request, "recuperar_contrasena.html")
