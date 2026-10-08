---
id: "pedidos-y-opiniones"
title: "Pedidos y opiniones"
section: "Recursos de la API"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/pedidos-y-opiniones"
source_updated_at: "05/06/2025"
captured_at: "2026-10-08T22:53:57.179Z"
sha256: "3f78c1d02ce42e5c19bde34ef802606462bc66bac3c81d47a786b62888ca828b"
---

# Pedidos y opiniones

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 05/06/2025  
**Captura:** 2026-10-08T22:53:57.179Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/pedidos-y-opiniones](https://developers.mercadolibre.com.co/es_co/pedidos-y-opiniones)

## Resumen

Agrupa ejemplos para consultar órdenes, métodos de pago y opiniones; también incluye bloqueo de compradores e información de productos vendidos.

## Contenido y conceptos documentados

- /orders/search se muestra para búsquedas por seller y buyer. Las respuestas de ejemplo incluyen paging, datos de la orden, pagos, publicaciones, feedback y envío.
- Las opiniones de orden pueden consultarse, crearse y modificarse; el vendedor puede responder mediante el recurso de reply.
- Los métodos de pago se consultan por site y luego por ID; la respuesta de detalle contiene costos, emisores, acreditación y opciones de cuotas.
- Para pedidos, el endpoint block-api filtra type=blocked_by_order con offset/limit; order_blacklist ofrece paginación por usuario.

## Operaciones de API
## Operaciones de API

### Consultar compradores bloqueados por pedidos

**Método:** `GET`  
**Ruta:** `/block-api/search/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista bloqueos relacionados con órdenes.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario consultado.
- `type` (query, obligatorio): blocked_by_order.
- `offset` (query, opcional): Por defecto 0.
- `limit` (query, opcional): Por defecto 10; máximo 1000.

**Solicitud**

No documentado en la fuente.

**Respuesta**

users con id y blocked_at; paging con offset, limit y total.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET con type=blocked_by_order.

### Consultar opiniones de una orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}/feedback`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene opiniones de comprador/vendedor asociadas a una orden.

**Parámetros**

- `order_id` (path, obligatorio): ID de orden.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto sale/purchase con from, to, status, reason, date_created, order_id, id, message, fulfilled, item, rating y otros datos de feedback.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /orders/1068825849/feedback.

### Consultar atributos de productos de una orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}/product`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene información específica del producto vendido dentro de la orden.

**Parámetros**

- `order_id` (path, obligatorio): ID de orden.

**Solicitud**

No documentado en la fuente.

**Respuesta**

attributes es una lista de name, value e id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo incluye IMEI y entry_date.

### Buscar órdenes de vendedor o comprador

**Método:** `GET`  
**Ruta:** `/orders/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca órdenes asociadas al seller o buyer indicado.

**Parámetros**

- `seller` (query): ID del vendedor; ejemplo de búsqueda.
- `buyer` (query): ID del comprador; ejemplo de búsqueda.

**Solicitud**

No documentado en la fuente.

**Respuesta**

La respuesta de ejemplo contiene query, display, paging y results con órdenes, ítems, pagos, buyer/seller, envío y feedback.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /orders/search?seller=... y GET /orders/search?buyer=....

### Listar métodos de pago por sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/payment_methods`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve los métodos de pago previstos por Mercado Pago para un site.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de id, name, payment_type_id, thumbnail y secure_thumbnail.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/payment_methods.

### Consultar método de pago

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/payment_methods/{payment_method_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el detalle de un método de pago de un site.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.
- `payment_method_id` (path, obligatorio): ID del método de pago.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, payment_type_id, card_issuer, site_id, imágenes, labels, costos financieros, plazos y payer_costs.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/payment_methods/amex.

### Consultar lista de usuarios bloqueados por órdenes

**Método:** `GET`  
**Ruta:** `/users/{user_id}/order_blacklist`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve los usuarios en la lista de bloqueo del usuario y permite paginación.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario.
- `offset` (query, opcional): Desplazamiento de paginación.
- `limit` (query, opcional): Cantidad por página.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de usuarios bloqueados; la estructura de respuesta completa no se detalla en el fragmento capturado.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/:userID/order_blacklist?offset=100&limit=50.

### Responder a opinión

**Método:** `POST`  
**Ruta:** `/feedback/{feedback_id}/reply`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Publica la respuesta de un vendedor a una opinión.

**Parámetros**

- `feedback_id` (path, obligatorio): ID de feedback.
- `Content-Type` (header, obligatorio): application/json.

**Solicitud**

JSON con reply.

**Respuesta**

Devuelve el feedback, reply_status, reply_date, visibility_date y reply.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- POST /feedback/{feedback_id}/reply con reply.

### Crear opinión de una orden

**Método:** `POST`  
**Ruta:** `/orders/{order_id}/feedback`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Envía una opinión relacionada con la compra o venta de la orden.

**Parámetros**

- `order_id` (path, obligatorio): ID de orden.
- `Content-Type` (header, obligatorio): application/json.

**Solicitud**

JSON de ejemplo con fulfilled, rating, message, reason, restock_item y has_seller_refunded_money.

**Respuesta**

La respuesta de ejemplo devuelve datos de la opinión, su estado, rating, message, order_id y participantes.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- POST /orders/1068825849/feedback.

### Modificar opinión

**Método:** `PUT`  
**Ruta:** `/feedback/{feedback_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza campos de una opinión existente.

**Parámetros**

- `feedback_id` (path, obligatorio): ID de feedback.
- `Content-Type` (header, obligatorio): application/json.

**Solicitud**

JSON de ejemplo con fulfilled, rating y message.

**Respuesta**

La respuesta muestra status, reason, site_id, date_created, cust_role, order_id, id, message, fulfilled, reply, cust_to y rating.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- PUT /feedback/{feedback_id}.

### Referencia HTTP GET /{SITE_ID}/payment_methods/{id}

**Método:** `GET`  
**Ruta:** `/{SITE_ID}/payment_methods/{id}`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /{SITE_ID}/payment_methods/{id}. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /sites/MLA/payment_methods/amex

**Método:** `GET`  
**Ruta:** `/sites/MLA/payment_methods/amex`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /sites/MLA/payment_methods/amex. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /users/{userID}/order_blacklist

**Método:** `GET`  
**Ruta:** `/users/{userID}/order_blacklist`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/{userID}/order_blacklist. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

- `offset` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.
- `limit` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

### Referencia HTTP GET /api.mercadopago.com/v1/payments/{PAYMENT_ID}

**Método:** `GET`  
**Ruta:** `/api.mercadopago.com/v1/payments/{PAYMENT_ID}`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /api.mercadopago.com/v1/payments/{PAYMENT_ID}. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/pedidos-y-opiniones](https://developers.mercadolibre.com.co/es_co/pedidos-y-opiniones)  
**Captura:** 2026-10-08T22:53:57.179Z
