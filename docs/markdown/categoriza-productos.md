---
id: "categoriza-productos"
title: "Categorización de productos"
section: "Guía para productos"
subsection: "Categorización"
url: "https://developers.mercadolibre.com.co/es_co/categoriza-productos"
source_updated_at: "30/12/2025"
captured_at: "2026-10-08T22:51:18.330Z"
sha256: "ba9c2b6cd14ac87e967c22f0efdc834934607340b6ea80a0609f624ae94d61f4"
---

# Categorización de productos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:51:18.330Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/categoriza-productos](https://developers.mercadolibre.com.co/es_co/categoriza-productos)

## Resumen

Describe cómo identificar el dominio/categoría más adecuado para un producto y consultar la taxonomía de un sitio. Incluye predicción por texto, conversión de dominio a categorías y consulta de categorías y su ruta desde la raíz.

## Contenido y conceptos documentados

- El predictor requiere `site_id` y `q`; el texto debe estar en el idioma del sitio. `limit` es opcional (por defecto 4, máximo 8) y `target` puede ser `core` o `classified`.
- Para mapear un dominio de catálogo a categorías se consulta `catalog_domains/{domain_id}/categories`; para recorrer la taxonomía del sitio se obtienen sus categorías y luego el detalle por `category_id`.
- La respuesta de categorías incluye `id` y `name`; la página también muestra datos de atributos y restricciones, por ejemplo `max_description_length`.
- Un error documentado para variaciones es 400 cuando se supera el máximo permitido de 100.

**Campos y respuestas:** `site_id`, `q`, `limit`, `target`, `domain_id`, `domain_name`, `category_id`, `category_name`, `attributes`, `id`, `name` y, en los datos de categoría, `max_description_length`.

**Ejemplos documentados:** predicción de dominio para una búsqueda de celulares, categorías por dominio, categorías del sitio y detalle de categoría.

## Operaciones de API

## Conceptos y recursos asociados

### Categorización de productos

Describe cómo identificar el dominio/categoría más adecuado para un producto y consultar la taxonomía de un sitio. Incluye predicción por texto, conversión de dominio a categorías y consulta de categorías y su ruta desde la raíz.

**Respuesta**

```json
{
  "fields": "`site_id`, `q`, `limit`, `target`, `domain_id`, `domain_name`, `category_id`, `category_name`, `attributes`, `id`, `name` y, en los datos de categoría, `max_description_length`."
}
```

**Errores documentados**

- 400: las variaciones no deben superar el máximo de 100.

**Ejemplos documentados**

- predicción de dominio para una búsqueda de celulares, categorías por dominio, categorías del sitio y detalle de categoría.
## Operaciones de API

### Consulta categorías asociadas a un dominio de catálogo

**Método:** `GET`  
**Ruta:** `/catalog_domains/{domain_id}/categories`  
**Autenticación:** No documentado en la fuente.

Consulta categorías asociadas a un dominio de catálogo.

**Parámetros**

- `domain_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "name"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- predicción de dominio para una búsqueda de celulares, categorías por dominio, categorías del sitio y detalle de categoría.

### Consulta detalle de una categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalle de una categoría.

**Parámetros**

- `category_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- predicción de dominio para una búsqueda de celulares, categorías por dominio, categorías del sitio y detalle de categoría.

### Lista categorías de un sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/categories`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista categorías de un sitio.

**Parámetros**

- `site_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- predicción de dominio para una búsqueda de celulares, categorías por dominio, categorías del sitio y detalle de categoría.

### Predice dominios a partir de una búsqueda `q`; admite `limit`

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/domain_discovery/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Predice dominios a partir de una búsqueda `q`; admite `limit`.

**Parámetros**

- `site_id` (path, obligatorio): Sitio donde se realiza la publicación.
- `q` (query, obligatorio): Título a predecir; debe estar en el idioma del sitio.
- `limit` (query, opcional): Por defecto 4; máximo 8.
- `target` (query, opcional): Puede ser core o classified.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "domain_id",
    "domain_name",
    "category_id",
    "category_name",
    "attributes"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- predicción de dominio para una búsqueda de celulares, categorías por dominio, categorías del sitio y detalle de categoría.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/categoriza-productos](https://developers.mercadolibre.com.co/es_co/categoriza-productos)  
**Captura:** 2026-10-08T22:51:18.330Z
