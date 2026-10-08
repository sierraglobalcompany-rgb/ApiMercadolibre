---
id: "opiniones-sobre-producto"
title: "Opiniones de productos"
section: "Guía para productos"
subsection: "Métricas y Tendencias"
url: "https://developers.mercadolibre.com.co/es_co/opiniones-sobre-producto"
source_updated_at: "18/09/2026"
captured_at: "2026-10-08T22:52:15.922Z"
sha256: "7378915beaf907c38645ee35c6cc7feee35d816769bf604ca846dc178fcd1b0c"
---

# Opiniones de productos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 18/09/2026  
**Captura:** 2026-10-08T22:52:15.922Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/opiniones-sobre-producto](https://developers.mercadolibre.com.co/es_co/opiniones-sobre-producto)

## Resumen

Explica cómo mostrar a compradores las evaluaciones de un producto. El flujo parte del `item_id` y consulta las reseñas del ítem; para productos de catálogo puede enviarse `catalog_product_id`. La API es de solo lectura y no genera notificaciones/webhooks en tiempo real. `offset` inicia en 0 y `limit` tiene valor predeterminado 5; `catalog_product_id` filtra evaluaciones de un producto de catálogo. la respuesta de paginación contiene `total`, `limit`, `offset` y `total_pageable`. Errores documentados: 400 por ID/limit/offset inválido, 401 token inválido, 403 permisos, 404 ítem inexistente/eliminado y 429 rate limit.

## Contenido y conceptos documentados

- La fuente describe paginación y campos raíz de las evaluaciones, además de campos de uso interno y sensibles. También detalla disponibilidad por sitio, restricciones por país y casos de usuarios CBT.
- El endpoint de reseñas está disponible para los sitios MLB, MLA, MLM, MLC, MCO, MPE y MLU. El identificador del ítem puede obtenerse previamente mediante la API de ítems. Respuesta/errores no transcritos en esta ficha: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### GET /items/{ITEM_ID}

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el identificador de publicación para el flujo descrito.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### GET /reviews/item/{ITEM_ID}

**Método:** `GET`  
**Ruta:** `/reviews/item/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta evaluaciones de un ítem; admite `catalog_product_id` para producto de catálogo.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `catalog_product_id` (query, opcional): Identificador de producto de catálogo; aparece en el ejemplo opcional.
- `offset` (query, opcional): Posición inicial; predeterminado 0.
- `limit` (query, opcional): Cantidad por página; predeterminado 5.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "ID, limit u offset inválido." } ```
- ```json {   "code": "401",   "meaning": "Token inválido, expirado o mal formado." } ```
- ```json {   "code": "403",   "meaning": "El token no tiene permisos necesarios." } ```
- ```json {   "code": "404",   "meaning": "El ítem no existe, se eliminó o pertenece a otro sitio." } ```
- ```json {   "code": "429",   "meaning": "Se excedió el rate limit." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/opiniones-sobre-producto](https://developers.mercadolibre.com.co/es_co/opiniones-sobre-producto)  
**Captura:** 2026-10-08T22:52:15.922Z
