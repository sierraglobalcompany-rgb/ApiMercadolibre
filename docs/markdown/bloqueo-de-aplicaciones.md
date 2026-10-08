---
id: "bloqueo-de-aplicaciones"
title: "Bloqueo de aplicaciones"
section: "Recursos de la API"
subsection: "Usuarios"
url: "https://developers.mercadolibre.com.co/es_co/bloqueo-de-aplicaciones"
source_updated_at: "15/04/2026"
captured_at: "2026-10-08T22:53:41.757Z"
sha256: "76e342bf2d2f15d04419713206949eee78b6ad59af1c87e92f5e4c86f604aa58"
---

# Bloqueo de aplicaciones

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 15/04/2026  
**Captura:** 2026-10-08T22:53:41.757Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/bloqueo-de-aplicaciones](https://developers.mercadolibre.com.co/es_co/bloqueo-de-aplicaciones)

## Resumen

La página explica por qué se puede bloquear una aplicación, cómo afecta a la operación de los vendedores y qué acciones tomar según el motivo. Mientras el bloqueo esté activo, la integración no puede consumir APIs de Mercado Libre ni de Mercado Pago.

## Contenido y conceptos documentados

Los motivos enumerados son `NOT_COMPLY_KYC` (validación de datos), `NOT_COMPLY_T&C_RULES` (Términos y Condiciones), `EXCESSIVE_API_CALL` (llamadas excesivas o uso incorrecto de token) e `INTEGRATORS_DATA_INFRACTION` (tráfico de datos). La fuente indica que los usuarios pueden recibir `unauthorized_scopes` con estado `401`. Recomienda revisar los datos de cuenta y validar identidad para KYC, respetar las reglas, controlar errores de la familia 400 no previstos y verificar el uso de APIs que generan valor.

## Operaciones de API

## Conceptos y recursos asociados

### Causas y efectos del bloqueo de aplicaciones

Describe motivos de bloqueo, impacto sobre vendedores y pasos de remediación para restablecer el uso de APIs.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "unauthorized_scopes",   "meaning": "La fuente indica estado HTTP 401 para usuarios afectados por una aplicación bloqueada." } ```

**Ejemplos documentados**

- Motivos: NOT_COMPLY_KYC, NOT_COMPLY_T&C_RULES, EXCESSIVE_API_CALL e INTEGRATORS_DATA_INFRACTION.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/bloqueo-de-aplicaciones](https://developers.mercadolibre.com.co/es_co/bloqueo-de-aplicaciones)  
**Captura:** 2026-10-08T22:53:41.757Z
