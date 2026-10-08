---
id: "recurso-de-visitas"
title: "Visitas"
section: "Guía para productos"
subsection: "Métricas y Tendencias"
url: "https://developers.mercadolibre.com.co/es_co/recurso-de-visitas"
source_updated_at: "02/01/2026"
captured_at: "2026-10-08T22:53:02.514Z"
sha256: "799e9497f341d32f53a1ff3cdd55bdfcab3e4cb97a8861c95795a3ab2455d550"
---

# Visitas

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 02/01/2026  
**Captura:** 2026-10-08T22:53:02.514Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/recurso-de-visitas](https://developers.mercadolibre.com.co/es_co/recurso-de-visitas)

## Resumen

Permite consultar visitas de usuarios y publicaciones por fechas o ventanas de tiempo. Al republicar un artículo, las visitas históricas se heredan del parent_item.

## Contenido y conceptos documentados

- Parámetros descritos: user_id, item_id, date_from/date_to ISO (máximo 150 días), ending opcional YYYY-MM-DD, unit con valor day y last para delimitar la ventana.
- Las respuestas incluyen total_visits y visits_detail; las consultas time_window agregan results por intervalo. /visits/items se describe como total de los últimos dos años.
- Errores documentados incluyen site inválido, fechas mal formadas o ausentes, ventana mayor a 150 días, ending inválido, más de un item, formato incorrecto de ID, token no autorizado y artículo inexistente en time_window.

## Operaciones de API
## Operaciones de API

### Consultar ventana de visitas por artículo

**Método:** `GET`  
**Ruta:** `/items/{item_id}/visits/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrupa visitas de un artículo por intervalos de tiempo.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.
- `last` (query, opcional): Cantidad de unidades hacia atrás.
- `unit` (query, obligatorio): Unidad; la fuente enumera day.
- `ending` (query, opcional): Fecha YYYY-MM-DD; por defecto fecha/hora actual.

**Solicitud**

No documentado en la fuente.

**Respuesta**

item_id, fechas, total_visits, last, unit y results por fecha.

**Errores documentados**

- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid Site ID: usuario o ítem no pertenece a un site local válido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "unknown date format: date_from/date_to faltante o inválido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid time window: rango máximo 150 días." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid date format for ending date: solo YYYY-MM-DD." } ```
- ```json {   "status": 400,   "code": "validation_parameters",   "meaning": "maximum amount of items to query is 1." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid item ID format." } ```
- ```json {   "status": 403,   "code": "PA_UNAUTHORIZED_RESULT_FROM_POLICIES",   "meaning": "Token inválido, vencido o sin permisos." } ```
- ```json {   "status": 404,   "code": "not_found",   "meaning": "Item not found en time_window." } ```

**Ejemplos**

- GET /items/MCO471870973/visits/time_window?last=2&unit=day&ending=2021-08-06.

### Consultar visitas de artículo por fechas

**Método:** `GET`  
**Ruta:** `/items/visits`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera visitas de un artículo en fechas determinadas y por site.

**Parámetros**

- `ids` (query, obligatorio): ID de artículo; máximo documentado uno.
- `date_from` (query, obligatorio): Fecha inicial ISO; máximo documentado 150 días.
- `date_to` (query, obligatorio): Fecha final ISO; máximo documentado 150 días.

**Solicitud**

No documentado en la fuente.

**Respuesta**

item_id, date_from, date_to, total_visits y visits_detail.

**Errores documentados**

- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid Site ID: usuario o ítem no pertenece a un site local válido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "unknown date format: date_from/date_to faltante o inválido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid time window: rango máximo 150 días." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid date format for ending date: solo YYYY-MM-DD." } ```
- ```json {   "status": 400,   "code": "validation_parameters",   "meaning": "maximum amount of items to query is 1." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid item ID format." } ```
- ```json {   "status": 403,   "code": "PA_UNAUTHORIZED_RESULT_FROM_POLICIES",   "meaning": "Token inválido, vencido o sin permisos." } ```
- ```json {   "status": 404,   "code": "not_found",   "meaning": "Item not found en time_window." } ```

**Ejemplos**

- GET /items/visits?ids=MCO473861358&date_from=2021-01-01&date_to=2021-02-01.

### Consultar visitas totales de usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items_visits`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera visitas de publicaciones de un usuario en un intervalo.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario.
- `date_from` (query, obligatorio): Fecha inicial ISO; máximo documentado 150 días.
- `date_to` (query, obligatorio): Fecha final ISO; máximo documentado 150 días.

**Solicitud**

No documentado en la fuente.

**Respuesta**

user_id, date_from, date_to, total_visits y visits_detail (company, quantity).

**Errores documentados**

- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid Site ID: usuario o ítem no pertenece a un site local válido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "unknown date format: date_from/date_to faltante o inválido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid time window: rango máximo 150 días." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid date format for ending date: solo YYYY-MM-DD." } ```
- ```json {   "status": 400,   "code": "validation_parameters",   "meaning": "maximum amount of items to query is 1." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid item ID format." } ```
- ```json {   "status": 403,   "code": "PA_UNAUTHORIZED_RESULT_FROM_POLICIES",   "meaning": "Token inválido, vencido o sin permisos." } ```
- ```json {   "status": 404,   "code": "not_found",   "meaning": "Item not found en time_window." } ```

**Ejemplos**

- GET /users/1000011398/items_visits?date_from=2021-01-01&date_to=2021-02-01.

### Consultar ventana de visitas por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items_visits/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrupa visitas de un usuario por intervalos dentro de una ventana.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario.
- `last` (query, opcional): Cuántos días hacia atrás.
- `unit` (query, obligatorio): Unidad; la fuente enumera day.
- `ending` (query, opcional): Fecha YYYY-MM-DD; por defecto fecha/hora actual.

**Solicitud**

No documentado en la fuente.

**Respuesta**

user_id, fechas, total_visits, last, unit y results agrupados por día.

**Errores documentados**

- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid Site ID: usuario o ítem no pertenece a un site local válido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "unknown date format: date_from/date_to faltante o inválido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid time window: rango máximo 150 días." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid date format for ending date: solo YYYY-MM-DD." } ```
- ```json {   "status": 400,   "code": "validation_parameters",   "meaning": "maximum amount of items to query is 1." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid item ID format." } ```
- ```json {   "status": 403,   "code": "PA_UNAUTHORIZED_RESULT_FROM_POLICIES",   "meaning": "Token inválido, vencido o sin permisos." } ```
- ```json {   "status": 404,   "code": "not_found",   "meaning": "Item not found en time_window." } ```

**Ejemplos**

- GET /users/1000011398/items_visits/time_window?last=2&unit=day.

### Consultar visitas totales de artículo

**Método:** `GET`  
**Ruta:** `/visits/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve las visitas acumuladas del artículo; la guía lo describe para los últimos dos años.

**Parámetros**

- `ids` (query, obligatorio): ID del artículo; la fuente limita esta consulta a uno.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto indexado por ID de ítem con el total.

**Errores documentados**

- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid Site ID: usuario o ítem no pertenece a un site local válido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "unknown date format: date_from/date_to faltante o inválido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid time window: rango máximo 150 días." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid date format for ending date: solo YYYY-MM-DD." } ```
- ```json {   "status": 400,   "code": "validation_parameters",   "meaning": "maximum amount of items to query is 1." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid item ID format." } ```
- ```json {   "status": 403,   "code": "PA_UNAUTHORIZED_RESULT_FROM_POLICIES",   "meaning": "Token inválido, vencido o sin permisos." } ```
- ```json {   "status": 404,   "code": "not_found",   "meaning": "Item not found en time_window." } ```

**Ejemplos**

- GET /visits/items?ids=MLB9992242141.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/recurso-de-visitas](https://developers.mercadolibre.com.co/es_co/recurso-de-visitas)  
**Captura:** 2026-10-08T22:53:02.514Z
