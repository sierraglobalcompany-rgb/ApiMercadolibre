---
id: "flete-dinamico"
title: "Flete dinámico"
section: "Guía para productos"
subsection: "Mercado Envíos 1"
url: "https://developers.mercadolibre.com.co/es_co/flete-dinamico"
source_updated_at: "02/09/2026"
captured_at: "2026-10-08T22:51:50.332Z"
sha256: "c5e49ab6257e9a94044cdf7b3441c05869f211b32b9502776c8466708916c63e"
---

# Flete dinámico

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 02/09/2026  
**Captura:** 2026-10-08T22:51:50.332Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/flete-dinamico](https://developers.mercadolibre.com.co/es_co/flete-dinamico)

## Resumen

La documentación presenta Flete Dinámico para integradores de Mercado Envíos 1 (ME1): métricas de integración, descarga y actualización de tarifas, consulta del procesamiento y simulación de cotizaciones. El flujo de actualización es asíncrono y comunica su resultado mediante un callback.

## Contenido y conceptos documentados

### Flujo, campos y restricciones

- Las rutas usan `Bearer`; las operaciones de tarifas y cotización indican que el token debe contener `caller_id`. La consulta de métricas está restringida a integradores habilitados/validados como partner.
- Las métricas requieren `site_id`, `ts_from` y `ts_to` en ISO-8601 UTC; `seller_id` es opcional. Se listan sitios `MLA`, `MLB`, `MCO`, `MLC`, `MLM`, `MLU`, `MBO`, `MPE` y `MLV`. La respuesta agrega latencia, disponibilidad, contingencias, caché, revalidaciones y conteos/errores. La fuente atribuye 400 a parámetros/formato inválido, 401 a token o client ID inválido y 403 a cliente no autorizado o seller fuera del partner; también lista 500 y 503 para errores del partner/upstream y autenticación.
- La plantilla se descarga con `site`. La actualización usa archivo XLSX en `multipart/form-data` (máximo 7 MB), `site`, `service` y `callback_url` HTTPS. El callback no debe usar localhost ni IP privada. La fuente señala respuesta con `resource_id`, webhook y estados/errores/advertencias de procesamiento.
- Para simular, `declared_value`, ancho, alto, largo y peso deben ser positivos; las dimensiones se expresan en cm y el peso en gramos. `destination.type` acepta `zipcode` o `city`. Se documenta un límite de 50 solicitudes por minuto; los errores incluyen 400 por datos inválidos, 401 por token/client/caller inválido, 403 si ME1 no está habilitado, 404 si no existe el recurso, 429 por límite, 500 por error de cálculo/datos y 503 por autenticación o calculadora.
- Para la plantilla se documentan 400 por `site` inválido/ausente, 401 por token inválido, 404 si no existe para el sitio, 500 al leer/codificar y 503 si falla autenticación. Para carga, 400 cubre parámetros, callback o archivo inválido, 401 token/caller ausente, 403 ME1 deshabilitado, 404 vendedor inexistente, 429 límite, 500 error interno y 503 autenticación. La consulta por `resource_id` documenta 400/401/403/404/500/503 con causas de recurso, caller, habilitación ME1, vendedor o descarga/codificación. La página también establece restricciones para tablas de contingencia (rangos no duplicados, solapados, invertidos o inválidos). Campos no descritos: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Métricas de ME1

**Método:** `GET`  
**Ruta:** `/shipping/me1/sites/{site_id}/metrics`  
**Autenticación:** Bearer token; la autenticación valida acceso de partner

Consulta indicadores de desempeño de la integración ME1 para un sitio y período.

**Parámetros**

- `site_id` (path, obligatorio): Sitio habilitado; la página enumera MLA, MLB, MCO, MLC, MLM, MLU, MBO, MPE y MLV.
- `ts_from` (query, obligatorio): Inicio ISO-8601 en UTC.
- `ts_to` (query, obligatorio): Fin ISO-8601 en UTC.
- `seller_id` (query, opcional): Filtra por vendedor.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- site_id
- seller_id
- partner
- from
- to
- summary.latency_avg_ms
- summary.latency_max_ms
- summary.uptime_pct
- summary.contingency_pct
- summary.cache_pct
- summary.revalidation_pct
- summary.errors[].item
- summary.errors[].pct
- summary.totals.req_count
- summary.totals.error_count
- summary.totals.contingency_count
- summary.totals.revalidation_count
- summary.totals.cache_hit_count

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Parámetros inválidos, falta site_id o el timestamp/seller_id tiene formato inválido." } ```
- ```json {   "code": 401,   "meaning": "Token o client ID inválido." } ```
- ```json {   "code": 403,   "meaning": "Cliente no autorizado o seller_id no permitido para el partner." } ```
- ```json {   "code": 500,   "meaning": "Error del partner o del servicio upstream." } ```
- ```json {   "code": 503,   "meaning": "Servicio de autenticación no disponible." } ```

**Ejemplos**

- Ejemplo de consulta mensual para MLB, con y sin seller_id.

### Consultar procesamiento de tarifas

**Método:** `GET`  
**Ruta:** `/shipping/me1/v1/tariff/{resource_id}`  
**Autenticación:** Bearer token; el token debe identificar caller_id

Consulta el estado y contenido de una carga de tarifas por su identificador de recurso.

**Parámetros**

- `resource_id` (path, obligatorio): Identificador UUID del recurso.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- resource_id
- status
- filename
- content (Base64)
- encoding
- mimetype

**Errores documentados**

- ```json {   "code": 400,   "meaning": "resource_id ausente o formato de caller_id inválido." } ```
- ```json {   "code": 401,   "meaning": "Token, client ID o caller_id inválido/ausente." } ```
- ```json {   "code": 403,   "meaning": "El vendedor no tiene ME1 habilitado." } ```
- ```json {   "code": 404,   "meaning": "No se encontró el tarifario para resource_id." } ```
- ```json {   "code": 500,   "meaning": "Error al recuperar el tarifario, descargar el archivo o codificar su contenido." } ```
- ```json {   "code": 503,   "meaning": "Servicio de autenticación no disponible." } ```

**Ejemplos**

- Estados documentados: Active, Created, Validating, Error e Inactive.

### Descargar plantilla de tarifas

**Método:** `GET`  
**Ruta:** `/shipping/me1/v1/tariff/template`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Descarga la plantilla XLSX de tarifas correspondiente al sitio.

**Parámetros**

- `site` (query, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Parámetro site ausente o inválido." } ```
- ```json {   "code": 401,   "meaning": "Token inválido." } ```
- ```json {   "code": 404,   "meaning": "Plantilla no encontrada para el site." } ```
- ```json {   "code": 500,   "meaning": "Error al leer o codificar el archivo." } ```
- ```json {   "code": 503,   "meaning": "Servicio de autenticación no disponible." } ```

**Ejemplos**

- Ejemplo con site=MLB.

### Simular cotización

**Método:** `POST`  
**Ruta:** `/shipping/me1/v1/quotation/simulate`  
**Autenticación:** Bearer token; el token debe identificar caller_id

Calcula cotizaciones ME1 para valor declarado, paquete y destino.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "declared_value (> 0)",
    "dimensions.width, dimensions.height, dimensions.length (cm, > 0)",
    "weight (gramos, entero positivo)",
    "destination.type (zipcode o city)",
    "destination.value"
  ]
}
```

**Respuesta**

- quotations[]: price
- quotations[]: speed
- quotations[]: service
- quotations[]: shipping_time
- quotations[]: handling_time
- quotations[]: promise

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Parámetros ausentes o inválidos; valores, dimensiones positivos y destino válido." } ```
- ```json {   "code": 401,   "meaning": "Token, client ID o caller_id inválido/ausente." } ```
- ```json {   "code": 403,   "meaning": "El vendedor no tiene ME1 habilitado." } ```
- ```json {   "code": 404,   "meaning": "Recurso no encontrado." } ```
- ```json {   "code": 429,   "meaning": "Límite de tasa excedido (50 RPM)." } ```
- ```json {   "code": 500,   "meaning": "Error al simular la cotización o recuperar datos del vendedor." } ```
- ```json {   "code": 503,   "meaning": "Autenticación o calculadora no disponible." } ```

