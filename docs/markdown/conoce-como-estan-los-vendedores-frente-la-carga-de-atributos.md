---
id: "conoce-como-estan-los-vendedores-frente-la-carga-de-atributos"
title: "Carga de atributos"
section: "Guía para productos"
subsection: "Métricas y Tendencias"
url: "https://developers.mercadolibre.com.co/es_co/conoce-como-estan-los-vendedores-frente-la-carga-de-atributos"
source_updated_at: "13/11/2023"
captured_at: "2026-10-08T22:51:13.773Z"
sha256: "48936a35ba06ef7300fc23f48c31d38300f38136610f1071cabe59bbef5e223d"
---

# Carga de atributos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/11/2023  
**Captura:** 2026-10-08T22:51:13.773Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/conoce-como-estan-los-vendedores-frente-la-carga-de-atributos](https://developers.mercadolibre.com.co/es_co/conoce-como-estan-los-vendedores-frente-la-carga-de-atributos)

## Resumen

Explica cómo consultar la calidad de carga de atributos de un vendedor o de una publicación. La respuesta presenta el nivel de completitud y las brechas de atributos; para una lectura por publicación se consulta su `item_id`.

## Contenido y conceptos documentados

- La guía diferencia la consulta agregada del vendedor (`seller_id`) y la consulta de completitud/calidad por publicación (`item_id`); el mensaje de validación también menciona `groups` como alternativa.
- `include_items` determina si la respuesta incluye el apartado con granularidad por ítem; su valor predeterminado es `false`. `include_incomplete_items` solicita publicaciones incompletas y `domain_id` filtra un dominio. La versión se indica mediante `v`.
- Se requiere `access_token` al llamar la API. La fuente presenta error 400 si se envía `seller_id` en el caso de consulta por ítem o si falta `item_id`; también indica 403 si `seller_id` no coincide con el vendedor asociado al token.
- La respuesta tiene datos de completitud/calidad y, cuando se solicita, desglose por ítem. Los nombres y niveles se explican en el glosario de la fuente.

**Campos y respuestas:** `seller_id`, `item_id`, `groups`, `include_items`, `include_incomplete_items`, `domain_id`, `v`, `status`, `adoption_status` y `quality_reason`; los demás campos de respuesta se describen en la página.

**Ejemplos documentados:** consulta de estado de vendedor y consulta del estado de una publicación.

## Operaciones de API

## Conceptos y recursos asociados

### Carga de atributos

Explica cómo consultar la calidad de carga de atributos de un vendedor o de una publicación. La respuesta presenta el nivel de completitud y las brechas de atributos; para una lectura por publicación se consulta su `item_id`.

**Respuesta**

```json
{
  "fields": "`seller_id`, `item_id`, `groups`, `include_items`, `include_incomplete_items`, `domain_id`, `v`, `status`, `adoption_status` y `quality_reason`; los demás campos de respuesta se describen en la página."
}
```

**Errores documentados**

- 400: falta una alternativa requerida entre seller_id, item_id o groups.
- 403: seller_id no coincide con el vendedor identificado por access_token.

**Ejemplos documentados**

- consulta de estado de vendedor y consulta del estado de una publicación.
## Operaciones de API

### Consulta calidad/carga agregada por `seller_id` o por publicación con `item_id`; admite `include_items` y `v`

**Método:** `GET`  
**Ruta:** `/catalog_quality/status`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta calidad/carga agregada por `seller_id` o por publicación con `item_id`; admite `include_items` y `v`.

**Parámetros**

- `seller_id` (query): Requerido para la consulta agregada; la fuente también acepta item_id o groups.
- `item_id` (query): Requerido para consulta por publicación; alternativa a seller_id/groups.
- `groups` (query): Alternativa mencionada por el mensaje de validación.
- `include_items` (query): Por defecto false.
- `include_incomplete_items` (query): Incluye publicaciones incompletas.
- `domain_id` (query): Filtro opcional por dominio.
- `v` (query, opcional): Versión opcional recomendada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "status",
    "adoption_status",
    "item_id",
    "quality_reason",
    "quality_level",
    "incomplete_items"
  ]
}
```

**Errores documentados**

- 400: debe proporcionarse seller_id o item_id (la fuente también menciona groups).
- 403: seller_id no coincide con el usuario del access token.

**Ejemplos**

- consulta de estado de vendedor y consulta del estado de una publicación.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/conoce-como-estan-los-vendedores-frente-la-carga-de-atributos](https://developers.mercadolibre.com.co/es_co/conoce-como-estan-los-vendedores-frente-la-carga-de-atributos)  
**Captura:** 2026-10-08T22:51:13.773Z
