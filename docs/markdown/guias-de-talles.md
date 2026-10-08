---
id: "guias-de-talles"
title: "Gestionar guía de talles"
section: "Guía para productos"
subsection: "Guías de Talles"
url: "https://developers.mercadolibre.com.co/es_co/guias-de-talles"
source_updated_at: "09/07/2026"
captured_at: "2026-10-08T22:51:54.750Z"
sha256: "a48b178f2349a3545420a1a07dbb659c56e0806dce95c1895276ef8d198da599"
---

# Gestionar guía de talles

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 09/07/2026  
**Captura:** 2026-10-08T22:51:54.750Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/guias-de-talles](https://developers.mercadolibre.com.co/es_co/guias-de-talles)

## Resumen

Explica cómo crear, consultar y mantener guías de talles del catálogo y cómo asociarlas a publicaciones. Cubre tipos de guía, atributos y filas de medidas, así como las diferencias entre guías `SPECIFIC`, `BRAND` y `STANDARD`.

## Contenido y conceptos documentados

### Modelo y restricciones

- La documentación indica autenticación `Bearer` y disponibilidad en Argentina, México, Brasil, Uruguay, Colombia, Perú, Ecuador y Chile. En los países indicados como soportados para creación personalizada se usa tipo `SPECIFIC`; la página diferencia además guías `BRAND` y `STANDARD`.
- La creación se realiza con `names`, `domain_id`, `site_id`, `main_attribute`, `attributes` y `rows`; `measure_type` puede ser `BODY_MEASURE`, `CLOTHING_MEASURE` o `MIXED_MEASURE` y queda inmutable. `name` admite hasta 60 caracteres y no permite paréntesis ni guiones. El dominio no debe llevar prefijo de sitio y el sitio del token debe corresponder.
- Los atributos admiten `required` y `main_attribute_candidate`; `number_unit` debe incluir `struct` y las listas deben usar `value_id` válidos. La especificación de dominio determina atributos válidos. Un valor de lista inválido puede producir `chart_validation_error` (HTTP 400) con código `value_is_not_in_the_list`.
- En filas de `BRAND`/`STANDARD` se documenta `sites`; en `SPECIFIC`, los atributos de fila. Se pueden agregar atributos de fila, pero no editar el talle principal ni borrar filas. La edición de la guía se limita a nombres y no altera el talle principal, filas ni atributos generales.
- La asociación usa `SIZE_GRID_ID` y `SIZE_GRID_ROW_ID`; este último va en atributos del ítem sin variaciones y dentro de cada variación cuando las hay. Solo se eliminan guías no utilizadas; el chequeo puede tardar 24 horas. Campos omitidos por la fuente: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Eliminar guía de talles

**Método:** `DELETE`  
**Ruta:** `/catalog/charts/$CHART_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Solicita la eliminación de una guía sin publicaciones asociadas.

**Parámetros**

- `CHART_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La verificación puede tardar hasta 24 horas; se muestran los estados INACTIVE y ACTIVE.

### Consultar guía de talles

**Método:** `GET`  
**Ruta:** `/catalog/charts/$CHART_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene definición y datos de una guía existente.

**Parámetros**

- `CHART_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- names
- domain_id
- site_id
- type
- seller_id
- main_attribute_id
- attributes
- rows

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con CHART_ID 232382.

### Crear guía de talles

**Método:** `POST`  
**Ruta:** `/catalog/charts`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una guía con nombres localizados, dominio, sitio, talle principal, atributos y filas.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "names",
    "domain_id",
    "site_id",
    "main_attribute",
    "attributes",
    "rows",
    "measure_type (BODY_MEASURE, CLOTHING_MEASURE o MIXED_MEASURE)"
  ]
}
```

**Respuesta**

- id
- names
- domain_id
- site_id
- type
- seller_id
- main_attribute_id
- attributes
- rows

**Errores documentados**

- ```json {   "code": 400,   "meaning": "chart_validation_error; puede incluir value_is_not_in_the_list cuando un valor de atributo tipo list no coincide con la ficha técnica." } ```

**Ejemplos**

- La fuente incluye ejemplos de guías SPECIFIC para calzado y prendas.

### Agregar fila de talles

**Método:** `POST`  
**Ruta:** `/catalog/charts/$CHART_ID/rows`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega una fila de medidas a una guía.

**Parámetros**

- `CHART_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "sites (para BRAND/STANDARD)",
    "attributes (para SPECIFIC)"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La estructura de fila depende del tipo de guía.

### Crear publicación asociada a guía

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una publicación que vincula una guía y una fila de talla.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "SIZE_GRID_ID",
    "SIZE_GRID_ROW_ID (en atributos del ítem sin variaciones; dentro de cada variación cuando existen variantes)"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página ofrece ejemplos para ítems con y sin variaciones.

### Actualizar nombres de guía

**Método:** `PUT`  
**Ruta:** `/catalog/charts/$CHART_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica los nombres localizados de una guía.

**Parámetros**

- `CHART_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "names"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La edición se limita a nombres; no altera el talle principal, filas o atributos generales.

### Actualizar fila de talles

**Método:** `PUT`  
**Ruta:** `/catalog/charts/$CHART_ID/rows/$ROW_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza o completa los atributos permitidos de una fila.

**Parámetros**

- `CHART_ID` (path, obligatorio)
- `ROW_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "atributos adicionales de la fila; no permite cambiar el talle principal"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- No permite eliminar filas ni cambiar el talle principal.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/guias-de-talles](https://developers.mercadolibre.com.co/es_co/guias-de-talles)  
**Captura:** 2026-10-08T22:51:54.750Z
