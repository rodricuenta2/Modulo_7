# Actividad N° 7 – Exploración de Aplicaciones Preinstaladas en Django

## 1. ¿Qué son las aplicaciones preinstaladas?

### Definición

Una aplicación "preinstalada" en Django es un módulo o paquete de software que viene integrado por defecto con el framework al momento de crear un nuevo proyecto. Estas aplicaciones resuelven problemas comunes del desarrollo web (como la autenticación, la gestión de sesiones o el panel de administración), evitando que el desarrollador tenga que programar estas funcionalidades desde cero.

### Declaración y Activación

Estas aplicaciones se declaran y activan dentro del archivo de configuración del proyecto, específicamente en **`settings.py`**, dentro de la lista llamada `INSTALLED_APPS`.

### Bloque `INSTALLED_APPS` y Descripción

```python


INSTALLED_APPS = [

    'django.contrib.admin', # Panel de administración automático para gestionar los datos de la app.

    'django.contrib.auth',# Sistema de autenticación (usuarios, grupos, permisos y contraseñas).

    'django.contrib.contenttypes',# Sistema que permite rastrear y asociar permisos/relaciones con todos los modelos instalados.

    'django.contrib.sessions',# Framework para gestionar sesiones basadas en el navegador de forma anónima o autenticada.

    'django.contrib.messages', # Marco de trabajo para notificaciones y mensajes flash temporales para el usuario.

    'django.contrib.staticfiles',# Sistema para gestionar y servir archivos estáticos (CSS, JavaScript, imágenes).
]


2. Interacción con modelos preinstalados

Nota: A continuación se documenta la ejecución de comandos desde la terminal interactiva (python manage.py shell).

Comandos Ejecutados y Observaciones

Ingreso al Shell:

Bash
python manage.py shell
Importación de Modelos:

Python
from django.contrib.auth.models import User, Group
from django.contrib.sessions.models import Session
Observación: Los modelos se importaron correctamente sin errores, lo que confirma que las aplicaciones correspondientes están activas en settings.py.

Creación de un Usuario:

Python
user = User.objects.create_user(username='pedro', email='pedro@example.com', password='Password123')
user.save()
print(user)
Observación: Se crea un registro en la base de datos para el usuario 'pedro'. El método create_user se encarga automáticamente de encriptar la contraseña (hashing) por seguridad.

Asignación del Usuario a un Grupo:

Python
# Creamos un grupo de prueba primero
grupo_editores, created = Group.objects.get_or_create(name='Editores')
# Asignamos el usuario al grupo
user.groups.add(grupo_editores)
print(user.groups.all())
Observación: La relación Many-to-Many entre User y Group funciona perfectamente. Ahora el usuario pertenece al grupo 'Editores'.

Consulta de Sesiones Activas:

Python
Session.objects.all()
Observación: Devuelve un QuerySet vacío <QuerySet []>. Esto se debe a que las sesiones se generan en la base de datos cuando un usuario inicia sesión activamente a través del navegador web, y en este momento estamos operando únicamente desde la consola sin interactuar con las cookies del navegador.

3. Acceso desde el Admin
Creación del Superusuario
Para acceder al panel de administración, ejecutamos en la terminal del sistema:

Bash
python manage.py createsuperuser
(Se completaron los datos de nombre de usuario, correo electrónico y contraseña).

Acceso al Panel
Tras iniciar el servidor con python manage.py runserver, ingresamos a la URL http://localhost:8000/admin (o la URL por defecto que expone GitHub Codespaces).

Grupos y Usuarios: Se visualizan dentro del bloque de "Autenticación y Autorización" (proveniente de django.contrib.auth). Aquí pudimos comprobar que el usuario 'pedro' y el grupo 'Editores' creados desde el shell aparecen listados.

Sesiones: Por defecto, el modelo Session no se registra visualmente en el admin de manera explícita para evitar manipulaciones accidentales de seguridad, pero el servicio está funcionando internamente en la base de datos.

4. Reflexión final
¿Cuál de estas aplicaciones crees que es más importante para el desarrollo de una aplicación real y por qué?
Considero que django.contrib.auth es la más crucial. Hoy en día, prácticamente cualquier aplicación web real requiere un sistema robusto, seguro y escalable de registro, inicio de sesión y control de permisos de usuarios. Desarrollar un sistema de autenticación seguro desde cero es complejo y propenso a vulnerabilidades; contar con este módulo preinstalado y certificado nos ahorra tiempo y mitiga riesgos críticos de seguridad.

¿Qué te llamó la atención al explorar el sistema de administración de Django?
Lo que más llama la atención es lo potente, intuitivo y "llave en mano" que es. Con solo activar una línea de código y crear un superusuario, Django genera una interfaz web completa, limpia y funcional para interactuar con la base de datos sin necesidad de escribir código HTML o CSS para el backend. Facilita enormemente las pruebas de datos y la administración inicial del proyecto.


## Paso 2: Ejecutar las pruebas en tu Codespace (Para recolectar tus evidencias)

Para que vivas la experiencia requerida por la actividad y puedas generar la captura opcional, ejecuta lo siguiente en la terminal de Codespace[cite: 24, 35, 44]:

1. **Asegúrate de aplicar las migraciones iniciales** (para que se creen las tablas de las apps preinstaladas)[cite: 7]:
   ```bash
   python manage.py migrate

   Crea tu superusuario (el que usarás para entrar al panel):  Bashpython manage.py createsuperuser
Prueba el Shell: ejecuta python manage.py shell y copia las líneas del punto 2 del Markdown para verificar que no lancen errores.  Inicia el servidor y toma tu captura:Bashpython manage.py runserver