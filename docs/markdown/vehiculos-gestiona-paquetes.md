---
id: "vehiculos-gestiona-paquetes"
title: "Gestiona paquetes de vehículos"
section: "Guía para vehículos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-paquetes"
source_updated_at: "24/11/2025"
captured_at: "2026-10-08T22:53:15.479Z"
sha256: "4a5b952ddae2b1387fbcb664451a28f7b11299a55366b58c5fc0bd6db611dcb1"
---

# Gestiona paquetes de vehículos

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 24/11/2025  
**Captura:** 2026-10-08T22:53:15.479Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-paquetes](https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-paquetes)

## Resumen

Explica la consulta de paquetes de publicación y destacados para categorías y usuarios, la disponibilidad de cupos y la actualización del listing type de un anuncio. También describe el nuevo modelo de paquetes para MLM y MCO.

## Contenido y conceptos documentados

- `package_content` es opcional, predeterminado `publications`; valores: `publications`, `upgrades` y `ALL`. Los paquetes incluyen identificadores, categoría, descripción, tipo, estado y fechas.
- Los estados descritos son activo, pendiente y finalizado. Los paquetes pueden ser mensuales o trimestrales; un paquete activado no se pausa, aunque puede inactivarse un destaque para liberar cupo. En MLM y MCO se separan suscripción y destacado; `gold` se presenta como Acelerador y `gold_premium` como Acelerador Plus.
- Para consultar disponibilidad se usa `categoryId` y `upgrades=true` al consultar cupos de upgrades. Para destacar, el vendedor debe haber contratado un paquete y enviar el listing type deseado.

## Operaciones de API
## Operaciones de API

### GET /categories/{CATEGORY_ID}/classifieds_promotion_packs

**Método:** `GET`  
**Ruta:** `/categories/{CATEGORY_ID}/classifieds_promotion_packs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta paquetes disponibles para una categoría; admite `package_content`.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio)
- `package_content` (query, opcional): publications, upgrades o ALL; default publications

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}/classifieds_promotion_packs

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/classifieds_promotion_packs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta paquetes contratados por un usuario; admite `package_content`.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `package_content` (query, opcional): publications, upgrades o ALL; default publications

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}/classifieds_promotion_packs/{LISTING_TYPE}/available

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/classifieds_promotion_packs/{LISTING_TYPE}/available`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta si hay publicaciones disponibles en el tipo indicado.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `LISTING_TYPE` (path, obligatorio)
- `categoryId` (query, obligatorio): Categoría
- `upgrades` (query, opcional): true para consultar upgrades

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "has_available_listings"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### POST /items/{ITEM_ID}/listing_type

**Método:** `POST`  
**Ruta:** `/items/{ITEM_ID}/listing_type`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza el tipo de publicación; el ejemplo envía `id=gold_premium`.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "id"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### Referencia HTTP GET /users/123456789/classifieds_promotion_packs/gold_premium/available

**Método:** `GET`  
**Ruta:** `/users/123456789/classifieds_promotion_packs/gold_premium/available`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/123456789/classifieds_promotion_packs/gold_premium/available. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

- `categoryId` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.
- `upgrades` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-paquetes](https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-paquetes)  
**Captura:** 2026-10-08T22:53:15.479Z
