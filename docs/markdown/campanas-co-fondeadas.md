---
id: "campanas-co-fondeadas"
title: "Campañas co-fondeadas"
section: "Guía para productos"
subsection: "Central de promociones"
url: "https://developers.mercadolibre.com.co/es_co/campanas-co-fondeadas"
source_updated_at: "22/01/2025"
captured_at: "2026-10-08T22:51:10.088Z"
sha256: "70e6ab735be17704fc17e355e96e1007893ca02b89bc178883d46182ace5bb63"
---

# Campañas co-fondeadas

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 22/01/2025  
**Captura:** 2026-10-08T22:51:10.088Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/campanas-co-fondeadas](https://developers.mercadolibre.com.co/es_co/campanas-co-fondeadas)

## Resumen

Explica cómo consultar y gestionar campañas cofinanciadas a las que Mercado Libre invita al vendedor. Mercado Libre aporta una parte del descuento; se consultan campañas e ítems, se incorporan ofertas y se eliminan cuando corresponda.

## Contenido y conceptos documentados

- La campaña usa `promotion_type=MARKETPLACE_CAMPAIGN` y `app_version=v2`; la respuesta contiene tipo, estado, fechas, nombre y beneficios.
- Los ítems comienzan como `candidate` y sin `offer_id`. Al incorporarlos reciben un identificador de oferta y cambia su estado.
- El filtro `status_item` admite `active` o `paused`. La fuente expone `benefits` y porcentajes de participación del vendedor y Mercado Libre.
- Los ejemplos muestran respuesta 200 OK al eliminar una oferta.

**Campos y respuestas:** `id`, `type`, `status`, `start_date`, `finish_date`, `deadline_date`, `name`, `benefits`, `seller_percentage`, `meli_percentage`, `offer_id`, `price` y `original_price`.

**Ejemplos documentados:** consulta de campaña e ítems, incorporación de un ítem y eliminación de una oferta.

## Operaciones de API

## Conceptos y recursos asociados

### Campañas co-fondeadas

Explica cómo consultar y gestionar campañas cofinanciadas a las que Mercado Libre invita al vendedor. Mercado Libre aporta una parte del descuento; se consultan campañas e ítems, se incorporan ofertas y se eliminan cuando corresponda.

**Respuesta**

```json
{
  "fields": "`id`, `type`, `status`, `start_date`, `finish_date`, `deadline_date`, `name`, `benefits`, `seller_percentage`, `meli_percentage`, `offer_id`, `price` y `original_price`."
}
```

**Ejemplos documentados**

- consulta de campaña e ítems, incorporación de un ítem y eliminación de una oferta.
## Operaciones de API

### Elimina la oferta usando tipo, ID de campaña y oferta

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la oferta usando tipo, ID de campaña y oferta.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query)
- `promotion_id` (query)
- `offer_id` (query)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de campaña e ítems, incorporación de un ítem y eliminación de una oferta.

### Consulta campaña cofinanciada y sus beneficios

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta campaña cofinanciada y sus beneficios.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: MARKETPLACE_CAMPAIGN
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

- consulta de campaña e ítems, incorporación de un ítem y eliminación de una oferta.

### Lista los ítems; admite `status_item` (`active` o `paused`)

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista los ítems; admite `status_item` (`active` o `paused`).

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: MARKETPLACE_CAMPAIGN
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

- consulta de campaña e ítems, incorporación de un ítem y eliminación de una oferta.

### Agrega un ítem candidato a la campaña

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega un ítem candidato a la campaña.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query)
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

- consulta de campaña e ítems, incorporación de un ítem y eliminación de una oferta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/campanas-co-fondeadas](https://developers.mercadolibre.com.co/es_co/campanas-co-fondeadas)  
**Captura:** 2026-10-08T22:51:10.088Z
