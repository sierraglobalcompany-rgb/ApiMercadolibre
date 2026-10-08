---
id: "ofertas-del-dia"
title: "Ofertas del día"
section: "Guía para productos"
subsection: "Central de promociones"
url: "https://developers.mercadolibre.com.co/es_co/ofertas-del-dia"
source_updated_at: "22/01/2025"
captured_at: "2026-10-08T22:52:13.326Z"
sha256: "f197f81c364bacc5cdc92b794339a308bfd2e7d252aa28da7eaf3a2bd78a1a86"
---

# Ofertas del día

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 22/01/2025  
**Captura:** 2026-10-08T22:52:13.326Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/ofertas-del-dia](https://developers.mercadolibre.com.co/es_co/ofertas-del-dia)

## Resumen

Describe cómo consultar los ítems de una campaña de Oferta del día, indicar una publicación para participar y retirar el ítem. La campaña se identifica como tipo `DOD` dentro de la API de promociones.

## Contenido y conceptos documentados

- Para consultar ítems se envían `promotion_type=DOD` y `app_version=v2`. La indicación usa `deal_price` y `promotion_type`; la eliminación envía el tipo de promoción en la consulta.
- La respuesta documenta estados del ítem y campos de campaña. Autenticación mostrada: OAuth Bearer. La respuesta puede incluir `id`, fechas, `status`, `price`, `original_price`, `max_discounted_price`, `min_discounted_price` y `stock`. Una oferta ya activada no se elimina durante su ciclo; si se quiere dejar de ofrecerla, se pausa el ítem. Errores: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### DELETE /seller-promotions/items/{ITEM_ID}

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina el ítem de la promoción; usa `app_version=v2` y `promotion_type`.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La fuente usa v2.
- `promotion_type` (query, obligatorio): Tipo de promoción; en esta página DOD.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /seller-promotions/promotions/{PROMOTION_ID}/items

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{PROMOTION_ID}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta ítems de la campaña con `promotion_type=DOD` y `app_version=v2`.

**Parámetros**

- `PROMOTION_ID` (path, obligatorio)
- `promotion_type` (query, obligatorio): Tipo de campaña DOD.
- `app_version` (query, obligatorio): La fuente usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "start_date",
    "finish_date",
    "status",
    "price",
    "original_price",
    "max_discounted_price",
    "min_discounted_price",
    "stock",
    "paging"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /seller-promotions/items/{ITEM_ID}

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Indica un ítem para una promoción con `deal_price` y `promotion_type`.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La fuente usa v2.

**Solicitud**

```json
{
  "fields": [
    "deal_price",
    "promotion_type"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "price",
    "original_price"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/ofertas-del-dia](https://developers.mercadolibre.com.co/es_co/ofertas-del-dia)  
**Captura:** 2026-10-08T22:52:13.326Z
