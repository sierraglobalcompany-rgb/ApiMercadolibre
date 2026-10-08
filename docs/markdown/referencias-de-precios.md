---
id: "referencias-de-precios"
title: "Referencias de precios"
section: "Guía para productos"
subsection: "Precios y Costos"
url: "https://developers.mercadolibre.com.co/es_co/referencias-de-precios"
source_updated_at: "17/12/2025"
captured_at: "2026-10-08T22:52:44.247Z"
sha256: "10131592f458a1241c95db4b2ae91a905f7cb339be2bb70f429583324463345a"
---

# Referencias de precios

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 17/12/2025  
**Captura:** 2026-10-08T22:52:44.247Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/referencias-de-precios](https://developers.mercadolibre.com.co/es_co/referencias-de-precios)

## Resumen

Explica las referencias de precios que Mercado Libre calcula para orientar el precio competitivo de un producto. Permite obtener los ítems del vendedor que cuentan con referencia y consultar el detalle asociado a un ítem.

## Contenido y conceptos documentados

### Consulta y restricciones

- La consulta por vendedor requiere que el usuario exista; el detalle requiere que el ítem exista. Ambas llamadas muestran autenticación Bearer.
- La lista devuelve `total` e `items`. El detalle incluye estado, moneda, precio actual/sugerido, niveles de precio, costos, diferencia porcentual, comparables y datos de promociones, cuando estén disponibles.
- La página documenta respuestas de error 401 para token inválido o ítem ajeno al vendedor y 404 para recurso no encontrado. El cuerpo de solicitud: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Detalle de referencia por ítem

**Método:** `GET`  
**Ruta:** `/suggestions/items/$ITEM_ID/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene precios sugeridos, comparables y datos de costos/promociones para el ítem.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- item_id
- status
- currency_id
- ratio
- current_price
- suggested_price
- lowest_price
- internal_price
- costs
- selling_fees
- shipping_fees
- applicable_suggestion
- percent_difference
- metadata
- graph
- compared_values
- promotion_detail

**Errores documentados**

- ```json {   "code": 401,   "meaning": "Caller no es propietario del ítem o access token inválido." } ```
- ```json {   "code": 404,   "meaning": "Referencia/ítem no encontrado." } ```

**Ejemplos**

- Precondición: el ítem debe existir.

### Ítems del usuario con referencia de precio

**Método:** `GET`  
**Ruta:** `/suggestions/user/$USER_ID/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista los ítems del vendedor que tienen referencias de precio.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- total
- items[]

**Errores documentados**

- ```json {   "code": 401,   "meaning": "El token no es del propietario del ítem o es inválido." } ```
- ```json {   "code": 404,   "meaning": "Ítem/recurso no encontrado." } ```

**Ejemplos**

- Precondición: el usuario debe existir.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/referencias-de-precios](https://developers.mercadolibre.com.co/es_co/referencias-de-precios)  
**Captura:** 2026-10-08T22:52:44.247Z
