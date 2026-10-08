---
id: "comision-por-vender"
title: "Costos por vender"
section: "Guía para productos"
subsection: "Precios y Costos"
url: "https://developers.mercadolibre.com.co/es_co/comision-por-vender"
source_updated_at: "03/09/2026"
captured_at: "2026-10-08T22:51:29.334Z"
sha256: "84ac01bd7f131aafd325aefef7b79a4e0cee1b1d8464dbe0e51e5c9a474252fa"
---

# Costos por vender

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 03/09/2026  
**Captura:** 2026-10-08T22:51:29.334Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/comision-por-vender](https://developers.mercadolibre.com.co/es_co/comision-por-vender)

## Resumen

Explica cómo estimar costos por venta mediante los precios de publicación del sitio, considerando precio, categoría/producto, moneda, tipo de publicación, logística, envío y tags de campañas. Incluye parámetros para Supermarket y cargos adicionales.

## Contenido y conceptos documentados

- El recurso `listing_prices` calcula componentes de costos para combinaciones de precio y atributos. La fuente destaca `fixed_fee`, `financing_add_on_fee`, `gross_amount` y `meli_percentage_fee`.
- `price` es el parámetro de entrada para calcular costos. Para aproximar el costo real se recomienda enviar `shipping_mode`, `logistic_type` y `billable_weight`; el peso facturable se expresa en gramos y es obligatorio para Argentina.
- `category_id` puede sustituirse por `catalog_product_id` para un cálculo más preciso. Se documentan `listing_type_id`, `currency_id`, `quantity`, `tags`, `shipping_modes` y campos relacionados con Supermarket.
- Para cotizar envíos en la estructura nueva, la respuesta y solicitud dependen de logística; la página indica que la ausencia de datos logísticos/peso puede provocar una comisión fija distinta de la cobrada.
- La fuente muestra error 400 `bad_request` para una solicitud incorrecta.

**Campos y respuestas:** `fixed_fee`, `financing_add_on_fee`, `gross_amount`, `meli_percentage_fee`, `price`, `category_id`, `catalog_product_id`, `currency_id`, `listing_type_id`, `logistic_type`, `shipping_mode(s)`, `billable_weight`, `tags` y `quantity`.

**Ejemplos documentados:** cálculo solo con precio, con categoría, moneda/tipo de publicación, logística y peso, y cálculo para Supermarket.

## Operaciones de API

## Conceptos y recursos asociados

### Costos por vender

Explica cómo estimar costos por venta mediante los precios de publicación del sitio, considerando precio, categoría/producto, moneda, tipo de publicación, logística, envío y tags de campañas. Incluye parámetros para Supermarket y cargos adicionales.

**Respuesta**

```json
{
  "fields": "`fixed_fee`, `financing_add_on_fee`, `gross_amount`, `meli_percentage_fee`, `price`, `category_id`, `catalog_product_id`, `currency_id`, `listing_type_id`, `logistic_type`, `shipping_mode(s)`, `billable_weight`, `tags` y `quantity`."
}
```

**Errores documentados**

- 400 bad_request: solicitud incorrecta.

**Ejemplos documentados**

- cálculo solo con precio, con categoría, moneda/tipo de publicación, logística y peso, y cálculo para Supermarket.
## Operaciones de API

### Consulta costos de publicación/venta con filtros como precio, categoría o producto, moneda, tipo de publicación y logística

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/listing_prices`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta costos de publicación/venta con filtros como precio, categoría o producto, moneda, tipo de publicación y logística.

**Parámetros**

- `site_id` (path, obligatorio): Variable de ruta documentada.
- `price` (query, obligatorio): Precio de venta del ítem.
- `category_id` (query): Categoría; puede usarse catalog_product_id para precisión de producto.
- `currency_id` (query): Moneda del sitio.
- `logistic_type` (query): Tipo logístico.
- `shipping_modes` (query): Modos de envío.
- `shipping_mode` (query): Modo de envío.
- `listing_type_id` (query): Tipo de publicación.
- `quantity` (query): Cantidad consultada.
- `tags` (query): Tag de campaña/elegibilidad; incluye supermarket_eligible.
- `billable_weight` (query): Peso facturable en gramos; obligatorio para Argentina.
- `catalog_product_id` (query): Producto de catálogo para cálculo más preciso.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "currency_id",
    "listing_type_id",
    "listing_fee_amount",
    "listing_fee_details",
    "fixed_fee",
    "gross_amount",
    "sale_fee_amount",
    "sale_fee_details",
    "financing_add_on_fee",
    "meli_percentage_fee",
    "percentage_fee"
  ]
}
```

**Errores documentados**

- 400 bad_request: solicitud inválida.

**Ejemplos**

- cálculo solo con precio, con categoría, moneda/tipo de publicación, logística y peso, y cálculo para Supermarket.

### Referencia HTTP GET /sites/MLA/listing_pricesprice=10345&listing_type_id=gold_special&category_id=MLA120350

**Método:** `GET`  
**Ruta:** `/sites/MLA/listing_pricesprice=10345&listing_type_id=gold_special&category_id=MLA120350`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /sites/MLA/listing_pricesprice=10345&listing_type_id=gold_special&category_id=MLA120350. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/comision-por-vender](https://developers.mercadolibre.com.co/es_co/comision-por-vender)  
**Captura:** 2026-10-08T22:51:29.334Z
