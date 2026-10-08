---
id: "consulta-usuarios"
title: "Consulta Usuarios"
section: "Guía para vehículos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/consulta-usuarios"
source_updated_at: "12/01/2026"
captured_at: "2026-10-08T22:53:13.564Z"
sha256: "3a5af6a69242f35065560ddb7d774a0e5de42ff894e9e769d94a06807c697eaf"
---

# Consulta Usuarios

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 12/01/2026  
**Captura:** 2026-10-08T22:53:13.564Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/consulta-usuarios](https://developers.mercadolibre.com.co/es_co/consulta-usuarios)

## Resumen

La página explica cómo consultar datos propios, públicos y privados de usuarios, consultar bloqueos de compradores y gestionar preferencias de pago inmediato y listas de bloqueo. Los recursos de usuario pueden devolver HTTP 206 cuando algunos datos no estén disponibles; en ese caso la respuesta queda incompleta.

## Contenido y conceptos documentados

- `GET /users/me` consulta el perfil propio. `GET /users/{USER_ID}` sirve para información pública y, con autorización del usuario, privada; los ejemplos incluyen identidad, dirección, reputación y estado.
- El endpoint unificado de bloqueos admite `type=blocked_by_questions` o `blocked_by_order`. `caller.id` y `type` son obligatorios; `client.id` y `user_blocked` opcionales; `offset` predeterminado 0 y `limit` predeterminado 10, máximo 1000. Respuesta: `users.id`, `users.blocked_at` y `paging`.
- Para aceptar solo Mercado Pago se envía `reason=by_user`; la eliminación revierte la marca. También se documenta borrar un bloqueo de órdenes y agregar un usuario a la lista negra de preguntas. Autenticación mostrada: `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### DELETE /users/{USER_ID}/immediate_payment/by_user

**Método:** `DELETE`  
**Ruta:** `/users/{USER_ID}/immediate_payment/by_user`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la marca de pago inmediato `by_user`.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### DELETE /users/{YOUR_CUST_ID}/order_blacklist/{SELLER_ID}

**Método:** `DELETE`  
**Ruta:** `/users/{YOUR_CUST_ID}/order_blacklist/{SELLER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina un usuario bloqueado para órdenes.

**Parámetros**

- `YOUR_CUST_ID` (path, obligatorio)
- `SELLER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /block-api/search/users/{USER_ID}

**Método:** `GET`  
**Ruta:** `/block-api/search/users/{USER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta bloqueos de un comprador por preguntas u órdenes.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `type` (query, obligatorio): blocked_by_questions o blocked_by_order
- `caller.id` (query, obligatorio): Usuario que consulta
- `client.id` (query, opcional): ID cliente
- `user_blocked` (query, opcional): ID comprador bloqueado
- `offset` (query, opcional): Predeterminado 0
- `limit` (query, opcional): Predeterminado 10, máximo 1000

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "users.id",
    "users.blocked_at",
    "paging.offset",
    "paging.limit",
    "paging.total"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/me

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta los datos del usuario autenticado.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta datos públicos o, con autorización, privados del usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### POST /users/{SELLER_ID}/questions_blacklist

**Método:** `POST`  
**Ruta:** `/users/{SELLER_ID}/questions_blacklist`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega un usuario a la lista de bloqueo de preguntas.

**Parámetros**

- `SELLER_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "user_id"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### PUT /users/{USER_ID}/immediate_payment

**Método:** `PUT`  
**Ruta:** `/users/{USER_ID}/immediate_payment`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Configura el pago inmediato; ejemplo con `reason=by_user`.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "reason"
  ],
  "example": "by_user"
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/consulta-usuarios](https://developers.mercadolibre.com.co/es_co/consulta-usuarios)  
**Captura:** 2026-10-08T22:53:13.564Z
