---
id: "calidad-de-las-publicaciones-inmuebles"
title: "Calidad de las Publicaciones"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/calidad-de-las-publicaciones-inmuebles"
source_updated_at: "19/06/2026"
captured_at: "2026-10-08T22:50:29.141Z"
sha256: "449a5a6f7814f2b7d2f97ce09e7aa169152fe51f6f9c76f9eafea43da681de08"
---

# Calidad de las Publicaciones

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 19/06/2026  
**Captura:** 2026-10-08T22:50:29.141Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/calidad-de-las-publicaciones-inmuebles](https://developers.mercadolibre.com.co/es_co/calidad-de-las-publicaciones-inmuebles)

## Resumen

Explica consultas de nivel, puntuación y acciones pendientes para mejorar calidad.

## Contenido y conceptos documentados

- Los objetivos incluyen fotos, especificaciones, video y tipo de publicación; los mínimos de fotos varían por inmueble.

## Operaciones de API

## Conceptos y recursos asociados

### Calidad de las Publicaciones

Explica consultas de nivel, puntuación y acciones pendientes para mejorar calidad.
## Operaciones de API

### Consultar calidad del ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}/health`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Retorna puntaje, nivel, objetivos y progreso.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "item_id",
    "health",
    "level",
    "goals[].id",
    "goals[].name",
    "apply",
    "progress",
    "progress_max",
    "data",
    "completed"
  ]
}
```

**Errores documentados**

- ```json {   "code": "health is not supported for this item",   "meaning": "No soportado para desarrollo, inactivo o con tags de penalización." } ```

**Ejemplos**

No documentado en la fuente.

### Consultar acciones pendientes

**Método:** `GET`  
**Ruta:** `/items/{item_id}/health/actions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Retorna acciones aplicables para mejorar calidad.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "item_id",
    "health",
    "actions[].id",
    "actions[].name"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar rangos de calidad

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/health_levels`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista niveles y rangos.

**Parámetros**

- `site_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "level",
    "health_min",
    "health_max"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/calidad-de-las-publicaciones-inmuebles](https://developers.mercadolibre.com.co/es_co/calidad-de-las-publicaciones-inmuebles)  
**Captura:** 2026-10-08T22:50:29.141Z
