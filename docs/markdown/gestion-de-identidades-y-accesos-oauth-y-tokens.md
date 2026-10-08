---
id: "gestion-de-identidades-y-accesos-oauth-y-tokens"
title: "Gestión de Identidades y Accesos (OAuth y Tokens)"
section: "Guía de seguridad"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/gestion-de-identidades-y-accesos-oauth-y-tokens"
source_updated_at: "30/03/2026"
captured_at: "2026-10-08T22:50:09.198Z"
sha256: "ef15d728a4847f45125c7154e572696b371064838b596bbc32d4879770cc308b"
---

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
