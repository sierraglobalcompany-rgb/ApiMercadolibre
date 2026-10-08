---
id: "persona-interesadas"
title: "Personas Interesadas"
section: "Guía para vehículos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/persona-interesadas"
source_updated_at: "26/01/2026"
captured_at: "2026-10-08T22:53:19.280Z"
sha256: "0d8f12950ed52e35dbbaab71a7318c27cd24cd84c60c68194980a59a6bfb9993"
---

# Personas Interesadas

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 26/01/2026  
**Captura:** 2026-10-08T22:53:19.280Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/persona-interesadas](https://developers.mercadolibre.com.co/es_co/persona-interesadas)

## Resumen

Explica la consulta de compradores interesados y leads generados en publicaciones de vehículos e inmuebles. Permite filtrar por período, tipo de contacto, ítem y comprador, y consultar por separado el detalle de un lead.

## Contenido y conceptos documentados

- La consulta de vendedores requiere `USER_ID`; filtros incluyen `offset` (0), `limit` (10), `date_from`, `date_to` (fecha actual por defecto), `contact_types`, `item_id` y `buyer_ids`. Tipos de lead: `whatsapp`, `question`, `call`, `credit`, `contact_request`, `visit request` y `reservation`.
- La respuesta contiene `results`, datos del comprador y `leads` con `id`/`uuid`, canal, tipo, fechas, referencia externa, ítem y estado; también `paging`, `date_from` y `date_to`. `include_guest=true` añade `guest` y `summary` para usuarios no logueados.
- Errores documentados: 400 por rango de fechas invertido o formatos inválidos, USER_ID inválido y parámetros inválidos. Disponible para vehículos e inmuebles en todos los sitios.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /v1/users/806525693/leads/buyers

La fuente menciona la ruta /v1/users/806525693/leads/buyers, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/v1/users/806525693/leads/buyers`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### GET /leads/{LEAD_ID}/details

**Método:** `GET`  
**Ruta:** `/leads/{LEAD_ID}/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalles adicionales del lead.

**Parámetros**

- `LEAD_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "summary": "Devuelve detalles adicionales del lead."
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "bad_request por rango de fechas invertido o inválido, USER_ID inválido o parámetro inválido." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /vis/leads/{LEAD_ID}

**Método:** `GET`  
**Ruta:** `/vis/leads/{LEAD_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta datos básicos del lead.

**Parámetros**

- `LEAD_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "summary": "Devuelve la información básica del lead."
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "bad_request por rango de fechas invertido o inválido, USER_ID inválido o parámetro inválido." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /vis/users/{USER_ID}/leads/buyers

**Método:** `GET`  
**Ruta:** `/vis/users/{USER_ID}/leads/buyers`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta interesados/leads del vendedor con filtros por fechas, contacto, ítem y comprador.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `offset` (query, opcional): Predeterminado 0.
- `limit` (query, opcional): Predeterminado 10.
- `date_from` (query, opcional): Fecha de inicio YYYY-MM-DD.
- `date_to` (query, opcional): Fecha de término; predeterminado fecha actual.
- `contact_types` (query, opcional): Tipos de contacto.
- `item_id` (query, opcional): Filtra por ítem.
- `buyer_ids` (query, opcional): Uno o varios compradores.
- `include_guest` (query, opcional): true agrega guest y summary.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "results",
    "paging",
    "date_from",
    "date_to",
    "guest",
    "summary",
    "leads.id",
    "leads.uuid",
    "leads.channel",
    "leads.contact_type",
    "leads.created_at",
    "leads.external_id",
    "leads.item_id",
    "leads.status"
  ]
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "bad_request por rango de fechas invertido o inválido, USER_ID inválido o parámetro inválido." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/persona-interesadas](https://developers.mercadolibre.com.co/es_co/persona-interesadas)  
**Captura:** 2026-10-08T22:53:19.280Z
