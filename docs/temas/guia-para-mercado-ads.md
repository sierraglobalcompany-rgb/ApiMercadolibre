# Guía para Mercado Ads

5 páginas del portal oficial en esta área.

## [Bonificaciones para Product Ads](../markdown/bonificaciones-para-product-ads.md)

Actualización indicada por la fuente: 08/01/2026. Captura: 2026-10-08T22:50:54.832Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/bonificaciones-para-product-ads](https://developers.mercadolibre.com.co/es_co/bonificaciones-para-product-ads)

# Bonificaciones para Product Ads

**Área:** Guía para Mercado Ads  
**Actualización indicada por la fuente:** 08/01/2026  
**Captura:** 2026-10-08T22:50:54.832Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/bonificaciones-para-product-ads](https://developers.mercadolibre.com.co/es_co/bonificaciones-para-product-ads)

## Resumen

Esta guía documenta la consulta de bonificaciones de Product Ads asociadas a una cuenta o campaña. Describe los tipos de beneficio y los datos de importe, saldo, vigencia, moneda y estado que devuelve la consulta.

## Contenido y conceptos documentados

- Tipos descritos: Certification, Seller Startup Program, Smart Benefits y Manual; la elegibilidad depende de cada beneficio.
- bonification puede contener datos de nivel Campaign o Account. Para campañas, puede incluir campaign_name y campaign_status; para ambos niveles se documentan status, fechas, moneda, amount, balance, days_remaining, campaign_id y benefit_name.
- Sin bonificaciones, la API responde HTTP 200 con el arreglo bonification vacío. Token inválido o expirado aparece como error 401.

## Operaciones de API

## Conceptos y recursos asociados

### Tipos de bonificaciones Product Ads

La guía describe Certification, Seller Startup Program, Smart Benefits y Manual, sujetos a condiciones propias de elegibilidad.
## Operaciones de API

### Consultar bonificaciones Product Ads

**Método:** `GET`  
**Ruta:** `/advertising/advertisers/bonifications`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista beneficios activos o históricos a nivel cuenta o campaña, incluyendo importe, saldo, moneda, vigencia y estado asociado.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

bonification[]: status, creation_date, end_date, currency_id, level, amount, balance, days_remaining, campaign_id, benefit_name; para campaña también campaign_name y campaign_status.

**Errores documentados**

- 401 unauthorized: invalid access token.

**Ejemplos**

- Sin bonificaciones responde HTTP 200 con bonification vacío.
- Tipos: Certification, Seller-startup-program, Smart-benefit y Manual.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/bonificaciones-para-product-ads](https://developers.mercadolibre.com.co/es_co/bonificaciones-para-product-ads)  
**Captura:** 2026-10-08T22:50:54.832Z

---

## [Brand Ads](../markdown/ads-bads.md)

Actualización indicada por la fuente: 09/06/2026. Captura: 2026-10-08T22:50:55.865Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/ads-bads](https://developers.mercadolibre.com.co/es_co/ads-bads)

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

---

## [Display Ads](../markdown/display.md)

Actualización indicada por la fuente: 07/03/2025. Captura: 2026-10-08T22:50:57.037Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/display](https://developers.mercadolibre.com.co/es_co/display)

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

---

## [Introducción a Mercado Ads](../markdown/introduccion-a-mercado-ads.md)

Actualización indicada por la fuente: 05/08/2024. Captura: 2026-10-08T22:50:58.436Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/introduccion-a-mercado-ads](https://developers.mercadolibre.com.co/es_co/introduccion-a-mercado-ads)

# Introducción a Mercado Ads

**Área:** Guía para Mercado Ads  
**Actualización indicada por la fuente:** 05/08/2024  
**Captura:** 2026-10-08T22:50:58.436Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/introduccion-a-mercado-ads](https://developers.mercadolibre.com.co/es_co/introduccion-a-mercado-ads)

## Resumen

Mercado Ads permite dar visibilidad a productos y organizar anuncios en campañas, definir inversión, pausar o activar campañas y consultar reportes y métricas.

## Contenido y conceptos documentados

- La página presenta Product Ads como promoción de publicaciones en posiciones relevantes y describe de forma general los productos publicitarios.
- Es introductoria y no especifica rutas HTTP, parámetros ni estructuras de solicitud/respuesta.

## Operaciones de API

## Conceptos y recursos asociados

### Productos de Mercado Ads

La introducción describe Product Ads para promocionar publicaciones en posiciones relevantes, agrupar anuncios en campañas, definir inversión, pausar/activar campañas y consultar reportes y métricas; no lista rutas HTTP.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/introduccion-a-mercado-ads](https://developers.mercadolibre.com.co/es_co/introduccion-a-mercado-ads)  
**Captura:** 2026-10-08T22:50:58.436Z

---

## [Product Ads para Catálogo y User Products](../markdown/product-ads-para-catalogo-y-user-products-lectura.md)

Actualización indicada por la fuente: 06/07/2026. Captura: 2026-10-08T22:50:59.574Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/product-ads-para-catalogo-y-user-products-lectura](https://developers.mercadolibre.com.co/es_co/product-ads-para-catalogo-y-user-products-lectura)

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

---
