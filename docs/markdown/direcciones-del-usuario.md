---
id: "direcciones-del-usuario"
title: "Direcciones del usuario"
section: "Recursos de la API"
subsection: "Usuarios"
url: "https://developers.mercadolibre.com.co/es_co/direcciones-del-usuario"
source_updated_at: "30/12/2025"
captured_at: "2026-10-08T22:53:45.340Z"
sha256: "7d66c607566c740520b9ee918a99b15d65a9233229603ef6c6e79f740d677c71"
---

# Direcciones del usuario

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:45.340Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/direcciones-del-usuario](https://developers.mercadolibre.com.co/es_co/direcciones-del-usuario)

## Resumen

La guía documenta la consulta de direcciones asociadas a un usuario y describe los campos de la respuesta, incluidos domicilio, ubicación, geolocalización, tipos y estado de cada dirección.

## Contenido y conceptos documentados

La respuesta de ejemplo incluye `id`, `user_id`, datos de contacto, `address_line`, calle, número, piso, apartamento y código postal; `city`, `state`, `country`, `neighborhood` y `municipality` pueden aportar identificadores y nombres. `search_location` describe la ubicación utilizada en búsquedas; `types` incluye ejemplos como `default_selling_address` y `shipping`. También se documentan `latitude`, `longitude`, `geolocation_type`, `status`, `date_created`, `normalized` y horarios especiales (`open_hours`).

## Operaciones de API
## Operaciones de API

### Consultar direcciones de usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/addresses`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve las direcciones asociadas al usuario y sus datos de ubicación, geolocalización, tipos y estado.

**Parámetros**

- `user_id` (path, obligatorio): Identificador del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con datos de dirección, city/state/country, search_location, types, coordenadas, status, date_created y open_hours.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El ejemplo usa user_id 145834937.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/direcciones-del-usuario](https://developers.mercadolibre.com.co/es_co/direcciones-del-usuario)  
**Captura:** 2026-10-08T22:53:45.340Z
