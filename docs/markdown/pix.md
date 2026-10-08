---
id: "pix"
title: "Campaña co-fondeada para PIX"
section: "Guía para productos"
subsection: "Central de promociones"
url: "https://developers.mercadolibre.com.co/es_co/pix"
source_updated_at: "25/04/2025"
captured_at: "2026-10-08T22:51:09.102Z"
sha256: "2d597bf8b6fbf2800cba359d65a71e3b83b679f45910571e9520fc4682551fd8"
---

# Campaña co-fondeada para PIX

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 25/04/2025  
**Captura:** 2026-10-08T22:51:09.102Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/pix](https://developers.mercadolibre.com.co/es_co/pix)

## Resumen

Documenta la participación en campañas cofinanciadas de pagos PIX. El tipo de promoción es `BANK`, el subtipo `COFINANCED` y la disponibilidad indicada por la fuente es exclusivamente para el sitio brasileño MLB.

## Contenido y conceptos documentados

- El detalle de campaña identifica `type`, `sub_type`, `status`, fechas y `payment_method` (`PIX`).
- Se consulta la campaña y sus ítems; los ítems candidatos pueden sumarse y una oferta pendiente o activa puede eliminarse.
- La respuesta de oferta incluye `price`, `original_price` y `offer_id`; la campaña muestra porcentajes de cofinanciación del vendedor y Mercado Libre.
- Se documenta el estado de ítem `candidate` y estados de campaña como `candidate`, `started` y `pending`. La sección de errores registra 400 Bad Request.

**Campos y respuestas:** `id`, `type`, `sub_type`, `status`, `start_date`, `finish_date`, `deadline_date`, `name`, `payment_method`, `seller_percentage`, `meli_percentage`, `price`, `original_price` y `offer_id`.

**Ejemplos documentados:** consulta con `promotion_type=BANK&app_version=v2`, respuesta de campaña y ejemplo de oferta.

## Operaciones de API

## Conceptos y recursos asociados

### Campaña co-fondeada para PIX

Documenta la participación en campañas cofinanciadas de pagos PIX. El tipo de promoción es `BANK`, el subtipo `COFINANCED` y la disponibilidad indicada por la fuente es exclusivamente para el sitio brasileño MLB.

**Respuesta**

```json
{
  "fields": "`id`, `type`, `sub_type`, `status`, `start_date`, `finish_date`, `deadline_date`, `name`, `payment_method`, `seller_percentage`, `meli_percentage`, `price`, `original_price` y `offer_id`."
}
```

**Errores documentados**

- 400 Bad Request: la fuente lo enumera como error de la operación.

**Ejemplos documentados**

- consulta con `promotion_type=BANK&app_version=v2`, respuesta de campaña y ejemplo de oferta.
## Operaciones de API

### Elimina una oferta identificando promoción y oferta

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina una oferta identificando promoción y oferta.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: BANK
- `promotion_id` (query)
- `offer_id` (query)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta con `promotion_type=BANK&app_version=v2`, respuesta de campaña y ejemplo de oferta.

### Consulta detalle de campaña PIX

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalle de campaña PIX.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: BANK
- `app_version` (query): Valor mostrado: v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "type",
    "status",
    "start_date",
    "finish_date",
    "deadline_date",
    "name"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta con `promotion_type=BANK&app_version=v2`, respuesta de campaña y ejemplo de oferta.

### Lista los ítems de la campaña

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista los ítems de la campaña.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: BANK
- `app_version` (query): Valor mostrado: v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "results",
    "paging",
    "status",
    "offer_id",
    "price",
    "original_price"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta con `promotion_type=BANK&app_version=v2`, respuesta de campaña y ejemplo de oferta.

### Agrega una oferta del ítem a la campaña

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega una oferta del ítem a la campaña.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: BANK
- `promotion_id` (query)
- `offer_id` (query)

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

No documentado en la fuente.

**Ejemplos**

- consulta con `promotion_type=BANK&app_version=v2`, respuesta de campaña y ejemplo de oferta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/pix](https://developers.mercadolibre.com.co/es_co/pix)  
**Captura:** 2026-10-08T22:51:09.102Z
