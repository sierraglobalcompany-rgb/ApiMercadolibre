---
id: "re-publica"
title: "Republicar ítems"
section: "Guía para productos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/re-publica"
source_updated_at: "29/12/2025"
captured_at: "2026-10-08T22:52:45.965Z"
sha256: "1dd10312fc0d052609fd7be4998a9c4ff54e34e14ba9018c0fc5073263b1b629"
---

# Republicar ítems

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:52:45.965Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/re-publica](https://developers.mercadolibre.com.co/es_co/re-publica)

## Resumen

Explica cómo volver a publicar un ítem cerrado conservando relaciones de ventas, preguntas y variantes cuando las reglas lo permiten. El flujo consulta primero su estado/fecha de cierre, lo cierra si es necesario y luego usa el recurso `relist` para crear una publicación nueva.

## Contenido y conceptos documentados

### Reglas y restricciones

- La página indica que el ítem padre debe haberse cerrado como máximo 60 días antes de la republicación. Los ítems `free` no trasladan visitas ni cantidad vendida; para vehículos, inmuebles y servicios se aplica el plazo de 60 días para mantener visitas.
- El ejemplo de cierre usa `PUT /items/$ITEM_ID` con `status: closed`. La republicación usa `POST /items/$ITEM_ID/relist` con `price`, `quantity` y `listing_type_id`; cuando hay variantes, el ejemplo conserva `variations`.
- Las llamadas muestran Bearer. Respuesta y errores específicos de la republicación: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Consultar estado de publicación

**Método:** `GET`  
**Ruta:** `/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene estado, fecha de cierre y datos del ítem padre.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- status
- stop_time
- expiration_time
- listing_type_id
- variations
- automatic_relist

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página consulta status y stop_time antes de relistar.

### Republicar ítem

**Método:** `POST`  
**Ruta:** `/items/$ITEM_ID/relist`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una publicación nueva a partir del ítem cerrado.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "price",
    "quantity",
    "listing_type_id",
    "variations (si aplica)"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El ítem debe haberse cerrado dentro de los 60 días previos, según la página.

### Cerrar ítem padre

**Método:** `PUT`  
**Ruta:** `/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cambia el estado del ítem a closed antes de republicarlo.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "status: closed"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de actualización para cerrar el ítem.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/re-publica](https://developers.mercadolibre.com.co/es_co/re-publica)  
**Captura:** 2026-10-08T22:52:45.965Z
