---
id: "rate-limit-error-429"
title: "Rate Limit / Error 429"
section: "FAQs"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/rate-limit-error-429"
source_updated_at: "05/05/2026"
captured_at: "2026-10-08T22:50:06.139Z"
sha256: "6b25428cdcd8ed5c3c458ffd3a9c03236c217fe0fd3a83483daf26490b3583cb"
---

# Rate Limit / Error 429

**Área:** FAQs  
**Actualización indicada por la fuente:** 05/05/2026  
**Captura:** 2026-10-08T22:50:06.139Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/rate-limit-error-429](https://developers.mercadolibre.com.co/es_co/rate-limit-error-429)

## Resumen

Recomienda gestionar exceso de solicitudes con backoff, menor concurrencia, paginación y control por Client ID.

## Contenido y conceptos documentados

- La guía indica no mezclar scroll_id con offset/limit; recomienda backoff exponencial con jitter.

## Operaciones de API

## Conceptos y recursos asociados

### Rate Limit / Error 429

Recomienda gestionar exceso de solicitudes con backoff, menor concurrencia, paginación y control por Client ID.
### Consulta de visitas con límites de volumen

La FAQ menciona que esta consulta admite un solo product_id por llamada; respete el límite de consumo del recurso.

**Ruta mencionada:** `/items/visits`  
**Método HTTP:** No documentado en la fuente.

**Parámetros documentados**

- `product_id` (query): ID de producto; la FAQ indica que se consulta uno por llamada.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/rate-limit-error-429](https://developers.mercadolibre.com.co/es_co/rate-limit-error-429)  
**Captura:** 2026-10-08T22:50:06.139Z
