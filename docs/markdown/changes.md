---
id: "changes"
title: "Cambios"
section: "Guía para productos"
subsection: "Reclamos, Devoluciones y Cambios"
url: "https://developers.mercadolibre.com.co/es_co/changes"
source_updated_at: "04/02/2026"
captured_at: "2026-10-08T22:51:08.170Z"
sha256: "d058bb5cd8c7da5af2b6f93c4468426e516168caf372cb769e242a3257a24aec"
---

# Cambios

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 04/02/2026  
**Captura:** 2026-10-08T22:51:08.170Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/changes](https://developers.mercadolibre.com.co/es_co/changes)

## Resumen

Describe la consulta de cambios asociados a una venta y el flujo de reemplazo de productos en una reclamación. La elegibilidad se comprueba en la reclamación antes de enviar la acción `allow_replace`.

## Contenido y conceptos documentados

- La guía cubre cambios para envíos Full y Cross Docking, con Cross Docking Drop Off indicado como próximo; reemplazos para Full y próximos para Cross Docking/Cross Docking Drop Off.
- El recurso de cambios relaciona la reclamación con la compra y expone identificadores, estados, ítems, fechas y datos de nuevas órdenes/envíos.
- Para ofrecer un reemplazo, consulta la reclamación y verifica que esté disponible la acción `allow_replace`; solo entonces envía el POST de resolución esperada.
- La respuesta exitosa se documenta como estado abierto. Si la acción no está permitida, la fuente muestra error 400. Estados de fallo incluyen `purchase_pay_failed` y `purchase_failed`.

**Campos y respuestas:** `claim_id`, `status`, `status_detail`, `items`, `expected_resolution`, `new_orders_ids`, `new_orders_shipments`, `date_created` y `last_updated`.

**Ejemplos documentados:** consulta GET de cambios, consulta GET de reclamación y POST de `allow_replace`, con casos de elegibilidad y rechazo.

## Operaciones de API

## Conceptos y recursos asociados

### Cambios

Describe la consulta de cambios asociados a una venta y el flujo de reemplazo de productos en una reclamación. La elegibilidad se comprueba en la reclamación antes de enviar la acción `allow_replace`.

**Respuesta**

```json
{
  "fields": "`claim_id`, `status`, `status_detail`, `items`, `expected_resolution`, `new_orders_ids`, `new_orders_shipments`, `date_created` y `last_updated`."
}
```

**Errores documentados**

- La respuesta exitosa se documenta como estado abierto. Si la acción no está permitida, la fuente muestra error 400. Estados de fallo incluyen `purchase_pay_failed` y `purchase_failed`.

**Ejemplos documentados**

- consulta GET de cambios, consulta GET de reclamación y POST de `allow_replace`, con casos de elegibilidad y rechazo.
### Ruta mencionada /claims/{CLAIM_ID}

La fuente menciona la ruta /claims/{CLAIM_ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/{CLAIM_ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Permite verificar si la reclamación ofrece la acción `allow_replace`

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/{claim_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Permite verificar si la reclamación ofrece la acción `allow_replace`.

**Parámetros**

- `claim_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta GET de cambios, consulta GET de reclamación y POST de `allow_replace`, con casos de elegibilidad y rechazo.

### Consulta cambios asociados a una reclamación

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/{claim_id}/changes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta cambios asociados a una reclamación.

**Parámetros**

- `claim_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "claim_id",
    "status",
    "status_detail",
    "items",
    "new_orders_ids",
    "new_orders_shipments",
    "date_created",
    "last_updated"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta GET de cambios, consulta GET de reclamación y POST de `allow_replace`, con casos de elegibilidad y rechazo.

### Inicia la oferta de reemplazo si está disponible

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/{claim_id}/expected-resolutions/allow-replace`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Inicia la oferta de reemplazo si está disponible.

**Parámetros**

- `claim_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: acción de reemplazo no permitida para esta reclamación.

**Ejemplos**

- consulta GET de cambios, consulta GET de reclamación y POST de `allow_replace`, con casos de elegibilidad y rechazo.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/changes](https://developers.mercadolibre.com.co/es_co/changes)  
**Captura:** 2026-10-08T22:51:08.170Z
