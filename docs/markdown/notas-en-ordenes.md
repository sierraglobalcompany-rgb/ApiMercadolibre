---
id: "notas-en-ordenes"
title: "Notas en órdenes"
section: "Guía para productos"
subsection: "Gestionar ventas"
url: "https://developers.mercadolibre.com.co/es_co/notas-en-ordenes"
source_updated_at: "29/12/2025"
captured_at: "2026-10-08T22:52:12.230Z"
sha256: "a2943b4b901d4da6602852dd74eb63843f24d41f2bc2bea4cbc61c7fb518639c"
---

# Notas en órdenes

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:52:12.230Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/notas-en-ordenes](https://developers.mercadolibre.com.co/es_co/notas-en-ordenes)

## Resumen

Documenta las operaciones para agregar, consultar, modificar y eliminar notas internas de órdenes. También describe el bloqueo de ofertas para un usuario específico mediante una lista negra del comprador.

## Contenido y conceptos documentados

- Las notas usan el campo `note` en el cuerpo y se identifican con `ORDER_ID` y `NOTE_ID`. El bloqueo se dirige al endpoint de usuario con `user_id` en el cuerpo.
- Los ejemplos usan OAuth Bearer y JSON. Los campos de respuesta, límites de texto y errores: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### DELETE /orders/{ORDER_ID}/notes/{NOTE_ID}

**Método:** `DELETE`  
**Ruta:** `/orders/{ORDER_ID}/notes/{NOTE_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina una nota.

**Parámetros**

- `ORDER_ID` (path, obligatorio)
- `NOTE_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /orders/{ORDER_ID}/notes

**Método:** `GET`  
**Ruta:** `/orders/{ORDER_ID}/notes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta las notas de una orden.

**Parámetros**

- `ORDER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /orders/{ORDER_ID}/notes

**Método:** `POST`  
**Ruta:** `/orders/{ORDER_ID}/notes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega una nota a la orden.

**Parámetros**

- `ORDER_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "note"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /users/{CUST_ID}/order_blacklist

**Método:** `POST`  
**Ruta:** `/users/{CUST_ID}/order_blacklist`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Bloquea ofertas del usuario indicado; el cuerpo contiene `user_id`.

**Parámetros**

- `CUST_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "user_id"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### PUT /orders/{ORDER_ID}/notes/{NOTE_ID}

**Método:** `PUT`  
**Ruta:** `/orders/{ORDER_ID}/notes/{NOTE_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica una nota existente.

**Parámetros**

- `ORDER_ID` (path, obligatorio)
- `NOTE_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "note"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/notas-en-ordenes](https://developers.mercadolibre.com.co/es_co/notas-en-ordenes)  
**Captura:** 2026-10-08T22:52:12.230Z
