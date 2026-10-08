---
id: "publica-servicios-vis"
title: "Publica servicios"
section: "Guía para servicios"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/publica-servicios-vis"
source_updated_at: "15/03/2023"
captured_at: "2026-10-08T22:53:09.203Z"
sha256: "10ff24f3bc0f256cb74a85c9024d4756526299e277e1a1bfe3edfcdcf71f9e81"
---

# Publica servicios

**Área:** Guía para servicios  
**Actualización indicada por la fuente:** 15/03/2023  
**Captura:** 2026-10-08T22:53:09.203Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/publica-servicios-vis](https://developers.mercadolibre.com.co/es_co/publica-servicios-vis)

## Resumen

Expone campos generales de publicaciones de servicios, consulta de ítems, tipos de publicación y un ejemplo de creación de clasificado.

## Contenido y conceptos documentados

- La publicación se representa como un ítem. El ejemplo de consulta muestra identidad, título, categoría, precio, moneda, disponibilidad, modalidad, fotos, contacto, ubicación, atributos y descripción.
- El ejemplo de creación usa POST y buying_mode=classified, pero la captura no muestra la URL destino; no se registra una ruta supuesta. Está basado en MLA y advierte cambiar category_id, currency_id y posiblemente listing_type_id para otros países.
- seller_custom_field es un string de uso interno, distinto de SELLER_SKU. listing_types permite conocer los tipos aceptados por site.

## Operaciones de API

## Conceptos y recursos asociados

### Ejemplo de creación de servicio

La fuente muestra una solicitud POST para crear un clasificado que requiere access_token, pero la captura no contiene la URL destino. El cuerpo enumera title, category_id, price, currency_id, available_quantity, buying_mode=classified, listing_type_id, condition, pictures, seller_contact, location, attributes y description.

**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

**Solicitud**

Ejemplo de JSON para clasificado con seller_contact, location, attributes e información básica de publicación; valores ilustrativos para MLA.

**Respuesta**

Ejemplo de respuesta con id, site_id, title, sold_quantity y permalink.

**Ejemplos documentados**

- La fuente no documenta ruta del POST; señala que el ejemplo usa categorías/moneda/tipo de publicación de MLA y deben cambiarse para otros países.
## Operaciones de API

### Consultar publicación

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los datos de una publicación de servicio/ítem por ID precedido del site_id.

**Parámetros**

- `item_id` (path, obligatorio): ID completo del ítem con prefijo del site.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con id, site_id, title, seller_id, category_id, price, currency_id, available_quantity, buying_mode, listing_type_id, pictures, seller_contact, location, attributes y description.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /items/MLA612001263.

### Listar tipos de publicación

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/listing_types`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta listing_type_id disponibles por site.

**Parámetros**

- `site_id` (path, obligatorio): Código del site.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Array con site_id, id y name; se ejemplifican gold_pro, gold_premium, gold_special, gold, silver, bronze y free.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/listing_types.

### Actualizar campo personalizado del vendedor

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza seller_custom_field, campo de uso interno distinto de SELLER_SKU.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

JSON con seller_custom_field como string.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- PUT /items/MLA599074368 con seller_custom_field.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/publica-servicios-vis](https://developers.mercadolibre.com.co/es_co/publica-servicios-vis)  
**Captura:** 2026-10-08T22:53:09.203Z
