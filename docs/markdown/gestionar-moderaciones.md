---
id: "gestionar-moderaciones"
title: "Gestionar moderaciones"
section: "Recursos de la API"
subsection: "Moderaciones"
url: "https://developers.mercadolibre.com.co/es_co/gestionar-moderaciones"
source_updated_at: "08/06/2026"
captured_at: "2026-10-08T22:53:48.734Z"
sha256: "12c1160929b3df9ea6348e033cf2cda4d525e18b832be9a5144d966af586e65b"
---

# Gestionar moderaciones

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 08/06/2026  
**Captura:** 2026-10-08T22:53:48.734Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestionar-moderaciones](https://developers.mercadolibre.com.co/es_co/gestionar-moderaciones)

## Resumen

La guía explica cómo consultar moderaciones activas y el historial de infracciones, interpretar sus motivos y soluciones y filtrar publicaciones afectadas. Recomienda mostrar al vendedor el `reason` y el `remedy` que la API devuelve para cada caso.

## Contenido y conceptos documentados

El `moderation_reference_id` se construye con el ID del elemento y el sufijo del tipo: `-ITM` para publicación, `-QUE` para pregunta/respuesta y `-REV` para opinión. La respuesta de última moderación incluye nombre, ID temporal, fecha, evidencias y textos `REASON`/`REMEDY`; una baja por `DENYLIST` puede tener solo motivo. Para moderaciones activas se buscan ítems `pending`, incluidos subestados como `warning`, `waiting_for_patch`, `held`, `pending_documentation`, `forbidden` y `picture_downloading_pending`. El histórico permite filtrar por elemento, tipo, fechas, idioma, límite, offset y orden; el límite indicado es de 1 a 20.

## Operaciones de API

## Conceptos y recursos asociados

### Estados, referencias y recomendaciones de moderación

Describe estados de moderación y cómo relacionar una notificación con la consulta de la última moderación.

**Respuesta**

No documentado en la fuente.

**Ejemplos documentados**

- Sufijos: ITM publicación; QUE preguntas/respuestas; REV opiniones de producto.
### Ruta mencionada /items

La fuente menciona la ruta /items, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/items`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Buscar ítems en moderación

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista ítems del usuario con status pending, incluyendo estados de moderación en revisión.

**Parámetros**

- `user_id` (path, obligatorio): Identificador del usuario.
- `status` (query, obligatorio): El ejemplo y la instrucción usan pending.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Respuesta con seller_id, paging, results y orders.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Subestados citados: warning, waiting_for_patch, held, pending_documentation, forbidden y picture_downloading_pending.

### Consultar histórico de infracciones

**Método:** `GET`  
**Ruta:** `/moderations/infractions/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta infracciones históricas del usuario para ítems, preguntas/respuestas y opiniones.

**Parámetros**

- `user_id` (path, obligatorio): Identificador del usuario.
- `related_item_id` (query): Filtra por publicación relacionada.
- `element_id` (query): Filtra por elemento moderado.
- `element_type` (query): ITM, REV o QUE.
- `date_created_since` (query): Fecha inicial YYYY-MM-DD.
- `date_created_to` (query): Fecha final YYYY-MM-DD.
- `language` (query): ES o PT; por defecto el idioma indicado por la fuente es inglés.
- `limit` (query): Entre 1 y 20; por defecto 20.
- `offset` (query): Desplazamiento para paginación.
- `sort` (query): Orden por fecha; ejemplo date_created_asc o date_created_desc.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto con infractions y paging; cada infracción puede incluir id, date_created, user_id, related_item_id, element_id/type, site_id, filter_subgroup, reason y remedy.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El ejemplo filtra date_created_since y limit.

### Consultar última moderación

**Método:** `GET`  
**Ruta:** `/moderations/last_moderation/{moderation_reference_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve la moderación activa más reciente de un elemento, con evidencias y motivos o soluciones.

**Parámetros**

- `moderation_reference_id` (path, obligatorio): ID del elemento seguido por sufijo -ITM, -QUE o -REV.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista con name, id, date_created, evidences y wordings (REASON/REMEDY); DENYLIST puede incluir solo REASON.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo: MLA1234567890-ITM.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestionar-moderaciones](https://developers.mercadolibre.com.co/es_co/gestionar-moderaciones)  
**Captura:** 2026-10-08T22:53:48.734Z
