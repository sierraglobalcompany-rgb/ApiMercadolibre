# FAQs

9 páginas del portal oficial en esta área.

## [Facturación / Billing info](../markdown/facturacion-billing-info.md)

Actualización indicada por la fuente: 14/08/2026. Captura: 2026-10-08T22:49:58.316Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/facturacion-billing-info](https://developers.mercadolibre.com.co/es_co/facturacion-billing-info)

# Facturación / Billing info

**Área:** FAQs  
**Actualización indicada por la fuente:** 14/08/2026  
**Captura:** 2026-10-08T22:49:58.316Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/facturacion-billing-info](https://developers.mercadolibre.com.co/es_co/facturacion-billing-info)

## Resumen

Responde dudas sobre migración del recurso billing_info, datos fiscales, estados de procesamiento, impuestos, notas fiscales y diferencia entre dirección fiscal y logística.

## Contenido y conceptos documentados

- El flujo recomendado obtiene buyer.billing_info.id desde /orders y consulta /orders/billing-info/{site_id}/{billing_info_id}.
- Los datos fiscales pueden estar incompletos o en PROCESSING; billing_info no sustituye la dirección de entrega del envío.

## Operaciones de API

## Conceptos y recursos asociados

### Consultar billing info actual

Consulta el ID obtenido desde buyer.billing_info.id; algunos campos dependen del sitio.

**Ruta mencionada:** `/orders/billing-info/{site_id}/{billing_info_id}`  
**Método HTTP:** No documentado en la fuente.

**Parámetros documentados**

- `site_id` (path, obligatorio): ID del sitio
- `billing_info_id` (path, obligatorio): ID desde la orden

**Respuesta**

```json
{
  "fields": [
    "doc_type",
    "doc_number",
    "tax_status",
    "dirección fiscal"
  ]
}
```
### Facturación / Billing info

Responde dudas sobre migración del recurso billing_info, datos fiscales, estados de procesamiento, impuestos, notas fiscales y diferencia entre dirección fiscal y logística.
### Consultar descuentos de orden

La FAQ lo menciona para descuentos según región.

**Ruta mencionada:** `/orders/{order_id}/discounts`  
**Método HTTP:** No documentado en la fuente.

**Parámetros documentados**

- `order_id` (path, obligatorio): Identificador de la ruta
### Billing info legado

Recurso deprecado para datos fiscales.

**Ruta mencionada:** `/orders/{order_id}/billing_info`  
**Método HTTP:** No documentado en la fuente.

**Parámetros documentados**

- `order_id` (path, obligatorio): ID de orden
### Obtener billing_info.id de orden

Leer buyer.billing_info.id desde la orden.

**Ruta mencionada:** `/orders`  
**Método HTTP:** No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "buyer.billing_info.id"
  ]
}
```
### Consultar dirección logística

Separa dirección de entrega de la dirección fiscal.

**Ruta mencionada:** `/shipments/{shipment_id}`  
**Método HTTP:** No documentado en la fuente.

**Parámetros documentados**

- `shipment_id` (path, obligatorio): Identificador de la ruta
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/facturacion-billing-info](https://developers.mercadolibre.com.co/es_co/facturacion-billing-info)  
**Captura:** 2026-10-08T22:49:58.316Z

---

## [Gestión de stock multiorigen / User Products](../markdown/stock-multiwarehouse.md)

Actualización indicada por la fuente: 14/08/2026. Captura: 2026-10-08T22:49:59.473Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/stock-multiwarehouse](https://developers.mercadolibre.com.co/es_co/stock-multiwarehouse)

# Gestión de stock multiorigen / User Products

**Área:** FAQs  
**Actualización indicada por la fuente:** 14/08/2026  
**Captura:** 2026-10-08T22:49:59.473Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/stock-multiwarehouse](https://developers.mercadolibre.com.co/es_co/stock-multiwarehouse)

## Resumen

Explica cómo leer y actualizar inventario por ubicación en cuentas con stock multiorigen.

## Contenido y conceptos documentados

- En multiorigen el stock usa User Products y seller_warehouse; available_quantity en /items puede no cambiar el inventario.
- selling_address depende del sitio; Fulfillment usa inventario meli_facility.

## Operaciones de API

## Conceptos y recursos asociados

### Gestión de stock multiorigen / User Products

Explica cómo leer y actualizar inventario por ubicación en cuentas con stock multiorigen.
### Ruta mencionada /user-products/{user_product_id}/stock/type/{seller_warehouse}

La fuente menciona la ruta /user-products/{user_product_id}/stock/type/{seller_warehouse}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/user-products/{user_product_id}/stock/type/{seller_warehouse}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Crear User Product

**Método:** `POST`  
**Ruta:** `/user-products`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La FAQ relaciona 409 con SKU/GTIN duplicados o concurrencia.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "sku",
    "gtin"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "409 Conflict",   "http_status": 409,   "meaning": "Posible SKU/GTIN duplicado o modificación concurrente." } ```

