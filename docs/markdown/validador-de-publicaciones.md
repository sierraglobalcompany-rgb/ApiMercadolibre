---
id: "validador-de-publicaciones"
title: "Validador de publicaciones"
section: "Primeros pasos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/validador-de-publicaciones"
source_updated_at: "30/12/2025"
captured_at: "2026-10-08T22:53:37.890Z"
sha256: "cd85e12f4ec406ae8341cce1d9bce5424c0a56b40e7376d30ecb6830453d558e"
---

# Validador de publicaciones

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:37.890Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/validador-de-publicaciones](https://developers.mercadolibre.com.co/es_co/validador-de-publicaciones)

## Resumen

El validador permite revisar el JSON de una publicación antes de publicarla y devuelve errores que ayudan a corregir tipos de datos y otros campos. La validación es opcional; la guía recomienda usarla durante el desarrollo, teniendo presente que no existe un entorno de preproducción.

## Contenido y conceptos documentados

Los ejemplos cubren una publicación estándar, una publicación con variaciones y un inmueble. El body puede incluir campos como `title`, `category_id`, `price`, `currency_id`, `available_quantity`, `buying_mode`, `listing_type_id`, `condition`, `description` y `pictures`; el ejemplo con variaciones agrega `variations`. La página muestra un error `400` con `message: body.invalid_field_types` cuando los tipos no coinciden (por ejemplo, precio como texto), y señala que una validación correcta responde `204 No Content`. No publica un catálogo completo de errores.

## Operaciones de API
## Operaciones de API

### Validar publicación

**Método:** `POST`  
**Ruta:** `/items/validate`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Valida el JSON de un ítem antes de publicarlo y devuelve errores de validación o 204 No Content si es válido.

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
    "description",
    "pictures"
  ],
  "note": "Son campos presentes en ejemplos; la página no declara que todos sean obligatorios."
}
```

**Respuesta**

204 No Content si la publicación pasa la validación; los ejemplos inválidos devuelven un body con message, error, status y cause.

**Errores documentados**

- ```json {   "meaning": "La respuesta de ejemplo usa message=body.invalid_field_types e informa los campos cuyo tipo recibido no coincide con el esperado.",   "code": "400" } ```

**Ejemplos**

- Ejemplos: publicación estándar, publicación con variations e inmueble.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/validador-de-publicaciones](https://developers.mercadolibre.com.co/es_co/validador-de-publicaciones)  
**Captura:** 2026-10-08T22:53:37.890Z
