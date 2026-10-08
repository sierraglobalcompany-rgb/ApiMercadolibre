---
id: "atributos-inmuebles"
title: "Atributos"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/atributos-inmuebles"
source_updated_at: "24/11/2025"
captured_at: "2026-10-08T22:50:27.959Z"
sha256: "4fb1dd26f7916df49f0ab69c07cd19db1bd49343ed3009e642451fa447c74787"
---

# Atributos

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 24/11/2025  
**Captura:** 2026-10-08T22:50:27.959Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/atributos-inmuebles](https://developers.mercadolibre.com.co/es_co/atributos-inmuebles)

## Resumen

Explica cómo consultar atributos por categoría e identificar campos obligatorios.

## Contenido y conceptos documentados

- tags.required=true señala atributos requeridos; se muestran COVERED_AREA, BEDROOMS, MAINTENANCE_FEE y PARKING_LOTS.

## Operaciones de API

## Conceptos y recursos asociados

### Atributos

Explica cómo consultar atributos por categoría e identificar campos obligatorios.
## Operaciones de API

### Consultar atributos

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve atributos y etiquetas de obligatoriedad.

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
    "tags.required",
    "hierarchy",
    "relevance",
    "value_type",
    "value_max_length",
    "allowed_units",
    "default_unit",
    "attribute_group_id",
    "attribute_group_name"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Crear publicación inmobiliaria

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La guía exige enviar pictures en la creación para los tipos indicados.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "category_id",
    "pictures[].source",
    "attributes"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Enviar descripción inmobiliaria

**Método:** `POST`  
**Ruta:** `/items/{item_id}/description`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Añade descripción en texto plano.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "plain_text"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- {"plain_text":"Descripción con texto plano"}

**Fuente:** [https://developers.mercadolibre.com.co/es_co/atributos-inmuebles](https://developers.mercadolibre.com.co/es_co/atributos-inmuebles)  
**Captura:** 2026-10-08T22:50:27.959Z
