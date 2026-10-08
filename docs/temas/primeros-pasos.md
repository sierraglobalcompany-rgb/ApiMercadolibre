# Primeros pasos

12 páginas del portal oficial en esta área.

## [Autenticación y Autorización](../markdown/autenticacion-y-autorizacion.md)

Actualización indicada por la fuente: 15/07/2026. Captura: 2026-10-08T22:49:37.732Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/autenticacion-y-autorizacion](https://developers.mercadolibre.com.co/es_co/autenticacion-y-autorizacion)

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

---

## [Buenas prácticas para uso de la plataforma](../markdown/buenas-practicas-para-uso-de-la-plataforma.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:53:25.827Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-uso-de-la-plataforma](https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-uso-de-la-plataforma)

# Buenas prácticas para uso de la plataforma

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:25.827Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-uso-de-la-plataforma](https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-uso-de-la-plataforma)

## Resumen

Reúne recomendaciones para integrar con la plataforma evitando moderaciones, suspensiones y problemas operativos: usar los recursos documentados, respetar restricciones de producto y gestionar límites.

## Contenido y conceptos documentados

- La fuente recomienda no hacer web crawling y trabajar mediante la API; limitar IPs del entorno y manejar HTTP 429 reduciendo o ajustando solicitudes.
- Usa motivos de comunicación solo en escenarios permitidos; no modifiques templates de etiquetas ni clones publicaciones/imágenes. Publica productos elegibles para catálogo en catálogo y asocia guía de talles a productos de moda.
- No se documentan operaciones HTTP ni parámetros en esta página: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Buenas prácticas para uso de la plataforma

Reúne recomendaciones para integrar con la plataforma evitando moderaciones, suspensiones y problemas operativos: usar los recursos documentados, respetar restricciones de producto y gestionar límites.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-uso-de-la-plataforma](https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-uso-de-la-plataforma)  
**Captura:** 2026-10-08T22:53:25.827Z

---

## [Consideraciones de diseño](../markdown/consideraciones-de-diseno.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:53:29.373Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/consideraciones-de-diseno](https://developers.mercadolibre.com.co/es_co/consideraciones-de-diseno)

