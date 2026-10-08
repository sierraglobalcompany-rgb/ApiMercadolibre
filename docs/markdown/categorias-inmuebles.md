---
id: "categorias-inmuebles"
title: "Categorías"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/categorias-inmuebles"
source_updated_at: "06/11/2025"
captured_at: "2026-10-08T22:50:30.263Z"
sha256: "dcad0aef3f54e8ff0da7cef4ab5499c671d00e248326d0c686de22df703c0107"
---

# Categorías

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 06/11/2025  
**Captura:** 2026-10-08T22:50:30.263Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/categorias-inmuebles](https://developers.mercadolibre.com.co/es_co/categorias-inmuebles)

## Resumen

Describe el recorrido del árbol de categorías desde sitio hasta el subtipo final.

## Contenido y conceptos documentados

- La selección usa PROPERTY_TYPE, OPERATION y OPERATION_SUBTYPE.

## Operaciones de API

## Conceptos y recursos asociados

### Categorías

Describe el recorrido del árbol de categorías desde sitio hasta el subtipo final.
### Ruta mencionada /categories/${ID}

La fuente menciona la ruta /categories/${ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/categories/${ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve detalle y subcategorías.

**Parámetros**

- `category_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "name",
    "children_categories",
    "settings",
    "currencies",
    "max_pictures_per_item",
    "status"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Listar categorías del sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/categories`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista categorías disponibles.

**Parámetros**

- `site_id` (path, obligatorio): Identificador de la ruta

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

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/categorias-inmuebles](https://developers.mercadolibre.com.co/es_co/categorias-inmuebles)  
**Captura:** 2026-10-08T22:50:30.263Z
