from django import forms
from .models import Usuario, Profesor, Curso, Video

class RegistroForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirmar contraseña")
    
    class Meta:
        model = Usuario
        fields = ['nombre_completo', 'nombre_usuario', 'email', 'contraseña', 'fecha_nacimiento', 'genero']
        widgets = {
            'contraseña': forms.PasswordInput(),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'nombre_completo': 'Nombre completo',
            'nombre_usuario': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'contraseña': 'Contraseña',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'genero': 'Género'
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('contraseña')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario o correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    remember_me = forms.BooleanField(required=False, label="Recordarme")

class ProfesorForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirmar contraseña")
    
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'correo', 'contacto', 'cedula', 
                 'fecha_nacimiento', 'direccion', 'contraseña', 'especialidad', 'biografia', 'foto']
        widgets = {
            'contraseña': forms.PasswordInput(),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'biografia': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('contraseña')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        return cleaned_data

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'descripcion', 'nivel', 'profesor', 'precio', 'duracion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['titulo', 'descripcion', 'url', 'curso', 'orden']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class RecuperarContrasenaForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico")