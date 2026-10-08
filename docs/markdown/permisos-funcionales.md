---
id: "permisos-funcionales"
title: "Permisos funcionales"
section: "Primeros pasos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/permisos-funcionales"
source_updated_at: "04/03/2026"
captured_at: "2026-10-08T22:53:35.095Z"
sha256: "2ff7b7b204c721eecf77b5fbc5d79a27e73775d36515bc9754c2f861c2dc17b9"
---

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
