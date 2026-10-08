---
id: "campanas-del-vendedor"
title: "Campañas del vendedor"
section: "Guía para productos"
subsection: "Central de promociones"
url: "https://developers.mercadolibre.com.co/es_co/campanas-del-vendedor"
source_updated_at: "13/03/2026"
captured_at: "2026-10-08T22:51:11.980Z"
sha256: "b764ad5dc96b2e69cb46ff0b6f9c38da1f9a3689e6ebfca1429042eec2e9ce8f"
---

# Campañas del vendedor

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/03/2026  
**Captura:** 2026-10-08T22:51:11.980Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/campanas-del-vendedor](https://developers.mercadolibre.com.co/es_co/campanas-del-vendedor)

## Resumen

Describe cómo crear y administrar campañas de descuento propias del vendedor. Incluye criterios de elegibilidad, duración máxima y operaciones para gestionar la campaña y sus ofertas.

## Contenido y conceptos documentados

- La duración máxima indicada es de 14 días. Se requiere reputación verde; el ítem debe estar activo, ser nuevo y no tener exposición gratuita.
- El aviso indica que el subtipo `FIXED_PERCENTAGE` dejará de estar disponible desde julio de 2025. La creación usa `SELLER_CAMPAIGN` y la guía muestra `FLEXIBLE_PERCENTAGE`.
- El filtro `status_item` admite `active` o `paused`. Las ofertas pueden contener `deal_price`, `top_deal_price`, `original_price` y `price`.
- La fuente restringe cambios de `top_deal_price` después de iniciar la campaña y presenta errores de validación 400, incluido el bloqueo de cambios de fecha de inicio.

**Campos y respuestas:** `id`, `type`, `status`, `sub_type`, `start_date`, `finish_date`, `promotion_id`, `price`, `original_price`, `deal_price` y `top_deal_price`.

**Ejemplos documentados:** alta, modificación, eliminación y consulta de campaña y ofertas.

## Operaciones de API

## Conceptos y recursos asociados

### Campañas del vendedor

Describe cómo crear y administrar campañas de descuento propias del vendedor. Incluye criterios de elegibilidad, duración máxima y operaciones para gestionar la campaña y sus ofertas.

**Respuesta**

```json
{
  "fields": "`id`, `type`, `status`, `sub_type`, `start_date`, `finish_date`, `promotion_id`, `price`, `original_price`, `deal_price` y `top_deal_price`."
}
```

**Errores documentados**

- 400 bad request: validación; la fuente muestra límites de porcentaje y restricciones de start_date para campañas iniciadas.

**Ejemplos documentados**

- alta, modificación, eliminación y consulta de campaña y ofertas.
## Operaciones de API

### Retira la oferta indicando campaña y tipo

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Retira la oferta indicando campaña y tipo.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: SELLER_CAMPAIGN
- `promotion_id` (query)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- alta, modificación, eliminación y consulta de campaña y ofertas.

### Elimina una campaña del vendedor

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina una campaña del vendedor.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: SELLER_CAMPAIGN
- `app_version` (query): Valor mostrado: v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- alta, modificación, eliminación y consulta de campaña y ofertas.

### Consulta detalle y estado

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalle y estado.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: SELLER_CAMPAIGN
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

- alta, modificación, eliminación y consulta de campaña y ofertas.

### Lista ítems; admite `status_item`

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista ítems; admite `status_item`.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: SELLER_CAMPAIGN
- `app_version` (query): Valor mostrado: v2
- `status_item` (query): active o paused.

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

- alta, modificación, eliminación y consulta de campaña y ofertas.

### Agrega una oferta para el ítem

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega una oferta para el ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: SELLER_CAMPAIGN
- `promotion_id` (query)

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

- alta, modificación, eliminación y consulta de campaña y ofertas.

### Crea una campaña `SELLER_CAMPAIGN`

**Método:** `POST`  
**Ruta:** `/seller-promotions/promotions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una campaña `SELLER_CAMPAIGN`.

**Parámetros**

- `app_version` (query): Valor mostrado: v2

**Solicitud**

```json
{
  "fields": [
    "promotion_type",
    "name",
    "sub_type",
    "start_date",
    "finish_date"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- alta, modificación, eliminación y consulta de campaña y ofertas.

### Modifica precios de la oferta

**Método:** `PUT`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica precios de la oferta.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: SELLER_CAMPAIGN
- `promotion_id` (query)

**Solicitud**

```json
{
  "fields": [
    "deal_price",
    "top_deal_price"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- alta, modificación, eliminación y consulta de campaña y ofertas.

### Actualiza una campaña existente

**Método:** `PUT`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza una campaña existente.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: SELLER_CAMPAIGN
- `app_version` (query): Valor mostrado: v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- alta, modificación, eliminación y consulta de campaña y ofertas.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/campanas-del-vendedor](https://developers.mercadolibre.com.co/es_co/campanas-del-vendedor)  
**Captura:** 2026-10-08T22:51:11.980Z
