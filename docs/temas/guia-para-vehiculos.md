# Guía para vehículos

11 páginas del portal oficial en esta área.

## [Calidad de publicaciones (vehículos)](../markdown/calidad-de-publicaciones-vehiculos.md)

Actualización indicada por la fuente: 19/06/2026. Captura: 2026-10-08T22:53:11.313Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones-vehiculos](https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones-vehiculos)

# Calidad de publicaciones (vehículos)

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 19/06/2026  
**Captura:** 2026-10-08T22:53:11.313Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones-vehiculos](https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones-vehiculos)

## Resumen

Describe consultas para conocer la puntuación de calidad vehicular, nivel y acciones pendientes que pueden elevar la exposición.

## Contenido y conceptos documentados

- Los rangos por sitio usan level, health_min y health_max. /health calcula la puntuación a partir de objetivos aplicables y devuelve goals con progress, progress_max, apply, completed y data. technical_specification puede indicar atributos faltantes.
- /health/actions presenta acciones pendientes. La fuente nombra picture, price, technical_specification, video, upgrade_listing y publish; indica que whatsapp ya no se contabiliza como objetivo de calidad aunque aún puede beneficiar conversiones.

## Operaciones de API
## Operaciones de API

### Consultar calidad de un ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}/health`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve puntuación, nivel y progreso de los objetivos de calidad aplicables.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

item_id, health, level y goals; cada objetivo puede contener progress, progress_max, id, name, apply, completed y data.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /items/MLM735814032/health.

### Consultar acciones para mejorar calidad

**Método:** `GET`  
**Ruta:** `/items/{item_id}/health/actions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista tareas pendientes que pueden mejorar el nivel/exposición de la publicación.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

item_id, health y actions con id/name.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /items/MLM735814032/health/actions.

### Consultar niveles de calidad por sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/health_levels`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene rangos de puntaje para niveles de calidad en un sitio.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de level, health_min y health_max; ejemplo basic, standard y professional.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLB/health_levels.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones-vehiculos](https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones-vehiculos)  
**Captura:** 2026-10-08T22:53:11.313Z

---

## [Categorías y Atributos](../markdown/categorias-y-atributos.md)

