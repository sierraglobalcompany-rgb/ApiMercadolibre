---
id: "buscador-de-productos"
title: "Buscador de productos"
section: "Guía para productos"
subsection: "Catálogo"
url: "https://developers.mercadolibre.com.co/es_co/buscador-de-productos"
source_updated_at: "29/12/2025"
captured_at: "2026-10-08T22:51:04.446Z"
sha256: "6df5aab15cacd6f3578e4919098454dd7686d365131db9e1820452ccc59c4b64"
---

# Buscador de productos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:51:04.446Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/buscador-de-productos](https://developers.mercadolibre.com.co/es_co/buscador-de-productos)

## Resumen

Describe cómo buscar productos de catálogo para asociar una publicación con la página de producto correcta. Permite buscar por identificador universal, texto o atributos, consultar el producto y revisar elegibilidad antes de publicar.

## Contenido y conceptos documentados

- `site_id` identifica el país y es obligatorio. La guía indica disponibilidad en Argentina, México, Brasil, Colombia, Chile, Uruguay, Perú y Ecuador.
- La búsqueda admite `product_identifier` (p. ej., GTIN/EAN/UPC/ISBN) o `q`; si no se envía `q`, `product_identifier` es obligatorio. Puede acotarse con `domain_id`.
- `status=active` devuelve productos elegibles para asociar; `status=inactive` devuelve productos aún no elegibles. Si se omite, se incluyen ambos estados.
- La búsqueda POST permite precisar la consulta mediante atributos. Los ejemplos cubren part number, product ID y atributos de catálogo.
- Para validar un producto se consultan campos como `id`, `status`, `attributes`, `pictures`, `pickers`, `main_features`, `short_description`, `permalink`, `children_ids`, `parent_id` y `buy_box_winner`. En productos inactivos algunos campos pueden ser nulos o vacíos.
- `catalog_product_id` de una publicación sirve para verificar la asociación adecuada antes de publicarla en catálogo; la fuente distingue productos padre no específicos y productos hijos.

**Campos y respuestas:** `catalog_product_id`, `id`, `status`, `domain_id`, `attributes`, `pictures`, `pickers`, `main_features`, `short_description`, `permalink`, `children_ids`, `parent_id` y `buy_box_winner`.

**Ejemplos documentados:** búsquedas GET por identificador, texto y dominio; búsqueda POST por atributos; consulta GET de un producto.

## Operaciones de API

## Conceptos y recursos asociados

### Buscador de productos

Describe cómo buscar productos de catálogo para asociar una publicación con la página de producto correcta. Permite buscar por identificador universal, texto o atributos, consultar el producto y revisar elegibilidad antes de publicar.

**Respuesta**

```json
{
  "fields": "`catalog_product_id`, `id`, `status`, `domain_id`, `attributes`, `pictures`, `pickers`, `main_features`, `short_description`, `permalink`, `children_ids`, `parent_id` y `buy_box_winner`."
}
```

**Ejemplos documentados**

- búsquedas GET por identificador, texto y dominio; búsqueda POST por atributos; consulta GET de un producto.
## Operaciones de API

### La guía usa esta lectura para validar `catalog_product_id` antes de crear una publicación de catálogo

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La guía usa esta lectura para validar `catalog_product_id` antes de crear una publicación de catálogo.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- búsquedas GET por identificador, texto y dominio; búsqueda POST por atributos; consulta GET de un producto.

### Consulta los datos del producto de catálogo

**Método:** `GET`  
**Ruta:** `/products/{product_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta los datos del producto de catálogo.

**Parámetros**

- `product_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "status",
    "domain_id",
    "attributes",
    "pictures",
    "pickers",
    "main_features",
    "short_description",
    "permalink",
    "children_ids",
    "parent_id",
    "buy_box_winner"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- búsquedas GET por identificador, texto y dominio; búsqueda POST por atributos; consulta GET de un producto.

### Busca por texto o identificador universal y filtros de catálogo

**Método:** `GET`  
**Ruta:** `/products/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca por texto o identificador universal y filtros de catálogo.

**Parámetros**

- `site_id` (query, obligatorio): La guía lo indica obligatorio.
- `status` (query): active/inactive; al omitirlo se incluyen ambos.
- `q` (query)
- `product_identifier` (query): Identificador universal; requerido cuando no se envía q.
- `domain_id` (query)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "results",
    "paging",
    "id",
    "status",
    "product_identifier",
    "domain_id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- búsquedas GET por identificador, texto y dominio; búsqueda POST por atributos; consulta GET de un producto.

### Realiza una búsqueda más específica basada en atributos

**Método:** `POST`  
**Ruta:** `/products/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Realiza una búsqueda más específica basada en atributos.

**Parámetros**

- `site_id` (query, obligatorio): La guía lo indica obligatorio.
- `status` (query): active/inactive; al omitirlo se incluyen ambos.
- `q` (query)
- `product_identifier` (query): Identificador universal; requerido cuando no se envía q.
- `domain_id` (query)

**Solicitud**

```json
{
  "fields": [
    "atributos de búsqueda"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "results",
    "paging",
    "id",
    "status",
    "product_identifier",
    "domain_id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- búsquedas GET por identificador, texto y dominio; búsqueda POST por atributos; consulta GET de un producto.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/buscador-de-productos](https://developers.mercadolibre.com.co/es_co/buscador-de-productos)  
**Captura:** 2026-10-08T22:51:04.446Z
