---
id: "reportes-descargas"
title: "Descargas"
section: "Guía para productos"
subsection: "Reportes de Facturación"
url: "https://developers.mercadolibre.com.co/es_co/reportes-descargas"
source_updated_at: "25/04/2024"
captured_at: "2026-10-08T22:51:33.064Z"
sha256: "a0cb93a5452af5b254ce39917c6db62e247b34febb09e32dc8f558e67b887526"
---

# Descargas

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 25/04/2024  
**Captura:** 2026-10-08T22:51:33.064Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/reportes-descargas](https://developers.mercadolibre.com.co/es_co/reportes-descargas)

## Resumen

Describe el ciclo de generación, consulta y descarga de reportes de facturación, además de la descarga del PDF de un documento legal. La generación devuelve un file_id; el cliente debe consultar su estado y descargar el archivo cuando figure READY.

## Contenido y conceptos documentados

- La generación recibe group, document_type y report_format. La página enumera grupos ML, MP, FLEX, FULL, INSURTECH y PAYMENT; el ejemplo usa BILL y CSV.
- Los estados documentados son PROCESSING, READY y ERROR. Si la generación falla, la fuente indica volver a consultar; la descarga del reporte se realiza después de READY.
- La descarga de documentos legales requiere el file_id obtenido mediante otro recurso; esta página no detalla aquí la operación que entrega ese identificador.
- Autenticación mostrada: Bearer. Los ejemplos de consulta y descarga usan document_type=BILL como parámetro de consulta.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Descargar documento legal

**Método:** `GET`  
**Ruta:** `/billing/integration/legal_document/{file_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Descarga un documento legal en formato PDF usando su file_id.

**Parámetros**

- `file_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Archivo PDF.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta indicada como descarga del PDF.

### Descargar reporte

**Método:** `GET`  
**Ruta:** `/billing/integration/reports/{file_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Descarga el archivo generado cuando su estado es READY.

**Parámetros**

- `file_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `document_type` (query, opcional): document_type (ejemplo: BILL)

**Solicitud**

No documentado en la fuente.

**Respuesta**

Archivo del reporte; el formato se define al generarlo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de descarga de reporte CSV.

### Consultar estado de generación

**Método:** `GET`  
**Ruta:** `/billing/integration/reports/{file_id}/status`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Devuelve el estado del reporte solicitado.

**Parámetros**

- `file_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `document_type` (query, opcional): document_type (ejemplo: BILL)

**Solicitud**

No documentado en la fuente.

**Respuesta**

status: PROCESSING, READY o ERROR.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta de ejemplo con status PROCESSING.

### Solicitar reporte de facturación

**Método:** `POST`  
**Ruta:** `/billing/integration/periods/key/{key}/reports`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Solicita generar un reporte para una clave de período.

**Parámetros**

- `key` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `group` (body, obligatorio): Grupo de reporte.
- `document_type` (body, obligatorio): Tipo de documento, ejemplo BILL.
- `report_format` (body, obligatorio): Formato, ejemplo CSV.

**Solicitud**

JSON con group, document_type y report_format.

**Respuesta**

Identificador fileId para seguir el proceso.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo group=ML, document_type=BILL, report_format=CSV.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/reportes-descargas](https://developers.mercadolibre.com.co/es_co/reportes-descargas)  
**Captura:** 2026-10-08T22:51:33.064Z
