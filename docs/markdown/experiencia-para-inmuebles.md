---
id: "experiencia-para-inmuebles"
title: "Experiencia para inmuebles"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/experiencia-para-inmuebles"
source_updated_at: "23/09/2026"
captured_at: "2026-10-08T22:50:38.813Z"
sha256: "fd6d962bea467e0098fa5d723efee44f74ffa8ba3f32d9d4b2ffcd17466bf568"
---

# Experiencia para inmuebles

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 23/09/2026  
**Captura:** 2026-10-08T22:50:38.813Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/experiencia-para-inmuebles](https://developers.mercadolibre.com.co/es_co/experiencia-para-inmuebles)

## Resumen

Documenta configuración de proveedores, leads, agendas de visitas y cambios multifamily.

## Contenido y conceptos documentados

- La configuración contiene requisitos, nóminas, notificaciones y factor de renta; operation puede ser price_updated, unit_added o unit_removed.

## Operaciones de API

## Conceptos y recursos asociados

### Experiencia para inmuebles

Documenta configuración de proveedores, leads, agendas de visitas y cambios multifamily.
## Operaciones de API

### Crear configuración de provider

**Método:** `POST`  
**Ruta:** `/vis-transactions-hub/configurations/provider`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea parámetros de visitas.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "seller_id",
    "codebtor_required",
    "latest_dependent_worker_payrolls",
    "latest_independent_worker_payrolls",
    "email_notify_schedule",
    "salary_multiplier",
    "allow_guest_login"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Activar solicitudes de visita en ítems

**Método:** `POST`  
**Ruta:** `/vis-transactions-hub/{providerId}/entities/items/tags`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Marca o desmarca los ítems.

**Parámetros**

- `providerId` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "seller_id",
    "item_ids[]",
    "enable_rex"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "ítems marcados/desmarcados"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar lead

**Método:** `GET`  
**Ruta:** `/vis/leads/{lead_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

external_id identifica la agenda asociada.

**Parámetros**

- `lead_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "external_id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar configuración provider

**Método:** `GET`  
**Ruta:** `/vis-transactions-hub/configurations/provider/{provider_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta configuración por provider.

**Parámetros**

- `provider_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "provider_id",
    "codebtor_required",
    "latest_dependent_worker_payrolls",
    "latest_independent_worker_payrolls",
    "email_notify_schedule",
    "salary_multiplier",
    "allow_guest_login"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar detalle de agenda

**Método:** `GET`  
**Ruta:** `/vis-transactions-hub/{providerId}/entities/schedules/{schedule_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta agenda por ID.

**Parámetros**

- `providerId` (path, obligatorio): Identificador de la ruta
- `schedule_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "unit_name",
    "user_id",
    "email",
    "name",
    "last_name",
    "item_id",
    "phone1",
    "phone2",
    "scheduling_time",
    "scheduling_time_period"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar configuración seller

**Método:** `GET`  
**Ruta:** `/vis-transactions-hub/configurations/seller/{seller_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta configuración por seller.

**Parámetros**

- `seller_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "provider_id",
    "codebtor_required",
    "latest_dependent_worker_payrolls",
    "latest_independent_worker_payrolls",
    "email_notify_schedule",
    "salary_multiplier",
    "allow_guest_login"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Actualizar configuración

**Método:** `PATCH`  
**Ruta:** `/vis-transactions-hub/configurations/provider/{providerId}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza configuración del provider.

**Parámetros**

- `providerId` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "codebtor_required",
    "latest_dependent_worker_payrolls",
    "latest_independent_worker_payrolls",
    "email_notify_schedule",
    "salary_multiplier",
    "allow_guest_login",
    "notification_url"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Actualizar estado de agenda

**Método:** `PUT`  
**Ruta:** `/vis-transactions-hub/{providerId}/entities/schedules`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza estado de la agenda.

**Parámetros**

- `providerId` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "scheduling_id",
    "status_code",
    "status_name",
    "message",
    "timestamp",
    "data"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Actualizar unidades multifamily

**Método:** `PUT`  
**Ruta:** `/vis-transactions-hub/{providerId}/entities/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza precios y altas/bajas.

**Parámetros**

- `providerId` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "item_id",
    "status_code",
    "status_name",
    "message",
    "timestamp",
    "data.units[].unit_name",
    "data.units[].price",
    "data.units[].operation"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- operation: price_updated, unit_added, unit_removed

**Fuente:** [https://developers.mercadolibre.com.co/es_co/experiencia-para-inmuebles](https://developers.mercadolibre.com.co/es_co/experiencia-para-inmuebles)  
**Captura:** 2026-10-08T22:50:38.813Z
