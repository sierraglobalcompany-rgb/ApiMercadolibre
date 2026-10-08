---
id: "desarrollos-inmobiliarios"
title: "Desarrollos inmobiliarios"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/desarrollos-inmobiliarios"
source_updated_at: "03/08/2026"
captured_at: "2026-10-08T22:50:36.682Z"
sha256: "45b0a2252bc5ee86753c70487e8bead2e9ed54f3c0b26f69dac07017346d078a"
---

# Desarrollos inmobiliarios

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 03/08/2026  
**Captura:** 2026-10-08T22:50:36.682Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/desarrollos-inmobiliarios](https://developers.mercadolibre.com.co/es_co/desarrollos-inmobiliarios)

## Resumen

Explica categorías, atributos, imágenes, desarrollos con variaciones, cotizaciones y unidades multifamily.

## Contenido y conceptos documentados

- Un desarrollo requiere al menos una variación; attributes describe el proyecto y variations las unidades.
- La página indica que quotations migra a VIS Leads el 13/08/2026.

## Operaciones de API

## Conceptos y recursos asociados

### Desarrollos inmobiliarios

Explica categorías, atributos, imágenes, desarrollos con variaciones, cotizaciones y unidades multifamily.
## Operaciones de API

### Consultar atributos por categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve atributos permitidos para la categoría y variaciones.

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
    "tags.allow_variations",
    "tags.required",
    "value_type",
    "value_max_length"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

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

### Crear desarrollo inmobiliario

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea el proyecto con al menos una variation y fotos asociadas.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "title",
    "category_id",
    "price",
    "currency_id",
    "available_quantity",
    "buying_mode",
    "listing_type_id",
    "condition",
    "location",
    "description",
    "pictures",
    "attributes",
    "variations[].price",
    "variations[].attribute_combinations",
    "variations[].available_quantity",
    "variations[].picture_ids"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "id",
    "site_id",
    "category_id",
    "price",
    "attributes",
    "variations",
    "status",
    "warnings"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La moneda de las variaciones coincide con el ítem; la moneda no se repite en su precio.

### Eliminar cotización

**Método:** `PUT`  
**Ruta:** `/quotations/{quotation_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina mediante delete=true.

**Parámetros**

- `quotation_id` (path, obligatorio): ID de cotización
- `caller.type` (query, obligatorio): seller en el ejemplo

**Solicitud**

```json
{
  "fields": [
    "delete"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "HTTP 200 OK"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- {"delete":true}

### Consultar cotización

**Método:** `GET`  
**Ruta:** `/quotations/{quotation_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalle de cotización.

**Parámetros**

- `quotation_id` (path, obligatorio): ID obtenido como external_id
- `caller.type` (query, obligatorio): seller o user

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "user",
    "item",
    "disclaimer",
    "created_at"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar cotizaciones por ítem

**Método:** `GET`  
**Ruta:** `/quotations/items_ids`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Admite uno o varios IDs separados por coma.

**Parámetros**

- `query` (query, obligatorio): ID o IDs separados por coma
- `caller.type` (query, obligatorio): seller en el ejemplo

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Reporte por vendedor

**Método:** `GET`  
**Ruta:** `/quotations/report`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Retorna total de cotizaciones del seller.

**Parámetros**

- `seller.id` (query, obligatorio): ID del seller

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "seller_id",
    "total",
    "date_from",
    "date_to"
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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/desarrollos-inmobiliarios](https://developers.mercadolibre.com.co/es_co/desarrollos-inmobiliarios)  
**Captura:** 2026-10-08T22:50:36.682Z
