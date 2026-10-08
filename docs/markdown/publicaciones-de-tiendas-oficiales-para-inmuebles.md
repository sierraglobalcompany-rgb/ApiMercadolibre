---
id: "publicaciones-de-tiendas-oficiales-para-inmuebles"
title: "Publicaciones de Tiendas Oficiales para Inmuebles"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/publicaciones-de-tiendas-oficiales-para-inmuebles"
source_updated_at: "06/11/2025"
captured_at: "2026-10-08T22:50:50.140Z"
sha256: "552d3e5687f270864332104bd474f23a870538e3491f5a0af4b7a4e61bc06811"
---

# Publicaciones de Tiendas Oficiales para Inmuebles

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 06/11/2025  
**Captura:** 2026-10-08T22:50:50.140Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/publicaciones-de-tiendas-oficiales-para-inmuebles](https://developers.mercadolibre.com.co/es_co/publicaciones-de-tiendas-oficiales-para-inmuebles)

## Resumen

Las publicaciones de usuarios con Tienda Oficial usan el flujo normal de POST /items e incluyen official_store_id para vincular el inmueble con la tienda correspondiente.

## Contenido y conceptos documentados

- official_store_id es obligatorio para usuarios asociados a una Tienda Oficial; si el vendedor no tiene una, se envía null.
- La guía muestra errores si falta el identificador o si el usuario no está autorizado para usar la tienda indicada.
- En una actualización del ítem solo se debe incluir official_store_id cuando se quiera cambiar la tienda; esta página no especifica la ruta de actualización.

## Operaciones de API
## Operaciones de API

### Publicar inmueble en Tienda Oficial

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Publica un aviso con official_store_id; es obligatorio para vendedores ligados a una Tienda Oficial y se envía null si el vendedor no tiene tienda.

**Parámetros**

- `official_store_id` (body, obligatorio): ID de tienda del usuario vinculado; null si no existe tienda.

**Solicitud**

JSON con official_store_id y campos de publicación.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400 item.official_store_id.invalid: usuario tipo brand debe proporcionar ID de tienda.
- 403 body.invalid_official_store_id: vendedor no autorizado para el ID indicado.

**Ejemplos**

- En actualizaciones, enviar official_store_id solo si se desea modificar la tienda; esta página no da ruta de actualización.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/publicaciones-de-tiendas-oficiales-para-inmuebles](https://developers.mercadolibre.com.co/es_co/publicaciones-de-tiendas-oficiales-para-inmuebles)  
**Captura:** 2026-10-08T22:50:50.140Z
