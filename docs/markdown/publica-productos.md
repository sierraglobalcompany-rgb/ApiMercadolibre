---
id: "publica-productos"
title: "Publicar productos"
section: "Guía para productos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/publica-productos"
source_updated_at: "09/01/2026"
captured_at: "2026-10-08T22:52:40.362Z"
sha256: "1f10c5259d56534aad2c1f89098c69fa4bd3adf093a60eec554bc69da117a2ae"
---

# Publicar productos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 09/01/2026  
**Captura:** 2026-10-08T22:52:40.362Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/publica-productos](https://developers.mercadolibre.com.co/es_co/publica-productos)

## Resumen

Guía general para consultar y crear publicaciones, con ejemplos de atributos, condiciones, términos de venta, variaciones, envío y pago inmediato. Recomienda a los nuevos flujos considerar el modelo User Products.

## Contenido y conceptos documentados

### Reglas de publicación

- Para consultar una publicación se usa el recurso de ítems; las fichas de categoría permiten conocer atributos y términos de venta antes de crearla.
- La creación se hace con `POST /items`. La fuente incluye campos como título, categoría, precio, moneda, cantidad, modo de compra, tipo de publicación, imágenes, atributos, términos de venta, envío y variaciones, según el ejemplo.
- `exclusive_channel` ya no se admite: debe usarse `channels`. Para nuevas implementaciones, la condición se especifica como `item_condition` en `attributes`; `condition` sigue por compatibilidad. La consulta de valores por categoría se vincula a la ficha técnica.
- Se puede publicar con cantidad cero para Fulfillment en Argentina, México y Brasil. Las categorías con pago inmediato se consultan mediante el recurso de categorías; la publicación usa el tag `immediate_payment` cuando corresponda.
- La fuente también indica que el título puede cambiarse vía PUT mientras `sold_quantity=0`. Los cuerpos completos y códigos de error: No documentado en la fuente salvo los ejemplos y la tabla de códigos enlazada.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /domains/{DOMAIN_ID}/technical_specs

La fuente menciona la ruta /domains/{DOMAIN_ID}/technical_specs, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/domains/{DOMAIN_ID}/technical_specs`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /users

La fuente menciona la ruta /users, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/users`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar atributos de categoría

**Método:** `GET`  
**Ruta:** `/categories/$CATEGORY_ID/attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene atributos y metadatos que aplican al publicar en una categoría.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- name
- value_type
- values
- attribute_group_id
- attribute_group_name
- required
- conditional_required

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar términos de venta

**Método:** `GET`  
**Ruta:** `/categories/$CATEGORY_ID/sale_terms`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene términos que pueden enviarse en una publicación de la categoría.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- name
- value_id
- value_name
- value_type

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página describe términos de garantía.

### Consultar publicación

**Método:** `GET`  
**Ruta:** `/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene la ficha de una publicación.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- site_id
- title
- category_id
- seller_id
- price
- currency_id
- available_quantity
- sold_quantity
- listing_type_id
- attributes
- variations
- sale_terms
- shipping
- channels

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar pago inmediato de categoría

**Método:** `GET`  
**Ruta:** `/sites/categories/$CATEGORY_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta si una categoría exige Mercado Pago como única opción.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- immediate_payment
- item_conditions

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Crear publicación

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea un ítem con los datos comerciales, atributos y opciones de logística permitidos.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "title",
    "category_id",
    "price",
    "currency_id",
    "available_quantity",
    "buying_mode",
    "listing_type_id",
    "pictures",
    "attributes",
    "sale_terms",
    "shipping",
    "tags",
    "variations",
    "channels",
    "item_condition"
  ]
}
```

**Respuesta**

- id
- site_id
- title
- seller_id
- category_id
- price
- currency_id
- available_quantity
- status
- permalink

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Incluye ejemplos para Argentina y Brasil, incluido tag immediate_payment.

### Actualizar publicación

**Método:** `PUT`  
**Ruta:** `/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica el título en el flujo descrito cuando sold_quantity es cero.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "title (solo cuando sold_quantity=0, según la página)"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Referencia HTTP POST /items/{ITEM_ID}

**Método:** `POST`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /items/{ITEM_ID}. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/publica-productos](https://developers.mercadolibre.com.co/es_co/publica-productos)  
**Captura:** 2026-10-08T22:52:40.362Z
