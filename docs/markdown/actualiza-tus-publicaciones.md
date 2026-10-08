---
id: "actualiza-tus-publicaciones"
title: "Actualiza tus publicaciones"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/actualiza-tus-publicaciones"
source_updated_at: "28/08/2026"
captured_at: "2026-10-08T22:50:16.377Z"
sha256: "ed573033af387aadd717d68c418d27d880a95a3932cad938154771bae83b702a"
---

# Actualiza tus publicaciones

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 28/08/2026  
**Captura:** 2026-10-08T22:50:16.377Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/actualiza-tus-publicaciones](https://developers.mercadolibre.com.co/es_co/actualiza-tus-publicaciones)

## Resumen

Documenta actualización parcial, seller_contact, ubicación, tipo de publicación, estado y eliminación de inmuebles.

## Contenido y conceptos documentados

- PUT /items/{item_id} modifica solo los campos enviados; desde 01/10/2026 country_code2 y phone2 son obligatorios en seller_contact según la fuente.
- Cerrar y luego enviar deleted=true elimina el ítem de forma irreversible.

## Operaciones de API

## Conceptos y recursos asociados

### Actualiza tus publicaciones

Documenta actualización parcial, seller_contact, ubicación, tipo de publicación, estado y eliminación de inmuebles.
## Operaciones de API

### Actualizar o eliminar inmueble

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica campos enviados; para eliminación irreversible, cerrar y luego deleted=true.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "title",
    "price",
    "video",
    "pictures",
    "description",
    "location",
    "attributes",
    "category",
    "seller_contact",
    "official_store_id",
    "status",
    "deleted"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "ítem actualizado",
    "status",
    "sub_status"
  ]
}
```

**Errores documentados**

- ```json {   "code": "seller_contact.required",   "http_status": 400,   "meaning": "Falta seller_contact." } ```
- ```json {   "code": "seller_contact.country_code2.required",   "http_status": 400,   "meaning": "Falta country_code2." } ```
- ```json {   "code": "seller_contact.phone2.required",   "http_status": 400,   "meaning": "Falta phone2." } ```
- ```json {   "code": "seller_contact.country_code2.invalid",   "http_status": 400,   "meaning": "Formato inválido." } ```
- ```json {   "code": "seller_contact.phone2.invalid",   "http_status": 400,   "meaning": "Formato inválido." } ```
- ```json {   "code": "requires_picture",   "http_status": 400,   "meaning": "Faltan imágenes para los tipos indicados." } ```
- ```json {   "code": "item optimistic locking error: conflict",   "http_status": 409,   "meaning": "Esperar unos segundos y reintentar." } ```

**Ejemplos**

- {"price":100000001}
- seller_contact.country_code2 y phone2 obligatorios desde 01/10/2026

### Cambiar tipo de destaque

**Método:** `POST`  
**Ruta:** `/items/{item_id}/listing_type`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Requiere paquete gold o gold_premium contratado.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "id"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "listing_type_id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- {"id":"gold_premium"}

**Fuente:** [https://developers.mercadolibre.com.co/es_co/actualiza-tus-publicaciones](https://developers.mercadolibre.com.co/es_co/actualiza-tus-publicaciones)  
**Captura:** 2026-10-08T22:50:16.377Z
