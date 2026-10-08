---
id: "publicaciones-requeridas-en-catalogo"
title: "Publicaciones requeridas"
section: "Guía para productos"
subsection: "Catálogo"
url: "https://developers.mercadolibre.com.co/es_co/publicaciones-requeridas-en-catalogo"
source_updated_at: "30/12/2025"
captured_at: "2026-10-08T22:52:38.143Z"
sha256: "7d7b26817bde6046ce136998b0482090613044f7abe8bb52634af4d7deae82af"
---

# Publicaciones requeridas

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:52:38.143Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/publicaciones-requeridas-en-catalogo](https://developers.mercadolibre.com.co/es_co/publicaciones-requeridas-en-catalogo)

## Resumen

Define cuándo una publicación debe migrar o publicarse en catálogo. La elegibilidad requiere el tag `catalog_listing_eligible` y un producto cuyo `listing_strategy` sea `catalog_required`; los dominios `catalog_only` restringen la publicación tradicional.

## Contenido y conceptos documentados

### Elegibilidad y flujo

- Consulta los dumps `catalog_required` y `catalog_only` del sitio antes de publicar. La fuente advierte que ignorarlos puede causar moderaciones `opt_obey` o `catalog_only_restricted`.
- La búsqueda de productos permite filtrar publicaciones activas por sitio, estrategia y texto; para una búsqueda sin caché el ejemplo agrega `skip_cache=true`.
- Los vendedores pueden listar ítems con `catalog_forewarning`, consultar la fecha asociada a una publicación y revisar infracciones de moderación por usuario.
- Las llamadas de API usan Bearer salvo las descargas de dumps, cuyos ejemplos no muestran autorización. Cuerpos, errores y algunos esquemas completos: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Dominios catalog_only

**Método:** `GET`  
**Ruta:** `/catalog/dumps/domains/$SITE_ID/catalog_only`  
**Autenticación:** No documentado en la fuente.

Descarga dominios donde solo se admite publicar en catálogo.

**Parámetros**

- `SITE_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- generation_date
- domains[].id
- domains[].date

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de dump para MLB.

### Dominios catalog_required

**Método:** `GET`  
**Ruta:** `/catalog/dumps/domains/$SITE_ID/catalog_required`  
**Autenticación:** No documentado en la fuente.

Descarga dominios con venta obligatoria en catálogo para el sitio.

**Parámetros**

- `SITE_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- generation_date
- domains[].id
- domains[].date

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de dump para MLB.

### Fecha de forewarning

**Método:** `GET`  
**Ruta:** `/items/$ITEM_ID/catalog_forewarning/date`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la fecha asociada a la advertencia de catálogo del ítem.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- date

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Infracciones del usuario

**Método:** `GET`  
**Ruta:** `/moderations/infractions/$USER_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta infracciones de moderación asociadas al usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- infractions
- date_created
- user_id
- related_item_id
- element_id
- element_type
- reason
- remedy

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Buscar productos de catálogo requeridos

**Método:** `GET`  
**Ruta:** `/products/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca productos activos que corresponden a una estrategia de publicación de catálogo.

**Parámetros**

- `status` (query, opcional): Ejemplo: active.
- `site_id` (query, obligatorio)
- `listing_strategy` (query, obligatorio): catalog_required.
- `q` (query, opcional)
- `skip_cache` (query, opcional)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- paging
- results[].id
- results[].domain_id
- results[].status
- results[].listing_strategy

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra una consulta con skip_cache=true.

### Ítems con aviso de catálogo

**Método:** `GET`  
**Ruta:** `/users/$USER_ID/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca ítems del vendedor con tag de advertencia de catálogo.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `tags` (query, obligatorio): catalog_forewarning.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- paging
- results

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/publicaciones-requeridas-en-catalogo](https://developers.mercadolibre.com.co/es_co/publicaciones-requeridas-en-catalogo)  
**Captura:** 2026-10-08T22:52:38.143Z
