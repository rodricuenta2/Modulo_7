===============================================================================
ACTIVIDAD MÓDULO 7 - SESIÓN 3
Blog con Django y PostgreSQL
===============================================================================

OBJETIVO:
Diseñar un modelo de datos en Django, propagarlo a una base de datos Postgres
y realizar consultas ORM.

PASOS REALIZADOS:

1. LEVANTAR PROYECTO DJANGO
   - Se instaló Django 6.0.6 y psycopg2-binary
   - Se creó el proyecto 'blog_project' con el comando:
     django-admin startproject blog_project

2. LEVANTAR BASE DE DATOS POSTGRES
   - Se activó PostgreSQL 16 en el servidor local
   - Se creó la base de datos 'blog_db'
   - Se creó el usuario 'blog_user' con contraseña 'blog_pass'
   - Se otorgaron todos los privilegios sobre blog_db a blog_user

3. CONFIGURAR ACCESO A BASE DE DATOS EN settings.py
   - Se configuró el diccionario DATABASES con:
     ENGINE: django.db.backends.postgresql
     NAME: blog_db
     USER: blog_user
     PASSWORD: blog_pass
     HOST: 127.0.0.1
     PORT: 5432

4. CREAR MODELOS DE DATOS (blog/models.py)
   - Modelo Autor: nombre, email, biografia, fecha_nacimiento
   - Modelo Articulo: titulo, contenido, fecha_publicacion, autor (FK)
   - Se registró la app 'blog' en INSTALLED_APPS

5. MIGRACIÓN DE DATOS
   - Se ejecutó: python manage.py makemigrations blog
   - Se ejecutó: python manage.py migrate
   - Las tablas blog_autor y blog_articulo se crearon en PostgreSQL

6. CONSULTAS ORM REALIZADAS:
   - Autor.objects.all() - Listar todos los autores
   - Articulo.objects.all() - Listar todos los artículos
   - Articulo.objects.filter(autor__nombre__icontains=...) - Filtrar por autor
   - Autor.objects.get(email=...) - Obtener autor por email
   - Articulo.objects.filter(autor=autor).count() - Contar artículos por autor
   - autor.articulos.all() - Relación inversa con related_name
   - Articulo.objects.all().order_by("titulo") - Ordenar artículos
   - Articulo.objects.first() / Articulo.objects.last() - Primer/último artículo
===============================================================================
