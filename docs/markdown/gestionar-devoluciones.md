---
id: "gestionar-devoluciones"
title: "Devoluciones"
section: "Guía para productos"
subsection: "Reclamos, Devoluciones y Cambios"
url: "https://developers.mercadolibre.com.co/es_co/gestionar-devoluciones"
source_updated_at: "22/12/2025"
captured_at: "2026-10-08T22:51:35.863Z"
sha256: "728d4231cd18ca266288e6ad25c753fa866e449c1558310aecb1b5039f80567b"
---

# Devoluciones

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 22/12/2025  
**Captura:** 2026-10-08T22:51:35.863Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestionar-devoluciones](https://developers.mercadolibre.com.co/es_co/gestionar-devoluciones)

## Resumen

La guía describe la consulta y revisión de devoluciones asociadas a reclamos, la obtención de razones para una revisión fallida, la carga de adjuntos y la consulta de costos de devolución. Las acciones y la evidencia se relacionan con claim_id o return_id según el recurso.

## Contenido y conceptos documentados

- La consulta de devoluciones de un reclamo devuelve identificadores, estado de devolución y dinero, logística, envío y seguimiento; entre los campos visibles aparecen id, last_updated, shipment_id, status, tracking_number, destination, address, refund_at, date_closed, claim_id y resource_id.
- La revisión del triage se consulta por return_id. Para enviar una revisión fallida se utiliza return-review y las razones dependen de flow y claim_id; la página muestra seller_return_failed.
- Los adjuntos se envían como archivo multipart con el campo file y devuelven user_id y file_name. La revisión fallida requiere reason y message; attachments es requerido para SRF2 y SRF4, y order_id solo aplica a una orden concreta en casos carrito. return-cost admite calculate_amount_usd=true.
- Autenticación mostrada: Bearer. La fuente incluye respuestas de reviews y costos, pero algunos detalles de reglas de negocio dependen del flujo del reclamo.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /claims/{CLAIMS}

La fuente menciona la ruta /claims/{CLAIMS}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/{CLAIMS}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /claims/{CLAIM_ID}

La fuente menciona la ruta /claims/{CLAIM_ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/{CLAIM_ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /claims/{CLAIM_ID}/returns/attachments

La fuente menciona la ruta /claims/{CLAIM_ID}/returns/attachments, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/{CLAIM_ID}/returns/attachments`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /shipments/{SHIPMENT_ID}/costs

La fuente menciona la ruta /shipments/{SHIPMENT_ID}/costs, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/shipments/{SHIPMENT_ID}/costs`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar costo de devolución

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/{claim_id}/charges/return-cost`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene información de cargos asociados a la devolución.

**Parámetros**

- `claim_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `calculate_amount_usd` (query, opcional): calculate_amount_usd opcional: true

**Solicitud**

No documentado en la fuente.

**Respuesta**

currency_id y amount; amount_usd aparece cuando calculate_amount_usd=true.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con calculate_amount_usd=true.

### Obtener razones para revisar devolución

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/returns/reasons`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Consulta razones aplicables al flujo del reclamo.

**Parámetros**

- `flow` (query, obligatorio): flow requerido
- `claim_id` (query, obligatorio): claim_id requerido

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista con id, name, detail, position y apply.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo flow=seller_return_failed.

### Consultar revisiones de una devolución

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/returns/{return_id}/reviews`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lee las revisiones o decisiones del triage asociadas a la devolución.

**Parámetros**

- `return_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista reviews con resource, status u otros datos presentados en el ejemplo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta de ejemplo con reviews.

### Consultar devoluciones de un reclamo

**Método:** `GET`  
**Ruta:** `/post-purchase/v2/claims/{claim_id}/returns`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene la devolución asociada al reclamo.

**Parámetros**

- `claim_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Datos de devolución, envío, tracking, dirección, fechas, estado y referencias del reclamo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de objeto de devolución.

### Adjuntar evidencia a devolución

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/{claim_id}/returns/attachments`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Carga evidencia para una revisión fallida.

**Parámetros**

- `claim_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

Multipart/form-data con archivo en campo file.

**Respuesta**

user_id y file_name; file_name identifica la evidencia que se referencia en la revisión.

**Errores documentados**

- 404 not_found_error: claim inexistente.
- bad_request: error al recuperar archivo cargado (por ejemplo, archivo no válido).
- 404 not_found: no se puede obtener el adjunto.

**Ejemplos**

- Ejemplo de carga de archivo PNG.

### Enviar revisión de devolución

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/returns/{return_id}/return-review`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Envía una revisión a la decisión del triage; la fuente muestra el caso conforme y la revisión fallida.

**Parámetros**

- `return_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `reason` (body, opcional): Identificador devuelto por /returns/reasons para la revisión fallida.
- `message` (body, opcional): Mensaje del vendedor requerido para revisión fallida.
- `attachments` (body, opcional): Nombres de archivos; requerido para las razones SRF2 y SRF4.
- `order_id` (body, opcional): Usar solo al revisar una orden específica dentro de un caso carrito.

**Solicitud**

Para revisión OK, {}. Para revisión fallida, arreglo(s) con reason y message; attachments es requerido para SRF2 y SRF4. order_id se usa solo para revisión de una orden en casos carrito.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de revisión conforme con body vacío.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestionar-devoluciones](https://developers.mercadolibre.com.co/es_co/gestionar-devoluciones)  
**Captura:** 2026-10-08T22:51:35.863Z
