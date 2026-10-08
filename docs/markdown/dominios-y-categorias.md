---
id: "dominios-y-categorias"
title: "Dominios y Categorías"
section: "Recursos de la API"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/dominios-y-categorias"
source_updated_at: "30/12/2025"
captured_at: "2026-10-08T22:53:46.261Z"
sha256: "d24f25b2af7d177e9ef6f228c1db698148c0d653549dc8854b36aca522cbcb6a"
---

# Dominios y Categorías

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:46.261Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/dominios-y-categorias](https://developers.mercadolibre.com.co/es_co/dominios-y-categorias)

## Resumen

La guía reúne consultas para descubrir sitios, categorías, dominios y datos de publicación. Distingue sitio (mercado, identificado por tres letras), dominio (familia de productos) y categoría (clasificación de productos dentro de un dominio). Sus ejemplos permiten obtener exposición y precios de publicación, navegar el árbol de categorías, consultar atributos y predecir una categoría a partir del artículo.

## Contenido y conceptos documentados

Las respuestas de los ejemplos incluyen IDs y nombres de sitios, categorías y dominios; detalles de categoría, exposición de la publicación, precios, atributos y packs para clasificados. El predictor de categoría utiliza `q` (y en el ejemplo, `limit`) y devuelve `domain_id`, `domain_name`, `category_id`, `category_name` y atributos sugeridos. El endpoint de especificaciones técnicas del dominio devuelve estructura de entrada y salida organizada en grupos y componentes. Las llamadas de ejemplo envían el access token en el header Bearer.

## Operaciones de API

## Conceptos y recursos asociados

### Sitios, dominios y categorías

Define los tres niveles usados por la API para organizar mercados y familias de productos.

**Respuesta**

Sitio se identifica con tres letras; el dominio agrupa familias de productos y una categoría clasifica productos similares.

**Ejemplos documentados**

- La fuente usa MLA/MLB/MLM y CELLPHONES/SNEAKERS/BICYCLES como ejemplos.
### Ruta mencionada /sites/{SITE_ID}/listing_types

La fuente menciona la ruta /sites/{SITE_ID}/listing_types, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/sites/{SITE_ID}/listing_types`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar atributos de categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene las definiciones de atributos de una categoría.

**Parámetros**

- `category_id` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de definiciones de atributos.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Listar categorías por sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/categories`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el árbol de categorías del sitio.

**Parámetros**

- `site_id` (path, obligatorio): ID del sitio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de id y name de categoría.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar detalle de categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el detalle de una categoría.

**Parámetros**

- `category_id` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

La respuesta de ejemplo contiene datos de identificación y configuración de categoría.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar exposiciones de publicación

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/listing_exposures`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene niveles de exposición y prioridades del sitio.

**Parámetros**

- `site_id` (path, obligatorio): ID del sitio, por ejemplo MLA.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Elementos con id, name, home_page, category_home_page, advertising_on_listing_page y priority_in_search.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar ficha técnica de dominio

**Método:** `GET`  
**Ruta:** `/domains/{domain_id}/technical_specs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene la estructura de especificaciones técnicas del dominio.

**Parámetros**

- `domain_id` (path, obligatorio): ID del dominio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto con input y grupos de especificaciones.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar packs de promoción de categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/classifieds_promotion_packs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene packs de promoción de clasificados para una categoría.

**Parámetros**

- `category_id` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

La respuesta de ejemplo lista packs con id, category_id, brand, description y price.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar precios de publicación

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/listing_prices`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista precios para vender y comprar en el sitio para el precio indicado.

**Parámetros**

- `site_id` (path, obligatorio): ID del sitio.
- `price` (query, obligatorio): Precio consultado; el ejemplo usa 1.

**Solicitud**

No documentado en la fuente.

**Respuesta**

La respuesta de ejemplo lista datos de precios por tipo de publicación.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Predecir dominio y categoría

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/domain_discovery/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca una categoría correspondiente a un artículo según término de búsqueda y atributos.

**Parámetros**

- `site_id` (path, obligatorio): ID del sitio.
- `q` (query, obligatorio): Término de búsqueda.
- `limit` (query, opcional): El ejemplo usa limit=1.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Resultados con domain_id, domain_name, category_id, category_name y atributos.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Referencia HTTP GET /sites/{SITE_ID}/listing_types

**Método:** `GET`  
**Ruta:** `/sites/{SITE_ID}/listing_types`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /sites/{SITE_ID}/listing_types. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Consultar sitios

**Método:** `GET`  
**Ruta:** `/sites`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista sitios de Mercado Libre y sus monedas predeterminadas.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo de elementos id, name y default_currency_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/dominios-y-categorias](https://developers.mercadolibre.com.co/es_co/dominios-y-categorias)  
**Captura:** 2026-10-08T22:53:46.261Z