Actualización indicada por la fuente: 02/04/2025. Captura: 2026-10-08T22:53:12.316Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/categorias-y-atributos](https://developers.mercadolibre.com.co/es_co/categorias-y-atributos)

# Categorías y Atributos

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 02/04/2025  
**Captura:** 2026-10-08T22:53:12.316Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/categorias-y-atributos](https://developers.mercadolibre.com.co/es_co/categorias-y-atributos)

## Resumen

Explica cómo elegir categorías y consultar atributos para estructurar publicaciones, con ejemplos para vehículos y dominios.

## Contenido y conceptos documentados

- Cada sitio tiene su propio árbol. La página recomienda predictor; category details incluye path_from_root y children_categories, mientras attributes lista campos requeridos y valores posibles.
- domain_discovery/search sugiere dominio/categoría según q; se documenta limit de 1 a 8 y target core o classified según vertical.
- top_values entrega valores populares; limit admite hasta 1000 y la métrica enumerada es NOL_90. known_attributes permite condicionar valores relacionados.
- categories/all descarga JSON gzip; X-Content-Created y X-Content-MD5 informan fecha y checksum. catalog_domains/{domain_id}/categories relaciona un dominio con sus categorías.

## Operaciones de API
## Operaciones de API

### Convertir dominio a categorías

**Método:** `GET`  
**Ruta:** `/catalog_domains/{domain_id}/categories`  
**Autenticación:** No documentado en la fuente.

Obtiene categorías de un dominio de catálogo.

**Parámetros**

- `domain_id` (path, obligatorio): ID de dominio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de id y name.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /catalog_domains/MLB-CARS_AND_VANS/categories.

### Consultar categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}`  
**Autenticación:** No documentado en la fuente.

Devuelve detalle, camino desde la raíz y categorías hijas.

**Parámetros**

- `category_id` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con id, name, picture, permalink, total_items_in_this_category, path_from_root, children_categories y settings.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /categories/MLA1743 y /categories/MLA1744.

### Consultar atributos de categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/attributes`  
**Autenticación:** No documentado en la fuente.

Devuelve atributos específicos y valores permitidos para publicar en una categoría.

**Parámetros**

- `category_id` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Atributos con id, name, tags, hierarchy, value_type y values; BRAND aparece como catalog_required/required en el ejemplo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /categories/MLA1744/attributes.

### Listar categorías del sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/categories`  
**Autenticación:** No documentado en la fuente.

Devuelve categorías del país/sitio.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista con id y name.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/categories.

### Descargar árbol completo de categorías

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/categories/all`  
**Autenticación:** No documentado en la fuente.

Devuelve volcado del árbol de categorías codificado como gzip.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

JSON comprimido con gzip; X-Content-Created y X-Content-MD5 informan generación y suma de verificación.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/categories/all.

### Buscar dominio y categoría sugeridos

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/domain_discovery/search`  
**Autenticación:** No documentado en la fuente.

Predice dominios/categorías para un término de búsqueda.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.
- `q` (query, obligatorio): Texto del producto.
- `limit` (query, opcional): La fuente señala rango de 1 a 8.
- `target` (query, opcional): core o classified según la vertical; se describe en la página.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Resultados con domain_id, domain_name, category_id, category_name y attributes.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/domain_discovery/search?limit=1&q=fiat%20uno.

### Consultar valores populares de atributo

**Método:** `POST`  
**Ruta:** `/catalog_domains/{domain_id}/attributes/{attribute_id}/top_values`  
**Autenticación:** No documentado en la fuente.

Devuelve valores frecuentes de un atributo de dominio, opcionalmente condicionados por otros atributos conocidos.

**Parámetros**

- `domain_id` (path, obligatorio): ID de dominio.
- `attribute_id` (path, obligatorio): ID de atributo.
- `limit` (query, opcional): Máximo 1000.
- `metric_type` (query, opcional): Métrica documentada NOL_90, nuevas publicaciones de los últimos 90 días.

**Solicitud**

Opcional: known_attributes como lista de id y value_id.

**Respuesta**

Array de id, name y metric.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- POST con BRAND; otro ejemplo consulta MODEL con known_attributes de BRAND.

### Referencia HTTP POST /catalog_domains/MLA-CARS_AND_VANS/attributes/BRAND/top_values

**Método:** `POST`  
**Ruta:** `/catalog_domains/MLA-CARS_AND_VANS/attributes/BRAND/top_values`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /catalog_domains/MLA-CARS_AND_VANS/attributes/BRAND/top_values. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP POST /catalog_domains/MLA-CARS_AND_VANS/attributes/MODEL/top_values

**Método:** `POST`  
**Ruta:** `/catalog_domains/MLA-CARS_AND_VANS/attributes/MODEL/top_values`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /catalog_domains/MLA-CARS_AND_VANS/attributes/MODEL/top_values. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/categorias-y-atributos](https://developers.mercadolibre.com.co/es_co/categorias-y-atributos)  
**Captura:** 2026-10-08T22:53:12.316Z

---

## [Consulta Usuarios](../markdown/consulta-usuarios.md)

Actualización indicada por la fuente: 12/01/2026. Captura: 2026-10-08T22:53:13.564Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/consulta-usuarios](https://developers.mercadolibre.com.co/es_co/consulta-usuarios)

# Consulta Usuarios

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 12/01/2026  
**Captura:** 2026-10-08T22:53:13.564Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/consulta-usuarios](https://developers.mercadolibre.com.co/es_co/consulta-usuarios)

## Resumen

La página explica cómo consultar datos propios, públicos y privados de usuarios, consultar bloqueos de compradores y gestionar preferencias de pago inmediato y listas de bloqueo. Los recursos de usuario pueden devolver HTTP 206 cuando algunos datos no estén disponibles; en ese caso la respuesta queda incompleta.

## Contenido y conceptos documentados

- `GET /users/me` consulta el perfil propio. `GET /users/{USER_ID}` sirve para información pública y, con autorización del usuario, privada; los ejemplos incluyen identidad, dirección, reputación y estado.
- El endpoint unificado de bloqueos admite `type=blocked_by_questions` o `blocked_by_order`. `caller.id` y `type` son obligatorios; `client.id` y `user_blocked` opcionales; `offset` predeterminado 0 y `limit` predeterminado 10, máximo 1000. Respuesta: `users.id`, `users.blocked_at` y `paging`.
- Para aceptar solo Mercado Pago se envía `reason=by_user`; la eliminación revierte la marca. También se documenta borrar un bloqueo de órdenes y agregar un usuario a la lista negra de preguntas. Autenticación mostrada: `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### DELETE /users/{USER_ID}/immediate_payment/by_user

**Método:** `DELETE`  
**Ruta:** `/users/{USER_ID}/immediate_payment/by_user`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la marca de pago inmediato `by_user`.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### DELETE /users/{YOUR_CUST_ID}/order_blacklist/{SELLER_ID}

**Método:** `DELETE`  
**Ruta:** `/users/{YOUR_CUST_ID}/order_blacklist/{SELLER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina un usuario bloqueado para órdenes.

**Parámetros**

- `YOUR_CUST_ID` (path, obligatorio)
- `SELLER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /block-api/search/users/{USER_ID}

**Método:** `GET`  
**Ruta:** `/block-api/search/users/{USER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta bloqueos de un comprador por preguntas u órdenes.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `type` (query, obligatorio): blocked_by_questions o blocked_by_order
- `caller.id` (query, obligatorio): Usuario que consulta
- `client.id` (query, opcional): ID cliente
- `user_blocked` (query, opcional): ID comprador bloqueado
- `offset` (query, opcional): Predeterminado 0
- `limit` (query, opcional): Predeterminado 10, máximo 1000

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "users.id",
    "users.blocked_at",
    "paging.offset",
    "paging.limit",
    "paging.total"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/me

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta los datos del usuario autenticado.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta datos públicos o, con autorización, privados del usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### POST /users/{SELLER_ID}/questions_blacklist

**Método:** `POST`  
**Ruta:** `/users/{SELLER_ID}/questions_blacklist`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega un usuario a la lista de bloqueo de preguntas.

**Parámetros**

- `SELLER_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "user_id"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### PUT /users/{USER_ID}/immediate_payment

**Método:** `PUT`  
**Ruta:** `/users/{USER_ID}/immediate_payment`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Configura el pago inmediato; ejemplo con `reason=by_user`.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "reason"
  ],
  "example": "by_user"
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/consulta-usuarios](https://developers.mercadolibre.com.co/es_co/consulta-usuarios)  
**Captura:** 2026-10-08T22:53:13.564Z

---

## [Créditos pre aprobados](../markdown/credits-motors.md)

Actualización indicada por la fuente: 15/03/2023. Captura: 2026-10-08T22:53:14.542Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/credits-motors](https://developers.mercadolibre.com.co/es_co/credits-motors)

# Créditos pre aprobados

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 15/03/2023  
**Captura:** 2026-10-08T22:53:14.542Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/credits-motors](https://developers.mercadolibre.com.co/es_co/credits-motors)

## Resumen

Describe las notificaciones de nuevos leads de crédito, la consulta de créditos disponibles para ítems del vendedor y el detalle de una propuesta. La funcionalidad aplica a vehículos en Brasil e inmuebles en Chile.

## Contenido y conceptos documentados

- La búsqueda puede filtrar por `item_id`, `status` (`approved`, `rejected`, `in_analysis`, `all`) y `financial_entity_id` (`MERCADO_PAGO`, `VOTORANTIM`, `SANTANDER`, `SCOTIA`). Si no se indica status, la fuente indica que devuelve los aprobados.
- El resumen incluye `id`, `item_id`, anticipo y cuotas, seller/buyer, entidad, fecha y `expired`; `proposal_id` depende de que la entidad financiera lo publique. El detalle puede incluir `buyer.full_name`, email y teléfono.
- Para datos de prueba se documenta `x-sandbox: true`. Errores incluyen 401 sin token y 400 por seller distinto al token, fechas inválidas/rango mayor a tres meses, entidad o ítem inválidos.

## Operaciones de API
## Operaciones de API

### GET /vis/loans/{CREDIT_ID}

**Método:** `GET`  
**Ruta:** `/vis/loans/{CREDIT_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el detalle del crédito y los datos de contacto disponibles del comprador.

**Parámetros**

- `CREDIT_ID` (path, obligatorio)
- `seller_id` (query, obligatorio): Vendedor del token

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "item_id",
    "buyer.id",
    "buyer.full_name",
    "buyer.email",
    "buyer.phone",
    "status"
  ]
}
```

**Errores documentados**

- ```json {   "code": "401",   "meaning": "Unauthorized: falta access token." } ```
- ```json {   "code": "400",   "meaning": "Seller no coincide con el token o CREDIT_ID no tiene formato UUID." } ```
- ```json {   "code": "404",   "meaning": "No se encontró el detalle del crédito." } ```
- ```json {   "code": "410",   "meaning": "El crédito expiró." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /vis/loans/search

**Método:** `GET`  
**Ruta:** `/vis/loans/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca créditos disponibles para los ítems del vendedor.

**Parámetros**

- `seller_id` (query, obligatorio): ID vendedor
- `date_from` (query, obligatorio): Fecha inicial ISO
- `date_to` (query, obligatorio): Fecha final ISO; rango máximo tres meses
- `item_id` (query, opcional): Ítem
- `status` (query, opcional): approved, rejected, in_analysis o all; default approved
- `financial_entity_id` (query, opcional): MERCADO_PAGO, VOTORANTIM, SANTANDER o SCOTIA

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "results",
    "id",
    "item_id",
    "down_payment_amount",
    "installments_number",
    "installments_amount",
    "seller_id",
    "buyer_id",
    "proposal_id",
    "date_created",
    "financial_entity_id",
    "expired",
    "paging"
  ]
}
```

**Errores documentados**

- ```json {   "code": "401",   "meaning": "Unauthorized: falta access token." } ```
- ```json {   "code": "400",   "meaning": "Seller no coincide con el token; fecha inválida o rango mayor a tres meses; entidad financiera o item inválidos." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/credits-motors](https://developers.mercadolibre.com.co/es_co/credits-motors)  
**Captura:** 2026-10-08T22:53:14.542Z

---

## [Gestiona paquetes de vehículos](../markdown/vehiculos-gestiona-paquetes.md)

Actualización indicada por la fuente: 24/11/2025. Captura: 2026-10-08T22:53:15.479Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-paquetes](https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-paquetes)

# Gestiona paquetes de vehículos

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 24/11/2025  
**Captura:** 2026-10-08T22:53:15.479Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-paquetes](https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-paquetes)

## Resumen

Explica la consulta de paquetes de publicación y destacados para categorías y usuarios, la disponibilidad de cupos y la actualización del listing type de un anuncio. También describe el nuevo modelo de paquetes para MLM y MCO.

## Contenido y conceptos documentados

- `package_content` es opcional, predeterminado `publications`; valores: `publications`, `upgrades` y `ALL`. Los paquetes incluyen identificadores, categoría, descripción, tipo, estado y fechas.
- Los estados descritos son activo, pendiente y finalizado. Los paquetes pueden ser mensuales o trimestrales; un paquete activado no se pausa, aunque puede inactivarse un destaque para liberar cupo. En MLM y MCO se separan suscripción y destacado; `gold` se presenta como Acelerador y `gold_premium` como Acelerador Plus.
- Para consultar disponibilidad se usa `categoryId` y `upgrades=true` al consultar cupos de upgrades. Para destacar, el vendedor debe haber contratado un paquete y enviar el listing type deseado.

## Operaciones de API
## Operaciones de API

### GET /categories/{CATEGORY_ID}/classifieds_promotion_packs

**Método:** `GET`  
**Ruta:** `/categories/{CATEGORY_ID}/classifieds_promotion_packs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta paquetes disponibles para una categoría; admite `package_content`.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio)
- `package_content` (query, opcional): publications, upgrades o ALL; default publications

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}/classifieds_promotion_packs

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/classifieds_promotion_packs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta paquetes contratados por un usuario; admite `package_content`.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `package_content` (query, opcional): publications, upgrades o ALL; default publications

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}/classifieds_promotion_packs/{LISTING_TYPE}/available

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/classifieds_promotion_packs/{LISTING_TYPE}/available`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta si hay publicaciones disponibles en el tipo indicado.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `LISTING_TYPE` (path, obligatorio)
- `categoryId` (query, obligatorio): Categoría
- `upgrades` (query, opcional): true para consultar upgrades

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "has_available_listings"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### POST /items/{ITEM_ID}/listing_type

**Método:** `POST`  
**Ruta:** `/items/{ITEM_ID}/listing_type`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza el tipo de publicación; el ejemplo envía `id=gold_premium`.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "id"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### Referencia HTTP GET /users/123456789/classifieds_promotion_packs/gold_premium/available

**Método:** `GET`  
**Ruta:** `/users/123456789/classifieds_promotion_packs/gold_premium/available`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/123456789/classifieds_promotion_packs/gold_premium/available. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

- `categoryId` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.
- `upgrades` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-paquetes](https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-paquetes)  
**Captura:** 2026-10-08T22:53:15.479Z

---

## [Gestiona preguntas y contactos](../markdown/vehiculos-gestiona-preguntas-y-contactos.md)

Actualización indicada por la fuente: 20/01/2026. Captura: 2026-10-08T22:53:16.353Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-preguntas-y-contactos](https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-preguntas-y-contactos)

# Gestiona preguntas y contactos

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 20/01/2026  
**Captura:** 2026-10-08T22:53:16.353Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-preguntas-y-contactos](https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-preguntas-y-contactos)

## Resumen

Documenta métricas de preguntas, visualizaciones de teléfono y clics de WhatsApp por publicación o usuario, con consultas en rangos de fechas y ventanas agregadas por hora o día.

## Contenido y conceptos documentados

- Las consultas por fechas usan `date_from` y `date_to` en formato ISO. Para ventanas se usan `last` y `unit` (`day` o `hour`); `ending` fija el fin y, para varios ítems, `ids` contiene identificadores separados por coma.
- La página ofrece consultas por `ITEM_ID` y por `USER_ID`; las consultas múltiples usan la ruta de colección `/items/contacts/.../time_window`. Las respuestas muestran total, periodo y el ítem o usuario correspondiente.
- La sección de errores documenta HTTP 400 para parámetros inválidos. Para visitas por publicación, la fuente remite al recurso de Visitas. Autenticación mostrada: OAuth Bearer.

## Operaciones de API
## Operaciones de API

### GET /items/contacts/phone_views/time_window

**Método:** `GET`  
**Ruta:** `/items/contacts/phone_views/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta visualizaciones agregadas de varios ítems mediante `ids`.

