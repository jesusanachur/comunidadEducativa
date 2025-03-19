from django.urls import path
from appComunidadEducativa import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('informacion', views.informacion, name="informacion"),
    path('inicio Sesion', views.inicio, name="inicio Sesion"),
    path('planes', views.planes, name="planes"),
    path('programas', views.programas, name="programas"),
    path('registro', views.registro, name="registro"),
    path('profesores', views.profesores, name="profesores"),
    path('registro', views.registro, name="pro"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)