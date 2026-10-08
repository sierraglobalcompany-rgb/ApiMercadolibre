---
id: "kits-virtuales"
title: "Kits virtuales"
section: "Guía para productos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/kits-virtuales"
source_updated_at: "17/09/2026"
captured_at: "2026-10-08T22:52:05.798Z"
sha256: "f6ccb6aed6cdebc69e4a88b26fb4aac19735a08903fa2b98f9b32833b972dded"
---

# Kits virtuales

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 17/09/2026  
**Captura:** 2026-10-08T22:52:05.798Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/kits-virtuales](https://developers.mercadolibre.com.co/es_co/kits-virtuales)

## Resumen

Describe la búsqueda de productos componentes, creación y modificación de kits virtuales, configuración de precios, consulta del precio de venta, stock y órdenes relacionadas. El kit se representa como un bundle y sus componentes conservan sus propios productos/órdenes.

## Contenido y conceptos documentados

- El flujo comienza buscando componentes y luego crea el kit con la estructura `bundle`; la fuente diferencia la creación con y sin sincronización de precios. Para cambios permitidos se actualiza el ítem del kit (por ejemplo, `price`).
- Para precios se consulta `/sale_price` y su bloque `bundle`; la automatización se gestiona con `bundle/prices_configuration`. Para una orden de un componente, `/bundle` permite recuperar las órdenes relacionadas. También se documenta stock calculado del kit.
- La estructura de búsqueda contempla `active_channels`, `main_product_id`, `added_products` y `search_filters`; `bundle.type=kit` identifica el kit y `bundle.components` contiene productos y cantidades, con el primer componente como principal. El precio de venta puede exponer `amount`, `regular_amount` y distribución por componente (`component_price`, `unit_amount`, `total_amount`). Tras publicar, componentes y cantidades no se pueden cambiar; solo son modificables campos permitidos como título/precio sujeto a configuración. La fuente muestra 400 `Updating the bundle node is not allowed`, 404 de componente inexistente y 429 por cuota excedida. También menciona `searchText`, `limit` y `context=channel_marketplace`.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /flex

La fuente menciona la ruta /flex, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/flex`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### GET /items/{ITEM_ID}/bundle/prices_configuration

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/bundle/prices_configuration`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta esa configuración.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /items/{ITEM_ID}/sale_price

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/sale_price`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el precio de venta y desglose del kit; el ejemplo usa `context=channel_marketplace`.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `context` (query, obligatorio): El ejemplo usa channel_marketplace.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "amount",
    "regular_amount",
    "bundle",
    "metadata"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /orders/{ORDER_ID}

**Método:** `GET`  
**Ruta:** `/orders/{ORDER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el detalle de una orden.

**Parámetros**

- `ORDER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /orders/{ORDER_ID}/bundle

**Método:** `GET`  
**Ruta:** `/orders/{ORDER_ID}/bundle`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera las órdenes de los componentes relacionadas con la venta del kit.

**Parámetros**

- `ORDER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "summary": "Órdenes relacionadas con los componentes del kit."
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /user-products/{USER_PRODUCT_ID}

**Método:** `GET`  
**Ruta:** `/user-products/{USER_PRODUCT_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta información de un User Product.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "bundle.type",
    "bundle.components"
  ],
  "summary": "Permite identificar el kit y sus User Products componentes."
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /user-products/{USER_PRODUCT_ID}/bundles

**Método:** `GET`  
**Ruta:** `/user-products/{USER_PRODUCT_ID}/bundles`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta los kits asociados a un User Product.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "summary": "Kits en los que está asociado el User Product consultado."
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /user-products/{USER_PRODUCT_ID}/stock

**Método:** `GET`  
**Ruta:** `/user-products/{USER_PRODUCT_ID}/stock`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el stock calculado del kit.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "summary": "Stock calculado del kit a partir del stock de sus componentes."
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /items/kits

**Método:** `POST`  
**Ruta:** `/items/kits`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea un kit virtual con sus componentes y configuración de precios.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "bundle",
    "components"
  ],
  "summary": "La solicitud crea un kit virtual con componentes."
}
```

**Respuesta**

```json
{
  "fields": [
    "id",
    "bundle",
    "components",
    "price"
  ]
}
```

**Errores documentados**

- ```json {   "code": "404",   "meaning": "UserProductComponent not found." } ```
- ```json {   "code": "429",   "meaning": "client.id over quota." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /users/{SELLER_ID}/kits/components/search

**Método:** `POST`  
**Ruta:** `/users/{SELLER_ID}/kits/components/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca productos candidatos a componente; usa `searchText` y `limit`.

**Parámetros**

- `SELLER_ID` (path, obligatorio)
- `searchText` (query, obligatorio): Texto de búsqueda de componentes.
- `limit` (query, opcional): Límite de resultados.

**Solicitud**

```json
{
  "fields": [
    "active_channels",
    "main_product_id",
    "added_products",
    "search_filters",
    "filters"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "404",   "meaning": "UserProductComponent not found." } ```
- ```json {   "code": "429",   "meaning": "client.id over quota." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### PUT /items/{ITEM_ID}

**Método:** `PUT`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica campos permitidos del ítem kit.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "price"
  ],
  "summary": "Ejemplo de modificación del precio del kit."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Updating the bundle node is not allowed." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### PUT /items/{ITEM_ID}/bundle/prices_configuration

**Método:** `PUT`  
**Ruta:** `/items/{ITEM_ID}/bundle/prices_configuration`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica la configuración de automatización de precios.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/kits-virtuales](https://developers.mercadolibre.com.co/es_co/kits-virtuales)  
**Captura:** 2026-10-08T22:52:05.798Z
