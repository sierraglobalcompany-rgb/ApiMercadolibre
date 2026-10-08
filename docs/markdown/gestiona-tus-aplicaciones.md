---
id: "gestiona-tus-aplicaciones"
title: "Gestiona tus aplicaciones"
section: "Primeros pasos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/gestiona-tus-aplicaciones"
source_updated_at: "30/12/2025"
captured_at: "2026-10-08T22:53:33.176Z"
sha256: "15bd4654af0f3b8f95134acedeaa05cd35d1decaf8148aac54c22f5cddbcc1ed"
---

# Gestiona tus aplicaciones

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:33.176Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestiona-tus-aplicaciones](https://developers.mercadolibre.com.co/es_co/gestiona-tus-aplicaciones)

## Resumen

La guía explica cómo consultar la ficha pública y los datos privados de una aplicación, revisar los grants de usuarios, listar aplicaciones autorizadas, revocar una autorización y consultar métricas de consumo. Las llamadas de ejemplo usan un access token Bearer; para los datos privados de la aplicación se indica usar el token del usuario propietario que la creó.

## Contenido y conceptos documentados

### Grants y estado de autorizaciones

Los grants incluyen `user_id`, `app_id`, `date_created` y `scopes` (`read`, `write` y, cuando se otorgó, `offline_access`). En DevCenter se pueden visualizar y exportar. La guía distingue los estados Nuevo (grant con menos de 24 horas), Activo (uso de APIs en los últimos 90 días) e Inactivo (sin llamadas durante ese período).

### Métricas de consumo

La respuesta de consumo agrupa solicitudes por estado HTTP y presenta recursos más consumidos y recursos con errores. La fecha es opcional; sin fechas se devuelve el consumo de los últimos 15 días. Los datos se actualizan hasta el día anterior y se recomiendan consultas mensuales para reducir el riesgo de timeout.

## Operaciones de API
## Operaciones de API

### Listar aplicaciones autorizadas por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/applications`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista las aplicaciones que un usuario autorizó, incluyendo fecha de autorización y scopes.

**Parámetros**

- `user_id` (path, obligatorio): Identificador del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista con user_id, app_id, date_created y scopes.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con user_id 26317316.

### Consultar detalles de una aplicación

**Método:** `GET`  
**Ruta:** `/applications/{app_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve la ficha de la aplicación. La página indica que los datos privados deben consultarse con el token del usuario que la creó.

**Parámetros**

- `app_id` (path, obligatorio): Identificador de la aplicación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo de respuesta: id, site_id, thumbnail, url, sandbox_mode, active, max_requests_per_hour y certification_status.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra la misma ruta para consultar los datos privados con el token del propietario.

### Consultar grants de una aplicación

**Método:** `GET`  
**Ruta:** `/applications/{app_id}/grants`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista los usuarios que otorgaron permisos a la aplicación y los scopes concedidos.

**Parámetros**

- `app_id` (path, obligatorio): Identificador de la aplicación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto con paging (total, limit, offset) y grants (user_id, app_id, date_created, scopes).

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Scopes de ejemplo: read, offline_access y write.

### Consultar métricas de consumo de aplicación

**Método:** `GET`  
**Ruta:** `/applications/v1/{app_id}/consumed-applications`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve el total de requests, su distribución por status y los recursos más consumidos o con errores.

**Parámetros**

- `app_id` (path, obligatorio): Identificador de la aplicación.
- `date_start` (query, opcional): Inicio del rango de fechas; el ejemplo lo incluye.
- `date_end` (query, opcional): Fin del rango de fechas; el ejemplo lo incluye.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Incluye app_id, total_request, request_by_status, top_apis_consumed y top_apis_consumed_error.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Sin fechas, la respuesta cubre los últimos 15 días; los datos están actualizados a D-1.

### Revocar autorización de usuario

**Método:** `DELETE`  
**Ruta:** `/users/{user_id}/applications/{app_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la autorización de un usuario a una aplicación.

**Parámetros**

- `user_id` (path, obligatorio): Identificador del usuario.
- `app_id` (path, obligatorio): Identificador de la aplicación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo de respuesta con user_id, app_id y msg: Autorización eliminada.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestiona-tus-aplicaciones](https://developers.mercadolibre.com.co/es_co/gestiona-tus-aplicaciones)  
**Captura:** 2026-10-08T22:53:33.176Z
