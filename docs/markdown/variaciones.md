---
id: "variaciones"
title: "Variaciones"
section: "Guía para productos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/variaciones"
source_updated_at: "30/12/2025"
captured_at: "2026-10-08T22:53:01.331Z"
sha256: "35223088ceb8a334fcbcf3764baadd4cf7026d556c3b1c8373abd7a8e4a1ca05"
---

# Variaciones

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:01.331Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/variaciones](https://developers.mercadolibre.com.co/es_co/variaciones)

## Resumen

Explica cómo reunir variantes de un mismo producto en una publicación y administrar su stock por combinación. El comprador selecciona atributos como color y talle, que aparecen asociados a la orden.

## Contenido y conceptos documentados

- Identifica en la categoría los atributos allow_variations; envíalos en attribute_combinations de todas las variantes. Los atributos variation_attribute describen propiedades particulares. Los requeridos se identifican con required=true.
- La fuente indica un máximo de 100 variantes por categoría y 250 para Moda, Accesorios para celulares y Autopartes. Cada variante requiere price, available_quantity, pictures y attribute_combinations; max_pictures_per_item_var indica el máximo de imágenes. No repitas combinaciones; un atributo ajeno a la categoría puede ser ignorado.
- El SKU de variante debe guardarse en SELLER_SKU dentro de attributes. Para consultar atributos de variantes, agrega include_attributes=all. Al actualizar, envía las variantes a conservar; con ventas solo se pueden sumar atributos. Se permite un atributo personalizado cuando no está definido por la categoría. La fuente recomienda el mismo precio para todas las variantes; si se envían precios distintos, la publicación y el pago consideran el precio más alto.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /orders

La fuente menciona la ruta /orders, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/orders`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Reglas de datos de variaciones

Las combinaciones deben ser válidas para la categoría, iguales en estructura entre variantes y no repetir combinaciones. SELLER_SKU identifica el stock de cada variante; seller_custom_field es distinto. La página indica límites de cantidad por categoría, atributos requeridos, máximo de imágenes configurable y restricciones para variantes vendidas. La fuente recomienda mantener el mismo precio entre variantes y advierte que la VIP y el pago consideran el valor más alto si difieren.

**Errores documentados**

- ```json {   "code": "variation_limit",   "meaning": "La fuente indica 100 variantes por categoría y 250 para Moda, Accesorios para celulares y Autopartes." } ```

**Ejemplos documentados**

- Ejemplos de color, talle, EAN/UPC, voltaje y un atributo personalizado.
## Operaciones de API

### Eliminar variación

**Método:** `DELETE`  
**Ruta:** `/items/{item_id}/variations/{variation_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la variante indicada; también se muestra como alternativa un PUT al ítem conservando solo los IDs deseados.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.
- `variation_id` (path, obligatorio): ID de la variante.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo devuelve información del ítem; no documenta un esquema reducido.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- DELETE /items/MLA599099879/variations/10449631060.

### Consultar atributos de categoría para variaciones

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Comprueba los tags allow_variations y variation_attribute de atributos de una categoría.

**Parámetros**

- `category_id` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de atributos con id, name, tags, value_type y values.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /categories/MLA126186/attributes; COLOR aparece con allow_variations.

### Consultar variaciones dentro del ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta un ítem; attributes=variations permite filtrar la respuesta a esa propiedad.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.
- `attributes` (query): El ejemplo usa variations.
- `include_attributes` (query): La fuente muestra all para incluir attributes de las variantes.

**Solicitud**

No documentado en la fuente.

**Respuesta**

La sección variations puede contener id, attribute_combinations, price, available_quantity, sold_quantity, picture_ids, seller_custom_field y catalog_product_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /items/MLA658778048?attributes=variations; también se documenta include_attributes=all.

### Listar variaciones de un ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}/variations`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve directamente el array de variantes de la publicación.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Array con id, attribute_combinations, price, available_quantity, sold_quantity, picture_ids, seller_custom_field y catalog_product_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /items/MLA658778048/variations.

### Consultar una variación

**Método:** `GET`  
**Ruta:** `/items/{item_id}/variations/{variation_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el detalle de una variante concreta.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.
- `variation_id` (path, obligatorio): ID de la variante.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo incluye id, attribute_combinations, price, available_quantity, sold_quantity, picture_ids y attributes (EAN/UPC).

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /items/MLA658778048/variations/15092589430.

### Crear publicación con variaciones

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea un ítem con variaciones y sus combinaciones de atributos, stock e imágenes.

**Parámetros**

- `category_id` (body): Categoría.
- `site_id` (body): Sitio.
- `title` (body): Título.
- `listing_type_id` (body): Tipo de publicación.
- `variations` (body): Combinaciones de atributos, precio, stock, atributos e imágenes por variante.

**Solicitud**

JSON con listing_type_id, pictures, title, available_quantity, category_id, buying_mode, currency_id, condition, site_id, price y variations. Cada variante incluye attribute_combinations, price, available_quantity, attributes, sold_quantity y picture_ids.

**Respuesta**

Ejemplo de respuesta de publicación con id, site_id, title y sold_quantity.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- POST http://api.mercadolibre.com/items con variantes por color y EAN.

### Agregar variación

**Método:** `POST`  
**Ruta:** `/items/{item_id}/variations`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega una variante con combinación, precio, stock e imágenes. La prosa dice PUT al ítem, pero el ejemplo de solicitud usa POST al recurso /variations.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

JSON de variante: attribute_combinations (id/value_id), price, available_quantity, sold_quantity y picture_ids.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- POST /items/MLA658778048/variations.

### Actualizar variaciones del ítem

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza variantes y atributos enviando la propiedad variations.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

JSON con variations; la fuente muestra id, attribute_combinations, attributes, price y available_quantity. Envíe las variantes a conservar. Con ventas, solo se pueden sumar atributos, no cambiar ni quitar los existentes.

**Respuesta**

Ejemplo devuelve el ítem y su lista variations.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- PUT /items/{item_id} para agregar combinaciones COLOR/VOLTAGE o modificar stock.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/variaciones](https://developers.mercadolibre.com.co/es_co/variaciones)  
**Captura:** 2026-10-08T22:53:01.331Z
