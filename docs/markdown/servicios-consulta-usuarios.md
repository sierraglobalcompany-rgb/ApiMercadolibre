---
id: "servicios-consulta-usuarios"
title: "Consulta Usuarios"
section: "Guía para servicios"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/servicios-consulta-usuarios"
source_updated_at: "29/04/2025"
captured_at: "2026-10-08T22:53:04.557Z"
sha256: "7daf1a0d502f06e2e8a62bb674060a63b7d2e50b5ca04173cd131f20dc9ee3f3"
---

# Consulta Usuarios

**Área:** Guía para servicios  
**Actualización indicada por la fuente:** 29/04/2025  
**Captura:** 2026-10-08T22:53:04.557Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/servicios-consulta-usuarios](https://developers.mercadolibre.com.co/es_co/servicios-consulta-usuarios)

## Resumen

Reúne consultas de perfil público y privado, actualización de dirección y consulta de bloqueos relacionados con preguntas o pedidos.

## Contenido y conceptos documentados

- /users/me consulta quien autorizó la aplicación; /users/{user_id} ofrece perfil público y /private puede incluir dirección completa y contacto si el usuario autorizó y el token tiene permiso.
- La actualización requiere permiso del usuario y recibe address con street, number, city y state.
- El endpoint de bloqueos unifica preguntas y órdenes: type acepta blocked_by_questions o blocked_by_order; client.id y user_blocked son opcionales, caller.id es obligatorio, offset inicia en 0 y limit en 10 (máximo 1000). La respuesta presenta users y paging.

## Operaciones de API
## Operaciones de API

### Buscar usuarios bloqueados

**Método:** `GET`  
**Ruta:** `/block-api/search/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta bloqueos asociados a un Buyer; endpoint unificado para preguntas y órdenes.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario.
- `client.id` (opcional): ID del cliente que realiza la solicitud.
- `type` (query, obligatorio): blocked_by_questions o blocked_by_order.
- `user_blocked` (opcional): ID del Buyer bloqueado.
- `caller.id` (obligatorio): ID del usuario que realiza la solicitud.
- `offset` (opcional): Por defecto 0.
- `limit` (opcional): Por defecto 10, máximo 1000.

**Solicitud**

No documentado en la fuente.

**Respuesta**

users con id y blocked_at; paging con offset, limit y total.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- type=blocked_by_questions y type=blocked_by_order; la fuente muestra 200 OK.

### Consultar usuario autenticado

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve información del usuario que autorizó la aplicación.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo contiene id, nickname, registration_date, country_id, address, user_type, tags, site_id, seller_reputation, buyer_reputation y status.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/me.

### Consultar información pública de usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta perfil y reputación pública por ID.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con id, nickname, registration_date, country_id, address de ciudad/estado, tags, reputaciones y status.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/202593498.

### Consultar información privada de usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/private`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN con permiso para estos datos

Consulta información privada de un usuario que autorizó la aplicación; requiere token con permiso.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo agrega street/number y datos de contacto al perfil.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/202593498/private.

### Actualizar dirección de usuario

**Método:** `PUT`  
**Ruta:** `/users/{user_id}/address`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza la dirección de un usuario que concedió permiso.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

JSON address con street, number, city y state.

**Respuesta**

Ejemplo devuelve perfil con dirección actualizada.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- PUT /users/202593498/address.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/servicios-consulta-usuarios](https://developers.mercadolibre.com.co/es_co/servicios-consulta-usuarios)  
**Captura:** 2026-10-08T22:53:04.557Z
