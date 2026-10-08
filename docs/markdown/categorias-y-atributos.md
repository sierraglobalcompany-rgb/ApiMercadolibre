---
id: "categorias-y-atributos"
title: "Categorías y Atributos"
section: "Guía para vehículos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/categorias-y-atributos"
source_updated_at: "02/04/2025"
captured_at: "2026-10-08T22:53:12.316Z"
sha256: "c8c19d8709d4334031bb68c68347124a224c72b84ae920524ee2533f4f173995"
---

# Categorías y Atributos

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 02/04/2025  
**Captura:** 2026-10-08T22:53:12.316Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/categorias-y-atributos](https://developers.mercadolibre.com.co/es_co/categorias-y-atributos)

## Resumen

Explica cómo elegir categorías y consultar atributos para estructurar publicaciones, con ejemplos para vehículos y dominios.

## Contenido y conceptos documentados

- Cada sitio tiene su propio árbol. La página recomienda predictor; category details incluye path_from_root y children_categories, mientras attributes lista campos requeridos y valores posibles.
- domain_discovery/search sugiere dominio/categoría según q; se documenta limit de 1 a 8 y target core o classified según vertical.
- top_values entrega valores populares; limit admite hasta 1000 y la métrica enumerada es NOL_90. known_attributes permite condicionar valores relacionados.
- categories/all descarga JSON gzip; X-Content-Created y X-Content-MD5 informan fecha y checksum. catalog_domains/{domain_id}/categories relaciona un dominio con sus categorías.

## Operaciones de API
## Operaciones de API

### Convertir dominio a categorías

**Método:** `GET`  
**Ruta:** `/catalog_domains/{domain_id}/categories`  
**Autenticación:** No documentado en la fuente.

Obtiene categorías de un dominio de catálogo.

**Parámetros**

- `domain_id` (path, obligatorio): ID de dominio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de id y name.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /catalog_domains/MLB-CARS_AND_VANS/categories.

### Consultar categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}`  
**Autenticación:** No documentado en la fuente.

Devuelve detalle, camino desde la raíz y categorías hijas.

**Parámetros**

- `category_id` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con id, name, picture, permalink, total_items_in_this_category, path_from_root, children_categories y settings.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /categories/MLA1743 y /categories/MLA1744.

### Consultar atributos de categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/attributes`  
**Autenticación:** No documentado en la fuente.

Devuelve atributos específicos y valores permitidos para publicar en una categoría.

**Parámetros**

- `category_id` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Atributos con id, name, tags, hierarchy, value_type y values; BRAND aparece como catalog_required/required en el ejemplo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /categories/MLA1744/attributes.

### Listar categorías del sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/categories`  
**Autenticación:** No documentado en la fuente.

Devuelve categorías del país/sitio.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista con id y name.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/categories.

### Descargar árbol completo de categorías

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/categories/all`  
**Autenticación:** No documentado en la fuente.

Devuelve volcado del árbol de categorías codificado como gzip.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

JSON comprimido con gzip; X-Content-Created y X-Content-MD5 informan generación y suma de verificación.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/categories/all.

### Buscar dominio y categoría sugeridos

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/domain_discovery/search`  
**Autenticación:** No documentado en la fuente.

Predice dominios/categorías para un término de búsqueda.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.
- `q` (query, obligatorio): Texto del producto.
- `limit` (query, opcional): La fuente señala rango de 1 a 8.
- `target` (query, opcional): core o classified según la vertical; se describe en la página.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Resultados con domain_id, domain_name, category_id, category_name y attributes.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/domain_discovery/search?limit=1&q=fiat%20uno.

### Consultar valores populares de atributo

**Método:** `POST`  
**Ruta:** `/catalog_domains/{domain_id}/attributes/{attribute_id}/top_values`  
**Autenticación:** No documentado en la fuente.

Devuelve valores frecuentes de un atributo de dominio, opcionalmente condicionados por otros atributos conocidos.

**Parámetros**

- `domain_id` (path, obligatorio): ID de dominio.
- `attribute_id` (path, obligatorio): ID de atributo.
- `limit` (query, opcional): Máximo 1000.
- `metric_type` (query, opcional): Métrica documentada NOL_90, nuevas publicaciones de los últimos 90 días.

**Solicitud**

Opcional: known_attributes como lista de id y value_id.

**Respuesta**

Array de id, name y metric.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- POST con BRAND; otro ejemplo consulta MODEL con known_attributes de BRAND.

### Referencia HTTP POST /catalog_domains/MLA-CARS_AND_VANS/attributes/BRAND/top_values

**Método:** `POST`  
**Ruta:** `/catalog_domains/MLA-CARS_AND_VANS/attributes/BRAND/top_values`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /catalog_domains/MLA-CARS_AND_VANS/attributes/BRAND/top_values. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP POST /catalog_domains/MLA-CARS_AND_VANS/attributes/MODEL/top_values

**Método:** `POST`  
**Ruta:** `/catalog_domains/MLA-CARS_AND_VANS/attributes/MODEL/top_values`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /catalog_domains/MLA-CARS_AND_VANS/attributes/MODEL/top_values. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/categorias-y-atributos](https://developers.mercadolibre.com.co/es_co/categorias-y-atributos)  
**Captura:** 2026-10-08T22:53:12.316Z
