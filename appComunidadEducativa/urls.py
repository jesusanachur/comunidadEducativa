from django.urls import path
from appComunidadEducativa import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('sobrenosotros', views.sobrenosotros, name="sobrenosotros"),
    path('inicioSesion', views.inicioSesion, name="inicioSesion"),
    path('planes', views.planes, name="planes"),
    path('programas', views.programas, name="programas"),
    path('registro', views.registro, name="registro"),
    path('profesores', views.profesores, name="profesores"),
    path('recuperar-contrasena', views.recuperar_contrasena, name="recuperar_contrasena"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)