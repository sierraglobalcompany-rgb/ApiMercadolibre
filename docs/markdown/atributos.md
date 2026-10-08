---
id: "atributos"
title: "Atributos"
section: "Recursos de la API"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/atributos"
source_updated_at: "08/06/2026"
captured_at: "2026-10-08T22:53:39.739Z"
sha256: "ecfc516ba66d54cb9e810eb4a6e96ffb5377edfe333f2b6d0f1d71694801b2fd"
---

# Atributos

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 08/06/2026  
**Captura:** 2026-10-08T22:53:39.739Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/atributos](https://developers.mercadolibre.com.co/es_co/atributos)

## Resumen

La página documenta cómo consultar la definición y la ficha técnica de atributos por categoría, validar campos condicionales y usarlos al crear o actualizar ítems. Los atributos pueden ser de tipo `string`, `number`, `number_unit`, `boolean` o `list`; su esquema incluye IDs, nombres, valores y tags de comportamiento. La fuente distingue los atributos necesarios para publicar de los que afectan el posicionamiento y cubre datos no aplicables (N/A), dimensiones del paquete y valores más usados.

## Contenido y conceptos documentados

### Tipos, valores y tags

Los valores de tipo texto y número admiten valores sugeridos y, según el atributo, valores nuevos; `number_unit` combina magnitud y unidad, `boolean` requiere un ID de valor y `list` usa los valores admitidos. Los tags describen comportamientos como variaciones, atributos fijos o inferidos, lectura solamente, obligatoriedad, atributos ocultos y campos condicionales.

### Requisitos y mantenimiento de atributos

`technical_specs/input` permite anticipar atributos requeridos y `technical_specs/output` organiza la ficha técnica para mostrarla. `conditional_required` se valida enviando los datos del ítem; la fuente limita ese recurso a Argentina, Brasil y México. Para marcar una especificación N/A se envía `value_id: "-1"` y `value_name: null`; su visualización usa `include_internal_attributes=true`. Los atributos requeridos no se pueden borrar y la fuente muestra el error `item.attributes.deleted_required`. Para actualizar atributos existentes, la guía recomienda conservar y reenviar los que deben permanecer.

### Dimensiones y calidad de publicación

Para ciertos vendedores ME2 en cross docking y `xd_drop_off`, se documentan `SELLER_PACKAGE_HEIGHT`, `SELLER_PACKAGE_LENGTH` y `SELLER_PACKAGE_WIDTH` en centímetros y `SELLER_PACKAGE_WEIGHT` en gramos; los vendedores ME1 continúan con `shipping.dimensions`. La búsqueda con el tag `incomplete_technical_specs` identifica ítems que pueden perder exposición. El endpoint de top values devuelve valores ordenados por `metric` descendente y acepta atributos conocidos adicionales.

## Operaciones de API

## Conceptos y recursos asociados

### Modelo de tipos y comportamientos de atributos

Explica tipos de valor y tags que condicionan obligatoriedad, variaciones, edición, visibilidad e inferencia.

**Respuesta**

No documentado en la fuente.

**Ejemplos documentados**

- Tags documentados incluyen required, conditional_required, fixed, inferred, allow_variations y read_only.
## Operaciones de API

### Actualizar o eliminar valores de atributos

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega o modifica atributos de una publicación; la guía también muestra cómo borrar un valor manteniendo el atributo.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la publicación.

**Solicitud**

```json
{
  "attributes": [
    {
      "id": "ID del atributo",
      "value_id": "ID del valor (opcional en ejemplo)",
      "value_name": "Nombre del valor (opcional en ejemplo)"
    }
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "item.attributes.deleted_required",   "meaning": "La página lo asocia a intentar borrar con null un atributo requerido." } ```

**Ejemplos**

- Para borrar un valor se envían value_id y value_name como null; los atributos con allow_variations no pueden marcarse N/A.

### Consultar atributos de categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve las definiciones de atributos disponibles para una categoría, incluidos sus tipos, valores posibles y tags.

**Parámetros**

- `category_id` (path, obligatorio): Identificador de la categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo de atributos con id, name, value_type, values, tags y grupos.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Tipos documentados: string, number, number_unit, boolean y list.

### Consultar atributos N/A de un ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}?attributes=attributes&include_internal_attributes=true`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los atributos del ítem incluyendo valores internos marcados como no aplicables.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la publicación.
- `attributes` (query): El ejemplo usa attributes=attributes.
- `include_internal_attributes` (query): El ejemplo usa true para incluir atributos internos N/A.

**Solicitud**

No documentado en la fuente.

**Respuesta**

La respuesta de ejemplo muestra attributes con value_id=-1 y value_name=null para N/A.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La llamada genérica de la fuente presenta una URL incompleta; el ejemplo concreto usa los dos parámetros de query indicados.

### Consultar publicación antes de actualizar atributos

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los datos del ítem y permite revisar los atributos ya cargados antes de enviar cambios.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la publicación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Respuesta de ítem que incluye attributes y valores existentes.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Crear publicación con dimensiones de paquete

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Ejemplo de creación de ítem con atributos de altura, longitud, ancho y peso del paquete.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "attributes": [
    "SELLER_PACKAGE_HEIGHT",
    "SELLER_PACKAGE_LENGTH",
    "SELLER_PACKAGE_WIDTH",
    "SELLER_PACKAGE_WEIGHT"
  ],
  "units": "cm para altura/longitud/ancho y g para peso"
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente ejemplifica el body con los atributos del paquete.

### Consultar ficha técnica de entrada

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/technical_specs/input`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Permite identificar grupos y atributos técnicos de entrada y los campos marcados como requeridos.

**Parámetros**

- `category_id` (path, obligatorio): Identificador de la categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto con groups, labels, components y configuración de entrada.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar ficha técnica de salida

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/technical_specs/output`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve la ficha técnica organizada para mostrar los productos como en Mercado Libre.

**Parámetros**

- `category_id` (path, obligatorio): Identificador de la categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto con main_title y groups de componentes de presentación.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Buscar ítems con ficha técnica incompleta

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista publicaciones del usuario que llevan el tag incomplete_technical_specs y pueden estar perdiendo exposición.

**Parámetros**

- `user_id` (path, obligatorio): Identificador del vendedor.
- `tags` (query, obligatorio): Se envía incomplete_technical_specs.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Respuesta con seller_id, paging, results, filters y available_filters.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con tags=incomplete_technical_specs.

### Referencia HTTP POST /catalog_domains/MLA-CELLPHONES/attributes/BRAND/top_values

**Método:** `POST`  
**Ruta:** `/catalog_domains/MLA-CELLPHONES/attributes/BRAND/top_values`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /catalog_domains/MLA-CELLPHONES/attributes/BRAND/top_values. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP POST /catalog_domains/MLA-CELLPHONES/attributes/MODEL/top_values

**Método:** `POST`  
**Ruta:** `/catalog_domains/MLA-CELLPHONES/attributes/MODEL/top_values`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /catalog_domains/MLA-CELLPHONES/attributes/MODEL/top_values. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Consultar valores más usados de un atributo

**Método:** `POST`  
**Ruta:** `/catalog_domains/{domain_id}/attributes/{attribute_id}/top_values`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve los valores más utilizados para un atributo de dominio, ordenados por su métrica; puede considerar otros atributos conocidos.

**Parámetros**

- `domain_id` (path, obligatorio): ID del dominio.
- `attribute_id` (path, obligatorio): ID del atributo.
- `limit` (query, opcional): Máximo de 1000 resultados.
- `metric_type` (query, opcional): La fuente menciona NOL_90.

**Solicitud**

```json
{
  "known_attributes": [
    {
      "id": "ID del atributo",
      "value_id": "ID del valor"
    }
  ]
}
```

**Respuesta**

Lista de id, name y metric, ordenada por metric descendente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Para calcular valores de MODEL, el ejemplo filtra por BRAND con value_id 206.

### Validar atributos condicionales

**Método:** `POST`  
**Ruta:** `/categories/{category_id}/attributes/conditional`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Determina si los atributos con tag conditional_required son necesarios para el ítem enviado.

**Parámetros**

- `category_id` (path, obligatorio): Identificador de la categoría.

**Solicitud**

```json
{
  "fields": [
    "title",
    "category_id",
    "price",
    "currency_id",
    "available_quantity",
    "buying_mode",
    "condition",
    "listing_type_id",
    "description",
    "pictures",
    "attributes"
  ],
  "note": "La fuente muestra un body de ítem como ejemplo; no declara que todos esos campos sean obligatorios."
}
```

**Respuesta**

La respuesta indica los required_attributes; el ejemplo de excepción devuelve required_attributes vacío.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente limita la disponibilidad a Argentina, Brasil y México.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/atributos](https://developers.mercadolibre.com.co/es_co/atributos)  
**Captura:** 2026-10-08T22:53:39.739Z
