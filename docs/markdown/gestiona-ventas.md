---
id: "gestiona-ventas"
title: "Órdenes"
section: "Guía para productos"
subsection: "Gestionar ventas"
url: "https://developers.mercadolibre.com.co/es_co/gestiona-ventas"
source_updated_at: "21/09/2026"
captured_at: "2026-10-08T22:52:16.978Z"
sha256: "c48a0dfb03ce005b4b57662ae375d153d2b08c866aa552dc7650603ff6d48faa"
---

# Órdenes

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 21/09/2026  
**Captura:** 2026-10-08T22:52:16.978Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestiona-ventas](https://developers.mercadolibre.com.co/es_co/gestiona-ventas)

## Resumen

Describe consulta y búsqueda de órdenes, detalle de productos, pagos, descuentos y envíos. La orden agrupa condiciones de compra visibles para comprador y vendedor.

## Contenido y conceptos documentados

- /orders/{order_id} incluye estado, fechas, artículos, pagos, feedback, envío y participantes; para feedback, la fuente remite a su recurso específico.
- /orders/search filtra por seller, buyer, item, tags/tags.not, q, estados, fechas, mediaciones y feedback. q busca ID de orden, ID/título del ítem y nickname de contraparte, no nombres ni email. Se muestran paginación y sort=date_desc.
- La consulta de envíos puede devolver varios registros. Hosted View siempre produce array; identifica el envío de compra por type=forward. La fuente advierte que el contrato de la vista actual (objeto por defecto) difiere del array de Hosted View y marca la vista actual como deprecada desde finales de septiembre de 2026.
- También se documentan conversión de moneda, atributos de productos y descuentos. La guía enumera estados confirmed, payment_required, payment_in_process, partially_paid, paid, partially_refunded, pending_cancel y cancelled.

## Operaciones de API

## Conceptos y recursos asociados

### Ciclo y estados de órdenes

La guía cubre consulta, búsqueda, pagos, descuentos, feedback y envíos. Indica retención de órdenes hasta 12 meses y exclusión de canceladas al buscar como vendedor; enumera estados confirmed, payment_required, payment_in_process, partially_paid, paid, partially_refunded, pending_cancel y cancelled.

**Ejemplos documentados**

- Ejemplos de orden pagada y de filtros por estado/fecha.
### Ruta mencionada /orders/{order_id}/feedback

La fuente menciona la ruta /orders/{order_id}/feedback, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/orders/{order_id}/feedback`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /discounts

La fuente menciona la ruta /discounts, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/discounts`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /shipments

La fuente menciona la ruta /shipments, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/shipments`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /packs

La fuente menciona la ruta /packs, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/packs`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /shipments/shipping.id

La fuente menciona la ruta /shipments/shipping.id, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/shipments/shipping.id`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar conversión de moneda

**Método:** `GET`  
**Ruta:** `/currency_conversions/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene la tasa entre moneda de origen y destino.

**Parámetros**

- `from` (query, obligatorio): Código de moneda de origen.
- `to` (query, obligatorio): Código de moneda destino.

**Solicitud**

No documentado en la fuente.

**Respuesta**

ratio.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /currency_conversions/search?from=ARS&to=BRL.

### Consultar orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve estado, fechas, productos, pagos, compradores/vendedores, feedback, envío y etiquetas.

**Parámetros**

- `order_id` (path, obligatorio): ID de orden.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo: id, status, status_detail, date_created, date_closed, order_items, total_amount, currency_id, buyer, seller, payments, feedback, context, shipping, static_tags y tags.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /orders/2000003508419013.

### Consultar descuentos de una orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}/discounts`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve descuentos que incidieron en la venta, incluidos cupón, campañas y cashback.

**Parámetros**

- `order_id` (path, obligatorio): ID de orden.

**Solicitud**

No documentado en la fuente.

**Respuesta**

details con type, coupon/supplier e items con quantity y amounts (total/seller).

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /orders/2000003508419013/discounts.

### Consultar atributos de productos de una orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}/product`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve los atributos registrados para los productos de una orden.

**Parámetros**

- `order_id` (path, obligatorio): ID de orden.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto con attributes; cada elemento puede contener name, value e id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con atributos IMEI y entry_date.

### Consultar envíos asociados a orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}/shipments`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene IDs/tipos de envíos. Hosted View siempre devuelve array; recorrer resultados y filtrar type=forward para identificar envío de compra. La vista actual se marca deprecada desde finales de septiembre de 2026.

**Parámetros**

- `order_id` (path, obligatorio): ID de orden.
- `hosted` (query, opcional): Default false; vista APICore sin detalle de envíos.
- `list_all` (query, opcional): En la vista actual, true devuelve array forward y return.
- `X-New-Domain` (header, opcional): Necesario en llamadas públicas para enrutar a Hosted View.
- `X-Api-Version` (header, opcional): Valor 2 solicita receiver_name y receiver_phone completos en receiver_address en la vista actual.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Hosted View: array de objetos {id,type}; se ejemplifican forward, return y return_to_buyer. Vista actual: objeto con datos del shipment, estado, modalidad, tracking, historial, shipping_items y dirección.

**Errores documentados**

- ```json {   "status": 200,   "meaning": "Envíos encontrados." } ```
- ```json {   "status": 204,   "meaning": "La orden no tiene envíos o están en propagación asíncrona." } ```
- ```json {   "status": 400,   "meaning": "Parámetros inválidos, como order_id no numérico." } ```
- ```json {   "status": 401,   "meaning": "Autenticación fallida o caller no identificado." } ```
- ```json {   "status": 403,   "meaning": "Permisos insuficientes." } ```
- ```json {   "status": 404,   "meaning": "order_id inexistente." } ```
- ```json {   "status": 500,   "meaning": "Error interno." } ```
- ```json {   "status": 503,   "meaning": "Servicio no disponible." } ```

**Ejemplos**

- GET /orders/{order_id}/shipments; ejemplos con X-New-Domain:true y list_all=true.

### Buscar órdenes

**Método:** `GET`  
**Ruta:** `/orders/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Filtra órdenes por usuario, ítem, estado, fechas, tags, mediaciones y feedback.

**Parámetros**

- `seller` (query): ID vendedor; aparece en ejemplos.
- `buyer` (query): ID comprador.
- `item` (query): ID o título.
- `tags` (query): Estados separados por coma.
- `tags.not` (query): Estados excluidos separados por coma.
- `q` (query): Busca ID de orden, ID/título de ítem o nickname de contraparte; no busca first_name, last_name ni email.
- `order.status` (query): Filtro u ordenamiento enumerado en la guía.
- `order.date_last_updated.from` (query): Filtro u ordenamiento enumerado en la guía.
- `order.date_last_updated.to` (query): Filtro u ordenamiento enumerado en la guía.
- `order.date_created.from` (query): Filtro u ordenamiento enumerado en la guía.
- `order.date_created.to` (query): Filtro u ordenamiento enumerado en la guía.
- `order.date_closed.from` (query): Filtro u ordenamiento enumerado en la guía.
- `order.date_closed.to` (query): Filtro u ordenamiento enumerado en la guía.
- `mediations.stage` (query): Filtro u ordenamiento enumerado en la guía.
- `mediations.status` (query): Filtro u ordenamiento enumerado en la guía.
- `feedback.status` (query): Filtro u ordenamiento enumerado en la guía.
- `feedback.sale.rating` (query): Filtro u ordenamiento enumerado en la guía.
- `feedback.sale.fulfilled` (query): Filtro u ordenamiento enumerado en la guía.
- `feedback.purchase.rating` (query): Filtro u ordenamiento enumerado en la guía.
- `feedback.purchase.fulfilled` (query): Filtro u ordenamiento enumerado en la guía.
- `sort` (query): Filtro u ordenamiento enumerado en la guía.

**Solicitud**

No documentado en la fuente.

**Respuesta**

query, results, sort, available_sorts, filters, paging y display; resultados con orden, pagos, compradores, vendedores, envíos e ítems.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Filtros order.status=paid, q y order.date_created.from/to; orden sort=date_desc.

### Referencia HTTP GET /shipments

**Método:** `GET`  
**Ruta:** `/shipments`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /shipments. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestiona-ventas](https://developers.mercadolibre.com.co/es_co/gestiona-ventas)  
**Captura:** 2026-10-08T22:52:16.978Z
