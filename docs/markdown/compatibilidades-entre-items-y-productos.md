---
id: "compatibilidades-entre-items-y-productos"
title: "Compatibilidades entre ítems y productos de Autopartes"
section: "Guía para productos"
subsection: "Categorización"
url: "https://developers.mercadolibre.com.co/es_co/compatibilidades-entre-items-y-productos"
source_updated_at: "14/07/2026"
captured_at: "2026-10-08T22:51:21.176Z"
sha256: "0bbcef30fefac8e8ee6761d378d2cdef41ddc5a7daa34d42f9ec8b3b23ab95ff"
---

# Compatibilidades entre ítems y productos de Autopartes

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 14/07/2026  
**Captura:** 2026-10-08T22:51:21.176Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/compatibilidades-entre-items-y-productos](https://developers.mercadolibre.com.co/es_co/compatibilidades-entre-items-y-productos)

## Resumen

Reúne las operaciones para buscar, consultar, agregar, copiar y eliminar compatibilidades entre ítems/User Products y productos de autopartes. Distingue compatibilidades del vendedor (`SELLER`) de las generadas por catálogo (`CATALOGO`), con restricciones específicas de lectura y escritura para cada origen.

## Contenido y conceptos documentados

- Las compatibilidades pueden incluir dominios, productos, notas y restricciones de posición. `source` diferencia `SELLER` y `CATALOGO`; `restrictions_required` indica si se deben informar posiciones.
- La lectura extendida expone información adicional. Para compatibilidades de catálogo, el detalle por ID no está disponible y la fuente indica que `id` y `catalog_product_id` pueden ser `null`.
- DELETE solo permite eliminar compatibilidades `SELLER`; las de catálogo se gestionan desde Mercado Libre. Desde el 15/07/2026, copiar y pegar desde User Product excluye compatibilidades `CATALOGO`.
- Las operaciones POST/PUT pueden guardar hasta 200 compatibilidades sincrónicamente y procesar el resto de forma asíncrona. Una compatibilidad universal no admite enviar simultáneamente productos/familias.
- La fuente informa límites de 100 RPM por APP_ID para el conteo de productos por familia. Errores de compatibilidad incluyen 400 por validación/formato, 403 por token/permisos y 404 por ítem, compatibilidad, producto o dominio inexistente. Para snapshots: 400 orden no encontrada, 401 token inválido y 403 orden sin reclamo o seller distinto.
- También se documentan excepciones de compatibilidad, conteo de sugerencias/reclamos, snapshots de compatibilidad de órdenes y búsqueda de vehículos agregados al catálogo.

**Campos y respuestas:** `source`, `id`, `catalog_product_id`, `restrictions_required`, `extended_information`, `item_to_copy`, `note`, `restrictions`, `created_compatibilities_count`, `reason_id`, `compatibilities_count`, `compatibilities_claims_count`, `notes_count`, `restrictions_count` y filtros `tags`.

**Ejemplos documentados:** consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

## Operaciones de API

## Conceptos y recursos asociados

### Compatibilidades entre ítems y productos de Autopartes

Reúne las operaciones para buscar, consultar, agregar, copiar y eliminar compatibilidades entre ítems/User Products y productos de autopartes. Distingue compatibilidades del vendedor (`SELLER`) de las generadas por catálogo (`CATALOGO`), con restricciones específicas de lectura y escritura para cada origen.

**Respuesta**

```json
{
  "fields": "`source`, `id`, `catalog_product_id`, `restrictions_required`, `extended_information`, `item_to_copy`, `note`, `restrictions`, `created_compatibilities_count`, `reason_id`, `compatibilities_count`, `compatibilities_claims_count`, `notes_count`, `restrictions_count` y filtros `tags`."
}
```

**Errores documentados**

- 400: validaciones de consistencia/formato y límites.
- 401: token inválido para consulta de snapshot.
- 403: token/permisos, orden sin claim o seller distinto.
- 404: ítem, producto, dominio o compatibilidad inexistente.

**Ejemplos documentados**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.
## Operaciones de API

### Elimina compatibilidades SELLER del ítem

**Método:** `DELETE`  
**Ruta:** `/items/{item_id}/compatibilities`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina compatibilidades SELLER del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `extended` (query): La lectura extendida incluye información adicional.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Elimina una compatibilidad SELLER por ID

**Método:** `DELETE`  
**Ruta:** `/items/{item_id}/compatibilities/{compatibility_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina una compatibilidad SELLER por ID.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `compatibility_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Elimina compatibilidades del User Product

**Método:** `DELETE`  
**Ruta:** `/user-products/{up_id}/compatibilities`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina compatibilidades del User Product.

**Parámetros**

- `up_id` (path, obligatorio): Variable de ruta documentada.
- `main_domain_id` (query): Dominio principal de compatibilidad.
- `extended` (query): La lectura extendida incluye información adicional.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Busca productos/vehículos nuevos añadidos al catálogo por `categoryId`

**Método:** `GET`  
**Ruta:** `/catalog_compatibilities/products_search/new`  
**Autenticación:** No documentado en la fuente.

Busca productos/vehículos nuevos añadidos al catálogo por `categoryId`.

**Parámetros**

- `categoryId` (query): Categoría de catálogo.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Obtiene valores de restricciones para dominios principal y secundario

**Método:** `GET`  
**Ruta:** `/catalog_compatibilities/restrictions/values`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene valores de restricciones para dominios principal y secundario.

**Parámetros**

- `main_domain_id` (query): Dominio principal de compatibilidad.
- `secondary_domain_id` (query): Dominio secundario de compatibilidad.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Descarga compatibilidades de catálogo por sitio

**Método:** `GET`  
**Ruta:** `/catalog/dumps/domains/{site_id}/compatibilities`  
**Autenticación:** No documentado en la fuente.

Descarga compatibilidades de catálogo por sitio.

**Parámetros**

- `site_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Consulta el vehículo elegido por el comprador para una orden

**Método:** `GET`  
**Ruta:** `/compats-snapshots/orders/{order_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el vehículo elegido por el comprador para una orden.

**Parámetros**

- `order_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: snapshot no encontrado para la orden.
- 401: token inválido.
- 403: la orden no tiene claim o el caller no es el seller de la publicación.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Consulta datos del ítem usados por el flujo de compatibilidades

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta datos del ítem usados por el flujo de compatibilidades.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Lista compatibilidades; admite `extended=true`

**Método:** `GET`  
**Ruta:** `/items/{item_id}/compatibilities`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista compatibilidades; admite `extended=true`.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `extended` (query): La lectura extendida incluye información adicional.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Consulta detalle por ID, sujeto a las limitaciones de origen de catálogo

**Método:** `GET`  
**Ruta:** `/items/{item_id}/compatibilities/{compatibility_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalle por ID, sujeto a las limitaciones de origen de catálogo.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `compatibility_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Consulta la nota de una compatibilidad

**Método:** `GET`  
**Ruta:** `/items/{item_id}/compatibilities/{compatibility_id}/note`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la nota de una compatibilidad.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `compatibility_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Consulta la excepción del ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}/compatibilities/exception`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la excepción del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Lista compatibilidades; admite `main_domain_id` y `extended=true`

**Método:** `GET`  
**Ruta:** `/user-products/{up_id}/compatibilities`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista compatibilidades; admite `main_domain_id` y `extended=true`.

**Parámetros**

- `up_id` (path, obligatorio): Variable de ruta documentada.
- `main_domain_id` (query): Dominio principal de compatibilidad.
- `extended` (query): La lectura extendida incluye información adicional.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Consulta la excepción del User Product

**Método:** `GET`  
**Ruta:** `/user-products/{user_product_id}/compatibilities/exception`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la excepción del User Product.

**Parámetros**

- `user_product_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Busca publicaciones por `tags` o por estado y presencia de compatibilidades

**Método:** `GET`  
**Ruta:** `/users/{seller_id}/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca publicaciones por `tags` o por estado y presencia de compatibilidades.

**Parámetros**

- `seller_id` (path, obligatorio): Variable de ruta documentada.
- `tags` (query): Filtro por tipo/estado de compatibilidad.
- `status` (query): Estado de publicación.
- `has_compatibilities` (query): Filtra publicaciones con compatibilidades.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Busca reclamos por incompatibilidad mediante `reason_id`

**Método:** `GET`  
**Ruta:** `/v1/claims/search`  
**Autenticación:** No documentado en la fuente.

Busca reclamos por incompatibilidad mediante `reason_id`.

**Parámetros**

- `reason_id` (query): Identificador de motivo de reclamo.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Cuenta productos de una familia que cumplen atributos

**Método:** `POST`  
**Ruta:** `/catalog_compatibilities/products_search/count_family_products`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta productos de una familia que cumplen atributos.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Consulta/genera tarjetas de compatibilidades para el dominio

**Método:** `POST`  
**Ruta:** `/items/catalog_domains/{domain_id}/compatibilities/cards`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta/genera tarjetas de compatibilidades para el dominio.

**Parámetros**

- `domain_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

```json
{
  "fields": [
    "item_id",
    "filters",
    "product_id (opcional)"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "title",
    "subtitle",
    "filter",
    "quantity"
  ]
}
```

**Errores documentados**

- 400: validaciones de consistencia.
- 403: token/permisos.
- 404: ítem/producto/dominio inexistente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Obtiene resumen de sugerencias/reclamos de compatibilidad

**Método:** `POST`  
**Ruta:** `/items/compatibilities_summary`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene resumen de sugerencias/reclamos de compatibilidad.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "domain_id",
    "items"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "item_id",
    "item_title",
    "compatibilities_count",
    "compatibilities_claims_count",
    "notes_count",
    "restrictions_count"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Agrega compatibilidades a un ítem

**Método:** `POST`  
**Ruta:** `/items/{item_id}/compatibilities`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega compatibilidades a un ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `extended` (query): La lectura extendida incluye información adicional.

**Solicitud**

```json
{
  "fields": [
    "compatibilities, item_to_copy, extended_information, note, restrictions"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Registra una excepción para el ítem

**Método:** `POST`  
**Ruta:** `/items/{item_id}/compatibilities/exception`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Registra una excepción para el ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

```json
{
  "fields": [
    "comment"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Agrega compatibilidades a un User Product

**Método:** `POST`  
**Ruta:** `/user-products/{up_id}/compatibilities`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega compatibilidades a un User Product.

**Parámetros**

- `up_id` (path, obligatorio): Variable de ruta documentada.
- `main_domain_id` (query): Dominio principal de compatibilidad.
- `extended` (query): La lectura extendida incluye información adicional.

**Solicitud**

```json
{
  "fields": [
    "compatibilities, item_to_copy, extended_information, note, restrictions"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Copia compatibilidades entre User Products/ítems

**Método:** `POST`  
**Ruta:** `/user-products/{up_id}/compatibilities/copy-paste`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Copia compatibilidades entre User Products/ítems.

**Parámetros**

- `up_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

```json
{
  "fields": [
    "item_to_copy, extended_information"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Registra una excepción para el User Product

**Método:** `POST`  
**Ruta:** `/user-products/{user_product_id}/compatibilities/exception`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Registra una excepción para el User Product.

**Parámetros**

- `user_product_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

```json
{
  "fields": [
    "comment"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Crea, actualiza o elimina entradas; la acción debe indicarse explícitamente

**Método:** `PUT`  
**Ruta:** `/items/{item_id}/compatibilities`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea, actualiza o elimina entradas; la acción debe indicarse explícitamente.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `extended` (query): La lectura extendida incluye información adicional.

**Solicitud**

```json
{
  "fields": [
    "create/update/delete, item_to_copy, extended_information, note, restrictions"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Actualiza compatibilidades de un User Product

**Método:** `PUT`  
**Ruta:** `/user-products/{up_id}/compatibilities`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza compatibilidades de un User Product.

**Parámetros**

- `up_id` (path, obligatorio): Variable de ruta documentada.
- `main_domain_id` (query): Dominio principal de compatibilidad.
- `extended` (query): La lectura extendida incluye información adicional.

**Solicitud**

```json
{
  "fields": [
    "item_to_copy, extended_information, note, restrictions"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Referencia HTTP POST /catalog_domains/MLB-CARS_AND_VANS/compatibilities/cards

**Método:** `POST`  
**Ruta:** `/catalog_domains/MLB-CARS_AND_VANS/compatibilities/cards`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /catalog_domains/MLB-CARS_AND_VANS/compatibilities/cards. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/compatibilidades-entre-items-y-productos](https://developers.mercadolibre.com.co/es_co/compatibilidades-entre-items-y-productos)  
**Captura:** 2026-10-08T22:51:21.176Z
