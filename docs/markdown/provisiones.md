---
id: "provisiones"
title: "Provisiones"
section: "Guía para productos"
subsection: "Reportes de Facturación"
url: "https://developers.mercadolibre.com.co/es_co/provisiones"
source_updated_at: "08/06/2026"
captured_at: "2026-10-08T22:52:37.232Z"
sha256: "26da150f4af471fea75a34dc1dc964f4b389e530262a222a5b0f993bf8e59e7f"
---

# Provisiones

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 08/06/2026  
**Captura:** 2026-10-08T22:52:37.232Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/provisiones](https://developers.mercadolibre.com.co/es_co/provisiones)

## Resumen

Explica cómo obtener el detalle de cargos y notas fiscales de un período, grupo de facturación y unidad de negocio: Mercado Libre, Mercado Pago, Flex, Full e Insurtech. La API admite facturas (`BILL`) y notas de crédito (`CREDIT_NOTE`), además de búsquedas de cargos asociados a órdenes o paquetes.

## Contenido y conceptos documentados

### Parámetros y uso

- Las rutas usan `Authorization: Bearer $ACCESS_TOKEN`. Las llamadas de detalle por período reciben una `KEY` mensual y permiten `group` y `document_type`.
- La página describe paginación de detalles con `limit` (por defecto 150, máximo 1000) y `from_id` (por defecto 0; la siguiente página usa `last_id`). Para ordenamiento menciona `sort_by` (`ID` o `DATE`) y `order_by` (`ASC` o `DESC`). El endpoint por órdenes limita `order_ids` a 60 por consulta y también permite filtrar por `pack_id`.
- Las respuestas documentadas contienen identificadores, cargos, ventas, pagos, envíos, artículos, descuentos, movimientos e información del documento; algunos datos cambian según el grupo/negocio. Para relacionar cargos con la operación, la fuente remite a recursos de órdenes, packs, envíos, descuentos, precio de venta y ofertas promocionales.
- Los cuerpos de solicitud y códigos de error específicos por ruta: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Detalle de facturación por orden o pack

**Método:** `GET`  
**Ruta:** `/billing/integration/group/ML/order/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Filtra detalles de facturación de Mercado Libre por órdenes o paquete.

**Parámetros**

- `order_ids` (query, opcional): Uno o varios IDs; máximo 60 por consulta.
- `pack_id` (query, opcional)
- `sort_by` (query, opcional): ID o DATE.
- `order_by` (query, opcional): ASC o DESC.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de consulta con order_ids.

### Detalle de facturación Mercado Libre

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/$KEY/group/ML/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta cargos y notas fiscales de Mercado Libre para la clave del período.

**Parámetros**

- `KEY` (path, obligatorio): Clave del período mensual.
- `document_type` (query): BILL o CREDIT_NOTE.
- `limit` (query, opcional): Por defecto 150; máximo 1000.
- `from_id` (query, opcional): Por defecto 0; continuar con last_id.
- `sort_by` (query, opcional): ID o DATE.
- `order_by` (query, opcional): ASC o DESC.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- charge_info
- legal_document_number
- legal_document_status
- creation_date_time
- detail_id
- transaction_detail
- detail_amount
- detail_type
- sales_info
- shipping_info
- items_info
- document_info
- marketplace_info

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra paginación por from_id y last_id.

### Detalle de facturación Flex

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/$KEY/group/ML/flex/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta cobros, bonificaciones y datos de envíos Flex por período.

**Parámetros**

- `KEY` (path, obligatorio): Clave del período mensual.
- `document_type` (query): BILL o CREDIT_NOTE.
- `limit` (query, opcional): Por defecto 150; máximo 1000.
- `from_id` (query, opcional): Por defecto 0; continuar con last_id.
- `sort_by` (query, opcional): ID o DATE.
- `order_by` (query, opcional): ASC o DESC.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- shipping_info
- shipping_id
- pack_id
- receiver_shipping_cost
- item_id
- movement_id
- operation_info
- detail_amount

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Detalle de facturación Full

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/$KEY/group/ML/full/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta cobros y bonificaciones por recolección y almacenamiento de productos.

**Parámetros**

- `KEY` (path, obligatorio): Clave del período mensual.
- `document_type` (query): BILL o CREDIT_NOTE.
- `limit` (query, opcional): Por defecto 150; máximo 1000.
- `from_id` (query, opcional): Por defecto 0; continuar con last_id.
- `sort_by` (query, opcional): ID o DATE.
- `order_by` (query, opcional): ASC o DESC.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- fulfillment_info
- inbound_id
- volume_type
- volume_unit
- amount_per_volume_unit
- volume
- volume_total
- items_info

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Detalle de facturación Insurtech

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/$KEY/group/ML/insurtech/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta cobros/bonificaciones de garantías aplicadas sobre productos.

**Parámetros**

- `KEY` (path, obligatorio): Clave del período mensual.
- `document_type` (query): BILL o CREDIT_NOTE.
- `limit` (query, opcional): Por defecto 150; máximo 1000.
- `from_id` (query, opcional): Por defecto 0; continuar con last_id.
- `sort_by` (query, opcional): ID o DATE.
- `order_by` (query, opcional): ASC o DESC.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- warranty_info
- warranty_id
- certificate_id
- warranty_product
- order_items

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Detalle de facturación Mercado Pago

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/$KEY/group/MP/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta movimientos, medios de pago y cobros de Mercado Pago por período.

**Parámetros**

- `KEY` (path, obligatorio): Clave del período mensual.
- `document_type` (query): BILL o CREDIT_NOTE.
- `limit` (query, opcional): Por defecto 150; máximo 1000.
- `from_id` (query, opcional): Por defecto 0; continuar con last_id.
- `sort_by` (query, opcional): ID o DATE.
- `order_by` (query, opcional): ASC o DESC.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- payment_info
- payment_id
- date_approved
- money_release_date
- payer_id
- payment_method_id
- tax_details
- transaction_amount
- document_info

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Precio de venta del ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}/sale_price`  
**Autenticación:** No documentado en la fuente.

Referencia para identificar el precio de venta del ítem.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Datos del pedido

**Método:** `GET`  
**Ruta:** `/orders`  
**Autenticación:** No documentado en la fuente.

Referencia para obtener datos de la orden vinculada al detalle de facturación.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Descuentos de la orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}/discounts`  
**Autenticación:** No documentado en la fuente.

Referencia para consultar descuentos y campañas aplicados a la orden.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Orders de un pack

**Método:** `GET`  
**Ruta:** `/packs`  
**Autenticación:** No documentado en la fuente.

Referencia para identificar las órdenes dentro de un pack.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Estado de oferta promocional

**Método:** `GET`  
**Ruta:** `/seller-promotions/offers/{offer_id}`  
**Autenticación:** No documentado en la fuente.

Referencia para consultar cambios y estado de una oferta.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Costo del envío

**Método:** `GET`  
**Ruta:** `/shipments`  
**Autenticación:** No documentado en la fuente.

Referencia para consultar el costo de envío.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/provisiones](https://developers.mercadolibre.com.co/es_co/provisiones)  
**Captura:** 2026-10-08T22:52:37.232Z
