---
id: "buenas-practicas-para-el-consumo-de-las-apis-de-reportes-de-facturacion"
title: "Buenas Prácticas para el Consumo de las APIs de Reportes de Facturación"
section: "Guía para productos"
subsection: "Reportes de Facturación"
url: "https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-el-consumo-de-las-apis-de-reportes-de-facturacion"
source_updated_at: "08/06/2026"
captured_at: "2026-10-08T22:51:03.392Z"
sha256: "64a9add6c4c4764fca01bf2ff84c4566726693725b903822aef72e7d83564de0"
---

# Buenas Prácticas para el Consumo de las APIs de Reportes de Facturación

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 08/06/2026  
**Captura:** 2026-10-08T22:51:03.392Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-el-consumo-de-las-apis-de-reportes-de-facturacion](https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-el-consumo-de-las-apis-de-reportes-de-facturacion)

## Resumen

Explica el consumo de reportes de facturación de Mercado Libre y Mercado Pago para conciliación fiscal y posventa. Recomienda consultar períodos, documentos y detalles con paginación y caché, sin usar estos recursos para operaciones en tiempo real.

## Contenido y conceptos documentados

- Los grupos de facturación son `ML` (Mercado Libre) y `MP` (Mercado Pago). La guía indica el parámetro global `group`; también señala que, al omitirlo, se obtiene información de ambos grupos.
- Los documentos admiten filtros `document_id` y `document_type` (`BILL` o `CREDIT_NOTE`). Para detalles se muestran `offset`, `limit`, `from_id`, `sort_by` y `order_by`.
- La clave mensual sigue `YYYY-MM-01`. Se recomienda consultar períodos una vez, derivar la clave y usar caché; evitar polling y lotes masivos.
- El flujo propuesto es obtener el período, recuperar documentos y consultar detalles por grupo. El resumen se recomienda consumir secuencialmente una vez al día.
- Para órdenes en tiempo real la guía remite a recursos operativos distintos. El error 429 indica exceso de solicitudes/bloqueo preventivo por IP; reducir frecuencia, usar caché y evitar batch.

**Campos y respuestas:** la guía describe períodos, documentos, detalles de facturación y descargas de documentos/reportes; los esquemas completos de respuesta no están documentados aquí.

**Ejemplos documentados:** paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

## Operaciones de API

## Conceptos y recursos asociados

### Buenas Prácticas para el Consumo de las APIs de Reportes de Facturación

Explica el consumo de reportes de facturación de Mercado Libre y Mercado Pago para conciliación fiscal y posventa. Recomienda consultar períodos, documentos y detalles con paginación y caché, sin usar estos recursos para operaciones en tiempo real.

**Respuesta**

```json
{
  "fields": "la guía describe períodos, documentos, detalles de facturación y descargas de documentos/reportes; los esquemas completos de respuesta no están documentados aquí."
}
```

**Errores documentados**

- 429 Too Many Requests: bloqueo preventivo por IP; reducir frecuencia, implementar caché y evitar batch masivo.

**Ejemplos documentados**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.
## Operaciones de API

### Consulta detalles por orden o pack

**Método:** `GET`  
**Ruta:** `/billing/integration/group/ML/order/details`  
**Autenticación:** No documentado en la fuente.

Consulta detalles por orden o pack.

**Parámetros**

- `order_ids` (query): Parámetro documentado.
- `group` (query): Grupo ML/MP; al omitirlo retorna ambos grupos según la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Descarga documento legal

**Método:** `GET`  
**Ruta:** `/billing/integration/legal_document/{file_id}`  
**Autenticación:** No documentado en la fuente.

Descarga documento legal.

**Parámetros**

- `file_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Lista períodos de facturación

**Método:** `GET`  
**Ruta:** `/billing/integration/monthly/periods`  
**Autenticación:** No documentado en la fuente.

Lista períodos de facturación.

**Parámetros**

- `group` (query): Grupo ML/MP; al omitirlo retorna ambos grupos según la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Lista documentos del período; admite tipo, identificador y paginación

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/{key}/documents`  
**Autenticación:** No documentado en la fuente.

Lista documentos del período; admite tipo, identificador y paginación.

**Parámetros**

- `key` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `group` (query): Grupo ML/MP; al omitirlo retorna ambos grupos según la fuente.
- `document_id` (query): Parámetro documentado.
- `document_type` (query): Tipo BILL o CREDIT_NOTE.
- `offset` (query): Paginación.
- `limit` (query): Paginación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Consulta detalles ML con paginación

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/{key}/group/ML/details`  
**Autenticación:** No documentado en la fuente.

Consulta detalles ML con paginación.

**Parámetros**

- `key` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `document_type` (query): Tipo BILL o CREDIT_NOTE.
- `limit` (query): Paginación.
- `from_id` (query): Cursor de paginación.
- `sort_by` (query): Ordenamiento documentado.
- `order_by` (query): Ordenamiento documentado.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Consulta detalles de pagos ML

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/{key}/group/ML/payment/details`  
**Autenticación:** No documentado en la fuente.

Consulta detalles de pagos ML.

**Parámetros**

- `key` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `document_type` (query): Tipo BILL o CREDIT_NOTE.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Consulta detalles MP con paginación

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/{key}/group/MP/details`  
**Autenticación:** No documentado en la fuente.

Consulta detalles MP con paginación.

**Parámetros**

- `key` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `document_type` (query): Tipo BILL o CREDIT_NOTE.
- `limit` (query): Paginación.
- `from_id` (query): Cursor de paginación.
- `sort_by` (query): Ordenamiento documentado.
- `order_by` (query): Ordenamiento documentado.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Resumen de percepciones, exclusivo para MLA

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/{key}/perceptions/summary`  
**Autenticación:** No documentado en la fuente.

Resumen de percepciones, exclusivo para MLA.

**Parámetros**

- `key` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Consulta resumen del período

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/{key}/summary/details`  
**Autenticación:** No documentado en la fuente.

Consulta resumen del período.

**Parámetros**

- `key` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `group` (query): Grupo ML/MP; al omitirlo retorna ambos grupos según la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Descarga reporte CSV/XLSX generado previamente

**Método:** `GET`  
**Ruta:** `/billing/integration/reports/{file_id}`  
**Autenticación:** No documentado en la fuente.

Descarga reporte CSV/XLSX generado previamente.

**Parámetros**

- `file_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Consulta el precio de venta de un ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}/sale_price`  
**Autenticación:** No documentado en la fuente.

Consulta el precio de venta de un ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Consulta datos de órdenes en tiempo real

**Método:** `GET`  
**Ruta:** `/orders`  
**Autenticación:** No documentado en la fuente.

Consulta datos de órdenes en tiempo real.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Consulta descuentos aplicados a una orden

**Método:** `GET`  
**Ruta:** `/orders/{id}/discounts`  
**Autenticación:** No documentado en la fuente.

Consulta descuentos aplicados a una orden.

**Parámetros**

- `id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Identifica órdenes agrupadas en packs

**Método:** `GET`  
**Ruta:** `/packs`  
**Autenticación:** No documentado en la fuente.

Identifica órdenes agrupadas en packs.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Consulta costos de envío

**Método:** `GET`  
**Ruta:** `/shipments`  
**Autenticación:** No documentado en la fuente.

Consulta costos de envío.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-el-consumo-de-las-apis-de-reportes-de-facturacion](https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-el-consumo-de-las-apis-de-reportes-de-facturacion)  
**Captura:** 2026-10-08T22:51:03.392Z
