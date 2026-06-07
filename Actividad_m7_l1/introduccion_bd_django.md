# Actividad N° 1: Introducción al Acceso a Bases de Datos con Django

## 1. Bases de datos en Django

### ¿Qué función cumple una base de datos dentro de una aplicación Django?
La base de datos es el componente encargado de **almacenar de forma persistente y organizada toda la información** que la aplicación necesita para funcionar. Esto incluye los datos ingresados por los usuarios, registros del sistema, configuraciones, y la gestión de usuarios y permisos nativa de Django. Sin ella, los datos se perderían cada vez que el servidor se reinicie.

### ¿Qué sistemas de bases de datos relacionales soporta Django por defecto?
Django ofrece soporte nativo (sin necesidad de instalar plugins complejos de terceros) para los siguientes sistemas de gestión de bases de datos relacionales (RDBMS):
* PostgreSQL
* MySQL
* MariaDB
* Oracle
* SQLite

### ¿Cuál es el motor de base de datos que se utiliza por defecto al crear un nuevo proyecto? ¿Por qué crees que es ese?
El motor por defecto es **SQLite** (configurado automáticamente en el archivo `settings.py` como `db.sqlite3`). 

**¿Por qué se elige este?:** Porque es una base de datos ligera que no requiere la instalación, configuración ni mantenimiento de un servidor de bases de datos independiente. Funciona directamente sobre un archivo local en el disco, lo que la hace ideal para la fase de desarrollo, prototipado rápido y pruebas, permitiendo que el proyecto funcione de inmediato tras ser creado.

---

## 2. ORM en Django

### ¿Qué es un ORM y cómo se diferencia de escribir sentencias SQL manualmente?
Un **ORM (Object-Relational Mapping)** es una técnica de programación que permite interactuar con la base de datos utilizando el paradigma de Orientación a Objetos del lenguaje de programación (en este caso, Python), en lugar de escribir código SQL nativo. 

**Diferencia principal:** Al escribir SQL manual, dependes de strings de texto específicos de la base de datos (ej. `SELECT * FROM libro WHERE autor = 'Cervantes';`). Con el ORM, utilizas métodos y sintaxis nativa de Python (ej. `Libro.objects.filter(autor="Cervantes")`), delegando en Django la traducción automática de ese código a la consulta SQL correspondiente.

### Menciona al menos dos ventajas de usar el ORM de Django.
1. **Independencia del motor de base de datos (Portabilidad):** Puedes cambiar el motor de la base de datos (por ejemplo, pasar de SQLite en desarrollo a PostgreSQL en producción) modificando solo un par de líneas en la configuración, sin necesidad de reescribir el código de tus consultas.
2. **Seguridad integrada:** El ORM de Django mitiga de forma automática ataques comunes como la *Inyección SQL* ($SQL\ Injection$), ya que sanitiza los parámetros de las consultas de manera interna.

### Explica qué significa que una clase modelo en Python represente una tabla en la base de datos.
Significa que existe un mapeo directo entre el código de Python y la estructura de almacenamiento. Cada **clase** que hereda de `models.Model` define la estructura de una nueva tabla; los **atributos de la clase** (como `titulo` o `autor`) definen las columnas y tipos de datos de dicha tabla; y cada **instancia (u objeto)** de esa clase representa una fila o registro específico dentro de la base de datos.

---

## 3. Migraciones

### ¿Qué son las migraciones en Django y por qué son importantes?
Las migraciones son el sistema que utiliza Django para propagar los cambios que realizas en tus modelos (añadir un campo, crear un modelo, eliminar una tabla) hacia la estructura real de la base de datos. 

Son cruciales porque actúan como un **control de versiones para el esquema de la base de datos**. Permiten que la base de datos evolucione junto con el código de manera controlada, automatizada y replicable en cualquier otro entorno de desarrollo o producción sin perder datos.

### ¿Qué comandos se utilizan para:
* **Crear una nueva migración a partir de cambios en los modelos:**
  ```bash
  python manage.py makemigrations