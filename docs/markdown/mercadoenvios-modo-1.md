---
id: "mercadoenvios-modo-1"
title: "Mercado Envíos 1"
section: "Guía para productos"
subsection: "Mercado Envíos 1"
url: "https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-1"
source_updated_at: "06/02/2026"
captured_at: "2026-10-08T22:52:08.527Z"
sha256: "83906ba1b864e923a3a1b503f6869451fde64e24fbde0d3a78f7f3014576dbda"
---

# Mercado Envíos 1

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 06/02/2026  
**Captura:** 2026-10-08T22:52:08.527Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-1](https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-1)

## Resumen

Explica cómo habilitar Mercado Envíos 1 para vendedores, publicar un ítem con esa modalidad, activarla en una publicación existente y consultar sus envíos. También presenta alertas relacionadas con fraude.

## Contenido y conceptos documentados

- Para publicar, los ejemplos configuran `shipping.mode` como `me1`; la activación sobre ítems existentes se realiza actualizando el ítem. La consulta de envíos se hace por `SHIPMENT_ID`.
- La documentación separa activación a nivel vendedor y a nivel ítem. Los ejemplos de publicación usan `shipping.mode=me1`, `local_pick_up` y `dimensions`. Una orden con tag `fraud_risk_detected` no debe enviarse al comprador. Autenticación mostrada: OAuth Bearer.

## Operaciones de API
## Operaciones de API

### GET /shipments/{SHIPMENT_ID}

**Método:** `GET`  
**Ruta:** `/shipments/{SHIPMENT_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el envío asociado a ME1.

**Parámetros**

- `SHIPMENT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "status",
    "substatus",
    "mode",
    "logistic_type"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /items

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Publica un ítem configurado con ME1.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "shipping.mode"
  ],
  "summary": "El ejemplo configura shipping.mode como me1."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /items/{ITEM_ID}

**Método:** `POST`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Publica/configura ME1 según el flujo ejemplificado para un ítem.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### PUT /items/{ITEM_ID}

**Método:** `PUT`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Activa ME1 en un ítem existente.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "shipping.mode"
  ],
  "summary": "El ejemplo actualiza la modalidad a me1."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-1](https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-1)  
**Captura:** 2026-10-08T22:52:08.527Z
