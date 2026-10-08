---
id: "producto-consulta-usuarios"
title: "Consulta usuarios"
section: "Recursos de la API"
subsection: "Usuarios"
url: "https://developers.mercadolibre.com.co/es_co/producto-consulta-usuarios"
source_updated_at: "12/01/2026"
captured_at: "2026-10-08T22:53:43.459Z"
sha256: "b3b228163414ac6e2401e6d99b9072f96b4e7eaf08dc08e3a0d993627edca9e4"
---

# Consulta usuarios

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 12/01/2026  
**Captura:** 2026-10-08T22:53:43.459Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/producto-consulta-usuarios](https://developers.mercadolibre.com.co/es_co/producto-consulta-usuarios)

## Resumen

Esta guía muestra cómo consultar el usuario autenticado y la información pública o privada de otro usuario. La respuesta puede incluir identidad, contacto, reputación, estado de cuenta y datos de ventas; la fuente advierte que la información privada no debe divulgarse. Los IDs nuevos pueden exceder Int32, por lo que deben almacenarse como Int64.

## Contenido y conceptos documentados

La respuesta de `/users/me` incluye el perfil del usuario del token. `/users/{user_id}` devuelve datos públicos y, cuando el usuario autorizó la aplicación y se usa un token válido, también puede incluir datos privados como nombre, email, teléfono y dirección. La página señala el error HTTP `206 Partial Content` cuando falla la consulta de algunos datos, por ejemplo la reputación.

## Operaciones de API
## Operaciones de API

### Consultar información de usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve el perfil público del usuario; si autorizó la aplicación y se usa su token, el ejemplo incluye datos privados adicionales.

**Parámetros**

- `user_id` (path, obligatorio): Identificador del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

El ejemplo público contiene perfil y reputación; el ejemplo autorizado también muestra contacto e información privada.

**Errores documentados**

- ```json {   "code": "206 Partial Content",   "meaning": "La API puede devolver datos incompletos si falla la consulta de algún dato, como la reputación." } ```

**Ejemplos**

- La fuente advierte que los IDs pueden exceder Int32 y deben manejarse como Int64.

### Consultar datos del usuario autenticado

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene la información asociada al usuario representado por el access token.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con id, nickname, registro, país, perfil, reputación y estado; algunos campos pueden ser privados del usuario autenticado.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/producto-consulta-usuarios](https://developers.mercadolibre.com.co/es_co/producto-consulta-usuarios)  
**Captura:** 2026-10-08T22:53:43.459Z
