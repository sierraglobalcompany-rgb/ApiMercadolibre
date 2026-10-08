---
id: "validaciones"
title: "Validaciones"
section: "Guía para productos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/validaciones"
source_updated_at: "29/12/2025"
captured_at: "2026-10-08T22:52:58.854Z"
sha256: "66811cda096e57ac31d1754fe8a107d60d371c6ef51a8925c14aaa29ddd49197"
---

# Validaciones

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:52:58.854Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/validaciones](https://developers.mercadolibre.com.co/es_co/validaciones)

## Resumen

Describe la respuesta de validación que puede acompañar la creación de una publicación para advertir o bloquear inconsistencias de datos, moderaciones, envío, imágenes u otros dominios.

## Contenido y conceptos documentados

### Estructura y tratamiento

- El objeto de error incluye `message`, `error`, `status` y `cause[]`. Cada causa identifica `department`, `cause_id`, `type` (`warning` o `error`), `code`, `references` y `message`; los warnings informan y no bloquean, mientras que los errores requieren acción.
- La tabla de la fuente asocia códigos con causa, atributo afectado y solución. Entre los ejemplos aparecen atributos condicionales, vendedor no autorizado para marca/categoría, normalización de valores, imágenes menores a 500 píxeles y validación del GTIN/código universal.
- Para validar un identificador universal, la página referencia `/product-identifier/validator?product_identifier=$UNIVERSAL_CODE_FIELD`, pero no indica el método HTTP. El resto de parámetros, autenticación y respuestas de ese recurso: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Validaciones de publicaciones

Describe el objeto validation_error/cause usado para reportar warnings y errores de publicación; incluye department, cause_id, type, code, references y message, así como ejemplos de validación de atributos, autorización, normalización, imágenes y GTIN.

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Validation error; cause[] puede contener validaciones de tipo warning o error." } ```
### Ruta mencionada /categories/{CATEGORY_ID}/{TYPE_ID}

La fuente menciona la ruta /categories/{CATEGORY_ID}/{TYPE_ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/categories/{CATEGORY_ID}/{TYPE_ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /categories/{CATEGORY_ID}

La fuente menciona la ruta /categories/{CATEGORY_ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/categories/{CATEGORY_ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /categories/{CATEGORY_ID}/attributes

La fuente menciona la ruta /categories/{CATEGORY_ID}/attributes, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/categories/{CATEGORY_ID}/attributes`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/validaciones](https://developers.mercadolibre.com.co/es_co/validaciones)  
**Captura:** 2026-10-08T22:52:58.854Z