# Consideraciones de diseño

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:29.373Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/consideraciones-de-diseno](https://developers.mercadolibre.com.co/es_co/consideraciones-de-diseno)

## Resumen

Describe convenciones comunes de las APIs de Mercado Libre: JSON, JSONP, selección de atributos, documentación con OPTIONS, manejo de errores y paginación.

## Contenido y conceptos documentados

- Las respuestas estándar de error contienen `message`, `error`, `status` y `cause`. Con `attributes` se limitan los campos devueltos. JSONP usa `callback` y presenta status, headers y body junto con la respuesta.
- La paginación usa `offset` y `limit`, con valores predeterminados 0 y 50. La página muestra `OPTIONS` para obtener metadatos del recurso.

## Operaciones de API
## Operaciones de API

### GET /currencies

**Método:** `GET`  
**Ruta:** `/currencies`  
**Autenticación:** No documentado en la fuente.

Lista monedas; el ejemplo admite `attributes=id` y `callback` para JSONP.

**Parámetros**

- `attributes` (query, opcional): Campos de respuesta a conservar.
- `callback` (query, opcional): Nombre de función para JSONP.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura incluye un ejemplo de llamada.

### GET /currencies/{CURRENCY_ID}

**Método:** `GET`  
**Ruta:** `/currencies/{CURRENCY_ID}`  
**Autenticación:** No documentado en la fuente.

Consulta datos de una moneda, por ejemplo `/currencies/ARS`.

**Parámetros**

- `CURRENCY_ID` (path, obligatorio)
- `attributes` (query, opcional): Campos de respuesta a conservar.
- `callback` (query, opcional): Nombre de función para JSONP.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura incluye un ejemplo de llamada.

### OPTIONS /currencies

**Método:** `OPTIONS`  
**Ruta:** `/currencies`  
**Autenticación:** No documentado en la fuente.

Obtiene documentación en JSON sobre el recurso de monedas.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "name",
    "description",
    "attributes"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura incluye un ejemplo de llamada.

### Referencia HTTP GET /currencies/ARS

**Método:** `GET`  
**Ruta:** `/currencies/ARS`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /currencies/ARS. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/consideraciones-de-diseno](https://developers.mercadolibre.com.co/es_co/consideraciones-de-diseno)  
**Captura:** 2026-10-08T22:53:29.373Z

---

## [Crea una aplicación en Mercado Libre](../markdown/crea-una-aplicacion-en-mercado-libre-es.md)

Actualización indicada por la fuente: 06/08/2026. Captura: 2026-10-08T22:53:30.364Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/crea-una-aplicacion-en-mercado-libre-es](https://developers.mercadolibre.com.co/es_co/crea-una-aplicacion-en-mercado-libre-es)

# Crea una aplicación en Mercado Libre

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 06/08/2026  
**Captura:** 2026-10-08T22:53:30.364Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/crea-una-aplicacion-en-mercado-libre-es](https://developers.mercadolibre.com.co/es_co/crea-una-aplicacion-en-mercado-libre-es)

## Resumen

Guía la creación y administración de una aplicación en DevCenter: datos básicos, scopes, notificaciones, autenticación/seguridad, permisos otorgados por usuarios y renovación del Client Secret.

## Contenido y conceptos documentados

- Los scopes de lectura habilitan métodos GET; los de escritura habilitan PUT, POST y DELETE. La aplicación define URL de callback y selecciona tópicos, por ejemplo Orders, Messages, Items, Catalog, Shipments y Promotions.
- El panel agrupa configuración, información básica, autenticación/seguridad y notificaciones. Client ID corresponde al APP ID; el Client Secret puede renovarse ahora o programarse.
- La página explica estados de autorizaciones (nueva, inactiva o activa) y recomienda pedir los permisos necesarios. No documenta operaciones HTTP concretas: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Crea una aplicación en Mercado Libre

Guía la creación y administración de una aplicación en DevCenter: datos básicos, scopes, notificaciones, autenticación/seguridad, permisos otorgados por usuarios y renovación del Client Secret.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/crea-una-aplicacion-en-mercado-libre-es](https://developers.mercadolibre.com.co/es_co/crea-una-aplicacion-en-mercado-libre-es)  
**Captura:** 2026-10-08T22:53:30.364Z

---

## [Desarrollo in-house Quick Start](../markdown/primeros-pasos-in-house.md)

Actualización indicada por la fuente: 06/10/2026. Captura: 2026-10-08T22:53:31.284Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/primeros-pasos-in-house](https://developers.mercadolibre.com.co/es_co/primeros-pasos-in-house)

# Desarrollo in-house Quick Start

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 06/10/2026  
**Captura:** 2026-10-08T22:53:31.284Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/primeros-pasos-in-house](https://developers.mercadolibre.com.co/es_co/primeros-pasos-in-house)

## Resumen

Propone una secuencia de implementación in-house: crear la app en la cuenta oficial del vendedor, configurar OAuth y scopes mínimos, procesar notificaciones y construir el flujo de ventas, despacho, fiscalidad y posventa.

## Contenido y conceptos documentados

- El access token tiene vigencia de 6 horas; la fuente recomienda almacenar tokens de forma segura y reemplazar el refresh token tras cada uso. Implementa `state` y PKCE cuando estén habilitados, y usa usuarios de prueba por sitio antes de producción.
- Se recomienda configurar webhooks, responder HTTP 200 en 500 ms y recuperar fallos recientes con `missed_feeds`; mantener TLS 1.2 o superior. Separa aplicaciones de Mercado Libre y Mercado Pago y crea la app en la cuenta oficial del vendedor.
- Para facturación, extraer `buyer.billing_info.id`; la página indica que el flujo anterior `/orders/billing-info` está deprecado. Para logística menciona `processing_time_tool`, `carrier_pickup` y `NODE_ID` en escenarios multiorigen.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /communications/notices

La fuente menciona la ruta /communications/notices, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/communications/notices`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /post-purchase/v1/claims/{CLAIM_ID}

La fuente menciona la ruta /post-purchase/v1/claims/{CLAIM_ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/post-purchase/v1/claims/{CLAIM_ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /post-purchase/v1/claims/{CLAIM_ID}/changes

La fuente menciona la ruta /post-purchase/v1/claims/{CLAIM_ID}/changes, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/post-purchase/v1/claims/{CLAIM_ID}/changes`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /post-purchase/v2/claims/{CLAIM_ID}/returns

La fuente menciona la ruta /post-purchase/v2/claims/{CLAIM_ID}/returns, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/post-purchase/v2/claims/{CLAIM_ID}/returns`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### GET /applications/{APP_ID}

**Método:** `GET`  
**Ruta:** `/applications/{APP_ID}`  
**Autenticación:** No documentado en la fuente.

Verifica la configuración y los scopes de una aplicación.

**Parámetros**

- `APP_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página menciona este recurso explícitamente.

### GET /orders/billing-info/{site_id}/{billing_info_id}

**Método:** `GET`  
**Ruta:** `/orders/billing-info/{site_id}/{billing_info_id}`  
**Autenticación:** No documentado en la fuente.

Consulta datos fiscales del comprador; la página indica que el flujo está deprecado.

**Parámetros**

- `site_id` (path, obligatorio)
- `billing_info_id` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página menciona este recurso explícitamente.

### GET /users/{USER_ID}/shipping/schedule/{LOGISTIC_TYPE}

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/shipping/schedule/{LOGISTIC_TYPE}`  
**Autenticación:** No documentado en la fuente.

Consulta la agenda de Coletas del usuario según tipo logístico.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `LOGISTIC_TYPE` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página menciona este recurso explícitamente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/primeros-pasos-in-house](https://developers.mercadolibre.com.co/es_co/primeros-pasos-in-house)  
**Captura:** 2026-10-08T22:53:31.284Z

---

## [Error 403](../markdown/error-403.md)

Actualización indicada por la fuente: 10/09/2026. Captura: 2026-10-08T22:53:32.355Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/error-403](https://developers.mercadolibre.com.co/es_co/error-403)

# Error 403

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 10/09/2026  
**Captura:** 2026-10-08T22:53:32.355Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/error-403](https://developers.mercadolibre.com.co/es_co/error-403)

## Resumen

Explica causas frecuentes de HTTP 403 y pasos para validar si la app, el usuario, los permisos, el scope o la IP impiden acceder al recurso.

## Contenido y conceptos documentados

- La fuente muestra respuestas con `status: 403`, `error` (`Invalid scopes` o `access_denied`), `message` y `code: FORBIDDEN`.
- Validaciones sugeridas: confirmar que la aplicación no esté bloqueada/deshabilitada, que el usuario esté activo, que tenga permisos, que la IP esté permitida y que la aplicación cuente con los scopes funcionales necesarios. La página enlaza a guías de datos de usuario, permisos e IPs.
- No documenta una operación HTTP concreta: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Error 403

Explica causas frecuentes de HTTP 403 y pasos para validar si la app, el usuario, los permisos, el scope o la IP impiden acceder al recurso.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/error-403](https://developers.mercadolibre.com.co/es_co/error-403)  
**Captura:** 2026-10-08T22:53:32.355Z

---

## [Gestiona tus aplicaciones](../markdown/gestiona-tus-aplicaciones.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:53:33.176Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/gestiona-tus-aplicaciones](https://developers.mercadolibre.com.co/es_co/gestiona-tus-aplicaciones)

# Gestiona tus aplicaciones

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:33.176Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestiona-tus-aplicaciones](https://developers.mercadolibre.com.co/es_co/gestiona-tus-aplicaciones)

## Resumen

La guía explica cómo consultar la ficha pública y los datos privados de una aplicación, revisar los grants de usuarios, listar aplicaciones autorizadas, revocar una autorización y consultar métricas de consumo. Las llamadas de ejemplo usan un access token Bearer; para los datos privados de la aplicación se indica usar el token del usuario propietario que la creó.

## Contenido y conceptos documentados

### Grants y estado de autorizaciones

Los grants incluyen `user_id`, `app_id`, `date_created` y `scopes` (`read`, `write` y, cuando se otorgó, `offline_access`). En DevCenter se pueden visualizar y exportar. La guía distingue los estados Nuevo (grant con menos de 24 horas), Activo (uso de APIs en los últimos 90 días) e Inactivo (sin llamadas durante ese período).

### Métricas de consumo

La respuesta de consumo agrupa solicitudes por estado HTTP y presenta recursos más consumidos y recursos con errores. La fecha es opcional; sin fechas se devuelve el consumo de los últimos 15 días. Los datos se actualizan hasta el día anterior y se recomiendan consultas mensuales para reducir el riesgo de timeout.

## Operaciones de API
## Operaciones de API

### Listar aplicaciones autorizadas por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/applications`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista las aplicaciones que un usuario autorizó, incluyendo fecha de autorización y scopes.

**Parámetros**

- `user_id` (path, obligatorio): Identificador del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista con user_id, app_id, date_created y scopes.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con user_id 26317316.

### Consultar detalles de una aplicación

**Método:** `GET`  
**Ruta:** `/applications/{app_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve la ficha de la aplicación. La página indica que los datos privados deben consultarse con el token del usuario que la creó.

**Parámetros**

- `app_id` (path, obligatorio): Identificador de la aplicación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo de respuesta: id, site_id, thumbnail, url, sandbox_mode, active, max_requests_per_hour y certification_status.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra la misma ruta para consultar los datos privados con el token del propietario.

### Consultar grants de una aplicación

**Método:** `GET`  
**Ruta:** `/applications/{app_id}/grants`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista los usuarios que otorgaron permisos a la aplicación y los scopes concedidos.

**Parámetros**

- `app_id` (path, obligatorio): Identificador de la aplicación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto con paging (total, limit, offset) y grants (user_id, app_id, date_created, scopes).

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Scopes de ejemplo: read, offline_access y write.

### Consultar métricas de consumo de aplicación

**Método:** `GET`  
**Ruta:** `/applications/v1/{app_id}/consumed-applications`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve el total de requests, su distribución por status y los recursos más consumidos o con errores.

**Parámetros**

- `app_id` (path, obligatorio): Identificador de la aplicación.
- `date_start` (query, opcional): Inicio del rango de fechas; el ejemplo lo incluye.
- `date_end` (query, opcional): Fin del rango de fechas; el ejemplo lo incluye.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Incluye app_id, total_request, request_by_status, top_apis_consumed y top_apis_consumed_error.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Sin fechas, la respuesta cubre los últimos 15 días; los datos están actualizados a D-1.

### Revocar autorización de usuario

**Método:** `DELETE`  
**Ruta:** `/users/{user_id}/applications/{app_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la autorización de un usuario a una aplicación.

**Parámetros**

- `user_id` (path, obligatorio): Identificador del usuario.
- `app_id` (path, obligatorio): Identificador de la aplicación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo de respuesta con user_id, app_id y msg: Autorización eliminada.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestiona-tus-aplicaciones](https://developers.mercadolibre.com.co/es_co/gestiona-tus-aplicaciones)  
**Captura:** 2026-10-08T22:53:33.176Z

---

## [Gestionar IPs de una aplicación](../markdown/gestionar-ips-de-una-aplicacion.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:53:34.108Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/gestionar-ips-de-una-aplicacion](https://developers.mercadolibre.com.co/es_co/gestionar-ips-de-una-aplicacion)

# Gestionar IPs de una aplicación

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:34.108Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestionar-ips-de-una-aplicacion](https://developers.mercadolibre.com.co/es_co/gestionar-ips-de-una-aplicacion)

## Resumen

Esta página describe la gestión de rangos IP desde DevCenter para aplicaciones habilitadas. La funcionalidad está limitada a integradores incluidos en la lista de permitidos y se opera desde la interfaz del administrador de la aplicación.

## Contenido y conceptos documentados

Los rangos aceptados son IPv4 o IPv6 en formato CIDR; el sistema valida el formato, la superposición y el límite disponible. Se pueden agregar rangos individualmente o cargar varios desde un CSV sin encabezados, con cada rango separado por coma. La carga masiva informa los registros exitosos y fallidos y permite descargar un CSV con errores para corregirlos. Para eliminar, se seleccionan uno o varios rangos y se confirma la acción.

## Operaciones de API

## Conceptos y recursos asociados

### Gestión de rangos IP de aplicaciones

Describe la administración visual de rangos IP permitidos desde DevCenter para integradores habilitados.

**Respuesta**

No documentado en la fuente.

**Ejemplos documentados**

- IPv4/IPv6 en CIDR; carga individual o CSV sin encabezados, con rangos separados por coma.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestionar-ips-de-una-aplicacion](https://developers.mercadolibre.com.co/es_co/gestionar-ips-de-una-aplicacion)  
**Captura:** 2026-10-08T22:53:34.108Z

---

## [Permisos funcionales](../markdown/permisos-funcionales.md)

Actualización indicada por la fuente: 04/03/2026. Captura: 2026-10-08T22:53:35.095Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/permisos-funcionales](https://developers.mercadolibre.com.co/es_co/permisos-funcionales)

# Permisos funcionales

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 04/03/2026  
**Captura:** 2026-10-08T22:53:35.095Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/permisos-funcionales](https://developers.mercadolibre.com.co/es_co/permisos-funcionales)

## Resumen

Los permisos funcionales definen qué recursos y métodos puede usar una aplicación cuando un usuario concede autorización. La página relaciona los scopes con áreas de la API y explica cómo resolver un rechazo por falta de permiso.

## Contenido y conceptos documentados

### Scopes

El scope de solo lectura habilita métodos `GET`; lectura y escritura habilita `PUT`, `POST` y `DELETE`. Los grupos descritos cubren usuarios, publicaciones, comunicación, publicidad, métricas del negocio, ventas y envíos, promociones y facturación. El permiso de Usuarios está activo por defecto. Cada grupo enumera recursos relacionados en la documentación.

### Error por permiso faltante

La respuesta de ejemplo usa HTTP `403` y el código `PA_UNAUTHORIZED_RESULT_FROM_POLICIES` con `blocked_by: PolicyAgent`. La solución indicada es habilitar en la configuración de la aplicación el permiso funcional asociado y sus scopes necesarios.

## Operaciones de API

## Conceptos y recursos asociados

### Error por falta de permiso funcional

La página ejemplifica un rechazo por políticas cuando la aplicación no tiene habilitado el permiso funcional correspondiente.

**Respuesta**

HTTP 403; code PA_UNAUTHORIZED_RESULT_FROM_POLICIES; blocked_by PolicyAgent.

**Errores documentados**

- ```json {   "code": "PA_UNAUTHORIZED_RESULT_FROM_POLICIES",   "meaning": "Al menos una política devolvió UNAUTHORIZED; status 403." } ```
### Scopes de permisos funcionales

Resume los permisos que se configuran para autorizar una aplicación y los métodos HTTP habilitados por los scopes.

**Respuesta**

No documentado en la fuente.

**Ejemplos documentados**

- Solo lectura habilita GET; lectura y escritura habilita PUT, POST y DELETE; Usuarios está activo por defecto.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/permisos-funcionales](https://developers.mercadolibre.com.co/es_co/permisos-funcionales)  
**Captura:** 2026-10-08T22:53:35.095Z

---

## [Realiza pruebas](../markdown/realiza-pruebas.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:53:35.894Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/realiza-pruebas](https://developers.mercadolibre.com.co/es_co/realiza-pruebas)

# Realiza pruebas

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:35.894Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/realiza-pruebas](https://developers.mercadolibre.com.co/es_co/realiza-pruebas)

## Resumen

Mercado Libre no ofrece un sandbox: la guía recomienda probar en producción con usuarios de test, que pueden simular acciones entre sí sin cargos ni sanciones para cuentas reales. Todas las operaciones de prueba deben usar usuarios y publicaciones de test; las credenciales se reciben al crear la cuenta y deben guardarse.

## Contenido y conceptos documentados

Se necesita un access token para crear un usuario de test y el body documentado contiene `site_id`. Se recomienda crear al menos un vendedor y un comprador de prueba. La guía indica un máximo de 10 usuarios de test por cuenta, eliminación de usuarios sin actividad durante 60 días y caducidad de estas cuentas. Para las publicaciones aconseja el título “Item de Prueba - Por favor, NO OFERTAR”, usar la categoría “Otros” cuando sea posible y no utilizar los tipos `gold` ni `gold_premium`. Para compras se usan tarjetas de prueba; el nombre y apellido del titular permite simular el resultado del pago (por ejemplo, `APRO APRO` para aprobación).

## Operaciones de API
## Operaciones de API

### Consultar usuario autenticado

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** Authorization: Bearer ACCESS_TOKEN

Ejemplo de llamada a /users/me que envía el access token en el header Authorization.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente para esta llamada.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo curl con token Bearer en el header.

### Crear usuario de test

**Método:** `POST`  
**Ruta:** `/users/test_user`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea un usuario de prueba para el sitio indicado.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "site_id": "Identificador del sitio donde operará el usuario de prueba."
}
```

**Respuesta**

Respuesta de ejemplo: id, nickname, password y site_status.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El ejemplo usa site_id MLA.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/realiza-pruebas](https://developers.mercadolibre.com.co/es_co/realiza-pruebas)  
**Captura:** 2026-10-08T22:53:35.894Z

---

## [Soporte para Integradores](../markdown/soporte-para-integradores.md)

Actualización indicada por la fuente: 18/09/2026. Captura: 2026-10-08T22:53:36.875Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/soporte-para-integradores](https://developers.mercadolibre.com.co/es_co/soporte-para-integradores)

# Soporte para Integradores

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 18/09/2026  
**Captura:** 2026-10-08T22:53:36.875Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/soporte-para-integradores](https://developers.mercadolibre.com.co/es_co/soporte-para-integradores)

## Resumen

La guía describe cómo abrir y seguir consultas o problemas técnicos con el Developer Partner Program (DPP), desde elegir la categoría y aplicación hasta aportar datos para reproducir un fallo y responder al equipo.

## Contenido y conceptos documentados

Los tickets pueden ser consultas o problemas. Ambos requieren asunto y descripción de hasta 5000 caracteres; los problemas permiten añadir vendedor afectado, IDs, método HTTP, recurso, request y respuesta. Para Productos se muestran las categorías Órdenes, Publicaciones, Pagos y Envíos. El portal asigna un número de caso y permite continuar el hilo por correo o desde View request. El bot está disponible 24/7; la atención personalizada opera de lunes a viernes de 9:00 a 18:00 GMT-3. Los SLA de primera respuesta personalizada son 2 días hábiles (Silver), 1 día hábil (Gold) y 3 horas hábiles (Platinum).

## Operaciones de API

## Conceptos y recursos asociados

### Soporte técnico para integradores

Describe el flujo del portal DPP para crear y seguir tickets de consultas o problemas técnicos.

**Respuesta**

No documentado en la fuente.

**Ejemplos documentados**

- Problemas pueden incluir método, recurso, request y respuesta; SLA personalizado: Silver 2 días hábiles, Gold 1 día hábil, Platinum 3 horas hábiles.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/soporte-para-integradores](https://developers.mercadolibre.com.co/es_co/soporte-para-integradores)  
**Captura:** 2026-10-08T22:53:36.875Z

---

## [Validador de publicaciones](../markdown/validador-de-publicaciones.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:53:37.890Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/validador-de-publicaciones](https://developers.mercadolibre.com.co/es_co/validador-de-publicaciones)

# Validador de publicaciones

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:37.890Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/validador-de-publicaciones](https://developers.mercadolibre.com.co/es_co/validador-de-publicaciones)

## Resumen

El validador permite revisar el JSON de una publicación antes de publicarla y devuelve errores que ayudan a corregir tipos de datos y otros campos. La validación es opcional; la guía recomienda usarla durante el desarrollo, teniendo presente que no existe un entorno de preproducción.

## Contenido y conceptos documentados

Los ejemplos cubren una publicación estándar, una publicación con variaciones y un inmueble. El body puede incluir campos como `title`, `category_id`, `price`, `currency_id`, `available_quantity`, `buying_mode`, `listing_type_id`, `condition`, `description` y `pictures`; el ejemplo con variaciones agrega `variations`. La página muestra un error `400` con `message: body.invalid_field_types` cuando los tipos no coinciden (por ejemplo, precio como texto), y señala que una validación correcta responde `204 No Content`. No publica un catálogo completo de errores.

## Operaciones de API
## Operaciones de API

### Validar publicación

**Método:** `POST`  
**Ruta:** `/items/validate`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Valida el JSON de un ítem antes de publicarlo y devuelve errores de validación o 204 No Content si es válido.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "title",
    "category_id",
    "price",
    "currency_id",
    "available_quantity",
    "buying_mode",
    "listing_type_id",
    "condition",
    "description",
    "pictures"
  ],
  "note": "Son campos presentes en ejemplos; la página no declara que todos sean obligatorios."
}
```

**Respuesta**

204 No Content si la publicación pasa la validación; los ejemplos inválidos devuelven un body con message, error, status y cause.

**Errores documentados**

- ```json {   "meaning": "La respuesta de ejemplo usa message=body.invalid_field_types e informa los campos cuyo tipo recibido no coincide con el esperado.",   "code": "400" } ```

**Ejemplos**

- Ejemplos: publicación estándar, publicación con variations e inmueble.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/validador-de-publicaciones](https://developers.mercadolibre.com.co/es_co/validador-de-publicaciones)  
**Captura:** 2026-10-08T22:53:37.890Z

---
