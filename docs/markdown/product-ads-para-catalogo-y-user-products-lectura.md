---
id: "product-ads-para-catalogo-y-user-products-lectura"
title: "Product Ads para Catálogo y User Products"
section: "Guía para Mercado Ads"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/product-ads-para-catalogo-y-user-products-lectura"
source_updated_at: "06/07/2026"
captured_at: "2026-10-08T22:50:59.574Z"
sha256: "e39b60ca9675908808fc37b73229b131718c4d0a2d12b27150d698c246b7034e"
---

# Product Ads para Catálogo y User Products

**Área:** Guía para Mercado Ads  
**Actualización indicada por la fuente:** 06/07/2026  
**Captura:** 2026-10-08T22:50:59.574Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/product-ads-para-catalogo-y-user-products-lectura](https://developers.mercadolibre.com.co/es_co/product-ads-para-catalogo-y-user-products-lectura)

## Resumen

La guía describe el flujo actual de Product Ads para ítems de Catálogo y User Products y la unificación de variantes en campañas basadas en Ad Groups. También identifica rutas legadas desactivadas para facilitar la migración.

## Contenido y conceptos documentados

- En el flujo actual, las variantes de un producto se centralizan en una campaña asociada al producto principal; las acciones de campaña afectan al conjunto de variantes. family_id y catalog_product_id son claves de agrupación. Para mapear ítems se usa parent_id (Catálogo), family_id (User Products) o item_id (publicaciones tradicionales).
- El filtro válido para buscar varios ítems es filters[item_ids]; la página indica que filters[item_id] singular ya no se soporta. Las métricas de anuncios fueron retiradas y se reemplazan por métricas de Ad Group.
- La guía declara desactivados permanentemente desde 27/05/2026 once endpoints legados, que responden 404. Las rutas actuales incluyen búsqueda/detalle de campañas y Ad Groups y sus métricas.
- Para métricas se describen rangos de hasta 90 días hacia atrás, un aggregation_type por consulta y métricas como clicks, prints, cost, cpc, ctr, amounts, quantities, acos, roas y competitividad.

## Operaciones de API

## Conceptos y recursos asociados

### Agrupación de variantes en Product Ads

Las variantes de Catálogo y User Products se centralizan en una campaña basada en el producto principal; las acciones afectan el conjunto. family_id y catalog_product_id son ejes de agrupación. La guía también registra once rutas legadas desactivadas.
## Operaciones de API

### Buscar Ad Groups por ítems

**Método:** `GET`  
**Ruta:** `/advertising/$ADVERTISER_SITE_ID/advertisers/$ADVERTISER_ID/product_ads/ad_groups/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene ad_group_id a partir de uno o varios ítems; usar parent_id para Catálogo, family_id para User Products o item_id para publicaciones tradicionales.

**Parámetros**

- `ADVERTISER_SITE_ID` (path, obligatorio): Site del anunciante.
- `ADVERTISER_ID` (path, obligatorio): ID de anunciante.
- `filters[item_ids]` (query, opcional): Filtro plural por IDs de ítems.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- filters[item_id] singular ya no está soportado.

### Búsqueda de anuncios marcada Deprecated

**Método:** `GET`  
**Ruta:** `/advertising/$ADVERTISER_SITE_ID/advertisers/$ADVERTISER_ID/product_ads/ads/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La página marca esta llamada como Deprecated; el flujo actual se apoya en Ad Groups.

**Parámetros**

- `ADVERTISER_SITE_ID` (path, obligatorio): Site de anunciante.
- `ADVERTISER_ID` (path, obligatorio): ID de anunciante.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- La fuente marca la llamada como Deprecated.

**Ejemplos**

No documentado en la fuente.

### Buscar campañas Product Ads

**Método:** `GET`  
**Ruta:** `/advertising/$ADVERTISER_SITE_ID/advertisers/$ADVERTISER_ID/product_ads/campaigns/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista campañas de un anunciante con filtros, fechas, paginación y métricas opcionales.

**Parámetros**

- `ADVERTISER_SITE_ID` (path, obligatorio): Site de anunciante.
- `ADVERTISER_ID` (path, obligatorio): ID de anunciante.
- `limit` (query, opcional): Límite.
- `offset` (query, opcional): Desplazamiento.
- `date_from` (query, opcional): Fecha inicial.
- `date_to` (query, opcional): Fecha final.
- `metrics` (query, opcional): Métricas solicitadas.
- `aggregation_type` (query, opcional): Solo puede solicitarse uno a la vez.
- `metrics_summary` (query, opcional): Solicita resumen de métricas.
- `filters[status]` (query, opcional): Filtro de estado mostrado.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Campañas y métricas; la guía anuncia roas_target desde enero de 2026.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Rango de métricas de hasta 90 días hacia atrás.

### Consultar anunciantes Product Ads

**Método:** `GET`  
**Ruta:** `/advertising/advertisers`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista anunciantes accesibles para el usuario con product_id=PADS.

**Parámetros**

- `product_id` (query, obligatorio): Usar PADS.

**Solicitud**

No documentado en la fuente.

**Respuesta**

advertisers[] con advertiser_id y site.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar detalle de Ad Group

**Método:** `GET`  
**Ruta:** `/advertising/$ADVERTISER_SITE_ID/product_ads/ad_groups/$AD_GROUP_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene información detallada y métricas de un Ad Group.

**Parámetros**

- `ADVERTISER_SITE_ID` (path, obligatorio): Site de anunciante.
- `AD_GROUP_ID` (path, obligatorio): ID de Ad Group.
- `date_from` (query, opcional): Fecha inicial de métricas.
- `date_to` (query, opcional): Fecha final de métricas.
- `metrics` (query, opcional): Métricas solicitadas.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Detalle del Ad Group y métricas seleccionadas.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar detalle y métricas de campaña

**Método:** `GET`  
**Ruta:** `/advertising/$ADVERTISER_SITE_ID/product_ads/campaigns/$CAMPAIGN_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta una campaña por ID con fechas y métricas opcionales.

**Parámetros**

- `ADVERTISER_SITE_ID` (path, obligatorio): Site de anunciante.
- `CAMPAIGN_ID` (path, obligatorio): ID de campaña.
- `date_from` (query, opcional): Fecha inicial.
- `date_to` (query, opcional): Fecha final.
- `metrics` (query, opcional): Métricas y competitividad.
- `aggregation_type` (query, opcional): La página muestra daily.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Detalle, métricas y campo roas_target según la actualización descrita.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Métricas: hasta 90 días hacia atrás.

### Descontinuado: /advertising/product_ads/ads/search

**Método:** `GET`  
**Ruta:** `/advertising/product_ads/ads/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Endpoint legado desactivado permanentemente el 27/05/2026; la página indica que devuelve 404 y que solo los endpoints documentados de Product Ads tienen soporte.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 404 desde la fecha de desactivación indicada.

**Ejemplos**

- Referencia histórica para identificar integraciones que deben migrar.

### Descontinuado: /advertising/advertisers/$ADVERTISER_ID/product_ads/campaigns

**Método:** `GET`  
**Ruta:** `/advertising/advertisers/$ADVERTISER_ID/product_ads/campaigns`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Endpoint legado desactivado permanentemente el 27/05/2026; la página indica que devuelve 404 y que solo los endpoints documentados de Product Ads tienen soporte.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 404 desde la fecha de desactivación indicada.

**Ejemplos**

- Referencia histórica para identificar integraciones que deben migrar.

### Descontinuado: /advertising/advertisers/$ADVERTISER_ID/product_ads/items

**Método:** `GET`  
**Ruta:** `/advertising/advertisers/$ADVERTISER_ID/product_ads/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Endpoint legado desactivado permanentemente el 27/05/2026; la página indica que devuelve 404 y que solo los endpoints documentados de Product Ads tienen soporte.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 404 desde la fecha de desactivación indicada.

**Ejemplos**

- Referencia histórica para identificar integraciones que deben migrar.

### Descontinuado: /advertising/product_ads/campaigns/$CAMPAIGN_ID

**Método:** `GET`  
**Ruta:** `/advertising/product_ads/campaigns/$CAMPAIGN_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Endpoint legado desactivado permanentemente el 27/05/2026; la página indica que devuelve 404 y que solo los endpoints documentados de Product Ads tienen soporte.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 404 desde la fecha de desactivación indicada.

**Ejemplos**

- Referencia histórica para identificar integraciones que deben migrar.

### Descontinuado: /advertising/product_ads/campaigns/$CAMPAIGN_ID/ads/metrics

**Método:** `GET`  
**Ruta:** `/advertising/product_ads/campaigns/$CAMPAIGN_ID/ads/metrics`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Endpoint legado desactivado permanentemente el 27/05/2026; la página indica que devuelve 404 y que solo los endpoints documentados de Product Ads tienen soporte.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 404 desde la fecha de desactivación indicada.

**Ejemplos**

- Referencia histórica para identificar integraciones que deben migrar.

### Descontinuado: /advertising/product_ads_2/campaigns/$CAMPAIGN_ID/ads/metrics

**Método:** `GET`  
**Ruta:** `/advertising/product_ads_2/campaigns/$CAMPAIGN_ID/ads/metrics`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Endpoint legado desactivado permanentemente el 27/05/2026; la página indica que devuelve 404 y que solo los endpoints documentados de Product Ads tienen soporte.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 404 desde la fecha de desactivación indicada.

**Ejemplos**

- Referencia histórica para identificar integraciones que deben migrar.

### Descontinuado: /advertising/product_ads/campaigns/$CAMPAIGN_ID/metrics

**Método:** `GET`  
**Ruta:** `/advertising/product_ads/campaigns/$CAMPAIGN_ID/metrics`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Endpoint legado desactivado permanentemente el 27/05/2026; la página indica que devuelve 404 y que solo los endpoints documentados de Product Ads tienen soporte.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 404 desde la fecha de desactivación indicada.

**Ejemplos**

- Referencia histórica para identificar integraciones que deben migrar.

### Descontinuado: /advertising/product_ads_2/campaigns/$CAMPAIGN_ID/metrics

**Método:** `GET`  
**Ruta:** `/advertising/product_ads_2/campaigns/$CAMPAIGN_ID/metrics`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Endpoint legado desactivado permanentemente el 27/05/2026; la página indica que devuelve 404 y que solo los endpoints documentados de Product Ads tienen soporte.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 404 desde la fecha de desactivación indicada.

**Ejemplos**

- Referencia histórica para identificar integraciones que deben migrar.

### Descontinuado: /advertising/product_ads/items/$ITEM_ID

**Método:** `GET`  
**Ruta:** `/advertising/product_ads/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Endpoint legado desactivado permanentemente el 27/05/2026; la página indica que devuelve 404 y que solo los endpoints documentados de Product Ads tienen soporte.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 404 desde la fecha de desactivación indicada.

**Ejemplos**

- Referencia histórica para identificar integraciones que deben migrar.

### Descontinuado: /advertising/$ADVERTISER_SITE_ID/advertisers/$ADVERTISER_ID/product_ads/items/search

**Método:** `GET`  
**Ruta:** `/advertising/$ADVERTISER_SITE_ID/advertisers/$ADVERTISER_ID/product_ads/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Endpoint legado desactivado permanentemente el 27/05/2026; la página indica que devuelve 404 y que solo los endpoints documentados de Product Ads tienen soporte.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 404 desde la fecha de desactivación indicada.

**Ejemplos**

- Referencia histórica para identificar integraciones que deben migrar.

### Descontinuado: /advertising/$ADVERTISER_SITE_ID/product_ads/items/$ITEM_ID

**Método:** `GET`  
**Ruta:** `/advertising/$ADVERTISER_SITE_ID/product_ads/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Endpoint legado desactivado permanentemente el 27/05/2026; la página indica que devuelve 404 y que solo los endpoints documentados de Product Ads tienen soporte.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 404 desde la fecha de desactivación indicada.

**Ejemplos**

- Referencia histórica para identificar integraciones que deben migrar.

### Consultar métricas de Ad Groups de campaña

**Método:** `GET`  
**Ruta:** `/advertising/$ADVERTISER_SITE_ID/product_ads/campaigns/$CAMPAIGN_ID/ad_groups/metrics`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene métricas de Ad Groups; para un solo día date_from=date_to y para períodos superiores usa filters[ad_group_ids].

**Parámetros**

- `ADVERTISER_SITE_ID` (path, obligatorio): Site.
- `CAMPAIGN_ID` (path, obligatorio): ID de campaña.
- `date_from` (query, obligatorio): Fecha inicial.
- `date_to` (query, obligatorio): Fecha final.
- `metrics` (query, obligatorio): Métricas a solicitar.
- `filters[ad_group_ids]` (query, opcional): Filtro para rangos de más de un día.

**Solicitud**

No documentado en la fuente.

**Respuesta**

results de métricas; vacío si no existen métricas para la fecha.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar métricas de anuncios del Ad Group

**Método:** `GET`  
**Ruta:** `/advertising/$ADVERTISER_SITE_ID/product_ads/ad_groups/$AD_GROUP_ID/ads`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve métricas de anuncios pertenecientes a un Ad Group en el intervalo solicitado.

**Parámetros**

- `ADVERTISER_SITE_ID` (path, obligatorio): Site.
- `AD_GROUP_ID` (path, obligatorio): ID de Ad Group.
- `date_from` (query, obligatorio): Fecha inicial.
- `date_to` (query, obligatorio): Fecha final.
- `metrics` (query, opcional): Métricas solicitadas.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Anuncios asociados y métricas.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Referencia HTTP GET /advertising/{ADVERTISER_SITE_ID}/advertisers/{ADVERTISER_ID}/product_ads/campaigns/{CAMPAIGN_ID}/ads/metrics

**Método:** `GET`  
**Ruta:** `/advertising/{ADVERTISER_SITE_ID}/advertisers/{ADVERTISER_ID}/product_ads/campaigns/{CAMPAIGN_ID}/ads/metrics`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /advertising/{ADVERTISER_SITE_ID}/advertisers/{ADVERTISER_ID}/product_ads/campaigns/{CAMPAIGN_ID}/ads/metrics. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

- `date_from` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.
- `date_to` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.
- `filters[item_ids]` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.
- `metrics` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/product-ads-para-catalogo-y-user-products-lectura](https://developers.mercadolibre.com.co/es_co/product-ads-para-catalogo-y-user-products-lectura)  
**Captura:** 2026-10-08T22:50:59.574Z
