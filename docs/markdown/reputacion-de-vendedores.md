---
id: "reputacion-de-vendedores"
title: "Reputación de vendedores"
section: "Guía para productos"
subsection: "Métricas y Tendencias"
url: "https://developers.mercadolibre.com.co/es_co/reputacion-de-vendedores"
source_updated_at: "11/08/2025"
captured_at: "2026-10-08T22:52:47.063Z"
sha256: "3319bd3e5a972874e58778c23bea4004e238583cad6b7c4deb3c3cbb813d1b08"
---

# Reputación de vendedores

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 11/08/2025  
**Captura:** 2026-10-08T22:52:47.063Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/reputacion-de-vendedores](https://developers.mercadolibre.com.co/es_co/reputacion-de-vendedores)

## Resumen

Explica la reputación como indicador de confianza y ofrece una consulta del usuario que contiene nivel, estado de vendedor profesional y métricas históricas y recientes de transacciones.

## Contenido y conceptos documentados

### Respuesta

- La consulta requiere el identificador del usuario y se muestra con autenticación Bearer.
- `seller_reputation` puede contener `level_id`, `power_seller_status`, `real_level`, `protection_end_date`, transacciones y calificaciones, además de métricas de ventas, reclamos, demoras de despacho y cancelaciones.
- Parámetros de consulta, cuerpo y errores: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Consultar reputación de vendedor

**Método:** `GET`  
**Ruta:** `/users/$USER_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene reputación, transacciones y métricas del usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- seller_reputation.level_id
- seller_reputation.power_seller_status
- seller_reputation.real_level
- seller_reputation.protection_end_date
- seller_reputation.transactions.canceled
- seller_reputation.transactions.completed
- seller_reputation.transactions.ratings.negative
- seller_reputation.transactions.ratings.neutral
- seller_reputation.transactions.ratings.positive
- seller_reputation.metrics.sales
- seller_reputation.metrics.claims
- seller_reputation.metrics.delayed_handling_time
- seller_reputation.metrics.cancellations

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/reputacion-de-vendedores](https://developers.mercadolibre.com.co/es_co/reputacion-de-vendedores)  
**Captura:** 2026-10-08T22:52:47.063Z
