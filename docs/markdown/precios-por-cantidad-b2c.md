---
id: "precios-por-cantidad-b2c"
title: "Precios por cantidad B2C"
section: "Guía para productos"
subsection: "Precios por cantidad"
url: "https://developers.mercadolibre.com.co/es_co/precios-por-cantidad-b2c"
source_updated_at: "18/09/2026"
captured_at: "2026-10-08T22:52:31.595Z"
sha256: "6a45ee9e4317976dfdb6cb4f0f4d19df2e2bfaa5fb8a74936ef26bffa2d20a3e"
---

# Precios por cantidad B2C

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 18/09/2026  
**Captura:** 2026-10-08T22:52:31.595Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/precios-por-cantidad-b2c](https://developers.mercadolibre.com.co/es_co/precios-por-cantidad-b2c)

## Resumen

Documenta los descuentos porcentuales por cantidad para compradores B2C en neumáticos. La guía describe disponibilidad MLB/MLM/MLA con fechas de activación indicadas por país, máximo de dos rangos y cantidades mínimas 2 y 4. Para escribir se requiere la versión actual del precio mediante el header x-version.

## Contenido y conceptos documentados

- Los nodos están en price_per_quantity[] como type=discount_percentage, percentage y conditions con channel_marketplace, min_purchase_unit y eligible=true. No usan user_type_business.
- El POST reemplaza la lista completa: omitir un id existente elimina ese nodo; para modificar un precio se elimina y se crea uno nuevo. No hay actualización in situ.
- Antes de escribir, GET /items/{item_id}/prices?display_version=true devuelve version; enviar esa versión como x-version en la escritura. En Automotive Tires solo se permiten dos rangos, min_purchase_unit 2 y 4.
- Los precios B2C aparecen en price_per_quantity, mientras prices[] conserva los nodos estándar. El precio final se consulta con sale_price?quantity=...; el metadata puede marcar is_price_per_quantity=true.

En los ejemplos de la fuente se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Identificar ítem con precio por cantidad

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la publicación y su tag standard_price_by_quantity.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id y tags.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de ítem con tag de PxQ.

### Leer precios y versión

**Método:** `GET`  
**Ruta:** `/items/{item_id}/prices`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene la configuración y version actual antes de escribir PxQ B2C.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `display_version` (query, obligatorio): Enviar true para incluir version.
- `show-all-prices` (header, obligatorio): true en el ejemplo para incluir rangos.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, prices[], version.

**Errores documentados**

- Si el header x-version no se envía en escritura, la API devuelve error.

**Ejemplos**

- Ejemplo display_version=true y show-all-prices=true.

### Consultar precio ganador por cantidad

**Método:** `GET`  
**Ruta:** `/items/{item_id}/sale_price`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene precio unitario aplicable para una cantidad dada.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `quantity` (query, opcional): Cantidad consultada; el ejemplo usa 5.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Precio de venta y metadata; is_price_per_quantity=true cuando el ganador es PxQ B2C.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con quantity=5.

### Configurar PxQ porcentual B2C

**Método:** `POST`  
**Ruta:** `/items/{item_id}/prices/price-per-quantity`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Sustituye la lista de rangos de descuentos por cantidad del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `x-version` (header, obligatorio): Versión actual obtenida del GET prices.
- `price_per_quantity` (body, obligatorio): Lista completa; omitir id existente lo elimina y nodos sin id crean precio.
- `type` (body, obligatorio): discount_percentage.
- `percentage` (body, obligatorio): Porcentaje mayor que 0 y menor que 100.
- `conditions.min_purchase_unit` (body, obligatorio): Solo 2 o 4 para neumáticos.
- `conditions.eligible` (body, obligatorio): Debe ser true.

**Solicitud**

price_per_quantity[] de tipo discount_percentage con percentage y conditions.context_restrictions=[channel_marketplace], min_purchase_unit 2/4 y eligible=true.

**Respuesta**

Objeto de precios con version y price_per_quantity[] con id, percentage y conditions.

**Errores documentados**

- 400 bad.request: se permiten como máximo 2 entries para channel_marketplace.
- 400 bad.request: falta version (header x-version).
- 409 item.version: versión enviada no es la actual.
- 400: porcentaje fuera de rango o conditions.eligible distinto de true.

**Ejemplos**

- Ejemplo de dos rangos al 15% y 17,5%.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/precios-por-cantidad-b2c](https://developers.mercadolibre.com.co/es_co/precios-por-cantidad-b2c)  
**Captura:** 2026-10-08T22:52:31.595Z
