---
id: "envios"
title: "Envíos"
section: "Guía para productos"
subsection: "Gestionar ventas"
url: "https://developers.mercadolibre.com.co/es_co/envios"
source_updated_at: "18/09/2026"
captured_at: "2026-10-08T22:51:37.708Z"
sha256: "2d954c8f9a8fc79c38e00a362957f689017ebcac475b25620906f2ca01e30e36"
---

# Envíos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 18/09/2026  
**Captura:** 2026-10-08T22:51:37.708Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/envios](https://developers.mercadolibre.com.co/es_co/envios)

## Resumen

Referencia de recursos de Mercado Envíos para consultar estados, detalle, artículos, costos, pagos, transportista, demoras, tiempo estimado, historial y órdenes relacionadas, además de dividir un envío. Las respuestas pueden requerir el formato nuevo; la operación de órdenes usa X-New-Domain.

## Contenido y conceptos documentados

- Los ejemplos usan Authorization Bearer. La consulta del detalle solicita x-format-new: true; varias rutas de subrecurso también muestran ese header. La consulta de órdenes asociadas requiere X-New-Domain:true.
- La documentación expone recursos de tracking, etiquetas de estado/subestado, transportista, SLA, lead time y retrasos. Los campos varían por recurso y la guía incluye fechas, costos y datos de ítems/pagos.
- La operación de split recibe un motivo y una lista de paquetes; el ejemplo usa DIMENSIONS_EXCEEDED. No se debe asumir el mismo encabezado o cuerpo para los demás recursos.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Listar estados y subestados

**Método:** `GET`  
**Ruta:** `/shipment_statuses`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Devuelve el catálogo de estados de envío y sus subestados.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de id, name y substatuses.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de estados to_be_agreed y pending.

### Consultar envío

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene el detalle general del envío; usar x-format-new: true en el ejemplo documentado.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Detalle del envío; el formato incluye campos de estado, etiquetas y datos de logística.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con x-format-new: true.

### Consultar transportista

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/carrier`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Recupera URL de seguimiento y nombre del transportista.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

url y name.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con nombre y URL de tracking.

### Consultar costos

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/costs`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene los importes y participantes vinculados al costo del envío.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

gross_amount y desglose receiver/cost, entre otros campos del ejemplo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con x-format-new: true.

### Consultar demoras

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/delays`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene demoras registradas para un envío.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

shipment_id y lista delays con tipo/detalle.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con x-format-new: true.

### Consultar historial de estados

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/history`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lista transiciones de estado y subestado del envío.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

status, substatus y fechas de evento.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con x-format-new: true.

### Consultar ítems del envío

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/items`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lista los productos incluidos en el envío.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

item_id, description y quantity.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de lista de ítems.

### Consultar tiempos de entrega

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/lead_time`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Recupera información de plazo y método logístico asociado.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

option_id, shipping_method y datos de tiempos del ejemplo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con x-format-new: true.

### Consultar órdenes asociadas

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/orders`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene órdenes vinculadas al envío; el ejemplo agrega X-New-Domain:true.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `X-New-Domain` (header, obligatorio): Header X-New-Domain: true

**Solicitud**

No documentado en la fuente.

**Respuesta**

Órdenes asociadas al shipment.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con header X-New-Domain:true.

### Consultar pagos del envío

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/payments`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lista pagos asociados al envío.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

payment_id, user_id y datos de pago del ejemplo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con x-format-new: true.

### Consultar SLA del envío

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/sla`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Devuelve el estado de cumplimiento del SLA y el servicio.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

status y service.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de status on_time.

### Dividir envío

**Método:** `POST`  
**Ruta:** `/shipments/{shipment_id}/split`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Solicita dividir un envío en paquetes según el motivo indicado.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `reason` (body, obligatorio): Motivo de división; el ejemplo usa DIMENSIONS_EXCEEDED.
- `packs` (body, obligatorio): Paquetes que resultan de la división.

**Solicitud**

reason y packs; el ejemplo usa reason=DIMENSIONS_EXCEEDED.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de solicitud de split.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/envios](https://developers.mercadolibre.com.co/es_co/envios)  
**Captura:** 2026-10-08T22:51:37.708Z
