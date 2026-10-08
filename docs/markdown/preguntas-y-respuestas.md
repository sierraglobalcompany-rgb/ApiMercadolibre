---
id: "preguntas-y-respuestas"
title: "Preguntas y Respuestas"
section: "Recursos de la API"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/preguntas-y-respuestas"
source_updated_at: "05/06/2025"
captured_at: "2026-10-08T22:53:59.153Z"
sha256: "c012546a8aafbe2c21bd469e49a7e4b6bc9473938db91f419fbe2adcaee6d3a6"
---

# Preguntas y Respuestas

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 05/06/2025  
**Captura:** 2026-10-08T22:53:59.153Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/preguntas-y-respuestas](https://developers.mercadolibre.com.co/es_co/preguntas-y-respuestas)

## Resumen

Documenta cómo buscar preguntas por ítem, consultar una pregunta, responderla y gestionar bloqueos de compradores.

## Contenido y conceptos documentados

- Para la nueva estructura, la página recomienda api_version=4. El ejemplo de búsqueda devuelve filtros y estados de pregunta como ANSWERED, UNANSWERED, CLOSED_UNANSWERED, DELETED y UNDER_REVIEW.
- Una pregunta se crea con text e item_id; una respuesta usa question_id y text.
- El endpoint de bloqueos admite type=blocked_by_questions, con paginación offset/limit; /users/{seller_id}/questions_blacklist/{user_id} quita un usuario bloqueado.
- No se documentan códigos de error específicos en esta página.

## Operaciones de API
## Operaciones de API

### Quitar usuario de lista de bloqueo de preguntas

**Método:** `DELETE`  
**Ruta:** `/users/{seller_id}/questions_blacklist/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina el usuario indicado de la lista de bloqueo del vendedor.

**Parámetros**

- `seller_id` (path, obligatorio): ID del vendedor.
- `user_id` (path, obligatorio): ID del usuario a desbloquear.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- DELETE /users/{seller_id}/questions_blacklist/{user_id}.

### Consultar bloqueos por preguntas

**Método:** `GET`  
**Ruta:** `/block-api/search/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta compradores bloqueados en el contexto de preguntas.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario consultado.
- `type` (query, obligatorio): blocked_by_questions.
- `offset` (query, opcional): Paginación; ejemplos de la fuente muestran 0.
- `limit` (query, opcional): Paginación; el ejemplo usa 10.

**Solicitud**

No documentado en la fuente.

**Respuesta**

users con id y blocked_at; paging con offset, limit y total. Sin bloqueos devuelve users vacío y total 0.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET con type=blocked_by_questions.

### Consultar preguntas recibidas

**Método:** `GET`  
**Ruta:** `/my/received_questions/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve preguntas recibidas por el usuario autenticado.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con total, limit y questions; cada pregunta puede contener date_created, item_id, seller_id, status, text, id, deleted_from_listing, hold, answer y from.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /my/received_questions/search.

### Consultar pregunta

**Método:** `GET`  
**Ruta:** `/questions/{question_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el detalle de una pregunta por ID.

**Parámetros**

- `question_id` (path, obligatorio): ID de la pregunta.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, answer, date_created, deleted_from_listing, hold, item_id, seller_id, status, text y from.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /questions/3957150025.

### Buscar preguntas por ítem

**Método:** `GET`  
**Ruta:** `/questions/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta preguntas realizadas sobre los ítems de un usuario; la fuente recomienda api_version=4 para la nueva estructura.

**Parámetros**

- `item_id` (query, obligatorio): ID de ítem, como en el ejemplo.
- `api_version` (query, opcional): La nota de la página recomienda valor 4.

**Solicitud**

No documentado en la fuente.

**Respuesta**

total, limit, questions, filters, available_filters y available_sorts; la lista incluye estados posibles.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /questions/search?item_id=MLA608007087; api_version=4.

### Responder pregunta

**Método:** `POST`  
**Ruta:** `/answers`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Envía una respuesta a una pregunta recibida.

**Parámetros**

- `Content-Type` (header, obligatorio): application/json.

**Solicitud**

JSON con question_id y text.

**Respuesta**

Pregunta con id, answer (date_created, status, text), date_created, item_id, seller_id, status, text y from.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- POST /answers con question_id y text.

### Realizar pregunta

**Método:** `POST`  
**Ruta:** `/questions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una pregunta sobre un ítem de otro usuario.

**Parámetros**

- `Content-Type` (header, obligatorio): application/json.

**Solicitud**

JSON con text e item_id.

**Respuesta**

id, answer, date_created, item_id, seller_id, status, text y from.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- POST /questions con text e item_id.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/preguntas-y-respuestas](https://developers.mercadolibre.com.co/es_co/preguntas-y-respuestas)  
**Captura:** 2026-10-08T22:53:59.153Z
