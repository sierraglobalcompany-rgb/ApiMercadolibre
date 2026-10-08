---
id: "mensajes-bloqueados"
title: "Mensajes bloqueados"
section: "Guía para productos"
subsection: "Mensajería posventa"
url: "https://developers.mercadolibre.com.co/es_co/mensajes-bloqueados"
source_updated_at: "10/07/2026"
captured_at: "2026-10-08T22:52:06.557Z"
sha256: "b1643164c8a3dec367ff8f8be98c32e6f47edc92727cef7bc4ebd503dc15f8bf"
---

# Mensajes bloqueados

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 10/07/2026  
**Captura:** 2026-10-08T22:52:06.557Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/mensajes-bloqueados](https://developers.mercadolibre.com.co/es_co/mensajes-bloqueados)

## Resumen

Explica cómo consultar una conversación de posventa y leer el estado que indica por qué la mensajería está bloqueada. La respuesta permite distinguir estados y subestados, con motivos que incluyen mediaciones, cancelaciones, reembolsos, restricciones, revisiones, devoluciones y situaciones de asistentes de IA.

## Contenido y conceptos documentados

- La consulta se hace por pack y vendedor, usando `tag=post_sale`. La respuesta incluye `status`, `substatus` y `status_date`; la documentación enumera razones concretas de bloqueo, que determinan si la conversación no está disponible o bajo qué condición.
- La página presenta ejemplos con status/substatus, pero no documenta una operación para desbloquear ni enviar mensajes desde este recurso. Autenticación mostrada: OAuth Bearer. Otros parámetros y errores: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /packs/22175467/sellers/32086568493

La fuente menciona la ruta /packs/22175467/sellers/32086568493, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/packs/22175467/sellers/32086568493`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### GET /messages/packs/{PACK_ID}/sellers/{SELLER_ID}

**Método:** `GET`  
**Ruta:** `/messages/packs/{PACK_ID}/sellers/{SELLER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta los mensajes y el estado de bloqueo de la conversación posventa.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `SELLER_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "paging",
    "conversation_status",
    "status",
    "substatus",
    "status_date",
    "status_update_allowed",
    "claim_ids",
    "shipping_id",
    "messages"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/mensajes-bloqueados](https://developers.mercadolibre.com.co/es_co/mensajes-bloqueados)  
**Captura:** 2026-10-08T22:52:06.557Z
