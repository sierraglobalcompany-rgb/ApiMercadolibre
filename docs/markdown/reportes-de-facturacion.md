---
id: "reportes-de-facturacion"
title: "Reportes de Facturación"
section: "Guía para productos"
subsection: "Reportes de Facturación"
url: "https://developers.mercadolibre.com.co/es_co/reportes-de-facturacion"
source_updated_at: "03/03/2026"
captured_at: "2026-10-08T22:52:45.129Z"
sha256: "3771e88a50c260e88dcb8952bcc391b54d083a1f4a706b03fb2d4bedef117627"
---

# Reportes de Facturación

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 03/03/2026  
**Captura:** 2026-10-08T22:52:45.129Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/reportes-de-facturacion](https://developers.mercadolibre.com.co/es_co/reportes-de-facturacion)

## Resumen

Documenta la consulta de períodos mensuales, documentos de facturación y resumen/detalle de cargos para Mercado Libre y Mercado Pago. Los informes permiten consultar facturas y notas de crédito y paginar sus resultados.

## Contenido y conceptos documentados

### Parámetros y uso

- Las llamadas usan Bearer y el parámetro `group` (`ML` o `MP`); la página indica que si se omite se puede obtener información de ambos grupos. `document_type` acepta `BILL` y `CREDIT_NOTE`.
- Los períodos admiten `offset` y `limit`; la consulta de períodos devuelve seis por defecto y permite hasta doce. Para documentos, `limit` tiene máximo 1000; la página recomienda paginar y no repetir consultas innecesarias.
- La respuesta de documentos agrega estado/IDs de documentos, importes, períodos, monedas, cantidades y archivos. El resumen puede incluir cargos, pagos cobrados, descuentos, créditos y deuda.
- Se documentan HTTP 206 (respuesta parcial/incompleta) y 429 (bloqueo preventivo por exceso de solicitudes desde IP). La página recomienda usar paginación y evitar llamadas repetitivas.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /billing/monthly/periods

La fuente menciona la ruta /billing/monthly/periods, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/billing/monthly/periods`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Períodos mensuales de facturación

**Método:** `GET`  
**Ruta:** `/billing/integration/monthly/periods`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista períodos recientes por grupo y tipo de documento.

**Parámetros**

- `group` (query): ML o MP; la página indica ambos grupos si se omite.
- `document_type` (query, obligatorio): BILL o CREDIT_NOTE.
- `offset` (query, opcional)
- `limit` (query, opcional): La página indica períodos por defecto y máximo de 12.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- offset
- limit
- total
- results[].amount
- results[].period.date_from
- results[].period.date_to
- results[].period.key
- results[].period.period_status

**Errores documentados**

- ```json {   "code": 206,   "meaning": "Respuesta parcial/incompleta." } ```
- ```json {   "code": 429,   "meaning": "Bloqueo preventivo por límite de solicitudes desde IP." } ```

**Ejemplos**

- El ejemplo solicita group=MP, document_type=BILL, offset y limit.

### Documentos de un período

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/$KEY/documents`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista facturas o notas de crédito del período indicado.

**Parámetros**

- `KEY` (path, obligatorio)
- `group` (query): ML o MP.
- `document_type` (query, obligatorio): BILL o CREDIT_NOTE.
- `offset` (query, opcional)
- `limit` (query, opcional): Máximo 1000.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- offset
- limit
- total
- results[].id
- results[].document_type
- results[].document_status
- results[].associated_document_id
- results[].currency_id
- results[].files

**Errores documentados**

- ```json {   "code": 206,   "meaning": "Respuesta parcial/incompleta." } ```
- ```json {   "code": 429,   "meaning": "Bloqueo preventivo por límite de solicitudes desde IP." } ```

**Ejemplos**

- La página incluye ejemplo de documentos de un período mensual.

### Resumen y detalle de facturación

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/$KEY/summary/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera cargos, pagos, créditos, cobros y deuda del período.

**Parámetros**

- `KEY` (path, obligatorio)
- `group` (query): ML o MP.
- `document_type` (query): BILL o CREDIT_NOTE, cuando aplique.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- user
- nickname
- bill_includes
- total_amount
- total_perceptions
- bonuses
- charges
- payment_collected
- operation_discount
- total_payment
- total_credit_note
- total_collected
- total_debt

**Errores documentados**

- ```json {   "code": 206,   "meaning": "Respuesta parcial/incompleta." } ```
- ```json {   "code": 429,   "meaning": "Bloqueo preventivo por límite de solicitudes desde IP." } ```

**Ejemplos**

- La fuente recomienda consumo secuencial, no batch, y una consulta diaria por usuario.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/reportes-de-facturacion](https://developers.mercadolibre.com.co/es_co/reportes-de-facturacion)  
**Captura:** 2026-10-08T22:52:45.129Z
