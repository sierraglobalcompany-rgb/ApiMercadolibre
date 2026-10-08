---
id: "cupones-del-vendedor"
title: "Cupones del vendedor"
section: "Guía para productos"
subsection: "Central de promociones"
url: "https://developers.mercadolibre.com.co/es_co/cupones-del-vendedor"
source_updated_at: "13/03/2026"
captured_at: "2026-10-08T22:51:30.604Z"
sha256: "af532e5e6b74894dc8327cab267f572ad491ae882e9fdaa41e0c92a128b799d7"
---

# Cupones del vendedor

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/03/2026  
**Captura:** 2026-10-08T22:51:30.604Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/cupones-del-vendedor](https://developers.mercadolibre.com.co/es_co/cupones-del-vendedor)

## Resumen

La página explica cómo crear, modificar, consultar y cerrar campañas de cupones del vendedor, además de asociar publicaciones a una campaña. La fuente limita la disponibilidad indicada a MLB (Brasil); exige reputación verde, publicaciones activas, nuevas y con exposición distinta de gratuita. Los cupones admiten descuento porcentual o monto fijo, fechas y presupuesto; el código parcial es opcional y su uso restringe el beneficio a compradores que lo conocen.

## Contenido y conceptos documentados

- Tipos: FIXED_PERCENTAGE y FIXED_AMOUNT. Para porcentaje se documentan min_purchase_amount y max_purchase_amount; los porcentajes deben quedar entre 5 y 80. La campaña admite hasta 31 días y el presupuesto solo puede incrementarse una vez iniciada.
- El código de cupón combina los primeros cinco caracteres del nickname del vendedor con el código del usuario, con un máximo de diez caracteres; sin código, el cupón queda disponible para todos los compradores.
- Al asociar una publicación a la campaña, la respuesta de precio promocional puede ser cero y el descuento se aplica en el checkout; la página indica que el vendedor no puede modificar esa publicación por separado durante la campaña.
- Autenticación mostrada en los ejemplos: Bearer. La fuente documenta errores de fechas, duración, nombre duplicado, rango de descuento, monto mínimo/máximo y cambios no permitidos en campañas iniciadas.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Retirar publicación de campaña

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Quita una publicación de la campaña especificada.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `promotion_type` (query, opcional): promotion_type=SELLER_COUPON_CAMPAIGN
- `promotion_id` (query, opcional): promotion_id
- `app_version` (query, opcional): app_version=v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

HTTP 200 OK.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta 200 OK documentada.

### Eliminar campaña

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Finaliza o elimina la campaña del vendedor.

**Parámetros**

- `promotion_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `promotion_type` (query, opcional): promotion_type=SELLER_COUPON_CAMPAIGN
- `app_version` (query, opcional): app_version=v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

HTTP 200 OK.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta 200 OK documentada.

### Consultar campaña

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene el detalle de una campaña, incluido el subtipo y beneficio.

**Parámetros**

- `promotion_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `promotion_type` (query, opcional): promotion_type=SELLER_COUPON_CAMPAIGN
- `app_version` (query, opcional): app_version=v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

Datos de campaña, estado, subtipo y configuración del cupón.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra respuestas de campañas FIXED_AMOUNT.

### Listar publicaciones de campaña

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}/items`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lista los ítems asociados a la campaña.

**Parámetros**

- `promotion_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `promotion_type` (query, opcional): promotion_type=SELLER_COUPON_CAMPAIGN
- `app_version` (query, opcional): app_version=v2
- `status_item` (query, opcional): status_item opcional: active o paused

**Solicitud**

No documentado en la fuente.

**Respuesta**

Publicaciones asociadas y sus datos de precio/estado.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Filtro status_item documentado para activas o pausadas.

### Asociar publicación a campaña

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Agrega una publicación a la campaña de cupones indicada.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `app_version` (query, opcional): app_version=v2
- `promotion_id` (body, obligatorio): Identificador de campaña.
- `promotion_type` (body, obligatorio): SELLER_COUPON_CAMPAIGN.

**Solicitud**

promotion_id y promotion_type=SELLER_COUPON_CAMPAIGN.

**Respuesta**

price y original_price de la publicación; el ejemplo muestra ambos en cero.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Solicitud compacta con promotion_id y promotion_type.

### Crear campaña de cupones

**Método:** `POST`  
**Ruta:** `/seller-promotions/promotions`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Crea una campaña SELLER_COUPON_CAMPAIGN con subtipo, beneficio, fechas y presupuesto.

**Parámetros**

- `app_version` (query, opcional): app_version=v2
- `promotion_type` (body, obligatorio): Debe ser SELLER_COUPON_CAMPAIGN.
- `name` (body, obligatorio): Nombre de campaña.
- `sub_type` (body, obligatorio): FIXED_PERCENTAGE o FIXED_AMOUNT.
- `fixed_percentage` (body, opcional): Porcentaje del beneficio cuando aplica.
- `fixed_amount` (body, opcional): Monto fijo del beneficio cuando aplica.
- `min_purchase_amount` (body, opcional): Monto mínimo de compra.
- `max_purchase_amount` (body, opcional): Máximo de reintegro para porcentual.
- `start_date` (body, obligatorio): Inicio de campaña.
- `finish_date` (body, obligatorio): Fin de campaña.
- `budget` (body, obligatorio): Presupuesto de campaña.
- `partial_coupon_code` (body, opcional): Código parcial opcional.

**Solicitud**

promotion_type, name, sub_type, fixed_percentage o fixed_amount, min_purchase_amount, max_purchase_amount (porcentaje), start_date, finish_date, budget y partial_coupon_code opcional.

**Respuesta**

Identificador, estado, nombre, subtipo, fechas y beneficio de la campaña.

**Errores documentados**

- 400: fechas fuera del rango permitido; duración excedida o insuficiente; nombre duplicado; porcentaje fuera de 5–80; monto o presupuesto incompatibles.

**Ejemplos**

- Ejemplo compacto de creación de campaña FIXED_AMOUNT y campaña con código parcial.

### Actualizar campaña

**Método:** `PUT`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Modifica los campos permitidos de una campaña existente.

**Parámetros**

- `promotion_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `promotion_type` (query, opcional): promotion_type=SELLER_COUPON_CAMPAIGN
- `app_version` (query, opcional): app_version=v2
- `promotion_type` (body, obligatorio): Tipo de promoción.
- `name` (body, opcional): Nombre modificable.
- `finish_date` (body, opcional): Fecha final modificable.
- `budget` (body, opcional): Solo puede incrementarse.

**Solicitud**

promotion_type requerido; la página enumera finish_date, name y budget entre los campos modificables y también muestra campos de beneficio.

**Respuesta**

Estado y datos actualizados de la campaña.

**Errores documentados**

- 400: campo no actualizable en estado STARTED; presupuesto no puede reducirse.

**Ejemplos**

- Ejemplo de actualización de campaña.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/cupones-del-vendedor](https://developers.mercadolibre.com.co/es_co/cupones-del-vendedor)  
**Captura:** 2026-10-08T22:51:30.604Z
