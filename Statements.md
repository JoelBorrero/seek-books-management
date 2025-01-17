# Reto de Codificación

## Posición: Backend Developer
*(Django + MongoDB + Cloud)*

### Título: Sistema de Gestión de Libros

---

## Contexto:

Desarrollar el backend de una aplicación que gestiona información de libros utilizando MongoDB como base de datos. La aplicación debe proporcionar una API REST utilizando Django DRF para realizar operaciones CRUD en la base de datos y realizar agregaciones mediante pipelines de MongoDB para obtener información específica.

---

## Requerimientos:

- [x] Utiliza el paquete `pymongo` para la integración con MongoDB.
- [x] Crea un modelo `Book` con al menos los siguientes campos:
  - [x] `title`
  - [x] `author`
  - [x] `published_date`
  - [x] `genre`
  - [x] `price`
- [x] Configura una API REST para realizar operaciones CRUD en el modelo `Book`.
- [ ] Implementa un endpoint adicional que utilice un aggregation pipeline de MongoDB para obtener el precio promedio de los libros publicados en un año específico.
- [x] Proporciona datos de prueba iniciales para al menos 5 libros utilizando un script de migración para la BD (podrías usar un ORM de Django para esto).

---

## Puntos adicionales:

- [ ] Implementa autenticación de usuarios utilizando **Token Authentication** y proteger las APIs con este token.
- [x] Agregar paginación a la API REST.
- [x] Utiliza **serializers personalizados** para la representación de datos.
- [ ] Implementar **pruebas unitarias** para al menos dos funciones clave.

---

## Recomendaciones:

- [ ] Incluye **instrucciones claras** sobre cómo configurar y ejecutar la aplicación.
- [ ] Asegúrate de que el código sea legible y siga las mejores prácticas de desarrollo.
- [ ] Valora la implementación correcta de los **pipelines de agregación de MongoDB**.
- [ ] Considera la **modularidad** y **reutilización del código**.
- [ ] Proporciona **comentarios** en el código donde sea necesario.

---

## Duración del Reto:

El reto debe ser entregado máximo **48 horas** luego de haber recibido el reto por email.

---

## Entregables:

- [x] Repositorio de [**GitHub**](https://github.com/JoelBorrero/seek-books-management) con el código fuente.
- [ ] URL de la API desplegada en **Amazon Web Services (AWS)** (o en **Azure** o **GCP**) usando los servicios en su capa free.
- [x] Documentación de los **endpoints** en **Swagger**.
- [x] Una colección en **Postman** con las llamadas a cada una de las APIs, incluyendo un par de casos ya grabados:
- [x] Uno con **HTTP Status 200** (exitoso).
- [x] Uno con **HTTP Status 500** (para caso de error) por cada endpoint.

### Notas del desarrollador:
- No tuve claro si el requisito 
  > Utiliza el paquete `pymongo` para la integración con MongoDB

  se refería a solamente `pymongo` o era viable utilizar `mongoengine` o `djongo`, que en teoría utiliza `pymongo` internamente, por lo cual sólo implementé `pymongo` puro intentando simular el uso del ORM de Django.
- Por lo anterior, el script de migración debe ser un script de Python que se ejecute en el contenedor de Django, pues no es posible ejecutar `manage.py loaddata` en este caso.
- Mi cuenta de AWS está bloqueada, por lo cual no pude desplegar la aplicación en AWS (y tampoco quería complicarme mucho con crear otro contenedor para `nginx` 😅).
- Tenía pensado utilizar `rest_auth` para la autenticación, pero por el tema de base de datos, no utilicé el paquete, y hacerlo a mano creo que ya fue suficiente con la simulación de un ORM 😅.