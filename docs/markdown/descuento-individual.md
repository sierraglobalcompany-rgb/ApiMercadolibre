---
id: "descuento-individual"
title: "Descuento individual"
section: "Guía para productos"
subsection: "Central de promociones"
url: "https://developers.mercadolibre.com.co/es_co/descuento-individual"
source_updated_at: "09/06/2026"
captured_at: "2026-10-08T22:51:34.905Z"
sha256: "d84ec0d8eb00428e639212670884bc3018694b4fd31de821284abea1d4d27bf2"
---

# Descuento individual

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 09/06/2026  
**Captura:** 2026-10-08T22:51:34.905Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/descuento-individual](https://developers.mercadolibre.com.co/es_co/descuento-individual)

## Resumen

Documenta la consulta, creación y eliminación de descuentos individuales PRICE_DISCOUNT sobre publicaciones. La oferta se aplica a un segmento de compradores y debe respetar condiciones de reputación, estado, condición y precio de la publicación.

## Contenido y conceptos documentados

- La fuente indica descuentos generales de 5–80 % y una duración máxima de 14 días. Las fechas se envían como fecha y hora; subir el precio puede retirar el descuento.
- Se documentan deal_price requerido, top_deal_price opcional, start_date, finish_date y promotion_type=PRICE_DISCOUNT. Una oferta DEAL en conflicto puede postergar el inicio hasta que termine.
- La respuesta de creación incluye price y original_price. La consulta puede incluir datos de boosted_offer como discount_meli_boosted_percentage, discount_meli_boost_amount y total_price_for_boosted_offer cuando aplica.
- Autenticación mostrada: Bearer. La fuente menciona restricciones para vendedores/items no elegibles y para libros en MLA.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Eliminar descuento individual

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Elimina la oferta indicada para el ítem.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `promotion_type` (query, opcional): promotion_type
- `app_version` (query, opcional): app_version=v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

HTTP 200 OK.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta 200 OK documentada.

### Consultar promociones de un ítem

**Método:** `GET`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene el estado promocional del ítem, incluido el descuento vigente o datos de oferta impulsada.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Datos de promociones y precio; si boosted_offer=true pueden aparecer discount_meli_boosted_percentage, discount_meli_boost_amount y total_price_for_boosted_offer.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra campos de boosted_offer.

### Crear descuento individual

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Crea una oferta de tipo PRICE_DISCOUNT para el ítem.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `app_version` (query, opcional): app_version=v2
- `deal_price` (body, obligatorio): Precio con descuento para todos.
- `top_deal_price` (body, opcional): Precio opcional para compradores leales nivel 3–6.
- `start_date` (body, obligatorio): Fecha de inicio.
- `finish_date` (body, obligatorio): Fecha final.
- `promotion_type` (body, obligatorio): PRICE_DISCOUNT.

**Solicitud**

deal_price (precio con descuento para todos), top_deal_price (opcional; para compradores Mercado Puntos niveles 3–6), start_date, finish_date y promotion_type=PRICE_DISCOUNT.

**Respuesta**

price y original_price.

**Errores documentados**

- buyer_discount_not_in_range: descuento general fuera del rango 5%–80%.
- best_buyer_discount_not_in_range: descuento para mejores compradores fuera del rango 5%–80%.
- discount_below_10_percent_difference: si el descuento general supera 35%, la diferencia para niveles 3–6 debe ser al menos 10%.
- discount_below_5_percent_difference: diferencia entre descuento general y niveles 3–6 inferior al 5%.
- error_credibility_price: el descuento no es suficiente para considerarse creíble; aplicar uno mayor.

**Ejemplos**

- Ejemplo de deal_price y fechas.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/descuento-individual](https://developers.mercadolibre.com.co/es_co/descuento-individual)  
**Captura:** 2026-10-08T22:51:34.905Z
