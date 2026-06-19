# Actividad N° 6 - Implementación de Operaciones CRUD con Django

## Respuestas al Cuestionario

### 1. ¿Cómo funciona el flujo completo de una operación CRUD?

El flujo sigue el patrón MVT (Modelo-Vista-Template) de Django:

- **Request (Petición):** El usuario interactúa mediante el navegador solicitando una acción (ej. hacer clic en "Eliminar").

- **URL Configuration:** Django recibe la URL, mapea la ruta y extrae los parámetros dinámicos necesarios (como el ID del objeto).

- **View (Vista):** La vista procesa la lógica del negocio. Si requiere datos, interactúa con el **Modelo** mediante el ORM (ej. `Libro.objects.get(id=id)`).

- **Template (Plantilla):** La vista renderiza la plantilla HTML inyectando los datos del modelo y la devuelve al navegador web en forma de respuesta HTTP. En operaciones de mutación (POST), se valida el formulario y se redirige (`redirect`) de vuelta al listado.

### 2. ¿Qué aprendiste sobre el enrutamiento y los parámetros dinámicos en URLs?

Aprendimos que Django maneja un sistema potente y legible para capturar variables directamente desde la ruta usando convertidores de ruta como `<int:id>`. Esto nos permite reutilizar una misma estructura de URL de manera segura, indicando explícitamente el tipo de dato que esperamos recibir en la vista, lo que facilita enormemente operaciones individuales sobre registros de la base de datos (como editar o eliminar).