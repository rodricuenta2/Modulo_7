
# Desarrollo de la Actividad N° 4: Gestión de Migraciones en Django

---

## 1. Comprensión teórica

### ¿Qué es una migración en Django?
Una migración en Django es un archivo de Python generado automáticamente (guardado en la carpeta `migrations/` de cada app) que actúa como un sistema de control de versiones para el esquema de la base de datos. Su función principal es propagar los cambios que realizas en tus modelos hacia las tablas reales de la base de datos.

### ¿Qué problema soluciona respecto a los cambios en los modelos?
Soluciona la desconexión entre el código orientado a objetos (Python) y el motor de bases de datos (SQL). Antes de las migraciones, si modificabas un modelo, tenías que escribir manualmente las sentencias SQL (`ALTER TABLE...`) directamente en la base de datos, lo que aumentaba el riesgo de errores, pérdida de datos y desincronización entre el código y el estado real de la base de datos.

### ¿Por qué no basta con modificar el archivo models.py directamente sin hacer migraciones?
Porque `models.py` es solo una definición conceptual en código Python. Modificarlo no altera automáticamente la estructura física de la base de datos. Django necesita procesar ese archivo, generar un plano de construcción (la migración) y luego ejecutarla para que el motor de base de datos cree o altere las columnas y tablas correspondientes.

---

## 2. Crear y aplicar migraciones

### a) Modificación del modelo
En el archivo `models.py` de la aplicación (por ejemplo, `principal`), se agregó el campo `isbn` al modelo existente:

```python
from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    # Campo nuevo solicitado:
    isbn = models.CharField(max_length=13, null=True, blank=True)
       

b) Ejecución de comandos de migración

python manage.py makemigrations

Qué hace: Analiza los cambios realizados en el archivo models.py en comparación con el estado actual de las migraciones. Al detectar el nuevo campo isbn, genera un nuevo archivo de migración en Python (por ejemplo, 0002_libro_isbn.py) dentro de la carpeta migrations/ de la app.

Nota: Este comando aún no altera la base de datos.

python manage.py migrate

Qué hace: Toma los archivos de migración que se han generado pero que aún no han sido aplicados y ejecuta las sentencias SQL correspondientes en el motor de base de datos actual. En este caso, añade físicamente la columna isbn a la tabla de libros.


c) Verificación del nuevo campo

Para comprobar que el campo quedó disponible de manera correcta, se puede verificar ingresando al shell de Django:

python manage.py shell

Dentro del entorno interactivo, ejecutamos:

from principal.models import Libro
# Creamos un registro de prueba con el nuevo campo
libro_test = Libro.objects.create(titulo="Django Avanzado", autor="Anónimo", isbn="1234567890123")
print(libro_test.isbn)  # Salida esperada: '1234567890123'


Alternativamente, al iniciar el servidor (python manage.py runserver) e ingresar al panel de administración de Django (/admin), el formulario del modelo Libro muestra con éxito el nuevo campo de texto para el isbn.

3. Aplicar migraciones existentes

Simulación pedagógica (Eliminar y volver a generar)

Se procedió a borrar de forma manual el archivo de migración generado en el paso anterior dentro de la carpeta migrations/.

Se ejecutaron nuevamente los comandos:

python manage.py makemigrations
python manage.py migrate

Resultado: Al haber borrado el registro del archivo, Django volvió a crear una migración equivalente. Al ejecutar migrate, si la base de datos ya tenía aplicada la columna de la prueba anterior, Django podría arrojar un error indicando que la columna ya existe, confirmando por qué esta práctica nunca debe hacerse en entornos de producción.


¿Qué sucede si no aplicas una migración pendiente?

Si dejas una migración pendiente (creada con makemigrations pero no ejecutada con migrate), tu código de Django estará desincronizado con la base de datos. En el momento en que tu aplicación intente realizar una consulta, crear o actualizar un registro que involucre las modificaciones pendientes, el servidor fallará lanzando excepciones de base de datos (por ejemplo, indicando que faltan columnas o tablas).

4. Revisión de estado (Opcional)

Comando ejecutado:

python manage.py showmigrations


Comentario de la información entregada:

Este comando lista de forma ordenada todas las aplicaciones del proyecto Django junto con cada uno de sus archivos de migración correspondientes.

¿Cómo saber cuáles ya se aplicaron?

Cada migración viene precedida por unos corchetes [ ].

Si aparece [X], significa que la migración ya fue aplicada con éxito en la base de datos.

Si aparece [ ] (vacío), significa que es una migración pendiente que aún requiere ejecutar el comando migrate.

