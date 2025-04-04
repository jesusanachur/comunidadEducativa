from django.db import models

class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=50, unique=True, blank=False, null=False)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=20, choices=[
        ('masculino', 'Masculino'), 
        ('femenino', 'Femenino'), 
        ('otro', 'Otro'),
        ('prefiero_no_decir', 'Prefiero no decir')
    ])
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre_usuario

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    contacto = models.CharField(max_length=20)
    cedula = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='profesores/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel = models.CharField(max_length=20, choices=[
        ('basico', 'Básico'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado')
    ])
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='cursos')
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion = models.PositiveIntegerField(help_text="Duración en semanas")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo

class Video(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    url = models.URLField(help_text="URL del video (YouTube, Vimeo, etc.)")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='videos')
    orden = models.PositiveIntegerField(default=0)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['orden']
        
    def __str__(self):
        return self.titulo