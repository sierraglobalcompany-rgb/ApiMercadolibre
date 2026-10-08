---
id: "feedback-sobre-venta"
title: "Feedback de una venta"
section: "Guía para productos"
subsection: "Gestionar ventas"
url: "https://developers.mercadolibre.com.co/es_co/feedback-sobre-venta"
source_updated_at: "29/12/2025"
captured_at: "2026-10-08T22:51:48.833Z"
sha256: "733d1940a4e1750c71c21dcb1b4719f8bc4a594bb4ae19873015e55edad8c574"
---

# Feedback de una venta

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:51:48.833Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/feedback-sobre-venta](https://developers.mercadolibre.com.co/es_co/feedback-sobre-venta)

## Resumen

Documenta cómo consultar y gestionar la opinión de una venta: registrar feedback, responderlo, recuperar el feedback de una orden y consultar o actualizar un feedback individual. Distingue ventas concretadas y no concretadas y explica las restricciones relacionadas con el estado y la vigencia de la orden.

## Contenido y conceptos documentados

### Flujo y campos

- Las llamadas muestran autenticación `Bearer`. La fuente ejemplifica feedback con `fulfilled`, `rating`, `message`, `reason` y `restock_item`; el texto del mensaje debe ser menor a 160 caracteres. Para feedback no concretado (`fulfilled=false`) se documenta `reason`.
- El vendedor no puede registrar un feedback no concretado una vez expirada la orden. En envíos personalizados o ME1, se recomienda esperar certeza de entrega antes de informar el resultado. El feedback de una venta no afecta la reputación del vendedor.
- El recurso de una orden presenta información de compra y venta, incluidos identificadores, rol, fecha, calificación, mensaje, motivo y estado de concreción. El vendedor puede consultar feedback hasta cinco años, según la página.
- Si se intenta enviar feedback repetido, la página indica HTTP 400; también menciona `not_fulfilled_feedback_in_order_expired`. Los demás detalles de autenticación, cuerpos y respuestas no visibles para cada llamada: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Consultar feedback

**Método:** `GET`  
**Ruta:** `/feedback/$FEEDBACK_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera los datos de un feedback individual.

**Parámetros**

- `FEEDBACK_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- order_id
- reason
- item
- role
- extended_feedback
- date_created
- fulfilled
- rating
- message

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página presenta un ejemplo de consulta por ID.

### Consultar feedback de orden

**Método:** `GET`  
**Ruta:** `/orders/$ORDER_ID/feedback`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera feedback relacionado con una orden para comprador y vendedor.

**Parámetros**

- `ORDER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- sale
- purchase
- id
- order_id
- reason
- item
- role
- extended_feedback
- date_created
- fulfilled
- rating
- message

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La documentación indica consulta por el vendedor hasta cinco años.

### Responder feedback

**Método:** `POST`  
**Ruta:** `/feedback/$FEEDBACK_ID/reply`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Publica una respuesta del vendedor a un feedback recibido.

**Parámetros**

- `FEEDBACK_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "reply"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La solicitud se ejemplifica con reply.

### Crear feedback de una venta

**Método:** `POST`  
**Ruta:** `/orders/$ORDER_ID/feedback`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Registra la calificación y comentario del vendedor sobre una orden.

**Parámetros**

- `ORDER_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "fulfilled",
    "rating",
    "message (menos de 160 caracteres)",
    "reason (si fulfilled=false)",
    "restock_item"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": 400,   "meaning": "not_fulfilled_feedback_in_order_expired: la orden expiró para feedback no concretado." } ```
- ```json {   "code": 400,   "meaning": "El feedback repetido no se acepta." } ```

**Ejemplos**

- El texto recomienda esperar confirmación de entrega en envíos personalizados o ME1.

### Actualizar feedback

**Método:** `PUT`  
**Ruta:** `/feedback/$FEEDBACK_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza los campos permitidos de un feedback existente.

**Parámetros**

- `FEEDBACK_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "fulfilled",
    "rating",
    "message"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/feedback-sobre-venta](https://developers.mercadolibre.com.co/es_co/feedback-sobre-venta)  
**Captura:** 2026-10-08T22:51:48.833Z
