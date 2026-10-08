---
id: "publicacion-en-catalogo"
title: "Publicar en catálogo"
section: "Guía para productos"
subsection: "Catálogo"
url: "https://developers.mercadolibre.com.co/es_co/publicacion-en-catalogo"
source_updated_at: "02/01/2026"
captured_at: "2026-10-08T22:52:39.215Z"
sha256: "68eb4b23d82409cfc035ff6dc1a82d87701ec420b7b8457aa03c2f3bd1f86dc8"
---

# Publicar en catálogo

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 02/01/2026  
**Captura:** 2026-10-08T22:52:39.215Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/publicacion-en-catalogo](https://developers.mercadolibre.com.co/es_co/publicacion-en-catalogo)

## Resumen

Documenta tres flujos: creación directa de una publicación de catálogo, opt-in desde una publicación tradicional y opt-in automático. También explica cómo comprobar o recuperar la sincronización entre el ítem tradicional y el de catálogo.

## Contenido y conceptos documentados

### Flujos y restricciones

- Para creación directa, el `catalog_product_id` debe corresponder a un producto activo (la excepción indicada para productos inactivos se limita a Autopartes) y se envía `catalog_listing: true`. El vendedor debe verificar que la ficha del producto coincida con lo que publicará.
- El opt-in tradicional asocia el `item_id` al `catalog_product_id`; para publicaciones con variaciones puede indicarse también `variation_id`.
- La consulta y corrección de sincronización de Buy Box usan el encabezado `x-public: true`. La solicitud de sincronización envía `item_id`; se documentan HTTP 200 para éxito y 422/500 para errores.
- El tag `catalog_boost` identifica publicaciones optineadas automáticamente y puede buscarse por vendedor. No todos los dominios admiten la misma modalidad; la guía señala limitaciones para IDs inactivos y el impacto de asociar una ficha incorrecta. Parámetros y respuestas no descritos: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Consultar ejemplo de ítem optineado

**Método:** `GET`  
**Ruta:** `/items/MLM1881484643`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Ejemplo de lectura de un ítem de catálogo optineado automáticamente.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- catalog_product_id
- catalog_listing
- tags
- item_relations

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura utiliza el ID de ejemplo MLM1881484643.

### Consultar sincronización de catálogo

**Método:** `GET`  
**Ruta:** `/public/buybox/sync/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Verifica la sincronización entre el ítem tradicional y el ítem de catálogo.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `x-public` (header, obligatorio): El ejemplo usa true.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La llamada de ejemplo incluye x-public: true.

### Buscar ítems catalog_boost

**Método:** `GET`  
**Ruta:** `/users/$SELLER_ID/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca publicaciones activas del vendedor optineadas automáticamente.

**Parámetros**

- `SELLER_ID` (path, obligatorio)
- `status` (query, obligatorio): active.
- `tags` (query, obligatorio): catalog_boost.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- paging
- results

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Crear ítem directamente en catálogo

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una publicación directa asociada a un producto de catálogo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "site_id",
    "title",
    "category_id",
    "price",
    "currency_id",
    "available_quantity",
    "buying_mode",
    "listing_type_id",
    "catalog_product_id",
    "catalog_listing=true",
    "attributes",
    "pictures"
  ]
}
```

**Respuesta**

- id
- site_id
- title
- seller_id
- category_id
- price
- currency_id
- catalog_product_id
- catalog_listing
- status
- item_relations

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La ficha exige confirmar catalog_product_id y enviar catalog_listing=true.

### Opt-in de publicación tradicional

**Método:** `POST`  
**Ruta:** `/items/catalog_listings`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Asocia un ítem tradicional con un producto del catálogo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "item_id",
    "catalog_product_id",
    "variation_id (si corresponde)"
  ]
}
```

**Respuesta**

- item_id
- variation_id
- catalog_product_id
- status

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra ejemplos para publicaciones con y sin variaciones.

### Sincronizar ítem de catálogo

**Método:** `POST`  
**Ruta:** `/public/buybox/sync`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Solicita corregir sincronización enviando el identificador de ítem.

**Parámetros**

- `x-public` (header, obligatorio): El ejemplo usa true.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "item_id"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "meaning": "La página enumera HTTP 422 como error, sin detallar su significado.",   "code": 422 } ```
- ```json {   "meaning": "La página enumera HTTP 500 como error, sin detallar su significado.",   "code": 500 } ```

**Ejemplos**

- La fuente documenta 200 para éxito y 422/500 en error.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/publicacion-en-catalogo](https://developers.mercadolibre.com.co/es_co/publicacion-en-catalogo)  
**Captura:** 2026-10-08T22:52:39.215Z
