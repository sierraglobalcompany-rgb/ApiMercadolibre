---
id: "seguridad-apps"
title: "Seguridad de aplicaciones"
section: "Guía de seguridad"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/seguridad-apps"
source_updated_at: "23/06/2026"
captured_at: "2026-10-08T22:50:15.089Z"
sha256: "acb0d5eedfb36a0234bc761fca680b6f0cf71e3cc3733d9641d833762bd54c5f"
---

# Seguridad de aplicaciones

**Área:** Guía de seguridad  
**Actualización indicada por la fuente:** 23/06/2026  
**Captura:** 2026-10-08T22:50:15.089Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/seguridad-apps](https://developers.mercadolibre.com.co/es_co/seguridad-apps)

## Resumen

Cubre protección de PII, validación de entradas, errores seguros, webhooks, rate limiting y dependencias.

## Contenido y conceptos documentados

- Recomienda cifrar y minimizar datos personales, validar en backend y procesar webhooks asíncronamente.

## Operaciones de API

## Conceptos y recursos asociados

### Seguridad de aplicaciones

Cubre protección de PII, validación de entradas, errores seguros, webhooks, rate limiting y dependencias.
## Operaciones de API

### Consultar recurso notificado en webhook

**Método:** `GET`  
**Ruta:** `/orders/{order_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La guía recomienda tratar el webhook como aviso y consultar el recurso oficial para validar su estado.

**Parámetros**

- `order_id` (path, obligatorio): ID de la orden incluida en resource.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET del recurso usando el access token del seller.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/seguridad-apps](https://developers.mercadolibre.com.co/es_co/seguridad-apps)  
**Captura:** 2026-10-08T22:50:15.089Z
