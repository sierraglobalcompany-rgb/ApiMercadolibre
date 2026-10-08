---
id: "automatizaciones-de-precios"
title: "Automatizaciones de precios"
section: "Guía para productos"
subsection: "Precios y Costos"
url: "https://developers.mercadolibre.com.co/es_co/automatizaciones-de-precios"
source_updated_at: "01/10/2026"
captured_at: "2026-10-08T22:51:01.963Z"
sha256: "3450de90411d8156a3c577dde0961386aa1d64589abdcfe31bd4d2c06ac51f27"
---

# Automatizaciones de precios

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 01/10/2026  
**Captura:** 2026-10-08T22:51:01.963Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/automatizaciones-de-precios](https://developers.mercadolibre.com.co/es_co/automatizaciones-de-precios)

## Resumen

Documenta cómo consultar, asignar, modificar y retirar reglas de automatización de precios, además de revisar el historial. Si un ítem tiene automatización activa, las actualizaciones de precio por la API de ítems se rechazan.

## Contenido y conceptos documentados

- Las reglas se identifican con `rule_id`; la fuente también muestra `min_price`, `max_price`, `status` (`ACTIVE` o `PAUSED`) y `status_detail`.
- Antes de modificar el precio de un ítem, consulta si tiene automatización. El cambio del campo `price` mediante `PUT /items/{item_id}` puede responder `item.price.not_modifiable` (400).
- También se documentan historial de precios y reglas disponibles a nivel de producto de catálogo.
- Errores de automatización documentados incluyen `item_not_found` (404), `user_not_authorized` (412), `item_not_automatizable` (412), `automation_already_created` (412), `automation_operation_not_allowed` (412) y errores de procesamiento de regla/estrategia (422).

**Campos y respuestas:** `rule_id`, `min_price`, `max_price`, `status`, `status_detail`, `item_id` y `price`; la estructura depende de cada operación.

**Ejemplos documentados:** consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

## Operaciones de API

## Conceptos y recursos asociados

### Automatizaciones de precios

Documenta cómo consultar, asignar, modificar y retirar reglas de automatización de precios, además de revisar el historial. Si un ítem tiene automatización activa, las actualizaciones de precio por la API de ítems se rechazan.

**Respuesta**

```json
{
  "fields": "`rule_id`, `min_price`, `max_price`, `status`, `status_detail`, `item_id` y `price`; la estructura depende de cada operación."
}
```

**Ejemplos documentados**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.
## Operaciones de API

### Elimina la automatización del ítem

**Método:** `DELETE`  
**Ruta:** `/pricing-automation/items/{item_id}/automation`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la automatización del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### Consulta la automatización del ítem

**Método:** `GET`  
**Ruta:** `/pricing-automation/items/{item_id}/automation`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la automatización del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### Consulta el historial de cambios de precio automatizados

**Método:** `GET`  
**Ruta:** `/pricing-automation/items/{item_id}/price/history`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el historial de cambios de precio automatizados.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### Consulta reglas disponibles para un ítem

**Método:** `GET`  
**Ruta:** `/pricing-automation/items/{item_id}/rules`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta reglas disponibles para un ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### Consulta reglas para un producto de catálogo

**Método:** `GET`  
**Ruta:** `/pricing-automation/products/{catalog_product_id}/rules`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta reglas para un producto de catálogo.

**Parámetros**

- `catalog_product_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### Lista ítems del usuario con automatizaciones; admite `offset` y `limit`

**Método:** `GET`  
**Ruta:** `/pricing-automation/users/{user_id}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista ítems del usuario con automatizaciones; admite `offset` y `limit`.

**Parámetros**

- `user_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `offset` (query): Parámetro de paginación.
- `limit` (query): Parámetro de paginación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### Asigna una regla (`rule_id`)

**Método:** `POST`  
**Ruta:** `/pricing-automation/items/{item_id}/automation`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Asigna una regla (`rule_id`).

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

```json
{
  "fields": [
    "rule_id"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### Asigna automatización indicando producto de catálogo

**Método:** `POST`  
**Ruta:** `/pricing-automation/items/{item_id}/automation/by-product/{catalog_product_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Asigna automatización indicando producto de catálogo.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `catalog_product_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### La guía advierte que cambiar el precio se rechaza si la automatización está activa

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La guía advierte que cambiar el precio se rechaza si la automatización está activa.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

```json
{
  "fields": [
    "price"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400 item.price.not_modifiable: precio no editable cuando la automatización está activa.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### Actualiza la regla asignada

**Método:** `PUT`  
**Ruta:** `/pricing-automation/items/{item_id}/automation`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza la regla asignada.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

```json
{
  "fields": [
    "rule_id"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/automatizaciones-de-precios](https://developers.mercadolibre.com.co/es_co/automatizaciones-de-precios)  
**Captura:** 2026-10-08T22:51:01.963Z
