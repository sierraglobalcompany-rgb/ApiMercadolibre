---
id: "gestionar-resolucion-de-reclamos"
title: "Gestionar resolución de reclamos"
section: "Guía para productos"
subsection: "Reclamos"
url: "https://developers.mercadolibre.com.co/es_co/gestionar-resolucion-de-reclamos"
source_updated_at: "08/09/2025"
captured_at: "2026-10-08T22:52:01.135Z"
sha256: "6fbb252e3102627c7daa87b04f4ba8e3997a66b19b8f8a937d95864a49040ba7"
---

# Gestionar resolución de reclamos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 08/09/2025  
**Captura:** 2026-10-08T22:52:01.135Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestionar-resolucion-de-reclamos](https://developers.mercadolibre.com.co/es_co/gestionar-resolucion-de-reclamos)

## Resumen

Describe las opciones del vendedor para escalar un reclamo a mediación y consultar o proponer resoluciones: devolución, reembolso completo o parcial y devolución del producto. Las acciones permitidas dependen del estado, la etapa y las resoluciones esperadas del reclamo.

## Contenido y conceptos documentados

### Resoluciones y condiciones

- Las llamadas documentan autenticación `Bearer`. Abrir una disputa inicia mediación; desde ese momento cesa el contacto directo con el comprador y el rol receptor pasa a ser `mediator`.
- La consulta de resoluciones esperadas informa el estado de la resolución y el participante. Los tipos citados incluyen `product`, `refund`, `change_product` y `return_product`, relacionados con flujos PNR/PDD.
- La oferta de reembolso parcial muestra moneda, importe y porcentaje recomendado, con restricciones. La página enumera 400 por parámetro inválido o porcentaje por debajo del mínimo, 403 cuando el ClaimId no existe, 404 cuando el usuario no está autorizado y 422 cuando el reclamo no es apto para el flujo (por ejemplo, CBT o sin etiqueta de devolución).
- Para solicitar reembolso parcial, el reclamo debe corresponder a PDD, tener `return_product` pendiente y permitir `allow_partial_refund` en `available_actions`; se elige un porcentaje disponible, no 100%. La fuente indica 50% como valor por defecto si se omite y que al aceptarse se cierra el reclamo.
- Reembolso total requiere que esté disponible la acción `refund`. `allow-return` permite aceptar la devolución del producto y sustituye el flujo anterior de aceptación/carga de resolución. Los detalles de cuerpo y códigos para rutas no especificados: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /claims/partial-refund/available-offers-resolutions

La fuente menciona la ruta /claims/partial-refund/available-offers-resolutions, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/partial-refund/available-offers-resolutions`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /claims/expected-resolutions

La fuente menciona la ruta /claims/expected-resolutions, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/expected-resolutions`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /v1/claims/{claim_id}/partial-refund/available-offers

La fuente menciona la ruta /v1/claims/{claim_id}/partial-refund/available-offers, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/v1/claims/{claim_id}/partial-refund/available-offers`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar resoluciones esperadas

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/expected-resolutions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista las resoluciones y el estado/participante asociado al reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- expected_resolution
- details
- player_role
- status
- labels

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La guía menciona product, refund, change_product y return_product, además de flujos PNR/PDD.

### Consultar ofertas de reembolso parcial

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/partial-refund/available-offers`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene importes y porcentajes disponibles o recomendados para una devolución parcial.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- currency_id
- available_offers[].amount
- available_offers[].percentage
- recommendations
- restrictions

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Parámetro inválido o intento por debajo del mínimo." } ```
- ```json {   "code": 403,   "meaning": "ClaimId no existe (así lo describe la fuente)." } ```
- ```json {   "code": 404,   "meaning": "Usuario no autorizado (así lo describe la fuente)." } ```
- ```json {   "code": 422,   "meaning": "Reclamo no apto para el flujo, por ejemplo CBT o sin etiqueta de devolución." } ```

**Ejemplos**

No documentado en la fuente.

### Abrir disputa

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/actions/open-dispute`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Inicia la mediación para un reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Tras abrirla cesa el mensaje directo al comprador y el rol receptor es mediator.

### Aceptar devolución

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/expected-resolutions/allow-return`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Acepta la devolución del producto como resolución del reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La guía presenta esta operación como reemplazo del flujo anterior de aceptación/carga de resolución.

### Solicitar reembolso parcial

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/expected-resolutions/partial-refund`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Solicita un porcentaje disponible de reembolso parcial para el reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Requiere PDD, return_product pendiente y available_actions con allow_partial_refund; no admite 100%; 50% por defecto si se omite.

### Solicitar reembolso completo

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/expected-resolutions/refund`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Propone el reembolso completo cuando el reclamo permite la acción refund.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página requiere que refund figure entre las acciones disponibles.

### Referencia HTTP GET /v1/claims/{claim_id}/partial-refund/available-offers

**Método:** `GET`  
**Ruta:** `/v1/claims/{claim_id}/partial-refund/available-offers`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /v1/claims/{claim_id}/partial-refund/available-offers. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /claims/expected-resolutions

**Método:** `GET`  
**Ruta:** `/claims/expected-resolutions`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /claims/expected-resolutions. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /claims/partial-refund/available-offers-resolutions

**Método:** `GET`  
**Ruta:** `/claims/partial-refund/available-offers-resolutions`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /claims/partial-refund/available-offers-resolutions. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestionar-resolucion-de-reclamos](https://developers.mercadolibre.com.co/es_co/gestionar-resolucion-de-reclamos)  
**Captura:** 2026-10-08T22:52:01.135Z
