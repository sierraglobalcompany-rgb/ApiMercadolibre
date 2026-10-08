---
id: "central-de-promociones"
title: "Gestionar promociones"
section: "Guía para productos"
subsection: "Central de promociones"
url: "https://developers.mercadolibre.com.co/es_co/central-de-promociones"
source_updated_at: "09/06/2026"
captured_at: "2026-10-08T22:51:58.602Z"
sha256: "9cc3fae1dbcd99bb6bed33dc6561a230bb6cdf05c37c37243451503cdde1a2eb"
---

# Gestionar promociones

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 09/06/2026  
**Captura:** 2026-10-08T22:51:58.602Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/central-de-promociones](https://developers.mercadolibre.com.co/es_co/central-de-promociones)

## Resumen

La Central de promociones unifica consultas y acciones sobre campañas, candidatos, ofertas, promociones asociadas a ítems y listas de exclusión de vendedores o publicaciones. Las solicitudes documentadas usan la versión de aplicación `v2`.

## Contenido y conceptos documentados

### Parámetros y restricciones

- Las llamadas muestran `Authorization: Bearer $ACCESS_TOKEN` y el query `app_version=v2`. Las rutas de detalle/listado también requieren `USER_ID`, `CANDIDATE_ID`, `OFFERS_ID`, `PROMOTION_ID` o `ITEM_ID` según el recurso; la consulta de promoción recibe `promotion_type`.
- El listado de ítems de una promoción admite filtros `item_id`, `status` (`started`, `pending`, `candidate`) y `status_item` (`active`, `paused`, por defecto `active`). Paginación: `limit` predeterminado 50 y máximo 50, más `search_after` (la documentación indica el alias anterior `searchAfter`), con cursor válido por cinco minutos y navegación hacia adelante.
- El borrado masivo de ofertas no aplica a DOD/LIGHTNING. La página señala errores `423_ENTITY_LOCKED` y `400_BAD_REQUEST`; la respuesta incluye `successful_ids` y `errors`.
- La lista de exclusión usa `exclusion_status` como texto `true`/`false`; la operación por ítem usa además `item_id`. Para pruebas se requieren usuarios/publicaciones de prueba y query `version=test`. Los cupones de campaña para vendedores se indican solo para MLB.
- En fichas de promoción se muestran estados, precios y, para ciertas ofertas, campos de boost como `boosted_offer`, `discount_meli_boosted_percentage`, `discount_meli_boost_amount` y `total_price_for_boosted_offer`. Detalles no especificados por cada ruta: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Eliminar ofertas del ítem

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina en bloque ofertas promocionales admitidas para el ítem.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- successful_ids
- errors

**Errores documentados**

- ```json {   "code": "423_ENTITY_LOCKED",   "meaning": "Entidad bloqueada." } ```
- ```json {   "code": "400_BAD_REQUEST",   "meaning": "Solicitud inválida." } ```

**Ejemplos**

- No aplica a ofertas DOD ni LIGHTNING.

### Consultar candidato

**Método:** `GET`  
**Ruta:** `/seller-promotions/candidates/$CANDIDATE_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el artículo candidato, promoción asociada y estado.

**Parámetros**

- `CANDIDATE_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- type
- status
- item_id
- promotion_id
- start_date
- finish_date
- deadline_date
- name
- benefits

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El identificador se recibe mediante notificación pública de candidatos.

### Consultar exclusiones del vendedor

**Método:** `GET`  
**Ruta:** `/seller-promotions/exclusion-list/seller`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista publicaciones excluidas del vendedor y sus estados.

**Parámetros**

- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- excluded
- not_excluded
- paging

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar exclusión de ítem del vendedor

**Método:** `GET`  
**Ruta:** `/seller-promotions/exclusion-list/seller/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta si un ítem está incluido en la lista de exclusión del vendedor.

**Parámetros**

- `item_id` (path, obligatorio)
- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- item_id
- exclusion_status

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Promociones del ítem

**Método:** `GET`  
**Ruta:** `/seller-promotions/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista las promociones asociadas a una publicación.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- results[].id
- results[].type
- results[].status
- results[].price
- results[].boosted_offer
- results[].discount_meli_boosted_percentage
- results[].discount_meli_boost_amount
- results[].total_price_for_boosted_offer

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Incluye tipos de promoción de ofertas y campos de boost cuando apliquen.

### Consultar oferta

**Método:** `GET`  
**Ruta:** `/seller-promotions/offers/$OFFERS_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta una oferta promocional, artículo asociado y estado.

**Parámetros**

- `OFFERS_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- offer_id
- id
- type
- status
- item_id
- promotion_id
- start_date
- finish_date
- deadline_date
- name
- benefits
- ref_id

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La oferta se identifica a partir de la notificación pública correspondiente.

### Detalle de promoción

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/$PROMOTION_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalle de una campaña por identificador y tipo.

**Parámetros**

- `PROMOTION_ID` (path, obligatorio)
- `promotion_type` (query, obligatorio)
- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- type
- status
- start_date
- finish_date
- deadline_date
- name
- benefits
- meli_percent
- seller_percent
- buy_quantity
- pay_quantity
- item_discount_percent

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Ítems de promoción

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/$PROMOTION_ID/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista artículos participantes y permite filtrar por artículo, estado y paginar.

**Parámetros**

- `PROMOTION_ID` (path, obligatorio)
- `promotion_type` (query, obligatorio)
- `item_id` (query, opcional)
- `status` (query, opcional): started, pending o candidate.
- `status_item` (query, opcional): active o paused; por defecto active.
- `app_version` (query, obligatorio): La página usa v2.
- `limit` (query, opcional): Predeterminado 50; máximo 50.
- `search_after` (query, opcional): Cursor hacia adelante con vigencia de cinco minutos; anteriormente se aceptaba searchAfter.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- results[].item_id
- results[].status
- results[].price
- results[].original_price
- results[].min_discounted_price
- results[].max_discounted_price
- results[].suggested_discounted_price
- paging

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Parámetros inválidos, por ejemplo status_item no permitido." } ```

**Ejemplos**

- La fuente muestra ejemplos con item_id, status=started y status_item=active.

### Promociones del usuario

**Método:** `GET`  
**Ruta:** `/seller-promotions/users/$USER_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista campañas y promociones relacionadas con el vendedor.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- results
- paging

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Solicitud de ejemplo con app_version=v2.

### Actualizar exclusión del ítem

**Método:** `POST`  
**Ruta:** `/seller-promotions/exclusion-list/item`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega o actualiza el estado de exclusión de una publicación.

**Parámetros**

- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "item_id",
    "exclusion_status (texto true o false)"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Actualizar exclusión del vendedor

**Método:** `POST`  
**Ruta:** `/seller-promotions/exclusion-list/seller`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza el estado de exclusión del vendedor.

**Parámetros**

- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "exclusion_status (texto true o false)"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/central-de-promociones](https://developers.mercadolibre.com.co/es_co/central-de-promociones)  
**Captura:** 2026-10-08T22:51:58.602Z
