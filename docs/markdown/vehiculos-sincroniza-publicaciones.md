---
id: "vehiculos-sincroniza-publicaciones"
title: "Sincroniza publicaciones (vehículos)"
section: "Guía para vehículos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/vehiculos-sincroniza-publicaciones"
source_updated_at: "28/08/2026"
captured_at: "2026-10-08T22:53:23.539Z"
sha256: "ccf57a6d3e68a41b036d96814120d576b89c45d4dd9e86e2763e24518241f1e8"
---

# Sincroniza publicaciones (vehículos)

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 28/08/2026  
**Captura:** 2026-10-08T22:53:23.539Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/vehiculos-sincroniza-publicaciones](https://developers.mercadolibre.com.co/es_co/vehiculos-sincroniza-publicaciones)

## Resumen

Documenta la actualización y sincronización de publicaciones de vehículos, incluyendo cambios de contenido, estado y datos de contacto. También describe restricciones y validaciones para `seller_contact`.

## Contenido y conceptos documentados

- La fuente enumera como actualizables `title`, `price`, `video`, `pictures`, `description`, `location`, `attributes` y `category`; incluye también `seller_contact`. El estado cambia con valores en minúscula: `cerrado`, `pausado` o `activo`.
- `seller_contact` contempla `contact`, `other_info`, códigos y números telefónicos, `email`, `webpage`, `country_code2` y `phone2`. La fuente lista errores HTTP 400 para campos obligatorios o inválidos.
- Si el PUT devuelve 409 por optimistic locking, existe un conflicto de actualización. Autenticación mostrada: OAuth Bearer.

## Operaciones de API
## Operaciones de API

### PUT /items/{ITEM_ID}

**Método:** `PUT`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza campos permitidos de una publicación vehicular, atributos o estado.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `status` (query, opcional): Estado en minúscula: cerrado, pausado o activo.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Validaciones seller_contact y campos obligatorios/numéricos inválidos." } ```
- ```json {   "code": "409",   "meaning": "Optimistic locking conflict al actualizar el ítem." } ```

**Ejemplos**

- La captura incluye ejemplos de llamada para este recurso.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/vehiculos-sincroniza-publicaciones](https://developers.mercadolibre.com.co/es_co/vehiculos-sincroniza-publicaciones)  
**Captura:** 2026-10-08T22:53:23.539Z
