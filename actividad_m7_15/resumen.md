# Actividad N° 5 - Consultas Personalizadas con ORM y SQL en Django

## Archivo de Reflexión

### 1. ¿Qué ventajas encuentras en usar el ORM frente a SQL tradicional?

* **Productividad y Legibilidad:** Permite escribir código en Python puro de manera más limpia, comprensible y rápida en lugar de concatenar cadenas de texto SQL complejas.
* **Independencia de la Base de Datos (Portabilidad):** El ORM de Django traduce las consultas automáticamente al motor configurado (SQLite, PostgreSQL, MySQL). Si cambiamos de motor, el código Python permanece intacto.
* **Seguridad:** El ORM maneja de forma automática la sanitización de datos, mitigando significativamente ataques de inyección SQL de manera nativa.


### 2. ¿En qué situaciones te parece útil ejecutar SQL directamente desde Django?

* **Optimización de Consultas Complejas:** Cuando se requieren reportes masivos con múltiples uniones (`JOINs`), subconsultas y funciones agregadas analíticas específicas que el ORM procesa de forma ineficiente.
* **Uso de Funciones Nativas del Motor:** Si se necesita exprimir características exclusivas de un motor específico (por ejemplo, funciones geoespaciales avanzadas o indexación JSON nativa en PostgreSQL) que no están completamente mapeadas en el ORM estándar.


### 3. ¿Qué dificultades encontraste al trabajar con consultas más avanzadas?

* **Curva de Aprendizaje de la Sintaxis:** Comprender el uso de herramientas abstractas como `annotate()`, `aggregate()`, u objetos de condición `Q` y `F` requiere asimilar una lógica diferente al SQL tradicional.
* **Control del Rendimiento (Problema del N+1):** Si no se tiene cuidado con cómo el ORM maneja las relaciones, es fácil generar cientos de consultas en bucle a la base de datos de manera involuntaria, lo cual requiere el uso avanzado de `select_related` o `prefetch_related`.