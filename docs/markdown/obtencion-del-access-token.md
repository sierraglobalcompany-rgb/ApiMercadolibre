---
id: "obtencion-del-access-token"
title: "Obtención del Access Token"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/obtencion-del-access-token"
source_updated_at: "05/11/2025"
captured_at: "2026-10-08T22:50:45.394Z"
sha256: "d478066d7b6f5818d23aa7e8796796785b8cfe20d53019aa55bf2f244a80af3e"
---

# Obtención del Access Token

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 05/11/2025  
**Captura:** 2026-10-08T22:50:45.394Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/obtencion-del-access-token](https://developers.mercadolibre.com.co/es_co/obtencion-del-access-token)

## Resumen

El flujo explicado obtiene un Access Token mediante OAuth authorization code. Requiere una aplicación creada y sus Client ID, Client Secret y Redirect URI; el usuario inicia sesión, autoriza y recibe un code en la URL de retorno.

## Contenido y conceptos documentados

- El code se intercambia en POST /oauth/token usando grant_type=authorization_code y el cuerpo application/x-www-form-urlencoded.
- La respuesta de éxito documenta access_token, token_type, expires_in, scope, user_id y refresh_token; el token tiene duración limitada.
- La página remite a la guía de autenticación para errores y no detalla aquí la operación de refresh.

## Operaciones de API
## Operaciones de API

### Obtener Access Token con authorization code

**Método:** `POST`  
**Ruta:** `/oauth/token`  
**Autenticación:** No documentado en la fuente.

Intercambia el código recibido tras el consentimiento por un Access Token OAuth temporal; requiere credenciales de aplicación y Redirect URI registrados.

**Parámetros**

- `grant_type` (body, obligatorio): La guía usa authorization_code.
- `client_id` (body, obligatorio): ID de la aplicación.
- `client_secret` (body, obligatorio): Clave secreta.
- `code` (body, obligatorio): Código devuelto en la redirección.
- `redirect_uri` (body, obligatorio): URI registrada.

**Solicitud**

application/x-www-form-urlencoded

**Respuesta**

access_token, token_type, expires_in, scope, user_id y refresh_token.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El flujo comienza en la URL de autorización del sitio correspondiente; esta página no detalla la operación refresh.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/obtencion-del-access-token](https://developers.mercadolibre.com.co/es_co/obtencion-del-access-token)  
**Captura:** 2026-10-08T22:50:45.394Z