**Ejemplos**

No documentado en la fuente.

### Consultar estado de ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Verifica estado durante sincronización asíncrona.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "status"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar stock de User Product

**Método:** `GET`  
**Ruta:** `/user-products/{user_product_id}/stock`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta stock locations y tipo de ubicación.

**Parámetros**

- `user_product_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "stock_locations",
    "type"
  ]
}
```

**Errores documentados**

- ```json {   "code": "stock-locations not found",   "meaning": "Stock no inicializado." } ```

**Ejemplos**

No documentado en la fuente.

### Crear stock location

**Método:** `POST`  
**Ruta:** `/user-products/{user_product_id}/stock/type/seller_warehouse`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea/asocia location con warehouse y cantidad.

**Parámetros**

- `user_product_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "store_id",
    "network_node_id",
    "quantity",
    "stock_locations"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "validation error",   "meaning": "Locations inválidas o faltantes." } ```

**Ejemplos**

No documentado en la fuente.

### Actualizar available_quantity

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Puede responder OK sin cambiar inventario multiorigen.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "available_quantity"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- {"available_quantity":10}

### Actualizar stock selling_address

**Método:** `PUT`  
**Ruta:** `/user-products/{user_product_id}/stock/type/selling_address`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Disponible solo en ciertos sitios según la FAQ.

**Parámetros**

- `user_product_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "quantity"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "the site is blocked for modifications to the selling address",   "meaning": "El sitio no admite selling_address." } ```

**Ejemplos**

- {"quantity":10}

### Actualizar stock por seller_warehouse

**Método:** `PUT`  
**Ruta:** `/user-products/{user_product_id}/stock/type/seller_warehouse`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza cantidad por ubicación.

**Parámetros**

- `user_product_id` (path, obligatorio): Identificador de la ruta

**Solicitud**

```json
{
  "fields": [
    "quantity",
    "store_id",
    "network_node_id",
    "stock_locations"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "stock-locations not found",   "meaning": "No hay stock locations inicializados." } ```

**Ejemplos**

- {"quantity":10}

### Referencia HTTP POST /user-products/{user_product_id}/stock/type/seller_

