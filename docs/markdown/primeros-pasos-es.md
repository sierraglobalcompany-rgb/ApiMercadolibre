---
id: "primeros-pasos-es"
title: "Primeros pasos"
section: "Guía para productos"
subsection: "Guías de Talles"
url: "https://developers.mercadolibre.com.co/es_co/primeros-pasos-es"
source_updated_at: "14/08/2024"
captured_at: "2026-10-08T22:52:34.957Z"
sha256: "e19b6086fefa2d02c66fc058e4b6481351aefeee9637cf79b5a80ac8738ba160"
---

# Primeros pasos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 14/08/2024  
**Captura:** 2026-10-08T22:52:34.957Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/primeros-pasos-es](https://developers.mercadolibre.com.co/es_co/primeros-pasos-es)

## Resumen

Guía el flujo inicial para vincular publicaciones de moda con guías de talles: determinar dominio, consultar dominios habilitados, obtener la ficha técnica, buscar guías disponibles y reconocer qué tipo aplicar. Expone guías BRAND, STANDARD y SPECIFIC; en Uruguay, Colombia, Perú, Ecuador y Chile la fuente menciona solo SPECIFIC.

## Contenido y conceptos documentados

- El domain_id se obtiene con el predictor de categorías; los atributos marcados grid_template_required determinan los filtros requeridos para buscar una guía. La ficha técnica del dominio expone atributos grid_id y grid_row_id usados al asociar la guía al ítem.
- GET active_domains lista dominios habilitados por site. Si no hay configuración, la fuente muestra 404 config_not_found.
- POST technical_specs?section=grids consulta la estructura requerida para una guía específica usando atributos del dominio; la respuesta sirve como especificación del JSON de creación de guías personalizadas.
- POST catalog/charts/search requiere domain_id, site_id, seller_id y los atributos requeridos por la ficha; type permite SPECIFIC, STANDARD o BRAND. offset/limit paginan más de 100 registros.
- POST catalog/charts/domains/search devuelve dominios con experiencia de guía según site_id y type BRAND o STANDARD.

En los ejemplos de la fuente se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar dominios habilitados

**Método:** `GET`  
**Ruta:** `/catalog/charts/{site_id}/configurations/active_domains`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista dominios con experiencia de guía de talles activa para un sitio.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

domains[] con domain_id.

**Errores documentados**

- 404 config_not_found: el sitio no tiene dominios activados.

**Ejemplos**

- Ejemplo para MLA.

### Consultar ficha técnica del dominio

**Método:** `GET`  
**Ruta:** `/domains/{domain_id}/technical_specs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los atributos y especificación de un dominio.

**Parámetros**

- `domain_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ficha técnica del dominio; se identifican value_type grid_id/grid_row_id y tag grid_template_required.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo MLA-SNEAKERS.

### Buscar dominios por tipo de guía

**Método:** `POST`  
**Ruta:** `/catalog/charts/domains/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve dominios configurados para una guía BRAND o STANDARD.

**Parámetros**

- `site_id` (body, obligatorio): Sitio.
- `type` (body, obligatorio): BRAND o STANDARD.

**Solicitud**

site_id y type.

**Respuesta**

domains[] con domain_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos de guías por marca y estándar.

### Buscar guías de talles

**Método:** `POST`  
**Ruta:** `/catalog/charts/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca guías sugeridas para publicación por dominio, sitio, seller, atributos y tipo.

**Parámetros**

- `offset` (query, opcional): Desplazamiento de resultados.
- `limit` (query, opcional): Límite; la guía permite paginar más de cien.
- `domain_id` (body, obligatorio): Dominio.
- `site_id` (body, obligatorio): Sitio.
- `seller_id` (body, obligatorio): Vendedor.
- `attributes` (body, obligatorio): Atributos definidos por grid_template_required.
- `type` (body, opcional): Tipo de guía BRAND, STANDARD o SPECIFIC.

**Solicitud**

domain_id, site_id, seller_id y attributes[]; type opcional: SPECIFIC, STANDARD o BRAND.

**Respuesta**

paging y charts[] con id, names, domain_id, type y atributos/filas.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo BRAND Adidas para mujer en SNEAKERS.

### Consultar esquema de guía de talles

**Método:** `POST`  
**Ruta:** `/domains/{domain_id}/technical_specs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la sección grids enviando los atributos requeridos para obtener la ficha de guía.

**Parámetros**

- `domain_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `section` (query, obligatorio): Debe ser grids.
- `attributes` (body, obligatorio): Atributos necesarios para resolver la guía, por ejemplo BRAND y GENDER.

**Solicitud**

attributes[] con los atributos de ficha técnica marcados grid_template_required.

**Respuesta**

Estructura input/groups/components para la guía, que define la especificación de creación.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con dominio MLA-SNEAKERS, marca Nike y género mujer.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/primeros-pasos-es](https://developers.mercadolibre.com.co/es_co/primeros-pasos-es)  
**Captura:** 2026-10-08T22:52:34.957Z
