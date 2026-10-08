---
id: "primeros-pasos-in-house"
title: "Desarrollo in-house Quick Start"
section: "Primeros pasos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/primeros-pasos-in-house"
source_updated_at: "06/10/2026"
captured_at: "2026-10-08T22:53:31.284Z"
sha256: "30d6c3bec9d60230a54cc500201b356111fbc48f3399dcee0805ad303d8c90c4"
---

# Desarrollo in-house Quick Start

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 06/10/2026  
**Captura:** 2026-10-08T22:53:31.284Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/primeros-pasos-in-house](https://developers.mercadolibre.com.co/es_co/primeros-pasos-in-house)

## Resumen

Propone una secuencia de implementación in-house: crear la app en la cuenta oficial del vendedor, configurar OAuth y scopes mínimos, procesar notificaciones y construir el flujo de ventas, despacho, fiscalidad y posventa.

## Contenido y conceptos documentados

- El access token tiene vigencia de 6 horas; la fuente recomienda almacenar tokens de forma segura y reemplazar el refresh token tras cada uso. Implementa `state` y PKCE cuando estén habilitados, y usa usuarios de prueba por sitio antes de producción.
- Se recomienda configurar webhooks, responder HTTP 200 en 500 ms y recuperar fallos recientes con `missed_feeds`; mantener TLS 1.2 o superior. Separa aplicaciones de Mercado Libre y Mercado Pago y crea la app en la cuenta oficial del vendedor.
- Para facturación, extraer `buyer.billing_info.id`; la página indica que el flujo anterior `/orders/billing-info` está deprecado. Para logística menciona `processing_time_tool`, `carrier_pickup` y `NODE_ID` en escenarios multiorigen.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /communications/notices

La fuente menciona la ruta /communications/notices, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/communications/notices`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /post-purchase/v1/claims/{CLAIM_ID}

La fuente menciona la ruta /post-purchase/v1/claims/{CLAIM_ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/post-purchase/v1/claims/{CLAIM_ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /post-purchase/v1/claims/{CLAIM_ID}/changes

La fuente menciona la ruta /post-purchase/v1/claims/{CLAIM_ID}/changes, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/post-purchase/v1/claims/{CLAIM_ID}/changes`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /post-purchase/v2/claims/{CLAIM_ID}/returns

La fuente menciona la ruta /post-purchase/v2/claims/{CLAIM_ID}/returns, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/post-purchase/v2/claims/{CLAIM_ID}/returns`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### GET /applications/{APP_ID}

**Método:** `GET`  
**Ruta:** `/applications/{APP_ID}`  
**Autenticación:** No documentado en la fuente.

Verifica la configuración y los scopes de una aplicación.

**Parámetros**

- `APP_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página menciona este recurso explícitamente.

### GET /orders/billing-info/{site_id}/{billing_info_id}

**Método:** `GET`  
**Ruta:** `/orders/billing-info/{site_id}/{billing_info_id}`  
**Autenticación:** No documentado en la fuente.

Consulta datos fiscales del comprador; la página indica que el flujo está deprecado.

**Parámetros**

- `site_id` (path, obligatorio)
- `billing_info_id` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página menciona este recurso explícitamente.

### GET /users/{USER_ID}/shipping/schedule/{LOGISTIC_TYPE}

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/shipping/schedule/{LOGISTIC_TYPE}`  
**Autenticación:** No documentado en la fuente.

Consulta la agenda de Coletas del usuario según tipo logístico.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `LOGISTIC_TYPE` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página menciona este recurso explícitamente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/primeros-pasos-in-house](https://developers.mercadolibre.com.co/es_co/primeros-pasos-in-house)  
**Captura:** 2026-10-08T22:53:31.284Z
