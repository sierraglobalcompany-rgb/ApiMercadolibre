---
id: "facturacion"
title: "Datos de Facturación"
section: "Guía para productos"
subsection: "Facturación"
url: "https://developers.mercadolibre.com.co/es_co/facturacion"
source_updated_at: "16/06/2026"
captured_at: "2026-10-08T22:51:32.170Z"
sha256: "e0bd043008f7db370d54eb453f3e090e6a4e6d2ad44a7a417b150715e6b60ca8"
---

# Datos de Facturación

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 16/06/2026  
**Captura:** 2026-10-08T22:51:32.170Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/facturacion](https://developers.mercadolibre.com.co/es_co/facturacion)

## Resumen

Documenta cómo recuperar la información de facturación del comprador para emitir documentos fiscales. Primero se consulta la orden para obtener buyer.billing_info.id; luego se consulta el recurso de facturación con site_id y ese identificador. La respuesta cambia según país y tipo de persona.

## Contenido y conceptos documentados

- La respuesta de la orden incluye buyer.billing_info.id, que se usa como billing_info_id en la consulta posterior.
- Los datos documentados incluyen identificación, nombre, clasificación tributaria, inscripciones y dirección. Entre los campos de dirección aparecen calle, número, ciudad, barrio, comentario, código postal, estado y país; los atributos tributarios varían según el sitio.
- Los ejemplos muestran información para personas naturales y jurídicas y campos regionales como taxpayer_type, state_registration, iibb_number, economic_activity, contributor y cfdi, según el país.
- Autenticación mostrada: Bearer. No hay cuerpo de solicitud para estas consultas.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar datos fiscales del comprador

**Método:** `GET`  
**Ruta:** `/orders/billing-info/{site_id}/{billing_info_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene datos de facturación para el sitio y el identificador extraído de la orden.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `billing_info_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Datos de comprador y facturación: identificación, datos tributarios e información de domicilio; los campos dependen del sitio y de la persona.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos regionales para personas físicas y jurídicas.

### Obtener identificador de facturación de una orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Consulta la orden y extrae buyer.billing_info.id para la llamada de facturación.

**Parámetros**

- `order_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Orden con buyer.id y buyer.billing_info.id, además de otros datos de la orden.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de una orden con billing_info.id.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/facturacion](https://developers.mercadolibre.com.co/es_co/facturacion)  
**Captura:** 2026-10-08T22:51:32.170Z
