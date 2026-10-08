---
id: "mercadoenvios-modo-2"
title: "Mercado Envíos 2"
section: "Guía para productos"
subsection: "Mercado Envíos 2"
url: "https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-2"
source_updated_at: "06/07/2026"
captured_at: "2026-10-08T22:52:09.574Z"
sha256: "d6dc7aaa8e9b6a3e863bf7ad099aa4fc731e61d25fd90d89a89b5b100cc0c31a"
---

# Mercado Envíos 2

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 06/07/2026  
**Captura:** 2026-10-08T22:52:09.574Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-2](https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-2)

## Resumen

Reúne el flujo de Mercado Envíos 2: agregar la modalidad a publicaciones, validar preferencias y atributos del dominio, consultar envíos y obtener etiquetas; también explica cómo consultar órdenes y calcular el total con envío.

## Contenido y conceptos documentados

- Para publicar se informa `shipping.mode` y se consultan preferencias del usuario/categoría; para atributos dependientes de dominio se usa `shipping_attributes`. La información adicional del envío se obtiene de `/shipments`, pues la orden conserva la identificación del envío.
- Las etiquetas admiten `response_type=pdf` o `zpl2` y `shipment_ids`. Para consultas con nueva estructura se muestra `X-Format-New: true`. La fuente lista errores 400 por validaciones/campos obligatorios o formato de ID, 401 por token inválido, 403 por falta de permisos y 404 cuando ítem/producto/dominio no existe. Para etiquetas se documentan medidas de impresión por país y estados que permiten reimpresión.
- Autenticación mostrada: OAuth Bearer. Otros campos no detallados: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### GET /catalog_domains/{DOMAIN_ID}/shipping_attributes

**Método:** `GET`  
**Ruta:** `/catalog_domains/{DOMAIN_ID}/shipping_attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta atributos requeridos por dominio.

**Parámetros**

- `DOMAIN_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Validación de consistencia, campos obligatorios o formato de IDs." } ```
- ```json {   "code": "401",   "meaning": "Token inválido." } ```
- ```json {   "code": "403",   "meaning": "Falta de permisos." } ```
- ```json {   "code": "404",   "meaning": "Ítem, producto o dominio no encontrado." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /categories/{CATEGORY_ID}/shipping_preferences

**Método:** `GET`  
**Ruta:** `/categories/{CATEGORY_ID}/shipping_preferences`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta requisitos/preferencias de envío de la categoría.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Validación de consistencia, campos obligatorios o formato de IDs." } ```
- ```json {   "code": "401",   "meaning": "Token inválido." } ```
- ```json {   "code": "403",   "meaning": "Falta de permisos." } ```
- ```json {   "code": "404",   "meaning": "Ítem, producto o dominio no encontrado." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /orders/{ORDER_ID}

**Método:** `GET`  
**Ruta:** `/orders/{ORDER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la orden y su identificador de envío.

**Parámetros**

- `ORDER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "shipping.id",
    "pack_id"
  ],
  "summary": "La orden contiene la identificación del envío; sus detalles adicionales se consultan en shipments."
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /shipment_labels

**Método:** `GET`  
**Ruta:** `/shipment_labels`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Genera/obtiene etiquetas para `shipment_ids`; admite `response_type=pdf` o `zpl2`.

**Parámetros**

- `shipment_ids` (query, obligatorio): Uno o varios identificadores de envío separados por coma.
- `response_type` (query, obligatorio): Formato documentado: pdf o zpl2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Validación de consistencia, campos obligatorios o formato de IDs." } ```
- ```json {   "code": "401",   "meaning": "Token inválido." } ```
- ```json {   "code": "403",   "meaning": "Falta de permisos." } ```
- ```json {   "code": "404",   "meaning": "Ítem, producto o dominio no encontrado." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /shipments/{SHIPMENT_ID}

**Método:** `GET`  
**Ruta:** `/shipments/{SHIPMENT_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalles del envío; el ejemplo nuevo usa `X-Format-New: true`.

**Parámetros**

- `SHIPMENT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "status",
    "substatus",
    "mode",
    "logistic_type"
  ]
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Validación de consistencia, campos obligatorios o formato de IDs." } ```
- ```json {   "code": "401",   "meaning": "Token inválido." } ```
- ```json {   "code": "403",   "meaning": "Falta de permisos." } ```
- ```json {   "code": "404",   "meaning": "Ítem, producto o dominio no encontrado." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /users/{USER_ID}/shipping_preferences

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/shipping_preferences`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta preferencias de envío del vendedor.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Validación de consistencia, campos obligatorios o formato de IDs." } ```
- ```json {   "code": "401",   "meaning": "Token inválido." } ```
- ```json {   "code": "403",   "meaning": "Falta de permisos." } ```
- ```json {   "code": "404",   "meaning": "Ítem, producto o dominio no encontrado." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /items

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Publica un ítem con configuración de ME2.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "shipping.mode"
  ],
  "summary": "El ejemplo publica con configuración ME2."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Validación de consistencia, campos obligatorios o formato de IDs." } ```
- ```json {   "code": "401",   "meaning": "Token inválido." } ```
- ```json {   "code": "403",   "meaning": "Falta de permisos." } ```
- ```json {   "code": "404",   "meaning": "Ítem, producto o dominio no encontrado." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-2](https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-2)  
**Captura:** 2026-10-08T22:52:09.574Z
