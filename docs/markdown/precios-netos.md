---
id: "precios-netos"
title: "Precios netos por cantidad"
section: "Guía para productos"
subsection: "Precios por cantidad"
url: "https://developers.mercadolibre.com.co/es_co/precios-netos"
source_updated_at: "16/09/2026"
captured_at: "2026-10-08T22:52:30.357Z"
sha256: "170b98389045046990df2817a14a4cb715d812803683706ac0e3bc012353b182"
---

# Precios netos por cantidad

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 16/09/2026  
**Captura:** 2026-10-08T22:52:30.357Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/precios-netos](https://developers.mercadolibre.com.co/es_co/precios-netos)

## Resumen

Permite a vendedores B2B elegibles de Brasil que pertenecen al Régimen Normal y usan el facturador fijar un valor neto por unidad. Mercado Libre calcula el precio final según ubicación del comprador y reglas fiscales. Esta configuración se integra en el flujo PxQ.

## Contenido y conceptos documentados

- El vendedor y el ítem deben ser elegibles: vendedor bajo Régimen Normal con facturador Mercado Libre y publicación con datos fiscales completos. El endpoint devuelve is_user_eligible, is_item_eligible, pending_actions y, si corresponde, causa/message.
- Los nodos se envían como prices[] standard con amount, currency_id, amount_tax_inclusion_type=net y conditions.context_restrictions channel_marketplace/user_type_business más min_purchase_unit. El rango inicial usa min_purchase_unit=1; hasta cinco rangos, con importe decreciente.
- Para reemplazar PxQ porcentual por precios netos, usar remove_percentage_pxq=true; de lo contrario la fuente indica incompatibilidad. La consulta de precios puede usar show-all-prices y x-calculate-net-taxes en sale_price.
- Errores de validación documentados usan invalid.price_per_quantity para tipo fiscal net ausente, min_purchase_unit inicial ausente/cero y orden de importes incoherente.

En los ejemplos de la fuente se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar elegibilidad de usuario e ítem

**Método:** `GET`  
**Ruta:** `/business/v1/sites/{site_id}/users/{user_id}/items/{item_id}/options/net-prices/seller/eligibility`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Valida requisitos fiscales y comerciales para configurar precios netos.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `user_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

user_id, item_id, is_user_eligible, is_item_eligible y pending_actions; puede incluir cause_id/message.

**Errores documentados**

- B2BSO-502: item has no tax information (publicación sin datos fiscales).
- Mensaje documentado: user ineligible for net prices by fiscal identities.

**Ejemplos**

- Ejemplos de usuario e ítem elegibles y de casos no elegibles.

### Identificar publicación con precios netos

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el ítem para encontrar el tag net_taxes_amount_prices.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

tags de publicación.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La guía usa net_taxes_amount_prices para reconocer la configuración.

### Consultar precios netos

**Método:** `GET`  
**Ruta:** `/items/{item_id}/prices`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista precios del ítem, incluidos rangos netos con show-all-prices.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `show-all-prices` (header, opcional): TRUE/FALSE, opcional para obtener los rangos.

**Solicitud**

No documentado en la fuente.

**Respuesta**

prices[] con amount_tax_inclusion_type y condiciones PxQ netas.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de consulta con show-all-prices: TRUE.

### Calcular precio neto por cantidad y destino

**Método:** `GET`  
**Ruta:** `/items/{item_id}/sale_price`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve el precio de venta contextualizado para la cantidad y destino del comprador.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `context` (query, obligatorio): Ejemplo incluye channel_marketplace,user_type_business.
- `quantity` (query, opcional): Cantidad solicitada.
- `destination_states` (query, opcional): Estado de destino; el ejemplo usa código BR-SP.
- `buyer_id` (query, opcional): Identificador del comprador.
- `x-calculate-net-taxes` (header, opcional): El ejemplo lo envía en true para cálculo neto.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Precio de venta calculado y componentes fiscales mostrados en la respuesta.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con comprador, cantidad y destination_states.

### Configurar precios netos por cantidad

**Método:** `POST`  
**Ruta:** `/items/{item_id}/prices/standard/quantity`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea o reemplaza nodos netos standard para compradores B2B.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `remove_percentage_pxq` (query, opcional): Si true elimina nodos PxQ porcentuales y los reemplaza por rangos netos.
- `prices` (body, obligatorio): Nodos de precios netos.
- `amount_tax_inclusion_type` (body, obligatorio): Debe ser net.
- `conditions.min_purchase_unit` (body, obligatorio): El nodo inicial requiere unidad mínima 1; otros nodos aumentan cantidad.
- `conditions.context_restrictions` (body, obligatorio): channel_marketplace y user_type_business.

**Solicitud**

prices[] con type=standard, amount, currency_id, amount_tax_inclusion_type=net y conditions.context_restrictions/min_purchase_unit.

**Respuesta**

id del ítem y prices[] con id, type, amount, currency_id y conditions.

**Errores documentados**

- 400 invalid.price_per_quantity: Net prices require a 'net' tax type across all prices per quantity.
- 400 invalid.price_per_quantity: Net prices require a price per unit amount.
- 400 invalid.price_per_quantity: Price per quantity min purchase unit below the minimum.
- 400 invalid.price_per_quantity: Price per quantity invalid coherence order.

**Ejemplos**

- Ejemplo con remove_percentage_pxq=true y rangos netos.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/precios-netos](https://developers.mercadolibre.com.co/es_co/precios-netos)  
**Captura:** 2026-10-08T22:52:30.357Z
