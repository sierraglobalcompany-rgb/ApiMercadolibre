---
id: "consulta-de-usuarios"
title: "Consulta de usuarios"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/consulta-de-usuarios"
source_updated_at: "06/11/2025"
captured_at: "2026-10-08T22:50:34.327Z"
sha256: "0e94603f3e69e9ea4ea5c06c6f4af479d511b294f4004a9deb61cb01566d287d"
---

# Consulta de usuarios

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 06/11/2025  
**Captura:** 2026-10-08T22:50:34.327Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/consulta-de-usuarios](https://developers.mercadolibre.com.co/es_co/consulta-de-usuarios)

## Resumen

Documenta consulta de perfil propio y público, pago inmediato y búsqueda de usuarios bloqueados.

## Contenido y conceptos documentados

- /users/me consulta perfil asociado al token; /users/{user_id} consulta un perfil público.

## Operaciones de API

## Conceptos y recursos asociados

### Consulta de usuarios

Documenta consulta de perfil propio y público, pago inmediato y búsqueda de usuarios bloqueados.
## Operaciones de API

### Consultar bloqueos por orden

**Método:** `GET`  
**Ruta:** `/block-api/search/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca bloqueos para órdenes.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario
- `type` (query, obligatorio): blocked_by_order

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "users[].id",
    "users[].blocked_at",
    "paging.offset",
    "paging.limit",
    "paging.total"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Activar pago inmediato

**Método:** `PUT`  
**Ruta:** `/users/{user_id}/immediate_payment`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Configura reason=by_user.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "reason"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- {"reason":"by_user"}

### Deshacer pago inmediato

**Método:** `DELETE`  
**Ruta:** `/users/{user_id}/immediate_payment/by_user`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina preferencia by_user.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar usuario público

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta perfil por ID.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "nickname",
    "country_id",
    "identification",
    "address",
    "phone",
    "user_type",
    "tags",
    "site_id",
    "seller_reputation",
    "buyer_reputation",
    "status"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar perfil propio

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Perfil del usuario asociado al token.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "nickname",
    "registration_date",
    "first_name",
    "last_name",
    "country_id",
    "email",
    "identification",
    "address",
    "phone",
    "user_type",
    "tags",
    "site_id",
    "seller_reputation",
    "buyer_reputation",
    "status"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/consulta-de-usuarios](https://developers.mercadolibre.com.co/es_co/consulta-de-usuarios)  
**Captura:** 2026-10-08T22:50:34.327Z
