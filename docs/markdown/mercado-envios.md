---
id: "mercado-envios"
title: "Gestión Mercado Envíos"
section: "Guía para productos"
subsection: "Envíos"
url: "https://developers.mercadolibre.com.co/es_co/mercado-envios"
source_updated_at: "23/04/2026"
captured_at: "2026-10-08T22:51:52.527Z"
sha256: "62e7d2db9641cb8bba4a5486e9066cc8e2fac356489beb26f0ebf20ac91804e1"
---

# Gestión Mercado Envíos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 23/04/2026  
**Captura:** 2026-10-08T22:51:52.527Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/mercado-envios](https://developers.mercadolibre.com.co/es_co/mercado-envios)

## Resumen

La página reúne recursos para conocer métodos y preferencias de envío, atributos requeridos por categoría o dominio y servicios logísticos disponibles para un User Product. También presenta el recurso de servicios de shippability como evolución de `shipping_modes`, y la consulta de configuración de envío de una publicación.

## Contenido y conceptos documentados

- El flujo recomendado es consultar métodos/preferencias y atributos antes de publicar o editar, para validar modalidades disponibles. Los servicios de un User Product pueden coexistir para varias logísticas (por ejemplo, Full, cross-docking y Flex); para validaciones sobre UP creados se indica usar el recurso nuevo en lugar de `/users/{USER_ID}/shipping_modes`.
- En el recurso de shippability se documentan `SITE_ID`, `USER_PRODUCT_ID` y el query opcional `legacy_attributes=true`; la respuesta agrupa servicios y atributos. La página cubre modalidades `custom`, `me2`, `me1`, `pharma` y opciones relacionadas. La categoría puede devolver `dimensions`, `logistics` y `me2_restrictions`; el recurso de shippability organiza `services` con tipo, dirección, flavor y velocidad, atributos de distribución y configuración de red, además de mapeo heredado opcional.
- Los ejemplos usan OAuth Bearer en varios recursos; para shippability muestran headers `Accept` y `Content-Type` JSON. Detalles no especificados: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### GET /catalog_domains/{DOMAIN_ID}/shipping_attributes

**Método:** `GET`  
**Ruta:** `/catalog_domains/{DOMAIN_ID}/shipping_attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta atributos logísticos requeridos por dominio.

**Parámetros**

- `DOMAIN_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "domain_id",
    "attributes"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /categories/{CATEGORY_ID}/shipping_preferences

**Método:** `GET`  
**Ruta:** `/categories/{CATEGORY_ID}/shipping_preferences`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta preferencias disponibles para una categoría.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "category_id",
    "dimensions",
    "logistics",
    "me2_restrictions"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /customers/marketplace/sites/{SITE_ID}/user-products/{USER_PRODUCT_ID}/contracts/shippability/services

**Método:** `GET`  
**Ruta:** `/customers/marketplace/sites/{SITE_ID}/user-products/{USER_PRODUCT_ID}/contracts/shippability/services`  
**Autenticación:** No documentado en la fuente.

Consulta servicios logísticos disponibles para un User Product; admite `legacy_attributes=true`.

**Parámetros**

- `SITE_ID` (path, obligatorio)
- `USER_PRODUCT_ID` (path, obligatorio)
- `legacy_attributes` (query, opcional): La fuente muestra true para solicitar atributos heredados.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "services",
    "mode",
    "logistic_types",
    "attributes",
    "dimensions",
    "costs",
    "adoption",
    "free_shipping",
    "local_pick_up"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /items/{ITEM_ID}

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la publicación, incluidos sus datos de envío.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "shipping",
    "mode",
    "local_pick_up",
    "logistic_type"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /sites/{SITE_ID}/shipping_methods

**Método:** `GET`  
**Ruta:** `/sites/{SITE_ID}/shipping_methods`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta métodos de envío del sitio.

**Parámetros**

- `SITE_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "name",
    "type",
    "deliver_to",
    "status",
    "site_id",
    "free_options"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /users/{USER_ID}/shipping_preferences

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/shipping_preferences`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta preferencias activas de envío del usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /users/{USER_ID}/shipping_modes

**Método:** `POST`  
**Ruta:** `/users/{USER_ID}/shipping_modes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta los modos del recurso heredado documentado en la página.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/mercado-envios](https://developers.mercadolibre.com.co/es_co/mercado-envios)  
**Captura:** 2026-10-08T22:51:52.527Z
