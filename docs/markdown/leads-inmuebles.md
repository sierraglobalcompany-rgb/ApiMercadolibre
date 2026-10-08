---
id: "leads-inmuebles"
title: "Leads"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/leads-inmuebles"
source_updated_at: "07/05/2026"
captured_at: "2026-10-08T22:50:42.774Z"
sha256: "90ac715da9ef469e32af27189589329a8250011a8da933cf5a3da9fb26cd9bb9"
---

# Leads

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 07/05/2026  
**Captura:** 2026-10-08T22:50:42.774Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/leads-inmuebles](https://developers.mercadolibre.com.co/es_co/leads-inmuebles)

## Resumen

Un lead representa un contacto de un comprador con una publicación: WhatsApp, pregunta, llamada, agenda de visita o cotización. La guía explica cómo consultar los interesados de un vendedor, filtrar por período/tipo/ítem/comprador, paginar los resultados y recuperar un detalle de lead o el texto de una pregunta asociada.

## Contenido y conceptos documentados

- Los filtros temporales son date_from y date_to; la paginación usa offset y limit. El valor por defecto documentado es offset=0, limit=10 y un rango de los últimos siete días.
- contact_types acepta whatsapp, question, call, schedule y quotation. schedule puede retornar vacío si el ítem no ofrece la función.
- include_guest=true agrega guest y summary. Los leads guest se devuelven completos para el rango de fechas y no se ven afectados por offset/limit.
- La respuesta agrupa compradores en results y expone paging, fechas y leads; el texto de preguntas se consulta por separado con external_id. La guía advierte que campos personales pueden depender del tipo de acceso y que preguntas sin responder por más de siete meses se eliminan.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /v1/users/806525693/leads/buyers

La fuente menciona la ruta /v1/users/806525693/leads/buyers, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/v1/users/806525693/leads/buyers`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Tipos de contacto de leads

La guía distingue whatsapp, question, call, schedule y quotation. schedule depende de que la publicación ofrezca agenda; include_guest=true añade leads y conteos de personas no registradas.
## Operaciones de API

### Consultar interesados y leads de un vendedor

**Método:** `GET`  
**Ruta:** `/vis/users/$USER_ID/leads/buyers`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista compradores interesados; filtra por fecha, tipo de contacto, ítem o comprador y permite paginación. include_guest=true agrega leads guest y un resumen por ítem.

**Parámetros**

- `USER_ID` (path, obligatorio): Identificador del vendedor.
- `offset` (query, opcional): Posición inicial; por defecto 0.
- `limit` (query, opcional): Cantidad máxima; por defecto 10.
- `date_from` (query, opcional): Fecha inicial YYYY-MM-DD; por defecto siete días antes.
- `date_to` (query, opcional): Fecha final YYYY-MM-DD; por defecto fecha actual.
- `contact_types` (query, opcional): Tipos de contacto; si se omite retorna todos.
- `item_id` (query, opcional): Filtro por publicación.
- `buyer_ids` (query, opcional): Uno o varios IDs separados por coma.
- `include_guest` (query, opcional): Incluye leads guest y guest/summary; paginación no aplica a guest.

**Solicitud**

No documentado en la fuente.

**Respuesta**

results[] con comprador, item_id y leads[]; paging.offset/limit/total; date_from/date_to. include_guest añade guest[] y summary[].

**Errores documentados**

- 400: rango de fechas invertido o formato/USER_ID/parámetro/tipo de lead inválido.
- 403: token inválido, expirado, no corresponde al vendedor o falta autorización.
- 404: lead no encontrado.
- 409: quota exceeded.

**Ejemplos**

- Tipos: whatsapp, question, call, schedule y quotation. schedule puede devolver arreglo vacío si no está habilitado en el ítem.

### Obtener detalle de un lead

**Método:** `GET`  
**Ruta:** `/vis/leads/$LEAD_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera los datos del lead indicado por ID, recibido en una notificación o en results.leads.id.

**Parámetros**

- `LEAD_ID` (path, obligatorio): Identificador del lead.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, item_id, created_at, contact_type, external_id, status, buyer_id y datos de contacto cuando estén disponibles.

**Errores documentados**

- 403: token inválido, expirado o sin permisos.
- 404: lead no encontrado para el usuario.

**Ejemplos**

- El detalle del lead no contiene el texto de una pregunta.

### Consultar pregunta asociada a un lead

**Método:** `GET`  
**Ruta:** `/questions/$QUESTION_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el mensaje de pregunta usando external_id como QUESTION_ID y api_version=4.

**Parámetros**

- `QUESTION_ID` (path, obligatorio): Coincide con external_id del lead.
- `api_version` (query, obligatorio): Usar 4 para la nueva estructura JSON.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, seller_id, buyer_id, item_id, status, text, fechas y answer.text/status/date_created.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Con estado BANNED, el texto puede venir vacío; la fuente advierte que preguntas sin respuesta de más de siete meses se eliminan.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/leads-inmuebles](https://developers.mercadolibre.com.co/es_co/leads-inmuebles)  
**Captura:** 2026-10-08T22:50:42.774Z
