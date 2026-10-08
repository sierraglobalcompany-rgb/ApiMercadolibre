---
id: "precio-por-cantidad"
title: "Precio por cantidad"
section: "Guía para productos"
subsection: "Precios por cantidad"
url: "https://developers.mercadolibre.com.co/es_co/precio-por-cantidad"
source_updated_at: "25/08/2026"
captured_at: "2026-10-08T22:52:24.852Z"
sha256: "4e58e2856f7aa70b3bdb9bf28dc1b5b14685116023974a1d2889c9e9368196fb"
---

# Precio por cantidad

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 25/08/2026  
**Captura:** 2026-10-08T22:52:24.852Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/precio-por-cantidad](https://developers.mercadolibre.com.co/es_co/precio-por-cantidad)

## Resumen

Gestiona precios mayoristas absolutos B2B mediante rangos de cantidad mínima. La guía señala que el endpoint heredado será discontinuado desde el 27/10/2026 para PxQ absoluto; seguirá destinado a Precios netos por cantidad. La disponibilidad descrita es MLB, MLM, MLC y MLA, para vendedores habilitados con tag business.

## Contenido y conceptos documentados

- Cada rango se representa como un precio standard con conditions.min_purchase_unit y context_restrictions que incluyen channel_marketplace y user_type_business. Una publicación admite una única tabla y hasta cinco rangos, con precio decreciente al aumentar la cantidad.
- Al modificar la tabla, enviar solo el id conserva el nodo; omitir un id existente lo elimina; enviar un nodo sin id crea precio. La respuesta puede asignar un id diferente al enviado. Moneda debe coincidir con el precio estándar; la guía indica error 404 si difiere.
- Los vendedores habilitados se identifican con tag business en /users; las publicaciones con la configuración usan standard_price_by_quantity. Los cambios notifican el tópico items prices.
- La consulta de precios puede usar el header show-all-prices; sale_price recibe context y quantity para resolver el precio por canal, tipo de comprador y cantidad.

En los ejemplos de la fuente se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /orders

La fuente menciona la ruta /orders, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/orders`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Identificar publicación con PxQ

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el ítem para detectar la etiqueta standard_price_by_quantity.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

tags de la publicación; se identifica standard_price_by_quantity.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de publicación con la etiqueta PxQ.

### Consultar tabla de precios

**Método:** `GET`  
**Ruta:** `/items/{item_id}/prices`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve precios vigentes; show-all-prices permite solicitar la vista ampliada de PxQ.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `show-all-prices` (header, opcional): TRUE/FALSE, opcional para ver todos los rangos.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id y prices[] con tipo, importe, moneda, condiciones y restricciones de contexto.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de prices con show-all-prices: TRUE.

### Calcular precio de venta por cantidad

**Método:** `GET`  
**Ruta:** `/items/{item_id}/sale_price`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Resuelve el precio ganador para canal y comprador con la cantidad solicitada.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `context` (query, opcional): Canales y contexto de comprador; el ejemplo usa channel_marketplace,user_type_business.
- `quantity` (query, opcional): Cantidad solicitada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Precio de venta calculado para el contexto y la cantidad.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con channel_marketplace,user_type_business y cantidad.

### Consultar tag Business

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Permite comprobar si el vendedor tiene el tag business asociado a PxQ.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, tags y demás datos de usuario.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La respuesta incluye business en tags.

### Definir precios absolutos por cantidad

**Método:** `POST`  
**Ruta:** `/items/{item_id}/prices/standard/quantity`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea, conserva o elimina nodos standard de la tabla PxQ.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `prices` (body, obligatorio): Lista de precios por cantidad.
- `id` (body, opcional): Si se envía conserva un nodo existente; omitirlo lo elimina; sin id crea un precio.
- `amount` (body, opcional): Monto del precio.
- `currency_id` (body, opcional): Moneda, igual a la del precio estándar.
- `conditions` (body, opcional): Incluye context_restrictions y min_purchase_unit.

**Solicitud**

prices[] con id para conservar un nodo; para crear, amount, currency_id y conditions.context_restrictions/min_purchase_unit.

**Respuesta**

id del ítem y prices[] con id, amount, currency_id y conditions.

**Errores documentados**

- 404: la moneda del PxQ y la del precio estándar son distintas.
- La omisión de un id existente elimina ese nodo; más de cinco rangos no está permitido.

**Ejemplos**

- Ejemplos con una tabla y con cinco rangos.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/precio-por-cantidad](https://developers.mercadolibre.com.co/es_co/precio-por-cantidad)  
**Captura:** 2026-10-08T22:52:24.852Z
