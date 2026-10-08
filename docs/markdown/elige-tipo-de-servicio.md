---
id: "elige-tipo-de-servicio"
title: "Elige tipo de servicio"
section: "Guía para servicios"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/elige-tipo-de-servicio"
source_updated_at: "30/12/2025"
captured_at: "2026-10-08T22:53:06.511Z"
sha256: "bee1851482489e84c3ecc0aaf1318efe220d8718f386bb87ce5cddf2452b6b35"
---

# Elige tipo de servicio

**Área:** Guía para servicios  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:06.511Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/elige-tipo-de-servicio](https://developers.mercadolibre.com.co/es_co/elige-tipo-de-servicio)

## Resumen

Explica cómo recorrer las categorías propias de cada site y consultar atributos antes de publicar un servicio.

## Contenido y conceptos documentados

- Cada país tiene su árbol de categorías. /sites/{site_id}/categories lista IDs/nombres y /categories/{category_id} permite recorrer la ruta desde la raíz y sus children_categories.
- El detalle y /attributes ayudan a identificar los valores de publicación. La página ejemplifica Argentina (MLA) y muestra una búsqueda filtrada por ID de categoría.

## Operaciones de API
## Operaciones de API

### Consultar detalle de categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve información y categorías hijas para navegar el árbol.

**Parámetros**

- `category_id` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, picture, permalink, total_items_in_this_category, path_from_root y children_categories.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /categories/MLA1071.

### Consultar atributos de categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Muestra atributos y valores posibles de una categoría.

**Parámetros**

- `category_id` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Atributos con id, name, value_type, tags y values en el ejemplo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /categories/MLA24272/attributes.

### Listar categorías del sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/categories`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el árbol de categorías de un país para elegir dónde publicar un servicio.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de categorías con id y name.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/categories.

### Buscar publicaciones por categoría

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Ejemplifica una búsqueda de publicaciones limitada a un ID de categoría.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.
- `category` (query, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/search?category=MLA5726.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/elige-tipo-de-servicio](https://developers.mercadolibre.com.co/es_co/elige-tipo-de-servicio)  
**Captura:** 2026-10-08T22:53:06.511Z
