---
id: "estadisticas-de-interacciones-en-inmuebles"
title: "Estadísticas de interacciones en Inmuebles"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/estadisticas-de-interacciones-en-inmuebles"
source_updated_at: "06/11/2025"
captured_at: "2026-10-08T22:50:37.756Z"
sha256: "7898e36872799d7e9bcde98dfe0c139a4aafd3d999e356bef7f88714f281b378"
---

# Estadísticas de interacciones en Inmuebles

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 06/11/2025  
**Captura:** 2026-10-08T22:50:37.756Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/estadisticas-de-interacciones-en-inmuebles](https://developers.mercadolibre.com.co/es_co/estadisticas-de-interacciones-en-inmuebles)

## Resumen

Documenta consultas de visitas, preguntas, vistas de teléfono y clics de WhatsApp por usuario o ítem.

## Contenido y conceptos documentados

- Los filtros usan date_from/date_to o last/unit/ending; algunos recursos admiten IDs separados por coma.

## Operaciones de API

## Conceptos y recursos asociados

### Estadísticas de interacciones en Inmuebles

Documenta consultas de visitas, preguntas, vistas de teléfono y clics de WhatsApp por usuario o ítem.
## Operaciones de API

### Vistas de teléfono por publicación

**Método:** `GET`  
**Ruta:** `/items/{item_id}/contacts/phone_views`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta interacciones telefónicas del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de ruta
- `date_from` (query): Fecha inicial ISO 8601
- `date_to` (query): Fecha final ISO 8601

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Vistas recientes por ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}/contacts/phone_views/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta vistas de teléfono en ventana.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de ruta
- `last` (query): Cantidad de unidades de tiempo
- `unit` (query): Unidad (day/hour)
- `ending` (query): Fecha límite ISO; omitir usa el momento de consulta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Vistas recientes por varios ítems

**Método:** `GET`  
**Ruta:** `/items/contacts/phone_views/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Acepta IDs separados por coma.

**Parámetros**

- `ids` (query): IDs de ítems separados por coma
- `last` (query): Cantidad de unidades de tiempo
- `unit` (query): Unidad (day/hour)
- `ending` (query): Fecha límite ISO; omitir usa el momento de consulta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Vistas de teléfono por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/contacts/phone_views`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta interacciones telefónicas del usuario.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de ruta
- `date_from` (query): Fecha inicial ISO 8601
- `date_to` (query): Fecha final ISO 8601

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Vistas recientes por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/contacts/phone_views/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta vistas de teléfono en ventana.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de ruta
- `last` (query): Cantidad de unidades de tiempo
- `unit` (query): Unidad (day/hour)
- `ending` (query): Fecha límite ISO; omitir usa el momento de consulta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Preguntas por publicación

**Método:** `GET`  
**Ruta:** `/items/{item_id}/contacts/questions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta preguntas del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de ruta
- `date_from` (query): Fecha inicial ISO 8601
- `date_to` (query): Fecha final ISO 8601

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Preguntas por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/contacts/questions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta preguntas del usuario.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de ruta
- `date_from` (query): Fecha inicial ISO 8601
- `date_to` (query): Fecha final ISO 8601

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Preguntas recientes por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/contacts/questions/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta preguntas en ventana.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de ruta
- `last` (query): Cantidad de unidades de tiempo
- `unit` (query): Unidad (day/hour)
- `ending` (query): Fecha límite ISO; omitir usa el momento de consulta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Visitas de publicación

**Método:** `GET`  
**Ruta:** `/visits/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve visitas del ítem.

**Parámetros**

- `ids` (query): ID del ítem

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "mapa item_id a total"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Visitas de publicación por rango

**Método:** `GET`  
**Ruta:** `/items/visits`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve visitas entre fechas.

**Parámetros**

- `ids` (query): ID del ítem
- `date_from` (query): Fecha inicial ISO 8601
- `date_to` (query): Fecha final ISO 8601

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Visitas por vendedor y rango

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items_visits`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta visitas del vendedor en intervalo.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de ruta
- `date_from` (query): Fecha inicial ISO 8601
- `date_to` (query): Fecha final ISO 8601

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Visitas recientes por vendedor

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items_visits/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta visitas en ventana.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de ruta
- `last` (query): Cantidad de unidades de tiempo
- `unit` (query): Unidad (day/hour)
- `ending` (query): Fecha límite ISO; omitir usa el momento de consulta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### WhatsApp por ítem y rango

**Método:** `GET`  
**Ruta:** `/items/{item_id}/contacts/whatsapp`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta clics en rango.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de ruta
- `date_from` (query): Fecha inicial ISO 8601
- `date_to` (query): Fecha final ISO 8601

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### WhatsApp reciente por ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}/contacts/whatsapp/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta clics en ventana.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de ruta
- `last` (query): Cantidad de unidades de tiempo
- `unit` (query): Unidad (day/hour)
- `ending` (query): Fecha límite ISO; omitir usa el momento de consulta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### WhatsApp reciente por varios ítems

**Método:** `GET`  
**Ruta:** `/items/contacts/whatsapp/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Acepta IDs separados por coma.

**Parámetros**

- `ids` (query): IDs separados por coma
- `last` (query): Cantidad de unidades de tiempo
- `unit` (query): Unidad (day/hour)
- `ending` (query): Fecha límite ISO; omitir usa el momento de consulta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### WhatsApp reciente por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/contacts/whatsapp/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta interacciones de WhatsApp en ventana.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de ruta
- `last` (query): Cantidad de unidades de tiempo
- `unit` (query): Unidad (day/hour)
- `ending` (query): Fecha límite ISO; omitir usa el momento de consulta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/estadisticas-de-interacciones-en-inmuebles](https://developers.mercadolibre.com.co/es_co/estadisticas-de-interacciones-en-inmuebles)  
**Captura:** 2026-10-08T22:50:37.756Z
