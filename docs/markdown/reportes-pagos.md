---
id: "reportes-pagos"
title: "Pagos"
section: "Guía para productos"
subsection: "Reportes de Facturación"
url: "https://developers.mercadolibre.com.co/es_co/reportes-pagos"
source_updated_at: "20/05/2025"
captured_at: "2026-10-08T22:52:20.308Z"
sha256: "a0e004780c9de55bca4c5d0daf7472b10d03cf8cf2942c983f874c3f59f24df2"
---

# Pagos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 20/05/2025  
**Captura:** 2026-10-08T22:52:20.308Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/reportes-pagos](https://developers.mercadolibre.com.co/es_co/reportes-pagos)

## Resumen

Documenta la consulta de pagos de facturas de un vendedor dentro de un período y la consulta del detalle de cargos y percepciones asociados a un pago.

## Contenido y conceptos documentados

- El período usa la clave `YYYY-mm-dd`. La consulta admite `sort_by` (`ID` o `DATE`), `order_by` (`ASC` o `DESC`), `offset` (0–10000) y `limit` (1–1000; valor predeterminado 150).
- `payment_id` es de tipo string para admitir identificadores alfanuméricos. El resumen puede incluir `credit_note_number`, fechas, tipo/método/estado, montos aplicados en este u otros períodos, saldo y devolución. El detalle incluye `association_amount`, `payment_amount`, `detail_id`, descripción y fecha del cargo.
- OAuth Bearer aparece en los ejemplos; errores: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### GET /billing/integration/payment/{PAYMENT_ID}/charges

**Método:** `GET`  
**Ruta:** `/billing/integration/payment/{PAYMENT_ID}/charges`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta cargos y percepciones asociados a un pago.

**Parámetros**

- `PAYMENT_ID` (path, obligatorio)
- `sort_by` (query, opcional): Valores ID o DATE.
- `order_by` (query, opcional): Orden ascendente o descendente.
- `offset` (query, opcional): Desplazamiento de resultados.
- `limit` (query, opcional): Límite de resultados; máximo 1000.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "payment_info",
    "charge_info",
    "detail_id",
    "detail_description",
    "detail_date"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /billing/integration/periods/key/{KEY}/group/ML/payment/details

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/{KEY}/group/ML/payment/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalle de facturas/pagos para un período.

**Parámetros**

- `KEY` (path, obligatorio)
- `sort_by` (query, opcional): Valores ID o DATE; predeterminado ID.
- `order_by` (query, opcional): Valores ASC o DESC; predeterminado ASC.
- `offset` (query, opcional): Rango documentado 0 a 10000; predeterminado 0.
- `limit` (query, opcional): Rango 1 a 1000; predeterminado 150.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "payment_id",
    "credit_note_number",
    "payment_date",
    "payment_type",
    "payment_method",
    "payment_status",
    "payment_amount",
    "amount_in_this_period",
    "amount_in_other_period",
    "remaining_amount",
    "return_amount"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/reportes-pagos](https://developers.mercadolibre.com.co/es_co/reportes-pagos)  
**Captura:** 2026-10-08T22:52:20.308Z
