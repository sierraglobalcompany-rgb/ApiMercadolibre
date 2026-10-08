---
id: "mercado-envios-costos-y-cotizaciones"
title: "Mercado Envíos - Costos y cotizaciones"
section: "FAQs"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/mercado-envios-costos-y-cotizaciones"
source_updated_at: "05/05/2026"
captured_at: "2026-10-08T22:50:03.242Z"
sha256: "eee30a04c324bf6059e5515c525f3395b430583e6c91256616ab6faa246bf057"
---

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
