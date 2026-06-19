import os
import django
from django.conf import settings
from django.db import models, connection

# ==============================================================================
# CONFIGURACIÓN DEL ENTORNO DJANGO (Para ejecutar como script independiente)
# ==============================================================================
if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',  # Base de datos en memoria para pruebas rápidas
            }
        },
        INSTALLED_APPS=[
            '__main__', # Registra este mismo archivo como app
        ],
    )
    django.setup()

# ==============================================================================
# DEFINICIÓN DEL MODELO
# ==============================================================================
class Libro(models.Model):
    titulo = models.CharField(max_length=100)       # Título del libro (máx 100 caracteres)
    autor = models.CharField(max_length=50)         # Autor del libro (máx 50 caracteres)
    paginas = models.IntegerField()                  # Cantidad de páginas (entero)
    disponible = models.BooleanField(default=True)  # Estado de disponibilidad (booleano)

    class Meta:
        app_label = '__main__'

# Crear las tablas en la base de datos en memoria
with connection.schema_editor() as schema_editor:
    schema_editor.create_model(Libro)

# Poblar la base de datos con datos de prueba para ver resultados
Libro.objects.bulk_create([
    Libro(titulo="Cien años de soledad", autor="Gabriel García Márquez", paginas=417, disponible=True),
    Libro(titulo="El amor en los tiempos del cólera", autor="Gabriel García Márquez", paginas=364, disponible=False),
    Libro(titulo="Crónica de una muerte anunciada", autor="Gabriel García Márquez", paginas=96, disponible=True),
    Libro(titulo="Pedro Páramo", autor="Juan Rulfo", paginas=128, disponible=True),
    Libro(titulo="El Aleph", autor="Jorge Luis Borges", paginas=144, disponible=False),
    Libro(titulo="Cuentos Cortos", autor="Autor Anónimo", paginas=50, disponible=True),
])

# ==============================================================================
# DESARROLLO DE LOS EJERCICIOS
# ==============================================================================

print("--- EJECUTANDO CONSULTAS ORM Y SQL ---\n")

# ------------------------------------------------------------------------------
# 1. Recuperación de registros
# ------------------------------------------------------------------------------
print("1. RECUPERACIÓN DE REGISTROS:")

# Recupera todos los libros registrados utilizando el método all()
todos_los_libros = Libro.objects.all()
print(f"-> Todos los libros ({len(todos_los_libros)} encontrados):", [l.titulo for l in todos_los_libros])

# Recupera solo los libros cuyo autor sea exactamente "Gabriel García Márquez" usando filter()
libros_garcia_marquez = Libro.objects.filter(autor="Gabriel García Márquez")
print("-> Libros de G. García Márquez:", [l.titulo for l in libros_garcia_marquez])

# Recupera los libros con más de 200 páginas usando el modificador __gt (Greater Than)
libros_mas_200_paginas = Libro.objects.filter(paginas__gt=200)
print("-> Libros con más de 200 páginas:", [f"{l.titulo} ({l.paginas} pág)" for l in libros_mas_200_paginas])


# ------------------------------------------------------------------------------
# 2. Filtros y exclusiones
# ------------------------------------------------------------------------------
print("\n2. FILTROS Y EXCLUSIONES:")

# Aplica un filtro para mostrar solo los libros donde disponible sea True
libros_disponibles = Libro.objects.filter(disponible=True)
print("-> Libros disponibles:", [l.titulo for l in libros_disponibles])

# Excluye todos los libros que tengan menos de 100 páginas usando exclude() con __lt (Less Than)
libros_grandes = Libro.objects.exclude(paginas__lt=100)
print("-> Libros excluyendo los de menos de 100 páginas:", [f"{l.titulo} ({l.paginas} pág)" for l in libros_grandes])


# ------------------------------------------------------------------------------
# 3. Consultas personalizadas con SQL
# ------------------------------------------------------------------------------
print("\n3. CONSULTAS PERSONALIZADAS CON SQL:")

# Ejecuta una consulta SQL directa utilizando raw() para obtener todos los libros ordenados por titulo
libros_ordenados_sql = Libro.objects.raw("SELECT * FROM __main___libro ORDER BY titulo ASC")
print("-> (SQL raw) Libros ordenados por título:", [l.titulo for l in libros_ordenados_sql])

# Usa connection.cursor() para ejecutar una query SQL personalizada (conteo de libros por autor)
with connection.cursor() as cursor:
    # Se ejecuta la sentencia SQL nativa de agrupación y conteo
    cursor.execute("SELECT autor, COUNT(*) FROM __main___libro GROUP BY autor")
    # Se recuperan todos los registros resultantes de la consulta
    conteo_por_autor_sql = cursor.fetchall()

print("-> (SQL cursor) Conteo de libros por autor:")
for fila in conteo_por_autor_sql:
    print(f"   Autor: {fila[0]} | Libros: {fila[1]}")


# ------------------------------------------------------------------------------
# 4. Campos específicos y anotaciones
# ------------------------------------------------------------------------------
print("\n4. CAMPOS ESPECÍFICOS Y ANOTACIONES:")

# Recupera solo los títulos de todos los libros usando values() retornando diccionarios llave-valor
titulos_values = Libro.objects.values('titulo')
print("-> Títulos obtenidos (con values()):", list(titulos_values))

# Agrega una anotación usando annotate() junto a Count() para calcular cuántos libros hay por autor desde el ORM
libros_por_autor_orm = Libro.objects.values('autor').annotate(total_libros=models.Count('id'))
print("-> (ORM annotate) Conteo de libros por autor:")
for registro in libros_por_autor_orm:
    print(f"   Autor: {registro['autor']} | Total: {registro['total_libros']}")