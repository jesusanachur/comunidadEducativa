from django.shortcuts import render
from .forms import RegistroForm, RecuperarContrasenaForm


def home(request):
    return render(request, "home.html")

def sobrenosotros(request):
    return render(request, "sobrenosotro.html")

def inicioSesion(request):
    return render(request, "inicioSesion.html")

def planes(request):
    return render(request, "planes.html")

def programas(request):
    return render(request, "programas.html")

  
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Aquí puedes guardar el formulario o hacer otras acciones
            # form.save()
            return render(request, 'registro.html', {'form': form})
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})
   
def profesores(request):
    return render(request, "profesore.html")

def recuperar_contrasena(request):
    if request.method == 'POST':
        form = RecuperarContrasenaForm(request.POST)
        if form.is_valid():
            # Aquí implementarías la lógica para enviar el correo de recuperación
            # email = form.cleaned_data['email']
            # enviar_correo_recuperacion(email)
            return render(request, "recuperar_contrasena.html", {'form': form, 'mensaje': 'Se han enviado instrucciones a tu correo'})
    else:
        form = RecuperarContrasenaForm()
    return render(request, "recuperar_contrasena.html", {'form': form})
    
    
