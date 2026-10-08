---
id: "autenticacion-y-autorizacion"
title: "Autenticación y Autorización"
section: "Primeros pasos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/autenticacion-y-autorizacion"
source_updated_at: "15/07/2026"
captured_at: "2026-10-08T22:49:37.732Z"
sha256: "7011f993b43802c38de47ec31240feb1a6207d9e26334fb0eb210a01e1edde47"
---

# Autenticación y Autorización

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 15/07/2026  
**Captura:** 2026-10-08T22:49:37.732Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/autenticacion-y-autorizacion](https://developers.mercadolibre.com.co/es_co/autenticacion-y-autorizacion)

## Resumen

Explica OAuth 2.0 para autorizar aplicaciones y obtener o renovar access tokens. El token debe enviarse en el header Authorization; el flujo incluye redirección del usuario, code y canje del código en el servidor.

## Contenido y conceptos documentados

- El flujo authorization code usa `client_id`, `redirect_uri`, `state` y, cuando corresponda, PKCE (`code_challenge`, `code_challenge_method`, `code_verifier`). El `redirect_uri` debe coincidir con el configurado y no contener datos variables.
- El canje usa `grant_type=authorization_code`, `client_id`, `client_secret`, `code`, `redirect_uri` y opcionalmente `code_verifier`; la renovación usa `grant_type=refresh_token`, `client_id`, `client_secret` y `refresh_token`. La respuesta ejemplificada incluye `access_token`, `token_type`, `expires_in`, `scope`, `user_id` y nuevo `refresh_token`.
- Errores enumerados: `invalid_client`, `invalid_grant` e `invalid_scope`. Envía `Authorization: Bearer $ACCESS_TOKEN` al llamar a las APIs.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /users/me

La fuente menciona la ruta /users/me, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/users/me`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### POST /oauth/token

**Método:** `POST`  
**Ruta:** `/oauth/token`  
**Autenticación:** No documentado en la fuente.

Intercambia un authorization code o renueva tokens mediante un cuerpo form-urlencoded.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "content_type": "application/x-www-form-urlencoded",
  "fields": [
    "grant_type",
    "client_id",
    "client_secret",
    "code",
    "redirect_uri",
    "code_verifier",
    "refresh_token"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "access_token",
    "token_type",
    "expires_in",
    "scope",
    "user_id",
    "refresh_token"
  ]
}
```

**Errores documentados**

- ```json {   "code": "invalid_client",   "meaning": "client_id o client_secret inválidos." } ```
- ```json {   "code": "invalid_grant",   "meaning": "Código o refresh token inválido, expirado/revocado o inconsistente con cliente/redirect." } ```
- ```json {   "code": "invalid_scope",   "meaning": "Scope solicitado inválido o mal formado." } ```

**Ejemplos**

- La fuente muestra canje de authorization_code y renovación refresh_token en el mismo endpoint.

### Referencia HTTP GET /users/me

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/me. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/autenticacion-y-autorizacion](https://developers.mercadolibre.com.co/es_co/autenticacion-y-autorizacion)  
**Captura:** 2026-10-08T22:49:37.732Z
