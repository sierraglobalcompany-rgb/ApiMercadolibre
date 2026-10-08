---
id: "dias-no-laborables"
title: "Envíos en feriados opcionales"
section: "Guía para productos"
subsection: "Mercado Envíos 2"
url: "https://developers.mercadolibre.com.co/es_co/dias-no-laborables"
source_updated_at: "24/02/2025"
captured_at: "2026-10-08T22:51:39.656Z"
sha256: "76d7e8cca0e0da8d2bfa47fe109a071e8dfbf84f580fd87033a56e545b968461"
---

# Envíos en feriados opcionales

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 24/02/2025  
**Captura:** 2026-10-08T22:51:39.656Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/dias-no-laborables](https://developers.mercadolibre.com.co/es_co/dias-no-laborables)

## Resumen

Permite consultar y configurar fechas en las que un vendedor no trabajará o desea operar en un feriado opcional. Una segunda consulta devuelve los días no laborables configurados y puede filtrarse por fecha.

## Contenido y conceptos documentados

- La configuración de fechas contiene dates con finalized, closed, enabled, checked, description y date.
- Para guardar fechas, se envían site_id y una lista dates con checked, description y date. La consulta optout devuelve los días no laborables; date es opcional.
- Autenticación mostrada: Bearer.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar feriados opcionales

**Método:** `GET`  
**Ruta:** `/shipping/seller/{seller_id}/working_day_middleend`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lista fechas habilitadas/configurables para la operación del vendedor.

**Parámetros**

- `seller_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

dates[] con finalized, closed, enabled, checked, description y date.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con dates.

### Consultar días no laborables

**Método:** `GET`  
**Ruta:** `/shipping/seller/{seller_id}/working_day_middleend/optout`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Recupera los días no laborables configurados, con filtro opcional por fecha.

**Parámetros**

- `seller_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `date` (query, opcional): date opcional: AAAA-MM-DD

**Solicitud**

No documentado en la fuente.

**Respuesta**

dates[] con fechas y descripción.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos con y sin date.

### Configurar días de trabajo

**Método:** `PUT`  
**Ruta:** `/shipping/seller/{seller_id}/working_day_middleend`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Guarda las fechas seleccionadas por el vendedor.

**Parámetros**

- `seller_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `site_id` (body, obligatorio): Identificador del sitio.
- `dates` (body, obligatorio): Fechas seleccionadas y sus descripciones.

**Solicitud**

site_id y dates[] con checked, description y date.

**Respuesta**

HTTP 200 en la actualización exitosa.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de actualización.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/dias-no-laborables](https://developers.mercadolibre.com.co/es_co/dias-no-laborables)  
**Captura:** 2026-10-08T22:51:39.656Z
