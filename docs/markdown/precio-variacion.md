---
id: "precio-variacion"
title: "Precio por variación"
section: "Guía para productos"
subsection: "User Products"
url: "https://developers.mercadolibre.com.co/es_co/precio-variacion"
source_updated_at: "13/08/2026"
captured_at: "2026-10-08T22:52:28.176Z"
sha256: "78237bef3ea02d27fdb57a97f22ef8cace960fa96976af0a8ca6cc2608197844"
---

# Precio por variación

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/08/2026  
**Captura:** 2026-10-08T22:52:28.176Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/precio-variacion](https://developers.mercadolibre.com.co/es_co/precio-variacion)

## Resumen

Describe la migración al modelo User Products, donde las condiciones de venta y los ítems de una misma familia se gestionan como productos relacionados. La activación es gradual; los vendedores nuevos se identifican por user_product_seller. La guía incluye publicación, edición de familias y variantes, consulta y migración de publicaciones antiguas.

## Contenido y conceptos documentados

- En el modelo nuevo, family_name es obligatorio al publicar; title se genera y no debe enviarse. El array variations deja de ser la representación de variantes y aparecen family_id y user_product_id. Cada User Product admite hasta 30 condiciones de venta (ítems).
- Las variantes comparten atributos parent PK; child PK identifican variaciones. La edición de familia separa common_content compartido y atributos específicos por user_product. Las tareas de edición de familia/variantes se procesan de forma asíncrona; hay que incluir todos los productos existentes de la familia cuando se actualizan variantes.
- Agregar una variante requiere todos los child PKs de la familia e imágenes; PARENT_PK, family_name y domain_id no se envían en esa operación. Actualizar familia admite family_name, domain_id y atributos parent PK/ITEM_CONDITION; KIT no es compatible con el recurso de actualización de familia.
- Para agregar una condición de venta a User Product se envían precio, categoría, moneda, modo de compra y tipo de publicación. title, domain_id, family_name, imágenes, atributos y stock se heredan/generan; no deben enviarse.
- UPtin migra cada variación a un nuevo ítem de manera asíncrona; se valida elegibilidad, se inicia una migración por ítem y se consulta su estado. El ítem origen permanece activo durante el proceso y luego se cierra.

En los ejemplos de la fuente se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar estado de migración

**Método:** `GET`  
**Ruta:** `/items/{item_original}/migration_live_listing`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el progreso y los nuevos ítems creados por la migración.

**Parámetros**

- `item_original` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

item_id, migration_completed, activation_completed, date_created, last_updated y new_items[] con new_item_id, variation_id, migration_status.

**Errores documentados**

- 200: consulta; 404: no fue posible realizar la migración.

**Ejemplos**

- Estados de migración pending/created.

### Validar elegibilidad de migración UPtin

**Método:** `GET`  
**Ruta:** `/items/{item_original}/user_product_listings/validate`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Determina si un ítem antiguo puede migrarse al formato User Products.

**Parámetros**

- `item_original` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

is_valid y cause[] con code, message y reference.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Elegibilidad requiere user_product_id, item multivariante y que no exista duplicado.

### Consultar productos de una familia por sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/user-products-families/{family_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve User Products asociados a la familia y el sitio.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `family_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

user_products_ids, family_id, site_id y user_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo para site MLA.

### Consultar familia

**Método:** `GET`  
**Ruta:** `/user-products-families/{family_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lee datos compartidos de la familia y sus atributos.

**Parámetros**

- `family_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

family_id, family_name, user_id, domain_id, attributes, child_attributes_ids y custom_attributes_names.

**Errores documentados**

- 200: OK; 404: no existe family_id.

**Ejemplos**

- Respuesta con BRAND, MODEL e ITEM_CONDITION.

### Listar variantes de familia

**Método:** `GET`  
**Ruta:** `/user-products-families/{family_id}/user-products`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve User Product IDs de la familia.

**Parámetros**

- `family_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

family_id y user_products_ids.

**Errores documentados**

- 200: OK; 404: no hay asociación para family_id.

**Ejemplos**

- Se recomienda consultar antes del PUT de variantes.

### Consultar tarea de familia

**Método:** `GET`  
**Ruta:** `/user-products-families/tasks/{task_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera estado y resultado por producto de una tarea asíncrona.

**Parámetros**

- `task_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

task_id, status, user-products[] con id, status, processed_date, last_updated y reasons.

**Errores documentados**

- 200: consulta; 404: Task not found.

**Ejemplos**

- Respuesta con productos succeeded, pending o failed.

### Consultar User Product

**Método:** `GET`  
**Ruta:** `/user-products/{user_product_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalle del producto, atributos, imágenes y familia.

**Parámetros**

- `user_product_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, user_id, domain_id, attributes, pictures, thumbnail, catalog_product_id, family_id, tags y fechas.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de User Product con memoria y condición.

### Buscar ítems asociados a User Product

**Método:** `GET`  
**Ruta:** `/users/{seller_id}/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Filtra ítems del vendedor mediante user_product_id.

**Parámetros**

- `seller_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `user_product_id` (query, obligatorio): Identificador del User Product.

**Solicitud**

No documentado en la fuente.

**Respuesta**

seller_id, results y paging.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de búsqueda por user_product_id.

### Consultar activación de User Products

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Comprueba el tag user_product_seller que identifica vendedores encendidos.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id y tags del usuario.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta con user_product_seller.

### Publicar ítem en modelo User Products

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una publicación con family_name; la plataforma genera title y user_product_id.

**Parámetros**

- `family_name` (body, obligatorio): Nombre genérico de la familia.
- `category_id` (body, obligatorio): Categoría del producto.
- `price` (body, obligatorio): Precio; puede diferir por condición de venta.
- `currency_id` (body, obligatorio): Moneda.
- `available_quantity` (body, obligatorio): Stock inicial.
- `attributes` (body, obligatorio): Atributos de familia/variante.

**Solicitud**

Datos de ítem: family_name, category_id, price, currency_id, available_quantity, sale_terms, buying_mode, listing_type_id, condition, pictures y attributes. No enviar title.

**Respuesta**

Ítem con title generado, family_name, user_product_id y datos de publicación.

**Errores documentados**

- 400: el modelo anterior de publicación no es aceptado tras activar el seller.

**Ejemplos**

- Ejemplos de dos ítems de distinto color agrupados por family_name.

### Iniciar migración UPtin

**Método:** `POST`  
**Ruta:** `/sites/{site_id}/items/user_product_listings`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Solicita migración de un ítem antiguo; se realiza de forma asíncrona.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `item_id` (body, obligatorio): Ítem origen que se migrará.

**Solicitud**

item_id.

**Respuesta**

200 OK; inicio del proceso asíncrono.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Un POST por cada ítem a migrar.

### Actualizar datos de familia y variantes mediante tarea

**Método:** `POST`  
**Ruta:** `/user-products-families/{family_id}/tasks`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Envía common_content y atributos por User Product en una tarea asíncrona.

**Parámetros**

- `family_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `common_content` (body, opcional): family_name, domain_id y atributos compartidos.
- `user_products` (body, obligatorio): Debe incluir todos los User Products existentes.
- `attributes` (body, obligatorio): Atributos diferenciados por cada producto.

**Solicitud**

common_content compartido y user_products[] con id y attributes. Incluir todos los User Products de la familia; no duplicar atributos entre niveles.

**Respuesta**

task_id, status y date_created.

**Errores documentados**

- 202: tarea aceptada; 400: formato, campos faltantes o producto ajeno a familia; 401: token; 404: familia inexistente.
- Errores de tarea incluyen fields.to_update.missing, user_products.null/incomplete, atributos faltantes o duplicados y conflicto entre common_content y atributos del producto.
- cause_id 31 fields.to_update.missing: no se enviaron cambios.
- cause_id 32 common_content.family_name.null: family_name no puede ser null.
- cause_id 33 common_content.domain_id.null: domain_id no puede ser null.
- cause_id 34 common_content.attributes.null: attributes compartidos no pueden ser null.
- cause_id 35 user_products.null: el array no puede ser null ni vacío.
- cause_id 36 user_products.id.null: falta id en user_products.
- cause_id 37 user_products.attributes.null: attributes por producto no pueden ser null.
- cause_id 38 user_products.incomplete: faltan productos de la familia.
- cause_id 39 user_products.family_not_exist: familia inexistente.
- cause_id 40 user_products.attribute_id.missing: falta attribute_id.
- cause_id 41 user_products.attribute_name.missing: falta attribute_name.
- cause_id 42 user_products.attribute_values.missing: faltan values del atributo.
- cause_id 43 user_products.attribute_value_id.missing: falta value_id.
- cause_id 44 user_products.attribute_value_name.missing: falta value_name.
- cause_id 45 user_products.duplicated_attribute: atributo duplicado en un producto.
- cause_id 46 user_products.update.failed: fallo inesperado en la actualización.
- cause_id 47 user_products.miss_match_attribute: child PK/custom no enviado a todos los productos cuando corresponde.
- cause_id 48 user_products.duplicated_attribute.by_common_content_and_by_user_product: atributo duplicado entre common_content y producto.
- cause_id 51 user_products.attributes.number_unit: unidad en value_name incorrecta.
- cause_id 55 family_id.collision: actualización produciría una familia ya mapeada.

**Ejemplos**

- Ejemplo con atributos comunes y atributos específicos por producto.

### Agregar variante a familia

**Método:** `POST`  
**Ruta:** `/user-products-families/{family_id}/user-products`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una variante dentro de una familia existente sin cambiar family_id.

**Parámetros**

- `family_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `attributes` (body, obligatorio): Todos los child PKs de la familia; no enviar parent PK ni domain_id.
- `pictures` (body, obligatorio): Al menos una imagen.
- `main_features` (body, opcional): Características; origin se envía en minúscula seller.

**Solicitud**

attributes con todos los child PKs; pictures con al menos una imagen; main_features opcional.

**Respuesta**

User Product con id, name, family_name, domain_id, attributes, pictures, family_id y main_features.

**Errores documentados**

- 201: creada; 400: falta campo/child PK, parent PK o campos no permitidos; 401: token; 404: familia inexistente.

**Ejemplos**

- Ejemplo de variante con COLOR y SIZE.

### Agregar condición de venta

**Método:** `POST`  
**Ruta:** `/user-products/{user_product_id}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea un ítem/publicación que representa una condición de venta del User Product.

**Parámetros**

- `user_product_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `price` (body, obligatorio): Precio.
- `category_id` (body, obligatorio): Categoría.
- `currency_id` (body, obligatorio): Moneda.
- `buying_mode` (body, obligatorio): buy_it_now en ejemplo.
- `listing_type_id` (body, obligatorio): Tipo de publicación.
- `catalog_product_id` (body, opcional): Solo si catalog_listing=true.

**Solicitud**

price, category_id, currency_id, buying_mode y listing_type_id requeridos; shipping, channels, tags, sale_terms, catalog_listing, catalog_product_id y official_store_id opcionales/condicionales.

**Respuesta**

HTTP 201 con el ítem y user_product_id/family_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos básicos, de catálogo y con campos opcionales.

### Editar atributos de ítem asociado

**Método:** `PUT`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La guía indica continuar actualizando ítems mediante PUT /items; cambios en atributos compartidos se replican al User Product de forma asíncrona.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente enumera atributos sincronizables como family_name, domain_id, catalog_product_id, pictures y tags.

### Actualizar datos comunes de familia

**Método:** `PUT`  
**Ruta:** `/user-products-families/{family_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza family_name, domain_id y atributos parent PK/ITEM_CONDITION; los productos se replican después de forma asíncrona.

**Parámetros**

- `family_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `family_name` (body, opcional): No puede ser null ni vacío.
- `domain_id` (body, opcional): No puede ser null.
- `attributes` (body, opcional): Atributos parent PK o ITEM_CONDITION; no admite custom.

**Solicitud**

family_name, domain_id y/o attributes de tipo PARENT_PK o ITEM_CONDITION.

**Respuesta**

201 con family_id, family_name, domain_id, attributes, child_attributes_ids y custom_attributes_names.

**Errores documentados**

- 400: payload vacío, nombre inválido, atributo custom/duplicado o ITEM_CONDITION vacío; 403: caller no coincide con dueño; 404: familia inexistente/sin productos; 409: bloqueada o hash de otra familia.

**Ejemplos**

- La semántica de values permite conservar, eliminar o modificar atributos según esté ausente, vacío o contenga valores.

### Actualizar variantes de familia

**Método:** `PUT`  
**Ruta:** `/user-products-families/{family_id}/user-products`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica, agrega o elimina atributos child PK/custom para las variantes; procesamiento asíncrono.

**Parámetros**

- `family_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `user_products` (body, obligatorio): Debe incluir todas las variantes existentes.
- `attributes` (body, obligatorio): Atributos child PK o custom, con name en cada objeto.

**Solicitud**

user_products[] con id y attributes[]; todos los productos de familia y cada atributo con name. No enviar parent PK, family_name, domain_id ni ITEM_CONDITION.

**Respuesta**

202 con task_id, status pending y date_created.

**Errores documentados**

- 400: campos faltantes o atributos no permitidos; 401: token; 404: familia inexistente. La tarea puede reportar user_products.incomplete.

**Ejemplos**

- Ejemplo de actualización de COLOR/SIZE con task_id.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/precio-variacion](https://developers.mercadolibre.com.co/es_co/precio-variacion)  
**Captura:** 2026-10-08T22:52:28.176Z
