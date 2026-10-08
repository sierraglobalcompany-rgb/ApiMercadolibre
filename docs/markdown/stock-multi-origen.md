---
id: "stock-multi-origen"
title: "Stock multi origen"
section: "Guía para productos"
subsection: "User Products"
url: "https://developers.mercadolibre.com.co/es_co/stock-multi-origen"
source_updated_at: "15/05/2026"
captured_at: "2026-10-08T22:52:50.281Z"
sha256: "7fda97051e172117ff9828b0f6a65db9885dbcca54531af0ebe0e6d722b734a2"
---

# Stock multi origen

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 15/05/2026  
**Captura:** 2026-10-08T22:52:50.281Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/stock-multi-origen](https://developers.mercadolibre.com.co/es_co/stock-multi-origen)

## Resumen

Explica cómo habilitar y gestionar depósitos de vendedor para distribuir el stock entre tiendas y nodos logísticos. El flujo identifica las capacidades del seller, localiza sus tiendas, crea publicaciones con ubicaciones de stock y después consulta/actualiza stock en User Products.

## Contenido y conceptos documentados

### Flujo, campos y restricciones

- Los sellers con `warehouse_management` gestionan un depósito; al sumar `multiwarehouse` pueden gestionar varios. En Brasil la página indica que los depósitos no pueden estar en estados distintos al del CNPJ. La habilitación de usuarios de prueba se solicita mediante un formulario y se procesa periódicamente.
- La búsqueda de tiendas usa el tag `stock_location`; sus resultados incluyen `store_id` y `network_node_id`. La creación envía `stock_locations` y devuelve `user_product_id`; luego se usa la API de stock de UP.
- La actualización de stock requiere el encabezado `x-version` obtenido al consultar. La fuente enumera errores 400 por ausencia de `stock_locations`, tienda inexistente/ajena/no configurada, `available_quantity` inválido, ausencia de `x-version` y configuración de depósito único con nodos múltiples; 409 corresponde a mismatch de versión.
- Las llamadas muestran Bearer. Los cuerpos completos y códigos no listados aquí: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /user-product

La fuente menciona la ruta /user-product, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/user-product`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /stock/

La fuente menciona la ruta /stock/, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/stock/`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar stock de User Product

**Método:** `GET`  
**Ruta:** `/user-products/$USER_PRODUCT_ID/stock`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene stock distribuido para la publicación y el header de versión.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- locations[].type
- locations[].quantity
- locations[].store_id
- locations[].network_node_id

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La respuesta incluye x-version.

### Consultar tags del vendedor

**Método:** `GET`  
**Ruta:** `/users/$USER_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene tags para identificar habilitación warehouse_management/multiwarehouse.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- nickname
- tags

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Tags determinan si se admite depósito único o múltiples.

### Buscar tiendas del vendedor

**Método:** `GET`  
**Ruta:** `/users/$USER_ID/stores/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca tiendas configuradas como stock_location.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `tags` (query, obligatorio): stock_location.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- paging
- results[].store_id
- results[].network_node_id
- results[].address_id
- results[].location

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Crear ítem multi-origen

**Método:** `POST`  
**Ruta:** `/items/multiwarehouse`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una publicación asociada a ubicaciones de stock del vendedor.

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
    "listing_type_id",
    "stock_locations[].store_id",
    "stock_locations[].network_node_id",
    "stock_locations[].quantity"
  ]
}
```

**Respuesta**

- id
- user_product_id
- stock_locations

**Errores documentados**

- ```json {   "code": 400,   "meaning": "stock_locations ausente, tienda inexistente/ajena o available_quantity no permitido para el seller." } ```

**Ejemplos**

- La fuente presenta estado 201 para éxito.

### Actualizar stock de warehouse

**Método:** `PUT`  
**Ruta:** `/user-products/$USER_PRODUCT_ID/stock/type/seller_warehouse`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza inventario por ubicación con control optimista de versión.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)
- `x-version` (header, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "locations[].store_id",
    "locations[].network_node_id",
    "locations[].quantity"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Missing X-Version header; seller de depósito único no puede enviar varios network_node_id; store ajeno/inexistente/no configurado o vacío." } ```
- ```json {   "code": 409,   "meaning": "Version mismatch; volver a consultar el stock y usar x-version actual." } ```

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/stock-multi-origen](https://developers.mercadolibre.com.co/es_co/stock-multi-origen)  
**Captura:** 2026-10-08T22:52:50.281Z
