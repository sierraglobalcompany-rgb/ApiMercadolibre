# Guía de seguridad

8 páginas del portal oficial en esta área.

## [Autenticación segura](../markdown/autenticacion-segura.md)

Actualización indicada por la fuente: 30/03/2026. Captura: 2026-10-08T22:50:07.455Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/autenticacion-segura](https://developers.mercadolibre.com.co/es_co/autenticacion-segura)

# Autenticación segura

**Área:** Guía de seguridad  
**Actualización indicada por la fuente:** 30/03/2026  
**Captura:** 2026-10-08T22:50:07.455Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/autenticacion-segura](https://developers.mercadolibre.com.co/es_co/autenticacion-segura)

## Resumen

Reúne recomendaciones sobre contraseñas, hash, MFA, fuerza bruta, recuperación, sesiones y cookies.

## Contenido y conceptos documentados

- Recomienda contraseñas de 12 caracteres, Argon2 o bcrypt, MFA y cookies Secure, HttpOnly y SameSite.

## Operaciones de API

## Conceptos y recursos asociados

### Autenticación segura

Reúne recomendaciones sobre contraseñas, hash, MFA, fuerza bruta, recuperación, sesiones y cookies.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/autenticacion-segura](https://developers.mercadolibre.com.co/es_co/autenticacion-segura)  
**Captura:** 2026-10-08T22:50:07.455Z

---

## [Control de acceso y autorización](../markdown/control-de-acceso-y-autorizacion.md)

Actualización indicada por la fuente: 30/03/2026. Captura: 2026-10-08T22:50:08.356Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/control-de-acceso-y-autorizacion](https://developers.mercadolibre.com.co/es_co/control-de-acceso-y-autorizacion)

# Control de acceso y autorización

**Área:** Guía de seguridad  
**Actualización indicada por la fuente:** 30/03/2026  
**Captura:** 2026-10-08T22:50:08.356Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/control-de-acceso-y-autorizacion](https://developers.mercadolibre.com.co/es_co/control-de-acceso-y-autorizacion)

## Resumen

Describe mínimo privilegio, denegación por defecto, verificación en cada petición, separación de sellers y mitigación IDOR.

## Contenido y conceptos documentados

- La autorización se valida en backend y debe comprobar que el recurso pertenece a un seller asignado.

## Operaciones de API

## Conceptos y recursos asociados

### Control de acceso y autorización

Describe mínimo privilegio, denegación por defecto, verificación en cada petición, separación de sellers y mitigación IDOR.
### Ruta mencionada /orders/123

La fuente menciona la ruta /orders/123, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/orders/123`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /orders/12345

La fuente menciona la ruta /orders/12345, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/orders/12345`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /orders/{order_id}

La fuente menciona la ruta /orders/{order_id}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/orders/{order_id}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /orders/123456

La fuente menciona la ruta /orders/123456, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/orders/123456`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/control-de-acceso-y-autorizacion](https://developers.mercadolibre.com.co/es_co/control-de-acceso-y-autorizacion)  
**Captura:** 2026-10-08T22:50:08.356Z

---

## [Gestión de Identidades y Accesos (OAuth y Tokens)](../markdown/gestion-de-identidades-y-accesos-oauth-y-tokens.md)

Actualización indicada por la fuente: 30/03/2026. Captura: 2026-10-08T22:50:09.198Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/gestion-de-identidades-y-accesos-oauth-y-tokens](https://developers.mercadolibre.com.co/es_co/gestion-de-identidades-y-accesos-oauth-y-tokens)

# Gestión de Identidades y Accesos (OAuth y Tokens)

**Área:** Guía de seguridad  
**Actualización indicada por la fuente:** 30/03/2026  
**Captura:** 2026-10-08T22:50:09.198Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestion-de-identidades-y-accesos-oauth-y-tokens](https://developers.mercadolibre.com.co/es_co/gestion-de-identidades-y-accesos-oauth-y-tokens)

## Resumen

Explica custodia de credenciales OAuth, tokens de acceso y refresh, renovación y revocación.

## Contenido y conceptos documentados

- Recomienda Authorization: Bearer, cifrado en reposo y no registrar tokens en logs.

## Operaciones de API

## Conceptos y recursos asociados

### Gestión de Identidades y Accesos (OAuth y Tokens)

Explica custodia de credenciales OAuth, tokens de acceso y refresh, renovación y revocación.
## Operaciones de API

### Ejemplo de consulta de órdenes con token

**Método:** `GET`  
**Ruta:** `/orders`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La página ilustra enviar el token OAuth en Authorization y no en la URL.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo seguro: Authorization: Bearer $ACCESS_TOKEN; no incluir access_token en query string.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestion-de-identidades-y-accesos-oauth-y-tokens](https://developers.mercadolibre.com.co/es_co/gestion-de-identidades-y-accesos-oauth-y-tokens)  
**Captura:** 2026-10-08T22:50:09.198Z

---

## [Gestión de inicidentes](../markdown/gestion-de-incidentes.md)

Actualización indicada por la fuente: 06/04/2026. Captura: 2026-10-08T22:50:10.452Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/gestion-de-incidentes](https://developers.mercadolibre.com.co/es_co/gestion-de-incidentes)

# Gestión de inicidentes

**Área:** Guía de seguridad  
**Actualización indicada por la fuente:** 06/04/2026  
**Captura:** 2026-10-08T22:50:10.452Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestion-de-incidentes](https://developers.mercadolibre.com.co/es_co/gestion-de-incidentes)

## Resumen

Propone clasificar, contener y resolver incidentes, asignar responsables, comunicar y elaborar post-mortems.

## Contenido y conceptos documentados

- Incluye severidades P1–P4 y pide notificar a security@mercadolibre.com si se afectan tokens o datos.

## Operaciones de API

## Conceptos y recursos asociados

### Gestión de inicidentes

Propone clasificar, contener y resolver incidentes, asignar responsables, comunicar y elaborar post-mortems.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestion-de-incidentes](https://developers.mercadolibre.com.co/es_co/gestion-de-incidentes)  
**Captura:** 2026-10-08T22:50:10.452Z

---

## [Infraestructura (Cifrado y TLS)](../markdown/infraestructura.md)

Actualización indicada por la fuente: 30/03/2026. Captura: 2026-10-08T22:50:11.690Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/infraestructura](https://developers.mercadolibre.com.co/es_co/infraestructura)

# Infraestructura (Cifrado y TLS)

**Área:** Guía de seguridad  
**Actualización indicada por la fuente:** 30/03/2026  
**Captura:** 2026-10-08T22:50:11.690Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/infraestructura](https://developers.mercadolibre.com.co/es_co/infraestructura)

## Resumen

Resume requisitos de TLS, suites criptográficas seguras y validación de certificados.

## Contenido y conceptos documentados

- TLS 1.2 es mínimo aceptado y TLS 1.3 recomendado; no se debe deshabilitar la validación del certificado.

## Operaciones de API

## Conceptos y recursos asociados

### Infraestructura (Cifrado y TLS)

Resume requisitos de TLS, suites criptográficas seguras y validación de certificados.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/infraestructura](https://developers.mercadolibre.com.co/es_co/infraestructura)  
**Captura:** 2026-10-08T22:50:11.690Z

---

## [Introducción](../markdown/introduccion-seguridad.md)

Actualización indicada por la fuente: 30/03/2026. Captura: 2026-10-08T22:50:12.581Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/introduccion-seguridad](https://developers.mercadolibre.com.co/es_co/introduccion-seguridad)

# Introducción

**Área:** Guía de seguridad  
**Actualización indicada por la fuente:** 30/03/2026  
**Captura:** 2026-10-08T22:50:12.581Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/introduccion-seguridad](https://developers.mercadolibre.com.co/es_co/introduccion-seguridad)

## Resumen

Presenta la guía de seguridad y la responsabilidad compartida entre la plataforma y el integrador.

## Contenido y conceptos documentados

- Mercado Libre protege la plataforma; el integrador responde por su aplicación, infraestructura y datos procesados.

## Operaciones de API

## Conceptos y recursos asociados

### Introducción

Presenta la guía de seguridad y la responsabilidad compartida entre la plataforma y el integrador.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/introduccion-seguridad](https://developers.mercadolibre.com.co/es_co/introduccion-seguridad)  
**Captura:** 2026-10-08T22:50:12.581Z

---

## [Monitoreo](../markdown/monitoreo.md)

Actualización indicada por la fuente: 30/03/2026. Captura: 2026-10-08T22:50:14.012Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/monitoreo](https://developers.mercadolibre.com.co/es_co/monitoreo)

# Monitoreo

**Área:** Guía de seguridad  
**Actualización indicada por la fuente:** 30/03/2026  
**Captura:** 2026-10-08T22:50:14.012Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/monitoreo](https://developers.mercadolibre.com.co/es_co/monitoreo)

## Resumen

Describe registros de auditoría, anomalías, alertas y métricas de monitoreo.

## Contenido y conceptos documentados

- Los logs pueden incluir fecha UTC, usuario, acción, recurso, resultado, IP y request_id; deben excluir secretos y PII completa.

## Operaciones de API

## Conceptos y recursos asociados

### Monitoreo

Describe registros de auditoría, anomalías, alertas y métricas de monitoreo.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/monitoreo](https://developers.mercadolibre.com.co/es_co/monitoreo)  
**Captura:** 2026-10-08T22:50:14.012Z

---

## [Seguridad de aplicaciones](../markdown/seguridad-apps.md)

Actualización indicada por la fuente: 23/06/2026. Captura: 2026-10-08T22:50:15.089Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/seguridad-apps](https://developers.mercadolibre.com.co/es_co/seguridad-apps)

# Seguridad de aplicaciones

**Área:** Guía de seguridad  
**Actualización indicada por la fuente:** 23/06/2026  
**Captura:** 2026-10-08T22:50:15.089Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/seguridad-apps](https://developers.mercadolibre.com.co/es_co/seguridad-apps)

## Resumen

Cubre protección de PII, validación de entradas, errores seguros, webhooks, rate limiting y dependencias.

## Contenido y conceptos documentados

- Recomienda cifrar y minimizar datos personales, validar en backend y procesar webhooks asíncronamente.

## Operaciones de API

## Conceptos y recursos asociados

### Seguridad de aplicaciones

Cubre protección de PII, validación de entradas, errores seguros, webhooks, rate limiting y dependencias.
## Operaciones de API

### Consultar recurso notificado en webhook

**Método:** `GET`  
**Ruta:** `/orders/{order_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La guía recomienda tratar el webhook como aviso y consultar el recurso oficial para validar su estado.

**Parámetros**

- `order_id` (path, obligatorio): ID de la orden incluida en resource.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET del recurso usando el access token del seller.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/seguridad-apps](https://developers.mercadolibre.com.co/es_co/seguridad-apps)  
**Captura:** 2026-10-08T22:50:15.089Z

---
