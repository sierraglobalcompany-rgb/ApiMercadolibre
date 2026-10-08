---
id: "envios-flex"
title: "Envíos Flex"
section: "Guía para productos"
subsection: "Mercado Envíos 2"
url: "https://developers.mercadolibre.com.co/es_co/envios-flex"
source_updated_at: "22/09/2026"
captured_at: "2026-10-08T22:51:40.878Z"
sha256: "ec49e0e0d20ab6e0c866051cf55ba9141809446e3c59efdd3ce51e26a96049f0"
---

# Envíos Flex

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 22/09/2026  
**Captura:** 2026-10-08T22:51:40.878Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/envios-flex](https://developers.mercadolibre.com.co/es_co/envios-flex)

## Resumen

Referencia para comprobar la compatibilidad Flex de categorías e ítems, consultar suscripciones y administrar cobertura por zonas, feriados y rangos de entrega. También cubre asociación de envíos de mensajería y asignación de conductores.

## Contenido y conceptos documentados

- Para determinar si una categoría soporta Flex, la respuesta de shipping_preferences debe incluir self_service en logistics. La habilitación puede variar por país y dominio; activar Flex convierte la publicación a ME2.
- La suscripción expone service_id, mode, origin, status y configuración. El service_id es necesario para configurar el servicio; habilitar Flex y Turbo puede producir suscripciones separadas.
- La lectura de zonas y rangos admite show_availables. La configuración de feriados y delivery-ranges se realiza para site_id, user_id y service_id. La página documenta un 422 para una configuración con rango de entrega extendido activo.
- La asociación de envíos de courier requiere vincular el usuario courier con el vendedor; sin vínculo, la fuente señala respuesta 403. Las consultas usan Bearer en sus ejemplos.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Desactivar Flex en un ítem

**Método:** `DELETE`  
**Ruta:** `/flex/sites/{site_id}/items/{item_id}/v2`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Retira el ítem de Flex.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Estado de la operación; la página documenta códigos de respuesta.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de desactivación.

### Consultar compatibilidad de categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/shipping_preferences`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Comprueba si la categoría incluye self_service entre sus tipos logísticos ME2.

**Parámetros**

- `category_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

category_id y logistics[].types/mode.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta de ejemplo con self_service.

### Consultar Flex de un ítem

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/items/{item_id}/v2`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Indica si el ítem se ofrece con Flex.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

has_flex boolean.

**Errores documentados**

- 400: dato inválido; 401: autorización inválida; 403: access token incorrecto; 404: ítem inexistente; 500: error interno.

**Ejemplos**

- Respuesta compacta {has_flex:true|false}.

### Consultar asignación del envío

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/shipments/{shipment_id}/assignment/v2`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene el conductor asignado al envío.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

driver_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta de ejemplo con driver_id.

### Consultar zonas de cobertura

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/coverage/zones/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lee zonas y opciones de cobertura Flex.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `show_availables` (query, opcional): show_availables opcional

**Solicitud**

No documentado en la fuente.

**Respuesta**

zones[] con id y cutoff (week, saturday, sunday); availables incluye las zonas disponibles cuando show_availables=true.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de consulta con show_availables.

### Consultar rangos de entrega Flex

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/delivery-ranges/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lee ventanas y rangos horarios de entrega.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `show_availables` (query, opcional): show_availables opcional

**Solicitud**

No documentado en la fuente.

**Respuesta**

delivery_window, delivery_ranges y availables cuando se solicitan.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con show_availables.

### Consultar feriados Flex

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/holidays/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene fechas de feriado configuradas para el servicio.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

holidays y datos de fecha/selección.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta con holidays.

### Consultar suscripciones Flex

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/subscriptions/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lista suscripciones del usuario, modo y service_id.

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

- Ejemplo con datos de Flex.

### Consultar estado de envío Flex

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Consulta estados y subestados del flujo Flex.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Estado/subestado y tags del envío.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de envío Flex.

### Activar Flex en un ítem

**Método:** `POST`  
**Ruta:** `/flex/sites/{site_id}/items/{item_id}/v2`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Realiza el opt-in Flex para el ítem.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Estado de la operación; la página documenta códigos de respuesta.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de activación.

### Asociar envío a courier

**Método:** `POST`  
**Ruta:** `/flex/sites/{site_id}/users/{courier_user_id}/courier-shipment/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Asocia shipment_id al usuario de mensajería que gestiona la entrega.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `courier_user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `shipment_id` (body, obligatorio): Identificador del envío asignado al courier.

**Solicitud**

shipment_id.

**Respuesta**

204 No Content en el caso exitoso; la fuente indica 403 si courier y vendedor no están vinculados.

**Errores documentados**

- 403: falta vinculación entre la cuenta courier y vendedor.

**Ejemplos**

- Ejemplo de asociación de shipment.

### Actualizar zonas de cobertura

**Método:** `PUT`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/coverage/zones/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Actualiza las zonas donde presta servicio el vendedor.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `zones` (body, obligatorio): Zonas con id y cutoff opcional.

**Solicitud**

zones[] con id y cutoff opcional; cutoff contiene week, saturday y sunday. Si se define cutoff por zona, cada zona puede usar valores distintos.

**Respuesta**

zones[] con id y cutoff; availables.zones[] puede mostrar id, label y barrios disponibles cuando se consulta con show_availables.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de request con zonas.

### Actualizar rangos de entrega Flex

**Método:** `PUT`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/delivery-ranges/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Actualiza ventanas y rangos de entrega.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `delivery_window` (body, obligatorio): Ventana de entrega.
- `delivery_ranges` (body, obligatorio): Rangos por día con capacidad, from, to y cutoff cuando corresponda.

**Solicitud**

delivery_window y delivery_ranges según ejemplo de la página.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 422: no se puede procesar mientras esté activo un rango extendido de entrega.

**Ejemplos**

- Ejemplo de body con rangos.

### Actualizar feriados Flex

**Método:** `PUT`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/holidays/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Actualiza los feriados del servicio.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `holidays` (body, obligatorio): Fechas de feriados y selección.

**Solicitud**

Lista holidays; la fuente indica selected=true para marcar días laborables habilitados.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de configuración de feriados.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/envios-flex](https://developers.mercadolibre.com.co/es_co/envios-flex)  
**Captura:** 2026-10-08T22:51:40.878Z
