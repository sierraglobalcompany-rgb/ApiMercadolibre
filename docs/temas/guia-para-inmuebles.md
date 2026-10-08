# Guía para inmuebles

26 páginas del portal oficial en esta área.

## [Actualiza tus publicaciones](../markdown/actualiza-tus-publicaciones.md)

Actualización indicada por la fuente: 28/08/2026. Captura: 2026-10-08T22:50:16.377Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/actualiza-tus-publicaciones](https://developers.mercadolibre.com.co/es_co/actualiza-tus-publicaciones)

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

---

## [Actualización variación inmuebles](../markdown/actualizacion-variacion-inmuebles.md)

Actualización indicada por la fuente: 08/11/2025. Captura: 2026-10-08T22:50:26.803Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/actualizacion-variacion-inmuebles](https://developers.mercadolibre.com.co/es_co/actualizacion-variacion-inmuebles)

# Actualización variación inmuebles

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 08/11/2025  
**Captura:** 2026-10-08T22:50:26.803Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/actualizacion-variacion-inmuebles](https://developers.mercadolibre.com.co/es_co/actualizacion-variacion-inmuebles)

## Resumen

Explica cómo agregar, actualizar y eliminar variaciones de una publicación.

## Contenido y conceptos documentados

- attribute_combinations describe la variante; las actualizaciones usan el ID de la variación, precio e inventario.

## Operaciones de API

## Conceptos y recursos asociados

### Actualización variación inmuebles

Explica cómo agregar, actualizar y eliminar variaciones de una publicación.
## Operaciones de API

### Agregar variación

**Método:** `POST`  
**Ruta:** `/items/{item_id}/variations`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega combinación de atributos, precio e inventario.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "attribute_combinations[]",
    "price",
    "available_quantity",
    "sold_quantity"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "variación creada; HTTP 201"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Eliminar variación

**Método:** `DELETE`  
**Ruta:** `/items/{item_id}/variations/{variation_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la variación por ID.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta
- `variation_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "variaciones restantes; HTTP 200"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Actualizar variaciones

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza variaciones identificadas por id.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "variations[].id",
    "available_quantity",
    "price"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "ítem actualizado; HTTP 200"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/actualizacion-variacion-inmuebles](https://developers.mercadolibre.com.co/es_co/actualizacion-variacion-inmuebles)  
**Captura:** 2026-10-08T22:50:26.803Z

---

## [Atributos](../markdown/atributos-inmuebles.md)

Actualización indicada por la fuente: 24/11/2025. Captura: 2026-10-08T22:50:27.959Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/atributos-inmuebles](https://developers.mercadolibre.com.co/es_co/atributos-inmuebles)

# Atributos

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 24/11/2025  
**Captura:** 2026-10-08T22:50:27.959Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/atributos-inmuebles](https://developers.mercadolibre.com.co/es_co/atributos-inmuebles)

## Resumen

Explica cómo consultar atributos por categoría e identificar campos obligatorios.

## Contenido y conceptos documentados

- tags.required=true señala atributos requeridos; se muestran COVERED_AREA, BEDROOMS, MAINTENANCE_FEE y PARKING_LOTS.

## Operaciones de API

## Conceptos y recursos asociados

### Atributos

Explica cómo consultar atributos por categoría e identificar campos obligatorios.
## Operaciones de API

### Consultar atributos

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve atributos y etiquetas de obligatoriedad.

**Parámetros**

- `category_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "name",
    "tags.required",
    "hierarchy",
    "relevance",
    "value_type",
    "value_max_length",
    "allowed_units",
    "default_unit",
    "attribute_group_id",
    "attribute_group_name"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Crear publicación inmobiliaria

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La guía exige enviar pictures en la creación para los tipos indicados.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "category_id",
    "pictures[].source",
    "attributes"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Enviar descripción inmobiliaria

**Método:** `POST`  
**Ruta:** `/items/{item_id}/description`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Añade descripción en texto plano.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "plain_text"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- {"plain_text":"Descripción con texto plano"}

**Fuente:** [https://developers.mercadolibre.com.co/es_co/atributos-inmuebles](https://developers.mercadolibre.com.co/es_co/atributos-inmuebles)  
**Captura:** 2026-10-08T22:50:27.959Z

---

## [Calidad de las Publicaciones](../markdown/calidad-de-las-publicaciones-inmuebles.md)

Actualización indicada por la fuente: 19/06/2026. Captura: 2026-10-08T22:50:29.141Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/calidad-de-las-publicaciones-inmuebles](https://developers.mercadolibre.com.co/es_co/calidad-de-las-publicaciones-inmuebles)

# Calidad de las Publicaciones

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 19/06/2026  
**Captura:** 2026-10-08T22:50:29.141Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/calidad-de-las-publicaciones-inmuebles](https://developers.mercadolibre.com.co/es_co/calidad-de-las-publicaciones-inmuebles)

## Resumen

Explica consultas de nivel, puntuación y acciones pendientes para mejorar calidad.

## Contenido y conceptos documentados

- Los objetivos incluyen fotos, especificaciones, video y tipo de publicación; los mínimos de fotos varían por inmueble.

## Operaciones de API

## Conceptos y recursos asociados

### Calidad de las Publicaciones

Explica consultas de nivel, puntuación y acciones pendientes para mejorar calidad.
## Operaciones de API

### Consultar calidad del ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}/health`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Retorna puntaje, nivel, objetivos y progreso.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "item_id",
    "health",
    "level",
    "goals[].id",
    "goals[].name",
    "apply",
    "progress",
    "progress_max",
    "data",
    "completed"
  ]
}
```

**Errores documentados**

- ```json {   "code": "health is not supported for this item",   "meaning": "No soportado para desarrollo, inactivo o con tags de penalización." } ```

**Ejemplos**

No documentado en la fuente.

### Consultar acciones pendientes

**Método:** `GET`  
**Ruta:** `/items/{item_id}/health/actions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Retorna acciones aplicables para mejorar calidad.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "item_id",
    "health",
    "actions[].id",
    "actions[].name"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar rangos de calidad

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/health_levels`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista niveles y rangos.

**Parámetros**

- `site_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "level",
    "health_min",
    "health_max"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/calidad-de-las-publicaciones-inmuebles](https://developers.mercadolibre.com.co/es_co/calidad-de-las-publicaciones-inmuebles)  
**Captura:** 2026-10-08T22:50:29.141Z

---

## [Categorías](../markdown/categorias-inmuebles.md)

Actualización indicada por la fuente: 06/11/2025. Captura: 2026-10-08T22:50:30.263Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/categorias-inmuebles](https://developers.mercadolibre.com.co/es_co/categorias-inmuebles)

# Categorías

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 06/11/2025  
**Captura:** 2026-10-08T22:50:30.263Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/categorias-inmuebles](https://developers.mercadolibre.com.co/es_co/categorias-inmuebles)

## Resumen

Describe el recorrido del árbol de categorías desde sitio hasta el subtipo final.

## Contenido y conceptos documentados

- La selección usa PROPERTY_TYPE, OPERATION y OPERATION_SUBTYPE.

## Operaciones de API

## Conceptos y recursos asociados

### Categorías

Describe el recorrido del árbol de categorías desde sitio hasta el subtipo final.
### Ruta mencionada /categories/${ID}

La fuente menciona la ruta /categories/${ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/categories/${ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve detalle y subcategorías.

**Parámetros**

- `category_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "name",
    "children_categories",
    "settings",
    "currencies",
    "max_pictures_per_item",
    "status"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Listar categorías del sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/categories`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista categorías disponibles.

**Parámetros**

- `site_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "name"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/categorias-inmuebles](https://developers.mercadolibre.com.co/es_co/categorias-inmuebles)  
**Captura:** 2026-10-08T22:50:30.263Z

---

## [Categorías y atributos](../markdown/categorias-atributos-inmuebles.md)

Actualización indicada por la fuente: 06/11/2025. Captura: 2026-10-08T22:50:31.245Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/categorias-atributos-inmuebles](https://developers.mercadolibre.com.co/es_co/categorias-atributos-inmuebles)

# Categorías y atributos

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 06/11/2025  
**Captura:** 2026-10-08T22:50:31.245Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/categorias-atributos-inmuebles](https://developers.mercadolibre.com.co/es_co/categorias-atributos-inmuebles)

## Resumen

Introduce el árbol de categorías de clasificados y su variación por sitio.

## Contenido y conceptos documentados

- Antes de publicar se escoge category_id específico del sitio y tipo de inmueble.

## Operaciones de API

## Conceptos y recursos asociados

### Categorías y atributos

Introduce el árbol de categorías de clasificados y su variación por sitio.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/categorias-atributos-inmuebles](https://developers.mercadolibre.com.co/es_co/categorias-atributos-inmuebles)  
**Captura:** 2026-10-08T22:50:31.245Z

---

## [Ciclo de vida de las publicaciones de Inmuebles](../markdown/ciclo-de-vida-de-las-publicaciones-de-inmuebles.md)

Actualización indicada por la fuente: 08/11/2025. Captura: 2026-10-08T22:50:32.256Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/ciclo-de-vida-de-las-publicaciones-de-inmuebles](https://developers.mercadolibre.com.co/es_co/ciclo-de-vida-de-las-publicaciones-de-inmuebles)

# Ciclo de vida de las publicaciones de Inmuebles

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 08/11/2025  
**Captura:** 2026-10-08T22:50:32.256Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/ciclo-de-vida-de-las-publicaciones-de-inmuebles](https://developers.mercadolibre.com.co/es_co/ciclo-de-vida-de-las-publicaciones-de-inmuebles)

## Resumen

Explica vigencia según sitio, categoría y operación, campos temporales y estados.

## Contenido y conceptos documentados

- stop_time marca el fin del ciclo; un ítem puede pasar a closed/expired aunque el paquete siga activo.

## Operaciones de API

## Conceptos y recursos asociados

### Ciclo de vida de las publicaciones de Inmuebles

Explica vigencia según sitio, categoría y operación, campos temporales y estados.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/ciclo-de-vida-de-las-publicaciones-de-inmuebles](https://developers.mercadolibre.com.co/es_co/ciclo-de-vida-de-las-publicaciones-de-inmuebles)  
**Captura:** 2026-10-08T22:50:32.256Z

---

## [Configuración o requisitos previos](../markdown/configuracion-o-requisitos-previos.md)

Actualización indicada por la fuente: 06/11/2025. Captura: 2026-10-08T22:50:33.208Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/configuracion-o-requisitos-previos](https://developers.mercadolibre.com.co/es_co/configuracion-o-requisitos-previos)

# Configuración o requisitos previos

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 06/11/2025  
**Captura:** 2026-10-08T22:50:33.208Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/configuracion-o-requisitos-previos](https://developers.mercadolibre.com.co/es_co/configuracion-o-requisitos-previos)

## Resumen

Guía inicial para cuenta, aplicación, credenciales, token y primera petición.

## Contenido y conceptos documentados

- La prueba GET /users/me debe retornar HTTP 200; se recomienda continuar con usuario test.

## Operaciones de API

## Conceptos y recursos asociados

### Configuración o requisitos previos

Guía inicial para cuenta, aplicación, credenciales, token y primera petición.
## Operaciones de API

### Comprobar token

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Retorna usuario asociado al token; la guía espera HTTP 200.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "datos del usuario"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/configuracion-o-requisitos-previos](https://developers.mercadolibre.com.co/es_co/configuracion-o-requisitos-previos)  
**Captura:** 2026-10-08T22:50:33.208Z

---

## [Consulta de usuarios](../markdown/consulta-de-usuarios.md)

Actualización indicada por la fuente: 06/11/2025. Captura: 2026-10-08T22:50:34.327Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/consulta-de-usuarios](https://developers.mercadolibre.com.co/es_co/consulta-de-usuarios)

# Consulta de usuarios

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 06/11/2025  
**Captura:** 2026-10-08T22:50:34.327Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/consulta-de-usuarios](https://developers.mercadolibre.com.co/es_co/consulta-de-usuarios)

## Resumen

Documenta consulta de perfil propio y público, pago inmediato y búsqueda de usuarios bloqueados.

## Contenido y conceptos documentados

- /users/me consulta perfil asociado al token; /users/{user_id} consulta un perfil público.

## Operaciones de API

## Conceptos y recursos asociados

### Consulta de usuarios

Documenta consulta de perfil propio y público, pago inmediato y búsqueda de usuarios bloqueados.
## Operaciones de API

### Consultar bloqueos por orden

**Método:** `GET`  
**Ruta:** `/block-api/search/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca bloqueos para órdenes.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario
- `type` (query, obligatorio): blocked_by_order

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "users[].id",
    "users[].blocked_at",
    "paging.offset",
    "paging.limit",
    "paging.total"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Activar pago inmediato

**Método:** `PUT`  
**Ruta:** `/users/{user_id}/immediate_payment`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Configura reason=by_user.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "reason"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- {"reason":"by_user"}

### Deshacer pago inmediato

**Método:** `DELETE`  
**Ruta:** `/users/{user_id}/immediate_payment/by_user`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina preferencia by_user.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar usuario público

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta perfil por ID.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "nickname",
    "country_id",
    "identification",
    "address",
    "phone",
    "user_type",
    "tags",
    "site_id",
    "seller_reputation",
    "buyer_reputation",
    "status"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar perfil propio

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Perfil del usuario asociado al token.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "nickname",
    "registration_date",
    "first_name",
    "last_name",
    "country_id",
    "email",
    "identification",
    "address",
    "phone",
    "user_type",
    "tags",
    "site_id",
    "seller_reputation",
    "buyer_reputation",
    "status"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/consulta-de-usuarios](https://developers.mercadolibre.com.co/es_co/consulta-de-usuarios)  
**Captura:** 2026-10-08T22:50:34.327Z

---

## [Contratación de paquetes de publicación](../markdown/contratacion-de-paquetes-de-publicacion.md)

Actualización indicada por la fuente: 08/11/2025. Captura: 2026-10-08T22:50:35.531Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/contratacion-de-paquetes-de-publicacion](https://developers.mercadolibre.com.co/es_co/contratacion-de-paquetes-de-publicacion)

# Contratación de paquetes de publicación

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 08/11/2025  
**Captura:** 2026-10-08T22:50:35.531Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/contratacion-de-paquetes-de-publicacion](https://developers.mercadolibre.com.co/es_co/contratacion-de-paquetes-de-publicacion)

## Resumen

Describe contratación de paquetes de publicación y destaque desde el portal.

## Contenido y conceptos documentados

- La contratación se realiza desde la cuenta; la fuente advierte que una cuenta real puede generar cargos.

## Operaciones de API

## Conceptos y recursos asociados

### Contratación de paquetes de publicación

Describe contratación de paquetes de publicación y destaque desde el portal.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/contratacion-de-paquetes-de-publicacion](https://developers.mercadolibre.com.co/es_co/contratacion-de-paquetes-de-publicacion)  
**Captura:** 2026-10-08T22:50:35.531Z

---

## [Desarrollos inmobiliarios](../markdown/desarrollos-inmobiliarios.md)

Actualización indicada por la fuente: 03/08/2026. Captura: 2026-10-08T22:50:36.682Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/desarrollos-inmobiliarios](https://developers.mercadolibre.com.co/es_co/desarrollos-inmobiliarios)

# Desarrollos inmobiliarios

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 03/08/2026  
**Captura:** 2026-10-08T22:50:36.682Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/desarrollos-inmobiliarios](https://developers.mercadolibre.com.co/es_co/desarrollos-inmobiliarios)

## Resumen

Explica categorías, atributos, imágenes, desarrollos con variaciones, cotizaciones y unidades multifamily.

## Contenido y conceptos documentados

- Un desarrollo requiere al menos una variación; attributes describe el proyecto y variations las unidades.
- La página indica que quotations migra a VIS Leads el 13/08/2026.

## Operaciones de API

## Conceptos y recursos asociados

### Desarrollos inmobiliarios

Explica categorías, atributos, imágenes, desarrollos con variaciones, cotizaciones y unidades multifamily.
## Operaciones de API

### Consultar atributos por categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve atributos permitidos para la categoría y variaciones.

**Parámetros**

- `category_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "name",
    "tags.allow_variations",
    "tags.required",
    "value_type",
    "value_max_length"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve detalle y subcategorías.

**Parámetros**

- `category_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "name",
    "children_categories",
    "settings",
    "currencies",
    "max_pictures_per_item",
    "status"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Crear desarrollo inmobiliario

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea el proyecto con al menos una variation y fotos asociadas.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "title",
    "category_id",
    "price",
    "currency_id",
    "available_quantity",
    "buying_mode",
    "listing_type_id",
    "condition",
    "location",
    "description",
    "pictures",
    "attributes",
    "variations[].price",
    "variations[].attribute_combinations",
    "variations[].available_quantity",
    "variations[].picture_ids"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "id",
    "site_id",
    "category_id",
    "price",
    "attributes",
    "variations",
    "status",
    "warnings"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La moneda de las variaciones coincide con el ítem; la moneda no se repite en su precio.

### Eliminar cotización

**Método:** `PUT`  
**Ruta:** `/quotations/{quotation_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina mediante delete=true.

**Parámetros**

- `quotation_id` (path, obligatorio): ID de cotización
- `caller.type` (query, obligatorio): seller en el ejemplo

**Solicitud**

```json
{
  "fields": [
    "delete"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "HTTP 200 OK"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- {"delete":true}

### Consultar cotización

**Método:** `GET`  
**Ruta:** `/quotations/{quotation_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalle de cotización.

**Parámetros**

- `quotation_id` (path, obligatorio): ID obtenido como external_id
- `caller.type` (query, obligatorio): seller o user

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "user",
    "item",
    "disclaimer",
    "created_at"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar cotizaciones por ítem

**Método:** `GET`  
**Ruta:** `/quotations/items_ids`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Admite uno o varios IDs separados por coma.

**Parámetros**

- `query` (query, obligatorio): ID o IDs separados por coma
- `caller.type` (query, obligatorio): seller en el ejemplo

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Reporte por vendedor

**Método:** `GET`  
**Ruta:** `/quotations/report`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Retorna total de cotizaciones del seller.

**Parámetros**

- `seller.id` (query, obligatorio): ID del seller

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "seller_id",
    "total",
    "date_from",
    "date_to"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Listar categorías del sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/categories`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista categorías disponibles.

**Parámetros**

- `site_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "name"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/desarrollos-inmobiliarios](https://developers.mercadolibre.com.co/es_co/desarrollos-inmobiliarios)  
**Captura:** 2026-10-08T22:50:36.682Z

---

## [Estadísticas de interacciones en Inmuebles](../markdown/estadisticas-de-interacciones-en-inmuebles.md)

Actualización indicada por la fuente: 06/11/2025. Captura: 2026-10-08T22:50:37.756Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/estadisticas-de-interacciones-en-inmuebles](https://developers.mercadolibre.com.co/es_co/estadisticas-de-interacciones-en-inmuebles)

# Estadísticas de interacciones en Inmuebles

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 06/11/2025  
**Captura:** 2026-10-08T22:50:37.756Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/estadisticas-de-interacciones-en-inmuebles](https://developers.mercadolibre.com.co/es_co/estadisticas-de-interacciones-en-inmuebles)

## Resumen

Documenta consultas de visitas, preguntas, vistas de teléfono y clics de WhatsApp por usuario o ítem.

## Contenido y conceptos documentados

- Los filtros usan date_from/date_to o last/unit/ending; algunos recursos admiten IDs separados por coma.

## Operaciones de API

## Conceptos y recursos asociados

### Estadísticas de interacciones en Inmuebles

Documenta consultas de visitas, preguntas, vistas de teléfono y clics de WhatsApp por usuario o ítem.
## Operaciones de API

### Vistas de teléfono por publicación

**Método:** `GET`  
**Ruta:** `/items/{item_id}/contacts/phone_views`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta interacciones telefónicas del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de ruta
- `date_from` (query): Fecha inicial ISO 8601
- `date_to` (query): Fecha final ISO 8601

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Vistas recientes por ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}/contacts/phone_views/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta vistas de teléfono en ventana.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de ruta
- `last` (query): Cantidad de unidades de tiempo
- `unit` (query): Unidad (day/hour)
- `ending` (query): Fecha límite ISO; omitir usa el momento de consulta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Vistas recientes por varios ítems

**Método:** `GET`  
**Ruta:** `/items/contacts/phone_views/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Acepta IDs separados por coma.

**Parámetros**

- `ids` (query): IDs de ítems separados por coma
- `last` (query): Cantidad de unidades de tiempo
- `unit` (query): Unidad (day/hour)
- `ending` (query): Fecha límite ISO; omitir usa el momento de consulta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Vistas de teléfono por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/contacts/phone_views`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta interacciones telefónicas del usuario.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de ruta
- `date_from` (query): Fecha inicial ISO 8601
- `date_to` (query): Fecha final ISO 8601

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Vistas recientes por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/contacts/phone_views/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta vistas de teléfono en ventana.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de ruta
- `last` (query): Cantidad de unidades de tiempo
- `unit` (query): Unidad (day/hour)
- `ending` (query): Fecha límite ISO; omitir usa el momento de consulta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Preguntas por publicación

**Método:** `GET`  
**Ruta:** `/items/{item_id}/contacts/questions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta preguntas del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de ruta
- `date_from` (query): Fecha inicial ISO 8601
- `date_to` (query): Fecha final ISO 8601

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Preguntas por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/contacts/questions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta preguntas del usuario.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de ruta
- `date_from` (query): Fecha inicial ISO 8601
- `date_to` (query): Fecha final ISO 8601

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Preguntas recientes por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/contacts/questions/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta preguntas en ventana.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de ruta
- `last` (query): Cantidad de unidades de tiempo
- `unit` (query): Unidad (day/hour)
- `ending` (query): Fecha límite ISO; omitir usa el momento de consulta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Visitas de publicación

**Método:** `GET`  
**Ruta:** `/visits/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve visitas del ítem.

**Parámetros**

- `ids` (query): ID del ítem

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "mapa item_id a total"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Visitas de publicación por rango

**Método:** `GET`  
**Ruta:** `/items/visits`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve visitas entre fechas.

**Parámetros**

- `ids` (query): ID del ítem
- `date_from` (query): Fecha inicial ISO 8601
- `date_to` (query): Fecha final ISO 8601

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Visitas por vendedor y rango

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items_visits`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta visitas del vendedor en intervalo.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de ruta
- `date_from` (query): Fecha inicial ISO 8601
- `date_to` (query): Fecha final ISO 8601

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Visitas recientes por vendedor

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items_visits/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta visitas en ventana.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de ruta
- `last` (query): Cantidad de unidades de tiempo
- `unit` (query): Unidad (day/hour)
- `ending` (query): Fecha límite ISO; omitir usa el momento de consulta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### WhatsApp por ítem y rango

**Método:** `GET`  
**Ruta:** `/items/{item_id}/contacts/whatsapp`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta clics en rango.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de ruta
- `date_from` (query): Fecha inicial ISO 8601
- `date_to` (query): Fecha final ISO 8601

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### WhatsApp reciente por ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}/contacts/whatsapp/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta clics en ventana.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de ruta
- `last` (query): Cantidad de unidades de tiempo
- `unit` (query): Unidad (day/hour)
- `ending` (query): Fecha límite ISO; omitir usa el momento de consulta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### WhatsApp reciente por varios ítems

**Método:** `GET`  
**Ruta:** `/items/contacts/whatsapp/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Acepta IDs separados por coma.

**Parámetros**

- `ids` (query): IDs separados por coma
- `last` (query): Cantidad de unidades de tiempo
- `unit` (query): Unidad (day/hour)
- `ending` (query): Fecha límite ISO; omitir usa el momento de consulta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### WhatsApp reciente por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/contacts/whatsapp/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta interacciones de WhatsApp en ventana.

**Parámetros**

- `user_id` (path, obligatorio): Identificador de ruta
- `last` (query): Cantidad de unidades de tiempo
- `unit` (query): Unidad (day/hour)
- `ending` (query): Fecha límite ISO; omitir usa el momento de consulta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "total",
    "date_from",
    "date_to; depende del recurso"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/estadisticas-de-interacciones-en-inmuebles](https://developers.mercadolibre.com.co/es_co/estadisticas-de-interacciones-en-inmuebles)  
**Captura:** 2026-10-08T22:50:37.756Z

---

## [Experiencia para inmuebles](../markdown/experiencia-para-inmuebles.md)

Actualización indicada por la fuente: 23/09/2026. Captura: 2026-10-08T22:50:38.813Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/experiencia-para-inmuebles](https://developers.mercadolibre.com.co/es_co/experiencia-para-inmuebles)

# Experiencia para inmuebles

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 23/09/2026  
**Captura:** 2026-10-08T22:50:38.813Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/experiencia-para-inmuebles](https://developers.mercadolibre.com.co/es_co/experiencia-para-inmuebles)

## Resumen

Documenta configuración de proveedores, leads, agendas de visitas y cambios multifamily.

## Contenido y conceptos documentados

- La configuración contiene requisitos, nóminas, notificaciones y factor de renta; operation puede ser price_updated, unit_added o unit_removed.

## Operaciones de API

## Conceptos y recursos asociados

### Experiencia para inmuebles

Documenta configuración de proveedores, leads, agendas de visitas y cambios multifamily.
## Operaciones de API

### Crear configuración de provider

**Método:** `POST`  
**Ruta:** `/vis-transactions-hub/configurations/provider`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea parámetros de visitas.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "seller_id",
    "codebtor_required",
    "latest_dependent_worker_payrolls",
    "latest_independent_worker_payrolls",
    "email_notify_schedule",
    "salary_multiplier",
    "allow_guest_login"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Activar solicitudes de visita en ítems

**Método:** `POST`  
**Ruta:** `/vis-transactions-hub/{providerId}/entities/items/tags`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Marca o desmarca los ítems.

**Parámetros**

- `providerId` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "seller_id",
    "item_ids[]",
    "enable_rex"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "ítems marcados/desmarcados"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar lead

**Método:** `GET`  
**Ruta:** `/vis/leads/{lead_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

external_id identifica la agenda asociada.

**Parámetros**

- `lead_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "external_id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar configuración provider

**Método:** `GET`  
**Ruta:** `/vis-transactions-hub/configurations/provider/{provider_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta configuración por provider.

**Parámetros**

- `provider_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "provider_id",
    "codebtor_required",
    "latest_dependent_worker_payrolls",
    "latest_independent_worker_payrolls",
    "email_notify_schedule",
    "salary_multiplier",
    "allow_guest_login"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar detalle de agenda

**Método:** `GET`  
**Ruta:** `/vis-transactions-hub/{providerId}/entities/schedules/{schedule_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta agenda por ID.

**Parámetros**

- `providerId` (path, obligatorio): Identificador de la ruta
- `schedule_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "unit_name",
    "user_id",
    "email",
    "name",
    "last_name",
    "item_id",
    "phone1",
    "phone2",
    "scheduling_time",
    "scheduling_time_period"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar configuración seller

**Método:** `GET`  
**Ruta:** `/vis-transactions-hub/configurations/seller/{seller_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta configuración por seller.

**Parámetros**

- `seller_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "provider_id",
    "codebtor_required",
    "latest_dependent_worker_payrolls",
    "latest_independent_worker_payrolls",
    "email_notify_schedule",
    "salary_multiplier",
    "allow_guest_login"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Actualizar configuración

**Método:** `PATCH`  
**Ruta:** `/vis-transactions-hub/configurations/provider/{providerId}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza configuración del provider.

**Parámetros**

- `providerId` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "codebtor_required",
    "latest_dependent_worker_payrolls",
    "latest_independent_worker_payrolls",
    "email_notify_schedule",
    "salary_multiplier",
    "allow_guest_login",
    "notification_url"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Actualizar estado de agenda

**Método:** `PUT`  
**Ruta:** `/vis-transactions-hub/{providerId}/entities/schedules`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza estado de la agenda.

**Parámetros**

- `providerId` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "scheduling_id",
    "status_code",
    "status_name",
    "message",
    "timestamp",
    "data"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Actualizar unidades multifamily

**Método:** `PUT`  
**Ruta:** `/vis-transactions-hub/{providerId}/entities/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza precios y altas/bajas.

**Parámetros**

- `providerId` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "item_id",
    "status_code",
    "status_name",
    "message",
    "timestamp",
    "data.units[].unit_name",
    "data.units[].price",
    "data.units[].operation"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- operation: price_updated, unit_added, unit_removed

**Fuente:** [https://developers.mercadolibre.com.co/es_co/experiencia-para-inmuebles](https://developers.mercadolibre.com.co/es_co/experiencia-para-inmuebles)  
**Captura:** 2026-10-08T22:50:38.813Z

---

## [Gestionar paquetes de inmuebles](../markdown/gestionar-paquetes-de-inmuebles.md)

Actualización indicada por la fuente: 24/11/2025. Captura: 2026-10-08T22:50:39.845Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/gestionar-paquetes-de-inmuebles](https://developers.mercadolibre.com.co/es_co/gestionar-paquetes-de-inmuebles)

# Gestionar paquetes de inmuebles

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 24/11/2025  
**Captura:** 2026-10-08T22:50:39.845Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestionar-paquetes-de-inmuebles](https://developers.mercadolibre.com.co/es_co/gestionar-paquetes-de-inmuebles)

## Resumen

Explica paquetes, cupos, estados y consultas de paquetes disponibles o contratados.

## Contenido y conceptos documentados

- silver habilita publicación; gold y gold_premium son destaques. package_content y status filtran consultas.

## Operaciones de API

## Conceptos y recursos asociados

### Gestionar paquetes de inmuebles

Explica paquetes, cupos, estados y consultas de paquetes disponibles o contratados.
### Ruta mencionada /items

La fuente menciona la ruta /items, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/items`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar paquetes disponibles

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/classifieds_promotion_packs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista paquetes de una categoría.

**Parámetros**

- `category_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "category_id",
    "brand",
    "description",
    "price",
    "package_type",
    "package_content",
    "duration",
    "status",
    "charge_type_id",
    "max_upgrades",
    "quota_type",
    "listing_details[].listing_type_id",
    "listing_details[].available_listings",
    "visibility"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Referencia HTTP POST /items

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /items. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Consultar paquetes por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/classifieds_promotion_packs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Filtra por package_content y status.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario
- `package_content` (query): publications, upgrades, developments o ALL
- `status` (query): active, paused, pending o finished; también aparece finalized

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "user_id",
    "promotion_pack_id",
    "category_id",
    "description",
    "package_type",
    "package_content",
    "status",
    "date_created",
    "date_start",
    "date_expires",
    "date_stopped",
    "last_updated",
    "engagement_type",
    "charge_id",
    "remaining_listings",
    "used_listings",
    "listing_details"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar paquetes por listing_type

**Método:** `GET`  
**Ruta:** `/users/{user_id}/classifieds_promotion_packs/{listing_type}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Filtra por tipo y categoría opcional.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario
- `listing_type` (path, opcional): silver, gold o gold_premium
- `categoryId` (query, opcional): Categoría principal

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestionar-paquetes-de-inmuebles](https://developers.mercadolibre.com.co/es_co/gestionar-paquetes-de-inmuebles)  
**Captura:** 2026-10-08T22:50:39.845Z

---

## [Glosario](../markdown/glosario-inmuebles.md)

Actualización indicada por la fuente: 06/11/2025. Captura: 2026-10-08T22:50:40.711Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/glosario-inmuebles](https://developers.mercadolibre.com.co/es_co/glosario-inmuebles)

# Glosario

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 06/11/2025  
**Captura:** 2026-10-08T22:50:40.711Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/glosario-inmuebles](https://developers.mercadolibre.com.co/es_co/glosario-inmuebles)

## Resumen

Glosario de conceptos del dominio de inmuebles.

## Contenido y conceptos documentados

- La captura de esta página no contiene entradas de glosario.

## Operaciones de API

## Conceptos y recursos asociados

### Glosario

Glosario de conceptos del dominio de inmuebles.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/glosario-inmuebles](https://developers.mercadolibre.com.co/es_co/glosario-inmuebles)  
**Captura:** 2026-10-08T22:50:40.711Z

---

## [Introducción guía de inmuebles](../markdown/introduccion-guia-de-inmuebles.md)

Actualización indicada por la fuente: 06/11/2025. Captura: 2026-10-08T22:50:41.797Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/introduccion-guia-de-inmuebles](https://developers.mercadolibre.com.co/es_co/introduccion-guia-de-inmuebles)

# Introducción guía de inmuebles

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 06/11/2025  
**Captura:** 2026-10-08T22:50:41.797Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/introduccion-guia-de-inmuebles](https://developers.mercadolibre.com.co/es_co/introduccion-guia-de-inmuebles)

## Resumen

Presenta el recorrido para publicar y administrar inmuebles.

## Contenido y conceptos documentados

- Remite a requisitos previos, publicación de prueba, categorías, atributos y localización.

## Operaciones de API

## Conceptos y recursos asociados

### Introducción guía de inmuebles

Presenta el recorrido para publicar y administrar inmuebles.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/introduccion-guia-de-inmuebles](https://developers.mercadolibre.com.co/es_co/introduccion-guia-de-inmuebles)  
**Captura:** 2026-10-08T22:50:41.797Z

---

## [Leads](../markdown/leads-inmuebles.md)

Actualización indicada por la fuente: 07/05/2026. Captura: 2026-10-08T22:50:42.774Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/leads-inmuebles](https://developers.mercadolibre.com.co/es_co/leads-inmuebles)

# Leads

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 07/05/2026  
**Captura:** 2026-10-08T22:50:42.774Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/leads-inmuebles](https://developers.mercadolibre.com.co/es_co/leads-inmuebles)

## Resumen

Un lead representa un contacto de un comprador con una publicación: WhatsApp, pregunta, llamada, agenda de visita o cotización. La guía explica cómo consultar los interesados de un vendedor, filtrar por período/tipo/ítem/comprador, paginar los resultados y recuperar un detalle de lead o el texto de una pregunta asociada.

## Contenido y conceptos documentados

- Los filtros temporales son date_from y date_to; la paginación usa offset y limit. El valor por defecto documentado es offset=0, limit=10 y un rango de los últimos siete días.
- contact_types acepta whatsapp, question, call, schedule y quotation. schedule puede retornar vacío si el ítem no ofrece la función.
- include_guest=true agrega guest y summary. Los leads guest se devuelven completos para el rango de fechas y no se ven afectados por offset/limit.
- La respuesta agrupa compradores en results y expone paging, fechas y leads; el texto de preguntas se consulta por separado con external_id. La guía advierte que campos personales pueden depender del tipo de acceso y que preguntas sin responder por más de siete meses se eliminan.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /v1/users/806525693/leads/buyers

La fuente menciona la ruta /v1/users/806525693/leads/buyers, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/v1/users/806525693/leads/buyers`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Tipos de contacto de leads

La guía distingue whatsapp, question, call, schedule y quotation. schedule depende de que la publicación ofrezca agenda; include_guest=true añade leads y conteos de personas no registradas.
## Operaciones de API

### Consultar interesados y leads de un vendedor

**Método:** `GET`  
**Ruta:** `/vis/users/$USER_ID/leads/buyers`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista compradores interesados; filtra por fecha, tipo de contacto, ítem o comprador y permite paginación. include_guest=true agrega leads guest y un resumen por ítem.

**Parámetros**

- `USER_ID` (path, obligatorio): Identificador del vendedor.
- `offset` (query, opcional): Posición inicial; por defecto 0.
- `limit` (query, opcional): Cantidad máxima; por defecto 10.
- `date_from` (query, opcional): Fecha inicial YYYY-MM-DD; por defecto siete días antes.
- `date_to` (query, opcional): Fecha final YYYY-MM-DD; por defecto fecha actual.
- `contact_types` (query, opcional): Tipos de contacto; si se omite retorna todos.
- `item_id` (query, opcional): Filtro por publicación.
- `buyer_ids` (query, opcional): Uno o varios IDs separados por coma.
- `include_guest` (query, opcional): Incluye leads guest y guest/summary; paginación no aplica a guest.

**Solicitud**

No documentado en la fuente.

**Respuesta**

results[] con comprador, item_id y leads[]; paging.offset/limit/total; date_from/date_to. include_guest añade guest[] y summary[].

**Errores documentados**

- 400: rango de fechas invertido o formato/USER_ID/parámetro/tipo de lead inválido.
- 403: token inválido, expirado, no corresponde al vendedor o falta autorización.
- 404: lead no encontrado.
- 409: quota exceeded.

**Ejemplos**

- Tipos: whatsapp, question, call, schedule y quotation. schedule puede devolver arreglo vacío si no está habilitado en el ítem.

### Obtener detalle de un lead

**Método:** `GET`  
**Ruta:** `/vis/leads/$LEAD_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera los datos del lead indicado por ID, recibido en una notificación o en results.leads.id.

**Parámetros**

- `LEAD_ID` (path, obligatorio): Identificador del lead.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, item_id, created_at, contact_type, external_id, status, buyer_id y datos de contacto cuando estén disponibles.

**Errores documentados**

- 403: token inválido, expirado o sin permisos.
- 404: lead no encontrado para el usuario.

**Ejemplos**

- El detalle del lead no contiene el texto de una pregunta.

### Consultar pregunta asociada a un lead

**Método:** `GET`  
**Ruta:** `/questions/$QUESTION_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el mensaje de pregunta usando external_id como QUESTION_ID y api_version=4.

**Parámetros**

- `QUESTION_ID` (path, obligatorio): Coincide con external_id del lead.
- `api_version` (query, obligatorio): Usar 4 para la nueva estructura JSON.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, seller_id, buyer_id, item_id, status, text, fechas y answer.text/status/date_created.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Con estado BANNED, el texto puede venir vacío; la fuente advierte que preguntas sin respuesta de más de siete meses se eliminan.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/leads-inmuebles](https://developers.mercadolibre.com.co/es_co/leads-inmuebles)  
**Captura:** 2026-10-08T22:50:42.774Z

---

## [Localizar Inmuebles](../markdown/localizar-inmuebles.md)

Actualización indicada por la fuente: 08/11/2025. Captura: 2026-10-08T22:50:43.880Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/localizar-inmuebles](https://developers.mercadolibre.com.co/es_co/localizar-inmuebles)

# Localizar Inmuebles

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 08/11/2025  
**Captura:** 2026-10-08T22:50:43.880Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/localizar-inmuebles](https://developers.mercadolibre.com.co/es_co/localizar-inmuebles)

## Resumen

La guía consulta la jerarquía de ubicaciones para seleccionar una zona y después buscar publicaciones inmobiliarias por caja geográfica y categoría. También documenta cómo ocultar y restaurar la dirección exacta de una publicación.

## Contenido y conceptos documentados

- El recorrido de datos es países → estados/provincias → ciudades → barrios/comunas. Las entidades pueden incluir identificadores, jerarquía superior, coordenadas y listas de ubicaciones hijas.
- Para búsqueda geográfica, item_location usa el formato lat:LAT1_LAT2,lon:LON1_LON2 junto con category. La fuente ilustra una búsqueda de categoría MLA1459 en el site MLA.
- PUT sobre address_line_by_reference oculta la dirección exacta; DELETE revierte el ocultamiento. La guía atribuye la decisión al gestor del inmueble por privacidad.

## Operaciones de API

## Conceptos y recursos asociados

### Jerarquía de ubicaciones inmobiliarias

La guía recorre país → estado/provincia → ciudad → barrio/comuna y usa esa información para buscar avisos por área geográfica u ocultar dirección exacta.
## Operaciones de API

### Buscar inmuebles por ubicación

**Método:** `GET`  
**Ruta:** `/sites/$COUNTRY_ID/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca avisos en un área de latitud/longitud y categoría.

**Parámetros**

- `COUNTRY_ID` (path, obligatorio): Identificador de país/site.
- `item_location` (query, obligatorio): lat:LAT1_LAT2,lon:LON1_LON2.
- `category` (query, obligatorio): ID de categoría inmobiliaria.
- `limit` (query, opcional): El ejemplo limita la respuesta.

**Solicitud**

No documentado en la fuente.

**Respuesta**

site_id, paging, results, sort, filters, available_filters y currency.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con site MLA y categoría MLA1459.

### Consultar barrio

**Método:** `GET`  
**Ruta:** `/classified_locations/neighborhoods/$NEIGHBORHOOD_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene barrio/comuna, ciudad, estado, país, subbarrios y coordenadas.

**Parámetros**

- `NEIGHBORHOOD_ID` (path, obligatorio): ID de barrio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, city, state, country, geo_information y subneighborhoods.

**Errores documentados**

- 404: barrio no encontrado.

**Ejemplos**

No documentado en la fuente.

### Consultar ciudad

**Método:** `GET`  
**Ruta:** `/classified_locations/cities/$CITY_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene ciudad, estado, país, barrios y coordenadas.

**Parámetros**

- `CITY_ID` (path, obligatorio): ID de ciudad.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, state, country, neighborhoods y geo_information.location.latitude/longitude.

**Errores documentados**

- 404: ciudad no encontrada.

**Ejemplos**

No documentado en la fuente.

### Consultar estado

**Método:** `GET`  
**Ruta:** `/classified_locations/states/$STATE_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene estado/provincia, país, ciudades y geolocalización.

**Parámetros**

- `STATE_ID` (path, obligatorio): ID del estado.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, country, geo_information, time_zone, time_zone_name y cities.

**Errores documentados**

- 404: estado no encontrado.

**Ejemplos**

No documentado en la fuente.

### Consultar país

**Método:** `GET`  
**Ruta:** `/classified_locations/countries/$COUNTRY_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene país por identificador de 2 o 3 caracteres.

**Parámetros**

- `COUNTRY_ID` (path, obligatorio): ID de país de 2 o 3 caracteres.

**Solicitud**

No documentado en la fuente.

**Respuesta**

País con id, name y datos de ubicación.

**Errores documentados**

- 404: país no encontrado.

**Ejemplos**

No documentado en la fuente.

### Listar países

**Método:** `GET`  
**Ruta:** `/classified_locations/countries`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista países disponibles para explorar ubicaciones inmobiliarias.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Arreglo de países con id, name y datos geográficos según respuesta.

**Errores documentados**

- No requiere parámetros de consulta.

**Ejemplos**

No documentado en la fuente.

### Ocultar dirección exacta

**Método:** `PUT`  
**Ruta:** `/items/$ITEM_ID/address_line_by_reference`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Oculta la dirección exacta por privacidad.

**Parámetros**

- `ITEM_ID` (path, obligatorio): ID del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Referencia HTTP GET /classified_locations/states/TUxBUENPUmFkZGIw

**Método:** `GET`  
**Ruta:** `/classified_locations/states/TUxBUENPUmFkZGIw`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /classified_locations/states/TUxBUENPUmFkZGIw. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /classified_locations/countries/AR

**Método:** `GET`  
**Ruta:** `/classified_locations/countries/AR`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /classified_locations/countries/AR. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Revertir ocultamiento de dirección

**Método:** `DELETE`  
**Ruta:** `/items/$ITEM_ID/address_line_by_reference`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina el tag de ocultamiento de dirección.

**Parámetros**

- `ITEM_ID` (path, obligatorio): ID del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/localizar-inmuebles](https://developers.mercadolibre.com.co/es_co/localizar-inmuebles)  
**Captura:** 2026-10-08T22:50:43.880Z

---

## [Obtención del Access Token](../markdown/obtencion-del-access-token.md)

Actualización indicada por la fuente: 05/11/2025. Captura: 2026-10-08T22:50:45.394Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/obtencion-del-access-token](https://developers.mercadolibre.com.co/es_co/obtencion-del-access-token)

# Obtención del Access Token

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 05/11/2025  
**Captura:** 2026-10-08T22:50:45.394Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/obtencion-del-access-token](https://developers.mercadolibre.com.co/es_co/obtencion-del-access-token)

## Resumen

El flujo explicado obtiene un Access Token mediante OAuth authorization code. Requiere una aplicación creada y sus Client ID, Client Secret y Redirect URI; el usuario inicia sesión, autoriza y recibe un code en la URL de retorno.

## Contenido y conceptos documentados

- El code se intercambia en POST /oauth/token usando grant_type=authorization_code y el cuerpo application/x-www-form-urlencoded.
- La respuesta de éxito documenta access_token, token_type, expires_in, scope, user_id y refresh_token; el token tiene duración limitada.
- La página remite a la guía de autenticación para errores y no detalla aquí la operación de refresh.

## Operaciones de API
## Operaciones de API

### Obtener Access Token con authorization code

**Método:** `POST`  
**Ruta:** `/oauth/token`  
**Autenticación:** No documentado en la fuente.

Intercambia el código recibido tras el consentimiento por un Access Token OAuth temporal; requiere credenciales de aplicación y Redirect URI registrados.

**Parámetros**

- `grant_type` (body, obligatorio): La guía usa authorization_code.
- `client_id` (body, obligatorio): ID de la aplicación.
- `client_secret` (body, obligatorio): Clave secreta.
- `code` (body, obligatorio): Código devuelto en la redirección.
- `redirect_uri` (body, obligatorio): URI registrada.

**Solicitud**

application/x-www-form-urlencoded

**Respuesta**

access_token, token_type, expires_in, scope, user_id y refresh_token.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El flujo comienza en la URL de autorización del sitio correspondiente; esta página no detalla la operación refresh.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/obtencion-del-access-token](https://developers.mercadolibre.com.co/es_co/obtencion-del-access-token)  
**Captura:** 2026-10-08T22:50:45.394Z

---

## [Paquetes y permisos para proyectos, desarrollos o emprendimientos inmobiliarios](../markdown/paquetes-y-permisos-para-proyectos-desarrollos-o-emprendimientos-inmobiliarios.md)

Actualización indicada por la fuente: 06/11/2025. Captura: 2026-10-08T22:50:46.283Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/paquetes-y-permisos-para-proyectos-desarrollos-o-emprendimientos-inmobiliarios](https://developers.mercadolibre.com.co/es_co/paquetes-y-permisos-para-proyectos-desarrollos-o-emprendimientos-inmobiliarios)

# Paquetes y permisos para proyectos, desarrollos o emprendimientos inmobiliarios

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 06/11/2025  
**Captura:** 2026-10-08T22:50:46.283Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/paquetes-y-permisos-para-proyectos-desarrollos-o-emprendimientos-inmobiliarios](https://developers.mercadolibre.com.co/es_co/paquetes-y-permisos-para-proyectos-desarrollos-o-emprendimientos-inmobiliarios)

## Resumen

Las publicaciones de proyectos o desarrollos pueden ofrecer unidades con variaciones. Para crearlas se requieren permisos adicionales y un paquete especial solicitado a soporte.

## Contenido y conceptos documentados

- El paquete se activa para un usuario y habilita una sola publicación con variaciones; una publicación adicional requiere otra solicitud.
- El usuario con este paquete no puede realizar publicaciones inmobiliarias convencionales, según la nota de la fuente.
- Una vez confirmada la activación, se continúa con la guía de variaciones.

## Operaciones de API

## Conceptos y recursos asociados

### Permisos y paquete para variaciones inmobiliarias

Se requieren privilegios y paquete especial solicitado a soporte. La activación es por usuario y habilita una publicación con variaciones; publicaciones adicionales requieren otra solicitud. El usuario no puede realizar publicaciones convencionales mientras usa este paquete.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/paquetes-y-permisos-para-proyectos-desarrollos-o-emprendimientos-inmobiliarios](https://developers.mercadolibre.com.co/es_co/paquetes-y-permisos-para-proyectos-desarrollos-o-emprendimientos-inmobiliarios)  
**Captura:** 2026-10-08T22:50:46.283Z

---

## [Pasos rápidos para publicar un inmueble de prueba](../markdown/pasos-rapidos-para-publicar-un-inmueble-de-prueba.md)

Actualización indicada por la fuente: 05/01/2026. Captura: 2026-10-08T22:50:47.235Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/pasos-rapidos-para-publicar-un-inmueble-de-prueba](https://developers.mercadolibre.com.co/es_co/pasos-rapidos-para-publicar-un-inmueble-de-prueba)

# Pasos rápidos para publicar un inmueble de prueba

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 05/01/2026  
**Captura:** 2026-10-08T22:50:47.235Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/pasos-rapidos-para-publicar-un-inmueble-de-prueba](https://developers.mercadolibre.com.co/es_co/pasos-rapidos-para-publicar-un-inmueble-de-prueba)

## Resumen

La guía recorre la puesta en marcha de una cuenta de pruebas inmobiliaria: crear el usuario de prueba, registrarlo como empresa inmobiliaria y solicitar su activación, obtener credenciales/tokens, validar la cuenta, activar un paquete y publicar un inmueble para luego consultar su estado.

## Contenido y conceptos documentados

- La fuente recomienda realizar las pruebas con un usuario de prueba y verificar /users/me antes de publicar.
- El flujo publica con POST /items y usa el ID devuelto para GET /items/$ITEM_ID.
- Se remite a las guías de token, configuración de usuario, paquetes y publicación inmobiliaria para los requisitos que dependen de la cuenta.

## Operaciones de API

## Conceptos y recursos asociados

### Flujo para publicar inmueble de prueba

El recorrido incluye crear usuario de prueba, registrarlo y activarlo como inmobiliaria, obtener token, validar cuenta, activar paquete, publicar y consultar el ítem.
## Operaciones de API

### Consultar publicación de prueba

**Método:** `GET`  
**Ruta:** `/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Verifica el estado con el identificador devuelto por POST /items.

**Parámetros**

- `ITEM_ID` (path, obligatorio): ID recibido al publicar.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Detalle de publicación para verificar estado.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Publicar inmueble de prueba

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una publicación de prueba con el JSON inmobiliario tras configurar y habilitar la cuenta.

**Parámetros**

- `body` (body, obligatorio): JSON con title, category_id, price, currency_id, available_quantity, buying_mode, listing_type_id, condition, description, location, pictures, attributes y seller_contact.

**Solicitud**

JSON de publicación inmobiliaria.

**Respuesta**

La respuesta proporciona el ID del ítem para consultar su estado.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Realizar las pruebas con usuario de prueba.

### Consultar usuario autenticado

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Valida que el token corresponde al usuario de prueba configurado.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Datos del usuario autenticado; verificar coincidencia con la cuenta de prueba.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/pasos-rapidos-para-publicar-un-inmueble-de-prueba](https://developers.mercadolibre.com.co/es_co/pasos-rapidos-para-publicar-un-inmueble-de-prueba)  
**Captura:** 2026-10-08T22:50:47.235Z

---

## [Primeros pasos](../markdown/primeros-pasos-inmuebles.md)

Actualización indicada por la fuente: 05/11/2025. Captura: 2026-10-08T22:50:48.098Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/primeros-pasos-inmuebles](https://developers.mercadolibre.com.co/es_co/primeros-pasos-inmuebles)

# Primeros pasos

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 05/11/2025  
**Captura:** 2026-10-08T22:50:48.098Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/primeros-pasos-inmuebles](https://developers.mercadolibre.com.co/es_co/primeros-pasos-inmuebles)

## Resumen

La página presenta de forma breve el recorrido previo para publicar un inmueble de prueba y enlaza el siguiente paso de la guía inmobiliaria.

## Contenido y conceptos documentados

- Su contenido es introductorio: menciona un diagrama de pasos esenciales y remite a “publicar un inmueble de prueba”.
- No especifica parámetros, cuerpos, respuestas ni operaciones HTTP en esta página.

## Operaciones de API

## Conceptos y recursos asociados

### Preparación para publicar inmueble de prueba

Página introductoria con diagrama de pasos esenciales que remite a la guía detallada de publicación; no describe rutas HTTP.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/primeros-pasos-inmuebles](https://developers.mercadolibre.com.co/es_co/primeros-pasos-inmuebles)  
**Captura:** 2026-10-08T22:50:48.098Z

---

## [Publica Inmuebles](../markdown/publica-inmueble.md)

Actualización indicada por la fuente: 28/08/2026. Captura: 2026-10-08T22:50:49.107Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/publica-inmueble](https://developers.mercadolibre.com.co/es_co/publica-inmueble)

# Publica Inmuebles

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 28/08/2026  
**Captura:** 2026-10-08T22:50:49.107Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/publica-inmueble](https://developers.mercadolibre.com.co/es_co/publica-inmueble)

## Resumen

Esta guía describe la creación de publicaciones inmobiliarias con POST /items. Recomienda validar el JSON y revisar los atributos requeridos, la ubicación y la calidad del aviso antes de enviarlo.

## Contenido y conceptos documentados

- El ejemplo de solicitud incluye campos de publicación como title, category_id, price, currency_id, available_quantity, buying_mode, listing_type_id, condition, description, location, pictures, attributes, channels, video_id y seller_contact.
- Desde 01/10/2026, country_code2 y phone2 son obligatorios en seller_contact para todos los tipos de usuario. Deben contener solo dígitos: el código de país va en country_code2 y el resto del número en phone2.
- Desde 23/02/2026, pictures debe incluir al menos una imagen para listing type silver y para tipos gold configurados con requires_picture=true; si falta, la fuente documenta HTTP 400, error 173 LTP_PICTURE_REQUIRED.
- Para publicar también en el Portal Inmobiliario de Chile (MLC), el ejemplo de la guía incluye CMG_SITE.

## Operaciones de API
## Operaciones de API

### Publicar inmueble

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea aviso inmobiliario. El JSON debe cumplir atributos y seller_contact; desde 01/10/2026 country_code2 y phone2 son obligatorios para todos los usuarios.

**Parámetros**

- `body` (body, obligatorio): JSON de publicación y seller_contact.

**Solicitud**

title, category_id, price, currency_id, available_quantity, buying_mode, listing_type_id, condition, description, location, pictures, attributes, channels, video_id y seller_contact.

**Respuesta**

Respuesta de creación con ID del ítem; otros campos: No documentado en la fuente.

**Errores documentados**

- 400 seller_contact.required: falta objeto seller_contact.
- 400 seller_contact.country_code2.required: falta country_code2.
- 400 seller_contact.phone2.required: falta phone2.
- 400 seller_contact.country_code2.invalid: formato inválido.
- 400 seller_contact.phone2.invalid: formato inválido.
- 400 error 173 LTP_PICTURE_REQUIRED: falta imagen para listing type silver o tipo gold con requires_picture=true.

**Ejemplos**

- country_code2 y phone2 solo llevan dígitos; código de país y resto del número van en campos separados.
- Para MLC, la guía indica CMG_SITE para listing_source portalinmobiliario.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/publica-inmueble](https://developers.mercadolibre.com.co/es_co/publica-inmueble)  
**Captura:** 2026-10-08T22:50:49.107Z

---

## [Publicaciones de Tiendas Oficiales para Inmuebles](../markdown/publicaciones-de-tiendas-oficiales-para-inmuebles.md)

Actualización indicada por la fuente: 06/11/2025. Captura: 2026-10-08T22:50:50.140Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/publicaciones-de-tiendas-oficiales-para-inmuebles](https://developers.mercadolibre.com.co/es_co/publicaciones-de-tiendas-oficiales-para-inmuebles)

# Publicaciones de Tiendas Oficiales para Inmuebles

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 06/11/2025  
**Captura:** 2026-10-08T22:50:50.140Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/publicaciones-de-tiendas-oficiales-para-inmuebles](https://developers.mercadolibre.com.co/es_co/publicaciones-de-tiendas-oficiales-para-inmuebles)

## Resumen

Las publicaciones de usuarios con Tienda Oficial usan el flujo normal de POST /items e incluyen official_store_id para vincular el inmueble con la tienda correspondiente.

## Contenido y conceptos documentados

- official_store_id es obligatorio para usuarios asociados a una Tienda Oficial; si el vendedor no tiene una, se envía null.
- La guía muestra errores si falta el identificador o si el usuario no está autorizado para usar la tienda indicada.
- En una actualización del ítem solo se debe incluir official_store_id cuando se quiera cambiar la tienda; esta página no especifica la ruta de actualización.

## Operaciones de API
## Operaciones de API

### Publicar inmueble en Tienda Oficial

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Publica un aviso con official_store_id; es obligatorio para vendedores ligados a una Tienda Oficial y se envía null si el vendedor no tiene tienda.

**Parámetros**

- `official_store_id` (body, obligatorio): ID de tienda del usuario vinculado; null si no existe tienda.

**Solicitud**

JSON con official_store_id y campos de publicación.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400 item.official_store_id.invalid: usuario tipo brand debe proporcionar ID de tienda.
- 403 body.invalid_official_store_id: vendedor no autorizado para el ID indicado.

**Ejemplos**

- En actualizaciones, enviar official_store_id solo si se desea modificar la tienda; esta página no da ruta de actualización.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/publicaciones-de-tiendas-oficiales-para-inmuebles](https://developers.mercadolibre.com.co/es_co/publicaciones-de-tiendas-oficiales-para-inmuebles)  
**Captura:** 2026-10-08T22:50:50.140Z

---

## [Solicitud de visita](../markdown/solicitud-de-visita.md)

Actualización indicada por la fuente: 08/11/2025. Captura: 2026-10-08T22:50:51.129Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/solicitud-de-visita](https://developers.mercadolibre.com.co/es_co/solicitud-de-visita)

# Solicitud de visita

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 08/11/2025  
**Captura:** 2026-10-08T22:50:51.129Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/solicitud-de-visita](https://developers.mercadolibre.com.co/es_co/solicitud-de-visita)

## Resumen

La guía explica cómo habilitar y gestionar solicitudes de visita para publicaciones inmobiliarias. La funcionalidad descrita está disponible en Chile (MLC) y requiere una cuenta inmobiliaria/profesional, autorización, publicaciones con CONTACT_SCHEDULE y configuración del tópico de notificaciones VIS Leads.

## Contenido y conceptos documentados

- Las notificaciones de solicitudes usan el topic vis_leads y la acción visit_request; incluyen recurso, usuario, aplicación, fechas de envío/recepción e intentos.
- La agenda se genera desde la experiencia del sitio; la fuente dice que no existe endpoint API para crear agendas directamente. El vendedor puede recuperar el detalle del lead/schedule con su LEAD_ID.
- La publicación puede perder la opción automáticamente ante disminución de reputación, cancelación de más del 50 % de visitas o republicación de anuncios existentes.

## Operaciones de API

## Conceptos y recursos asociados

### Flujo y notificaciones de solicitudes de visita

Requiere cuenta inmobiliaria/profesional, token, publicación con CONTACT_SCHEDULE y notificaciones VIS Leads; agenda se gestiona en el sitio, no mediante creación directa por API.
## Operaciones de API

### Obtener detalle de solicitud de visita

**Método:** `GET`  
**Ruta:** `/vis/leads/$LEAD_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera una agenda usando el ID de lead de visita recibido por VIS Leads.

**Parámetros**

- `LEAD_ID` (path, obligatorio): ID del lead/schedule.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, item_id, created_at, contact_type, external_id, status, buyer_id y datos del comprador disponibles.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página dice que no existe endpoint API para crear agendas directamente. La disponibilidad descrita es MLC.
- Topic vis_leads y acción visit_request.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/solicitud-de-visita](https://developers.mercadolibre.com.co/es_co/solicitud-de-visita)  
**Captura:** 2026-10-08T22:50:51.129Z

---

## [Variaciones](../markdown/variaciones-para-inmuebles.md)

Actualización indicada por la fuente: 09/11/2025. Captura: 2026-10-08T22:50:52.096Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/variaciones-para-inmuebles](https://developers.mercadolibre.com.co/es_co/variaciones-para-inmuebles)

# Variaciones

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 09/11/2025  
**Captura:** 2026-10-08T22:50:52.096Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/variaciones-para-inmuebles](https://developers.mercadolibre.com.co/es_co/variaciones-para-inmuebles)

## Resumen

Las variaciones permiten representar varias unidades o alternativas dentro de una publicación de proyecto inmobiliario, con diferencias en atributos como área, dormitorios o baños. La guía muestra cómo identificar categorías habilitadas, consultar atributos y recuperar las variaciones publicadas.

## Contenido y conceptos documentados

- Categorías citadas: MLA401806 (Argentina), MLU455673 (Uruguay), MLC157523 (Chile) y MLM170376 (México). La disponibilidad indicada corresponde a esos sitios.
- En los atributos, allow_variations=true identifica los que van en attribute_combinations; los atributos comunes van en attributes.
- La publicación requiere privilegios y paquete de desarrollo; la guía indica que el paquete habilita una sola publicación.
- La respuesta puede incluir variations, item_relations, attribute_combinations, available_quantity, sold_quantity, price, sale_terms y picture_ids. La fuente enumera errores 400 por atributos obligatorios omitidos/mal ubicados/valores no permitidos y cuota agotada.

## Operaciones de API

## Conceptos y recursos asociados

### Estructura y requisitos de variaciones

Los atributos comunes van en attributes y los variables en attribute_combinations. Requiere privilegios/paquete; la guía enumera errores 400 por atributos obligatorios omitidos, mal ubicados o valores no permitidos y por cuota agotada.
## Operaciones de API

### Consultar atributos de categoría

**Método:** `GET`  
**Ruta:** `/categories/$CATEGORY_ID/attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Identifica atributos obligatorios y permitidos para variaciones; allow_variations=true indica que van en attribute_combinations.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Atributos con tags required y allow_variations.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar categoría con variaciones

**Método:** `GET`  
**Ruta:** `/categories/$CATEGORY_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Comprueba que attribute_types indique variations.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

attribute_types con valor variations.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La guía cita MLA401806, MLU455673, MLC157523 y MLM170376.

### Consultar variación específica

**Método:** `GET`  
**Ruta:** `/items/$ITEM_ID/variations/$VARIATION_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene una variación por ID dentro de un ítem.

**Parámetros**

- `ITEM_ID` (path, obligatorio): ID del ítem.
- `VARIATION_ID` (path, obligatorio): ID numérico de la variación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Estructura de variación descrita para la consulta del ítem.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar variaciones del inmueble

**Método:** `GET`  
**Ruta:** `/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Solicita el ítem con attributes=variations.

**Parámetros**

- `ITEM_ID` (path, obligatorio): ID del ítem.
- `attributes` (query, obligatorio): La guía usa variations.

**Solicitud**

No documentado en la fuente.

**Respuesta**

variations[], item_relations[] y campos como attribute_combinations, available_quantity, sold_quantity, price, sale_terms y picture_ids.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/variaciones-para-inmuebles](https://developers.mercadolibre.com.co/es_co/variaciones-para-inmuebles)  
**Captura:** 2026-10-08T22:50:52.096Z

---
