---
id: "tipos-de-publicacion-y-actualizaciones-de-articulos"
title: "Tipos de publicación"
section: "Guía para productos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/tipos-de-publicacion-y-actualizaciones-de-articulos"
source_updated_at: "01/06/2026"
captured_at: "2026-10-08T22:52:53.651Z"
sha256: "37aa57597cebb06f1db9875557bd3c26539fbe7639ed412e378183b49366179a"
---

# Tipos de publicación

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 01/06/2026  
**Captura:** 2026-10-08T22:52:53.651Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/tipos-de-publicacion-y-actualizaciones-de-articulos](https://developers.mercadolibre.com.co/es_co/tipos-de-publicacion-y-actualizaciones-de-articulos)

## Resumen

Referencia de tipos de publicación y exposición para consultar opciones disponibles por sitio, categoría, usuario o ítem, así como alternativas de upgrade/downgrade y cambio de tipo.

## Contenido y conceptos documentados

### Tipos, exposición y cambio

- Los tipos de Marketplace citados son `free`, `gold_special` y `gold_pro`, con disponibilidad variable por sitio. En Argentina, la página describe `gold_special` sin cuotas promocionales y `gold_pro` con cuotas más convenientes y costo asociado.
- Para elegir una opción se consultan tipos por sitio, tipos habilitados por usuario/categoría, exposición por sitio o tipo, y opciones disponibles para el ítem. También existe consulta de `stop_time` mediante el atributo de ítem.
- La operación de cambio usa el recurso `/items/$ITEM_ID/listing_type`; la página indica que el tipo de publicación solo puede cambiarse una vez. Las llamadas muestran Bearer; la fuente no documenta cuerpos de consulta y errores completos para cada GET.

## Operaciones de API
## Operaciones de API

### Consultar downgrades

**Método:** `GET`  
**Ruta:** `/items/$ITEM_ID/available_downgrades`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista downgrades disponibles para el ítem.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- name
- available
- cause

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Tipos disponibles para ítem

**Método:** `GET`  
**Ruta:** `/items/$ITEM_ID/available_listing_types`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista listing types que puede usar el ítem.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- name
- available
- cause

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar upgrades

**Método:** `GET`  
**Ruta:** `/items/$ITEM_ID/available_upgrades`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista upgrades de tipo de publicación disponibles.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- name
- available
- cause

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar stop_time del ítem

**Método:** `GET`  
**Ruta:** `/items/$TIEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Ejemplo de consulta del atributo stop_time de la publicación.

**Parámetros**

- `TIEM_ID` (path, obligatorio): La fuente escribe TIEM_ID en la URL de ejemplo.
- `attributes` (query, obligatorio): stop_time.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- stop_time

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Listar exposiciones

**Método:** `GET`  
**Ruta:** `/sites/$SITE_ID/listing_exposures`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista niveles de exposición para un sitio.

**Parámetros**

- `SITE_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- name
- home_page
- category_home_page
- advertising_on_listing_page
- priority_in_search

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar exposición

**Método:** `GET`  
**Ruta:** `/sites/$SITE_ID/listing_exposures/$EXPOSURE_LEVEL`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta configuración de un nivel de exposición.

**Parámetros**

- `SITE_ID` (path, obligatorio)
- `EXPOSURE_LEVEL` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- name
- home_page
- category_home_page
- advertising_on_listing_page
- priority_in_search

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Listar tipos de publicación del sitio

**Método:** `GET`  
**Ruta:** `/sites/$SITE_ID/listing_types`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta listing types disponibles en el sitio.

**Parámetros**

- `SITE_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- site_id
- id
- name
- configuration
- buy_it_now
- auction
- classified
- immediate_payment
- listing_fee_criteria
- sale_fee_criteria

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar tipo de publicación

**Método:** `GET`  
**Ruta:** `/sites/$SITE_ID/listing_types/$LISTING_TYPE_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene configuración de un listing type.

**Parámetros**

- `SITE_ID` (path, obligatorio)
- `LISTING_TYPE_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- name
- configuration
- requires_picture
- max_stock_per_item
- duration_days
- buy_it_now
- auction
- classified
- immediate_payment

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar tipo free disponible

**Método:** `GET`  
**Ruta:** `/users/$USER_ID/available_listing_type/free`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta disponibilidad del tipo gratuito para usuario y categoría.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `category_id` (query, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- available
- remaining_listings
- cause

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Listar tipos disponibles para usuario

**Método:** `GET`  
**Ruta:** `/users/$USER_ID/available_listing_types`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta tipos de publicación habilitados para usuario y categoría.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `category_id` (query, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- available
- remaining_listings
- cause

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Cambiar tipo de publicación

**Método:** `POST`  
**Ruta:** `/items/$TIEM_ID/listing_type`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza el listing type del ítem.

**Parámetros**

- `TIEM_ID` (path, obligatorio): La fuente escribe TIEM_ID en el ejemplo.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "listing_type_id"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página indica que el tipo solo puede modificarse una vez.

### Referencia HTTP GET /sites/MLA/listing_types/gold_special

**Método:** `GET`  
**Ruta:** `/sites/MLA/listing_types/gold_special`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /sites/MLA/listing_types/gold_special. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /sites/MLA/listing_exposures/high

**Método:** `GET`  
**Ruta:** `/sites/MLA/listing_exposures/high`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /sites/MLA/listing_exposures/high. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/tipos-de-publicacion-y-actualizaciones-de-articulos](https://developers.mercadolibre.com.co/es_co/tipos-de-publicacion-y-actualizaciones-de-articulos)  
**Captura:** 2026-10-08T22:52:53.651Z
