from django.contrib import admin
from .models import Usuario, Profesor, Curso, Video

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Video)