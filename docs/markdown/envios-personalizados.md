---
id: "envios-personalizados"
title: "Envíos Personalizados"
section: "Guía para productos"
subsection: "Envíos"
url: "https://developers.mercadolibre.com.co/es_co/envios-personalizados"
source_updated_at: "13/03/2026"
captured_at: "2026-10-08T22:51:42.998Z"
sha256: "bc5af1e6c589aafa1363ed44aeaf7cfd7c3152d972f07c685eca1bebc42f82ce"
---

# Envíos Personalizados

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/03/2026  
**Captura:** 2026-10-08T22:51:42.998Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/envios-personalizados](https://developers.mercadolibre.com.co/es_co/envios-personalizados)

## Resumen

Explica el modo custom, donde el vendedor define costos y gestiona la logística, y not_specified, donde comprador y vendedor acuerdan detalles y no existe shipment_id. También describe cómo consultar opciones y reportar tracking, promesa, entrega o cancelación.

## Contenido y conceptos documentados

- Al crear un ítem se configura shipping.mode=custom con costos y descripciones; not_specified puede usarse para acordar el envío. El envío personalizado gratuito solo se permite en categorías que no aceptan Mercado Envíos.
- La respuesta shipping_options muestra options con id, option_hash, name, currency_id, list_cost, cost, base_cost, display y speed.
- Estados documentados: Pending puede pasar a Shipped, Delivered o Cancelled; Shipped admite actualizar tracking/promesa; Delivered puede volver a Pending o Shipped; Cancelled es terminal.
- Para actualizar envío se envían receiver_id y, según el escenario, status, speed, tracking_number o comments. tracking_number es requerido por API en el flujo indicado aunque la página aclara que no aparece en listados/detalles de venta. Auth Bearer.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar opciones de costo

**Método:** `GET`  
**Ruta:** `/items/{item_id}/shipping_options`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Devuelve la tabla de costos custom para un código postal.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `zip_code` (query, obligatorio): zip_code requerido

**Solicitud**

No documentado en la fuente.

**Respuesta**

destination, options[{id,option_hash,name,currency_id,list_cost,cost,base_cost,display,speed}], buyer y custom_message.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con zip_code.

### Crear publicación con envío personalizado

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Crea un ítem cuyo shipping se configura como custom y contiene tabla de costos.

**Parámetros**

- `title` (body, obligatorio): Título de la publicación.
- `category_id` (body, obligatorio): Categoría.
- `price` (body, obligatorio): Precio.
- `shipping` (body, obligatorio): Modo, modalidad local, gratuidad, métodos y costos.

**Solicitud**

Cuerpo de publicación con shipping.mode=custom, local_pick_up, free_shipping, methods y costs[{description,cost}].

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo completo compacto con dos costos.

### Cancelar envío personalizado

**Método:** `POST`  
**Ruta:** `/shipments/{shipment_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Informa cancelación de la venta/envío.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `status` (body, obligatorio): Debe ser cancelled en el ejemplo.
- `receiver_id` (body, obligatorio): Identificador del receptor.

**Solicitud**

status=cancelled y receiver_id.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de cancelación.

### Actualizar envío de publicación

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Configura envío custom o envío gratis not_specified cuando la categoría no admite Mercado Envíos.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `shipping` (body, obligatorio): Modo custom o not_specified, gratuidad y costos.

**Solicitud**

shipping.mode, local_pick_up, free_shipping, methods y costs; para gratuito usa free_shipping=true y costs vacío.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo para costos custom y ejemplo de envío gratis.

### Actualizar tracking o estado

**Método:** `PUT`  
**Ruta:** `/shipments/{shipment_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Actualiza número de seguimiento, promesa o estado según la transición del envío.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `receiver_id` (body, obligatorio): Identificador del receptor.
- `status` (body, opcional): Estado enviado según transición.
- `speed` (body, opcional): Horas para promesa de entrega.
- `tracking_number` (body, opcional): Número de seguimiento.
- `comments` (body, opcional): Comentario opcional.

**Solicitud**

tracking_number y receiver_id; en escenarios de estado puede incluir status, speed, comments.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos para shipped, actualizar speed y delivered.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/envios-personalizados](https://developers.mercadolibre.com.co/es_co/envios-personalizados)  
**Captura:** 2026-10-08T22:51:42.998Z
