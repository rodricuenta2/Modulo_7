
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
       
