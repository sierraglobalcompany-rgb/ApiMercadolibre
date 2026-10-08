---
id: "identificadores-de-productos"
title: "Identificadores de productos"
section: "Guía para productos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/identificadores-de-productos"
source_updated_at: "30/12/2025"
captured_at: "2026-10-08T22:52:02.036Z"
sha256: "95c0f45476d3a85dd0958dd323391e4924991e0b39b7aaf363bc0e59c41d457b"
---

# Identificadores de productos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:52:02.036Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/identificadores-de-productos](https://developers.mercadolibre.com.co/es_co/identificadores-de-productos)

## Resumen

Explica cómo manejar identificadores de producto, especialmente GTIN, al crear o actualizar publicaciones y variaciones, y cómo consultar los atributos devueltos. La lógica depende de si el identificador aplica al producto y de las razones documentadas para no enviarlo.

## Contenido y conceptos documentados

- La página distingue identificadores GTIN y describe su lógica de uso como atributo. En publicación se muestra `attributes` con `id: GTIN`; en publicaciones con variaciones el dato se informa en la variación correspondiente. También documenta razones por las que puede omitirse el GTIN y cómo consultar todos los atributos.
- Los ejemplos incluyen alta de ítems, actualización de atributos y variaciones y consulta con `include_attributes=all`. Si falta un GTIN marcado como `conditional_required`, se documenta el error 400 `item.attribute.missing_conditional_required` (cause_id 7810). Si no existe GTIN, puede enviarse `EMPTY_GTIN_REASON` en los casos permitidos; la fuente también muestra este atributo como condicionalmente requerido.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /items/y

La fuente menciona la ruta /items/y, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/items/y`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /categories/{CATEGORY_ID}/attributes

La fuente menciona la ruta /categories/{CATEGORY_ID}/attributes, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/categories/{CATEGORY_ID}/attributes`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### GET /items/{ITEM_ID}

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la publicación con `include_attributes=all` para revisar sus identificadores.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `include_attributes` (query, opcional): El ejemplo usa all para incluir todos los atributos.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "attributes",
    "GTIN",
    "variations"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /items

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una publicación con atributos de producto, incluido GTIN cuando corresponda.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "attributes",
    "GTIN"
  ],
  "summary": "Ejemplos de creación con GTIN en atributos."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "validation_error, cause_id 7810 y código item.attribute.missing_conditional_required cuando falta GTIN o EMPTY_GTIN_REASON requerido condicionalmente." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### PUT /items/{ITEM_ID}

**Método:** `PUT`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza atributos de una publicación para agregar o corregir GTIN.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "attributes",
    "GTIN",
    "variations"
  ],
  "summary": "Los ejemplos actualizan GTIN en atributos o variaciones."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "validation_error, cause_id 7810 y código item.attribute.missing_conditional_required cuando falta GTIN o EMPTY_GTIN_REASON requerido condicionalmente." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/identificadores-de-productos](https://developers.mercadolibre.com.co/es_co/identificadores-de-productos)  
**Captura:** 2026-10-08T22:52:02.036Z
