---
id: "items-y-busquedas"
title: "Ítems y Búsquedas"
section: "Recursos de la API"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/items-y-busquedas"
source_updated_at: "10/09/2026"
captured_at: "2026-10-08T22:53:49.815Z"
sha256: "f8f0cd709dde113809ec5af2226bef7ea9c873a3a5aa04fe56995fc1fe19a654"
---

# Ítems y Búsquedas

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 10/09/2026  
**Captura:** 2026-10-08T22:53:49.815Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/items-y-busquedas](https://developers.mercadolibre.com.co/es_co/items-y-busquedas)

## Resumen

La página reúne búsquedas de publicaciones por sitio y por cuenta de vendedor, filtros y ordenamientos, consulta múltiple de ítems/usuarios y recorridos de más de 1.000 resultados. Distingue los ítems activos de los listados del sitio frente al inventario publicado en la cuenta del vendedor. Las consultas usan ejemplos con `Authorization: Bearer`; los multiget legacy están en migración a endpoints bulk.

## Contenido y conceptos documentados

- **Búsqueda por sitio y por vendedor:** `/sites/{site_id}/search` consulta publicaciones activas de los listados; `/users/{user_id}/items/search` obtiene las publicaciones de la cuenta. La primera admite filtros y `sort`; la segunda puede buscar por `sku` (`seller_custom_field`), `seller_sku`, estado, identificador de producto y tipo de publicación. La fuente desaconseja sustituir las notificaciones de ítems por búsquedas periódicas.
- **Exposición y restricciones:** `reputation_health_gauge` admite `unhealthy`, `warning` y `healthy` en México, Chile y Brasil. Vendedores con más de 200.000 ítems pueden tener `aggregations_allowed=false` y no recibir `filters`/`available_filters`; `include_filters=true` puede producir HTTP 206 en ese caso, mientras que sin el parámetro se documenta HTTP 200.
- **Recorridos grandes:** para superar 1.000 ítems o preguntas se usa `search_type=scan` (en preguntas, `searchtype=scan`) y se omite `offset`. El `scroll_id` se renueva por llamada, vence en cinco minutos y el recorrido termina cuando devuelve `null`; el ejemplo de ítems indica `limit` predeterminado de 50 y máximo de 100.
- **Multiget y migración:** las consultas legacy `/items?ids=` y `/users?ids=` aceptan hasta 20 resultados y responden en formato verbose (`code` y `body`). La página pide migrar antes del 25/10/2026 a `/items/bulk?ids=` y `/users/bulk?ids=`. En `/items/bulk`, el código pasa a `status_code`, se agrega `id` en la raíz y los atributos se seleccionan con prefijo `body.`; el método HTTP de estos reemplazos no se indica en esta página.
- **Cantidad disponible:** `available_quantity` en recursos públicos es referencial. La página mapea los rangos `RANGO_1_50`, `RANGO_51_100`, `RANGO_101_150`, `RANGO_151_200`, `RANGO_201_250`, `RANGO_251_500`, `RANGO_501_5000`, `RANGO_5001_50000` y `RANGO_50001_99999` a 1, 50, 100, 150, 200, 250, 500, 5.000 y 50.000, respectivamente.
- **Errores:** para multiget la fuente sugiere revisar 401 y 403, pero su significado es No documentado en la fuente. Otros parámetros, autenticación adicional y límites fuera de los descritos: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Disponibilidad pública referencial de available_quantity

En los recursos públicos de Ítems y Búsquedas, available_quantity se entrega como una referencia por rangos, no como cantidad exacta.

**Respuesta**

```json
{
  "field": "available_quantity",
  "reference_ranges": {
    "RANGO_1_50": 1,
    "RANGO_51_100": 50,
    "RANGO_101_150": 100,
    "RANGO_151_200": 150,
    "RANGO_201_250": 200,
    "RANGO_251_500": 250,
    "RANGO_501_5000": 500,
    "RANGO_5001_50000": 5000,
    "RANGO_50001_99999": 50000
  }
}
```
### Migración de multiget a bulk

Los endpoints legacy /items?ids= y /users?ids= conviven temporalmente con /items/bulk?ids= y /users/bulk?ids=. La fuente pide migrar antes del 25/10/2026 y señala que desde octubre de 2026 deben usarse los endpoints bulk. En /items/bulk, code pasa a status_code, id queda en el nivel raíz y attributes requiere prefijos body.; no documenta aquí el método HTTP de los reemplazos.

**Respuesta**

```json
{
  "legacy_to_replacement": {
    "/items?ids={ITEM_ID1},{ITEM_ID2}": "/items/bulk?ids={ITEM_ID1},{ITEM_ID2}",
    "/users?ids={USER_ID1},{USER_ID2}": "/users/bulk?ids={USER_ID1},{USER_ID2}"
  },
  "items_bulk_changes": [
    "code pasa a status_code",
    "id aparece en el nivel raíz",
    "los atributos seleccionados usan prefijo body."
  ],
  "migration_deadline": "25/10/2026"
}
```

**Ejemplos documentados**

- Método HTTP del reemplazo: No documentado en esta página.
### Ruta mencionada /items/bulk

La fuente menciona la ruta /items/bulk, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/items/bulk`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /sites/SITEID/search

La fuente menciona la ruta /sites/SITEID/search, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/sites/SITEID/search`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /users/bulk

La fuente menciona la ruta /users/bulk, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/users/bulk`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consulta múltiple de ítems (multiget legado)

**Método:** `GET`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene hasta 20 ítems en una llamada y devuelve una entrada verbose por cada consulta; este endpoint está en proceso de deprecación y la fuente indica migrar a /items/bulk.

**Parámetros**

- `ids` (query, obligatorio): Lista de IDs de ítems; la fuente documenta máximo 20 resultados por llamada.
- `attributes` (query, opcional): Selecciona atributos de ítems; el ejemplo usa id, price, category_id y title. La variante con attributes está deprecada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "shape": "Lista de resultados verbose, con code y body por ítem.",
  "sample_body_fields": [
    "id",
    "site_id",
    "title",
    "seller_id",
    "category_id",
    "price",
    "currency_id",
    "initial_quantity",
    "available_quantity",
    "sale_terms",
    "date_created",
    "last_updated",
    "health"
  ]
}
```

**Errores documentados**

- ```json {   "code": 401,   "meaning": "La fuente menciona revisar este código, pero no documenta su significado." } ```
- ```json {   "code": 403,   "meaning": "La fuente menciona revisar este código, pero no documenta su significado." } ```

**Ejemplos**

- GET /items?ids=MLA599260060,MLA594239600
- GET /items?ids=MLA599260060,MLA594239600&attributes=id,price,category_id,title

### Búsqueda de preguntas mediante scan

**Método:** `GET`  
**Ruta:** `/questions/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Permite recorrer preguntas de un ítem cuando se necesitan más de 1.000 registros; usa scan y paginación con scroll_id.

**Parámetros**

- `searchtype` (query, obligatorio): Usar scan para búsqueda de más de 1.000 preguntas.
- `item` (query, obligatorio): ID del ítem cuyas preguntas se consultan.
- `scroll_id` (query, opcional): Token de continuación: actualizar en cada llamada; expira en 5 minutos.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "documented_fields": [
    "scroll_id"
  ],
  "notes": [
    "La consulta se repite con el scroll_id actualizado hasta que la respuesta indique null."
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /questions/search?searchtype=scan&item=ITEM_ID

### Búsqueda de publicaciones del sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca publicaciones activas de los listados por vendedor o nickname; admite categoría, filtros y ordenamiento.

**Parámetros**

- `site_id` (path, obligatorio): Identificador del sitio.
- `seller_id` (query, opcional): ID del vendedor; ejemplo seller_id=$SELLER_ID.
- `nickname` (query, opcional): Nickname del vendedor.
- `category` (query, opcional): ID de categoría para acotar los resultados del vendedor.
- `shipping_cost` (query, opcional): El ejemplo usa free para filtrar publicaciones con envío gratis.
- `sort` (query, opcional): Orden disponible; ejemplo price_asc. La fuente indica que por defecto se usa relevancia.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "documented_fields": [
    "available_sorts",
    "available_filters"
  ],
  "notes": [
    "La fuente describe resultados de ítems activos de los listados."
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/SITE_ID/search?seller_id=$SELLER_ID
- GET /sites/SITE_ID/search?nickname=$NICKNAME&sort=price_asc
- GET /sites/SITE_ID/search?seller_id=$SELLER_ID&shipping_cost=free

### Consulta múltiple de usuarios (multiget legado)

**Método:** `GET`  
**Ruta:** `/users`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene hasta 20 usuarios en una llamada y devuelve una entrada verbose por usuario; la documentación indica migrar al reemplazo bulk.

**Parámetros**

- `ids` (query, obligatorio): Lista de IDs de usuarios; máximo documentado de 20 resultados por llamada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "shape": "Lista de resultados verbose, con code y body por usuario.",
  "sample_body_fields": [
    "id",
    "nickname",
    "registration_date",
    "country_id",
    "address",
    "user_type",
    "tags",
    "logo",
    "points",
    "site_id",
    "permalink",
    "seller_reputation",
    "buyer_reputation",
    "status"
  ]
}
```

**Errores documentados**

- ```json {   "code": 401,   "meaning": "La fuente menciona revisar este código, pero no documenta su significado." } ```
- ```json {   "code": 403,   "meaning": "La fuente menciona revisar este código, pero no documenta su significado." } ```

**Ejemplos**

- GET /users?ids=401114259,287440999

### Búsqueda de publicaciones de un vendedor

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta las publicaciones de la cuenta del vendedor, con filtros por SKU, estado, salud de exposición y producto; permite recuperar lotes grandes con scan.

**Parámetros**

- `user_id` (path, obligatorio): ID del vendedor.
- `reputation_health_gauge` (query, opcional): Valores documentados: unhealthy, warning y healthy. La funcionalidad se indica para México, Chile y Brasil.
- `sku` (query, opcional): Busca por el campo seller_custom_field.
- `seller_sku` (query, opcional): Busca por el atributo SELLER_SKU.
- `status` (query, opcional): Filtra por estado; el ejemplo usa active.
- `missing_product_identifiers` (query, opcional): true busca publicaciones sin identificador de producto; false las que sí lo tienen o están enviándolo.
- `include_filters` (query, opcional): Con true incluye filters y available_filters, ausentes por defecto para reducir el tiempo de respuesta.
- `orders` (query, opcional): ID de ordenamiento disponible; ejemplo start_time_desc.
- `listing_type_id` (query, opcional): Filtro de tipo de publicación; ejemplo gold_pro.
- `search_type` (query, opcional): Usar scan para búsquedas superiores a 1.000 registros; se omite offset.
- `scroll_id` (query, opcional): Token devuelto por scan; debe actualizarse en cada llamada y expira en 5 minutos.
- `limit` (query, opcional): En scan se devuelven 50 por defecto y se documenta un máximo de 100.
- `offset` (query, opcional): La fuente indica quitarlo al consultar con search_type=scan.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "documented_fields": [
    "seller_id",
    "query",
    "paging.limit",
    "paging.offset",
    "paging.total",
    "results",
    "orders",
    "available_orders"
  ],
  "conditional_fields": [
    "filters",
    "available_filters (al enviar include_filters=true)"
  ],
  "notes": [
    "Los resultados son IDs de publicaciones. La fuente incluye ejemplos de available_filters por estado, tipo de publicación, envío y otros."
  ],
  "status_codes": [
    200,
    206
  ],
  "status_notes": [
    "Para vendedores restringidos, include_filters=true produce HTTP 206; sin ese parámetro se documenta HTTP 200."
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/USER_ID/items/search?sku=$SELLER_CUSTOM_FIELD
- GET /users/USER_ID/items/search?seller_sku=$SELLER_SKU
- GET /users/USER_ID/items/search?missing_product_identifiers=true
- GET /users/USER_ID/items/search?search_type=scan

### Restricciones de búsqueda del vendedor

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items/search/restrictions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta si las agregaciones, consultas y ordenamientos están habilitados para el vendedor; la restricción por más de 200.000 publicaciones afecta los filtros de búsqueda.

**Parámetros**

- `user_id` (path, obligatorio): ID del vendedor.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": {
    "aggregations_allowed": "Indica si se permiten agregaciones; false se asocia a vendedores con más de 200.000 ítems.",
    "query_allowed": "Indica si la consulta está permitida.",
    "sort_allowed": "Indica si el ordenamiento está permitido."
  }
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/USER_ID/items/search/restrictions
- Ejemplo de respuesta: aggregations_allowed=false, query_allowed=true, sort_allowed=true

**Fuente:** [https://developers.mercadolibre.com.co/es_co/items-y-busquedas](https://developers.mercadolibre.com.co/es_co/items-y-busquedas)  
**Captura:** 2026-10-08T22:53:49.815Z
