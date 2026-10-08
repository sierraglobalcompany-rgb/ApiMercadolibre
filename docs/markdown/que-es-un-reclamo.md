---
id: "que-es-un-reclamo"
title: "Gestionar reclamos"
section: "Guía para productos"
subsection: "Reclamos"
url: "https://developers.mercadolibre.com.co/es_co/que-es-un-reclamo"
source_updated_at: "20/08/2026"
captured_at: "2026-10-08T22:52:00.017Z"
sha256: "fffa9485ca6a34f0df2ab8bfff088defa4a443ccaa5c8d969a17866aa4cd2bf2"
---

# Gestionar reclamos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 20/08/2026  
**Captura:** 2026-10-08T22:52:00.017Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/que-es-un-reclamo](https://developers.mercadolibre.com.co/es_co/que-es-un-reclamo)

## Resumen

Presenta el modelo de reclamos posventa y las consultas para recuperar un reclamo, personalizar su búsqueda, consultar motivos, revisar historial de acciones y estados, y saber si afecta la reputación. La guía relaciona estos recursos con notificaciones de reclamos y acciones.

## Contenido y conceptos documentados

### Modelo, búsqueda y campos

- Las operaciones documentan `Bearer`. Un reclamo reúne `id`, `resource_id`, `status`, `type`, `stage`, versión/cantidad, recurso, motivo, participantes y acciones disponibles, resolución, fechas, cobertura, sitio y entidades relacionadas. Los estados incluyen `opened`/`closed`; tipos visibles incluyen mediación, devolución, fulfillment, caso ML, cancelación, cambio y servicio.
- La búsqueda requiere al menos un filtro real: offset/limit/sort solos producen HTTP 400. `resource_id` depende de `resource`; `players.user_id` depende de `players.role`; `order_id` y `pack_id` son mutuamente excluyentes. `offset` por defecto 0 y máximo 9999; `limit` por defecto 30 y máximo 100; `offset + limit` debe ser menor que 10000. Las fechas se expresan con milisegundos. Se recomienda acotar por rol y usuario; buscar solo por estado puede ser costoso y sujeto a límites.
- Los filtros documentados incluyen `id`, `type`, `stage`, `status`, recurso e ID, `reason_id`, `site_id`, jugador/rol, orden o paquete, pago, reclamo padre y rangos de fechas de creación/actualización.
- `detail` añade `due_date`, responsable, título, descripción y problema. Motivos, historial de acciones/estados y `affects-reputation` tienen sus propios campos; la respuesta de reputación puede indicar `affected`, `not_affected` o `not_applies`, además de incentivo y vencimiento. Errores de las llamadas individuales: No documentado en la fuente salvo la búsqueda inválida HTTP 400.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /claims/{CLAIM_ID}/detail

La fuente menciona la ruta /claims/{CLAIM_ID}/detail, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/{CLAIM_ID}/detail`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /v1/claims/search

La fuente menciona la ruta /v1/claims/search, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/v1/claims/search`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /claims/reasons/{REASON_ID}

La fuente menciona la ruta /claims/reasons/{REASON_ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/reasons/{REASON_ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /claims/{CLAIM_ID}

La fuente menciona la ruta /claims/{CLAIM_ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/{CLAIM_ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /claims/affects-reputation

La fuente menciona la ruta /claims/affects-reputation, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/affects-reputation`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /claims/detail

La fuente menciona la ruta /claims/detail, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/detail`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /claims/actions-history

La fuente menciona la ruta /claims/actions-history, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/actions-history`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar reclamo

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene información principal, participantes, acciones disponibles y resolución del reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- resource_id
- status
- type
- stage
- claim_version
- claimed_quantity
- parent_id
- resource
- reason_id
- fulfilled
- quantity_type
- players
- available_actions
- resolution
- reason
- date_created
- last_updated
- benefited
- closed_by
- applied_coverage
- site_id
- related_entities

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Estados: opened y closed; tipos documentados incluyen mediations, return, fulfillment, ml_case, cancel_sale, cancel_purchase, change y service.

### Historial de acciones

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/actions-history`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta las acciones registradas y sus participantes.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- action_name
- player_role
- action_reason_id
- claim_stage
- claim_status
- date_created

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar impacto en reputación

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/affects-reputation`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Determina si el reclamo afecta la reputación del vendedor.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- affects_reputation (affected, not_affected o not_applies)
- has_incentive
- due_date

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Detalle de reclamo

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/detail`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta datos de vencimiento, responsable y descripción del problema.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- due_date
- action_responsible
- title
- description
- problem

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Historial de estados

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/status-history`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta las transiciones de estado y etapa del reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- stage
- status
- date
- change_by

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar motivo de reclamo

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/reasons/$REASON_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene definición, configuración y flujos permitidos de un motivo.

**Parámetros**

- `REASON_ID` (path, obligatorio)
- `flow` (query, opcional)
- `delivered` (query, opcional)
- `deep` (query, opcional)
- `name` (query, opcional)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- flow
- name
- detail
- position
- group
- site_id
- settings
- allowed_flows
- expected_resolutions
- rules_engine_triage
- parent
- children_title
- status
- date_created

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra ejemplo de reason_id PDD9939.

### Buscar reclamos

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca reclamos mediante filtros dependientes y paginación acotada.

**Parámetros**

- `id` (query, opcional)
- `type` (query, opcional)
- `stage` (query, opcional)
- `status` (query, opcional)
- `resource` (query, opcional)
- `resource_id` (query, opcional): Requiere resource.
- `reason_id` (query, opcional)
- `site_id` (query, opcional)
- `players.role` (query, opcional)
- `players.user_id` (query, opcional): Requiere players.role.
- `order_id` (query, opcional): Mutuamente excluyente con pack_id.
- `pack_id` (query, opcional): Mutuamente excluyente con order_id.
- `payment_id` (query, opcional)
- `parent_id` (query, opcional)
- `date_created` (query, opcional)
- `last_updated` (query, opcional)
- `offset` (query, opcional): Por defecto 0; máximo 9999.
- `limit` (query, opcional): Por defecto 30; máximo 100; offset+limit menor que 10000.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- paging.total
- paging.offset
- paging.limit
- data[]

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Sin filtro real; dependencias inválidas; paginación sin filtro o parámetros incompatibles." } ```

**Ejemplos**

- Los filtros de fecha usan timestamps con milisegundos. La fuente recomienda filtrar por rol y usuario; desaconseja consulta amplia solo por status.

### Referencia HTTP GET /claims/affects-reputation

**Método:** `GET`  
**Ruta:** `/claims/affects-reputation`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /claims/affects-reputation. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /claims/{CLAIM_ID}

**Método:** `GET`  
**Ruta:** `/claims/{CLAIM_ID}`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /claims/{CLAIM_ID}. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /claims/reasons/{REASON_ID}

**Método:** `GET`  
**Ruta:** `/claims/reasons/{REASON_ID}`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /claims/reasons/{REASON_ID}. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /claims/detail

**Método:** `GET`  
**Ruta:** `/claims/detail`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /claims/detail. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /v1/claims/search

**Método:** `GET`  
**Ruta:** `/v1/claims/search`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /v1/claims/search. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /claims/actions-history

**Método:** `GET`  
**Ruta:** `/claims/actions-history`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /claims/actions-history. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/que-es-un-reclamo](https://developers.mercadolibre.com.co/es_co/que-es-un-reclamo)  
**Captura:** 2026-10-08T22:52:00.017Z
