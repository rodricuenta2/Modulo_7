# Consultas básicas con el ORM
# Tomando como base el modelo provisto:

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    publicado = models.BooleanField(default=True)


# Obtener todos los libros
todos_los_libros = Libro.objects.all()


# Filtrar los libros por autor igual a "Cervantes"
libros_cervantes = Libro.objects.filter(autor="Cervantes")


# Obtener un libro específico por su id
# Suponiendo que buscamos el id=1
libro_especifico = Libro.objects.get(id=1)