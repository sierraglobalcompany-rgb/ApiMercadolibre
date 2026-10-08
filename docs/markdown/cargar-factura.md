---
id: "cargar-factura"
title: "Cargar y Obtener Facturas - Emisión Propia"
section: "Guía para productos"
subsection: "Facturación"
url: "https://developers.mercadolibre.com.co/es_co/cargar-factura"
source_updated_at: "16/03/2026"
captured_at: "2026-10-08T22:51:15.123Z"
sha256: "9efb332eefe9d1e9fb02fb66cfcf6c3f84aa8efb067e264b1bea4502be5670bd"
---

# Cargar y Obtener Facturas - Emisión Propia

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 16/03/2026  
**Captura:** 2026-10-08T22:51:15.123Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/cargar-factura](https://developers.mercadolibre.com.co/es_co/cargar-factura)

## Resumen

Documenta la carga, consulta y eliminación de facturas fiscales asociadas a un pack/orden. La integración permite adjuntar archivos, recuperar sus identificadores y descargar el documento asociado.

## Contenido y conceptos documentados

- La carga utiliza el recurso del pack; si `pack_id` es nulo, la guía indica usar el `order_id` como valor, conservando el recurso `/packs`.
- Se documentan facturas en PDF y XML (`application/pdf`, `application/xml`, `text/xml`). La página describe validaciones de autorización, tipo, tamaño, archivo vacío, cantidad de adjuntos y modalidad de envío.
- La respuesta de carga entrega una lista `ids`; cada identificador se usa para consultar un documento. También se documenta consultar los IDs asociados y eliminar facturas del pack.
- Códigos mostrados en las respuestas: 400 por archivo/datos vacíos o inválidos; 403 por autorización/acceso; 404 por pack o documento inexistente; 406 por texto de consulta no aceptable; 409 por conflicto con archivos ya adjuntos; 500 al recuperar el body de una solicitud de datos fiscales.

**Campos y respuestas:** `pack_id`, `fiscal_document_id` y respuesta de carga `ids`.

**Ejemplos documentados:** carga de factura, consulta de IDs, descarga de factura y eliminación del documento del pack.

## Operaciones de API

## Conceptos y recursos asociados

### Cargar y Obtener Facturas - Emisión Propia

Documenta la carga, consulta y eliminación de facturas fiscales asociadas a un pack/orden. La integración permite adjuntar archivos, recuperar sus identificadores y descargar el documento asociado.

**Respuesta**

```json
{
  "fields": "`pack_id`, `fiscal_document_id` y respuesta de carga `ids`."
}
```

**Errores documentados**

- 400: archivo/datos vacíos o inválidos.
- 403: autorización/acceso denegados.
- 404: pack o documento inexistente.
- 406: texto de consulta no aceptable.
- 409: conflicto con archivos ya adjuntos.
- 500: error al recuperar el body en solicitud de datos fiscales.

**Ejemplos documentados**

- carga de factura, consulta de IDs, descarga de factura y eliminación del documento del pack.
### Ruta mencionada /orders/

La fuente menciona la ruta /orders/, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/orders/`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Elimina facturas asociadas al pack

**Método:** `DELETE`  
**Ruta:** `/packs/{pack_id}/fiscal_documents`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina facturas asociadas al pack.

**Parámetros**

- `pack_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 403: usuario no autorizado.
- 404: el pack no tiene factura adjunta.

**Ejemplos**

- carga de factura, consulta de IDs, descarga de factura y eliminación del documento del pack.

### Obtiene los IDs de las facturas asociadas

**Método:** `GET`  
**Ruta:** `/packs/{pack_id}/fiscal_documents`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los IDs de las facturas asociadas.

**Parámetros**

- `pack_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "ids"
  ]
}
```

**Errores documentados**

- 403: usuario no autorizado.
- 404: pack sin documentos o sin factura del usuario.

**Ejemplos**

- carga de factura, consulta de IDs, descarga de factura y eliminación del documento del pack.

### Recupera una factura específica

**Método:** `GET`  
**Ruta:** `/packs/{pack_id}/fiscal_documents/{fiscal_document_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera una factura específica.

**Parámetros**

- `pack_id` (path, obligatorio): Variable de ruta documentada.
- `fiscal_document_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: identificador de documento inexistente.
- 403: usuario no autorizado.
- 404: documento no recuperable del almacenamiento.

**Ejemplos**

- carga de factura, consulta de IDs, descarga de factura y eliminación del documento del pack.

### Adjunta factura(s) al pack

**Método:** `POST`  
**Ruta:** `/packs/{pack_id}/fiscal_documents`  
**Autenticación:** No documentado en la fuente.

Adjunta factura(s) al pack.

**Parámetros**

- `pack_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

```json
{
  "content_types": [
    "application/pdf",
    "application/xml",
    "text/xml"
  ],
  "note": "Adjunto fiscal; nombre y límite exacto dependen de las validaciones descritas."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: archivo vacío, tipo/tamaño/nombre no válido.
- 403: falta de autorización o sitio no habilitado.
- 409: ya existe adjunto o se excede cantidad por tipo.

**Ejemplos**

- carga de factura, consulta de IDs, descarga de factura y eliminación del documento del pack.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/cargar-factura](https://developers.mercadolibre.com.co/es_co/cargar-factura)  
**Captura:** 2026-10-08T22:51:15.123Z
