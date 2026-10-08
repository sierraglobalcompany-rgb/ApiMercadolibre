---
id: "bonificaciones-para-product-ads"
title: "Bonificaciones para Product Ads"
section: "Guía para Mercado Ads"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/bonificaciones-para-product-ads"
source_updated_at: "08/01/2026"
captured_at: "2026-10-08T22:50:54.832Z"
sha256: "7909a0fd9b7d104471767fa7cfd7f58a90ca0e8be1e8a282045db77d5ba8f24f"
---

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
