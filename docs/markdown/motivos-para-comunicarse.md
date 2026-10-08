---
id: "motivos-para-comunicarse"
title: "Motivos para comunicarse"
section: "Guía para productos"
subsection: "Mensajería posventa"
url: "https://developers.mercadolibre.com.co/es_co/motivos-para-comunicarse"
source_updated_at: "29/09/2026"
captured_at: "2026-10-08T22:52:10.373Z"
sha256: "05abb9e9f8305efc8d03ec6140aec110f298b02836a76fe995216eb442b3e4da"
---

# Motivos para comunicarse

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/09/2026  
**Captura:** 2026-10-08T22:52:10.373Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/motivos-para-comunicarse](https://developers.mercadolibre.com.co/es_co/motivos-para-comunicarse)

## Resumen

Documenta el catálogo de motivos y opciones de comunicación posventa, la cantidad de mensajes disponibles y el envío de mensajes con plantillas o texto libre. También incluye la promesa de entrega y plantillas que dependen del país.

## Contenido y conceptos documentados

- El flujo consulta opciones para un pack, revisa las capacidades disponibles y envía la opción seleccionada. Los cuerpos usan `option_id`; según el caso también `template_id`, `text` o datos de promesa de entrega. Después de la respuesta del comprador, los mensajes siguientes se envían por el recurso de mensajería habitual. Las opciones exponen `option_id`, `template_id`, `char_limit`, `child_options` y `cap_available`; algunas plantillas requieren variables `vars`.
- La disponibilidad puede ser cero, caso en el que no se permiten mensajes. Se muestran templates localizados por sitio y ejemplos de errores. Autenticación mostrada: OAuth Bearer; el ejemplo usa `tag=post_sale`.

## Operaciones de API
## Operaciones de API

### GET /messages/action_guide/packs/{PACK_ID}

**Método:** `GET`  
**Ruta:** `/messages/action_guide/packs/{PACK_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta los motivos/opciones de comunicación disponibles para el pack.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "options",
    "option_id",
    "template_id",
    "char_limit",
    "child_options",
    "cap_available"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /messages/action_guide/packs/{PACK_ID}/caps_available

**Método:** `GET`  
**Ruta:** `/messages/action_guide/packs/{PACK_ID}/caps_available`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la capacidad disponible para enviar mensajes.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "cap_available"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /messages/action_guide/packs/{PACK_ID}/option

**Método:** `POST`  
**Ruta:** `/messages/action_guide/packs/{PACK_ID}/option`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Envía una opción; el cuerpo puede incluir `option_id`, `template_id` y, para opción libre, `text`.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.

**Solicitud**

```json
{
  "fields": [
    "option_id",
    "template_id",
    "text",
    "vars"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "id",
    "status",
    "text",
    "message_date",
    "message_moderation"
  ]
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Texto supera el límite; errores de solicitud por caso exceptuado." } ```
- ```json {   "code": "403",   "meaning": "Cap no disponible o conversación bloqueada." } ```
- ```json {   "code": "404",   "meaning": "option_id no válido." } ```
- ```json {   "code": "409",   "meaning": "Otra solicitud está bloqueando la operación." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/motivos-para-comunicarse](https://developers.mercadolibre.com.co/es_co/motivos-para-comunicarse)  
**Captura:** 2026-10-08T22:52:10.373Z
