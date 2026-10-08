---
id: "estados-de-ordenes-me1"
title: "Estados de órdenes y seguimiento"
section: "Guía para productos"
subsection: "Mercado Envíos 1"
url: "https://developers.mercadolibre.com.co/es_co/estados-de-ordenes-me1"
source_updated_at: "17/09/2026"
captured_at: "2026-10-08T22:51:45.719Z"
sha256: "1af30075457cad6e3fba0872b092b03b31d76b80c771115d39c96f9a1a448d5f"
---

# Estados de órdenes y seguimiento

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 17/09/2026  
**Captura:** 2026-10-08T22:51:45.719Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/estados-de-ordenes-me1](https://developers.mercadolibre.com.co/es_co/estados-de-ordenes-me1)

## Resumen

Explica cómo relacionar una orden con su envío y notificar cambios de estado para Mercado Envíos 1. La guía recomienda la ruta V2 seller_notifications; la V1 se marca como antigua y con descontinuación indicada para el 31/10.

## Contenido y conceptos documentados

- GET orders/{order_id}/shipments entrega el id del envío que se utilizará para notificar.
- La notificación V2 recibe status, substatus y campos de seguimiento, además de payload.service_id, comment y date. La fecha debe estar en ISO 8601 con zona horaria; tracking_number y tracking_url son opcionales pero deben enviarse juntos. service_id varía por país (MLB 11, MLA 154, MLM 231876, MLC 282578, MCO 282579, MLU 282604, MPE 361180).
- Antes de reportar un subestado de Shipped, la fuente exige registrar primero el evento con status null (en camino); si no, el shipment no se actualiza.
- La fuente advierte que la operación V1 está planificada para descontinuarse el 31/10 y recomienda V2. Para subestados de Shipped, primero debe notificarse el evento con status null (en camino). Errores documentados incluyen fecha previa al envío, remitente incorrecto, modo distinto de ME1, combinación de estado/subestado inválida, JSON inválido, rate limit, indisponibilidad temporal y error interno.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Obtener envío de la orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}/shipments`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Recupera el shipment asociado a una orden ME1.

**Parámetros**

- `order_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id (shipment_id), mode, created_by, order_id, status y substatus.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con mode=me1.

### Notificar estado de envío V1 (antigua)

**Método:** `POST`  
**Ruta:** `/shipments/{shipment_id}/seller_notifications`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Ruta antigua de notificaciones; la fuente indica descontinuación para 31/10.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente identifica esta ruta como V1 antigua.

### Notificar estado de envío V2

**Método:** `POST`  
**Ruta:** `/v2/shipments/{shipment_id}/seller_notifications`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Registra una actualización de estado/tracking de ME1.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `payload` (body, obligatorio): Objeto con service_id, comment y date.
- `tracking_number` (body, opcional): Opcional; debe acompañarse con tracking_url.
- `tracking_url` (body, opcional): Opcional; debe acompañarse con tracking_number.
- `status` (body, obligatorio): shipped, delivered o not_delivered.
- `substatus` (body, obligatorio): Debe enviarse; JSON null si no aplica.

**Solicitud**

payload.service_id requerido; payload.date requerido en ISO 8601 con zona horaria; payload.comment opcional; tracking_number y tracking_url opcionales pero deben enviarse juntos; status requerido (shipped, delivered o not_delivered); substatus debe estar presente y puede ser JSON null. service_id por site: MLB=11, MLA=154, MLM=231876, MLC=282578, MCO=282579, MLU=282604, MPE=361180.

**Respuesta**

HTTP 200 con {status: OK}; error con status_code, error_code, message, timestamp y request_id.

**Errores documentados**

- 400 event_date_before_shipment_creation_date: fecha anterior a la creación del envío.
- 403 forbidden_client: caller.id no corresponde al remitente del envío.
- 400 shipment_mode_is_not_me1: el envío no pertenece a ME1.
- 403 bad_request: combinación status-substatus no permitida.
- 400 invalid_seller_json_format: formato JSON inválido.
- 429: límite de tasa alcanzado.
- 503: servicio temporalmente no disponible.
- 500: error interno de procesamiento.

**Ejemplos**

- Ejemplo de notificación delivered con payload y tracking.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/estados-de-ordenes-me1](https://developers.mercadolibre.com.co/es_co/estados-de-ordenes-me1)  
**Captura:** 2026-10-08T22:51:45.719Z
