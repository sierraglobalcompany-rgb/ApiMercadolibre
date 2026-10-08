---
id: "calidad-de-publicaciones"
title: "Calidad de publicaciones"
section: "Guía para productos"
subsection: "Métricas y Tendencias"
url: "https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones"
source_updated_at: "31/01/2025"
captured_at: "2026-10-08T22:51:07.212Z"
sha256: "7a5b685c0e682202257e5c4515c6e9cc3a512e5bc8f498f4a99c6bd95bf00f23"
---

# Calidad de publicaciones

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 31/01/2025  
**Captura:** 2026-10-08T22:51:07.212Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones](https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones)

## Resumen

Documenta el recurso de performance para presentar calidad de publicaciones y acciones pendientes o completadas que pueden mejorarla. Incluye consultas para ítems y User Products, niveles por sitio y la transición desde `/health`.

## Contenido y conceptos documentados

- El nivel se presenta con métricas y acciones. `level_wording` varía por sitio; la guía enumera niveles básico, medio y bueno con etiquetas localizadas.
- Las respuestas incluyen datos como `entity_id`, `entity_type`, `level`, `level_wording`, `score`, `progress`, `rules`, `status`, `title`, `label`, `link`, `wordings` y `calculated_at`.
- El estado de una acción/regla es `PENDING` si requiere acciones y `COMPLETED` si ya se realizaron.
- La guía indica que `/health` será descontinuado el 7 de febrero y sustituido por `/performance`; no indica el año en esa afirmación.
- Errores documentados: 400 solicitud inválida; 401 la entidad no pertenece al vendedor del token; 403 permisos insuficientes; 404 datos de performance no generados; 500 error interno.

**Campos y respuestas:** `entity_id`, `entity_type`, `level`, `level_wording`, `score`, `progress`, `rules`, `status`, `title`, `label`, `link`, `wordings` y `calculated_at`.

**Ejemplos documentados:** consultas GET para un ítem y un User Product.

## Operaciones de API

## Conceptos y recursos asociados

### Calidad de publicaciones

Documenta el recurso de performance para presentar calidad de publicaciones y acciones pendientes o completadas que pueden mejorarla. Incluye consultas para ítems y User Products, niveles por sitio y la transición desde `/health`.

**Respuesta**

```json
{
  "fields": "`entity_id`, `entity_type`, `level`, `level_wording`, `score`, `progress`, `rules`, `status`, `title`, `label`, `link`, `wordings` y `calculated_at`."
}
```

**Errores documentados**

- Errores documentados: 400 solicitud inválida; 401 la entidad no pertenece al vendedor del token; 403 permisos insuficientes; 404 datos de performance no generados; 500 error interno.

**Ejemplos documentados**

- consultas GET para un ítem y un User Product.
## Operaciones de API

### Obtiene calidad y acciones de mejora para una publicación

**Método:** `GET`  
**Ruta:** `/item/{item_id}/performance`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene calidad y acciones de mejora para una publicación.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "entity_id",
    "entity_type",
    "level",
    "level_wording",
    "score",
    "progress",
    "rules",
    "status",
    "calculated_at"
  ]
}
```

**Errores documentados**

- 400: solicitud inválida.
- 401: la entidad no pertenece al vendedor del token.
- 403: permisos insuficientes.
- 404: performance no generado.
- 500: error interno.

**Ejemplos**

- consultas GET para un ítem y un User Product.

### Obtiene calidad y acciones asociadas al User Product

**Método:** `GET`  
**Ruta:** `/user-product/{user_product_id}/performance`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene calidad y acciones asociadas al User Product.

**Parámetros**

- `user_product_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "entity_id",
    "entity_type",
    "level",
    "level_wording",
    "score",
    "progress",
    "rules",
    "status",
    "calculated_at"
  ]
}
```

**Errores documentados**

- 400: solicitud inválida.
- 401: la entidad no pertenece al vendedor del token.
- 403: permisos insuficientes.
- 404: performance no generado.
- 500: error interno.

**Ejemplos**

- consultas GET para un ítem y un User Product.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones](https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones)  
**Captura:** 2026-10-08T22:51:07.212Z
