---
id: "envios-colectas-places"
title: "Envíos Colecta y Places"
section: "Guía para productos"
subsection: "Mercado Envíos 2"
url: "https://developers.mercadolibre.com.co/es_co/envios-colectas-places"
source_updated_at: "25/09/2026"
captured_at: "2026-10-08T22:51:38.852Z"
sha256: "6f46bb1c3c61f995b1583f9cf3664a75a4c44574da64339ff8c68032ed009cac"
---

# Envíos Colecta y Places

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 25/09/2026  
**Captura:** 2026-10-08T22:51:38.852Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/envios-colectas-places](https://developers.mercadolibre.com.co/es_co/envios-colectas-places)

## Resumen

Documenta la consulta y configuración de capacidad de despacho, tiempos de preparación y horarios para vendedores y nodos de Places. El flujo cambia a node_id cuando hay Multi-Origin, y las rutas dependen del tipo logístico o de servicio.

## Contenido y conceptos documentados

- Cobertura descrita: Argentina, Brasil, México, Chile, Colombia y Uruguay; Perú aparece con drop_off. La página menciona Colecta rápida en Brasil como xd_same_day.
- La capacidad se representa por día con capacity_min, capacity_max y capacity.value. Para actualizar, maximum debe ser false y value no puede exceder capacity_max; la fuente documenta errores 400 por formato, máximo e infinito y 404 por logística no válida.
- El tiempo de preparación usa SERVICE_TYPE=carrier_pickup y header X-Version:v3. Los tiempos tienen formato HH:MM; si processing_times va vacío se aplican valores por defecto de la logística documentada, los días bloqueados se ignoran y el cambio del día vigente aplica a la semana siguiente.
- El horario incluye schedule por día, work y detail con from, to, cutoff, milkrun_same_day y otros campos. En Multi-Origin se debe consultar/configurar por NETWORK_NODE_ID.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar horario de nodo

**Método:** `GET`  
**Ruta:** `/nodes/{network_node_id}/schedule/{logistic_type}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Consulta horarios de despacho en un nodo.

**Parámetros**

- `network_node_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `logistic_type` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

seller_id y schedule por día.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo xd_drop_off.

### Consultar preparación de nodo

**Método:** `GET`  
**Ruta:** `/nodes/{network_node_id}/service/{service_type}/processing_time_tool`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lee tiempos de preparación del nodo.

**Parámetros**

- `network_node_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_type` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `X-Version` (header, obligatorio): Header X-Version: v3 según llamada por servicio

**Solicitud**

No documentado en la fuente.

**Respuesta**

Opciones de tiempo y estado por día.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de nodo con carrier_pickup.

### Consultar capacidad de nodo

**Método:** `GET`  
**Ruta:** `/nodes/{node_id}/capacity_middleend`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lee la capacidad por día en un nodo de Places.

**Parámetros**

- `node_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

peak_season_mode y capacities por día.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con node_id.

### Consultar capacidad de vendedor

**Método:** `GET`  
**Ruta:** `/users/{user_id}/capacity_middleend/{logistic_type}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lee los límites y configuración de capacidad por día para la logística.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `logistic_type` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

peak_season_mode y capacities con day, capacity_min, capacity_max, capacity.value, maximum, source, can_add_capacity, can_subtract_capacity e intervention.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo logistic_type=cross_docking.

### Consultar preparación de vendedor

**Método:** `GET`  
**Ruta:** `/users/{user_id}/service/{service_type}/processing_time_tool`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lee opciones y tiempos de preparación por día.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_type` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `X-Version` (header, obligatorio): Header X-Version: v3

**Solicitud**

No documentado en la fuente.

**Respuesta**

Por día: modified_by_meli, intervention_type, visible, enabled, current_processing_time y available_options.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- service_type documentado: carrier_pickup.

### Consultar horario de vendedor

**Método:** `GET`  
**Ruta:** `/users/{user_id}/shipping/schedule/{logistic_type}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Consulta horarios de despacho por día y logística.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `logistic_type` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

seller_id y schedule por día con work y detail (from, to, cutoff, SLA y datos logísticos).

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo cross_docking.

### Actualizar capacidad de nodo

**Método:** `PUT`  
**Ruta:** `/nodes/{network_node_id}/capacity_middleend`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Actualiza la capacidad de despacho por nodo.

**Parámetros**

- `network_node_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `capacities` (body, obligatorio): Lista de capacidades por día.

**Solicitud**

Mismo formato capacities[] que la actualización por vendedor; maximum=false.

**Respuesta**

Mensaje de éxito o error documentado.

**Errores documentados**

- 400: error de parseo; excede capacidad máxima; capacidad infinita no permitida. 404: tipo logístico no válido.

**Ejemplos**

- La fuente indica reutilizar el JSON de usuario.

### Actualizar preparación de nodo

**Método:** `PUT`  
**Ruta:** `/nodes/{network_node_id}/service/{service_type}/processing_time_tool`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Guarda tiempos por día del nodo.

**Parámetros**

- `network_node_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_type` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `X-Version` (header, obligatorio): Header X-Version: v3
- `processing_times` (body, obligatorio): Tiempos de preparación HH:MM por día.

**Solicitud**

Mismo objeto processing_times con valores HH:MM.

**Respuesta**

message de confirmación.

**Errores documentados**

- 400: invalid processing time configuration.

**Ejemplos**

- La página indica utilizar el mismo JSON de vendedor.

### Actualizar capacidad de vendedor

**Método:** `PUT`  
**Ruta:** `/users/{user_id}/capacity_middleend/{logistic_type}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Actualiza la capacidad por día del vendedor.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `logistic_type` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `capacities` (body, obligatorio): Lista de capacidades por día.

**Solicitud**

capacities[] con day y capacity.value; maximum debe ser false.

**Respuesta**

Mensaje de éxito o error documentado.

**Errores documentados**

- 400: error al parsear body; capacity value exceeds maximum allowed capacity; infinite capacity is not allowed. 404: not valid logistic type.

**Ejemplos**

- Ejemplo con capacidades para días de la semana.

### Actualizar preparación de vendedor

**Método:** `PUT`  
**Ruta:** `/users/{user_id}/service/{service_type}/processing_time_tool`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Guarda tiempos por día para el servicio.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_type` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `X-Version` (header, obligatorio): Header X-Version: v3
- `processing_times` (body, obligatorio): Tiempos de preparación HH:MM por día.

**Solicitud**

processing_times con días y processing_time en HH:MM.

**Respuesta**

message de confirmación.

**Errores documentados**

- 400: invalid processing time configuration.

**Ejemplos**

- Ejemplo con lunes a sábado.

### Referencia HTTP GET /users/123456789/capacity_middleend/cross_docking

**Método:** `GET`  
**Ruta:** `/users/123456789/capacity_middleend/cross_docking`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/123456789/capacity_middleend/cross_docking. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /users/123456789/service/carrier_pickup/processing_time_tool

**Método:** `GET`  
**Ruta:** `/users/123456789/service/carrier_pickup/processing_time_tool`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/123456789/service/carrier_pickup/processing_time_tool. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /users/123456789/shipping/schedule/cross_docking

**Método:** `GET`  
**Ruta:** `/users/123456789/shipping/schedule/cross_docking`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/123456789/shipping/schedule/cross_docking. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /nodes/MXP20157465171/service/carrier_pickup/processing_time_tool

**Método:** `GET`  
**Ruta:** `/nodes/MXP20157465171/service/carrier_pickup/processing_time_tool`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /nodes/MXP20157465171/service/carrier_pickup/processing_time_tool. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /nodes/MXP20157465171/schedule/xd_drop_off

**Método:** `GET`  
**Ruta:** `/nodes/MXP20157465171/schedule/xd_drop_off`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /nodes/MXP20157465171/schedule/xd_drop_off. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP PUT /users/123456789/service/carrier_pickup/processing_time_tool

**Método:** `PUT`  
**Ruta:** `/users/123456789/service/carrier_pickup/processing_time_tool`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud PUT a /users/123456789/service/carrier_pickup/processing_time_tool. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP PUT /users/123456789/capacity_middleend/cross_docking

**Método:** `PUT`  
**Ruta:** `/users/123456789/capacity_middleend/cross_docking`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud PUT a /users/123456789/capacity_middleend/cross_docking. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP PUT /nodes/MXP20157465171/service/carrier_pickup/processing_time_tool

**Método:** `PUT`  
**Ruta:** `/nodes/MXP20157465171/service/carrier_pickup/processing_time_tool`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud PUT a /nodes/MXP20157465171/service/carrier_pickup/processing_time_tool. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/envios-colectas-places](https://developers.mercadolibre.com.co/es_co/envios-colectas-places)  
**Captura:** 2026-10-08T22:51:38.852Z
