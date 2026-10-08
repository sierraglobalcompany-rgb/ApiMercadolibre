---
id: "variaciones-para-inmuebles"
title: "Variaciones"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/variaciones-para-inmuebles"
source_updated_at: "09/11/2025"
captured_at: "2026-10-08T22:50:52.096Z"
sha256: "652ecc66cc8f67d3777cff91f43beb19fcdc59b584be4f2304228b60f6dca25a"
---

# Variaciones

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 09/11/2025  
**Captura:** 2026-10-08T22:50:52.096Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/variaciones-para-inmuebles](https://developers.mercadolibre.com.co/es_co/variaciones-para-inmuebles)

## Resumen

Las variaciones permiten representar varias unidades o alternativas dentro de una publicación de proyecto inmobiliario, con diferencias en atributos como área, dormitorios o baños. La guía muestra cómo identificar categorías habilitadas, consultar atributos y recuperar las variaciones publicadas.

## Contenido y conceptos documentados

- Categorías citadas: MLA401806 (Argentina), MLU455673 (Uruguay), MLC157523 (Chile) y MLM170376 (México). La disponibilidad indicada corresponde a esos sitios.
- En los atributos, allow_variations=true identifica los que van en attribute_combinations; los atributos comunes van en attributes.
- La publicación requiere privilegios y paquete de desarrollo; la guía indica que el paquete habilita una sola publicación.
- La respuesta puede incluir variations, item_relations, attribute_combinations, available_quantity, sold_quantity, price, sale_terms y picture_ids. La fuente enumera errores 400 por atributos obligatorios omitidos/mal ubicados/valores no permitidos y cuota agotada.

## Operaciones de API

## Conceptos y recursos asociados

### Estructura y requisitos de variaciones

Los atributos comunes van en attributes y los variables en attribute_combinations. Requiere privilegios/paquete; la guía enumera errores 400 por atributos obligatorios omitidos, mal ubicados o valores no permitidos y por cuota agotada.
## Operaciones de API

### Consultar atributos de categoría

**Método:** `GET`  
**Ruta:** `/categories/$CATEGORY_ID/attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Identifica atributos obligatorios y permitidos para variaciones; allow_variations=true indica que van en attribute_combinations.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Atributos con tags required y allow_variations.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar categoría con variaciones

**Método:** `GET`  
**Ruta:** `/categories/$CATEGORY_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Comprueba que attribute_types indique variations.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

attribute_types con valor variations.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La guía cita MLA401806, MLU455673, MLC157523 y MLM170376.

### Consultar variación específica

**Método:** `GET`  
**Ruta:** `/items/$ITEM_ID/variations/$VARIATION_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene una variación por ID dentro de un ítem.

**Parámetros**

- `ITEM_ID` (path, obligatorio): ID del ítem.
- `VARIATION_ID` (path, obligatorio): ID numérico de la variación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Estructura de variación descrita para la consulta del ítem.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar variaciones del inmueble

**Método:** `GET`  
**Ruta:** `/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Solicita el ítem con attributes=variations.

**Parámetros**

- `ITEM_ID` (path, obligatorio): ID del ítem.
- `attributes` (query, obligatorio): La guía usa variations.

**Solicitud**

No documentado en la fuente.

**Respuesta**

variations[], item_relations[] y campos como attribute_combinations, available_quantity, sold_quantity, price, sale_terms y picture_ids.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/variaciones-para-inmuebles](https://developers.mercadolibre.com.co/es_co/variaciones-para-inmuebles)  
**Captura:** 2026-10-08T22:50:52.096Z
