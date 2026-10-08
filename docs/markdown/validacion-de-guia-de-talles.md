---
id: "validacion-de-guia-de-talles"
title: "Validación de guía de talles"
section: "Guía para productos"
subsection: "Guías de Talles"
url: "https://developers.mercadolibre.com.co/es_co/validacion-de-guia-de-talles"
source_updated_at: "30/12/2025"
captured_at: "2026-10-08T22:52:57.692Z"
sha256: "3df33f856c8438e6f421b5e7fa2f96feb78327c12598c8d22563c14815c4dcff"
---

# Validación de guía de talles

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:52:57.692Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/validacion-de-guia-de-talles](https://developers.mercadolibre.com.co/es_co/validacion-de-guia-de-talles)

## Resumen

La página describe controles al crear guías de talles y asociarlas con publicaciones de moda. La fuente dice que el recurso está disponible en Argentina, México, Brasil, Uruguay, Colombia, Perú, Ecuador y Chile.

## Contenido y conceptos documentados

- Completa ficha técnica, atributos requeridos y variaciones; verifica género con los atributos del dominio y, donde aplique, usa género y marca para encontrar una guía adecuada.
- La creación valida el atributo principal, atributos requeridos de filas, tipo y rango de medidas y duplicados.
- Para asociar una guía, la publicación debe tener SIZE_GRID_ID, SIZE_GRID_ROW_ID y SIZE válidos y consistentes con la fila; la fuente también verifica atributos como GENDER y que la guía personalizada pertenezca al vendedor.
- En Live Listings no se evalúan estas reglas al cambiar precio/stock o estados pausado/cerrado. Las publicaciones inconsistentes pueden moderarse y pausarse.
- Códigos documentados: chart_tech_specs_not_found, main_attribute_missing_error, invalid_main_attribute_id, required_row_attribute_not_found, invalid_row_attribute_value, value_out_of_range, invalid_attribute_value, duplicated_measure_value, value_is_not_the_same_type, invalid_row_attribute, missing.fashion_grid.grid_id.values, missing.fashion_grid.grid_row_id.values, missing.fashion_grid.size.values, invalid.fashion_grid.grid_id.values, invalid.fashion_grid.grid_row_id.values, invalid.fashion_grid.size.values e invalid.fashion_grid.seller_id.values. La fuente reutiliza invalid.fashion_grid.size.values en el ejemplo de SIZE y GENDER.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /catalog_domains/{DOMAIN_ID}/attributes/GENDER

La fuente menciona la ruta /catalog_domains/{DOMAIN_ID}/attributes/GENDER, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/catalog_domains/{DOMAIN_ID}/attributes/GENDER`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /items

La fuente menciona la ruta /items, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/items`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Validaciones de guías de talles

Documenta validaciones al crear guías de talles y asociarlas a publicaciones de moda. Revisa género, atributo principal, campos requeridos y consistencia de medidas; la asociación exige SIZE_GRID_ID, SIZE_GRID_ROW_ID y SIZE coherentes. La página muestra códigos y mensajes de error, algunos con cause_id y references; no define una ruta HTTP para validar la guía.

**Errores documentados**

- ```json {   "code": "chart_tech_specs_not_found",   "meaning": "El género no existe en la ficha técnica del dominio." } ```
- ```json {   "code": "main_attribute_missing_error",   "meaning": "Falta el atributo principal." } ```
- ```json {   "code": "invalid_main_attribute_id",   "meaning": "El atributo principal indicado no es válido." } ```
- ```json {   "code": "required_row_attribute_not_found",   "meaning": "Falta un atributo requerido en una fila." } ```
- ```json {   "code": "invalid_row_attribute_value",   "meaning": "El valor de fila no es permitido." } ```
- ```json {   "code": "value_out_of_range",   "meaning": "Una medida está fuera del rango permitido." } ```
- ```json {   "code": "invalid_attribute_value",   "meaning": "El atributo principal incluye valores no relacionados con talles." } ```
- ```json {   "code": "duplicated_measure_value",   "meaning": "La medida está duplicada." } ```
- ```json {   "code": "value_is_not_the_same_type",   "meaning": "FILTRABLE_SIZE mezcla valores numéricos y alfanuméricos." } ```
- ```json {   "code": "invalid_row_attribute",   "meaning": "Atributo incompatible con el tipo de medida de la guía." } ```
- ```json {   "code": "missing.fashion_grid.grid_id.values",   "meaning": "Falta SIZE_GRID_ID." } ```
- ```json {   "code": "missing.fashion_grid.grid_row_id.values",   "meaning": "Falta SIZE_GRID_ROW_ID." } ```
- ```json {   "code": "missing.fashion_grid.size.values",   "meaning": "Falta SIZE." } ```
- ```json {   "code": "invalid.fashion_grid.grid_id.values",   "meaning": "SIZE_GRID_ID no corresponde a una guía válida." } ```
- ```json {   "code": "invalid.fashion_grid.grid_row_id.values",   "meaning": "SIZE_GRID_ROW_ID no existe en la guía." } ```
- ```json {   "code": "invalid.fashion_grid.size.values",   "meaning": "SIZE o GENDER no coincide con la fila de la guía." } ```
- ```json {   "code": "invalid.fashion_grid.seller_id.values",   "meaning": "La guía personalizada pertenece a otro vendedor." } ```

**Ejemplos documentados**

- Ejemplos JSON de errores de creación/asociación y de una infracción con reason/remedy.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/validacion-de-guia-de-talles](https://developers.mercadolibre.com.co/es_co/validacion-de-guia-de-talles)  
**Captura:** 2026-10-08T22:52:57.692Z
