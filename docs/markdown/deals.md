---
id: "deals"
title: "Campañas tradicionales"
section: "Guía para productos"
subsection: "Central de promociones"
url: "https://developers.mercadolibre.com.co/es_co/deals"
source_updated_at: "09/06/2026"
captured_at: "2026-10-08T22:51:12.858Z"
sha256: "328bba4da639f1b7a6dea700d0b9ea13079cc496ac7f85459ccec77c819141d9"
---

# Campañas tradicionales

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 09/06/2026  
**Captura:** 2026-10-08T22:51:12.858Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/deals](https://developers.mercadolibre.com.co/es_co/deals)

## Resumen

Documenta campañas tradicionales DEAL organizadas por Mercado Libre para vendedores invitados. El flujo permite consultar la campaña y precios sugeridos, aceptar la invitación con una oferta, ajustarla o retirarla.

## Contenido y conceptos documentados

- Los ítems candidatos pueden tener estado `candidate`; el filtro `status_item` admite `active` o `paused`.
- La consulta de ítems puede incluir `min_discounted_price`, `max_discounted_price` y `suggested_discounted_price`, calculados por Mercado Libre como referencia para definir el precio.
- Las ofertas pueden exponer `deal_price`, `top_deal_price`, `top_price` y `original_price`. Si `boosted_offer` es true, pueden aparecer `discount_meli_boosted_percentage`, `discount_meli_boost_amount` y `total_price_for_boosted_offer`.
- Un `deal_price` que no cumple el precio sugerido puede producir 400 `ERROR_CREDIBILITY_DISCOUNTED_PRICE`. La guía también enumera errores generales 400, 401, 403, 404, 422, 429 y 500.

**Campos y respuestas:** `promotion_id`, `promotion_type`, `status`, `deal_price`, `top_deal_price`, `top_price`, `original_price`, precios mínimo/máximo/sugerido y campos `boosted_offer`.

**Ejemplos documentados:** consulta de campaña e ítems, alta, modificación y baja de ofertas.

## Operaciones de API

## Conceptos y recursos asociados

### Campañas tradicionales

Documenta campañas tradicionales DEAL organizadas por Mercado Libre para vendedores invitados. El flujo permite consultar la campaña y precios sugeridos, aceptar la invitación con una oferta, ajustarla o retirarla.

**Respuesta**

```json
{
  "fields": "`promotion_id`, `promotion_type`, `status`, `deal_price`, `top_deal_price`, `top_price`, `original_price`, precios mínimo/máximo/sugerido y campos `boosted_offer`."
}
```

**Errores documentados**

- 400 ERROR_CREDIBILITY_DISCOUNTED_PRICE: el precio de descuento no es creíble/no cumple precio sugerido.
- 401 Unauthorized: token inválido o vencido.
- 403 Forbidden: operación sin permiso.
- 404 Not Found: recurso inexistente.
- 422 Unprocessable Entity: datos inválidos o inconsistentes.
- 429 Too Many Requests: límite excedido.
- 500 Internal Server Error: error interno.

**Ejemplos documentados**

- consulta de campaña e ítems, alta, modificación y baja de ofertas.
## Operaciones de API

### Elimina una oferta indicando tipo y campaña

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina una oferta indicando tipo y campaña.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: DEAL
- `promotion_id` (query)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de campaña e ítems, alta, modificación y baja de ofertas.

### Consulta una campaña tradicional DEAL

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta una campaña tradicional DEAL.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: DEAL
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

- consulta de campaña e ítems, alta, modificación y baja de ofertas.

### Lista ítems y precios sugeridos; admite `status_item`

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista ítems y precios sugeridos; admite `status_item`.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: DEAL
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

- consulta de campaña e ítems, alta, modificación y baja de ofertas.

### Agrega una oferta a la campaña

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega una oferta a la campaña.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: DEAL
- `promotion_id` (query)

**Solicitud**

```json
{
  "fields": [
    "price",
    "top_price",
    "original_price"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400 ERROR_CREDIBILITY_DISCOUNTED_PRICE: el precio no cumple los requisitos de precio sugerido.

**Ejemplos**

- consulta de campaña e ítems, alta, modificación y baja de ofertas.

### Modifica la oferta del ítem

**Método:** `PUT`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica la oferta del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: DEAL
- `promotion_id` (query)

**Solicitud**

```json
{
  "fields": [
    "price",
    "top_price",
    "original_price"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400 ERROR_CREDIBILITY_DISCOUNTED_PRICE: el precio no cumple los requisitos de precio sugerido.

**Ejemplos**

- consulta de campaña e ítems, alta, modificación y baja de ofertas.

### Referencia HTTP GET /seller-promotions/items/{ITEM_ID}

**Método:** `GET`  
**Ruta:** `/seller-promotions/items/{ITEM_ID}`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /seller-promotions/items/{ITEM_ID}. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/deals](https://developers.mercadolibre.com.co/es_co/deals)  
**Captura:** 2026-10-08T22:51:12.858Z
