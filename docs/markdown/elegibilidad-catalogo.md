---
id: "elegibilidad-catalogo"
title: "Elegibilidad de catálogo"
section: "Guía para productos"
subsection: "Catálogo"
url: "https://developers.mercadolibre.com.co/es_co/elegibilidad-catalogo"
source_updated_at: "29/12/2025"
captured_at: "2026-10-08T22:51:36.682Z"
sha256: "2de4018b7c6e09382d86beefef8124025b08a42117f095f5bf0349e694132e4f"
---

# Elegibilidad de catálogo

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:51:36.682Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/elegibilidad-catalogo](https://developers.mercadolibre.com.co/es_co/elegibilidad-catalogo)

## Resumen

Explica cómo localizar publicaciones de catálogo, publicaciones de marketplace y artículos elegibles para catálogo, y cómo consultar la elegibilidad individual o por lote. El flujo diferencia la publicación de catálogo vinculada a catalog_product_id de la publicación estándar.

## Contenido y conceptos documentados

- El recurso de búsqueda admite catalog_listing=true o false; también permite filtrar por tags=catalog_listing_eligible y combinar otros filtros como status.
- La consulta individual devuelve id, site_id, domain_id, buy_box_eligible, status y, cuando existen, datos de variaciones. La fuente menciona estados READY_FOR_OPTIN, ALREADY_OPTED_IN y CLOSED.
- La búsqueda masiva recibe ids separados por coma. La guía lista disponibilidad en Argentina, México, Brasil, Colombia, Chile, Uruguay, Perú y Ecuador.
- Autenticación mostrada: Bearer.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar elegibilidad de publicación

**Método:** `GET`  
**Ruta:** `/items/{item_id}/catalog_listing_eligibility`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Devuelve si una publicación puede incorporarse al catálogo y sus datos relacionados.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, site_id, domain_id, buy_box_eligible, status y variaciones cuando aplica.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos de publicación con y sin variaciones.

### Consultar elegibilidad por lote

**Método:** `GET`  
**Ruta:** `/multiget/catalog_listing_eligibility`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene elegibilidad de varios ítems en una sola consulta.

**Parámetros**

- `ids` (query, opcional): ids: identificadores de ítem separados por coma

**Solicitud**

No documentado en la fuente.

**Respuesta**

Resultados de elegibilidad por ítem.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con dos ids.

### Buscar publicaciones y elegibilidad de catálogo

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items/search`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lista publicaciones del vendedor filtrando por modalidad de catálogo o etiqueta de elegibilidad.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `catalog_listing` (query, opcional): catalog_listing=true|false
- `catalog_listing` (query, opcional): tags=catalog_listing_eligible
- `status` (query, opcional): status opcional como filtro

**Solicitud**

No documentado en la fuente.

**Respuesta**

seller_id y publicaciones; la respuesta distingue marketplace y catálogo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos con catalog_listing=true, false y tags=catalog_listing_eligible.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/elegibilidad-catalogo](https://developers.mercadolibre.com.co/es_co/elegibilidad-catalogo)  
**Captura:** 2026-10-08T22:51:36.682Z
