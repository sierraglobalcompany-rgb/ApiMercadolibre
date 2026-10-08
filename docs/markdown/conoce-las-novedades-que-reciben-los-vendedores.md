---
id: "conoce-las-novedades-que-reciben-los-vendedores"
title: "Comunicaciones"
section: "Recursos de la API"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/conoce-las-novedades-que-reciben-los-vendedores"
source_updated_at: "07/05/2025"
captured_at: "2026-10-08T22:53:42.622Z"
sha256: "448d493a0c1a51759a572cee7b459afab8a72648e7e08bb5b2b4bdb8c346ca1b"
---

# Comunicaciones

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 07/05/2025  
**Captura:** 2026-10-08T22:53:42.622Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/conoce-las-novedades-que-reciben-los-vendedores](https://developers.mercadolibre.com.co/es_co/conoce-las-novedades-que-reciben-los-vendedores)

## Resumen

El recurso de Comunicaciones permite consultar novedades vigentes, alertas, lanzamientos, capacitaciones y publicidades destinadas a vendedores o integradores. Cada respuesta depende del usuario cuyo access token se usa; la consulta más reciente aparece primero.

## Contenido y conceptos documentados

Para comunicaciones de vendedores se usa el token de cada vendedor; las dirigidas a la integración requieren el token del usuario propietario de la aplicación y que este haya otorgado el grant. `limit` y `offset` controlan la paginación. La respuesta contiene `paging` y `results`; cada resultado puede incluir `actions`, `id`, `label`, `description`, `highlighted`, `from_date` y `tags`. La fuente también describe agrupaciones por categoría y subcategoría y tipos de tags para áreas como envíos, eventos, facturación, países y publicaciones.

## Operaciones de API
## Operaciones de API

### Consultar comunicaciones vigentes

**Método:** `GET`  
**Ruta:** `/communications/notices`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve las comunicaciones activas para el usuario autenticado, con paginación, acciones, fechas y tags.

**Parámetros**

- `limit` (query, opcional): Límite máximo de comunicaciones.
- `offset` (query, opcional): Desplazamiento para paginar resultados.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto con paging y results; results puede incluir actions, id, label, description, highlighted, from_date y tags.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Token de vendedor para sus comunicaciones; token owner de la app para comunicaciones de la integración.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/conoce-las-novedades-que-reciben-los-vendedores](https://developers.mercadolibre.com.co/es_co/conoce-las-novedades-que-reciben-los-vendedores)  
**Captura:** 2026-10-08T22:53:42.622Z
