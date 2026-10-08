---
id: "stock-multiwarehouse"
title: "Gestión de stock multiorigen / User Products"
section: "FAQs"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/stock-multiwarehouse"
source_updated_at: "14/08/2026"
captured_at: "2026-10-08T22:49:59.473Z"
sha256: "53f135d6f36c5570cce15be3cc43a88135ecf33988d9e579d160591814f57ee2"
---

# Gestión de stock multiorigen / User Products

**Área:** FAQs  
**Actualización indicada por la fuente:** 14/08/2026  
**Captura:** 2026-10-08T22:49:59.473Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/stock-multiwarehouse](https://developers.mercadolibre.com.co/es_co/stock-multiwarehouse)

## Resumen

Explica cómo leer y actualizar inventario por ubicación en cuentas con stock multiorigen.

## Contenido y conceptos documentados

- En multiorigen el stock usa User Products y seller_warehouse; available_quantity en /items puede no cambiar el inventario.
- selling_address depende del sitio; Fulfillment usa inventario meli_facility.

## Operaciones de API

## Conceptos y recursos asociados

### Gestión de stock multiorigen / User Products

Explica cómo leer y actualizar inventario por ubicación en cuentas con stock multiorigen.
### Ruta mencionada /user-products/{user_product_id}/stock/type/{seller_warehouse}

La fuente menciona la ruta /user-products/{user_product_id}/stock/type/{seller_warehouse}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/user-products/{user_product_id}/stock/type/{seller_warehouse}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Crear User Product

**Método:** `POST`  
**Ruta:** `/user-products`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La FAQ relaciona 409 con SKU/GTIN duplicados o concurrencia.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "sku",
    "gtin"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "409 Conflict",   "http_status": 409,   "meaning": "Posible SKU/GTIN duplicado o modificación concurrente." } ```

**Ejemplos**

No documentado en la fuente.

### Consultar estado de ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Verifica estado durante sincronización asíncrona.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "status"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar stock de User Product

**Método:** `GET`  
**Ruta:** `/user-products/{user_product_id}/stock`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta stock locations y tipo de ubicación.

**Parámetros**

- `user_product_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "stock_locations",
    "type"
  ]
}
```

**Errores documentados**

- ```json {   "code": "stock-locations not found",   "meaning": "Stock no inicializado." } ```

**Ejemplos**

No documentado en la fuente.

### Crear stock location

**Método:** `POST`  
**Ruta:** `/user-products/{user_product_id}/stock/type/seller_warehouse`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea/asocia location con warehouse y cantidad.

**Parámetros**

- `user_product_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "store_id",
    "network_node_id",
    "quantity",
    "stock_locations"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "validation error",   "meaning": "Locations inválidas o faltantes." } ```

**Ejemplos**

No documentado en la fuente.

### Actualizar available_quantity

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Puede responder OK sin cambiar inventario multiorigen.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "available_quantity"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- {"available_quantity":10}

### Actualizar stock selling_address

**Método:** `PUT`  
**Ruta:** `/user-products/{user_product_id}/stock/type/selling_address`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Disponible solo en ciertos sitios según la FAQ.

**Parámetros**

- `user_product_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "quantity"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "the site is blocked for modifications to the selling address",   "meaning": "El sitio no admite selling_address." } ```

**Ejemplos**

- {"quantity":10}

### Actualizar stock por seller_warehouse

**Método:** `PUT`  
**Ruta:** `/user-products/{user_product_id}/stock/type/seller_warehouse`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza cantidad por ubicación.

**Parámetros**

- `user_product_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "quantity",
    "store_id",
    "network_node_id",
    "stock_locations"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "stock-locations not found",   "meaning": "No hay stock locations inicializados." } ```

**Ejemplos**

- {"quantity":10}

### Referencia HTTP POST /user-products/{user_product_id}/stock/type/seller_

**Método:** `POST`  
**Ruta:** `/user-products/{user_product_id}/stock/type/seller_`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /user-products/{user_product_id}/stock/type/seller_. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/stock-multiwarehouse](https://developers.mercadolibre.com.co/es_co/stock-multiwarehouse)  
**Captura:** 2026-10-08T22:49:59.473Z