**Parámetros**

- `ids` (query, obligatorio): IDs separados por coma
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour
- `ending` (query, opcional): Fin de ventana

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/contacts/questions/time_window

**Método:** `GET`  
**Ruta:** `/items/contacts/questions/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta preguntas agregadas para varios ítems mediante `ids`.

**Parámetros**

- `ids` (query, obligatorio): IDs separados por coma
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour
- `ending` (query, opcional): Fin de ventana

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/contacts/whatsapp/time_window

**Método:** `GET`  
**Ruta:** `/items/contacts/whatsapp/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta clics agregados de WhatsApp para varios ítems.

**Parámetros**

- `ids` (query, obligatorio): IDs separados por coma
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour
- `ending` (query, opcional): Fin de ventana

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/{ITEM_ID}/contacts/phone_views

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/contacts/phone_views`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta visualizaciones del teléfono de una publicación por fechas.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `date_from` (query, obligatorio): Inicio del rango ISO
- `date_to` (query, obligatorio): Fin del rango ISO

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/{ITEM_ID}/contacts/phone_views/time_window

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/contacts/phone_views/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta visualizaciones agregadas para una publicación.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/{ITEM_ID}/contacts/questions

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/contacts/questions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta preguntas recibidas por una publicación en un rango de fechas.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `date_from` (query, obligatorio): Inicio del rango ISO
- `date_to` (query, obligatorio): Fin del rango ISO

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/{ITEM_ID}/contacts/questions/time_window

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/contacts/questions/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta preguntas agregadas por ventana para una publicación.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/{ITEM_ID}/contacts/whatsapp

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/contacts/whatsapp`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta clics de WhatsApp de una publicación por fechas.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `date_from` (query, obligatorio): Inicio del rango ISO
- `date_to` (query, obligatorio): Fin del rango ISO

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/{ITEM_ID}/contacts/whatsapp/time_window

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/contacts/whatsapp/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta clics de WhatsApp agregados para una publicación.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}/contacts/phone_views

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/contacts/phone_views`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta visualizaciones de teléfonos de las publicaciones de un usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `date_from` (query, obligatorio): Inicio del rango ISO
- `date_to` (query, obligatorio): Fin del rango ISO

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}/contacts/phone_views/time_window

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/contacts/phone_views/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta visualizaciones agregadas por usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}/contacts/questions

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/contacts/questions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta preguntas de las publicaciones del usuario en un rango de fechas.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `date_from` (query, obligatorio): Inicio del rango ISO
- `date_to` (query, obligatorio): Fin del rango ISO

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}/contacts/questions/time_window

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/contacts/questions/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta preguntas agregadas por ventana para un usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}/contacts/whatsapp/time_window

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/contacts/whatsapp/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta clics de WhatsApp agregados para un usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `last` (query, obligatorio): Cantidad de horas o días
- `unit` (query, obligatorio): day o hour

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Parámetros o fechas inválidas." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-preguntas-y-contactos](https://developers.mercadolibre.com.co/es_co/vehiculos-gestiona-preguntas-y-contactos)  
**Captura:** 2026-10-08T22:53:16.353Z

---

## [Introducción](../markdown/introduccion-vehiculos.md)

Actualización indicada por la fuente: 09/09/2026. Captura: 2026-10-08T22:53:17.228Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/introduccion-vehiculos](https://developers.mercadolibre.com.co/es_co/introduccion-vehiculos)

# Introducción

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 09/09/2026  
**Captura:** 2026-10-08T22:53:17.228Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/introduccion-vehiculos](https://developers.mercadolibre.com.co/es_co/introduccion-vehiculos)

## Resumen

Introduce la guía de integración de vehículos: consultar usuarios, gestionar paquetes, publicar avisos, atender leads y sincronizar publicaciones. También enlaza a configuración inicial, autenticación y usuarios de prueba.

## Contenido y conceptos documentados

- La fuente presenta una ruta de aprendizaje que parte de los primeros pasos y continúa con publicación y gestión de leads. Esta página introductoria no detalla parámetros, cuerpos, respuestas ni errores de API: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Introducción

Introduce la guía de integración de vehículos: consultar usuarios, gestionar paquetes, publicar avisos, atender leads y sincronizar publicaciones. También enlaza a configuración inicial, autenticación y usuarios de prueba.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/introduccion-vehiculos](https://developers.mercadolibre.com.co/es_co/introduccion-vehiculos)  
**Captura:** 2026-10-08T22:53:17.228Z

---

## [Localiza vehículos](../markdown/localizacion-de-vehiculos.md)

Actualización indicada por la fuente: 21/07/2025. Captura: 2026-10-08T22:53:18.230Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/localizacion-de-vehiculos](https://developers.mercadolibre.com.co/es_co/localizacion-de-vehiculos)

# Localiza vehículos

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 21/07/2025  
**Captura:** 2026-10-08T22:53:18.230Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/localizacion-de-vehiculos](https://developers.mercadolibre.com.co/es_co/localizacion-de-vehiculos)

## Resumen

Documenta los recursos de ubicaciones clasificadas para explorar países, estados, ciudades y barrios, y explica qué identificador enviar al publicar un vehículo.

## Contenido y conceptos documentados

- Las ubicaciones se consultan jerárquicamente. En la solicitud de publicación se envía el ID del barrio; si la ciudad no tiene barrios, se envía el ID de ciudad. Al enviar un barrio, la API completa estado y ciudad.
- La lista de países incluye `id`, `name`, `locale` y `currency_id`; los recursos de ubicación incluyen las entidades padre y, para ciudades/barrios, datos geográficos. Autenticación mostrada: OAuth Bearer.

## Operaciones de API
## Operaciones de API

### GET /classified_locations/cities/{CITY_ID}

**Método:** `GET`  
**Ruta:** `/classified_locations/cities/{CITY_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta una ciudad, sus barrios y datos geográficos.

**Parámetros**

- `CITY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /classified_locations/countries

**Método:** `GET`  
**Ruta:** `/classified_locations/countries`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista países habilitados para ubicaciones clasificadas.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /classified_locations/countries/{COUNTRY_ID}

**Método:** `GET`  
**Ruta:** `/classified_locations/countries/{COUNTRY_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta datos de un país.

**Parámetros**

- `COUNTRY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /classified_locations/neighborhoods/{NEIGHBORHOOD_ID}

**Método:** `GET`  
**Ruta:** `/classified_locations/neighborhoods/{NEIGHBORHOOD_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta un barrio y su jerarquía geográfica.

**Parámetros**

- `NEIGHBORHOOD_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /classified_locations/states/{STATE_ID}

**Método:** `GET`  
**Ruta:** `/classified_locations/states/{STATE_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta un estado y sus ciudades.

**Parámetros**

- `STATE_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/localizacion-de-vehiculos](https://developers.mercadolibre.com.co/es_co/localizacion-de-vehiculos)  
**Captura:** 2026-10-08T22:53:18.230Z

---

## [Personas Interesadas](../markdown/persona-interesadas.md)

Actualización indicada por la fuente: 26/01/2026. Captura: 2026-10-08T22:53:19.280Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/persona-interesadas](https://developers.mercadolibre.com.co/es_co/persona-interesadas)

# Personas Interesadas

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 26/01/2026  
**Captura:** 2026-10-08T22:53:19.280Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/persona-interesadas](https://developers.mercadolibre.com.co/es_co/persona-interesadas)

## Resumen

Explica la consulta de compradores interesados y leads generados en publicaciones de vehículos e inmuebles. Permite filtrar por período, tipo de contacto, ítem y comprador, y consultar por separado el detalle de un lead.

## Contenido y conceptos documentados

- La consulta de vendedores requiere `USER_ID`; filtros incluyen `offset` (0), `limit` (10), `date_from`, `date_to` (fecha actual por defecto), `contact_types`, `item_id` y `buyer_ids`. Tipos de lead: `whatsapp`, `question`, `call`, `credit`, `contact_request`, `visit request` y `reservation`.
- La respuesta contiene `results`, datos del comprador y `leads` con `id`/`uuid`, canal, tipo, fechas, referencia externa, ítem y estado; también `paging`, `date_from` y `date_to`. `include_guest=true` añade `guest` y `summary` para usuarios no logueados.
- Errores documentados: 400 por rango de fechas invertido o formatos inválidos, USER_ID inválido y parámetros inválidos. Disponible para vehículos e inmuebles en todos los sitios.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /v1/users/806525693/leads/buyers

La fuente menciona la ruta /v1/users/806525693/leads/buyers, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/v1/users/806525693/leads/buyers`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### GET /leads/{LEAD_ID}/details

**Método:** `GET`  
**Ruta:** `/leads/{LEAD_ID}/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalles adicionales del lead.

**Parámetros**

- `LEAD_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "summary": "Devuelve detalles adicionales del lead."
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "bad_request por rango de fechas invertido o inválido, USER_ID inválido o parámetro inválido." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /vis/leads/{LEAD_ID}

**Método:** `GET`  
**Ruta:** `/vis/leads/{LEAD_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta datos básicos del lead.

**Parámetros**

- `LEAD_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "summary": "Devuelve la información básica del lead."
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "bad_request por rango de fechas invertido o inválido, USER_ID inválido o parámetro inválido." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /vis/users/{USER_ID}/leads/buyers

**Método:** `GET`  
**Ruta:** `/vis/users/{USER_ID}/leads/buyers`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta interesados/leads del vendedor con filtros por fechas, contacto, ítem y comprador.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `offset` (query, opcional): Predeterminado 0.
- `limit` (query, opcional): Predeterminado 10.
- `date_from` (query, opcional): Fecha de inicio YYYY-MM-DD.
- `date_to` (query, opcional): Fecha de término; predeterminado fecha actual.
- `contact_types` (query, opcional): Tipos de contacto.
- `item_id` (query, opcional): Filtra por ítem.
- `buyer_ids` (query, opcional): Uno o varios compradores.
- `include_guest` (query, opcional): true agrega guest y summary.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "results",
    "paging",
    "date_from",
    "date_to",
    "guest",
    "summary",
    "leads.id",
    "leads.uuid",
    "leads.channel",
    "leads.contact_type",
    "leads.created_at",
    "leads.external_id",
    "leads.item_id",
    "leads.status"
  ]
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "bad_request por rango de fechas invertido o inválido, USER_ID inválido o parámetro inválido." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/persona-interesadas](https://developers.mercadolibre.com.co/es_co/persona-interesadas)  
**Captura:** 2026-10-08T22:53:19.280Z

---

## [Publica vehículos](../markdown/publica-vehiculos.md)

Actualización indicada por la fuente: 28/08/2026. Captura: 2026-10-08T22:53:20.752Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/publica-vehiculos](https://developers.mercadolibre.com.co/es_co/publica-vehiculos)

# Publica vehículos

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 28/08/2026  
**Captura:** 2026-10-08T22:53:20.752Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/publica-vehiculos](https://developers.mercadolibre.com.co/es_co/publica-vehiculos)

## Resumen

Describe la creación y consulta de publicaciones de vehículos, la carga de descripción y la búsqueda de avisos por tags. Detalla atributos como placa, chasis, ubicación, financiación y contacto del vendedor.

## Contenido y conceptos documentados

- Para crear la publicación se envía un objeto de ítem con atributos vehiculares. La placa debe corresponder al vehículo y cumplir formatos por país; se enumeran formatos para Brasil, Argentina y Chile. Para ubicación se usa el ID de barrio o ciudad correspondiente.
- En publicaciones de concesionarios, `seller_contact` debe enviarse completo; la fuente enumera `contact`, `other_info`, `country_code`, `area_code`, `phone`, `email`, `webpage`, `country_code2` y datos relacionados. Si falta cuando aplica, se rechaza con HTTP 400.
- La financiación usa sale terms `WITH_FINANCING_OPTIONS` y `INITIAL_PAYMENT_AMOUNT`; la fuente indica habilitación para MLA. La descripción se crea después del ítem, en texto plano y sin datos de contacto. Para avisos con tag de moderación se consulta `users/{USER_ID}/items/search?tags={TAG}`.

## Operaciones de API
## Operaciones de API

### GET /items/{ITEM_ID}

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta los datos de un vehículo publicado.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Falta seller_contact cuando es obligatorio para perfil de concesionario." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /items/{ITEM_ID}/description

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/description`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la descripción del ítem.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "text",
    "plain_text",
    "date_created",
    "snapshot"
  ]
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Falta seller_contact cuando es obligatorio para perfil de concesionario." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /users/{USER_ID}/items/search

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista publicaciones del usuario filtradas por `tags`.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `tags` (query, obligatorio): Tag por el que se filtran publicaciones.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Falta seller_contact cuando es obligatorio para perfil de concesionario." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### POST /items

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una publicación de vehículo.

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
    "attributes",
    "location",
    "seller_contact"
  ],
  "summary": "Datos de creación de la publicación vehicular; los requisitos dependen de sitio y perfil."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Falta seller_contact cuando es obligatorio para perfil de concesionario." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### POST /items/{ITEM_ID}/description

**Método:** `POST`  
**Ruta:** `/items/{ITEM_ID}/description`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea la descripción después de crear la publicación.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Falta seller_contact cuando es obligatorio para perfil de concesionario." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/publica-vehiculos](https://developers.mercadolibre.com.co/es_co/publica-vehiculos)  
**Captura:** 2026-10-08T22:53:20.752Z

---

## [Sincroniza publicaciones (vehículos)](../markdown/vehiculos-sincroniza-publicaciones.md)

Actualización indicada por la fuente: 28/08/2026. Captura: 2026-10-08T22:53:23.539Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/vehiculos-sincroniza-publicaciones](https://developers.mercadolibre.com.co/es_co/vehiculos-sincroniza-publicaciones)

# Sincroniza publicaciones (vehículos)

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 28/08/2026  
**Captura:** 2026-10-08T22:53:23.539Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/vehiculos-sincroniza-publicaciones](https://developers.mercadolibre.com.co/es_co/vehiculos-sincroniza-publicaciones)

## Resumen

Documenta la actualización y sincronización de publicaciones de vehículos, incluyendo cambios de contenido, estado y datos de contacto. También describe restricciones y validaciones para `seller_contact`.

## Contenido y conceptos documentados

- La fuente enumera como actualizables `title`, `price`, `video`, `pictures`, `description`, `location`, `attributes` y `category`; incluye también `seller_contact`. El estado cambia con valores en minúscula: `cerrado`, `pausado` o `activo`.
- `seller_contact` contempla `contact`, `other_info`, códigos y números telefónicos, `email`, `webpage`, `country_code2` y `phone2`. La fuente lista errores HTTP 400 para campos obligatorios o inválidos.
- Si el PUT devuelve 409 por optimistic locking, existe un conflicto de actualización. Autenticación mostrada: OAuth Bearer.

## Operaciones de API
## Operaciones de API

### PUT /items/{ITEM_ID}

**Método:** `PUT`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza campos permitidos de una publicación vehicular, atributos o estado.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `status` (query, opcional): Estado en minúscula: cerrado, pausado o activo.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Validaciones seller_contact y campos obligatorios/numéricos inválidos." } ```
- ```json {   "code": "409",   "meaning": "Optimistic locking conflict al actualizar el ítem." } ```

**Ejemplos**

- La captura incluye ejemplos de llamada para este recurso.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/vehiculos-sincroniza-publicaciones](https://developers.mercadolibre.com.co/es_co/vehiculos-sincroniza-publicaciones)  
**Captura:** 2026-10-08T22:53:23.539Z

---
