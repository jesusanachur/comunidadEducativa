from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def informacion(request):
    return render(request,"informacion.html")

def inicio (request):
    return render(request,"inicio Sesion.html")

def planes(request):
    return render(request,"planes.html")

def programas(request):
    return render(request,"programas.html")

def registro(request):
    return render(request,"registro.html")

def profesores(request):
    return render(request,"profesore.html")

def regitro(request):
    return render(request,"regitro.html")
    
# Create your views her
# Create your views here.
