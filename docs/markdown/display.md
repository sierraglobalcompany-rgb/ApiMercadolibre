---
id: "display"
title: "Display Ads"
section: "Guía para Mercado Ads"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/display"
source_updated_at: "07/03/2025"
captured_at: "2026-10-08T22:50:57.037Z"
sha256: "066cebb0c09542ca68f4b36f58e7a2caac84ee405b48101df63835e6494ea85e"
---

# Display Ads

**Área:** Guía para Mercado Ads  
**Actualización indicada por la fuente:** 07/03/2025  
**Captura:** 2026-10-08T22:50:57.037Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/display](https://developers.mercadolibre.com.co/es_co/display)

## Resumen

Display Ads permite que vendedores, agencias y marcas creen anuncios segmentados y revisen resultados en distintos espacios del ecosistema de Mercado Libre. La guía cubre anunciantes, campañas, line items, creativos y métricas.

## Contenido y conceptos documentados

- Display se habilita a través de Asesores Comerciales de Mercado Libre. La consulta de anunciantes requiere product_id=DISPLAY; sort_by y sort_order son opcionales en esa ruta.
- Las operaciones documentadas permiten listar campañas, métricas de campaña, line items, métricas por dimensión y creativos.
- La fuente incluye errores 400 por parámetros requeridos y 404 cuando no hay campañas, line items o creativos para los identificadores enviados.

## Operaciones de API

## Conceptos y recursos asociados

### Acceso a Display Ads

Display se habilita mediante Asesores Comerciales de Mercado Libre; la guía describe campañas, line items, creativos, segmentación y métricas de atribución.
## Operaciones de API

### Consultar anunciantes Display

**Método:** `GET`  
**Ruta:** `/advertising/advertisers`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista anunciantes por producto.

**Parámetros**

- `product_id` (query, obligatorio): DISPLAY para esta guía.
- `sort_by` (query, opcional): advertiser_id o site_id; por defecto advertiser_id.
- `sort_order` (query, opcional): asc/desc; por defecto desc.

**Solicitud**

No documentado en la fuente.

**Respuesta**

advertisers[] con advertiser_id, site_id, advertiser_name y account_name.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Headers: Content-Type: application/json y Api-Version: 1.

### Listar campañas Display

**Método:** `GET`  
**Ruta:** `/advertising/advertisers/$ADVERTISER_ID/display/campaigns`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista campañas del anunciante.

**Parámetros**

- `ADVERTISER_ID` (path, obligatorio): ID de anunciante.
- `sort_by` (query, opcional): Ejemplo start_date.
- `sort_order` (query, opcional): Ejemplo desc.

**Solicitud**

No documentado en la fuente.

**Respuesta**

results[] con id, name, start_date, end_date y campos de campaña.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Listar creativos

**Método:** `GET`  
**Ruta:** `/advertising/advertisers/$ADVERTISER_ID/display/campaigns/$CAMPAIGN_ID/line_items/$LINE_ITEM_ID/creatives`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista creativos de un line item.

**Parámetros**

- `ADVERTISER_ID` (path, obligatorio): ID de anunciante.
- `CAMPAIGN_ID` (path, obligatorio): ID de campaña.
- `LINE_ITEM_ID` (path, obligatorio): ID de line item.
- `sort_by` (query, opcional): Ejemplo start_date.
- `sort_order` (query, opcional): asc/desc.

**Solicitud**

No documentado en la fuente.

**Respuesta**

results[] con creative_id, name, status, line_item_id y campaign_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Listar line items

**Método:** `GET`  
**Ruta:** `/advertising/advertisers/$ADVERTISER_ID/display/campaigns/$CAMPAIGN_ID/line_items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista line items de campaña.

**Parámetros**

- `ADVERTISER_ID` (path, obligatorio): ID de anunciante.
- `CAMPAIGN_ID` (path, obligatorio): ID de campaña.
- `sort_by` (query, opcional): Ejemplo start_date.
- `sort_order` (query, opcional): asc/desc.

**Solicitud**

No documentado en la fuente.

**Respuesta**

results[] con line_item_id, name, fechas y campaign_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar métricas de campaña Display

**Método:** `GET`  
**Ruta:** `/advertising/advertisers/$ADVERTISER_ID/display/campaigns/$CAMPAIGN_ID/metrics`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene métricas de una campaña en un período.

**Parámetros**

- `ADVERTISER_ID` (path, obligatorio): ID de anunciante.
- `CAMPAIGN_ID` (path, obligatorio): ID de campaña.
- `date_from` (query, obligatorio): Fecha inicial YYYY-MM-DD.
- `date_to` (query, obligatorio): Fecha final YYYY-MM-DD.

**Solicitud**

No documentado en la fuente.

**Respuesta**

metrics[] con date, site_id, currency, prints, clicks y resultados.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar métricas por dimensión

**Método:** `GET`  
**Ruta:** `/advertising/advertisers/$ADVERTISER_ID/display/metrics`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene métricas de dimensión y campaña para un período.

**Parámetros**

- `ADVERTISER_ID` (path, obligatorio): ID de anunciante.
- `dimension` (query, obligatorio): El ejemplo usa line_items.
- `date_from` (query, obligatorio): Fecha inicial.
- `date_to` (query, obligatorio): Fecha final.
- `campaign_id` (query, obligatorio): ID de campaña.

**Solicitud**

No documentado en la fuente.

**Respuesta**

campaign_id/line_item_id y metrics[] por fecha.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/display](https://developers.mercadolibre.com.co/es_co/display)  
**Captura:** 2026-10-08T22:50:57.037Z
