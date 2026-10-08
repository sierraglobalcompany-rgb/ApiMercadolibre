---
id: "tienda-oficial"
title: "Tiendas Oficiales"
section: "Guía para productos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/tienda-oficial"
source_updated_at: "27/02/2026"
captured_at: "2026-10-08T22:52:52.494Z"
sha256: "00f05d533956d6206f7ce9f44140168a097987c403744c8ea1ff481d408c967a"
---

# Tiendas Oficiales

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 27/02/2026  
**Captura:** 2026-10-08T22:52:52.494Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/tienda-oficial](https://developers.mercadolibre.com.co/es_co/tienda-oficial)

## Resumen

Documenta cómo consultar las marcas asociadas a un usuario de Tienda Oficial y cómo recuperar los datos de una marca concreta. Un usuario puede tener una o varias marcas; en publicaciones, la tienda se identifica mediante `official_store_id`.

## Contenido y conceptos documentados

### Marcas y respuestas

- Ambas consultas muestran `Authorization: Bearer $ACCESS_TOKEN`. La lista incluye estado del vínculo, sitio y marcas, con `official_store_id`, nombre, estado, nombre de fantasía, reputación, URLs, palabras clave e imágenes.
- Para consultar una marca, se envían `USER_ID` y `BRAND` en la ruta. La página muestra 400 cuando el identificador contiene caracteres distintos de dígitos.
- Para sellers multimarca, la publicación debe incluir un `official_store_id` válido: omitirlo puede producir `item.official_store_id.invalid` (400); usar uno no permitido en el sitio puede producir 403. Cuerpos y errores restantes: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Listar marcas de Tienda Oficial

**Método:** `GET`  
**Ruta:** `/users/$USER_ID/brands`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene marcas vinculadas a un usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- status
- cust_id
- shield_id
- site_id
- user_type
- brands[].site_id
- brands[].official_store_id
- brands[].name
- brands[].type
- brands[].status
- brands[].fantasy_name
- brands[].date_created
- brands[].landing_permalink
- brands[].keywords
- brands[].pictures

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Un usuario puede tener varias marcas.

### Consultar marca del usuario

**Método:** `GET`  
**Ruta:** `/users/$USER_ID/brands/$BRAND`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalle de una marca vinculada al usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `BRAND` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- official_store_id
- name
- type
- status
- brand_id
- brand_name
- brand_registry

**Errores documentados**

- ```json {   "code": 400,   "meaning": "officialStoreId debe contener solo dígitos." } ```

**Ejemplos**

- La página muestra 400 para identificador no numérico.

### Referencia HTTP GET /users/1477536226/brands/aaaaa

**Método:** `GET`  
**Ruta:** `/users/1477536226/brands/aaaaa`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/1477536226/brands/aaaaa. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/tienda-oficial](https://developers.mercadolibre.com.co/es_co/tienda-oficial)  
**Captura:** 2026-10-08T22:52:52.494Z
