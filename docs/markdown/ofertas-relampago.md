---
id: "ofertas-relampago"
title: "Ofertas relámpago"
section: "Guía para productos"
subsection: "Central de promociones"
url: "https://developers.mercadolibre.com.co/es_co/ofertas-relampago"
source_updated_at: "09/06/2026"
captured_at: "2026-10-08T22:52:14.750Z"
sha256: "63e6392601b055c4494b91f5779d4f0fe96184d80cc578a66f0d28e2d61c02eb"
---

# Ofertas relámpago

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 09/06/2026  
**Captura:** 2026-10-08T22:52:14.750Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/ofertas-relampago](https://developers.mercadolibre.com.co/es_co/ofertas-relampago)

## Resumen

Documenta la consulta, incorporación y retiro de ítems en campañas Lightning. También explica el descuento adicional opcional (boost) que Mercado Libre puede aplicar sobre la oferta base.

## Contenido y conceptos documentados

- La consulta de ítems usa `promotion_type=LIGHTNING` y `app_version=v2`; la incorporación muestra `deal_price` y `stock`. La consulta por ítem puede incluir `boosted_offer`, `discount_meli_boosted_percentage`, `discount_meli_boost_amount` y `total_price_for_boosted_offer`, únicamente cuando `boosted_offer` es verdadero.
- Se describen estados de los ítems y respuestas de campaña. La respuesta de campaña incluye `id`, fechas, `status`, `price`, `original_price`, límites de precio y rango de `stock`. Las ofertas activadas no se eliminan durante el ciclo; la fuente indica pausarlas si se desea dejar de ofrecerlas. Autenticación mostrada: OAuth Bearer.

## Operaciones de API
## Operaciones de API

### DELETE /seller-promotions/items/{ITEM_ID}

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Retira el ítem de la campaña con `promotion_type=LIGHTNING`.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La fuente usa v2.
- `promotion_type` (query, obligatorio): Tipo de promoción LIGHTNING.

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

Consulta la oferta del ítem, incluidos campos de boost cuando aplica.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

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

- Ejemplo de llamada documentado en la fuente.

### GET /seller-promotions/promotions/{PROMOTION_ID}/items

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{PROMOTION_ID}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta ítems de la campaña Lightning.

**Parámetros**

- `PROMOTION_ID` (path, obligatorio)
- `promotion_type` (query, obligatorio): Tipo de campaña LIGHTNING.
- `app_version` (query, obligatorio): La fuente usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "start_date",
    "finish_date",
    "status",
    "price",
    "original_price",
    "max_discounted_price",
    "min_discounted_price",
    "stock",
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

Incorpora el ítem con `deal_price` y `stock`.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La fuente usa v2.

**Solicitud**

```json
{
  "fields": [
    "deal_price",
    "stock",
    "promotion_type"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "price",
    "original_price"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/ofertas-relampago](https://developers.mercadolibre.com.co/es_co/ofertas-relampago)  
**Captura:** 2026-10-08T22:52:14.750Z
