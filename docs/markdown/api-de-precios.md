---
id: "api-de-precios"
title: "Precios de productos"
section: "Guía para productos"
subsection: "Precios y Costos"
url: "https://developers.mercadolibre.com.co/es_co/api-de-precios"
source_updated_at: "26/02/2026"
captured_at: "2026-10-08T22:52:29.260Z"
sha256: "847c8938eed5745d32a505d6ecc610cccdd345c30b25015d9be529766974ad55"
---

# Precios de productos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 26/02/2026  
**Captura:** 2026-10-08T22:52:29.260Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/api-de-precios](https://developers.mercadolibre.com.co/es_co/api-de-precios)

## Resumen

Presenta los recursos para resolver el precio de venta ganador y consultar todos los precios vigentes de un ítem. La guía recomienda estos endpoints en lugar de los campos price, base_price y original_price de /items; para creación/edición de ítems se mantiene /items. La edición de precios mediante /prices/standard figura como no disponible todavía en la fuente.

## Contenido y conceptos documentados

- GET sale_price calcula el importe final para un contexto de canal y nivel de comprador; el metadata de promoción solo se entrega si el token pertenece al vendedor del ítem.
- context admite channel_marketplace; channel_proximity, mp_merchants y mp_links se describen como no habilitados aún. Los niveles buyer_loyalty_3 a buyer_loyalty_6 no están disponibles en MLU ni MPE.
- GET prices lista nodos standard y promotion con amount, regular_amount, currency_id, last_updated y conditions.context_restrictions/start_time/end_time. Datos sensibles de promoción pueden ocultarse para token ajeno.
- Antes de cambiar precio por PUT /items, revisar automatización de precio. La guía indica que desde el 18/03/2026 cambiar solo price con automatización produce 400; con otros atributos, el campo price puede ignorarse con warning.
- La operación POST /items/{item_id}/prices/standard se documenta como propuesta todavía no disponible; exige enviar los canales donde está publicado el precio y conditions.context_restrictions.

En los ejemplos de la fuente se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar precios vigentes

**Método:** `GET`  
**Ruta:** `/items/{item_id}/prices`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista precios standard y promocionales del ítem por canal/contexto.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id del ítem y prices[] con id, type, amount, regular_amount, currency_id, last_updated y conditions.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con nodos standard y promotion.

### Consultar precio de venta ganador

**Método:** `GET`  
**Ruta:** `/items/{item_id}/sale_price`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve el precio calculado para el contexto de canal y nivel de comprador.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `context` (query, opcional): Filtro de canal/nivel; la fuente recomienda al menos un canal.

**Solicitud**

No documentado en la fuente.

**Respuesta**

price_id, amount, regular_amount, currency_id, reference_date y metadata de promoción si el token pertenece al seller.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo channel_marketplace,buyer_loyalty_3.

### Editar precios standard (aún no disponible)

**Método:** `POST`  
**Ruta:** `/items/{item_id}/prices/standard`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La fuente describe la futura sustitución del PUT de ítems para editar precios; el recurso aún no está habilitado.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `prices` (body, obligatorio): Lista de precios por canal.
- `conditions.context_restrictions` (body, obligatorio): Canal de venta correspondiente.
- `amount` (body, obligatorio): Nuevo precio.
- `currency_id` (body, obligatorio): Moneda local.

**Solicitud**

prices[] con conditions.context_restrictions, amount y currency_id; incluir canales donde existe precio standard.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: mezcla inválida de nodo sin restricción con otros restringidos; múltiples nodos sin restricción; canales inválidos o canales publicados omitidos.

**Ejemplos**

- Ejemplo con channel_marketplace y channel_mshops.

### Actualizar precio mediante ítem

**Método:** `PUT`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La guía mantiene la edición mediante PUT en el recurso /items y advierte sobre el efecto de la automatización de precios. La página no muestra aquí el formato completo de URL ni del cuerpo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- Desde 18/03/2026: si hay automatización, una solicitud que actualiza solo price se rechaza con HTTP 400; si price se envía junto con otros atributos, se procesa con HTTP 200 pero price se ignora y se devuelve warning.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/api-de-precios](https://developers.mercadolibre.com.co/es_co/api-de-precios)  
**Captura:** 2026-10-08T22:52:29.260Z
