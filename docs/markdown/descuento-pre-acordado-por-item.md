---
id: "descuento-pre-acordado-por-item"
title: "Pre-acordado por ítem y liquidación stock Full"
section: "Guía para productos"
subsection: "Central de promociones"
url: "https://developers.mercadolibre.com.co/es_co/descuento-pre-acordado-por-item"
source_updated_at: "09/06/2026"
captured_at: "2026-10-08T22:52:23.677Z"
sha256: "97e0853dcc3c13c91c9ca7a5758f1f2d6d31669064dcb328e796dad3c380e130"
---

# Pre-acordado por ítem y liquidación stock Full

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 09/06/2026  
**Captura:** 2026-10-08T22:52:23.677Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/descuento-pre-acordado-por-item](https://developers.mercadolibre.com.co/es_co/descuento-pre-acordado-por-item)

## Resumen

Documenta campañas de descuento pre-acordado por ítem (`PRE_NEGOTIATED`) y de liquidación de stock Full (`UNHEALTHY_STOCK`), que comparten la lógica de consulta, aceptación y retiro de ofertas.

## Contenido y conceptos documentados

- Los detalles de campaña incluyen `id`, `type`, `status`, fechas, nombre y ofertas con precio original/final, estado, fechas y `benefits` (`type`, `meli_percent`, `seller_percent`). El filtro `status_item` admite `active` o `paused`.
- Puede existir boost adicional: `boosted_offer`, `discount_meli_boosted_percentage`, `discount_meli_boost_amount` y `total_price_for_boosted_offer`, solo cuando `boosted_offer=true`. La página incluye vista de vendedor, estados y parámetros de aceptación/eliminación.
- Autenticación mostrada: OAuth Bearer. Detalles no listados: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### DELETE /seller-promotions/items/{ITEM_ID}

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la oferta; se identifican `promotion_type`, `promotion_id` y `offer_id` en la consulta.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `promotion_type` (query, obligatorio): Tipo de campaña.
- `promotion_id` (query, obligatorio): Identificador de campaña.
- `offer_id` (query, obligatorio): Identificador de oferta.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /seller-promotions/items/{ITEM_ID}

**Método:** `GET`  
**Ruta:** `/seller-promotions/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la oferta del ítem; puede devolver los campos condicionales de boost.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `promotion_type` (query, obligatorio): Tipo de promoción; PRE_NEGOTIATED o UNHEALTHY_STOCK.
- `app_version` (query, obligatorio): La fuente usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "boosted_offer",
    "discount_meli_boosted_percentage",
    "discount_meli_boost_amount",
    "total_price_for_boosted_offer"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente indica consultar los campos boost a través del endpoint de ítem.

### GET /seller-promotions/promotions/{PROMOTION_ID}

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{PROMOTION_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalles de una campaña; usa `promotion_type` y `app_version=v2`.

**Parámetros**

- `PROMOTION_ID` (path, obligatorio)
- `promotion_type` (query, obligatorio): PRE_NEGOTIATED o UNHEALTHY_STOCK.
- `app_version` (query, obligatorio): La fuente usa v2.

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
    "name",
    "offers"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /seller-promotions/promotions/{PROMOTION_ID}/items

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{PROMOTION_ID}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta ofertas de la campaña; admite `promotion_type`, `app_version` y `status_item`.

**Parámetros**

- `PROMOTION_ID` (path, obligatorio)
- `promotion_type` (query, obligatorio): PRE_NEGOTIATED o UNHEALTHY_STOCK.
- `app_version` (query, obligatorio): La fuente usa v2.
- `status_item` (query, opcional): Filtro; admite active o paused.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "results",
    "id",
    "offer_id",
    "price",
    "original_price",
    "status",
    "benefits",
    "paging"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /seller-promotions/items/{ITEM_ID}

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Acepta/indica el descuento para el ítem.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/descuento-pre-acordado-por-item](https://developers.mercadolibre.com.co/es_co/descuento-pre-acordado-por-item)  
**Captura:** 2026-10-08T22:52:23.677Z