**Ejemplos**

- Límite publicado: 50 solicitudes por minuto; el token debe contener caller_id.

### Actualizar tarifas ME1

**Método:** `POST`  
**Ruta:** `/shipping/me1/v1/tariff/update`  
**Autenticación:** Bearer token; el token debe identificar caller_id

Envía un archivo de tarifas para validación y actualización asíncrona.

**Parámetros**

- `site` (form-data, obligatorio)
- `service` (form-data, obligatorio)
- `file` (form-data, obligatorio): Archivo XLSX de máximo 7 MB.
- `callback_url` (form-data, obligatorio): URL HTTPS; no localhost ni IP privada.

**Solicitud**

```json
{
  "content_type": "multipart/form-data",
  "fields": [
    "site",
    "service",
    "file (.xlsx, máximo 7 MB)",
    "callback_url"
  ]
}
```

**Respuesta**

- resource_id
- callback webhook: event
- timestamp
- data.resource_id
- data.seller_id
- data.site_id
- data.service
- data.status
- data.errors
- data.warnings

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Parámetros inválidos, callback_url inválido o archivo mayor de 7 MB." } ```
- ```json {   "code": 401,   "meaning": "Token inválido o caller_id ausente." } ```
- ```json {   "code": 403,   "meaning": "El vendedor no tiene ME1 habilitado." } ```
- ```json {   "code": 404,   "meaning": "Vendedor no encontrado." } ```
- ```json {   "code": 429,   "meaning": "Límite de tasa excedido." } ```
- ```json {   "code": 500,   "meaning": "Error interno del servidor." } ```
- ```json {   "code": 503,   "meaning": "Servicio de autenticación no disponible." } ```

**Ejemplos**

- El token debe contener caller_id; la respuesta y procesamiento se notifican en forma asíncrona.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/flete-dinamico](https://developers.mercadolibre.com.co/es_co/flete-dinamico)  
**Captura:** 2026-10-08T22:51:50.332Z
