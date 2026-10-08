---
id: "ads-bads"
title: "Brand Ads"
section: "Guía para Mercado Ads"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/ads-bads"
source_updated_at: "09/06/2026"
captured_at: "2026-10-08T22:50:55.865Z"
sha256: "eaf7e214badcb27c392cc03054b5c5204bba08c19c66a4fb1db777be3fa82eb8"
---

# Brand Ads

**Área:** Guía para Mercado Ads  
**Actualización indicada por la fuente:** 09/06/2026  
**Captura:** 2026-10-08T22:50:55.865Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/ads-bads](https://developers.mercadolibre.com.co/es_co/ads-bads)

## Resumen

Brand Ads ofrece campañas con anuncios y palabras clave cuya posición depende de la coincidencia con la búsqueda y de la subasta entre CPC máximo y Ad-Score. La guía expone consultas de anunciantes, campañas, ítems, keywords y métricas.

## Contenido y conceptos documentados

- La consulta inicial usa product_id=BADS; la fuente también enumera PADS y DISPLAY. Los anuncios se describen para vendedores/marcas que cumplan requisitos de reputación, cantidad mínima de publicaciones y disponibilidad por site.
- Las rutas documentadas permiten listar/detallar campañas, consultar ítems y keywords de campañas custom y recuperar métricas por anunciante, campaña, keyword o resumen.
- La página informa que desde 17/06/2026 ciertos anunciantes se migran a PAds: dejan de aparecer en product_id=BADS, sus consultas de campaña/métricas responden 204 y el histórico permanece disponible 30 días adicionales.

## Operaciones de API

## Conceptos y recursos asociados

### Migración Brand Ads a Product Ads

Desde 17/06/2026 algunos vendedores pasan a PAds; dejan de aparecer con product_id=BADS, campañas/métricas responden 204 y el histórico permanece 30 días adicionales.
### Ruta mencionada /currencies

La fuente menciona la ruta /currencies, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/currencies`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar anunciantes

**Método:** `GET`  
**Ruta:** `/advertising/advertisers`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista anunciantes por product_id.

**Parámetros**

- `product_id` (query, obligatorio): Tipo de producto; usar BADS.

**Solicitud**

No documentado en la fuente.

**Respuesta**

advertisers[] con advertiser_id, site_id, advertiser_name y account_name.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Headers documentados: Content-Type: application/json y Api-Version: 1.

### Consultar detalle de campaña

**Método:** `GET`  
**Ruta:** `/advertising/advertisers/$ADVERTISER_ID/brand_ads/campaigns/$CAMPAIGN_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene datos de campaña.

**Parámetros**

- `ADVERTISER_ID` (path, obligatorio): ID de anunciante.
- `CAMPAIGN_ID` (path, obligatorio): ID de campaña.

**Solicitud**

No documentado en la fuente.

**Respuesta**

campaign_id, name, fechas, advertiser_id, campaign_type y status.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar anuncios de campaña custom

**Método:** `GET`  
**Ruta:** `/advertising/advertisers/$ADVERTISER_ID/brand_ads/campaigns/$CAMPAIGN_ID/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista ítems de campaña custom.

**Parámetros**

- `ADVERTISER_ID` (path, obligatorio): ID de anunciante.
- `CAMPAIGN_ID` (path, obligatorio): ID de campaña.

**Solicitud**

No documentado en la fuente.

**Respuesta**

campaign_id, status e item_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar keywords de campaña custom

**Método:** `GET`  
**Ruta:** `/advertising/advertisers/$ADVERTISER_ID/brand_ads/campaigns/$CAMPAIGN_ID/keywords`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista keywords de campaña.

**Parámetros**

- `ADVERTISER_ID` (path, obligatorio): ID de anunciante.
- `CAMPAIGN_ID` (path, obligatorio): ID de campaña.

**Solicitud**

No documentado en la fuente.

**Respuesta**

campaign_id, type, term, match_type, is_negative y cpc.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Buscar campañas Brand Ads

**Método:** `GET`  
**Ruta:** `/advertising/advertisers/$ADVERTISER_ID/brand_ads/campaigns`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista campañas del anunciante.

**Parámetros**

- `ADVERTISER_ID` (path, obligatorio): ID de anunciante.

**Solicitud**

No documentado en la fuente.

**Respuesta**

paging y campaigns[] con datos de campaña.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar métricas de campaña

**Método:** `GET`  
**Ruta:** `/advertising/advertisers/$ADVERTISER_ID/brand_ads/campaigns/$CAMPAIGN_ID/metrics`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Métricas de una campaña en el período.

**Parámetros**

- `ADVERTISER_ID` (path, obligatorio): ID de anunciante.
- `CAMPAIGN_ID` (path, obligatorio): ID de campaña.
- `date_from` (query, obligatorio): Fecha inicial.
- `date_to` (query, obligatorio): Fecha final.

**Solicitud**

No documentado en la fuente.

**Respuesta**

dashboard con métricas por fecha.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar métricas agregadas

**Método:** `GET`  
**Ruta:** `/advertising/advertisers/$ADVERTISER_ID/brand_ads/campaigns/metrics`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Métricas de campañas por período/agregación.

**Parámetros**

- `ADVERTISER_ID` (path, obligatorio): ID de anunciante.
- `date_from` (query, obligatorio): Fecha inicial YYYY-MM-DD.
- `date_to` (query, obligatorio): Fecha final YYYY-MM-DD.
- `aggregation_type` (query, obligatorio): La guía usa daily.

**Solicitud**

No documentado en la fuente.

**Respuesta**

dashboard con series de métricas por fecha.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar métricas de keywords

**Método:** `GET`  
**Ruta:** `/advertising/advertisers/$ADVERTISER_ID/brand_ads/campaigns/$CAMPAIGN_ID/keywords/metrics`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve resultados por palabra clave.

**Parámetros**

- `ADVERTISER_ID` (path, obligatorio): ID de anunciante.
- `CAMPAIGN_ID` (path, obligatorio): ID de campaña.
- `date_from` (query, obligatorio): Fecha inicial.
- `date_to` (query, obligatorio): Fecha final.

**Solicitud**

No documentado en la fuente.

**Respuesta**

metrics[] con keyword, prints, clicks, ctr y cvr.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar resumen completo de campañas

**Método:** `GET`  
**Ruta:** `/advertising/advertisers/$ADVERTISER_ID/brand_ads/campaigns/full_summary`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Resumen de campañas del anunciante por período.

**Parámetros**

- `ADVERTISER_ID` (path, obligatorio): ID de anunciante.
- `date_from` (query, obligatorio): Fecha inicial.
- `date_to` (query, obligatorio): Fecha final.

**Solicitud**

No documentado en la fuente.

**Respuesta**

summary[] con datos y estado de campaña.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/ads-bads](https://developers.mercadolibre.com.co/es_co/ads-bads)  
**Captura:** 2026-10-08T22:50:55.865Z
