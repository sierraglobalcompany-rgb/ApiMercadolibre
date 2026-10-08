---
id: "experiencia-de-compra"
title: "Experiencia de compra"
section: "Guía para productos"
subsection: "Métricas y Tendencias"
url: "https://developers.mercadolibre.com.co/es_co/experiencia-de-compra"
source_updated_at: "03/02/2026"
captured_at: "2026-10-08T22:51:47.114Z"
sha256: "94026661f158870feb77ade0f2a197579b171ba71de7cccdbfc7f3408cde7147"
---

# Experiencia de compra

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 03/02/2026  
**Captura:** 2026-10-08T22:51:47.114Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/experiencia-de-compra](https://developers.mercadolibre.com.co/es_co/experiencia-de-compra)

## Resumen

Esta página describe el contrato para consultar la experiencia de compra de publicaciones y productos de usuario (UP). La respuesta permite mostrar nivel, estado, problemas y acciones recomendadas para ayudar al vendedor a mejorar la atención y la exposición. La funcionalidad está disponible en Argentina, Brasil, Uruguay, México, Colombia, Chile y Perú.

## Contenido y conceptos documentados

### Conceptos y restricciones

- Las dos consultas requieren `locale`; la fuente enumera `es_MX`, `es_UY`, `es_CO`, `es_CL`, `es_AR`, `es_PE`, `pt_BR` y `en_US` para ítems, y no incluye `en_US` en la lista para UP.
- La autenticación documentada es `Authorization: Bearer $ACCESS_TOKEN`. No se envía un cuerpo.
- Para ítems, la respuesta contiene `item_id`, `title`, `subtitles`, `actions`, `reputation`, `status` y `metrics_details`, con problemas y distribución de métricas. Para UP contiene `up_id`, `freeze`, `title`, `consequence`, `reputation`, `status`, `reasoning`, `recommendations`, `principal_actionable` y `ai_generated`; los kits también pueden incluir `is_kit` y `kit_components`.
- Desde la migración al modelo User Products, consultar por el endpoint de ítems una publicación ya migrada devuelve HTTP 302; las publicaciones no migradas conservan el comportamiento indicado.
- La fuente documenta errores HTTP 400, 404 y 500. Campos no especificados por la página: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Experiencia de compra de ítem

**Método:** `GET`  
**Ruta:** `/reputation/items/$ITEM_ID/purchase_experience/integrators`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el estado, reputación, métricas y acciones sugeridas para la experiencia de compra de una publicación.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `locale` (query, obligatorio): Locale requerido; la lista de ítems incluye es_MX, es_UY, es_CO, es_CL, es_AR, es_PE, pt_BR y en_US.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- item_id
- freeze
- status
- title
- subtitles
- actions
- reputation
- metrics_details

**Errores documentados**

- ```json {   "code": 302,   "meaning": "Ítem ya migrado a User Products; aplicar el recurso para UP." } ```
- ```json {   "code": 400,   "meaning": "Bad Request" } ```
- ```json {   "code": 404,   "meaning": "Resource not found" } ```
- ```json {   "code": 500,   "meaning": "Internal Server Error" } ```

**Ejemplos**

- Ejemplo con ITEM_ID MLA1391786841 y locale=es_AR; la fuente incluye respuesta con métricas y problemas.

### Experiencia de compra de User Product

**Método:** `GET`  
**Ruta:** `/reputation/user_products/{UP_ID}/purchase_experience/integrators`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene la experiencia de compra de un User Product, con análisis, recomendaciones y posibles componentes de kit.

**Parámetros**

- `UP_ID` (path, obligatorio)
- `locale` (query, obligatorio): Locale requerido; la lista para UP omite en_US.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- up_id
- freeze
- title
- consequence
- reputation
- status
- reasoning
- recommendations
- principal_actionable
- ai_generated
- is_kit
- kit_components

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Bad Request" } ```
- ```json {   "code": 404,   "meaning": "Resource not found" } ```
- ```json {   "code": 500,   "meaning": "Internal Server Error" } ```

**Ejemplos**

- La página presenta ejemplos de UP y kit con componentes.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/experiencia-de-compra](https://developers.mercadolibre.com.co/es_co/experiencia-de-compra)  
**Captura:** 2026-10-08T22:51:47.114Z
