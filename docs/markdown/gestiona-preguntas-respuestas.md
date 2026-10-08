---
id: "gestiona-preguntas-respuestas"
title: "Preguntas y respuestas"
section: "Guía para productos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/gestiona-preguntas-respuestas"
source_updated_at: "29/09/2023"
captured_at: "2026-10-08T22:52:34.051Z"
sha256: "af2d74ac67062988ab8afe8f43ad2545c54c4102d706e02b64200afb2949ddf6"
---

# Preguntas y respuestas

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/09/2023  
**Captura:** 2026-10-08T22:52:34.051Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestiona-preguntas-respuestas](https://developers.mercadolibre.com.co/es_co/gestiona-preguntas-respuestas)

## Resumen

Referencia para buscar preguntas recibidas por vendedor o por ítem, consultar una pregunta, formular o responder preguntas, medir el tiempo de respuesta y eliminar preguntas. La búsqueda usa api_version=4; la fuente limita a 2.000 caracteres el texto de pregunta/respuesta.

## Contenido y conceptos documentados

- La búsqueda por vendedor o ítem devuelve preguntas con estado, fecha, texto, respuesta y remitente. Estados descritos incluyen UNANSWERED, ANSWERED, BANNED y CLOSED_UNANSWERED; preguntas sin respuesta con más de siete meses se eliminan.
- La búsqueda soporta filtros y ordenamiento, entre ellos seller_id, item/item_id, from, status, offset, limit, sort_fields y sort_types. sort_fields acepta item_id, seller_id, from_id y date_created; sort_types ASC o DESC.
- Las preguntas y respuestas se limitan a 2.000 caracteres. La respuesta debe incluir question_id y text; formular pregunta usa text e item_id.
- El tiempo de respuesta ofrece períodos weekdays_working_hours, weekdays_extra_hours y weekend. La guía recomienda notificaciones para eventos de preguntas; el estado BANNED puede investigarse en moderations/infractions.

En los ejemplos de la fuente se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /my/questions/hidden

La fuente menciona la ruta /my/questions/hidden, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/my/questions/hidden`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /moderations/infractions

La fuente menciona la ruta /moderations/infractions, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/moderations/infractions`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /items

La fuente menciona la ruta /items, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/items`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Eliminar pregunta

**Método:** `DELETE`  
**Ruta:** `/questions/{question_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la pregunta usando su ID y token del usuario.

**Parámetros**

- `question_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada DELETE.

### Consultar pregunta

**Método:** `GET`  
**Ruta:** `/questions/{question_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalle de una pregunta por su identificador.

**Parámetros**

- `question_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `api_version` (query, obligatorio): La guía muestra api_version=4.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, seller_id, buyer_id, item_id, status, text, fechas, answer y from.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente incluye respuesta de Vehículos con datos de contacto.

### Buscar preguntas

**Método:** `GET`  
**Ruta:** `/questions/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca preguntas por vendedor, publicación o usuario remitente.

**Parámetros**

- `seller_id` (query, opcional): Filtro de preguntas recibidas por vendedor.
- `item` (query, opcional): Filtro por publicación.
- `item_id` (query, opcional): Filtro por publicación en ejemplo de flujo de respuesta.
- `from` (query, opcional): ID de usuario remitente.
- `api_version` (query, obligatorio): La guía recomienda versión 4.
- `sort_fields` (query, opcional): Campos item_id,seller_id,from_id,date_created separados por coma.
- `sort_types` (query, opcional): ASC o DESC para los campos ordenados.
- `limit` (query, opcional): Tamaño de página.
- `offset` (query, opcional): Desplazamiento de resultados.

**Solicitud**

No documentado en la fuente.

**Respuesta**

total, limit, questions[] con date_created, item_id, seller_id, status, text, id, flags, answer y from; filtros y paginación.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos por seller_id, item, from y sort.

### Consultar tiempos de respuesta

**Método:** `GET`  
**Ruta:** `/users/{user_id}/questions/response_time`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve estadísticas de tiempo de respuesta por período.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

user_id y métricas de tiempo/porcentaje de respuesta por periodos de días laborales y fin de semana.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con periods de respuesta.

### Responder pregunta

**Método:** `POST`  
**Ruta:** `/answers`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Registra una respuesta para una pregunta recibida.

**Parámetros**

- `question_id` (body, obligatorio): ID de la pregunta.
- `text` (body, obligatorio): Respuesta, máximo 2.000 caracteres.

**Solicitud**

question_id y text.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de respuesta a una pregunta.

### Formular pregunta

**Método:** `POST`  
**Ruta:** `/questions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una pregunta sobre una publicación.

**Parámetros**

- `text` (body, obligatorio): Texto de la pregunta; máximo 2.000 caracteres.
- `item_id` (body, obligatorio): Publicación consultada.

**Solicitud**

text e item_id; UTF-8 recomendado.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo JSON con text e item_id.

### Referencia HTTP POST /my/questions/hidden

**Método:** `POST`  
**Ruta:** `/my/questions/hidden`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /my/questions/hidden. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestiona-preguntas-respuestas](https://developers.mercadolibre.com.co/es_co/gestiona-preguntas-respuestas)  
**Captura:** 2026-10-08T22:52:34.051Z
