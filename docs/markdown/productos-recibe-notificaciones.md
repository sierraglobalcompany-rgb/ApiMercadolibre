---
id: "productos-recibe-notificaciones"
title: "Notificaciones"
section: "Recursos de la API"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/productos-recibe-notificaciones"
source_updated_at: "14/09/2026"
captured_at: "2026-10-08T22:53:54.597Z"
sha256: "074c635ab0a04205f0142efe8bfdfb308fb43b66d67f6904d705f017968cd06b"
---

# Notificaciones

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 14/09/2026  
**Captura:** 2026-10-08T22:53:54.597Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/productos-recibe-notificaciones](https://developers.mercadolibre.com.co/es_co/productos-recibe-notificaciones)

## Resumen

Las notificaciones entregan eventos en tiempo real de cambios de recursos, evitando consultar la API de forma periódica. La integración configura en DevCenter la URL callback y los tópicos; recibe un POST en esa URL y luego consulta el recurso indicado para obtener sus datos completos. La documentación cubre topics generales y subtemas, varios recursos de ventas, publicaciones, envíos, créditos y posventa, y recuperación de notificaciones perdidas.

## Contenido y conceptos documentados

### Configuración y entrega

La URL callback debe ser pública y recibir los tópicos elegidos. Las notificaciones usan UTC; `payments` y `messages` no aplican a inmuebles, servicios ni automóviles. El payload general incluye `_id`, `resource`, `user_id`, `topic`, `application_id`, `attempts`, `sent` y `received`; los topics tipificados agregan `actions`. La aplicación debe confirmar con HTTP 200 en un máximo de 500 ms. Si no se acepta, hay reintentos durante una hora; la fuente recomienda confirmar rápidamente y procesar después con una cola.

### Recuperación y consulta de eventos

Cada evento debe verificarse consultando el recurso de `resource`; puede reflejar cambios originados en otras superficies o integraciones. `missed_feeds` conserva hasta dos días las notificaciones que no recibieron 200 tras los intentos de entrega. Para `items`, la consulta requiere `site_id`; pueden usarse filtros de tema y paginación. El ejemplo indica 10 resultados por defecto.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /stock/fulfillment/operations

La fuente menciona la ruta /stock/fulfillment/operations, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/stock/fulfillment/operations`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /stock/fulfillment/operations/9876

La fuente menciona la ruta /stock/fulfillment/operations/9876, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/stock/fulfillment/operations/9876`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /vis/loan/66e93589-2d10-11ed-ae7f-0aa30fafa621

La fuente menciona la ruta /vis/loan/66e93589-2d10-11ed-ae7f-0aa30fafa621, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/vis/loan/66e93589-2d10-11ed-ae7f-0aa30fafa621`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /leads/{LEAD_ID}/details

La fuente menciona la ruta /leads/{LEAD_ID}/details, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/leads/{LEAD_ID}/details`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /post-purchase

La fuente menciona la ruta /post-purchase, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/post-purchase`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /sites/{SITE_ID}/user-products-families/{FAMILY_ID}

La fuente menciona la ruta /sites/{SITE_ID}/user-products-families/{FAMILY_ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/sites/{SITE_ID}/user-products-families/{FAMILY_ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Entrega de notificaciones por callback

Describe configuración del callback, estructura de notificación, tópicos y política de reintentos antes de consultar el recurso informado.

**Solicitud**

El callback recibe HTTP POST en una URL pública configurada por la integración; se recomienda responder HTTP 200 en 500 ms.

**Respuesta**

Payload general con _id, resource, user_id, topic, application_id, attempts, sent y received; los topics tipificados pueden incluir actions.

**Ejemplos documentados**

- Reintentos durante una hora; missed_feeds conserva notificaciones perdidas hasta 2 días.
## Operaciones de API

### Consultar asignación de envío Flex

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/shipments/{shipment_id}/assignment/v1`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene información de la asignación Flex para el envío.

**Parámetros**

- `site_id` (path, obligatorio): ID del sitio.
- `shipment_id` (path, obligatorio): ID del envío.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar candidato a promoción

**Método:** `GET`  
**Ruta:** `/seller-promotions/candidates/{candidate_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalles de un candidato a promoción del vendedor.

**Parámetros**

- `candidate_id` (path, obligatorio): ID del candidato.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar sugerencia de catálogo

**Método:** `GET`  
**Ruta:** `/catalog_suggestions/{suggestion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene una sugerencia de catálogo.

**Parámetros**

- `suggestion_id` (path, obligatorio): ID de sugerencia.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar collection de pago

**Método:** `GET`  
**Ruta:** `/collections/{payment_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los detalles de la collection/pago notificada.

**Parámetros**

- `payment_id` (path, obligatorio): ID del pago.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar factura de usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/invoices/{invoice_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los detalles de una factura del usuario.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.
- `invoice_id` (path, obligatorio): ID de factura.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar familia de User Products

**Método:** `GET`  
**Ruta:** `/user-products-families/{family_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene una familia del recurso User Products.

**Parámetros**

- `family_id` (path, obligatorio): ID de la familia.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar ítem notificado

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los detalles del ítem asociado a la notificación.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Respuesta de ejemplo con id, title, price, currency_id, available_quantity, sold_quantity y status.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Listar leads VIS de usuario

**Método:** `GET`  
**Ruta:** `/vis/users/{user_id}/leads`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta los leads VIS del usuario asociado a la notificación.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar recurso de mensajes

**Método:** `GET`  
**Ruta:** `/messages/{resource}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el recurso de mensajes indicado por la notificación.

**Parámetros**

- `resource` (path, obligatorio): Segmento de recurso recibido en la notificación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar notificaciones perdidas

**Método:** `GET`  
**Ruta:** `/missed_feeds`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera eventos fallidos conservados en missed_feeds; admite filtros y paginación.

**Parámetros**

- `app_id` (query, obligatorio): ID de aplicación.
- `topic` (query, opcional): Filtro por tópico.
- `site_id` (query): Obligatorio al consultar topic=items; otros tópicos no lo requieren.
- `offset` (query, opcional): Desplazamiento para paginación.
- `limit` (query, opcional): Límite de resultados; por defecto 10.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto con messages; registros de ejemplo incluyen resource, user_id, topic, application_id, attempts, sent/received, request y response.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "La consulta de notificaciones perdidas para topic=items sin site_id devuelve HTTP 400." } ```

**Ejemplos**

- Conserva notificaciones perdidas hasta dos días.

### Consultar oferta de vendedor

**Método:** `GET`  
**Ruta:** `/seller-promotions/offers/{offers_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalles de una oferta de seller promotions.

**Parámetros**

- `offers_id` (path, obligatorio): ID de oferta.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar orden desde notificación

**Método:** `GET`  
**Ruta:** `/orders/{order_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los detalles del pedido indicado por el evento.

**Parámetros**

- `order_id` (path, obligatorio): ID de orden.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La guía indica consultar el resource recibido.

### Consultar crédito VIS

**Método:** `GET`  
**Ruta:** `/vis/loans/{credit_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los detalles de un préstamo/crédito VIS para el vendedor.

**Parámetros**

- `credit_id` (path, obligatorio): ID del crédito.
- `seller_id` (query, obligatorio): ID del vendedor.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar price-to-win

**Método:** `GET`  
**Ruta:** `/items/{item_id}/price_to_win`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el recurso price-to-win del ítem.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar pregunta

**Método:** `GET`  
**Ruta:** `/questions/{question_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene la pregunta indicada en la notificación.

**Parámetros**

- `question_id` (path, obligatorio): ID de la pregunta.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar recurso indicado en notificación

**Método:** `GET`  
**Ruta:** `/{resource}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene la ruta del recurso enviada en resource; la página muestra ejemplos de fulfillment y post-compra.

**Parámetros**

- `resource` (path, obligatorio): Ruta recibida en el campo resource.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El path concreto depende del resource recibido.

### Referencia HTTP GET /stock/fulfillment/operations

**Método:** `GET`  
**Ruta:** `/stock/fulfillment/operations`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /stock/fulfillment/operations. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Consultar precio de venta

**Método:** `GET`  
**Ruta:** `/items/{item_id}/sale_price`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el precio del ítem para el contexto indicado.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.
- `context` (query, obligatorio): Contexto del precio indicado en la notificación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar envío

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el detalle del envío notificado.

**Parámetros**

- `shipment_id` (path, obligatorio): ID del envío.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar stock de User Product

**Método:** `GET`  
**Ruta:** `/user-products/{user_product_id}/stock`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene stock de un producto de usuario.

**Parámetros**

- `user_product_id` (path, obligatorio): ID del User Product.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar detalles de sugerencias de ítem

**Método:** `GET`  
**Ruta:** `/suggestions/items/{item_id}/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalles de sugerencias relacionadas con un ítem.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar User Product

**Método:** `GET`  
**Ruta:** `/user_products/{up_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el User Product señalado por la notificación.

**Parámetros**

- `up_id` (path, obligatorio): ID del User Product.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar lead VIS

**Método:** `GET`  
**Ruta:** `/vis/leads/{lead_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el lead indicado por una notificación VIS.

**Parámetros**

- `lead_id` (path, obligatorio): ID del lead.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/productos-recibe-notificaciones](https://developers.mercadolibre.com.co/es_co/productos-recibe-notificaciones)  
**Captura:** 2026-10-08T22:53:54.597Z
