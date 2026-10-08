---
id: "stock-distribuido"
title: "Stock distribuido"
section: "Guía para productos"
subsection: "User Products"
url: "https://developers.mercadolibre.com.co/es_co/stock-distribuido"
source_updated_at: "20/04/2026"
captured_at: "2026-10-08T22:52:49.284Z"
sha256: "d89c2328a63dbd213598ee42f4face57cc6b4ef5eb391eee1d7b8357439c776e"
---

# Stock distribuido

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 20/04/2026  
**Captura:** 2026-10-08T22:52:49.284Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/stock-distribuido](https://developers.mercadolibre.com.co/es_co/stock-distribuido)

## Resumen

Introduce el stock distribuido para un User Product mediante ubicaciones (`stock_locations`). Distingue stock gestionado por Mercado Libre en Full de ubicaciones controladas por el vendedor y describe la concurrencia mediante la versión del stock.

## Contenido y conceptos documentados

### Tipos de ubicación y control de versión

- `meli_facility` representa depósitos Full y no admite modificación por API; `selling_address` representa el depósito del vendedor para logísticas como cross docking, drop-off o Flex; `seller_warehouse` representa depósitos del vendedor en multi-origen.
- La respuesta de consulta contiene ubicaciones con tipo, cantidad y datos de usuario/nodo/tienda. El GET devuelve el encabezado `x-version` (entero largo); debe enviarse al modificar stock.
- Sin `x-version`, la modificación devuelve HTTP 400; con versión desactualizada, devuelve 409. Ante 409 se vuelve a consultar el stock y se usa la nueva versión.
- La fuente indica edición de `selling_address` solo en MLA/MLC cuando la experiencia está activa; `seller_warehouse` requiere que el seller esté habilitado y tenga el tag `warehouse_management`. Campos de request y errores adicionales: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /stock/type/seller_warehouse

La fuente menciona la ruta /stock/type/seller_warehouse, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/stock/type/seller_warehouse`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /stock/

La fuente menciona la ruta /stock/, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/stock/`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /stock/type/selling_address

La fuente menciona la ruta /stock/type/selling_address, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/stock/type/selling_address`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /items

La fuente menciona la ruta /items, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/items`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar stock distribuido

**Método:** `GET`  
**Ruta:** `/user-products/$USER_PRODUCT_ID/stock`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene ubicaciones de stock del User Product y su versión.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- locations[].type
- locations[].quantity
- locations[].user_id
- locations[].id
- locations[].network_node_id
- locations[].store_id

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La respuesta envía el encabezado x-version.

### Actualizar stock seller_warehouse

**Método:** `PUT`  
**Ruta:** `/user-products/$USER_PRODUCT_ID/stock/type/seller_warehouse`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica stock de la ubicación seller warehouse.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)
- `x-version` (header, obligatorio): Versión devuelta por GET /stock.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Falta x-version." } ```
- ```json {   "code": 409,   "meaning": "Versión desactualizada; consultar nuevamente el stock." } ```

**Ejemplos**

No documentado en la fuente.

### Actualizar stock selling_address

**Método:** `PUT`  
**Ruta:** `/user-products/$USER_PRODUCT_ID/stock/type/selling_address`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica stock de la ubicación del vendedor compatible con el site.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)
- `x-version` (header, obligatorio): Versión devuelta por GET /stock.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Falta el header x-version." } ```
- ```json {   "code": 409,   "meaning": "La versión no coincide; consultar de nuevo el stock." } ```

**Ejemplos**

No documentado en la fuente.

### Referencia HTTP PUT /stock/type/seller_warehouse

**Método:** `PUT`  
**Ruta:** `/stock/type/seller_warehouse`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud PUT a /stock/type/seller_warehouse. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP PUT /stock/type/selling_address

**Método:** `PUT`  
**Ruta:** `/stock/type/selling_address`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud PUT a /stock/type/selling_address. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/stock-distribuido](https://developers.mercadolibre.com.co/es_co/stock-distribuido)  
**Captura:** 2026-10-08T22:52:49.284Z
