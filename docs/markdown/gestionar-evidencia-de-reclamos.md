---
id: "gestionar-evidencia-de-reclamos"
title: "Gestionar evidencia de reclamos"
section: "Guía para productos"
subsection: "Reclamos"
url: "https://developers.mercadolibre.com.co/es_co/gestionar-evidencia-de-reclamos"
source_updated_at: "13/04/2025"
captured_at: "2026-10-08T22:51:53.737Z"
sha256: "3c54d3f4fd5a3e3db70e0a360e86dc3ec9137f8744be6db7d594426450c4c605"
---

# Gestionar evidencia de reclamos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/04/2025  
**Captura:** 2026-10-08T22:51:53.737Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestionar-evidencia-de-reclamos](https://developers.mercadolibre.com.co/es_co/gestionar-evidencia-de-reclamos)

## Resumen

Describe la gestión de evidencias de envío en reclamos: consultar evidencias, subir y descargar archivos, registrar datos de despacho/entrega y declarar una gestión o promesa de envío. El recurso se organiza por identificador de reclamo.

## Contenido y conceptos documentados

### Evidencias y restricciones

- Las llamadas documentan autenticación `Bearer`. Los adjuntos admiten JPG, PNG o PDF de hasta 5 MB; la subida devuelve metadatos del archivo y un identificador que se usa en la ruta de consulta/descarga. La solicitud de ejemplo incluye el encabezado `x-public: true`.
- La evidencia de envío contiene datos como tipo, método/empresa de envío, agencia de destino, fechas, datos del receptor, número de seguimiento y adjuntos. La página distingue entrega por correo, encomienda, entrega personal y correo electrónico, con requisitos de datos según modalidad.
- Las fechas pueden seguir formato largo o corto según el ejemplo. No se deben remitir evidencias de envío en una mediación/disputa; una evidencia enviada no se puede modificar.
- Los códigos de error por operación y los cuerpos de respuesta que la captura no detalla: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /claims/actions/evidences

La fuente menciona la ruta /claims/actions/evidences, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/actions/evidences`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar adjunto de evidencia

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/attachments-evidences/$ATTACHMENT_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene metadatos del archivo adjunto a una evidencia.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)
- `ATTACHMENT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- filename
- original_filename
- size
- date_created
- type

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Descargar adjunto de evidencia

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/attachments-evidences/$ATTACHMENTS_ID/download`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Descarga el archivo asociado a la evidencia.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)
- `ATTACHMENTS_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Listar evidencias del reclamo

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/evidences`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera las evidencias de envío asociadas a un reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- attachments
- type
- date_shipped
- date_delivered
- destination_agency
- receiver_email
- receiver_id
- receiver_name
- shipping_company_name
- shipping_method
- tracking_number
- handling_date

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de consulta de evidencias por reclamo.

### Registrar evidencia de envío

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/actions/evidences`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Registra evidencia de despacho o entrega para el reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "type",
    "shipping_method",
    "shipping_company_name",
    "destination_agency",
    "date_shipped",
    "date_delivered",
    "receiver_email",
    "receiver_id",
    "receiver_name",
    "tracking_number",
    "attachments"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra ejemplos diferenciados por modalidad: mail, entrusted, personal_delivery y email; los campos requeridos dependen del tipo.

### Cargar adjunto de evidencia

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/attachments-evidences`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Carga un archivo para asociarlo como evidencia del reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "multipart/form-data",
  "fields": [
    "file (JPG, PNG o PDF; máximo 5 MB)"
  ]
}
```

**Respuesta**

- user_id
- file_name
- attachment_id (file_name)

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El ejemplo de carga usa el encabezado x-public: true.

### Registrar gestión de envío

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/evidences`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Registra una gestión/promesa de envío del reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "type: handling_shipping_evidence",
    "handling_date"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Referencia HTTP POST /claims/actions/evidences

**Método:** `POST`  
**Ruta:** `/claims/actions/evidences`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /claims/actions/evidences. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

### Referencia HTTP POST /post-purchase/v1/claims/949903015/act

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/949903015/act`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /post-purchase/v1/claims/949903015/act. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestionar-evidencia-de-reclamos](https://developers.mercadolibre.com.co/es_co/gestionar-evidencia-de-reclamos)  
**Captura:** 2026-10-08T22:51:53.737Z
