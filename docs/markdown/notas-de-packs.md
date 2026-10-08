---
id: "notas-de-packs"
title: "Notas de Packs"
section: "Guía para productos"
subsection: "Gestionar ventas"
url: "https://developers.mercadolibre.com.co/es_co/notas-de-packs"
source_updated_at: "12/09/2025"
captured_at: "2026-10-08T22:52:11.192Z"
sha256: "37d2ee480f7cc2cd329ad639345d8a5bb7301bbac6d57a72905a9b8cf037d7ac"
---

# Notas de Packs

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 12/09/2025  
**Captura:** 2026-10-08T22:52:11.192Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/notas-de-packs](https://developers.mercadolibre.com.co/es_co/notas-de-packs)

## Resumen

Documenta la creación, actualización, consulta individual y búsqueda de notas informativas asociadas a un pack. Las notas registran texto y metadatos de origen/autoría para que los actores de venta y posventa compartan información contextual.

## Contenido y conceptos documentados

- `note` es el campo de texto; al crear una nota la fuente indica longitud máxima de 300 caracteres. Las respuestas incluyen `id`, `date_created`, `date_last_updated`, `note`, `seller_id` y, cuando aplica, `source_bu` y `operator_id`; la búsqueda devuelve `pack_id` y `results`.
- Los ejemplos incluyen `X-Public: true`, `Content-Type: application/json` y OAuth Bearer. Las tablas identifican `packID`, `noteID` y `accessToken` como parámetros. Errores: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### GET /packs/{PACK_ID}/notes

**Método:** `GET`  
**Ruta:** `/packs/{PACK_ID}/notes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca/lista las notas del pack.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `access_token` (query, obligatorio): Token de acceso documentado también como parámetro.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "pack_id",
    "results"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /packs/{PACK_ID}/notes/{NOTE_ID}

**Método:** `GET`  
**Ruta:** `/packs/{PACK_ID}/notes/{NOTE_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta una nota por pack e identificador.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `NOTE_ID` (path, obligatorio)
- `access_token` (query, obligatorio): Token de acceso documentado también como parámetro.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "date_created",
    "date_last_updated",
    "note",
    "source_bu",
    "seller_id",
    "operator_id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /packs/{PACK_ID}/notes

**Método:** `POST`  
**Ruta:** `/packs/{PACK_ID}/notes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una nota informativa; cuerpo `note` obligatorio, máximo 300 caracteres.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `access_token` (query, obligatorio): Token de acceso documentado también como parámetro.

**Solicitud**

```json
{
  "fields": [
    "note"
  ],
  "constraints": {
    "note": "Obligatorio; máximo 300 caracteres."
  }
}
```

**Respuesta**

```json
{
  "fields": [
    "id",
    "date_created",
    "date_last_updated",
    "note",
    "source_bu",
    "seller_id",
    "operator_id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### PUT /packs/{PACK_ID}/notes/{NOTE_ID}

**Método:** `PUT`  
**Ruta:** `/packs/{PACK_ID}/notes/{NOTE_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza el texto de una nota existente.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `NOTE_ID` (path, obligatorio)
- `access_token` (query, obligatorio): Token de acceso documentado también como parámetro.

**Solicitud**

```json
{
  "fields": [
    "note"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "id",
    "date_created",
    "date_last_updated",
    "note",
    "source_bu",
    "seller_id",
    "operator_id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/notas-de-packs](https://developers.mercadolibre.com.co/es_co/notas-de-packs)  
**Captura:** 2026-10-08T22:52:11.192Z
