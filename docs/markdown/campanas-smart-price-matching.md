---
id: "campanas-smart-price-matching"
title: "Co-fondeada automatizada y precios competitivos"
section: "Guía para productos"
subsection: "Central de promociones"
url: "https://developers.mercadolibre.com.co/es_co/campanas-smart-price-matching"
source_updated_at: "09/06/2026"
captured_at: "2026-10-08T22:51:19.909Z"
sha256: "f8b08bbc1cb4a5eb0e1f6290dc8e8bfc33a2ffbcf88849caa9894979a927d6d1"
---

# Co-fondeada automatizada y precios competitivos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 09/06/2026  
**Captura:** 2026-10-08T22:51:19.909Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/campanas-smart-price-matching](https://developers.mercadolibre.com.co/es_co/campanas-smart-price-matching)

## Resumen

Explica la gestión de campañas automatizadas y de precios competitivos: SMART, PRICE_MATCHING y PRICE_MATCHING_MELI_ALL. Permite consultar campañas e ítems, incorporar ofertas y retirarlas, e identificar descuentos adicionales aplicados por Mercado Libre.

## Contenido y conceptos documentados

- Los ejemplos usan `promotion_type` para diferenciar los tipos de campaña y `app_version=v2`. Las campañas pueden ser cofinanciadas o financiadas al 100 % por Mercado Libre, según el tipo.
- En los ítems, `status_item` filtra `active` o `paused`; los estados de oferta incluyen `candidate` y ofertas activas. La oferta contiene `offer_id`, `price` y `original_price`.
- Si `boosted_offer` es `true`, la respuesta puede incluir `discount_meli_boosted_percentage`, `discount_meli_boost_amount` y `total_price_for_boosted_offer`.
- La fuente muestra respuestas 200 OK al retirar ofertas.

**Campos y respuestas:** `promotion_id`, `promotion_type`, `status`, `offer_id`, `price`, `original_price`, `boosted_offer`, `discount_meli_boosted_percentage`, `discount_meli_boost_amount` y `total_price_for_boosted_offer`.

**Ejemplos documentados:** detalle e ítems para los tres tipos; alta y eliminación de ofertas.

## Operaciones de API

## Conceptos y recursos asociados

### Co-fondeada automatizada y precios competitivos

Explica la gestión de campañas automatizadas y de precios competitivos: SMART, PRICE_MATCHING y PRICE_MATCHING_MELI_ALL. Permite consultar campañas e ítems, incorporar ofertas y retirarlas, e identificar descuentos adicionales aplicados por Mercado Libre.

**Respuesta**

```json
{
  "fields": "`promotion_id`, `promotion_type`, `status`, `offer_id`, `price`, `original_price`, `boosted_offer`, `discount_meli_boosted_percentage`, `discount_meli_boost_amount` y `total_price_for_boosted_offer`."
}
```

**Ejemplos documentados**

- detalle e ítems para los tres tipos; alta y eliminación de ofertas.
## Operaciones de API

### Retira la oferta usando tipo, campaña y `offer_id`

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Retira la oferta usando tipo, campaña y `offer_id`.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `app_version` (query): La guía muestra v2.
- `promotion_type` (query): Tipo de campaña indicado en cada ejemplo.
- `promotion_id` (query): Identificador de campaña.
- `offer_id` (query): Identificador de oferta.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- detalle e ítems para los tres tipos; alta y eliminación de ofertas.

### Consulta la oferta de un ítem

**Método:** `GET`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la oferta de un ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `app_version` (query): La guía muestra v2.
- `promotion_type` (query): Tipo de campaña indicado en cada ejemplo.
- `promotion_id` (query): Identificador de campaña.
- `offer_id` (query): Identificador de oferta.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "type",
    "sub_type",
    "status",
    "start_date",
    "finish_date",
    "deadline_date",
    "name",
    "offer_id",
    "price",
    "original_price"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- detalle e ítems para los tres tipos; alta y eliminación de ofertas.

### Consulta detalle de campaña SMART o PRICE_MATCHING

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalle de campaña SMART o PRICE_MATCHING.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta documentada.
- `promotion_type` (query): Tipo de campaña indicado en cada ejemplo.
- `app_version` (query): La guía muestra v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "type",
    "sub_type",
    "status",
    "start_date",
    "finish_date",
    "deadline_date",
    "name",
    "offer_id",
    "price",
    "original_price"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- detalle e ítems para los tres tipos; alta y eliminación de ofertas.

### Lista ítems asociados a la campaña

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista ítems asociados a la campaña.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta documentada.
- `promotion_type` (query): Tipo de campaña indicado en cada ejemplo.
- `app_version` (query): La guía muestra v2.
- `status_item` (query): Filtro active o paused.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "type",
    "sub_type",
    "status",
    "start_date",
    "finish_date",
    "deadline_date",
    "name",
    "offer_id",
    "price",
    "original_price"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- detalle e ítems para los tres tipos; alta y eliminación de ofertas.

### Agrega una oferta a la campaña

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega una oferta a la campaña.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `app_version` (query): La guía muestra v2.
- `promotion_type` (query): Tipo de campaña indicado en cada ejemplo.
- `promotion_id` (query): Identificador de campaña.
- `offer_id` (query): Identificador de oferta.

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

- detalle e ítems para los tres tipos; alta y eliminación de ofertas.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/campanas-smart-price-matching](https://developers.mercadolibre.com.co/es_co/campanas-smart-price-matching)  
**Captura:** 2026-10-08T22:51:19.909Z
