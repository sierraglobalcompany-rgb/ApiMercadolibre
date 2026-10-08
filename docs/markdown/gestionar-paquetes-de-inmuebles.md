---
id: "gestionar-paquetes-de-inmuebles"
title: "Gestionar paquetes de inmuebles"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/gestionar-paquetes-de-inmuebles"
source_updated_at: "24/11/2025"
captured_at: "2026-10-08T22:50:39.845Z"
sha256: "03d3ca4abb2946bc682b65327c65322a366d8ed9d5ba52b733265000ad1f2c88"
---

# Gestionar paquetes de inmuebles

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 24/11/2025  
**Captura:** 2026-10-08T22:50:39.845Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestionar-paquetes-de-inmuebles](https://developers.mercadolibre.com.co/es_co/gestionar-paquetes-de-inmuebles)

## Resumen

Explica paquetes, cupos, estados y consultas de paquetes disponibles o contratados.

## Contenido y conceptos documentados

- silver habilita publicación; gold y gold_premium son destaques. package_content y status filtran consultas.

## Operaciones de API

## Conceptos y recursos asociados

### Gestionar paquetes de inmuebles

Explica paquetes, cupos, estados y consultas de paquetes disponibles o contratados.
### Ruta mencionada /items

La fuente menciona la ruta /items, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/items`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar paquetes disponibles

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/classifieds_promotion_packs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista paquetes de una categoría.

**Parámetros**

- `category_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "category_id",
    "brand",
    "description",
    "price",
    "package_type",
    "package_content",
    "duration",
    "status",
    "charge_type_id",
    "max_upgrades",
    "quota_type",
    "listing_details[].listing_type_id",
    "listing_details[].available_listings",
    "visibility"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Referencia HTTP POST /items

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /items. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

### Consultar paquetes por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/classifieds_promotion_packs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Filtra por package_content y status.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario
- `package_content` (query): publications, upgrades, developments o ALL
- `status` (query): active, paused, pending o finished; también aparece finalized

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "user_id",
    "promotion_pack_id",
    "category_id",
    "description",
    "package_type",
    "package_content",
    "status",
    "date_created",
    "date_start",
    "date_expires",
    "date_stopped",
    "last_updated",
    "engagement_type",
    "charge_id",
    "remaining_listings",
    "used_listings",
    "listing_details"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar paquetes por listing_type

**Método:** `GET`  
**Ruta:** `/users/{user_id}/classifieds_promotion_packs/{listing_type}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Filtra por tipo y categoría opcional.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario
- `listing_type` (path, opcional): silver, gold o gold_premium
- `categoryId` (query, opcional): Categoría principal

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestionar-paquetes-de-inmuebles](https://developers.mercadolibre.com.co/es_co/gestionar-paquetes-de-inmuebles)  
**Captura:** 2026-10-08T22:50:39.845Z
