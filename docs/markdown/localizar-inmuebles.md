---
id: "localizar-inmuebles"
title: "Localizar Inmuebles"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/localizar-inmuebles"
source_updated_at: "08/11/2025"
captured_at: "2026-10-08T22:50:43.880Z"
sha256: "4a9da6eb3f59642a6ccda91a0f18fe6600e8b8a0f104c70d88a0d2c671e54e4a"
---

# Localizar Inmuebles

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 08/11/2025  
**Captura:** 2026-10-08T22:50:43.880Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/localizar-inmuebles](https://developers.mercadolibre.com.co/es_co/localizar-inmuebles)

## Resumen

La guía consulta la jerarquía de ubicaciones para seleccionar una zona y después buscar publicaciones inmobiliarias por caja geográfica y categoría. También documenta cómo ocultar y restaurar la dirección exacta de una publicación.

## Contenido y conceptos documentados

- El recorrido de datos es países → estados/provincias → ciudades → barrios/comunas. Las entidades pueden incluir identificadores, jerarquía superior, coordenadas y listas de ubicaciones hijas.
- Para búsqueda geográfica, item_location usa el formato lat:LAT1_LAT2,lon:LON1_LON2 junto con category. La fuente ilustra una búsqueda de categoría MLA1459 en el site MLA.
- PUT sobre address_line_by_reference oculta la dirección exacta; DELETE revierte el ocultamiento. La guía atribuye la decisión al gestor del inmueble por privacidad.

## Operaciones de API

## Conceptos y recursos asociados

### Jerarquía de ubicaciones inmobiliarias

La guía recorre país → estado/provincia → ciudad → barrio/comuna y usa esa información para buscar avisos por área geográfica u ocultar dirección exacta.
## Operaciones de API

### Buscar inmuebles por ubicación

**Método:** `GET`  
**Ruta:** `/sites/$COUNTRY_ID/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca avisos en un área de latitud/longitud y categoría.

**Parámetros**

- `COUNTRY_ID` (path, obligatorio): Identificador de país/site.
- `item_location` (query, obligatorio): lat:LAT1_LAT2,lon:LON1_LON2.
- `category` (query, obligatorio): ID de categoría inmobiliaria.
- `limit` (query, opcional): El ejemplo limita la respuesta.

**Solicitud**

No documentado en la fuente.

**Respuesta**

site_id, paging, results, sort, filters, available_filters y currency.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con site MLA y categoría MLA1459.

### Consultar barrio

**Método:** `GET`  
**Ruta:** `/classified_locations/neighborhoods/$NEIGHBORHOOD_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene barrio/comuna, ciudad, estado, país, subbarrios y coordenadas.

**Parámetros**

- `NEIGHBORHOOD_ID` (path, obligatorio): ID de barrio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, city, state, country, geo_information y subneighborhoods.

**Errores documentados**

- 404: barrio no encontrado.

**Ejemplos**

No documentado en la fuente.

### Consultar ciudad

**Método:** `GET`  
**Ruta:** `/classified_locations/cities/$CITY_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene ciudad, estado, país, barrios y coordenadas.

**Parámetros**

- `CITY_ID` (path, obligatorio): ID de ciudad.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, state, country, neighborhoods y geo_information.location.latitude/longitude.

**Errores documentados**

- 404: ciudad no encontrada.

**Ejemplos**

No documentado en la fuente.

### Consultar estado

**Método:** `GET`  
**Ruta:** `/classified_locations/states/$STATE_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene estado/provincia, país, ciudades y geolocalización.

**Parámetros**

- `STATE_ID` (path, obligatorio): ID del estado.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, country, geo_information, time_zone, time_zone_name y cities.

**Errores documentados**

- 404: estado no encontrado.

**Ejemplos**

No documentado en la fuente.

### Consultar país

**Método:** `GET`  
**Ruta:** `/classified_locations/countries/$COUNTRY_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene país por identificador de 2 o 3 caracteres.

**Parámetros**

- `COUNTRY_ID` (path, obligatorio): ID de país de 2 o 3 caracteres.

**Solicitud**

No documentado en la fuente.

**Respuesta**

País con id, name y datos de ubicación.

**Errores documentados**

- 404: país no encontrado.

**Ejemplos**

No documentado en la fuente.

### Listar países

**Método:** `GET`  
**Ruta:** `/classified_locations/countries`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista países disponibles para explorar ubicaciones inmobiliarias.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Arreglo de países con id, name y datos geográficos según respuesta.

**Errores documentados**

- No requiere parámetros de consulta.

**Ejemplos**

No documentado en la fuente.

### Ocultar dirección exacta

**Método:** `PUT`  
**Ruta:** `/items/$ITEM_ID/address_line_by_reference`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Oculta la dirección exacta por privacidad.

**Parámetros**

- `ITEM_ID` (path, obligatorio): ID del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Referencia HTTP GET /classified_locations/states/TUxBUENPUmFkZGIw

**Método:** `GET`  
**Ruta:** `/classified_locations/states/TUxBUENPUmFkZGIw`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /classified_locations/states/TUxBUENPUmFkZGIw. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /classified_locations/countries/AR

**Método:** `GET`  
**Ruta:** `/classified_locations/countries/AR`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /classified_locations/countries/AR. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Revertir ocultamiento de dirección

**Método:** `DELETE`  
**Ruta:** `/items/$ITEM_ID/address_line_by_reference`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina el tag de ocultamiento de dirección.

**Parámetros**

- `ITEM_ID` (path, obligatorio): ID del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/localizar-inmuebles](https://developers.mercadolibre.com.co/es_co/localizar-inmuebles)  
**Captura:** 2026-10-08T22:50:43.880Z
