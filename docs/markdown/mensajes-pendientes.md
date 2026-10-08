---
id: "mensajes-pendientes"
title: "Mensajes pendientes"
section: "Guía para productos"
subsection: "Mensajería posventa"
url: "https://developers.mercadolibre.com.co/es_co/mensajes-pendientes"
source_updated_at: "11/09/2025"
captured_at: "2026-10-08T22:52:07.457Z"
sha256: "65ffd2b7a07792f9d27a45d045bbc2b015b2f223d2bf3b02258a946fd71a6716"
---

# Mensajes pendientes

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 11/09/2025  
**Captura:** 2026-10-08T22:52:07.457Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/mensajes-pendientes](https://developers.mercadolibre.com.co/es_co/mensajes-pendientes)

## Resumen

Documenta la consulta de mensajes posventa pendientes de lectura, tanto a partir de un recurso recibido por notificación como para un rol. Incluye el flujo para obtener la conversación y marcar como leídos los mensajes.

## Contenido y conceptos documentados

- La consulta específica por recurso usa `/messages/unread/{RESOURCE}`; la consulta general usa `/messages/unread` y exige `role` (`seller` o `buyer`); la consulta por recurso devuelve `user_id` y `results` con `resource` y `count`. El ejemplo incluye `tag=post_sale`. Para ver la conversación se consulta el recurso de mensajes del pack.
- La página explica el flujo desde notificaciones y el marcado de lectura, pero no muestra una ruta HTTP separada para dicha acción. Autenticación mostrada: OAuth Bearer. Errores documentados: 400 por IDs vacíos/inválidos, mensajes de órdenes distintas o mensaje inexistente; 404 cuando el mensaje no puede recuperarse del almacenamiento.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /packs/1234/sellers/2345

La fuente menciona la ruta /packs/1234/sellers/2345, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/packs/1234/sellers/2345`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /packs/1977056109/sellers/378136913

La fuente menciona la ruta /packs/1977056109/sellers/378136913, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/packs/1977056109/sellers/378136913`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /packs/2000000089077943/seller/415458330

La fuente menciona la ruta /packs/2000000089077943/seller/415458330, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/packs/2000000089077943/seller/415458330`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### GET /messages/packs/{PACK_ID}/sellers/{SELLER_ID}

**Método:** `GET`  
**Ruta:** `/messages/packs/{PACK_ID}/sellers/{SELLER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los mensajes de la conversación para procesar el recurso pendiente.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `SELLER_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "paging",
    "conversation_status",
    "messages"
  ]
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "IDs vacíos/inválidos, ID inexistente o IDs de mensajes de órdenes distintas." } ```
- ```json {   "code": "404",   "meaning": "El mensaje no puede recuperarse del almacenamiento." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /messages/unread

**Método:** `GET`  
**Ruta:** `/messages/unread`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta mensajes no leídos por rol; `role` es obligatorio y admite `seller` o `buyer`.

**Parámetros**

- `role` (query, obligatorio): Rol consultado: seller o buyer.
- `tag` (query, opcional): Identifica el flujo posventa.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "user_id",
    "results",
    "resource",
    "count"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /messages/unread/{RESOURCE}

**Método:** `GET`  
**Ruta:** `/messages/unread/{RESOURCE}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta mensajes pendientes de lectura para el recurso de una notificación.

**Parámetros**

- `RESOURCE` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "user_id",
    "results",
    "resource",
    "count"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### Referencia HTTP GET /messages/unread/packs/1234/sellers/2345

**Método:** `GET`  
**Ruta:** `/messages/unread/packs/1234/sellers/2345`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /messages/unread/packs/1234/sellers/2345. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

- `tag` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/mensajes-pendientes](https://developers.mercadolibre.com.co/es_co/mensajes-pendientes)  
**Captura:** 2026-10-08T22:52:07.457Z
