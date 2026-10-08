# Guía para servicios

7 páginas del portal oficial en esta área.

## [Administra áreas de cobertura](../markdown/administra-areas-de-cobertura.md)

Actualización indicada por la fuente: 15/03/2023. Captura: 2026-10-08T22:53:03.494Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/administra-areas-de-cobertura](https://developers.mercadolibre.com.co/es_co/administra-areas-de-cobertura)

# Administra áreas de cobertura

**Área:** Guía para servicios  
**Actualización indicada por la fuente:** 15/03/2023  
**Captura:** 2026-10-08T22:53:03.494Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/administra-areas-de-cobertura](https://developers.mercadolibre.com.co/es_co/administra-areas-de-cobertura)

## Resumen

Explica cómo descubrir IDs predefinidos de cobertura y asociarlos a una publicación de servicio.

## Contenido y conceptos documentados

- El listado por sitio devuelve id, description, zone y type; se muestran áreas de Argentina y un ID nacional.
- El detalle se obtiene por ID de área. Para asignar cobertura, la fuente envía una lista de IDs bajo coverage_areas mediante PUT al ítem.

## Operaciones de API
## Operaciones de API

### Consultar área de cobertura por ID

**Método:** `GET`  
**Ruta:** `/coverage_areas/{coverage_area_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalle de un área identificada por su ID.

**Parámetros**

- `coverage_area_id` (path, obligatorio): ID preestablecido del área.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, description, zone y type.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /coverage_areas/TUxBUEpVSnk3YmUz.

### Listar áreas de cobertura

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/coverage_areas`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista áreas disponibles para el sitio/país.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Array con id, description, zone y type.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/coverage_areas.

### Asignar áreas de cobertura

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza el ítem con las áreas geográficas atendidas por el servicio.

**Parámetros**

- `item_id` (path, obligatorio): ID de publicación.

**Solicitud**

JSON con coverage_areas como lista de IDs de cobertura.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- PUT /items/ITEM_ID con dos IDs de área.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/administra-areas-de-cobertura](https://developers.mercadolibre.com.co/es_co/administra-areas-de-cobertura)  
**Captura:** 2026-10-08T22:53:03.494Z

---

## [Consulta Usuarios](../markdown/servicios-consulta-usuarios.md)

Actualización indicada por la fuente: 29/04/2025. Captura: 2026-10-08T22:53:04.557Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/servicios-consulta-usuarios](https://developers.mercadolibre.com.co/es_co/servicios-consulta-usuarios)

# Consulta Usuarios

**Área:** Guía para servicios  
**Actualización indicada por la fuente:** 29/04/2025  
**Captura:** 2026-10-08T22:53:04.557Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/servicios-consulta-usuarios](https://developers.mercadolibre.com.co/es_co/servicios-consulta-usuarios)

## Resumen

Reúne consultas de perfil público y privado, actualización de dirección y consulta de bloqueos relacionados con preguntas o pedidos.

## Contenido y conceptos documentados

- /users/me consulta quien autorizó la aplicación; /users/{user_id} ofrece perfil público y /private puede incluir dirección completa y contacto si el usuario autorizó y el token tiene permiso.
- La actualización requiere permiso del usuario y recibe address con street, number, city y state.
- El endpoint de bloqueos unifica preguntas y órdenes: type acepta blocked_by_questions o blocked_by_order; client.id y user_blocked son opcionales, caller.id es obligatorio, offset inicia en 0 y limit en 10 (máximo 1000). La respuesta presenta users y paging.

## Operaciones de API
## Operaciones de API

### Buscar usuarios bloqueados

**Método:** `GET`  
**Ruta:** `/block-api/search/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta bloqueos asociados a un Buyer; endpoint unificado para preguntas y órdenes.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario.
- `client.id` (opcional): ID del cliente que realiza la solicitud.
- `type` (query, obligatorio): blocked_by_questions o blocked_by_order.
- `user_blocked` (opcional): ID del Buyer bloqueado.
- `caller.id` (obligatorio): ID del usuario que realiza la solicitud.
- `offset` (opcional): Por defecto 0.
- `limit` (opcional): Por defecto 10, máximo 1000.

**Solicitud**

No documentado en la fuente.

**Respuesta**

users con id y blocked_at; paging con offset, limit y total.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- type=blocked_by_questions y type=blocked_by_order; la fuente muestra 200 OK.

### Consultar usuario autenticado

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve información del usuario que autorizó la aplicación.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo contiene id, nickname, registration_date, country_id, address, user_type, tags, site_id, seller_reputation, buyer_reputation y status.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/me.

### Consultar información pública de usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta perfil y reputación pública por ID.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con id, nickname, registration_date, country_id, address de ciudad/estado, tags, reputaciones y status.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/202593498.

### Consultar información privada de usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/private`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN con permiso para estos datos

Consulta información privada de un usuario que autorizó la aplicación; requiere token con permiso.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo agrega street/number y datos de contacto al perfil.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/202593498/private.

### Actualizar dirección de usuario

**Método:** `PUT`  
**Ruta:** `/users/{user_id}/address`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza la dirección de un usuario que concedió permiso.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

JSON address con street, number, city y state.

**Respuesta**

Ejemplo devuelve perfil con dirección actualizada.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- PUT /users/202593498/address.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/servicios-consulta-usuarios](https://developers.mercadolibre.com.co/es_co/servicios-consulta-usuarios)  
**Captura:** 2026-10-08T22:53:04.557Z

---

## [Consultas avanzadas](../markdown/consultas-avanzadas-2.md)

Actualización indicada por la fuente: 15/03/2023. Captura: 2026-10-08T22:53:05.581Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/consultas-avanzadas-2](https://developers.mercadolibre.com.co/es_co/consultas-avanzadas-2)

# Consultas avanzadas

**Área:** Guía para servicios  
**Actualización indicada por la fuente:** 15/03/2023  
**Captura:** 2026-10-08T22:53:05.581Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/consultas-avanzadas-2](https://developers.mercadolibre.com.co/es_co/consultas-avanzadas-2)

## Resumen

Presenta casos de uso de información de mercado para comparar precios y atributos, orientar estrategias de vendedores y ayudar a compradores a encontrar productos.

## Contenido y conceptos documentados

- La página diferencia datos públicos de datos privados: no se deben obtener datos privados de usuarios que no autorizaron la aplicación.
- Propone buscar artículos por categoría, comparar precios y atributos, calcular promedios y analizar categorías, contactos y visitas. Los pasos y endpoints se remiten a otras guías.

## Operaciones de API

## Conceptos y recursos asociados

### Consultas y análisis de mercado

Sugiere herramientas que comparen precios y atributos de publicaciones para ayudar a vendedores a analizar su mercado. La fuente advierte que los datos privados de usuarios requieren autorización; esta página no define operaciones HTTP concretas.

**Ejemplos documentados**

- Casos de uso: comparar precios por categoría, calcular promedios y revisar atributos, contactos y visitas públicas.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/consultas-avanzadas-2](https://developers.mercadolibre.com.co/es_co/consultas-avanzadas-2)  
**Captura:** 2026-10-08T22:53:05.581Z

---

## [Elige tipo de servicio](../markdown/elige-tipo-de-servicio.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:53:06.511Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/elige-tipo-de-servicio](https://developers.mercadolibre.com.co/es_co/elige-tipo-de-servicio)

# Elige tipo de servicio

**Área:** Guía para servicios  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:06.511Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/elige-tipo-de-servicio](https://developers.mercadolibre.com.co/es_co/elige-tipo-de-servicio)

## Resumen

Explica cómo recorrer las categorías propias de cada site y consultar atributos antes de publicar un servicio.

## Contenido y conceptos documentados

- Cada país tiene su árbol de categorías. /sites/{site_id}/categories lista IDs/nombres y /categories/{category_id} permite recorrer la ruta desde la raíz y sus children_categories.
- El detalle y /attributes ayudan a identificar los valores de publicación. La página ejemplifica Argentina (MLA) y muestra una búsqueda filtrada por ID de categoría.

## Operaciones de API
## Operaciones de API

### Consultar detalle de categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve información y categorías hijas para navegar el árbol.

**Parámetros**

- `category_id` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, picture, permalink, total_items_in_this_category, path_from_root y children_categories.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /categories/MLA1071.

### Consultar atributos de categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Muestra atributos y valores posibles de una categoría.

**Parámetros**

- `category_id` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Atributos con id, name, value_type, tags y values en el ejemplo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /categories/MLA24272/attributes.

### Listar categorías del sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/categories`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el árbol de categorías de un país para elegir dónde publicar un servicio.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de categorías con id y name.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/categories.

### Buscar publicaciones por categoría

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Ejemplifica una búsqueda de publicaciones limitada a un ID de categoría.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.
- `category` (query, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/search?category=MLA5726.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/elige-tipo-de-servicio](https://developers.mercadolibre.com.co/es_co/elige-tipo-de-servicio)  
**Captura:** 2026-10-08T22:53:06.511Z

---

## [Introducción](../markdown/guia-para-servicios.md)

Actualización indicada por la fuente: 15/03/2023. Captura: 2026-10-08T22:53:08.327Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/guia-para-servicios](https://developers.mercadolibre.com.co/es_co/guia-para-servicios)

# Introducción

**Área:** Guía para servicios  
**Actualización indicada por la fuente:** 15/03/2023  
**Captura:** 2026-10-08T22:53:08.327Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/guia-para-servicios](https://developers.mercadolibre.com.co/es_co/guia-para-servicios)

## Resumen

Introduce el modelo de servicios clasificados de Mercado Libre, con contacto directo y condiciones de contratación coordinadas entre usuarios.

## Contenido y conceptos documentados

- Una aplicación puede publicar servicios, medir contactos, buscar por geolocalización, comparar precio/prestaciones, enviar recordatorios y sugerir ofertas similares. Esta página introductoria no documenta métodos ni rutas HTTP.

## Operaciones de API

## Conceptos y recursos asociados

### Modelo de publicación de servicios

Presenta servicios como clasificados donde los datos de contacto son públicos y contacto, pago y contratación se coordinan entre las partes. No especifica rutas HTTP concretas.

**Ejemplos documentados**

- Casos de uso: publicar servicios, medir contactos, buscar por geolocalización, comparar prestaciones/precios, recordatorios y sugerencias.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/guia-para-servicios](https://developers.mercadolibre.com.co/es_co/guia-para-servicios)  
**Captura:** 2026-10-08T22:53:08.327Z

---

## [Publica servicios](../markdown/publica-servicios-vis.md)

Actualización indicada por la fuente: 15/03/2023. Captura: 2026-10-08T22:53:09.203Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/publica-servicios-vis](https://developers.mercadolibre.com.co/es_co/publica-servicios-vis)

# Publica servicios

**Área:** Guía para servicios  
**Actualización indicada por la fuente:** 15/03/2023  
**Captura:** 2026-10-08T22:53:09.203Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/publica-servicios-vis](https://developers.mercadolibre.com.co/es_co/publica-servicios-vis)

## Resumen

Expone campos generales de publicaciones de servicios, consulta de ítems, tipos de publicación y un ejemplo de creación de clasificado.

## Contenido y conceptos documentados

- La publicación se representa como un ítem. El ejemplo de consulta muestra identidad, título, categoría, precio, moneda, disponibilidad, modalidad, fotos, contacto, ubicación, atributos y descripción.
- El ejemplo de creación usa POST y buying_mode=classified, pero la captura no muestra la URL destino; no se registra una ruta supuesta. Está basado en MLA y advierte cambiar category_id, currency_id y posiblemente listing_type_id para otros países.
- seller_custom_field es un string de uso interno, distinto de SELLER_SKU. listing_types permite conocer los tipos aceptados por site.

## Operaciones de API

## Conceptos y recursos asociados

### Ejemplo de creación de servicio

La fuente muestra una solicitud POST para crear un clasificado que requiere access_token, pero la captura no contiene la URL destino. El cuerpo enumera title, category_id, price, currency_id, available_quantity, buying_mode=classified, listing_type_id, condition, pictures, seller_contact, location, attributes y description.

**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

**Solicitud**

Ejemplo de JSON para clasificado con seller_contact, location, attributes e información básica de publicación; valores ilustrativos para MLA.

**Respuesta**

Ejemplo de respuesta con id, site_id, title, sold_quantity y permalink.

**Ejemplos documentados**

- La fuente no documenta ruta del POST; señala que el ejemplo usa categorías/moneda/tipo de publicación de MLA y deben cambiarse para otros países.
## Operaciones de API

### Consultar publicación

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los datos de una publicación de servicio/ítem por ID precedido del site_id.

**Parámetros**

- `item_id` (path, obligatorio): ID completo del ítem con prefijo del site.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con id, site_id, title, seller_id, category_id, price, currency_id, available_quantity, buying_mode, listing_type_id, pictures, seller_contact, location, attributes y description.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /items/MLA612001263.

### Listar tipos de publicación

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/listing_types`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta listing_type_id disponibles por site.

**Parámetros**

- `site_id` (path, obligatorio): Código del site.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Array con site_id, id y name; se ejemplifican gold_pro, gold_premium, gold_special, gold, silver, bronze y free.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/listing_types.

### Actualizar campo personalizado del vendedor

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza seller_custom_field, campo de uso interno distinto de SELLER_SKU.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

JSON con seller_custom_field como string.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- PUT /items/MLA599074368 con seller_custom_field.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/publica-servicios-vis](https://developers.mercadolibre.com.co/es_co/publica-servicios-vis)  
**Captura:** 2026-10-08T22:53:09.203Z

---

## [Sincroniza publicaciones](../markdown/servicio-sincroniza-publicaciones.md)

Actualización indicada por la fuente: 15/03/2023. Captura: 2026-10-08T22:53:10.446Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/servicio-sincroniza-publicaciones](https://developers.mercadolibre.com.co/es_co/servicio-sincroniza-publicaciones)

# Sincroniza publicaciones

**Área:** Guía para servicios  
**Actualización indicada por la fuente:** 15/03/2023  
**Captura:** 2026-10-08T22:53:10.446Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/servicio-sincroniza-publicaciones](https://developers.mercadolibre.com.co/es_co/servicio-sincroniza-publicaciones)

## Resumen

Explica cómo mantener una publicación activa sincronizada con otros sistemas mediante cambios permitidos de contenido, precio, stock o estado.

## Contenido y conceptos documentados

- Los campos modificables dependen de ventas y estado; la página enumera title, available_quantity, price, video, pictures, description, shipping y category en su contexto. La descripción se agrega con POST.
- Con ventas no se pueden modificar condition, buying mode, métodos de pago distintos de Mercado Pago, dimensiones de envío ni warranty. El título tiene restricción adicional y el tipo de publicación solo se cambia una vez.
- Los estados se envían en minúscula: paused impide el contacto, closed finaliza y no se reactiva (puede republicarse), active reactiva un ítem pausado. Para eliminar, primero cierra y luego envía deleted=true; si aparece 409 optimistic_locking conflict, espera unos segundos antes de repetir.

## Operaciones de API
## Operaciones de API

### Actualizar publicación

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza campos editables, estado, inventario o eliminación mediante PUT al recurso del ítem; las restricciones dependen de ventas y estado.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

Ejemplos: title y price; status=paused/closed; deleted=true tras cerrar; available_quantity. La página enumera title, available_quantity, price, video, pictures, description (solo agregar un post), shipping y category como editables en su contexto.

**Respuesta**

200 OK indicado en la actualización de título/precio; otras estructuras no documentadas.

**Errores documentados**

- ```json {   "status": 409,   "code": "optimistic_locking error: conflict",   "meaning": "El segundo PUT de eliminación puede tener conflicto; la fuente indica esperar unos segundos hasta actualizar la información." } ```

**Ejemplos**

- PUT /items/ITEM_ID para título/precio, estado y stock; eliminación requiere primero status=closed y luego deleted=true.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/servicio-sincroniza-publicaciones](https://developers.mercadolibre.com.co/es_co/servicio-sincroniza-publicaciones)  
**Captura:** 2026-10-08T22:53:10.446Z

---
