---
id: "pxq-porcentaje-b2b"
title: "Precios por cantidad porcentaje B2B"
section: "Guía para productos"
subsection: "Precios por cantidad"
url: "https://developers.mercadolibre.com.co/es_co/pxq-porcentaje-b2b"
source_updated_at: "01/10/2026"
captured_at: "2026-10-08T22:52:32.943Z"
sha256: "310cb5de072065bf1dd28d65734730e4e415b9523b96f3d476c112fa7ca98e3d"
---

# Precios por cantidad porcentaje B2B

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 01/10/2026  
**Captura:** 2026-10-08T22:52:32.943Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/pxq-porcentaje-b2b](https://developers.mercadolibre.com.co/es_co/pxq-porcentaje-b2b)

## Resumen

Explica PxQ B2B porcentual: rangos de descuento progresivos calculados sobre el precio vigente, de modo que el porcentaje se conserva cuando cambia el precio base o hay promoción. Disponible en MLB, MLM, MLC y MLA para vendedores business habilitados; la fuente indica la futura discontinuación del modelo absoluto el 27/10/2026.

## Contenido y conceptos documentados

- Cada ítem admite una tabla de hasta cinco rangos; min_purchase_unit puede ir de 1 a 100 y el porcentaje debe aumentar al aumentar la cantidad mínima. Para la mayoría de dominios B2B se exige user_type_business en context_restrictions; Automotive Tires tiene condiciones específicas.
- Las recomendaciones previas calculan cantidades, precios sugeridos, descuento, margen y costo logístico; el request admite hasta cinco cantidades. La guía dice consultar recomendaciones antes de configurar PxQ.
- Para escribir, primero consultar prices con display_version=true y enviar la versión en X-Version. price_per_quantity[] usa discount_percentage, percentage y conditions con channel_marketplace, user_type_business, min_purchase_unit y eligible=true.
- Los cambios agregan, conservan o quitan nodos según ids; quitar todos requiere array vacío. remove-absolute-pxq=true sustituye nodos absolutos por los nuevos porcentuales. Automotive Tires en MLA tiene bloqueo indicado para PxQ B2B desde 21/07/2026.
- Los errores descritos cubren X-Version ausente/obsoleta, id inexistente, porcentaje inválido, eligible ausente, orden de descuentos, precio recomendado, cantidades incoherentes, máximo de rangos y dominio de neumáticos.

En los ejemplos de la fuente se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /items/{ITEM_ID}/prices/standard/quantity

La fuente menciona la ruta /items/{ITEM_ID}/prices/standard/quantity, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/items/{ITEM_ID}/prices/standard/quantity`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /orders

La fuente menciona la ruta /orders, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/orders`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Identificar ítem con tabla PxQ

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta tag standard_price_by_quantity.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id y tags.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de publicación con precio por cantidad.

### Consultar precios y versión

**Método:** `GET`  
**Ruta:** `/items/{item_id}/prices`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene nodos de precio, rangos B2B y version actual.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `display_version` (query, obligatorio): true para obtener version.
- `show-all-prices` (header, obligatorio): true en ejemplo para exponer todos los rangos.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, prices[], version y price_per_quantity[] con condiciones.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de lectura de versión y tabla de precios.

### Consultar precio unitario B2B

**Método:** `GET`  
**Ruta:** `/items/{item_id}/sale_price`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Resuelve el precio aplicado a contexto business y cantidad.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `context` (query, obligatorio): Debe incluir user_type_business; ejemplo agrega channel_marketplace.
- `quantity` (query, opcional): Cantidad consultada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Precio ganador contextualizado para cantidad.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con contexto business y quantity.

### Consultar habilitación B2B

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Verifica tag business del usuario.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id y tags; la etiqueta business identifica usuarios habilitados.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de usuario con tag business.

### Configurar PxQ porcentual B2B

**Método:** `POST`  
**Ruta:** `/items/{item_id}/prices/price-per-quantity`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea, conserva o elimina la tabla porcentual por cantidad.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `remove-absolute-pxq` (query, opcional): true reemplaza rangos absolutos existentes.
- `X-Version` (header, obligatorio): Versión actual del ítem, obligatoria.
- `price_per_quantity` (body, obligatorio): Lista de rangos; puede ser [] para eliminarlos todos.
- `type` (body, obligatorio): discount_percentage.
- `percentage` (body, obligatorio): Mayor que 0 y menor que 100; aumenta según cantidad.
- `conditions.context_restrictions` (body, obligatorio): channel_marketplace y user_type_business en los casos documentados.
- `conditions.min_purchase_unit` (body, obligatorio): Cantidad mínima; rango general documentado 1–100.
- `conditions.eligible` (body, obligatorio): Debe ser true.

**Solicitud**

price_per_quantity[] con type=discount_percentage, percentage y conditions (context_restrictions, min_purchase_unit, eligible=true).

**Respuesta**

prices[] y price_per_quantity[] con porcentajes, id, last_updated y conditions.

**Errores documentados**

- 400 bad.request: falta X-Version, id PxQ inexistente, porcentaje inválido o eligible distinto de true.
- 409 item.version: la versión no es la actual.
- Otros errores documentados: descuentos no crecientes, precio resultante sobre recomendado, cantidad incoherente, exceso de rangos y Automotive Tires.

**Ejemplos**

- Ejemplo de tabla porcentual con X-Version y de eliminación con array vacío.

### Solicitar recomendaciones de precios

**Método:** `POST`  
**Ruta:** `/prices-per-quantity/v1/recommendations`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Calcula rangos sugeridos en función de cantidad, precio estándar, moneda y ahorro logístico.

**Parámetros**

- `item_id` (body, obligatorio): ID de ítem con prefijo de sitio.
- `range_item_quantities` (body, opcional): Cantidades a calcular; máximo cinco.
- `price.standard_amount` (body, obligatorio): Precio estándar.
- `price.currency` (body, obligatorio): Moneda.

**Solicitud**

item_id, range_item_quantities opcional (hasta 5, cada una >=1) y price.standard_amount/currency.

**Respuesta**

site_id, item_id, seller_id, precio y recommendations[] con cantidad, importe, descuentos, profit y shipping.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con cantidades 2, 5 y 10.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/pxq-porcentaje-b2b](https://developers.mercadolibre.com.co/es_co/pxq-porcentaje-b2b)  
**Captura:** 2026-10-08T22:52:32.943Z
