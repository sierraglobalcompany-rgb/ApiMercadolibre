---
id: "actualizacion-variacion-inmuebles"
title: "Actualización variación inmuebles"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/actualizacion-variacion-inmuebles"
source_updated_at: "08/11/2025"
captured_at: "2026-10-08T22:50:26.803Z"
sha256: "d773a78afa2a28287d537c5a234ded0fae3d55964187fe68b426f7bcc472ed65"
---

# Actualización variación inmuebles

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 08/11/2025  
**Captura:** 2026-10-08T22:50:26.803Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/actualizacion-variacion-inmuebles](https://developers.mercadolibre.com.co/es_co/actualizacion-variacion-inmuebles)

## Resumen

Explica cómo agregar, actualizar y eliminar variaciones de una publicación.

## Contenido y conceptos documentados

- attribute_combinations describe la variante; las actualizaciones usan el ID de la variación, precio e inventario.

## Operaciones de API

## Conceptos y recursos asociados

### Actualización variación inmuebles

Explica cómo agregar, actualizar y eliminar variaciones de una publicación.
## Operaciones de API

### Agregar variación

**Método:** `POST`  
**Ruta:** `/items/{item_id}/variations`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega combinación de atributos, precio e inventario.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "attribute_combinations[]",
    "price",
    "available_quantity",
    "sold_quantity"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "variación creada; HTTP 201"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Eliminar variación

**Método:** `DELETE`  
**Ruta:** `/items/{item_id}/variations/{variation_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la variación por ID.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta
- `variation_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "variaciones restantes; HTTP 200"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Actualizar variaciones

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza variaciones identificadas por id.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "variations[].id",
    "available_quantity",
    "price"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "ítem actualizado; HTTP 200"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/actualizacion-variacion-inmuebles](https://developers.mercadolibre.com.co/es_co/actualizacion-variacion-inmuebles)  
**Captura:** 2026-10-08T22:50:26.803Z
