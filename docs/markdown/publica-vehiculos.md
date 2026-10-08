---
id: "publica-vehiculos"
title: "Publica vehículos"
section: "Guía para vehículos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/publica-vehiculos"
source_updated_at: "28/08/2026"
captured_at: "2026-10-08T22:53:20.752Z"
sha256: "cf55cfe9ae6acd54129a395641f218b541d7e20c1ced1af0d96557e7ff664a31"
---

# Publica vehículos

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 28/08/2026  
**Captura:** 2026-10-08T22:53:20.752Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/publica-vehiculos](https://developers.mercadolibre.com.co/es_co/publica-vehiculos)

## Resumen

Describe la creación y consulta de publicaciones de vehículos, la carga de descripción y la búsqueda de avisos por tags. Detalla atributos como placa, chasis, ubicación, financiación y contacto del vendedor.

## Contenido y conceptos documentados

- Para crear la publicación se envía un objeto de ítem con atributos vehiculares. La placa debe corresponder al vehículo y cumplir formatos por país; se enumeran formatos para Brasil, Argentina y Chile. Para ubicación se usa el ID de barrio o ciudad correspondiente.
- En publicaciones de concesionarios, `seller_contact` debe enviarse completo; la fuente enumera `contact`, `other_info`, `country_code`, `area_code`, `phone`, `email`, `webpage`, `country_code2` y datos relacionados. Si falta cuando aplica, se rechaza con HTTP 400.
- La financiación usa sale terms `WITH_FINANCING_OPTIONS` y `INITIAL_PAYMENT_AMOUNT`; la fuente indica habilitación para MLA. La descripción se crea después del ítem, en texto plano y sin datos de contacto. Para avisos con tag de moderación se consulta `users/{USER_ID}/items/search?tags={TAG}`.

## Operaciones de API
## Operaciones de API

### GET /items/{ITEM_ID}

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta los datos de un vehículo publicado.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Falta seller_contact cuando es obligatorio para perfil de concesionario." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/{ITEM_ID}/description

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/description`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la descripción del ítem.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "text",
    "plain_text",
    "date_created",
    "snapshot"
  ]
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Falta seller_contact cuando es obligatorio para perfil de concesionario." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}/items/search

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista publicaciones del usuario filtradas por `tags`.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `tags` (query, obligatorio): Tag por el que se filtran publicaciones.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Falta seller_contact cuando es obligatorio para perfil de concesionario." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### POST /items

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una publicación de vehículo.

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
    "attributes",
    "location",
    "seller_contact"
  ],
  "summary": "Datos de creación de la publicación vehicular; los requisitos dependen de sitio y perfil."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Falta seller_contact cuando es obligatorio para perfil de concesionario." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### POST /items/{ITEM_ID}/description

**Método:** `POST`  
**Ruta:** `/items/{ITEM_ID}/description`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea la descripción después de crear la publicación.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Falta seller_contact cuando es obligatorio para perfil de concesionario." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/publica-vehiculos](https://developers.mercadolibre.com.co/es_co/publica-vehiculos)  
**Captura:** 2026-10-08T22:53:20.752Z
