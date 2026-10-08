---
id: "envios-fulfillment"
title: "Envíos Fulfillment"
section: "Guía para productos"
subsection: "Mercado Envíos 2"
url: "https://developers.mercadolibre.com.co/es_co/envios-fulfillment"
source_updated_at: "05/10/2026"
captured_at: "2026-10-08T22:51:41.912Z"
sha256: "688ab176e238e81ef3f0c6ad84ed03c73ad8db9fc36dd7a1fb4b05c0eaf9af75"
---

# Envíos Fulfillment

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 05/10/2026  
**Captura:** 2026-10-08T22:51:41.912Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/envios-fulfillment](https://developers.mercadolibre.com.co/es_co/envios-fulfillment)

## Resumen

Guía de consultas de inventario Full: recuperar el inventory_id desde una publicación, revisar stock disponible/no disponible y buscar operaciones de stock. Full se indica disponible en Argentina, Brasil, México, Chile y Colombia.

## Contenido y conceptos documentados

- Cada variación puede tener su propio inventory_id. El stock incluye total, available_quantity, not_available_quantity, not_available_detail y external_references.
- Con include_attributes=conditions se muestran condiciones adicionales de stock no disponible, como daños o productos no soportados.
- La búsqueda de operaciones requiere seller_id e inventory_id; permite filtrar por fecha, tipo, external_references.shipment_id, paginación y scroll. El intervalo máximo documentado es 60 días y, si no se especifican fechas, el default son los últimos 15 días. La fuente informa disponibilidad de datos por últimos 12 meses.
- Errores documentados incluyen seller_product_not_found, validation_error, forbidden, unauthorized, too_many_request e internal_error; HTTP 400 por rango mayor a 60 días o filtros inválidos, 401/403 por autorización, 404 por inventario, 429 por límite y 500 interno.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar stock Full

**Método:** `GET`  
**Ruta:** `/inventories/{inventory_id}/stock/fulfillment`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene cantidades disponibles y no disponibles del inventario.

**Parámetros**

- `inventory_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `include_attributes` (query, opcional): include_attributes=conditions opcional

**Solicitud**

No documentado en la fuente.

**Respuesta**

inventory_id, total, available_quantity, not_available_quantity, not_available_detail y external_references; conditions si se solicita.

**Errores documentados**

- 400 validation_error; 401 unauthorized; 403 forbidden; 404 seller_product_not_found; 429 too_many_request; 500 internal_error.

**Ejemplos**

- Ejemplo de stock y ejemplo con include_attributes=conditions.

### Obtener inventory_id

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Consulta la publicación para recuperar inventory_id necesario para leer stock Full.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, site_id y inventory_id; en publicaciones con variaciones existe inventory_id por variación.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de publicación con inventory_id.

### Buscar operaciones de stock Full

**Método:** `GET`  
**Ruta:** `/stock/fulfillment/operations/search`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lista movimientos de inventario para vendedor e inventario con filtros y scroll.

**Parámetros**

- `seller_id` (query, obligatorio): seller_id requerido
- `inventory_id` (query, opcional): inventory_id (lista separada por coma)
- `date_from` (query, opcional): date_from/date_to opcionales
- `type` (query, opcional): type
- `external_references.shipment_id` (query, opcional): external_references.shipment_id
- `limit` (query, opcional): limit
- `sort` (query, opcional): sort
- `scroll` (query, opcional): scroll

**Solicitud**

No documentado en la fuente.

**Respuesta**

paging y results; cada resultado incluye id, seller_id, inventory_id, date_created, type, detail, result y external_references.

**Errores documentados**

- 400 validation_error por seller_id ausente, tipo/limit inválidos o rango superior a 60 días; 401 unauthorized; 403 forbidden; 429 too_many_request; 500 internal_error.

**Ejemplos**

- Ejemplos con rango de fechas, filtros type/shipment_id y scroll.

### Referencia HTTP GET /stock/fulfillment/operations/{OPERATION_ID}

**Método:** `GET`  
**Ruta:** `/stock/fulfillment/operations/{OPERATION_ID}`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /stock/fulfillment/operations/{OPERATION_ID}. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /stock/fulfillment/operations/329663159

**Método:** `GET`  
**Ruta:** `/stock/fulfillment/operations/329663159`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /stock/fulfillment/operations/329663159. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/envios-fulfillment](https://developers.mercadolibre.com.co/es_co/envios-fulfillment)  
**Captura:** 2026-10-08T22:51:41.912Z
