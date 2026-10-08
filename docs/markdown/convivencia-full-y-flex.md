---
id: "convivencia-full-y-flex"
title: "Convivencia Full/Flex (MLA y MLC)"
section: "Guía para productos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/convivencia-full-y-flex"
source_updated_at: "15/05/2026"
captured_at: "2026-10-08T22:51:24.144Z"
sha256: "4f54c9aea4aaad38a29a5a3db1f9a235490a92d37f54d222b9eedc75ffd236cf"
---

# Convivencia Full/Flex (MLA y MLC)

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 15/05/2026  
**Captura:** 2026-10-08T22:51:24.144Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/convivencia-full-y-flex](https://developers.mercadolibre.com.co/es_co/convivencia-full-y-flex)

## Resumen

Explica la lectura y modificación de stock para User Products en convivencia Full/Flex en MLA y MLC. La modificación depende de la versión de la entidad devuelta en el encabezado `x-version`.

## Contenido y conceptos documentados

- La consulta de stock tiene un límite indicado de 100 RPM.
- La lectura devuelve el encabezado `x-version`; debe enviarse en el PUT de actualización. Si falta, la fuente indica 400; si ya no es la versión más reciente, indica 409.
- La ruta `selling_address` no es válida en algunos escenarios de fulfillment/stock. Para vendedores con un único depósito tipo seller warehouse, la recomendación es operar con `seller_warehouse`.
- La guía enumera errores 400 por ausencia de inventario, falta de stock fulfillment, necesidad de inbound previo, falta de `x-version` y configuración de depósito único.

**Campos y respuestas:** identificador User Product, tipo de stock y encabezado `x-version`.

**Ejemplos documentados:** lectura de stock y actualización del stock `selling_address`.

## Operaciones de API

## Conceptos y recursos asociados

### Convivencia Full/Flex (MLA y MLC)

Explica la lectura y modificación de stock para User Products en convivencia Full/Flex en MLA y MLC. La modificación depende de la versión de la entidad devuelta en el encabezado `x-version`.

**Respuesta**

```json
{
  "fields": "identificador User Product, tipo de stock y encabezado `x-version`."
}
```

**Errores documentados**

- 400: no se puede actualizar selling_address en los escenarios descritos o falta X-Version.
- 409: la versión enviada no es la más reciente.

**Ejemplos documentados**

- lectura de stock y actualización del stock `selling_address`.
### Ruta mencionada /user-product

La fuente menciona la ruta /user-product, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/user-product`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consulta stock; la respuesta incluye `x-version`

**Método:** `GET`  
**Ruta:** `/user-products/{user_product_id}/stock`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta stock; la respuesta incluye `x-version`.

**Parámetros**

- `user_product_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "x-version"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- lectura de stock y actualización del stock `selling_address`.

### Ruta recomendada para gestionar stock de seller warehouse en la condición descrita

**Método:** `PUT`  
**Ruta:** `/user-products/{id}/stock/type/seller_warehouse`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Ruta recomendada para gestionar stock de seller warehouse en la condición descrita.

**Parámetros**

- `id` (path, obligatorio): Variable de ruta documentada.
- `x-version` (header, obligatorio): Versión devuelta por la consulta GET de stock.

**Solicitud**

```json
{
  "fields": [
    "x-version header",
    "stock"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: falta x-version o no puede modificarse ese tipo de stock.
- 409: x-version no es la versión más reciente.

**Ejemplos**

- lectura de stock y actualización del stock `selling_address`.

### Actualiza stock de dirección de venta y requiere `x-version`

**Método:** `PUT`  
**Ruta:** `/user-products/{user_product_id}/stock/type/selling_address`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza stock de dirección de venta y requiere `x-version`.

**Parámetros**

- `user_product_id` (path, obligatorio): Variable de ruta documentada.
- `x-version` (header, obligatorio): Versión devuelta por la consulta GET de stock.

**Solicitud**

```json
{
  "fields": [
    "x-version header",
    "stock"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: falta x-version o no puede modificarse ese tipo de stock.
- 409: x-version no es la versión más reciente.

**Ejemplos**

- lectura de stock y actualización del stock `selling_address`.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/convivencia-full-y-flex](https://developers.mercadolibre.com.co/es_co/convivencia-full-y-flex)  
**Captura:** 2026-10-08T22:51:24.144Z
