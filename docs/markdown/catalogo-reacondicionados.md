---
id: "catalogo-reacondicionados"
title: "Catálogo reacondicionados"
section: "Guía para productos"
subsection: "Catálogo"
url: "https://developers.mercadolibre.com.co/es_co/catalogo-reacondicionados"
source_updated_at: "29/12/2025"
captured_at: "2026-10-08T22:51:16.468Z"
sha256: "c912894686b7b553f54178b0126b548be404716b9fd7aea551ac86887000024f"
---

# Catálogo reacondicionados

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:51:16.468Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/catalogo-reacondicionados](https://developers.mercadolibre.com.co/es_co/catalogo-reacondicionados)

## Resumen

Documenta la publicación de productos reacondicionados en catálogo. La condición y el grado de reacondicionamiento se expresan en atributos; el grado determina la elegibilidad y la asociación con la página de producto reacondicionado.

## Contenido y conceptos documentados

- `ITEM_CONDITION` debe indicar `refurbished` (reacondicionado). El atributo obligatorio `GRADING` admite `Excelente`, `Bueno` o `Aceptable` según la fuente.
- Sin `GRADING`, el ítem no es elegible para catálogo. Tras agregarlo, se debe consultar nuevamente la elegibilidad.
- Para publicar, la guía indica enviar `catalog_product_id` (PDP tradicional) y `catalog_listing: true`; también menciona la publicación mediante `/items/catalog_listings`.
- Los campos `picker_id` y `attribute_id` identifican `GRADING` en los ejemplos.

**Campos y respuestas:** `ITEM_CONDITION`, `GRADING`, `catalog_product_id`, `catalog_listing`, `picker_id` y `attribute_id`.

**Ejemplos documentados:** valores de grado y solicitud de publicación en catálogo reacondicionado.

## Operaciones de API

## Conceptos y recursos asociados

### Catálogo reacondicionados

Documenta la publicación de productos reacondicionados en catálogo. La condición y el grado de reacondicionamiento se expresan en atributos; el grado determina la elegibilidad y la asociación con la página de producto reacondicionado.

**Respuesta**

```json
{
  "fields": "`ITEM_CONDITION`, `GRADING`, `catalog_product_id`, `catalog_listing`, `picker_id` y `attribute_id`."
}
```

**Ejemplos documentados**

- valores de grado y solicitud de publicación en catálogo reacondicionado.
### Ruta mencionada /products/search

La fuente menciona la ruta /products/search, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/products/search`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Crea el ítem de catálogo con `catalog_product_id` y `catalog_listing: true`

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** No documentado en la fuente.

Crea el ítem de catálogo con `catalog_product_id` y `catalog_listing: true`.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "ITEM_CONDITION",
    "GRADING",
    "catalog_product_id",
    "catalog_listing"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- valores de grado y solicitud de publicación en catálogo reacondicionado.

### Publica el ítem reacondicionado en catálogo

**Método:** `POST`  
**Ruta:** `/items/catalog_listings`  
**Autenticación:** No documentado en la fuente.

Publica el ítem reacondicionado en catálogo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "catalog_product_id",
    "GRADING"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "id",
    "status"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- valores de grado y solicitud de publicación en catálogo reacondicionado.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/catalogo-reacondicionados](https://developers.mercadolibre.com.co/es_co/catalogo-reacondicionados)  
**Captura:** 2026-10-08T22:51:16.468Z
