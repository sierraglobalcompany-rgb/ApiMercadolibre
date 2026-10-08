---
id: "mensajeria-post-venta"
title: "Gestión de mensajes"
section: "Guía para productos"
subsection: "Mensajería posventa"
url: "https://developers.mercadolibre.com.co/es_co/mensajeria-post-venta"
source_updated_at: "27/04/2026"
captured_at: "2026-10-08T22:51:51.425Z"
sha256: "7783477080c943480cee1d53a05b6977c4a6d1cc5a3616500de1ae492eaf4da6"
---

# Gestión de mensajes

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 27/04/2026  
**Captura:** 2026-10-08T22:51:51.425Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/mensajeria-post-venta](https://developers.mercadolibre.com.co/es_co/mensajeria-post-venta)

## Resumen

La documentación describe la mensajería posventa para consultar conversaciones de un pack, obtener un mensaje individual, responder al comprador y adjuntar archivos. Indica que la transición a la nueva arquitectura no incorpora nuevos endpoints públicos ni exige una migración obligatoria; cuando pack_id no está disponible, se conserva la ruta de packs usando order_id como identificador. La fecha de captura y la fecha declarada por la fuente se conservan en esta ficha.

## Contenido y conceptos documentados

- El flujo se identifica con `tag=post_sale`; para listar mensajes se admiten `limit` y `offset`. Los mensajes del comprador moderados no se muestran; los mensajes del vendedor permanecen visibles aunque hayan sido moderados. La página también documenta identificadores de agentes por país y consideraciones de transición.
- Los anexos se cargan como `multipart/form-data` con el campo `file`; la respuesta proporciona el identificador que luego se consulta. La página incluye ejemplos para listar, enviar, consultar mensajes y cargar/obtener anexos.
- Autenticación mostrada: `Authorization: Bearer $ACCESS_TOKEN`. La fuente lista errores 400 por paginación o cuerpo inválido y texto no permitido o mayor a 350 caracteres; 403 por falta de acceso, mediación o envío Full no entregado; 404 por mensaje no encontrado; 422 por clave de anexo inválida y 500 por falla al guardar archivos.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /packs/2000000089077943/seller/415458330

La fuente menciona la ruta /packs/2000000089077943/seller/415458330, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/packs/2000000089077943/seller/415458330`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /packs

La fuente menciona la ruta /packs, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/packs`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /packs/{pack_id}/sellers/{seller_id}/conversations/{type}

La fuente menciona la ruta /packs/{pack_id}/sellers/{seller_id}/conversations/{type}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/packs/{pack_id}/sellers/{seller_id}/conversations/{type}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### GET /messages/attachments/{ATTACHMENT_ID}

**Método:** `GET`  
**Ruta:** `/messages/attachments/{ATTACHMENT_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera un anexo previamente cargado.

**Parámetros**

- `ATTACHMENT_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.
- `site_id` (query, obligatorio): Sitio asociado al anexo.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "summary": "La fuente indica que devuelve el archivo solicitado."
}
```

**Errores documentados**

- ```json {   "code": "422",   "meaning": "Clave de anexo inexistente, inaccesible o ajena al usuario." } ```

**Ejemplos**

- La página incluye ejemplos de llamada y respuesta para este recurso.

### GET /messages/{MESSAGE_ID}

**Método:** `GET`  
**Ruta:** `/messages/{MESSAGE_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el detalle de un mensaje por identificador.

**Parámetros**

- `MESSAGE_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "message_id",
    "date_created",
    "from",
    "to",
    "text",
    "attachments"
  ],
  "summary": "Detalle del mensaje según campos descritos."
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "El identificador de mensaje no existe." } ```
- ```json {   "code": "403",   "meaning": "El usuario no tiene acceso al mensaje." } ```
- ```json {   "code": "404",   "meaning": "El mensaje no puede recuperarse del almacenamiento." } ```

**Ejemplos**

- La página incluye ejemplos de llamada y respuesta para este recurso.

### GET /messages/packs/{PACK_ID}/sellers/{USER_ID}

**Método:** `GET`  
**Ruta:** `/messages/packs/{PACK_ID}/sellers/{USER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista mensajes de la conversación posventa de un pack; la fuente muestra paginación con `limit` y `offset`.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `USER_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa; los ejemplos usan post_sale.
- `limit` (query, opcional): Cantidad de mensajes solicitados.
- `offset` (query, opcional): Desplazamiento de paginación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "messages",
    "paging"
  ],
  "summary": "Lista de mensajes del pack y paginación."
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "limit debe ser mayor que cero; limit u offset inválidos." } ```
- ```json {   "code": "403",   "meaning": "El token no tiene acceso al recurso/orden." } ```

**Ejemplos**

- La página incluye ejemplos de llamada y respuesta para este recurso.

### POST /messages/attachments

**Método:** `POST`  
**Ruta:** `/messages/attachments`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Carga un anexo para el sitio indicado; usa multipart y `file`.

**Parámetros**

- `tag` (query, obligatorio): Identifica el flujo posventa.
- `site_id` (query, obligatorio): Sitio para la carga del anexo.

**Solicitud**

```json
{
  "fields": [
    "file"
  ],
  "content_type": "multipart/form-data"
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Archivo vacío, nombre inválido, más de 25 MB o más de 25 anexos; parámetros/cuerpo inválidos." } ```
- ```json {   "code": "500",   "meaning": "El archivo no se pudo guardar temporalmente." } ```

**Ejemplos**

- La página incluye ejemplos de llamada y respuesta para este recurso.

### POST /messages/packs/{PACK_ID}/sellers/{USER_ID}

**Método:** `POST`  
**Ruta:** `/messages/packs/{PACK_ID}/sellers/{USER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Envía un mensaje al comprador dentro del pack.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `USER_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.

**Solicitud**

```json
{
  "fields": [
    "from",
    "to",
    "text",
    "attachments"
  ],
  "summary": "Cuerpo JSON de mensaje; errores documentan los campos from y to.site_id."
}
```

**Respuesta**

```json
{
  "fields": [
    "message_id",
    "status",
    "text",
    "message_moderation"
  ]
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Texto/cuerpo/receptor/remitente/recurso/site_id inválido; texto máximo 350 caracteres." } ```
- ```json {   "code": "403",   "meaning": "Sin acceso a la orden, mediación activa o envío Full aún no entregado." } ```
- ```json {   "code": "422",   "meaning": "Clave de anexo inexistente, inaccesible o ajena al usuario." } ```

**Ejemplos**

- La página incluye ejemplos de llamada y respuesta para este recurso.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/mensajeria-post-venta](https://developers.mercadolibre.com.co/es_co/mensajeria-post-venta)  
**Captura:** 2026-10-08T22:51:51.425Z
