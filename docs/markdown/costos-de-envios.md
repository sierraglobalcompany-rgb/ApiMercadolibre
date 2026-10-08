---
id: "costos-de-envios"
title: "Costos de envío"
section: "Guía para productos"
subsection: "Mercado Envíos 2"
url: "https://developers.mercadolibre.com.co/es_co/costos-de-envios"
source_updated_at: "13/02/2026"
captured_at: "2026-10-08T22:51:25.439Z"
sha256: "c0ed3a59b590ec189b2a170e3354bdcb49d07a389e730b5c4dbb0a0dbd4dec85"
---

# Costos de envío

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/02/2026  
**Captura:** 2026-10-08T22:51:25.439Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/costos-de-envios](https://developers.mercadolibre.com.co/es_co/costos-de-envios)

## Resumen

Documenta la información de envío para publicar/editar un ítem y las opciones/costos estimados durante la compra. Distingue la obligación de envío gratis de la simulación de costo y permite cotizar el destino por código postal o ciudad.

## Contenido y conceptos documentados

- Para publicación/edición, consulta el ítem y revisa `shipping.free_shipping` y `mandatory_free_shipping`; si este último aparece, la condición es obligatoria.
- La cotización previa de costo usa `/users/{user_id}/shipping_options/free`. La fuente exige al menos uno de `item_id` o `dimensions`; acepta además precio, tipo de publicación, modalidad, condición, logística y opción de envío gratis.
- La cotización es aproximada, considera una sola unidad y aplica a ítems disponibles en Marketplace. Se describen tipos logísticos como `cross_docking`, `drop_off`, `fulfillment`, `xd_drop_off` y `self_service`.
- Para la etapa de compra, `/items/{item_id}/shipping_options` consulta opciones adaptadas al destino mediante `zip_code` o `city_to`.
- Errores documentados incluyen 400 por `seller_id` o código postal inválido, 403 por error/ítem inválido y 404 por ítem o área de cobertura no encontrada.

**Campos y respuestas:** `mandatory_free_shipping`, `free_shipping`, `dimensions`, `item_price`, `listing_type_id`, `mode`, `condition`, `logistic_type`, `zip_code` y `city_to`.

**Ejemplos documentados:** cotización por dimensiones con datos del ítem, por código postal y por ciudad.

## Operaciones de API

## Conceptos y recursos asociados

### Costos de envío

Documenta la información de envío para publicar/editar un ítem y las opciones/costos estimados durante la compra. Distingue la obligación de envío gratis de la simulación de costo y permite cotizar el destino por código postal o ciudad.

**Respuesta**

```json
{
  "fields": "`mandatory_free_shipping`, `free_shipping`, `dimensions`, `item_price`, `listing_type_id`, `mode`, `condition`, `logistic_type`, `zip_code` y `city_to`."
}
```

**Errores documentados**

- 400: seller_id sin valor o zip_code inválido.
- 403: error de API/ítem inválido.
- 404: ítem o área de cobertura no encontrada.

**Ejemplos documentados**

- cotización por dimensiones con datos del ítem, por código postal y por ciudad.
## Operaciones de API

### Consulta la configuración de envío gratis del ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la configuración de envío gratis del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: seller_id sin valor o zip_code inválido.
- 403: ítem inválido.
- 404: ítem o cobertura no encontrada.

**Ejemplos**

- cotización por dimensiones con datos del ítem, por código postal y por ciudad.

### Obtiene opciones y costos de envío para la compra con `zip_code` o `city_to`

**Método:** `GET`  
**Ruta:** `/items/{item_id}/shipping_options`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene opciones y costos de envío para la compra con `zip_code` o `city_to`.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `zip_code` (query): Destino por código postal.
- `city_to` (query): Destino por ciudad.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: seller_id sin valor o zip_code inválido.
- 403: ítem inválido.
- 404: ítem o cobertura no encontrada.

**Ejemplos**

- cotización por dimensiones con datos del ítem, por código postal y por ciudad.

### Estima el costo de envío para publicar/editar; requiere `item_id` o `dimensions`

**Método:** `GET`  
**Ruta:** `/users/{user_id}/shipping_options/free`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Estima el costo de envío para publicar/editar; requiere `item_id` o `dimensions`.

**Parámetros**

- `user_id` (path, obligatorio): Variable de ruta documentada.
- `item_id` (query): La fuente requiere item_id o dimensions.
- `dimensions` (query): La fuente requiere item_id o dimensions.
- `verbose` (query): Parámetro de detalle mostrado en la fuente.
- `item_price` (query): Precio del ítem.
- `listing_type_id` (query): Tipo de publicación.
- `mode` (query): Modo de envío.
- `condition` (query): Condición.
- `logistic_type` (query): Tipo logístico.
- `free_shipping` (query): Indica la configuración de envío gratis.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: seller_id sin valor o zip_code inválido.
- 403: ítem inválido.
- 404: ítem o cobertura no encontrada.

**Ejemplos**

- cotización por dimensiones con datos del ítem, por código postal y por ciudad.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/costos-de-envios](https://developers.mercadolibre.com.co/es_co/costos-de-envios)  
**Captura:** 2026-10-08T22:51:25.439Z
