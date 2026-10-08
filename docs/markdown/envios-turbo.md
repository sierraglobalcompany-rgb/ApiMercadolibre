---
id: "envios-turbo"
title: "Envíos Turbo"
section: "Guía para productos"
subsection: "Mercado Envíos 2"
url: "https://developers.mercadolibre.com.co/es_co/envios-turbo"
source_updated_at: "11/02/2026"
captured_at: "2026-10-08T22:51:43.948Z"
sha256: "26bfe82a2f7f4483e5024f84e28b9f014ae5a9e8b66893690dd473de8d621e1d"
---

# Envíos Turbo

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 11/02/2026  
**Captura:** 2026-10-08T22:51:43.948Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/envios-turbo](https://developers.mercadolibre.com.co/es_co/envios-turbo)

## Resumen

Describe Turbo como entregas rápidas de menos de tres horas basadas en la logística Flex. La página enumera áreas metropolitanas cubiertas, configuración de suscripciones, radio y rangos de entrega, así como identificación Turbo en los envíos.

## Contenido y conceptos documentados

- La fuente declara disponibilidad para AMBA (Argentina), São Paulo (Brasil) y Santiago (Chile), aunque la introducción destaca AMBA y São Paulo. Es requisito previo tener Flex activo y cumplir condiciones de cuenta de prueba descritas en la guía.
- Las llamadas de Flex/Turbo comparten límite de 1000 rpm. Las dimensiones y peso máximos se detallan en la sección de configuración/ítems; consultar las restricciones de producto antes de activar.
- La suscripción devuelve mode TURBO/FLEX, service_id, origin, status y configuration. Para el radio, la fuente da límites disponibles por respuesta; para rangos, los valores From/To se toman de configuration.accurate_ranges y deben enviarse todos los rangos activos al actualizar.
- La consulta de shipment identifica Turbo por la etiqueta turbo. En algunos recursos relacionados la fuente advierte diferencias de tags; no convierte esas menciones en operaciones documentadas aquí.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar radio de cobertura Turbo

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/coverage/radius/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene radio vigente y, con show_availables, límites disponibles.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `show_availables` (query, opcional): show_availables boolean opcional

**Solicitud**

No documentado en la fuente.

**Respuesta**

radius y availables.radius.min/max.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo radius=5000.

### Consultar rangos de entrega Turbo

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/delivery-ranges/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene ventanas y rangos configurados y opciones disponibles.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `show_availables` (query, opcional): show_availables boolean opcional

**Solicitud**

No documentado en la fuente.

**Respuesta**

delivery_window, delivery_ranges por día y availables (capacity, rangos, ventanas y días).

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con varios rangos horarios.

### Consultar suscripciones Turbo/Flex

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/subscriptions/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Recupera suscripciones y service_id del usuario.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

site_id, user_id, service_id, mode, origin, status y configuration.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con modos TURBO y FLEX.

### Identificar envío Turbo

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Consulta el envío para reconocer la etiqueta Turbo.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

tags incluye turbo para identificar el tipo logístico.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de envío con tag turbo.

### Actualizar radio Turbo

**Método:** `PUT`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/coverage/radius/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Actualiza el radio de cobertura del servicio.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `radius` (body, obligatorio): Radio de cobertura configurado.

**Solicitud**

radius.

**Respuesta**

Códigos 200, 400, 401, 403, 404 y 500 documentados.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo request radius.

### Actualizar rangos Turbo

**Método:** `PUT`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/delivery-ranges/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Actualiza la configuración de rangos del vendedor.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `delivery_window` (body, opcional): Ventana de entrega.
- `delivery_ranges` (body, obligatorio): Rangos activos; deben enviarse todos los activos.

**Solicitud**

delivery_window y delivery_ranges; para conservar rangos se deben enviar todos los activos.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente exige rangos disponibles exactos de configuration.accurate_ranges.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/envios-turbo](https://developers.mercadolibre.com.co/es_co/envios-turbo)  
**Captura:** 2026-10-08T22:51:43.948Z
