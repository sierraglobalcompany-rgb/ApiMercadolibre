---
id: "facturacion-billing-info"
title: "Facturación / Billing info"
section: "FAQs"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/facturacion-billing-info"
source_updated_at: "14/08/2026"
captured_at: "2026-10-08T22:49:58.316Z"
sha256: "d4f73eed012113dcf8d569e3f2553cb1813ec2044586fedbb61eb44bd6e1141b"
---

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
