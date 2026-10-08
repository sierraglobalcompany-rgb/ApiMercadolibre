---
id: "usuarios-y-aplicaciones"
title: "Usuarios y Aplicaciones"
section: "Recursos de la API"
subsection: "Usuarios"
url: "https://developers.mercadolibre.com.co/es_co/usuarios-y-aplicaciones"
source_updated_at: "30/12/2025"
captured_at: "2026-10-08T22:54:02.190Z"
sha256: "ef8fa5bc5e51719772fe29e48fe67c179da1fccafd023d52579f52ceda2e9489"
---

# Usuarios y Aplicaciones

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:54:02.190Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/usuarios-y-aplicaciones](https://developers.mercadolibre.com.co/es_co/usuarios-y-aplicaciones)

## Resumen

Documenta recursos para consultar y actualizar usuarios, direcciones, métodos de pago, marcas, tipos de publicación, aplicaciones y notificaciones.

## Contenido y conceptos documentados

- /users/{user_id} incluye perfil, contacto, estado y reputación; /users/me devuelve información del usuario autenticado y /addresses detalla direcciones.
- Los métodos aceptados por un usuario se consultan separadamente. Las marcas pueden incluir official_store_id; los paquetes y recursos available_listing_types describen disponibilidad de tipos promocionales por usuario/categoría.
- También se consultan detalles de aplicación, se revocan permisos y se recupera missed_feeds por app_id. La tabla de recursos incluye GET y POST para paquetes promocionales, pero solo detalla una consulta GET.

## Operaciones de API
## Operaciones de API

### Revocar permisos de aplicación

**Método:** `DELETE`  
**Ruta:** `/users/{user_id}/applications/{application_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Revoca permisos otorgados por el usuario a una aplicación.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario/cust_id.
- `application_id` (path, obligatorio): ID de aplicación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- DELETE /users/{cust_Id}/applications/{app_id}.

### Consultar aplicación

**Método:** `GET`  
**Ruta:** `/applications/{application_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve datos de una aplicación registrada.

**Parámetros**

- `application_id` (path, obligatorio): ID de la aplicación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo incluye id, site_id, name, description, owner_id, need_authorization, short_name, url, callback_url, sandbox_mode, is_public, active, max_requests_per_hour, scopes y domains.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /applications/3022782903258037.

### Consultar notificaciones no recibidas

**Método:** `GET`  
**Ruta:** `/missed_feeds`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el histórico de notificaciones perdidas para una aplicación.

**Parámetros**

- `app_id` (query, obligatorio): ID de aplicación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /missed_feeds?app_id=$APP_ID.

### Consultar usuario autenticado

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve información asociada al usuario conectado a la cuenta.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo de dirección asociada con user_id, contact, phone, address_line, street_number/name, zip_code, city, state, country y otros datos.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/me.

### Consultar usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve el perfil, datos de contacto, dirección, reputación y estado del usuario.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con id, nickname, datos personales, país, email/teléfono, address, user_type, tags, seller_reputation, buyer_reputation, status y credit.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/{User_id}.

### Consultar métodos de pago aceptados por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/accepted_payment_methods`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista métodos de pago aceptados por el vendedor.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Métodos con id, name, payment_type_id, thumbnail y secure_thumbnail.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/206946886/accepted_payment_methods.

### Consultar direcciones de usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/addresses`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve direcciones asociadas al usuario.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con id, user_id, contact, phone, address_line, street_number/name, zip_code, city, state, country y open_hours.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/206946886/addresses.

### Consultar tipo de publicación para categoría

**Método:** `GET`  
**Ruta:** `/users/{user_id}/available_listing_type/{listing_type_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Determina si un tipo de listado está disponible en una categoría para el usuario.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario.
- `listing_type_id` (path, obligatorio): Tipo de publicación.
- `category_id` (query, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

available, cause, code y mapping.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/206946886/available_listing_type/gold_special?category_id=MLA6602.

### Consultar tipos de publicación disponibles

**Método:** `GET`  
**Ruta:** `/users/{user_id}/available_listing_types`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve tipos de publicación disponibles para usuario y, según categoría, sus excepciones.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario.
- `category_id` (query, opcional): La tabla indica filtro por categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

available y exceptions_by_category; cada tipo incluye site_id, id, name, remaining_listings y mapping.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/206946886/available_listing_types.

### Consultar marcas de usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/brands`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera marcas vinculadas a un usuario; official_store_id identifica tienda.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo contiene cust_id, tags y brands con name, status, site_id, categories_ids, official_store_id, tags y pictures.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/12345678/brands.

### Listar paquetes de promoción del usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/classifieds_promotion_packs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta paquetes promocionales asociados al usuario.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con id, user_id, promotion_pack_id, category_id, description, package_type, status y fechas.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/135146148/classifieds_promotion_packs.

### Consultar paquete habilitado por tipo y categoría

**Método:** `GET`  
**Ruta:** `/users/{user_id}/classifieds_promotion_packs/{listing_type_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Indica si un usuario tiene publicaciones disponibles para un tipo de listado y categoría.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.
- `listing_type_id` (path, obligatorio): Tipo de listado.
- `categoryId` (query, obligatorio): ID de categoría; la captura usa camelCase.

**Solicitud**

No documentado en la fuente.

**Respuesta**

has_available_listings boolean.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/206946886/classifieds_promotion_packs/silver?categoryId=MLA1459.

### Operación POST de paquetes promocionales

**Método:** `POST`  
**Ruta:** `/users/{user_id}/classifieds_promotion_packs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La tabla de recursos también enumera POST para classifieds_promotion_packs, pero la captura no especifica su cuerpo ni comportamiento.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El recurso aparece con métodos GET y POST; el ejemplo detallado de la captura es GET.

### Actualizar usuario

**Método:** `PUT`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza datos del usuario, incluidos dirección, teléfono y datos personales/empresariales ilustrados en la fuente.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.
- `Content-Type` (header, obligatorio): application/json.

**Solicitud**

Ejemplo JSON con address, state, city, zip_dode (tal como aparece escrito en la captura), phone, first_name, last_name, company y mercadoenvios.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- PUT /users/123456789 con campos de perfil.

### Referencia HTTP GET /users/206946886/available_listing_type/gold_special

**Método:** `GET`  
**Ruta:** `/users/206946886/available_listing_type/gold_special`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/206946886/available_listing_type/gold_special. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

- `category_id` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

### Referencia HTTP GET /users/206946886/classifieds_promotion_packs/silver

**Método:** `GET`  
**Ruta:** `/users/206946886/classifieds_promotion_packs/silver`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/206946886/classifieds_promotion_packs/silver. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

- `categoryId` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/usuarios-y-aplicaciones](https://developers.mercadolibre.com.co/es_co/usuarios-y-aplicaciones)  
**Captura:** 2026-10-08T22:54:02.190Z
