---
id: "gestionar-mensaje-de-un-reclamo"
title: "Gestionar mensajes de un reclamo"
section: "Guía para productos"
subsection: "Reclamos"
url: "https://developers.mercadolibre.com.co/es_co/gestionar-mensaje-de-un-reclamo"
source_updated_at: "14/07/2024"
captured_at: "2026-10-08T22:51:55.861Z"
sha256: "52731622bf19f4ac09d4769ef17d0642e73682b9ec9266595d807aebcf8f535a"
---

# Gestionar mensajes de un reclamo

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 14/07/2024  
**Captura:** 2026-10-08T22:51:55.861Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestionar-mensaje-de-un-reclamo](https://developers.mercadolibre.com.co/es_co/gestionar-mensaje-de-un-reclamo)

## Resumen

Documenta el intercambio de mensajes y archivos adjuntos de un reclamo: consultar mensajes propios, cargar adjuntos, enviar un mensaje según las acciones disponibles y consultar o descargar archivos vinculados.

## Contenido y conceptos documentados

### Reglas de mensajería

- Las llamadas usan autenticación `Bearer`. Los adjuntos permitidos son JPG, PNG y PDF hasta 5 MB; el nombre debe tener como máximo 125 caracteres y ajustarse a `[a-zA-Z0-9._-]`.
- Para enviar mensajes, el reclamo debe ofrecer la acción `send_message`. El cuerpo documenta `receiver_role`, `message` y, opcionalmente, los nombres devueltos al cargar adjuntos. El ejemplo de envío devuelve HTTP 201.
- Solo se muestran los mensajes moderados propios. La respuesta incluye remitente/destinatario, mensaje y traducción, fechas, adjuntos, estado, etapa, moderación, repetición y motivo. Se documentan estados `available`, `moderated`, `rejected`, `pending_translation` y resultados de moderación `clean`, `rejected`, `pending`, `non_moderated`; la fuente también presenta `OUT_OF_PLACE_LANGUAGE`.
- Los roles posibles dependen del reclamo; la página indica que `warehouse_dispatcher` no puede enviar mensajes. Los códigos de error por operación: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /claims/{CLAIMS_ID}/messages

La fuente menciona la ruta /claims/{CLAIMS_ID}/messages, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/{CLAIMS_ID}/messages`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar adjunto de mensaje

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/attachments/$ATTACHMENTS_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera metadatos de un archivo adjunto.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)
- `ATTACHMENTS_ID` (path, obligatorio)

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

### Descargar adjunto de mensaje

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/attachments/$ATTACHMENTS_ID/download`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Descarga un archivo adjunto al reclamo.

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

### Consultar mensajes del reclamo

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/messages`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista los mensajes visibles asociados al reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- sender_role
- receiver_role
- message
- translated_message
- date_created
- date_read
- attachments
- status
- stage
- message_moderation
- repeated

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La respuesta considera estados available, moderated, rejected y pending_translation; moderación clean, rejected, pending o non_moderated.

### Enviar mensaje en reclamo

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/actions/send-message`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Envía un mensaje a un rol participante si la acción está disponible para el reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "receiver_role",
    "message",
    "attachments (nombres de archivos, opcional)"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente indica HTTP 201 Created; requiere acción send_message y warehouse_dispatcher no puede enviar.

### Cargar adjunto del mensaje

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/attachments`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Carga un archivo para adjuntarlo a un mensaje del reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "multipart/form-data",
  "fields": [
    "file (JPG, PNG o PDF; máximo 5 MB)",
    "filename (hasta 125 caracteres; patrón [a-zA-Z0-9._-])"
  ]
}
```

**Respuesta**

- filename

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Referencia HTTP GET /claims/{CLAIMS_ID}/messages

**Método:** `GET`  
**Ruta:** `/claims/{CLAIMS_ID}/messages`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /claims/{CLAIMS_ID}/messages. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP POST /post-purchase/v1/claims/5204934310/act

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/5204934310/act`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /post-purchase/v1/claims/5204934310/act. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP POST /post-purchase/v1/claims/{CLAIM_ID}/actions/se

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/{CLAIM_ID}/actions/se`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /post-purchase/v1/claims/{CLAIM_ID}/actions/se. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestionar-mensaje-de-un-reclamo](https://developers.mercadolibre.com.co/es_co/gestionar-mensaje-de-un-reclamo)  
**Captura:** 2026-10-08T22:51:55.861Z
