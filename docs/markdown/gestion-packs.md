---
id: "gestion-packs"
title: "Packs"
section: "Guía para productos"
subsection: "Gestionar ventas"
url: "https://developers.mercadolibre.com.co/es_co/gestion-packs"
source_updated_at: "29/12/2025"
captured_at: "2026-10-08T22:52:18.512Z"
sha256: "730ef3e7f2218a955f27b2d22bebfade9e4f369d8dd3df5cde9f2a2c33ada042"
---

# Packs

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:52:18.512Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestion-packs](https://developers.mercadolibre.com.co/es_co/gestion-packs)

## Resumen

Describe la relación entre packs, órdenes, pagos y envíos para gestionar ventas agrupadas. El flujo consulta primero el pack, luego sus órdenes, y obtiene los detalles de envío desde el recurso de shipments.

## Contenido y conceptos documentados

- Los cupones y descuentos no deben interpretarse solo desde `discount` en el nodo de pagos de la orden; la fuente recomienda los recursos específicos de descuentos/promociones. Para despachar, el vendedor puede marcar que ya tiene el producto mediante `ready_to_ship`.
- Los ejemplos usan OAuth Bearer. Los esquemas completos de pack y orden: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /api.mercadopago.com/v1/payments/{id}

La fuente menciona la ruta /api.mercadopago.com/v1/payments/{id}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/api.mercadopago.com/v1/payments/{id}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /orders/{ORDER_ID}/discounts

La fuente menciona la ruta /orders/{ORDER_ID}/discounts, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/orders/{ORDER_ID}/discounts`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### GET /orders/{ORDER_ID}

**Método:** `GET`  
**Ruta:** `/orders/{ORDER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el detalle de una orden del pack.

**Parámetros**

- `ORDER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "order_items",
    "payments",
    "shipping"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /packs/{PACK_ID}

**Método:** `GET`  
**Ruta:** `/packs/{PACK_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el pack y sus órdenes vinculadas.

**Parámetros**

- `PACK_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "orders"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /shipments/{SHIPMENT_ID}/process/ready_to_ship

**Método:** `POST`  
**Ruta:** `/shipments/{SHIPMENT_ID}/process/ready_to_ship`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Marca disponibilidad del producto para iniciar el despacho.

**Parámetros**

- `SHIPMENT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestion-packs](https://developers.mercadolibre.com.co/es_co/gestion-packs)  
**Captura:** 2026-10-08T22:52:18.512Z
