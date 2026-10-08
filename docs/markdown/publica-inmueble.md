---
id: "publica-inmueble"
title: "Publica Inmuebles"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/publica-inmueble"
source_updated_at: "28/08/2026"
captured_at: "2026-10-08T22:50:49.107Z"
sha256: "bddabc7b1c8c3143d9b9c8e7f743e8718a13b06987e4b563c67b61b6911ad067"
---

# Publica Inmuebles

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 28/08/2026  
**Captura:** 2026-10-08T22:50:49.107Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/publica-inmueble](https://developers.mercadolibre.com.co/es_co/publica-inmueble)

## Resumen

Esta guía describe la creación de publicaciones inmobiliarias con POST /items. Recomienda validar el JSON y revisar los atributos requeridos, la ubicación y la calidad del aviso antes de enviarlo.

## Contenido y conceptos documentados

- El ejemplo de solicitud incluye campos de publicación como title, category_id, price, currency_id, available_quantity, buying_mode, listing_type_id, condition, description, location, pictures, attributes, channels, video_id y seller_contact.
- Desde 01/10/2026, country_code2 y phone2 son obligatorios en seller_contact para todos los tipos de usuario. Deben contener solo dígitos: el código de país va en country_code2 y el resto del número en phone2.
- Desde 23/02/2026, pictures debe incluir al menos una imagen para listing type silver y para tipos gold configurados con requires_picture=true; si falta, la fuente documenta HTTP 400, error 173 LTP_PICTURE_REQUIRED.
- Para publicar también en el Portal Inmobiliario de Chile (MLC), el ejemplo de la guía incluye CMG_SITE.

## Operaciones de API
## Operaciones de API

### Publicar inmueble

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea aviso inmobiliario. El JSON debe cumplir atributos y seller_contact; desde 01/10/2026 country_code2 y phone2 son obligatorios para todos los usuarios.

**Parámetros**

- `body` (body, obligatorio): JSON de publicación y seller_contact.

**Solicitud**

title, category_id, price, currency_id, available_quantity, buying_mode, listing_type_id, condition, description, location, pictures, attributes, channels, video_id y seller_contact.

**Respuesta**

Respuesta de creación con ID del ítem; otros campos: No documentado en la fuente.

**Errores documentados**

- 400 seller_contact.required: falta objeto seller_contact.
- 400 seller_contact.country_code2.required: falta country_code2.
- 400 seller_contact.phone2.required: falta phone2.
- 400 seller_contact.country_code2.invalid: formato inválido.
- 400 seller_contact.phone2.invalid: formato inválido.
- 400 error 173 LTP_PICTURE_REQUIRED: falta imagen para listing type silver o tipo gold con requires_picture=true.

**Ejemplos**

- country_code2 y phone2 solo llevan dígitos; código de país y resto del número van en campos separados.
- Para MLC, la guía indica CMG_SITE para listing_source portalinmobiliario.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/publica-inmueble](https://developers.mercadolibre.com.co/es_co/publica-inmueble)  
**Captura:** 2026-10-08T22:50:49.107Z
