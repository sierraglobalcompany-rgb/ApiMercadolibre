---
id: "resumen-percepciones"
title: "Percepciones"
section: "Guía para productos"
subsection: "Reportes de Facturación"
url: "https://developers.mercadolibre.com.co/es_co/resumen-percepciones"
source_updated_at: "12/03/2026"
captured_at: "2026-10-08T22:52:21.229Z"
sha256: "91093b06d25895bb068f27cf23ad079d707cffaf068288a18f8c6bf89fb1b1f2"
---

# Percepciones

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 12/03/2026  
**Captura:** 2026-10-08T22:52:21.229Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/resumen-percepciones](https://developers.mercadolibre.com.co/es_co/resumen-percepciones)

## Resumen

Permite consultar el resumen de percepciones de un período y luego recuperar el detalle de una percepción de Mercado Libre o Mercado Pago. La fuente aclara que esta funcionalidad aplica solamente a Argentina.

## Contenido y conceptos documentados

- El resumen puede filtrarse por grupo de facturación (`ML` o `MP`) y moneda (`USD` o `ARS`). Sus campos incluyen `document_id`, `society`, `legal_document_number`, condición fiscal, monto, tipo/régimen impositivo, base imponible, alícuota, coeficiente, fecha y estado.
- En el detalle se usan datos del resumen: `tax_type` y `document_id`; para Mercado Pago también `tax_id`. El detalle puede variar por régimen e incluye datos como `detail_id`, `taxable_amount`, `tax_amount`, transacción, importes y moneda.
- Autenticación mostrada: OAuth Bearer. Errores no especificados: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### GET /billing/integration/group/ML/perceptions/details

**Método:** `GET`  
**Ruta:** `/billing/integration/group/ML/perceptions/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el detalle de percepciones de Mercado Libre; admite `document_id`, `tax_type`, paginación y moneda.

**Parámetros**

- `document_id` (query, obligatorio): Documento que se consulta.
- `tax_type` (query, obligatorio): Código del tipo de impuesto.
- `offset` (query, opcional): Desplazamiento.
- `limit` (query, opcional): Cantidad de resultados.
- `currency` (query, opcional): Moneda: USD o ARS.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "offset",
    "limit",
    "total",
    "results",
    "detail_id",
    "date_created",
    "taxable_amount",
    "tax_amount",
    "amount",
    "gross_amount",
    "currency",
    "errors"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /billing/integration/group/MP/perceptions/details

**Método:** `GET`  
**Ruta:** `/billing/integration/group/MP/perceptions/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el detalle de percepciones de Mercado Pago; admite además `tax_id`.

**Parámetros**

- `document_id` (query, obligatorio): Documento que se consulta.
- `tax_type` (query, obligatorio): Código del tipo de impuesto.
- `tax_id` (query, obligatorio): Identificador del impuesto requerido en el flujo MP.
- `offset` (query, opcional): Desplazamiento.
- `limit` (query, opcional): Cantidad de resultados.
- `currency` (query, opcional): Moneda: USD o ARS.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "offset",
    "limit",
    "total",
    "results",
    "detail_id",
    "movement_id",
    "reference_id",
    "taxable_amount",
    "tax_amount",
    "amount",
    "gross_amount",
    "currency",
    "errors"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /billing/integration/periods/key/{KEY}/perceptions/summary

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/{KEY}/perceptions/summary`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el resumen de percepciones del período; se muestra filtro `group` y `currency`.

**Parámetros**

- `KEY` (path, obligatorio)
- `group` (query, opcional): Grupo de facturación; ejemplos ML y MP.
- `currency` (query, opcional): Moneda: USD o ARS.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "summary",
    "document_id",
    "society",
    "legal_document_number",
    "amount",
    "tax_type",
    "taxable_amount",
    "aliquot",
    "currency",
    "errors"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/resumen-percepciones](https://developers.mercadolibre.com.co/es_co/resumen-percepciones)  
**Captura:** 2026-10-08T22:52:21.229Z
