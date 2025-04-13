Este proyecto es una plataforma educativa en línea desarrollada con Django que permite a los usuarios registrarse, acceder a cursos, ver videos educativos y gestionar perfiles de profesores y estudiantes. La plataforma está diseñada para facilitar el aprendizaje en línea con un sistema intuitivo y funcionalidades completas.

Características principales
Autenticación de usuarios: Registro e inicio de sesión para estudiantes y profesores

Gestión de cursos: Creación y administración de cursos por parte de profesores

Contenido educativo: Videos organizados por cursos

Perfiles personalizados: Para estudiantes y profesores

Diseño responsive: Adaptable a diferentes dispositivos

Tecnologías utilizadas
Backend: Django (Python)

Frontend: HTML, CSS, JavaScript

Base de datos: SQLite (por defecto, configurable para producción)

Instalación y configuración
Requisitos previos
Python 3.8+

pip

virtualenv (recomendado)

Pasos para la instalación

Clonar el repositorio:

git clone [URL_DEL_REPOSITORIO]
cd appComunidadEducativa

Crear y activar un entorno virtual (recomendado):
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Instalar dependencias:

pip install -r requirements.txt

Configurar la base de datos:

python manage.py migrate

Ejecutar el servidor de desarrollo:
python manage.py runserver

Estructura del proyecto

appComunidadEducativa/
│
├── admin.py         # Configuración del panel de administración
├── apps.py          # Configuración de la aplicación
├── forms.py         # Formularios para usuarios, profesores, cursos y videos
├── models.py        # Modelos de base de datos
├── static/          # Archivos estáticos (CSS, JS, imágenes)
│   ├── contacto.css
│   ├── informacion.css
│   ├── inicioSesion.css
│   └── planes.css
└── ...


Uso de la plataforma
Para estudiantes
Registro: Completa el formulario de registro con tus datos personales.

Inicio de sesión: Accede con tu nombre de usuario y contraseña.

Explorar cursos: Navega por los cursos disponibles.

Ver videos: Accede al contenido educativo de cada curso.

Para profesores
Registro: Completa el formulario de registro de profesor.

Inicio de sesión: Accede con tus credenciales.

Crear cursos: Añade nuevos cursos con título, descripción y nivel.

Subir videos: Añade contenido educativo a tus cursos.

Para administradores
Accede al panel de administración en /admin

Gestiona usuarios, profesores, cursos y videos

Supervisa la actividad de la plataforma

Personalización
Puedes personalizar los estilos editando los archivos CSS en la carpeta static/:

contacto.css: Estilos para el formulario de contacto

informacion.css: Estilos para páginas informativas

inicioSesion.css: Estilos para el formulario de inicio de sesión

planes.css: Estilos para la sección de planes de suscripción
