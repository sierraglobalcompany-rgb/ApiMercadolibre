---
id: "descripcion-de-articulos"
title: "Descripción de productos"
section: "Guía para productos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/descripcion-de-articulos"
source_updated_at: "13/03/2026"
captured_at: "2026-10-08T22:51:34.084Z"
sha256: "7d28bdaeca309add04eb1f7a5da06a8795872f1dd795ae651307b04a959af108"
---

# Descripción de productos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/03/2026  
**Captura:** 2026-10-08T22:51:34.084Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/descripcion-de-articulos](https://developers.mercadolibre.com.co/es_co/descripcion-de-articulos)

## Resumen

La guía cubre consulta y edición de la descripción de un ítem. La API trabaja con texto plano en plain_text; admite saltos de línea con \n y recomienda una descripción concisa, legible y sin duplicar información de atributos.

## Contenido y conceptos documentados

- La respuesta de consulta incluye text, plain_text, last_updated, date_created y snapshot.
- POST sirve para crear la descripción; intentar crearla cuando ya existe devuelve error. PUT actualiza la descripción y la variante api_version=2 informa la posición de caracteres no válidos.
- El campo de escritura documentado es plain_text. La fuente muestra el error HTTP 400 item.description.type.invalid cuando la descripción no es texto plano.
- Autenticación mostrada: Bearer.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar descripción

**Método:** `GET`  
**Ruta:** `/items/{item_id}/description`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene la descripción vigente del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

text, plain_text, last_updated, date_created y snapshot.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta de ejemplo con los campos de descripción.

### Crear descripción

**Método:** `POST`  
**Ruta:** `/items/{item_id}/description`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Crea una descripción para el ítem cuando todavía no tiene una.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `plain_text` (body, obligatorio): Descripción en texto plano.

**Solicitud**

plain_text con texto plano; los saltos de línea se representan con \n.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: item.description.type.invalid si no es texto plano; POST sobre una descripción existente produce error.

**Ejemplos**

- Ejemplo de plain_text.

### Actualizar descripción

**Método:** `PUT`  
**Ruta:** `/items/{item_id}/description`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Reemplaza la descripción existente; api_version=2 permite obtener detalle de posición inválida.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `api_version` (query, opcional): api_version=2 (variante mostrada por la fuente)
- `plain_text` (body, obligatorio): Descripción en texto plano.

**Solicitud**

plain_text con texto plano.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400 item.description.type.invalid; la versión 2 indica el índice de carácter inválido.

**Ejemplos**

- Ejemplo de actualización de plain_text.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/descripcion-de-articulos](https://developers.mercadolibre.com.co/es_co/descripcion-de-articulos)  
**Captura:** 2026-10-08T22:51:34.084Z
