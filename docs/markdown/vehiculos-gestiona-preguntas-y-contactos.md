---
id: "vehiculos-gestiona-preguntas-y-contactos"
title: "Gestiona preguntas y contactos"
section: "Guía para vehículos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-preguntas-y-contactos"
source_updated_at: "20/01/2026"
captured_at: "2026-10-08T22:53:16.353Z"
sha256: "2261703b13d7f718552e2360a7d88d6cd44be6f88c03483d886b9259cae04db0"
---

# Gestiona preguntas y contactos

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 20/01/2026  
**Captura:** 2026-10-08T22:53:16.353Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-preguntas-y-contactos](https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-preguntas-y-contactos)

## Resumen

Documenta métricas de preguntas, visualizaciones de teléfono y clics de WhatsApp por publicación o usuario, con consultas en rangos de fechas y ventanas agregadas por hora o día.

## Contenido y conceptos documentados

- Las consultas por fechas usan `date_from` y `date_to` en formato ISO. Para ventanas se usan `last` y `unit` (`day` o `hour`); `ending` fija el fin y, para varios ítems, `ids` contiene identificadores separados por coma.
- La página ofrece consultas por `ITEM_ID` y por `USER_ID`; las consultas múltiples usan la ruta de colección `/items/contacts/.../time_window`. Las respuestas muestran total, periodo y el ítem o usuario correspondiente.
- La sección de errores documenta HTTP 400 para parámetros inválidos. Para visitas por publicación, la fuente remite al recurso de Visitas. Autenticación mostrada: OAuth Bearer.

## Operaciones de API
## Operaciones de API

### GET /items/contacts/phone_views/time_window

**Método:** `GET`  
**Ruta:** `/items/contacts/phone_views/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta visualizaciones agregadas de varios ítems mediante `ids`.

**Parámetros**

- `ids` (query, obligatorio): IDs separados por coma
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour
- `ending` (query, opcional): Fin de ventana

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/contacts/questions/time_window

**Método:** `GET`  
**Ruta:** `/items/contacts/questions/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta preguntas agregadas para varios ítems mediante `ids`.

**Parámetros**

- `ids` (query, obligatorio): IDs separados por coma
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour
- `ending` (query, opcional): Fin de ventana

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/contacts/whatsapp/time_window

**Método:** `GET`  
**Ruta:** `/items/contacts/whatsapp/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta clics agregados de WhatsApp para varios ítems.

**Parámetros**

- `ids` (query, obligatorio): IDs separados por coma
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour
- `ending` (query, opcional): Fin de ventana

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/{ITEM_ID}/contacts/phone_views

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/contacts/phone_views`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta visualizaciones del teléfono de una publicación por fechas.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `date_from` (query, obligatorio): Inicio del rango ISO
- `date_to` (query, obligatorio): Fin del rango ISO

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/{ITEM_ID}/contacts/phone_views/time_window

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/contacts/phone_views/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta visualizaciones agregadas para una publicación.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/{ITEM_ID}/contacts/questions

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/contacts/questions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta preguntas recibidas por una publicación en un rango de fechas.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `date_from` (query, obligatorio): Inicio del rango ISO
- `date_to` (query, obligatorio): Fin del rango ISO

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/{ITEM_ID}/contacts/questions/time_window

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/contacts/questions/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta preguntas agregadas por ventana para una publicación.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/{ITEM_ID}/contacts/whatsapp

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/contacts/whatsapp`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta clics de WhatsApp de una publicación por fechas.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `date_from` (query, obligatorio): Inicio del rango ISO
- `date_to` (query, obligatorio): Fin del rango ISO

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/{ITEM_ID}/contacts/whatsapp/time_window

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/contacts/whatsapp/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta clics de WhatsApp agregados para una publicación.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}/contacts/phone_views

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/contacts/phone_views`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta visualizaciones de teléfonos de las publicaciones de un usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `date_from` (query, obligatorio): Inicio del rango ISO
- `date_to` (query, obligatorio): Fin del rango ISO

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}/contacts/phone_views/time_window

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/contacts/phone_views/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta visualizaciones agregadas por usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}/contacts/questions

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/contacts/questions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta preguntas de las publicaciones del usuario en un rango de fechas.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `date_from` (query, obligatorio): Inicio del rango ISO
- `date_to` (query, obligatorio): Fin del rango ISO

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}/contacts/questions/time_window

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/contacts/questions/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta preguntas agregadas por ventana para un usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}/contacts/whatsapp/time_window

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/contacts/whatsapp/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta clics de WhatsApp agregados para un usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-preguntas-y-contactos](https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-preguntas-y-contactos)  
**Captura:** 2026-10-08T22:53:16.353Z
