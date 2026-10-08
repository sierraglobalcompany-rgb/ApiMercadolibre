---
id: "campanas-con-descuento-por-cantidad"
title: "Campañas con descuento por cantidad"
section: "Guía para productos"
subsection: "Central de promociones"
url: "https://developers.mercadolibre.com.co/es_co/campanas-con-descuento-por-cantidad"
source_updated_at: "13/03/2026"
captured_at: "2026-10-08T22:51:11.035Z"
sha256: "a80d42d5c00713d41f054f67d3348a017f2103f55b55bd180defe8fbe5f6f834"
---

# Campañas con descuento por cantidad

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/03/2026  
**Captura:** 2026-10-08T22:51:11.035Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/campanas-con-descuento-por-cantidad](https://developers.mercadolibre.com.co/es_co/campanas-con-descuento-por-cantidad)

## Resumen

Documenta campañas de descuento por cantidad/volumen, donde el comprador obtiene un descuento al alcanzar una combinación de unidades compradas y pagadas. Incluye creación y administración de campañas y ofertas asociadas.

## Contenido y conceptos documentados

- La campaña define `sub_type`, cantidades de compra/pago, porcentaje de descuento, fechas y posibilidad de combinación (`allow_combination`).
- El antiguo mecanismo de descuento por volumen de Mercado Livre fue descontinuado; las campañas existentes continúan hasta su finalización.
- Los ítems aplicables comienzan como `candidate` sin `offer_id`; al agregarlos reciben un identificador de oferta.
- El filtro `status_item` admite `active` o `paused`; las ofertas usan `promotion_type=VOLUME` y `app_version=v2`.
- La fuente documenta respuestas 200 OK al actualizar o eliminar según operación; al eliminar la campaña, el cuerpo puede ser nulo.

**Campos y respuestas:** `promotion_id`, `promotion_type`, `status`, `sub_type`, `buy_quantity`, `pay_quantity`, `discount_percentage`, `allow_combination`, `start_date`, `finish_date`, `offer_id`, `price` y `original_price`.

**Ejemplos documentados:** crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.

## Operaciones de API

## Conceptos y recursos asociados

### Campañas con descuento por cantidad

Documenta campañas de descuento por cantidad/volumen, donde el comprador obtiene un descuento al alcanzar una combinación de unidades compradas y pagadas. Incluye creación y administración de campañas y ofertas asociadas.

**Respuesta**

```json
{
  "fields": "`promotion_id`, `promotion_type`, `status`, `sub_type`, `buy_quantity`, `pay_quantity`, `discount_percentage`, `allow_combination`, `start_date`, `finish_date`, `offer_id`, `price` y `original_price`."
}
```

**Ejemplos documentados**

- crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.
## Operaciones de API

### Elimina una oferta indicando tipo, campaña y oferta

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina una oferta indicando tipo, campaña y oferta.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: VOLUME
- `promotion_id` (query)
- `offer_id` (query)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.

### Elimina una campaña VOLUME

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina una campaña VOLUME.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: VOLUME
- `app_version` (query): Valor mostrado: v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.

### Consulta detalle y estado de campaña

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalle y estado de campaña.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: VOLUME
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

- crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.

### Lista ítems y ofertas; admite `status_item`

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista ítems y ofertas; admite `status_item`.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: VOLUME
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

- crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.

### Agrega un ítem candidato

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega un ítem candidato.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: VOLUME
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

- crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.

### Crea una campaña VOLUME

**Método:** `POST`  
**Ruta:** `/seller-promotions/promotions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una campaña VOLUME.

**Parámetros**

- `app_version` (query): Valor mostrado: v2

**Solicitud**

```json
{
  "fields": [
    "name",
    "sub_type",
    "buy_quantity",
    "pay_quantity",
    "discount_percentage",
    "allow_combination",
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

- crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.

### Actualiza una campaña

**Método:** `PUT`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza una campaña.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: VOLUME
- `app_version` (query): Valor mostrado: v2

**Solicitud**

```json
{
  "fields": [
    "campos editables"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/campanas-con-descuento-por-cantidad](https://developers.mercadolibre.com.co/es_co/campanas-con-descuento-por-cantidad)  
**Captura:** 2026-10-08T22:51:11.035Z