**Método:** `POST`  
**Ruta:** `/user-products/{user_product_id}/stock/type/seller_`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /user-products/{user_product_id}/stock/type/seller_. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/stock-multiwarehouse](https://developers.mercadolibre.com.co/es_co/stock-multiwarehouse)  
**Captura:** 2026-10-08T22:49:59.473Z

---

## [Imágenes y moderaciones](../markdown/imagenes-y-moderaciones.md)

Actualización indicada por la fuente: 05/05/2026. Captura: 2026-10-08T22:50:00.497Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/imagenes-y-moderaciones](https://developers.mercadolibre.com.co/es_co/imagenes-y-moderaciones)

# Imágenes y moderaciones

**Área:** FAQs  
**Actualización indicada por la fuente:** 05/05/2026  
**Captura:** 2026-10-08T22:50:00.497Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/imagenes-y-moderaciones](https://developers.mercadolibre.com.co/es_co/imagenes-y-moderaciones)

## Resumen

Resuelve dudas sobre imágenes rechazadas o pendientes, formatos y frecuencia de diagnóstico.

## Contenido y conceptos documentados

- Las imágenes deben ser accesibles desde la plataforma; WebP puede aparecer tras optimización interna.

## Operaciones de API

## Conceptos y recursos asociados

### Imágenes y moderaciones

Resuelve dudas sobre imágenes rechazadas o pendientes, formatos y frecuencia de diagnóstico.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/imagenes-y-moderaciones](https://developers.mercadolibre.com.co/es_co/imagenes-y-moderaciones)  
**Captura:** 2026-10-08T22:50:00.497Z

---

## [Items - Atributos de envío y dimensiones](../markdown/items-atributos-de-envio-y-dimensiones.md)

Actualización indicada por la fuente: 14/08/2026. Captura: 2026-10-08T22:50:01.324Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/items-atributos-de-envio-y-dimensiones](https://developers.mercadolibre.com.co/es_co/items-atributos-de-envio-y-dimensiones)

# Items - Atributos de envío y dimensiones

**Área:** FAQs  
**Actualización indicada por la fuente:** 14/08/2026  
**Captura:** 2026-10-08T22:50:01.324Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/items-atributos-de-envio-y-dimensiones](https://developers.mercadolibre.com.co/es_co/items-atributos-de-envio-y-dimensiones)

## Resumen

Detalla unidades y validaciones para dimensiones de embalaje y restricciones logísticas.

## Contenido y conceptos documentados

- Las dimensiones se expresan en cm y el peso en gramos; SELLER_PACKAGE_* se envía como valores numéricos sin unidad.
- La guía indica que MANUFACTURING_TIME no debe omitirse ni ser nulo.

## Operaciones de API

## Conceptos y recursos asociados

### Items - Atributos de envío y dimensiones

Detalla unidades y validaciones para dimensiones de embalaje y restricciones logísticas.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/items-atributos-de-envio-y-dimensiones](https://developers.mercadolibre.com.co/es_co/items-atributos-de-envio-y-dimensiones)  
**Captura:** 2026-10-08T22:50:01.324Z

---

## [ME1 / ME2 y envío gratis](../markdown/me1-me2-y-envio-gratis.md)

Actualización indicada por la fuente: 14/08/2026. Captura: 2026-10-08T22:50:02.383Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/me1-me2-y-envio-gratis](https://developers.mercadolibre.com.co/es_co/me1-me2-y-envio-gratis)

# ME1 / ME2 y envío gratis

**Área:** FAQs  
**Actualización indicada por la fuente:** 14/08/2026  
**Captura:** 2026-10-08T22:50:02.383Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/me1-me2-y-envio-gratis](https://developers.mercadolibre.com.co/es_co/me1-me2-y-envio-gratis)

## Resumen

Aclara cómo ME1/ME2, preferencias de cuenta y elegibilidad del mercado afectan envío gratis.

## Contenido y conceptos documentados

- La guía atribuye beneficios automáticos principalmente a ME2 y señala que no se puede forzar envío gratis nacional solo por API.

## Operaciones de API

## Conceptos y recursos asociados

### ME1 / ME2 y envío gratis

Aclara cómo ME1/ME2, preferencias de cuenta y elegibilidad del mercado afectan envío gratis.
## Operaciones de API

### Actualizar modo de envío

**Método:** `PUT`  
**Ruta:** `/items`  
**Autenticación:** No documentado en la fuente.

Ejemplo shipping.mode=me1; preferencias de cuenta pueden prevalecer.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "shipping.mode",
    "free_shipping"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "logistic_type"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- {"shipping":{"mode":"me1"},"free_shipping":true

**Fuente:** [https://developers.mercadolibre.com.co/es_co/me1-me2-y-envio-gratis](https://developers.mercadolibre.com.co/es_co/me1-me2-y-envio-gratis)  
**Captura:** 2026-10-08T22:50:02.383Z

---

## [Mercado Envíos - Costos y cotizaciones](../markdown/mercado-envios-costos-y-cotizaciones.md)

Actualización indicada por la fuente: 05/05/2026. Captura: 2026-10-08T22:50:03.242Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/mercado-envios-costos-y-cotizaciones](https://developers.mercadolibre.com.co/es_co/mercado-envios-costos-y-cotizaciones)

# Mercado Envíos - Costos y cotizaciones

**Área:** FAQs  
**Actualización indicada por la fuente:** 05/05/2026  
**Captura:** 2026-10-08T22:50:03.242Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/mercado-envios-costos-y-cotizaciones](https://developers.mercadolibre.com.co/es_co/mercado-envios-costos-y-cotizaciones)

## Resumen

Indica qué contexto enviar para cotizar envíos y qué campos consultar para conciliar costos.

## Contenido y conceptos documentados

- receiver.cost refleja el costo del comprador y senders[].cost el asociado al vendedor; promoted_amount/save son informativos.

## Operaciones de API

## Conceptos y recursos asociados

### Mercado Envíos - Costos y cotizaciones

Indica qué contexto enviar para cotizar envíos y qué campos consultar para conciliar costos.
### Cotizar opciones de envío

Añada contexto de ítem y logística para una cotización coherente.

**Ruta mencionada:** `/users/{user_id}/shipping_options/free`  
**Método HTTP:** No documentado en la fuente.

**Parámetros documentados**

- `user_id` (path, obligatorio): ID de vendedor
- `item_id` (query): ID del ítem
- `dimensions` (query): Dimensiones; peso en gramos enteros
- `item_price` (query): Precio
- `listing_type_id` (query): Tipo de publicación
- `mode` (query): Modo de envío
- `logistic_type` (query): Tipo logístico
- `free_shipping` (query): Indicador aplicable

**Respuesta**

```json
{
  "fields": [
    "list_cost",
    "moneda del sitio"
  ]
}
```
### Consultar costos del envío

Costos finales atribuidos a comprador y vendedor.

**Ruta mencionada:** `/shipments/{id}/costs`  
**Método HTTP:** No documentado en la fuente.

**Parámetros documentados**

- `id` (path, obligatorio): Identificador de la ruta

**Respuesta**

```json
{
  "fields": [
    "receiver.cost",
    "senders[].cost",
    "promoted_amount",
    "save"
  ]
}
```
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/mercado-envios-costos-y-cotizaciones](https://developers.mercadolibre.com.co/es_co/mercado-envios-costos-y-cotizaciones)  
**Captura:** 2026-10-08T22:50:03.242Z

---

## [Preguntas Frecuentes](../markdown/faq-preguntas-frecuentes.md)

Actualización indicada por la fuente: 01/05/2026. Captura: 2026-10-08T22:50:04.271Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/faq-preguntas-frecuentes](https://developers.mercadolibre.com.co/es_co/faq-preguntas-frecuentes)

# Preguntas Frecuentes

**Área:** FAQs  
**Actualización indicada por la fuente:** 01/05/2026  
**Captura:** 2026-10-08T22:50:04.271Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/faq-preguntas-frecuentes](https://developers.mercadolibre.com.co/es_co/faq-preguntas-frecuentes)

## Resumen

Índice temático de FAQs sobre rate limits, stock, envíos, facturación, imágenes, promociones y atributos.

## Contenido y conceptos documentados

- Agrupa enlaces por tema y términos de búsqueda.

## Operaciones de API

## Conceptos y recursos asociados

### Preguntas Frecuentes

Índice temático de FAQs sobre rate limits, stock, envíos, facturación, imágenes, promociones y atributos.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/faq-preguntas-frecuentes](https://developers.mercadolibre.com.co/es_co/faq-preguntas-frecuentes)  
**Captura:** 2026-10-08T22:50:04.271Z

---

## [Promotions / Pricing](../markdown/promotions-pricing.md)

Actualización indicada por la fuente: 05/05/2026. Captura: 2026-10-08T22:50:05.234Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/promotions-pricing](https://developers.mercadolibre.com.co/es_co/promotions-pricing)

# Promotions / Pricing

**Área:** FAQs  
**Actualización indicada por la fuente:** 05/05/2026  
**Captura:** 2026-10-08T22:50:05.234Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/promotions-pricing](https://developers.mercadolibre.com.co/es_co/promotions-pricing)

## Resumen

Explica diferencias posibles entre campañas, price_to_win y presentación del frontend.

## Contenido y conceptos documentados

- La activación puede ser asíncrona y la visualización puede recalcularse por contexto logístico o geográfico.

## Operaciones de API

## Conceptos y recursos asociados

### Promotions / Pricing

Explica diferencias posibles entre campañas, price_to_win y presentación del frontend.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/promotions-pricing](https://developers.mercadolibre.com.co/es_co/promotions-pricing)  
**Captura:** 2026-10-08T22:50:05.234Z

---

## [Rate Limit / Error 429](../markdown/rate-limit-error-429.md)

Actualización indicada por la fuente: 05/05/2026. Captura: 2026-10-08T22:50:06.139Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/rate-limit-error-429](https://developers.mercadolibre.com.co/es_co/rate-limit-error-429)

# Rate Limit / Error 429

**Área:** FAQs  
**Actualización indicada por la fuente:** 05/05/2026  
**Captura:** 2026-10-08T22:50:06.139Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/rate-limit-error-429](https://developers.mercadolibre.com.co/es_co/rate-limit-error-429)

## Resumen

Recomienda gestionar exceso de solicitudes con backoff, menor concurrencia, paginación y control por Client ID.

## Contenido y conceptos documentados

- La guía indica no mezclar scroll_id con offset/limit; recomienda backoff exponencial con jitter.

## Operaciones de API

## Conceptos y recursos asociados

### Rate Limit / Error 429

Recomienda gestionar exceso de solicitudes con backoff, menor concurrencia, paginación y control por Client ID.
### Consulta de visitas con límites de volumen

La FAQ menciona que esta consulta admite un solo product_id por llamada; respete el límite de consumo del recurso.

**Ruta mencionada:** `/items/visits`  
**Método HTTP:** No documentado en la fuente.

**Parámetros documentados**

- `product_id` (query): ID de producto; la FAQ indica que se consulta uno por llamada.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/rate-limit-error-429](https://developers.mercadolibre.com.co/es_co/rate-limit-error-429)  
**Captura:** 2026-10-08T22:50:06.139Z

---
