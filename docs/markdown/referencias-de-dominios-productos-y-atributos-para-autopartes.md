---
id: "referencias-de-dominios-productos-y-atributos-para-autopartes"
title: "Referencias de dominios, productos y atributos para Autopartes"
section: "Guía para productos"
subsection: "Categorización"
url: "https://developers.mercadolibre.com.co/es_co/referencias-de-dominios-productos-y-atributos-para-autopartes"
source_updated_at: "15/06/2026"
captured_at: "2026-10-08T22:52:43.356Z"
sha256: "192953fd613b3f1c101c36feb7997a57a7d5b1429372225dd77573df423ccd26"
---

# Referencias de dominios, productos y atributos para Autopartes

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 15/06/2026  
**Captura:** 2026-10-08T22:52:43.356Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/referencias-de-dominios-productos-y-atributos-para-autopartes](https://developers.mercadolibre.com.co/es_co/referencias-de-dominios-productos-y-atributos-para-autopartes)

## Resumen

Referencia de dominios y atributos para compatibilidad de autopartes en seis sitios. Expone qué campos usar como filtros principales, secundarios y opcionales, cómo consultar ítems con compatibilidades pendientes y cómo obtener valores frecuentes para atributos.

## Contenido y conceptos documentados

### Dominios, filtros y ciclo de compatibilidades

- Para MLA, MLB y MLU se usa `CARS_AND_VANS`; para MLM, MLC y MCO se usa `CARS_AND_VANS_FOR_COMPATIBILITIES` (con el prefijo del site). La página mapea marca, modelo, año, versión y motor, además de filtros secundarios y opcionales según dominio.
- Los ítems pueden buscarse con tags `pending_compatibilities` e `incomplete_compatibilities`. La ruta de `top_values` permite consultar valores más frecuentes, con campos como `id`, `name`, `metric`, `known_attributes` y `value_id`.
- La fuente indica que `POST /catalog_compatibilities/products_search/chunks` dejó de estar disponible el 15/07/2026; se conserva aquí como referencia histórica y no como operación vigente.
- Las llamadas muestran Bearer. Los cuerpos y errores por ruta que no aparecen en la captura: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Consultar dominio de compatibilidades

**Método:** `GET`  
**Ruta:** `/catalog_domains/$DOMAIN_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el dominio usado para categorizar autopartes y configurar filtros.

**Parámetros**

- `DOMAIN_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- known_attributes

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente enumera dominios distintos por sitio.

### Consultar atributos de categoría

**Método:** `GET`  
**Ruta:** `/categories/$CATEGORY_ID/attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los atributos asociados a una categoría de autopartes.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- name
- value_id
- value_name

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Buscar compatibilidades pendientes

**Método:** `GET`  
**Ruta:** `/users/$SELLER_ID/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca ítems usando tags pending_compatibilities o incomplete_compatibilities.

**Parámetros**

- `SELLER_ID` (path, obligatorio)
- `tags` (query, obligatorio): pending_compatibilities o incomplete_compatibilities.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- paging
- results

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Búsqueda de compatibilidades por chunks (retirada)

**Método:** `POST`  
**Ruta:** `/catalog_compatibilities/products_search/chunks`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La fuente registra que la operación dejó de estar disponible el 15/07/2026.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- No disponible desde 15/07/2026, según la fuente.

### Valores frecuentes del atributo

**Método:** `POST`  
**Ruta:** `/catalog_domains/$DOMAIN_ID/attributes/$ATTRIBUTE_ID/top_values`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene valores frecuentes para BRAND, MODEL, VEHICLE_YEAR u otro atributo del dominio.

**Parámetros**

- `DOMAIN_ID` (path, obligatorio)
- `ATTRIBUTE_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "La página muestra llamada POST sin cuerpo explícito."
  ]
}
```

**Respuesta**

- id
- name
- metric
- known_attributes
- value_id

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Los ejemplos consultan BRAND, MODEL y VEHICLE_YEAR.

### Referencia HTTP POST /catalog_domains/MLA-CARS_AND_VANS/attributes/BRAND/top_values

**Método:** `POST`  
**Ruta:** `/catalog_domains/MLA-CARS_AND_VANS/attributes/BRAND/top_values`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /catalog_domains/MLA-CARS_AND_VANS/attributes/BRAND/top_values. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP POST /catalog_domains/MLA-CARS_AND_VANS/attributes/VEHICLE_YEAR/top_values

**Método:** `POST`  
**Ruta:** `/catalog_domains/MLA-CARS_AND_VANS/attributes/VEHICLE_YEAR/top_values`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /catalog_domains/MLA-CARS_AND_VANS/attributes/VEHICLE_YEAR/top_values. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP POST /catalog_domains/MLA-CARS_AND_VANS/attributes/MODEL/top_values

**Método:** `POST`  
**Ruta:** `/catalog_domains/MLA-CARS_AND_VANS/attributes/MODEL/top_values`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /catalog_domains/MLA-CARS_AND_VANS/attributes/MODEL/top_values. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/referencias-de-dominios-productos-y-atributos-para-autopartes](https://developers.mercadolibre.com.co/es_co/referencias-de-dominios-productos-y-atributos-para-autopartes)  
**Captura:** 2026-10-08T22:52:43.356Z
