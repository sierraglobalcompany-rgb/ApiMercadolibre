---
id: "localizacion-de-vehiculos"
title: "Localiza vehículos"
section: "Guía para vehículos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/localizacion-de-vehiculos"
source_updated_at: "21/07/2025"
captured_at: "2026-10-08T22:53:18.230Z"
sha256: "c3c81efa7f6d2d47729f2a0dad4e92f0ee3a5c4597a036d7b56e63ccc709f368"
---

# Localiza vehículos

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 21/07/2025  
**Captura:** 2026-10-08T22:53:18.230Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/localizacion-de-vehiculos](https://developers.mercadolibre.com.co/es_co/localizacion-de-vehiculos)

## Resumen

Documenta los recursos de ubicaciones clasificadas para explorar países, estados, ciudades y barrios, y explica qué identificador enviar al publicar un vehículo.

## Contenido y conceptos documentados

- Las ubicaciones se consultan jerárquicamente. En la solicitud de publicación se envía el ID del barrio; si la ciudad no tiene barrios, se envía el ID de ciudad. Al enviar un barrio, la API completa estado y ciudad.
- La lista de países incluye `id`, `name`, `locale` y `currency_id`; los recursos de ubicación incluyen las entidades padre y, para ciudades/barrios, datos geográficos. Autenticación mostrada: OAuth Bearer.

## Operaciones de API
## Operaciones de API

### GET /classified_locations/cities/{CITY_ID}

**Método:** `GET`  
**Ruta:** `/classified_locations/cities/{CITY_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta una ciudad, sus barrios y datos geográficos.

**Parámetros**

- `CITY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /classified_locations/countries

**Método:** `GET`  
**Ruta:** `/classified_locations/countries`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista países habilitados para ubicaciones clasificadas.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /classified_locations/countries/{COUNTRY_ID}

**Método:** `GET`  
**Ruta:** `/classified_locations/countries/{COUNTRY_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta datos de un país.

**Parámetros**

- `COUNTRY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /classified_locations/neighborhoods/{NEIGHBORHOOD_ID}

**Método:** `GET`  
**Ruta:** `/classified_locations/neighborhoods/{NEIGHBORHOOD_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta un barrio y su jerarquía geográfica.

**Parámetros**

- `NEIGHBORHOOD_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /classified_locations/states/{STATE_ID}

**Método:** `GET`  
**Ruta:** `/classified_locations/states/{STATE_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta un estado y sus ciudades.

**Parámetros**

- `STATE_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/localizacion-de-vehiculos](https://developers.mercadolibre.com.co/es_co/localizacion-de-vehiculos)  
**Captura:** 2026-10-08T22:53:18.230Z
