---
id: "producto-sincroniza-modifica-publicaciones"
title: "Sincroniza y modifica publicaciones"
section: "Guía para productos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/producto-sincroniza-modifica-publicaciones"
source_updated_at: "24/03/2026"
captured_at: "2026-10-08T22:52:48.068Z"
sha256: "eaaff276499886b2025c58bb40b64eac16a281f691caefc98e035bc4c3149829"
---

# Sincroniza y modifica publicaciones

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 24/03/2026  
**Captura:** 2026-10-08T22:52:48.068Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/producto-sincroniza-modifica-publicaciones](https://developers.mercadolibre.com.co/es_co/producto-sincroniza-modifica-publicaciones)

## Resumen

Describe cómo sincronizar cambios de publicaciones activas con otros sistemas, actualizar atributos permitidos y gestionar precio, stock, imágenes, descripción, envío y términos de venta. Incluye restricciones por ventas, variantes, promociones y automatización de precios.

## Contenido y conceptos documentados

### Reglas de actualización

- Para cambiar un ítem se usa `PUT /items/$ITEM_ID`; campos editables dependen de su estado. Con ventas no se permite cambiar título, modo de compra ni ciertos métodos de pago; sin ventas (`sold_quantity=0`) sí puede cambiarse el título. El tipo de publicación solo se puede modificar una vez.
- Desde el 18/03/2026, una actualización que solo envía `price` se rechaza con HTTP 400 cuando hay automatización de precios activa; si se envía junto con otros campos, la página indica que se procesa pero el precio se ignora y se devuelve un warning.
- La fuente documenta errores 409 por optimistic locking al actualizar rápidamente; se recomienda esperar unos segundos antes de repetir. También muestra cambio de `MANUFACTURING_TIME` y límites de `PURCHASE_MAX_QUANTITY`.
- La categoría determina los `sale_terms` válidos. Los cuerpos completos y códigos distintos a los ejemplos: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Consultar términos de venta

**Método:** `GET`  
**Ruta:** `/categories/$CATEGORY_ID/sale_terms`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los términos de venta permitidos en la categoría.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- name
- value_type
- value_id
- value_name

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página usa MANUFACTURING_TIME como ejemplo.

### Crear publicación de prueba

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea un ítem de prueba para validar cambios y sincronización.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "site_id",
    "title",
    "category_id",
    "price",
    "currency_id",
    "pictures"
  ]
}
```

**Respuesta**

- id
- seller_id
- category_id
- price
- status

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo para MLA.

### Actualizar publicación

**Método:** `PUT`  
**Ruta:** `/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza campos permitidos de un ítem, incluidas propiedades comerciales y términos de venta.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "title",
    "price",
    "available_quantity",
    "sale_terms",
    "status",
    "condition",
    "attributes"
  ]
}
```

**Respuesta**

- message
- warning

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Actualización solo de price rechazada cuando aplica automatización de precio." } ```
- ```json {   "code": 409,   "meaning": "item optimistic locking error: conflict; esperar antes de repetir." } ```

**Ejemplos**

- La fuente indica que si price se envía junto con otros atributos puede ignorarse y producir warning.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/producto-sincroniza-modifica-publicaciones](https://developers.mercadolibre.com.co/es_co/producto-sincroniza-modifica-publicaciones)  
**Captura:** 2026-10-08T22:52:48.068Z
