# Recursos de la API

22 páginas del portal oficial en esta área.

## [Atributos](../markdown/atributos.md)

Actualización indicada por la fuente: 08/06/2026. Captura: 2026-10-08T22:53:39.739Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/atributos](https://developers.mercadolibre.com.co/es_co/atributos)

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

---

## [Bloqueo de aplicaciones](../markdown/bloqueo-de-aplicaciones.md)

Actualización indicada por la fuente: 15/04/2026. Captura: 2026-10-08T22:53:41.757Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/bloqueo-de-aplicaciones](https://developers.mercadolibre.com.co/es_co/bloqueo-de-aplicaciones)

# Bloqueo de aplicaciones

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 15/04/2026  
**Captura:** 2026-10-08T22:53:41.757Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/bloqueo-de-aplicaciones](https://developers.mercadolibre.com.co/es_co/bloqueo-de-aplicaciones)

## Resumen

La página explica por qué se puede bloquear una aplicación, cómo afecta a la operación de los vendedores y qué acciones tomar según el motivo. Mientras el bloqueo esté activo, la integración no puede consumir APIs de Mercado Libre ni de Mercado Pago.

## Contenido y conceptos documentados

Los motivos enumerados son `NOT_COMPLY_KYC` (validación de datos), `NOT_COMPLY_T&C_RULES` (Términos y Condiciones), `EXCESSIVE_API_CALL` (llamadas excesivas o uso incorrecto de token) e `INTEGRATORS_DATA_INFRACTION` (tráfico de datos). La fuente indica que los usuarios pueden recibir `unauthorized_scopes` con estado `401`. Recomienda revisar los datos de cuenta y validar identidad para KYC, respetar las reglas, controlar errores de la familia 400 no previstos y verificar el uso de APIs que generan valor.

## Operaciones de API

## Conceptos y recursos asociados

### Causas y efectos del bloqueo de aplicaciones

Describe motivos de bloqueo, impacto sobre vendedores y pasos de remediación para restablecer el uso de APIs.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "unauthorized_scopes",   "meaning": "La fuente indica estado HTTP 401 para usuarios afectados por una aplicación bloqueada." } ```

**Ejemplos documentados**

- Motivos: NOT_COMPLY_KYC, NOT_COMPLY_T&C_RULES, EXCESSIVE_API_CALL e INTEGRATORS_DATA_INFRACTION.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/bloqueo-de-aplicaciones](https://developers.mercadolibre.com.co/es_co/bloqueo-de-aplicaciones)  
**Captura:** 2026-10-08T22:53:41.757Z

---

## [Comunicaciones](../markdown/conoce-las-novedades-que-reciben-los-vendedores.md)

Actualización indicada por la fuente: 07/05/2025. Captura: 2026-10-08T22:53:42.622Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/conoce-las-novedades-que-reciben-los-vendedores](https://developers.mercadolibre.com.co/es_co/conoce-las-novedades-que-reciben-los-vendedores)

# Comunicaciones

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 07/05/2025  
**Captura:** 2026-10-08T22:53:42.622Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/conoce-las-novedades-que-reciben-los-vendedores](https://developers.mercadolibre.com.co/es_co/conoce-las-novedades-que-reciben-los-vendedores)

## Resumen

El recurso de Comunicaciones permite consultar novedades vigentes, alertas, lanzamientos, capacitaciones y publicidades destinadas a vendedores o integradores. Cada respuesta depende del usuario cuyo access token se usa; la consulta más reciente aparece primero.

## Contenido y conceptos documentados

Para comunicaciones de vendedores se usa el token de cada vendedor; las dirigidas a la integración requieren el token del usuario propietario de la aplicación y que este haya otorgado el grant. `limit` y `offset` controlan la paginación. La respuesta contiene `paging` y `results`; cada resultado puede incluir `actions`, `id`, `label`, `description`, `highlighted`, `from_date` y `tags`. La fuente también describe agrupaciones por categoría y subcategoría y tipos de tags para áreas como envíos, eventos, facturación, países y publicaciones.

## Operaciones de API
## Operaciones de API

### Consultar comunicaciones vigentes

**Método:** `GET`  
**Ruta:** `/communications/notices`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve las comunicaciones activas para el usuario autenticado, con paginación, acciones, fechas y tags.

**Parámetros**

- `limit` (query, opcional): Límite máximo de comunicaciones.
- `offset` (query, opcional): Desplazamiento para paginar resultados.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto con paging y results; results puede incluir actions, id, label, description, highlighted, from_date y tags.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Token de vendedor para sus comunicaciones; token owner de la app para comunicaciones de la integración.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/conoce-las-novedades-que-reciben-los-vendedores](https://developers.mercadolibre.com.co/es_co/conoce-las-novedades-que-reciben-los-vendedores)  
**Captura:** 2026-10-08T22:53:42.622Z

---

## [Consulta usuarios](../markdown/producto-consulta-usuarios.md)

Actualización indicada por la fuente: 12/01/2026. Captura: 2026-10-08T22:53:43.459Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/producto-consulta-usuarios](https://developers.mercadolibre.com.co/es_co/producto-consulta-usuarios)

# Consulta usuarios

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 12/01/2026  
**Captura:** 2026-10-08T22:53:43.459Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/producto-consulta-usuarios](https://developers.mercadolibre.com.co/es_co/producto-consulta-usuarios)

## Resumen

Esta guía muestra cómo consultar el usuario autenticado y la información pública o privada de otro usuario. La respuesta puede incluir identidad, contacto, reputación, estado de cuenta y datos de ventas; la fuente advierte que la información privada no debe divulgarse. Los IDs nuevos pueden exceder Int32, por lo que deben almacenarse como Int64.

## Contenido y conceptos documentados

La respuesta de `/users/me` incluye el perfil del usuario del token. `/users/{user_id}` devuelve datos públicos y, cuando el usuario autorizó la aplicación y se usa un token válido, también puede incluir datos privados como nombre, email, teléfono y dirección. La página señala el error HTTP `206 Partial Content` cuando falla la consulta de algunos datos, por ejemplo la reputación.

## Operaciones de API
## Operaciones de API

### Consultar información de usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve el perfil público del usuario; si autorizó la aplicación y se usa su token, el ejemplo incluye datos privados adicionales.

**Parámetros**

- `user_id` (path, obligatorio): Identificador del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

El ejemplo público contiene perfil y reputación; el ejemplo autorizado también muestra contacto e información privada.

**Errores documentados**

- ```json {   "code": "206 Partial Content",   "meaning": "La API puede devolver datos incompletos si falla la consulta de algún dato, como la reputación." } ```

**Ejemplos**

- La fuente advierte que los IDs pueden exceder Int32 y deben manejarse como Int64.

### Consultar datos del usuario autenticado

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene la información asociada al usuario representado por el access token.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con id, nickname, registro, país, perfil, reputación y estado; algunos campos pueden ser privados del usuario autenticado.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/producto-consulta-usuarios](https://developers.mercadolibre.com.co/es_co/producto-consulta-usuarios)  
**Captura:** 2026-10-08T22:53:43.459Z

---

## [Diagnóstico de imágenes](../markdown/diagnostico-imagenes.md)

Actualización indicada por la fuente: 29/12/2025. Captura: 2026-10-08T22:53:44.400Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/diagnostico-imagenes](https://developers.mercadolibre.com.co/es_co/diagnostico-imagenes)

# Diagnóstico de imágenes

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:53:44.400Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/diagnostico-imagenes](https://developers.mercadolibre.com.co/es_co/diagnostico-imagenes)

## Resumen

La API de diagnóstico analiza imágenes antes de asociarlas a una publicación y devuelve problemas detectados junto con textos de corrección. Evalúa, según categoría, fondo no blanco, tamaño mínimo, texto o logos y marcas de agua. La guía recomienda validar cada imagen durante la carga y especificar su uso dentro del ítem.

## Contenido y conceptos documentados

El body contiene `picture_url` o `picture_id` (se debe enviar solo uno) y `context.category_id`; también puede incluir `id`, `context.title` y `context.picture_type`. La URL debe ser pública, estática y accesible. Los tipos de imagen son `thumbnail`, `variation_thumbnail` y `other`; si se omite el tipo, se devuelven diagnósticos para todos. La respuesta incluye un ID y una lista `diagnostics`, con `picture_type`, `action`, `detections` y `wordings`. `action: diagnostic` indica hallazgos; `empty` significa que la imagen es válida. La fuente recomienda permitir continuar si el diagnóstico falla, mostrando que no fue posible validar.

## Operaciones de API
## Operaciones de API

### Diagnosticar imagen de publicación

**Método:** `POST`  
**Ruta:** `/moderations/pictures/diagnostic`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Valida una imagen para detectar condiciones que pueden causar moderación antes de asociarla a una publicación.

**Parámetros**

- `picture_url` (body): Enviar exactamente uno de picture_url o picture_id; no ambos.
- `picture_id` (body): Enviar exactamente uno de picture_url o picture_id; no ambos.
- `context.category_id` (body, obligatorio): Categoría usada para seleccionar reglas.
- `id` (body, opcional): ID opcional; si se omite, se genera automáticamente.
- `context.title` (body, opcional): Título recomendado para aportar contexto.
- `context.picture_type` (body, opcional): thumbnail, variation_thumbnail u other; opcional según fuente, recomendado si se conoce el uso.

**Solicitud**

```json
{
  "fields": [
    "id",
    "picture_url o picture_id",
    "context.category_id",
    "context.title",
    "context.picture_type"
  ],
  "note": "Enviar solo uno de picture_url o picture_id."
}
```

**Respuesta**

Objeto con id y diagnostics; cada diagnóstico incluye picture_type, action, detections y wordings.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Las detecciones documentadas incluyen white_background, minimum_size, text_logo y watermark.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/diagnostico-imagenes](https://developers.mercadolibre.com.co/es_co/diagnostico-imagenes)  
**Captura:** 2026-10-08T22:53:44.400Z

---

## [Direcciones del usuario](../markdown/direcciones-del-usuario.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:53:45.340Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/direcciones-del-usuario](https://developers.mercadolibre.com.co/es_co/direcciones-del-usuario)

# Direcciones del usuario

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:45.340Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/direcciones-del-usuario](https://developers.mercadolibre.com.co/es_co/direcciones-del-usuario)

## Resumen

La guía documenta la consulta de direcciones asociadas a un usuario y describe los campos de la respuesta, incluidos domicilio, ubicación, geolocalización, tipos y estado de cada dirección.

## Contenido y conceptos documentados

La respuesta de ejemplo incluye `id`, `user_id`, datos de contacto, `address_line`, calle, número, piso, apartamento y código postal; `city`, `state`, `country`, `neighborhood` y `municipality` pueden aportar identificadores y nombres. `search_location` describe la ubicación utilizada en búsquedas; `types` incluye ejemplos como `default_selling_address` y `shipping`. También se documentan `latitude`, `longitude`, `geolocation_type`, `status`, `date_created`, `normalized` y horarios especiales (`open_hours`).

## Operaciones de API
## Operaciones de API

### Consultar direcciones de usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/addresses`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve las direcciones asociadas al usuario y sus datos de ubicación, geolocalización, tipos y estado.

**Parámetros**

- `user_id` (path, obligatorio): Identificador del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con datos de dirección, city/state/country, search_location, types, coordenadas, status, date_created y open_hours.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El ejemplo usa user_id 145834937.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/direcciones-del-usuario](https://developers.mercadolibre.com.co/es_co/direcciones-del-usuario)  
**Captura:** 2026-10-08T22:53:45.340Z

---

## [Dominios y Categorías](../markdown/dominios-y-categorias.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:53:46.261Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/dominios-y-categorias](https://developers.mercadolibre.com.co/es_co/dominios-y-categorias)

# Dominios y Categorías

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:46.261Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/dominios-y-categorias](https://developers.mercadolibre.com.co/es_co/dominios-y-categorias)

## Resumen

La guía reúne consultas para descubrir sitios, categorías, dominios y datos de publicación. Distingue sitio (mercado, identificado por tres letras), dominio (familia de productos) y categoría (clasificación de productos dentro de un dominio). Sus ejemplos permiten obtener exposición y precios de publicación, navegar el árbol de categorías, consultar atributos y predecir una categoría a partir del artículo.

## Contenido y conceptos documentados

Las respuestas de los ejemplos incluyen IDs y nombres de sitios, categorías y dominios; detalles de categoría, exposición de la publicación, precios, atributos y packs para clasificados. El predictor de categoría utiliza `q` (y en el ejemplo, `limit`) y devuelve `domain_id`, `domain_name`, `category_id`, `category_name` y atributos sugeridos. El endpoint de especificaciones técnicas del dominio devuelve estructura de entrada y salida organizada en grupos y componentes. Las llamadas de ejemplo envían el access token en el header Bearer.

## Operaciones de API

## Conceptos y recursos asociados

### Sitios, dominios y categorías

Define los tres niveles usados por la API para organizar mercados y familias de productos.

**Respuesta**

Sitio se identifica con tres letras; el dominio agrupa familias de productos y una categoría clasifica productos similares.

**Ejemplos documentados**

- La fuente usa MLA/MLB/MLM y CELLPHONES/SNEAKERS/BICYCLES como ejemplos.
### Ruta mencionada /sites/{SITE_ID}/listing_types

La fuente menciona la ruta /sites/{SITE_ID}/listing_types, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/sites/{SITE_ID}/listing_types`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar atributos de categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene las definiciones de atributos de una categoría.

**Parámetros**

- `category_id` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de definiciones de atributos.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Listar categorías por sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/categories`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el árbol de categorías del sitio.

**Parámetros**

- `site_id` (path, obligatorio): ID del sitio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de id y name de categoría.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar detalle de categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el detalle de una categoría.

**Parámetros**

- `category_id` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

La respuesta de ejemplo contiene datos de identificación y configuración de categoría.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar exposiciones de publicación

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/listing_exposures`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene niveles de exposición y prioridades del sitio.

**Parámetros**

- `site_id` (path, obligatorio): ID del sitio, por ejemplo MLA.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Elementos con id, name, home_page, category_home_page, advertising_on_listing_page y priority_in_search.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar ficha técnica de dominio

**Método:** `GET`  
**Ruta:** `/domains/{domain_id}/technical_specs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene la estructura de especificaciones técnicas del dominio.

**Parámetros**

- `domain_id` (path, obligatorio): ID del dominio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto con input y grupos de especificaciones.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar packs de promoción de categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/classifieds_promotion_packs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene packs de promoción de clasificados para una categoría.

**Parámetros**

- `category_id` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

La respuesta de ejemplo lista packs con id, category_id, brand, description y price.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar precios de publicación

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/listing_prices`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista precios para vender y comprar en el sitio para el precio indicado.

**Parámetros**

- `site_id` (path, obligatorio): ID del sitio.
- `price` (query, obligatorio): Precio consultado; el ejemplo usa 1.

**Solicitud**

No documentado en la fuente.

**Respuesta**

La respuesta de ejemplo lista datos de precios por tipo de publicación.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Predecir dominio y categoría

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/domain_discovery/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca una categoría correspondiente a un artículo según término de búsqueda y atributos.

**Parámetros**

- `site_id` (path, obligatorio): ID del sitio.
- `q` (query, obligatorio): Término de búsqueda.
- `limit` (query, opcional): El ejemplo usa limit=1.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Resultados con domain_id, domain_name, category_id, category_name y atributos.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Referencia HTTP GET /sites/{SITE_ID}/listing_types

**Método:** `GET`  
**Ruta:** `/sites/{SITE_ID}/listing_types`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /sites/{SITE_ID}/listing_types. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Consultar sitios

**Método:** `GET`  
**Ruta:** `/sites`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista sitios de Mercado Libre y sus monedas predeterminadas.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo de elementos id, name y default_currency_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/dominios-y-categorias](https://developers.mercadolibre.com.co/es_co/dominios-y-categorias)  
**Captura:** 2026-10-08T22:53:46.261Z

---

## [Favoritos](../markdown/marcadores.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:53:47.588Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/marcadores](https://developers.mercadolibre.com.co/es_co/marcadores)

# Favoritos

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:47.588Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/marcadores](https://developers.mercadolibre.com.co/es_co/marcadores)

## Resumen

El recurso de Marcadores permite consultar los ítems guardados por el usuario, registrar un marcador y eliminarlo. La página describe la sincronización de estas referencias con aplicaciones móviles.

## Contenido y conceptos documentados

El acceso a la lista requiere el token del usuario. El ejemplo de respuesta contiene `item_id` y `bookmarked_date`; para crear un marcador se envía `item_id` en el body. No documentado en la fuente: límites, errores y paginación.

## Operaciones de API
## Operaciones de API

### Consultar marcadores del usuario

**Método:** `GET`  
**Ruta:** `/users/me/bookmarks`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve referencias a los ítems guardados por el usuario autenticado.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de item_id y bookmarked_date.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Agregar marcador

**Método:** `POST`  
**Ruta:** `/users/me/bookmarks`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega una referencia de ítem a los marcadores del usuario.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "item_id": "Identificador de ítem."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El ejemplo envía item_id en JSON.

### Eliminar marcador

**Método:** `DELETE`  
**Ruta:** `/users/me/bookmarks/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la referencia del ítem indicado.

**Parámetros**

- `item_id` (path, obligatorio): Identificador del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

El ejemplo muestra item_id y bookmarked_date.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/marcadores](https://developers.mercadolibre.com.co/es_co/marcadores)  
**Captura:** 2026-10-08T22:53:47.588Z

---

## [Gestionar moderaciones](../markdown/gestionar-moderaciones.md)

Actualización indicada por la fuente: 08/06/2026. Captura: 2026-10-08T22:53:48.734Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/gestionar-moderaciones](https://developers.mercadolibre.com.co/es_co/gestionar-moderaciones)

# Gestionar moderaciones

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 08/06/2026  
**Captura:** 2026-10-08T22:53:48.734Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestionar-moderaciones](https://developers.mercadolibre.com.co/es_co/gestionar-moderaciones)

## Resumen

La guía explica cómo consultar moderaciones activas y el historial de infracciones, interpretar sus motivos y soluciones y filtrar publicaciones afectadas. Recomienda mostrar al vendedor el `reason` y el `remedy` que la API devuelve para cada caso.

## Contenido y conceptos documentados

El `moderation_reference_id` se construye con el ID del elemento y el sufijo del tipo: `-ITM` para publicación, `-QUE` para pregunta/respuesta y `-REV` para opinión. La respuesta de última moderación incluye nombre, ID temporal, fecha, evidencias y textos `REASON`/`REMEDY`; una baja por `DENYLIST` puede tener solo motivo. Para moderaciones activas se buscan ítems `pending`, incluidos subestados como `warning`, `waiting_for_patch`, `held`, `pending_documentation`, `forbidden` y `picture_downloading_pending`. El histórico permite filtrar por elemento, tipo, fechas, idioma, límite, offset y orden; el límite indicado es de 1 a 20.

## Operaciones de API

## Conceptos y recursos asociados

### Estados, referencias y recomendaciones de moderación

Describe estados de moderación y cómo relacionar una notificación con la consulta de la última moderación.

**Respuesta**

No documentado en la fuente.

**Ejemplos documentados**

- Sufijos: ITM publicación; QUE preguntas/respuestas; REV opiniones de producto.
### Ruta mencionada /items

La fuente menciona la ruta /items, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/items`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Buscar ítems en moderación

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista ítems del usuario con status pending, incluyendo estados de moderación en revisión.

**Parámetros**

- `user_id` (path, obligatorio): Identificador del usuario.
- `status` (query, obligatorio): El ejemplo y la instrucción usan pending.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Respuesta con seller_id, paging, results y orders.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Subestados citados: warning, waiting_for_patch, held, pending_documentation, forbidden y picture_downloading_pending.

### Consultar histórico de infracciones

**Método:** `GET`  
**Ruta:** `/moderations/infractions/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta infracciones históricas del usuario para ítems, preguntas/respuestas y opiniones.

**Parámetros**

- `user_id` (path, obligatorio): Identificador del usuario.
- `related_item_id` (query): Filtra por publicación relacionada.
- `element_id` (query): Filtra por elemento moderado.
- `element_type` (query): ITM, REV o QUE.
- `date_created_since` (query): Fecha inicial YYYY-MM-DD.
- `date_created_to` (query): Fecha final YYYY-MM-DD.
- `language` (query): ES o PT; por defecto el idioma indicado por la fuente es inglés.
- `limit` (query): Entre 1 y 20; por defecto 20.
- `offset` (query): Desplazamiento para paginación.
- `sort` (query): Orden por fecha; ejemplo date_created_asc o date_created_desc.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto con infractions y paging; cada infracción puede incluir id, date_created, user_id, related_item_id, element_id/type, site_id, filter_subgroup, reason y remedy.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El ejemplo filtra date_created_since y limit.

### Consultar última moderación

**Método:** `GET`  
**Ruta:** `/moderations/last_moderation/{moderation_reference_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve la moderación activa más reciente de un elemento, con evidencias y motivos o soluciones.

**Parámetros**

- `moderation_reference_id` (path, obligatorio): ID del elemento seguido por sufijo -ITM, -QUE o -REV.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista con name, id, date_created, evidences y wordings (REASON/REMEDY); DENYLIST puede incluir solo REASON.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo: MLA1234567890-ITM.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestionar-moderaciones](https://developers.mercadolibre.com.co/es_co/gestionar-moderaciones)  
**Captura:** 2026-10-08T22:53:48.734Z

---

## [Miembros del Programa](../markdown/miembros-del-programa.md)

Actualización indicada por la fuente: 26/07/2026. Captura: 2026-10-08T22:53:51.200Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/miembros-del-programa](https://developers.mercadolibre.com.co/es_co/miembros-del-programa)

# Miembros del Programa

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 26/07/2026  
**Captura:** 2026-10-08T22:53:51.200Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/miembros-del-programa](https://developers.mercadolibre.com.co/es_co/miembros-del-programa)

## Resumen

La página describe el flujo de Brand Protection Program (BPP) para que titulares de derechos o representantes autorizados consulten motivos habilitados, denuncien publicaciones y respondan a la documentación presentada por el vendedor. Su uso está restringido a miembros del programa.

## Contenido y conceptos documentados

Los motivos de denuncia tienen IDs, grupo, tipo y descripciones; el ejemplo incluye falsificación, uso ilegal de marca, libros, imágenes y otros derechos. Una denuncia devuelve un `denounce_id`; su consulta incluye estado, motivo, publicación, vendedor, fechas y documentos. La guía enumera estados desde `CREATED` hasta aprobación, rechazo o descarte. El vendedor dispone de 3 días (excepto domingos) para responder; el miembro tiene luego 3 días corridos. Solo se responde un caso en `DOCUMENTATION_PRESENTED`; para aprobar se envía `documentation_approved: "true"`, y para rechazar, `"false"` más `reject_member_id` tomado de `reject_option_member`.

## Operaciones de API

## Conceptos y recursos asociados

### Flujo de Brand Protection Program

Resume estados, plazos y restricción de uso del proceso de denuncias de propiedad intelectual.

**Respuesta**

No documentado en la fuente.

**Ejemplos documentados**

- Uso exclusivo de miembros; el vendedor dispone de 3 días excepto domingos y el miembro tiene 3 días corridos para responder.
## Operaciones de API

### Consultar caso de denuncia BPP

**Método:** `GET`  
**Ruta:** `/moderations/pppi/case/{denounce_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene estado, datos de ítem y vendedor, fechas y documentos del caso.

**Parámetros**

- `denounce_id` (path, obligatorio): ID de la denuncia.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Incluye item_info, last_updated, documents, reason_id/text, current_status, seller_id y datos de miembros.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Denunciar publicación BPP

**Método:** `POST`  
**Ruta:** `/moderations/pppi/denounces/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una denuncia de propiedad intelectual contra una publicación.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem denunciado.

**Solicitud**

```json
{
  "report_reason_id": "ID de motivo habilitado.",
  "comment": "Comentario de la denuncia."
}
```

**Respuesta**

Respuesta con status y denounce_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El ejemplo devuelve status 201.

### Consultar motivos de denuncia BPP

**Método:** `GET`  
**Ruta:** `/moderations/pppi/denounces/{site_id}/ITM/options`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista los motivos de denuncia que el miembro tiene habilitados para ítems del sitio.

**Parámetros**

- `site_id` (path, obligatorio): ID del sitio, por ejemplo MLA.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de motivos con id, group, type y descripciones/textos por idioma.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Disponible solo para miembros del Brand Protection Program.

### Responder documentación de caso BPP

**Método:** `POST`  
**Ruta:** `/moderations/pppi/case/{denounce_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Aprueba o rechaza la documentación presentada por el vendedor en una denuncia.

**Parámetros**

- `denounce_id` (path, obligatorio): ID de la denuncia.

**Solicitud**

```json
{
  "documentation_approved": "true para aprobar; false para rechazar.",
  "member_quittance": "Texto o null.",
  "reject_member_id": "ID de motivo de rechazo obtenido en reject_option_member; usado al rechazar."
}
```

**Respuesta**

Respuesta del caso con current_status y datos de la denuncia, incluida la lista reject_option_member.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Solo se responde cuando el caso está en DOCUMENTATION_PRESENTED.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/miembros-del-programa](https://developers.mercadolibre.com.co/es_co/miembros-del-programa)  
**Captura:** 2026-10-08T22:53:51.200Z

---

## [Moderaciones con pausado](../markdown/moderaciones-con-pausado.md)

Actualización indicada por la fuente: 12/06/2026. Captura: 2026-10-08T22:53:52.153Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/moderaciones-con-pausado](https://developers.mercadolibre.com.co/es_co/moderaciones-con-pausado)

# Moderaciones con pausado

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 12/06/2026  
**Captura:** 2026-10-08T22:53:52.153Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/moderaciones-con-pausado](https://developers.mercadolibre.com.co/es_co/moderaciones-con-pausado)

## Resumen

Esta guía cubre moderaciones preventivas que pausan publicaciones por precio inusual, falta de ventas, procesamiento de imágenes o reportes de inmuebles no disponibles. Indica cómo localizar los ítems, obtener el motivo y la solución sugerida y reactivar una publicación cuando corresponda.

## Contenido y conceptos documentados

Se buscan publicaciones con `status=paused` y `tags=moderation_penalty`; la respuesta devuelve IDs en `results`. La referencia para consultar moderación usa el ID de publicación seguido de `-ITM`. Durante la carga de imágenes por URL, la guía describe estados `paused` o `not_yet_active` con `picture_download_pending`; la publicación se activa automáticamente si las fotos se procesan correctamente. Para imágenes se indican mínimos de 250 px por lado y más de 500 px en al menos un lado. La reactivación usa el estado `active`; si un inmueble ya no está disponible, se recomienda cerrarlo en vez de reactivarlo.

## Operaciones de API

## Conceptos y recursos asociados

### Moderaciones preventivas con pausado

Describe causas, evidencia y acciones para moderaciones que pausan ítems sin el flujo under_review.

**Respuesta**

No documentado en la fuente.

**Ejemplos documentados**

- Motivos: precio inusual, falta de ventas, descarga de imágenes y reporte de inmueble no disponible.
## Operaciones de API

### Buscar ítems pausados con penalidad

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista publicaciones pausadas con tag moderation_penalty para revisar una moderación preventiva.

**Parámetros**

- `user_id` (path, obligatorio): Identificador del vendedor.
- `tags` (query, obligatorio): moderation_penalty.
- `status` (query, obligatorio): paused.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Respuesta con seller_id, paging, results, orders y available_orders.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Reactivar publicación pausada

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cambia el estado de la publicación a active tras revisar el motivo de la pausa.

**Parámetros**

- `item_id` (path, obligatorio): Identificador de la publicación.

**Solicitud**

```json
{
  "status": "active"
}
```

**Respuesta**

La página muestra un ejemplo de recurso actualizado; forma completa de respuesta: no documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Si un inmueble ya no está disponible, la fuente recomienda cerrarlo.

### Consultar moderación preventiva

**Método:** `GET`  
**Ruta:** `/moderations/last_moderation/{moderation_reference_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la última moderación de una publicación pausada, como precio inusual, ítem abandonado o inmueble reportado como no disponible.

**Parámetros**

- `moderation_reference_id` (path, obligatorio): ID de publicación seguido por -ITM.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Respuesta con name, id, date_created, wordings y evidence.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos: MLA926647862-ITM y MLA123444123-ITM.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/moderaciones-con-pausado](https://developers.mercadolibre.com.co/es_co/moderaciones-con-pausado)  
**Captura:** 2026-10-08T22:53:52.153Z

---

## [Moderaciones de imágenes](../markdown/moderaciones-de-imagenes.md)

Actualización indicada por la fuente: 21/07/2025. Captura: 2026-10-08T22:53:53.123Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/moderaciones-de-imagenes](https://developers.mercadolibre.com.co/es_co/moderaciones-de-imagenes)

# Moderaciones de imágenes

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 21/07/2025  
**Captura:** 2026-10-08T22:53:53.123Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/moderaciones-de-imagenes](https://developers.mercadolibre.com.co/es_co/moderaciones-de-imagenes)

## Resumen

La página explica que una publicación puede ser moderada por calidad de imágenes y cómo revisar el motivo para corregir las fotos. Recomienda validar antes de publicar con el diagnóstico de imágenes; también menciona la carga al CDN mediante `/pictures/items/upload`, sin documentar allí método ni detalles de esa operación.

## Contenido y conceptos documentados

Las moderaciones de imagen pueden aparecer con estado `active` o `paused` y tag `poor_quality_thumbnail`. La consulta devuelve el nombre de la moderación, ID, fecha, `REASON`, `REMEDY` y evidencia en la sección `pictures`. Los ejemplos muestran `WATERMARK` y `MULTIPLE`; las soluciones piden corregir problemas como marcas de agua, logos, iluminación o encuadre. La referencia se construye según la guía de moderaciones. Para subir imágenes al CDN, la fuente menciona `/pictures/items/upload`; el método, autenticación, parámetros y respuesta están No documentado en la fuente de esta página.

## Operaciones de API

## Conceptos y recursos asociados

### Moderaciones por calidad de imagen

Resume el tag, estados y ejemplos de problemas de imagen, y referencia la carga de imágenes al CDN.

**Respuesta**

No documentado en la fuente.

**Ejemplos documentados**

- La página menciona /pictures/items/upload pero no documenta su método ni sus parámetros.
## Operaciones de API

### Consultar moderación de imágenes

**Método:** `GET`  
**Ruta:** `/moderations/last_moderation/{moderation_reference_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene las moderaciones de calidad de imagen de un elemento y sus evidencias y textos de corrección.

**Parámetros**

- `moderation_reference_id` (path, obligatorio): Referencia del elemento; la página remite a Gestionar Moderaciones.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista con name, id, date_created, wordings (REASON/REMEDY) y evidence.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Los ejemplos muestran WATERMARK y MULTIPLE.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/moderaciones-de-imagenes](https://developers.mercadolibre.com.co/es_co/moderaciones-de-imagenes)  
**Captura:** 2026-10-08T22:53:53.123Z

---

## [Notificaciones](../markdown/productos-recibe-notificaciones.md)

Actualización indicada por la fuente: 14/09/2026. Captura: 2026-10-08T22:53:54.597Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/productos-recibe-notificaciones](https://developers.mercadolibre.com.co/es_co/productos-recibe-notificaciones)

# Notificaciones

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 14/09/2026  
**Captura:** 2026-10-08T22:53:54.597Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/productos-recibe-notificaciones](https://developers.mercadolibre.com.co/es_co/productos-recibe-notificaciones)

## Resumen

Las notificaciones entregan eventos en tiempo real de cambios de recursos, evitando consultar la API de forma periódica. La integración configura en DevCenter la URL callback y los tópicos; recibe un POST en esa URL y luego consulta el recurso indicado para obtener sus datos completos. La documentación cubre topics generales y subtemas, varios recursos de ventas, publicaciones, envíos, créditos y posventa, y recuperación de notificaciones perdidas.

## Contenido y conceptos documentados

### Configuración y entrega

La URL callback debe ser pública y recibir los tópicos elegidos. Las notificaciones usan UTC; `payments` y `messages` no aplican a inmuebles, servicios ni automóviles. El payload general incluye `_id`, `resource`, `user_id`, `topic`, `application_id`, `attempts`, `sent` y `received`; los topics tipificados agregan `actions`. La aplicación debe confirmar con HTTP 200 en un máximo de 500 ms. Si no se acepta, hay reintentos durante una hora; la fuente recomienda confirmar rápidamente y procesar después con una cola.

### Recuperación y consulta de eventos

Cada evento debe verificarse consultando el recurso de `resource`; puede reflejar cambios originados en otras superficies o integraciones. `missed_feeds` conserva hasta dos días las notificaciones que no recibieron 200 tras los intentos de entrega. Para `items`, la consulta requiere `site_id`; pueden usarse filtros de tema y paginación. El ejemplo indica 10 resultados por defecto.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /stock/fulfillment/operations

La fuente menciona la ruta /stock/fulfillment/operations, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/stock/fulfillment/operations`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /stock/fulfillment/operations/9876

La fuente menciona la ruta /stock/fulfillment/operations/9876, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/stock/fulfillment/operations/9876`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /vis/loan/66e93589-2d10-11ed-ae7f-0aa30fafa621

La fuente menciona la ruta /vis/loan/66e93589-2d10-11ed-ae7f-0aa30fafa621, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/vis/loan/66e93589-2d10-11ed-ae7f-0aa30fafa621`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /leads/{LEAD_ID}/details

La fuente menciona la ruta /leads/{LEAD_ID}/details, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/leads/{LEAD_ID}/details`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /post-purchase

La fuente menciona la ruta /post-purchase, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/post-purchase`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /sites/{SITE_ID}/user-products-families/{FAMILY_ID}

La fuente menciona la ruta /sites/{SITE_ID}/user-products-families/{FAMILY_ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/sites/{SITE_ID}/user-products-families/{FAMILY_ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Entrega de notificaciones por callback

Describe configuración del callback, estructura de notificación, tópicos y política de reintentos antes de consultar el recurso informado.

**Solicitud**

El callback recibe HTTP POST en una URL pública configurada por la integración; se recomienda responder HTTP 200 en 500 ms.

**Respuesta**

Payload general con _id, resource, user_id, topic, application_id, attempts, sent y received; los topics tipificados pueden incluir actions.

**Ejemplos documentados**

- Reintentos durante una hora; missed_feeds conserva notificaciones perdidas hasta 2 días.
## Operaciones de API

### Consultar asignación de envío Flex

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/shipments/{shipment_id}/assignment/v1`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene información de la asignación Flex para el envío.

**Parámetros**

- `site_id` (path, obligatorio): ID del sitio.
- `shipment_id` (path, obligatorio): ID del envío.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar candidato a promoción

**Método:** `GET`  
**Ruta:** `/seller-promotions/candidates/{candidate_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalles de un candidato a promoción del vendedor.

**Parámetros**

- `candidate_id` (path, obligatorio): ID del candidato.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar sugerencia de catálogo

**Método:** `GET`  
**Ruta:** `/catalog_suggestions/{suggestion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene una sugerencia de catálogo.

**Parámetros**

- `suggestion_id` (path, obligatorio): ID de sugerencia.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar collection de pago

**Método:** `GET`  
**Ruta:** `/collections/{payment_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los detalles de la collection/pago notificada.

**Parámetros**

- `payment_id` (path, obligatorio): ID del pago.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar factura de usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/invoices/{invoice_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los detalles de una factura del usuario.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.
- `invoice_id` (path, obligatorio): ID de factura.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar familia de User Products

**Método:** `GET`  
**Ruta:** `/user-products-families/{family_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene una familia del recurso User Products.

**Parámetros**

- `family_id` (path, obligatorio): ID de la familia.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar ítem notificado

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los detalles del ítem asociado a la notificación.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Respuesta de ejemplo con id, title, price, currency_id, available_quantity, sold_quantity y status.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Listar leads VIS de usuario

**Método:** `GET`  
**Ruta:** `/vis/users/{user_id}/leads`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta los leads VIS del usuario asociado a la notificación.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar recurso de mensajes

**Método:** `GET`  
**Ruta:** `/messages/{resource}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el recurso de mensajes indicado por la notificación.

**Parámetros**

- `resource` (path, obligatorio): Segmento de recurso recibido en la notificación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar notificaciones perdidas

**Método:** `GET`  
**Ruta:** `/missed_feeds`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera eventos fallidos conservados en missed_feeds; admite filtros y paginación.

**Parámetros**

- `app_id` (query, obligatorio): ID de aplicación.
- `topic` (query, opcional): Filtro por tópico.
- `site_id` (query): Obligatorio al consultar topic=items; otros tópicos no lo requieren.
- `offset` (query, opcional): Desplazamiento para paginación.
- `limit` (query, opcional): Límite de resultados; por defecto 10.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto con messages; registros de ejemplo incluyen resource, user_id, topic, application_id, attempts, sent/received, request y response.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "La consulta de notificaciones perdidas para topic=items sin site_id devuelve HTTP 400." } ```

**Ejemplos**

- Conserva notificaciones perdidas hasta dos días.

### Consultar oferta de vendedor

**Método:** `GET`  
**Ruta:** `/seller-promotions/offers/{offers_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalles de una oferta de seller promotions.

**Parámetros**

- `offers_id` (path, obligatorio): ID de oferta.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar orden desde notificación

**Método:** `GET`  
**Ruta:** `/orders/{order_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los detalles del pedido indicado por el evento.

**Parámetros**

- `order_id` (path, obligatorio): ID de orden.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La guía indica consultar el resource recibido.

### Consultar crédito VIS

**Método:** `GET`  
**Ruta:** `/vis/loans/{credit_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los detalles de un préstamo/crédito VIS para el vendedor.

**Parámetros**

- `credit_id` (path, obligatorio): ID del crédito.
- `seller_id` (query, obligatorio): ID del vendedor.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar price-to-win

**Método:** `GET`  
**Ruta:** `/items/{item_id}/price_to_win`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el recurso price-to-win del ítem.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar pregunta

**Método:** `GET`  
**Ruta:** `/questions/{question_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene la pregunta indicada en la notificación.

**Parámetros**

- `question_id` (path, obligatorio): ID de la pregunta.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar recurso indicado en notificación

**Método:** `GET`  
**Ruta:** `/{resource}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene la ruta del recurso enviada en resource; la página muestra ejemplos de fulfillment y post-compra.

**Parámetros**

- `resource` (path, obligatorio): Ruta recibida en el campo resource.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El path concreto depende del resource recibido.

### Referencia HTTP GET /stock/fulfillment/operations

**Método:** `GET`  
**Ruta:** `/stock/fulfillment/operations`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /stock/fulfillment/operations. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Consultar precio de venta

**Método:** `GET`  
**Ruta:** `/items/{item_id}/sale_price`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el precio del ítem para el contexto indicado.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.
- `context` (query, obligatorio): Contexto del precio indicado en la notificación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar envío

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el detalle del envío notificado.

**Parámetros**

- `shipment_id` (path, obligatorio): ID del envío.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar stock de User Product

**Método:** `GET`  
**Ruta:** `/user-products/{user_product_id}/stock`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene stock de un producto de usuario.

**Parámetros**

- `user_product_id` (path, obligatorio): ID del User Product.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar detalles de sugerencias de ítem

**Método:** `GET`  
**Ruta:** `/suggestions/items/{item_id}/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalles de sugerencias relacionadas con un ítem.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar User Product

**Método:** `GET`  
**Ruta:** `/user_products/{up_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el User Product señalado por la notificación.

**Parámetros**

- `up_id` (path, obligatorio): ID del User Product.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar lead VIS

**Método:** `GET`  
**Ruta:** `/vis/leads/{lead_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el lead indicado por una notificación VIS.

**Parámetros**

- `lead_id` (path, obligatorio): ID del lead.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/productos-recibe-notificaciones](https://developers.mercadolibre.com.co/es_co/productos-recibe-notificaciones)  
**Captura:** 2026-10-08T22:53:54.597Z

---

## [Pedidos y opiniones](../markdown/pedidos-y-opiniones.md)

Actualización indicada por la fuente: 05/06/2025. Captura: 2026-10-08T22:53:57.179Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/pedidos-y-opiniones](https://developers.mercadolibre.com.co/es_co/pedidos-y-opiniones)

# Pedidos y opiniones

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 05/06/2025  
**Captura:** 2026-10-08T22:53:57.179Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/pedidos-y-opiniones](https://developers.mercadolibre.com.co/es_co/pedidos-y-opiniones)

## Resumen

Agrupa ejemplos para consultar órdenes, métodos de pago y opiniones; también incluye bloqueo de compradores e información de productos vendidos.

## Contenido y conceptos documentados

- /orders/search se muestra para búsquedas por seller y buyer. Las respuestas de ejemplo incluyen paging, datos de la orden, pagos, publicaciones, feedback y envío.
- Las opiniones de orden pueden consultarse, crearse y modificarse; el vendedor puede responder mediante el recurso de reply.
- Los métodos de pago se consultan por site y luego por ID; la respuesta de detalle contiene costos, emisores, acreditación y opciones de cuotas.
- Para pedidos, el endpoint block-api filtra type=blocked_by_order con offset/limit; order_blacklist ofrece paginación por usuario.

## Operaciones de API
## Operaciones de API

### Consultar compradores bloqueados por pedidos

**Método:** `GET`  
**Ruta:** `/block-api/search/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista bloqueos relacionados con órdenes.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario consultado.
- `type` (query, obligatorio): blocked_by_order.
- `offset` (query, opcional): Por defecto 0.
- `limit` (query, opcional): Por defecto 10; máximo 1000.

**Solicitud**

No documentado en la fuente.

**Respuesta**

users con id y blocked_at; paging con offset, limit y total.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET con type=blocked_by_order.

### Consultar opiniones de una orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}/feedback`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene opiniones de comprador/vendedor asociadas a una orden.

**Parámetros**

- `order_id` (path, obligatorio): ID de orden.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto sale/purchase con from, to, status, reason, date_created, order_id, id, message, fulfilled, item, rating y otros datos de feedback.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /orders/1068825849/feedback.

### Consultar atributos de productos de una orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}/product`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene información específica del producto vendido dentro de la orden.

**Parámetros**

- `order_id` (path, obligatorio): ID de orden.

**Solicitud**

No documentado en la fuente.

**Respuesta**

attributes es una lista de name, value e id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo incluye IMEI y entry_date.

### Buscar órdenes de vendedor o comprador

**Método:** `GET`  
**Ruta:** `/orders/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca órdenes asociadas al seller o buyer indicado.

**Parámetros**

- `seller` (query): ID del vendedor; ejemplo de búsqueda.
- `buyer` (query): ID del comprador; ejemplo de búsqueda.

**Solicitud**

No documentado en la fuente.

**Respuesta**

La respuesta de ejemplo contiene query, display, paging y results con órdenes, ítems, pagos, buyer/seller, envío y feedback.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /orders/search?seller=... y GET /orders/search?buyer=....

### Listar métodos de pago por sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/payment_methods`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve los métodos de pago previstos por Mercado Pago para un site.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de id, name, payment_type_id, thumbnail y secure_thumbnail.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/payment_methods.

### Consultar método de pago

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/payment_methods/{payment_method_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el detalle de un método de pago de un site.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.
- `payment_method_id` (path, obligatorio): ID del método de pago.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, payment_type_id, card_issuer, site_id, imágenes, labels, costos financieros, plazos y payer_costs.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/payment_methods/amex.

### Consultar lista de usuarios bloqueados por órdenes

**Método:** `GET`  
**Ruta:** `/users/{user_id}/order_blacklist`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve los usuarios en la lista de bloqueo del usuario y permite paginación.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario.
- `offset` (query, opcional): Desplazamiento de paginación.
- `limit` (query, opcional): Cantidad por página.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de usuarios bloqueados; la estructura de respuesta completa no se detalla en el fragmento capturado.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/:userID/order_blacklist?offset=100&limit=50.

### Responder a opinión

**Método:** `POST`  
**Ruta:** `/feedback/{feedback_id}/reply`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Publica la respuesta de un vendedor a una opinión.

**Parámetros**

- `feedback_id` (path, obligatorio): ID de feedback.
- `Content-Type` (header, obligatorio): application/json.

**Solicitud**

JSON con reply.

**Respuesta**

Devuelve el feedback, reply_status, reply_date, visibility_date y reply.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- POST /feedback/{feedback_id}/reply con reply.

### Crear opinión de una orden

**Método:** `POST`  
**Ruta:** `/orders/{order_id}/feedback`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Envía una opinión relacionada con la compra o venta de la orden.

**Parámetros**

- `order_id` (path, obligatorio): ID de orden.
- `Content-Type` (header, obligatorio): application/json.

**Solicitud**

JSON de ejemplo con fulfilled, rating, message, reason, restock_item y has_seller_refunded_money.

**Respuesta**

La respuesta de ejemplo devuelve datos de la opinión, su estado, rating, message, order_id y participantes.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- POST /orders/1068825849/feedback.

### Modificar opinión

**Método:** `PUT`  
**Ruta:** `/feedback/{feedback_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza campos de una opinión existente.

**Parámetros**

- `feedback_id` (path, obligatorio): ID de feedback.
- `Content-Type` (header, obligatorio): application/json.

**Solicitud**

JSON de ejemplo con fulfilled, rating y message.

**Respuesta**

La respuesta muestra status, reason, site_id, date_created, cust_role, order_id, id, message, fulfilled, reply, cust_to y rating.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- PUT /feedback/{feedback_id}.

### Referencia HTTP GET /{SITE_ID}/payment_methods/{id}

**Método:** `GET`  
**Ruta:** `/{SITE_ID}/payment_methods/{id}`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /{SITE_ID}/payment_methods/{id}. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /sites/MLA/payment_methods/amex

**Método:** `GET`  
**Ruta:** `/sites/MLA/payment_methods/amex`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /sites/MLA/payment_methods/amex. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /users/{userID}/order_blacklist

**Método:** `GET`  
**Ruta:** `/users/{userID}/order_blacklist`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/{userID}/order_blacklist. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

- `offset` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.
- `limit` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

### Referencia HTTP GET /api.mercadopago.com/v1/payments/{PAYMENT_ID}

**Método:** `GET`  
**Ruta:** `/api.mercadopago.com/v1/payments/{PAYMENT_ID}`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /api.mercadopago.com/v1/payments/{PAYMENT_ID}. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/pedidos-y-opiniones](https://developers.mercadolibre.com.co/es_co/pedidos-y-opiniones)  
**Captura:** 2026-10-08T22:53:57.179Z

---

## [Preguntas frecuentes sobre validación de datos](../markdown/validacion-de-datos.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:53:58.238Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/validacion-de-datos](https://developers.mercadolibre.com.co/es_co/validacion-de-datos)

# Preguntas frecuentes sobre validación de datos

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:58.238Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/validacion-de-datos](https://developers.mercadolibre.com.co/es_co/validacion-de-datos)

## Resumen

Describe el proceso de verificación de identidad y regularización de datos de cuentas de Mercado Libre.

## Contenido y conceptos documentados

- La validación aplica a compradores, vendedores e integradores; el titular o representante legal debe realizarla. Puede solicitarse al crear la cuenta o al revalidar por cambios de perfil, titularidad o actividad.
- En cuentas de empresa se validan tanto la persona jurídica como la persona que la representa. La información de beneficiarios finales varía por país según la guía.
- El proceso puede tardar hasta 72 horas. Si los datos no se regularizan, la fuente indica que vendedores pueden perder publicaciones activas y permisos para nuevas autorizaciones; integradores pueden dejar de recibir autorizaciones de nuevos vendedores.

## Operaciones de API

## Conceptos y recursos asociados

### Flujo de validación de identidad de cuenta

La validación comprueba la identidad de compradores, vendedores e integradores; la realiza el titular de la cuenta o representante legal. Aplica al crear una cuenta y cuando el perfil o las actividades requieren revalidación. La captura no documenta endpoint HTTP.

**Ejemplos documentados**

- La fuente indica que la validación puede demorar hasta 72 horas.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/validacion-de-datos](https://developers.mercadolibre.com.co/es_co/validacion-de-datos)  
**Captura:** 2026-10-08T22:53:58.238Z

---

## [Preguntas y Respuestas](../markdown/preguntas-y-respuestas.md)

Actualización indicada por la fuente: 05/06/2025. Captura: 2026-10-08T22:53:59.153Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/preguntas-y-respuestas](https://developers.mercadolibre.com.co/es_co/preguntas-y-respuestas)

# Preguntas y Respuestas

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 05/06/2025  
**Captura:** 2026-10-08T22:53:59.153Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/preguntas-y-respuestas](https://developers.mercadolibre.com.co/es_co/preguntas-y-respuestas)

## Resumen

Documenta cómo buscar preguntas por ítem, consultar una pregunta, responderla y gestionar bloqueos de compradores.

## Contenido y conceptos documentados

- Para la nueva estructura, la página recomienda api_version=4. El ejemplo de búsqueda devuelve filtros y estados de pregunta como ANSWERED, UNANSWERED, CLOSED_UNANSWERED, DELETED y UNDER_REVIEW.
- Una pregunta se crea con text e item_id; una respuesta usa question_id y text.
- El endpoint de bloqueos admite type=blocked_by_questions, con paginación offset/limit; /users/{seller_id}/questions_blacklist/{user_id} quita un usuario bloqueado.
- No se documentan códigos de error específicos en esta página.

## Operaciones de API
## Operaciones de API

### Quitar usuario de lista de bloqueo de preguntas

**Método:** `DELETE`  
**Ruta:** `/users/{seller_id}/questions_blacklist/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina el usuario indicado de la lista de bloqueo del vendedor.

**Parámetros**

- `seller_id` (path, obligatorio): ID del vendedor.
- `user_id` (path, obligatorio): ID del usuario a desbloquear.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- DELETE /users/{seller_id}/questions_blacklist/{user_id}.

### Consultar bloqueos por preguntas

**Método:** `GET`  
**Ruta:** `/block-api/search/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta compradores bloqueados en el contexto de preguntas.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario consultado.
- `type` (query, obligatorio): blocked_by_questions.
- `offset` (query, opcional): Paginación; ejemplos de la fuente muestran 0.
- `limit` (query, opcional): Paginación; el ejemplo usa 10.

**Solicitud**

No documentado en la fuente.

**Respuesta**

users con id y blocked_at; paging con offset, limit y total. Sin bloqueos devuelve users vacío y total 0.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET con type=blocked_by_questions.

### Consultar preguntas recibidas

**Método:** `GET`  
**Ruta:** `/my/received_questions/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve preguntas recibidas por el usuario autenticado.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con total, limit y questions; cada pregunta puede contener date_created, item_id, seller_id, status, text, id, deleted_from_listing, hold, answer y from.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /my/received_questions/search.

### Consultar pregunta

**Método:** `GET`  
**Ruta:** `/questions/{question_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el detalle de una pregunta por ID.

**Parámetros**

- `question_id` (path, obligatorio): ID de la pregunta.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, answer, date_created, deleted_from_listing, hold, item_id, seller_id, status, text y from.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /questions/3957150025.

### Buscar preguntas por ítem

**Método:** `GET`  
**Ruta:** `/questions/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta preguntas realizadas sobre los ítems de un usuario; la fuente recomienda api_version=4 para la nueva estructura.

**Parámetros**

- `item_id` (query, obligatorio): ID de ítem, como en el ejemplo.
- `api_version` (query, opcional): La nota de la página recomienda valor 4.

**Solicitud**

No documentado en la fuente.

**Respuesta**

total, limit, questions, filters, available_filters y available_sorts; la lista incluye estados posibles.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /questions/search?item_id=MLA608007087; api_version=4.

### Responder pregunta

**Método:** `POST`  
**Ruta:** `/answers`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Envía una respuesta a una pregunta recibida.

**Parámetros**

- `Content-Type` (header, obligatorio): application/json.

**Solicitud**

JSON con question_id y text.

**Respuesta**

Pregunta con id, answer (date_created, status, text), date_created, item_id, seller_id, status, text y from.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- POST /answers con question_id y text.

### Realizar pregunta

**Método:** `POST`  
**Ruta:** `/questions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una pregunta sobre un ítem de otro usuario.

**Parámetros**

- `Content-Type` (header, obligatorio): application/json.

**Solicitud**

JSON con text e item_id.

**Respuesta**

id, answer, date_created, item_id, seller_id, status, text y from.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- POST /questions con text e item_id.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/preguntas-y-respuestas](https://developers.mercadolibre.com.co/es_co/preguntas-y-respuestas)  
**Captura:** 2026-10-08T22:53:59.153Z

---

## [Publicaciones denunciadas](../markdown/publicaciones-denunciadas.md)

Actualización indicada por la fuente: 26/07/2026. Captura: 2026-10-08T22:54:00.163Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/publicaciones-denunciadas](https://developers.mercadolibre.com.co/es_co/publicaciones-denunciadas)

# Publicaciones denunciadas

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 26/07/2026  
**Captura:** 2026-10-08T22:54:00.163Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/publicaciones-denunciadas](https://developers.mercadolibre.com.co/es_co/publicaciones-denunciadas)

## Resumen

Describe consultas y respuestas a denuncias de propiedad intelectual asociadas a publicaciones y vendedores.

## Contenido y conceptos documentados

- GET de casos filtra por offset, fecha y estado; la tabla llama current_status al campo, aunque los ejemplos usan query status. El detalle muestra item_info, reason_id, due_date, documentos e imágenes denunciadas; is_rollbackable solo es true en ciertos estados.
- Para adjuntar evidencia, se acepta PDF, JPG o PNG de hasta 5 MB; file_name devuelto se usa como document_name en la respuesta.
- La respuesta puede incluir seller_quittance, document_name, photos_new/photos_removed y variations con picture_ids. La fuente distingue respuesta por derechos de imágenes, imágenes a reemplazar y documentación.
- Estados descritos incluyen CREATED, PENDING_MODERATION, WAITING_DOCUMENTATION, ROLLBACK, DOCUMENTATION_PRESENTED, WAITING_FOR_PATCH_PDP, DOCUMENTATION_APPROVED, DOCUMENTATION_NOT_APPROVED, DOCUMENTATION_NOT_PRESENTED, MEMBER_NOT_RESPOND y ACUERDO. Se enumeran motivos PPPI1 a PPPI23 con algunos códigos omitidos.

## Operaciones de API

## Conceptos y recursos asociados

### Estados y motivos de denuncias

La fuente lista estados y reason_id para tipos de infracción. El plazo due_date depende del caso; publicaciones pueden pausarse, reactivarse o eliminarse conforme a la respuesta y revisión.

**Ejemplos documentados**

- Reason IDs documentados incluyen PPPI1-PPPI23 con algunos saltos y ACUERDO; ejemplos de estados incluyen WAITING_DOCUMENTATION y DOCUMENTATION_APPROVED.
### Ruta mencionada /pictures

La fuente menciona la ruta /pictures, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/pictures`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar detalle de denuncia

**Método:** `GET`  
**Ruta:** `/moderations/pppi/case/{case_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene denuncia, ítem, documentos e imágenes asociadas a un caso.

**Parámetros**

- `case_id` (path, obligatorio): Identificador de denuncia.

**Solicitud**

No documentado en la fuente.

**Respuesta**

case_id, current_status, item_info, reason_id, public_member_name, date_created, due_date, last_updated, is_rollbackable, documents, document_name/url, photos_denounced, photos_new, element_related_count, member_quittance, seller_quittance y user_product_ids.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /moderations/pppi/case/37168941.

### Consultar denuncias de publicaciones

**Método:** `GET`  
**Ruta:** `/moderations/pppi/cases`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista casos por vendedor, fecha y estado de la denuncia.

**Parámetros**

- `offset` (query, obligatorio): Paginación; máximo 50 resultados por página.
- `date_created` (query, obligatorio): Fecha inicial hasta la fecha actual; se puede enviar vacía según el ejemplo.
- `status` (query, obligatorio): Estado de denuncia; ejemplo DOCUMENTATION_APPROVED. La tabla de la fuente lo nombra current_status.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Array de casos con case_id, item_id, current_status, date_created, due_date, element_related_count, reason_text, user_product_ids; incluye total, offset y limit.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET con offset=0, date_created y status=DOCUMENTATION_APPROVED.

### Responder denuncia

**Método:** `POST`  
**Ruta:** `/moderations/pppi/case/{case_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Envía comentario, documento o cambios de imágenes para responder a un caso.

**Parámetros**

- `case_id` (path, obligatorio): ID de denuncia.

**Solicitud**

JSON de ejemplo con seller_quittance, document_name, photos_new, photos_removed y variations (id/picture_ids) cuando hay variantes. La documentación puede ser obligatoria u opcional según el tipo de denuncia.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos sin variantes, con variaciones y respuesta solo con documento.

### Cargar archivo probatorio

**Método:** `PUT`  
**Ruta:** `/moderations/pppi/case/files`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Sube archivo PDF, JPG o PNG como evidencia para responder una denuncia.

**Parámetros**

- `case_id` (query, obligatorio): ID de denuncia.
- `name` (query, obligatorio): Nombre del archivo.
- `form` (body, obligatorio): Archivo probatorio; máximo 5 MB.

**Solicitud**

Carga multipart del archivo en el campo descrito como form.

**Respuesta**

file_name para usar luego en document_name.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- PUT con case_id, name y archivo JPG.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/publicaciones-denunciadas](https://developers.mercadolibre.com.co/es_co/publicaciones-denunciadas)  
**Captura:** 2026-10-08T22:54:00.163Z

---

## [Ubicación y Monedas](../markdown/ubicacion-y-monedas.md)

Actualización indicada por la fuente: 27/03/2025. Captura: 2026-10-08T22:54:01.179Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/ubicacion-y-monedas](https://developers.mercadolibre.com.co/es_co/ubicacion-y-monedas)

# Ubicación y Monedas

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 27/03/2025  
**Captura:** 2026-10-08T22:54:01.179Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/ubicacion-y-monedas](https://developers.mercadolibre.com.co/es_co/ubicacion-y-monedas)

## Resumen

Agrupa consultas de países, estados, ciudades, códigos postales y monedas disponibles en Mercado Libre.

## Contenido y conceptos documentados

- Los recursos classified_locations permiten recorrer país, estado y ciudad; el ejemplo de país incluye locale, currency_id, separadores y zona horaria.
- La conversión usa from y to y devuelve rate, inv_rate y creation_date; el ejemplo usa el header x-format-new=true.
- La fuente advierte que Chile, Ecuador y Perú no tienen códigos postales locales disponibles por esta API. Para México indica mantener la guía actual de carga de MXN, aunque en ciertos flujos se muestre el símbolo MXN.

## Operaciones de API
## Operaciones de API

### Consultar ciudad

**Método:** `GET`  
**Ruta:** `/classified_locations/cities/{city_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene datos de una ciudad y sus referencias geográficas.

**Parámetros**

- `city_id` (path, obligatorio): ID de ciudad.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, state, country y geo_information.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /classified_locations/cities/TUxVQ0NBQjY1MmQ1.

### Listar países de ubicaciones clasificadas

**Método:** `GET`  
**Ruta:** `/classified_locations/countries`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista los países y sus configuraciones regionales y monedas.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Array de id, name, locale y currency_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Incluye CO con es_CO y COP.

### Consultar país

**Método:** `GET`  
**Ruta:** `/classified_locations/countries/{country_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene datos de un país, separadores, zona horaria y estados.

**Parámetros**

- `country_id` (path, obligatorio): ID de país.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, locale, currency_id, decimal_separator, thousands_separator, time_zone, geo_information y states.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /classified_locations/countries/UY.

### Consultar estado/provincia

**Método:** `GET`  
**Ruta:** `/classified_locations/states/{state_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene un estado y las ciudades asociadas.

**Parámetros**

- `state_id` (path, obligatorio): ID de estado.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, country, geo_information y cities.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /classified_locations/states/UY-RO.

### Consultar ubicación por código postal

**Método:** `GET`  
**Ruta:** `/countries/{country_id}/zip_codes/{zip_code}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca ubicación asociada a un código postal de país.

**Parámetros**

- `country_id` (path, obligatorio): ID de país.
- `zip_code` (path, obligatorio): Código postal.

**Solicitud**

No documentado en la fuente.

**Respuesta**

zip_code, city, state y country.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /countries/AR/zip_codes/5000.

### Buscar intervalo de códigos postales

**Método:** `GET`  
**Ruta:** `/country/{country_id}/zip_codes/search_between`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene información postal entre dos códigos para un país.

**Parámetros**

- `country_id` (path, obligatorio): ID de país.
- `zip_code_from` (query, obligatorio): Código postal inicial.
- `zip_code_to` (query, obligatorio): Código postal final.

**Solicitud**

No documentado en la fuente.

**Respuesta**

zip_code, city, state, country y extended_attributes.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /country/AR/zip_codes/search_between?zip_code_from=5000&zip_code_to=5100.

### Listar monedas

**Método:** `GET`  
**Ruta:** `/currencies/`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista monedas disponibles con descripción, símbolo y decimales.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Array de id, description, symbol y decimal_places.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /currencies/.

### Consultar moneda

**Método:** `GET`  
**Ruta:** `/currencies/{currency_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalle de una moneda.

**Parámetros**

- `currency_id` (path, obligatorio): Código de moneda.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, description, symbol y decimal_places.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /currencies/CLP.

### Consultar conversión de monedas

**Método:** `GET`  
**Ruta:** `/currency_conversions/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene tasa de cambio y fecha para el par solicitado.

**Parámetros**

- `from` (query, obligatorio): Código de moneda de origen.
- `to` (query, obligatorio): Código de moneda destino.
- `x-format-new` (header): El ejemplo usa true para el formato nuevo.

**Solicitud**

No documentado en la fuente.

**Respuesta**

currency_base, currency_quote, rate, inv_rate y creation_date.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /currency_conversions/search?from=ARS&to=CLP con x-format-new:true.

### Referencia HTTP GET /classified_locations/states/UY-RO

**Método:** `GET`  
**Ruta:** `/classified_locations/states/UY-RO`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /classified_locations/states/UY-RO. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /currencies/CLP

**Método:** `GET`  
**Ruta:** `/currencies/CLP`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /currencies/CLP. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /classified_locations/countries/UY

**Método:** `GET`  
**Ruta:** `/classified_locations/countries/UY`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /classified_locations/countries/UY. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /countries/AR/zip_codes/5000

**Método:** `GET`  
**Ruta:** `/countries/AR/zip_codes/5000`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /countries/AR/zip_codes/5000. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /country/AR/zip_codes/search_between

**Método:** `GET`  
**Ruta:** `/country/AR/zip_codes/search_between`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /country/AR/zip_codes/search_between. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

- `zip_code_from` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.
- `zip_code_to` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/ubicacion-y-monedas](https://developers.mercadolibre.com.co/es_co/ubicacion-y-monedas)  
**Captura:** 2026-10-08T22:54:01.179Z

---

## [Usuarios y Aplicaciones](../markdown/usuarios-y-aplicaciones.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:54:02.190Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/usuarios-y-aplicaciones](https://developers.mercadolibre.com.co/es_co/usuarios-y-aplicaciones)

# Usuarios y Aplicaciones

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:54:02.190Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/usuarios-y-aplicaciones](https://developers.mercadolibre.com.co/es_co/usuarios-y-aplicaciones)

## Resumen

Documenta recursos para consultar y actualizar usuarios, direcciones, métodos de pago, marcas, tipos de publicación, aplicaciones y notificaciones.

## Contenido y conceptos documentados

- /users/{user_id} incluye perfil, contacto, estado y reputación; /users/me devuelve información del usuario autenticado y /addresses detalla direcciones.
- Los métodos aceptados por un usuario se consultan separadamente. Las marcas pueden incluir official_store_id; los paquetes y recursos available_listing_types describen disponibilidad de tipos promocionales por usuario/categoría.
- También se consultan detalles de aplicación, se revocan permisos y se recupera missed_feeds por app_id. La tabla de recursos incluye GET y POST para paquetes promocionales, pero solo detalla una consulta GET.

## Operaciones de API
## Operaciones de API

### Revocar permisos de aplicación

**Método:** `DELETE`  
**Ruta:** `/users/{user_id}/applications/{application_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Revoca permisos otorgados por el usuario a una aplicación.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario/cust_id.
- `application_id` (path, obligatorio): ID de aplicación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- DELETE /users/{cust_Id}/applications/{app_id}.

### Consultar aplicación

**Método:** `GET`  
**Ruta:** `/applications/{application_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve datos de una aplicación registrada.

**Parámetros**

- `application_id` (path, obligatorio): ID de la aplicación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo incluye id, site_id, name, description, owner_id, need_authorization, short_name, url, callback_url, sandbox_mode, is_public, active, max_requests_per_hour, scopes y domains.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /applications/3022782903258037.

### Consultar notificaciones no recibidas

**Método:** `GET`  
**Ruta:** `/missed_feeds`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el histórico de notificaciones perdidas para una aplicación.

**Parámetros**

- `app_id` (query, obligatorio): ID de aplicación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /missed_feeds?app_id=$APP_ID.

### Consultar usuario autenticado

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve información asociada al usuario conectado a la cuenta.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo de dirección asociada con user_id, contact, phone, address_line, street_number/name, zip_code, city, state, country y otros datos.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/me.

### Consultar usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve el perfil, datos de contacto, dirección, reputación y estado del usuario.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con id, nickname, datos personales, país, email/teléfono, address, user_type, tags, seller_reputation, buyer_reputation, status y credit.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/{User_id}.

### Consultar métodos de pago aceptados por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/accepted_payment_methods`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista métodos de pago aceptados por el vendedor.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Métodos con id, name, payment_type_id, thumbnail y secure_thumbnail.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/206946886/accepted_payment_methods.

### Consultar direcciones de usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/addresses`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve direcciones asociadas al usuario.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con id, user_id, contact, phone, address_line, street_number/name, zip_code, city, state, country y open_hours.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/206946886/addresses.

### Consultar tipo de publicación para categoría

**Método:** `GET`  
**Ruta:** `/users/{user_id}/available_listing_type/{listing_type_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Determina si un tipo de listado está disponible en una categoría para el usuario.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario.
- `listing_type_id` (path, obligatorio): Tipo de publicación.
- `category_id` (query, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

available, cause, code y mapping.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/206946886/available_listing_type/gold_special?category_id=MLA6602.

### Consultar tipos de publicación disponibles

**Método:** `GET`  
**Ruta:** `/users/{user_id}/available_listing_types`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve tipos de publicación disponibles para usuario y, según categoría, sus excepciones.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario.
- `category_id` (query, opcional): La tabla indica filtro por categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

available y exceptions_by_category; cada tipo incluye site_id, id, name, remaining_listings y mapping.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/206946886/available_listing_types.

### Consultar marcas de usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/brands`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera marcas vinculadas a un usuario; official_store_id identifica tienda.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo contiene cust_id, tags y brands con name, status, site_id, categories_ids, official_store_id, tags y pictures.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/12345678/brands.

### Listar paquetes de promoción del usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/classifieds_promotion_packs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta paquetes promocionales asociados al usuario.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo con id, user_id, promotion_pack_id, category_id, description, package_type, status y fechas.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/135146148/classifieds_promotion_packs.

### Consultar paquete habilitado por tipo y categoría

**Método:** `GET`  
**Ruta:** `/users/{user_id}/classifieds_promotion_packs/{listing_type_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Indica si un usuario tiene publicaciones disponibles para un tipo de listado y categoría.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.
- `listing_type_id` (path, obligatorio): Tipo de listado.
- `categoryId` (query, obligatorio): ID de categoría; la captura usa camelCase.

**Solicitud**

No documentado en la fuente.

**Respuesta**

has_available_listings boolean.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/206946886/classifieds_promotion_packs/silver?categoryId=MLA1459.

### Operación POST de paquetes promocionales

**Método:** `POST`  
**Ruta:** `/users/{user_id}/classifieds_promotion_packs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La tabla de recursos también enumera POST para classifieds_promotion_packs, pero la captura no especifica su cuerpo ni comportamiento.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El recurso aparece con métodos GET y POST; el ejemplo detallado de la captura es GET.

### Actualizar usuario

**Método:** `PUT`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza datos del usuario, incluidos dirección, teléfono y datos personales/empresariales ilustrados en la fuente.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.
- `Content-Type` (header, obligatorio): application/json.

**Solicitud**

Ejemplo JSON con address, state, city, zip_dode (tal como aparece escrito en la captura), phone, first_name, last_name, company y mercadoenvios.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- PUT /users/123456789 con campos de perfil.

### Referencia HTTP GET /users/206946886/available_listing_type/gold_special

**Método:** `GET`  
**Ruta:** `/users/206946886/available_listing_type/gold_special`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/206946886/available_listing_type/gold_special. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

- `category_id` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

### Referencia HTTP GET /users/206946886/classifieds_promotion_packs/silver

**Método:** `GET`  
**Ruta:** `/users/206946886/classifieds_promotion_packs/silver`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/206946886/classifieds_promotion_packs/silver. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

- `categoryId` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/usuarios-y-aplicaciones](https://developers.mercadolibre.com.co/es_co/usuarios-y-aplicaciones)  
**Captura:** 2026-10-08T22:54:02.190Z

---

## [Validar datos de vendedores](../markdown/validar-datos-de-vendedores.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:54:03.236Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/validar-datos-de-vendedores](https://developers.mercadolibre.com.co/es_co/validar-datos-de-vendedores)

# Validar datos de vendedores

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:54:03.236Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/validar-datos-de-vendedores](https://developers.mercadolibre.com.co/es_co/validar-datos-de-vendedores)

## Resumen

Permite que integradores revisen si un vendedor tiene la cuenta habilitada y los datos completos para vender, recibir pagos o usar la tarjeta prepaga.

## Contenido y conceptos documentados

- GET /users/{user_id}?attributes=status permite observar permisos de operación, códigos de bloqueo y acciones requeridas.
- La fuente recomienda que la validación la realice la persona titular o el representante legal y dice que puede tardar hasta tres días hábiles. En el ejemplo, list.allow=false y rejected_by_regulations señalan que faltan datos regulatorios.

## Operaciones de API
## Operaciones de API

### Consultar estado regulatorio de vendedor

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el estado del usuario para identificar permisos de venta, cobro y acciones regulatorias pendientes.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.
- `attributes` (query, obligatorio): El ejemplo filtra la respuesta a status.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto status con billing, buy, sell, required_action, site_status, mercado_pago, permisos list/immediate_payment y códigos asociados.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/123456789?attributes=status.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/validar-datos-de-vendedores](https://developers.mercadolibre.com.co/es_co/validar-datos-de-vendedores)  
**Captura:** 2026-10-08T22:54:03.236Z

---

## [¿Qué es Brand Protection Program?](../markdown/que-es-brand-protection-program.md)

Actualización indicada por la fuente: 15/03/2023. Captura: 2026-10-08T22:53:38.771Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/que-es-brand-protection-program](https://developers.mercadolibre.com.co/es_co/que-es-brand-protection-program)

# ¿Qué es Brand Protection Program?

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 15/03/2023  
**Captura:** 2026-10-08T22:53:38.771Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/que-es-brand-protection-program](https://developers.mercadolibre.com.co/es_co/que-es-brand-protection-program)

## Resumen

Presenta el programa para proteger marcas, obras y otras creaciones, y el flujo de denuncia y respuesta de vendedores.

## Contenido y conceptos documentados

- Los titulares pueden denunciar publicaciones; Mercado Libre avisa al vendedor y puede pausar el anuncio mientras responde.
- El vendedor puede aportar facturas o autorización del titular; en denuncias de imágenes, puede corregirlas y enviar imágenes nuevas. La página indica cuatro días para responder y cuatro días para que el titular revise.
- Si el titular acepta o no responde dentro del plazo, la publicación puede reactivarse; si rechaza por motivos válidos o el vendedor no responde a tiempo, puede darse de baja. La decisión final corresponde al miembro y no a Mercado Libre.

## Operaciones de API

## Conceptos y recursos asociados

### Flujo del Brand Protection Program

Programa para que titulares de derechos denuncien posibles infracciones de propiedad intelectual en publicaciones. El vendedor puede responder con pruebas o corregir imágenes; si no responde dentro del plazo indicado, la publicación puede darse de baja. La página no define rutas HTTP.

**Ejemplos documentados**

- El flujo describe inscripción, denuncia, respuesta del vendedor y revisión del titular; la fuente menciona plazos de cuatro días.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/que-es-brand-protection-program](https://developers.mercadolibre.com.co/es_co/que-es-brand-protection-program)  
**Captura:** 2026-10-08T22:53:38.771Z

---

## [Ítems y Búsquedas](../markdown/items-y-busquedas.md)

Actualización indicada por la fuente: 10/09/2026. Captura: 2026-10-08T22:53:49.815Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/items-y-busquedas](https://developers.mercadolibre.com.co/es_co/items-y-busquedas)

# Ítems y Búsquedas

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 10/09/2026  
**Captura:** 2026-10-08T22:53:49.815Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/items-y-busquedas](https://developers.mercadolibre.com.co/es_co/items-y-busquedas)

## Resumen

La página reúne búsquedas de publicaciones por sitio y por cuenta de vendedor, filtros y ordenamientos, consulta múltiple de ítems/usuarios y recorridos de más de 1.000 resultados. Distingue los ítems activos de los listados del sitio frente al inventario publicado en la cuenta del vendedor. Las consultas usan ejemplos con `Authorization: Bearer`; los multiget legacy están en migración a endpoints bulk.

## Contenido y conceptos documentados

- **Búsqueda por sitio y por vendedor:** `/sites/{site_id}/search` consulta publicaciones activas de los listados; `/users/{user_id}/items/search` obtiene las publicaciones de la cuenta. La primera admite filtros y `sort`; la segunda puede buscar por `sku` (`seller_custom_field`), `seller_sku`, estado, identificador de producto y tipo de publicación. La fuente desaconseja sustituir las notificaciones de ítems por búsquedas periódicas.
- **Exposición y restricciones:** `reputation_health_gauge` admite `unhealthy`, `warning` y `healthy` en México, Chile y Brasil. Vendedores con más de 200.000 ítems pueden tener `aggregations_allowed=false` y no recibir `filters`/`available_filters`; `include_filters=true` puede producir HTTP 206 en ese caso, mientras que sin el parámetro se documenta HTTP 200.
- **Recorridos grandes:** para superar 1.000 ítems o preguntas se usa `search_type=scan` (en preguntas, `searchtype=scan`) y se omite `offset`. El `scroll_id` se renueva por llamada, vence en cinco minutos y el recorrido termina cuando devuelve `null`; el ejemplo de ítems indica `limit` predeterminado de 50 y máximo de 100.
- **Multiget y migración:** las consultas legacy `/items?ids=` y `/users?ids=` aceptan hasta 20 resultados y responden en formato verbose (`code` y `body`). La página pide migrar antes del 25/10/2026 a `/items/bulk?ids=` y `/users/bulk?ids=`. En `/items/bulk`, el código pasa a `status_code`, se agrega `id` en la raíz y los atributos se seleccionan con prefijo `body.`; el método HTTP de estos reemplazos no se indica en esta página.
- **Cantidad disponible:** `available_quantity` en recursos públicos es referencial. La página mapea los rangos `RANGO_1_50`, `RANGO_51_100`, `RANGO_101_150`, `RANGO_151_200`, `RANGO_201_250`, `RANGO_251_500`, `RANGO_501_5000`, `RANGO_5001_50000` y `RANGO_50001_99999` a 1, 50, 100, 150, 200, 250, 500, 5.000 y 50.000, respectivamente.
- **Errores:** para multiget la fuente sugiere revisar 401 y 403, pero su significado es No documentado en la fuente. Otros parámetros, autenticación adicional y límites fuera de los descritos: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Disponibilidad pública referencial de available_quantity

En los recursos públicos de Ítems y Búsquedas, available_quantity se entrega como una referencia por rangos, no como cantidad exacta.

**Respuesta**

```json
{
  "field": "available_quantity",
  "reference_ranges": {
    "RANGO_1_50": 1,
    "RANGO_51_100": 50,
    "RANGO_101_150": 100,
    "RANGO_151_200": 150,
    "RANGO_201_250": 200,
    "RANGO_251_500": 250,
    "RANGO_501_5000": 500,
    "RANGO_5001_50000": 5000,
    "RANGO_50001_99999": 50000
  }
}
```
### Migración de multiget a bulk

Los endpoints legacy /items?ids= y /users?ids= conviven temporalmente con /items/bulk?ids= y /users/bulk?ids=. La fuente pide migrar antes del 25/10/2026 y señala que desde octubre de 2026 deben usarse los endpoints bulk. En /items/bulk, code pasa a status_code, id queda en el nivel raíz y attributes requiere prefijos body.; no documenta aquí el método HTTP de los reemplazos.

**Respuesta**

```json
{
  "legacy_to_replacement": {
    "/items?ids={ITEM_ID1},{ITEM_ID2}": "/items/bulk?ids={ITEM_ID1},{ITEM_ID2}",
    "/users?ids={USER_ID1},{USER_ID2}": "/users/bulk?ids={USER_ID1},{USER_ID2}"
  },
  "items_bulk_changes": [
    "code pasa a status_code",
    "id aparece en el nivel raíz",
    "los atributos seleccionados usan prefijo body."
  ],
  "migration_deadline": "25/10/2026"
}
```

**Ejemplos documentados**

- Método HTTP del reemplazo: No documentado en esta página.
### Ruta mencionada /items/bulk

La fuente menciona la ruta /items/bulk, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/items/bulk`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /sites/SITEID/search

La fuente menciona la ruta /sites/SITEID/search, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/sites/SITEID/search`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /users/bulk

La fuente menciona la ruta /users/bulk, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/users/bulk`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consulta múltiple de ítems (multiget legado)

**Método:** `GET`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene hasta 20 ítems en una llamada y devuelve una entrada verbose por cada consulta; este endpoint está en proceso de deprecación y la fuente indica migrar a /items/bulk.

**Parámetros**

- `ids` (query, obligatorio): Lista de IDs de ítems; la fuente documenta máximo 20 resultados por llamada.
- `attributes` (query, opcional): Selecciona atributos de ítems; el ejemplo usa id, price, category_id y title. La variante con attributes está deprecada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "shape": "Lista de resultados verbose, con code y body por ítem.",
  "sample_body_fields": [
    "id",
    "site_id",
    "title",
    "seller_id",
    "category_id",
    "price",
    "currency_id",
    "initial_quantity",
    "available_quantity",
    "sale_terms",
    "date_created",
    "last_updated",
    "health"
  ]
}
```

**Errores documentados**

- ```json {   "code": 401,   "meaning": "La fuente menciona revisar este código, pero no documenta su significado." } ```
- ```json {   "code": 403,   "meaning": "La fuente menciona revisar este código, pero no documenta su significado." } ```

**Ejemplos**

- GET /items?ids=MLA599260060,MLA594239600
- GET /items?ids=MLA599260060,MLA594239600&attributes=id,price,category_id,title

### Búsqueda de preguntas mediante scan

**Método:** `GET`  
**Ruta:** `/questions/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Permite recorrer preguntas de un ítem cuando se necesitan más de 1.000 registros; usa scan y paginación con scroll_id.

**Parámetros**

- `searchtype` (query, obligatorio): Usar scan para búsqueda de más de 1.000 preguntas.
- `item` (query, obligatorio): ID del ítem cuyas preguntas se consultan.
- `scroll_id` (query, opcional): Token de continuación: actualizar en cada llamada; expira en 5 minutos.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "documented_fields": [
    "scroll_id"
  ],
  "notes": [
    "La consulta se repite con el scroll_id actualizado hasta que la respuesta indique null."
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /questions/search?searchtype=scan&item=ITEM_ID

### Búsqueda de publicaciones del sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca publicaciones activas de los listados por vendedor o nickname; admite categoría, filtros y ordenamiento.

**Parámetros**

- `site_id` (path, obligatorio): Identificador del sitio.
- `seller_id` (query, opcional): ID del vendedor; ejemplo seller_id=$SELLER_ID.
- `nickname` (query, opcional): Nickname del vendedor.
- `category` (query, opcional): ID de categoría para acotar los resultados del vendedor.
- `shipping_cost` (query, opcional): El ejemplo usa free para filtrar publicaciones con envío gratis.
- `sort` (query, opcional): Orden disponible; ejemplo price_asc. La fuente indica que por defecto se usa relevancia.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "documented_fields": [
    "available_sorts",
    "available_filters"
  ],
  "notes": [
    "La fuente describe resultados de ítems activos de los listados."
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/SITE_ID/search?seller_id=$SELLER_ID
- GET /sites/SITE_ID/search?nickname=$NICKNAME&sort=price_asc
- GET /sites/SITE_ID/search?seller_id=$SELLER_ID&shipping_cost=free

### Consulta múltiple de usuarios (multiget legado)

**Método:** `GET`  
**Ruta:** `/users`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene hasta 20 usuarios en una llamada y devuelve una entrada verbose por usuario; la documentación indica migrar al reemplazo bulk.

**Parámetros**

- `ids` (query, obligatorio): Lista de IDs de usuarios; máximo documentado de 20 resultados por llamada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "shape": "Lista de resultados verbose, con code y body por usuario.",
  "sample_body_fields": [
    "id",
    "nickname",
    "registration_date",
    "country_id",
    "address",
    "user_type",
    "tags",
    "logo",
    "points",
    "site_id",
    "permalink",
    "seller_reputation",
    "buyer_reputation",
    "status"
  ]
}
```

**Errores documentados**

- ```json {   "code": 401,   "meaning": "La fuente menciona revisar este código, pero no documenta su significado." } ```
- ```json {   "code": 403,   "meaning": "La fuente menciona revisar este código, pero no documenta su significado." } ```

**Ejemplos**

- GET /users?ids=401114259,287440999

### Búsqueda de publicaciones de un vendedor

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta las publicaciones de la cuenta del vendedor, con filtros por SKU, estado, salud de exposición y producto; permite recuperar lotes grandes con scan.

**Parámetros**

- `user_id` (path, obligatorio): ID del vendedor.
- `reputation_health_gauge` (query, opcional): Valores documentados: unhealthy, warning y healthy. La funcionalidad se indica para México, Chile y Brasil.
- `sku` (query, opcional): Busca por el campo seller_custom_field.
- `seller_sku` (query, opcional): Busca por el atributo SELLER_SKU.
- `status` (query, opcional): Filtra por estado; el ejemplo usa active.
- `missing_product_identifiers` (query, opcional): true busca publicaciones sin identificador de producto; false las que sí lo tienen o están enviándolo.
- `include_filters` (query, opcional): Con true incluye filters y available_filters, ausentes por defecto para reducir el tiempo de respuesta.
- `orders` (query, opcional): ID de ordenamiento disponible; ejemplo start_time_desc.
- `listing_type_id` (query, opcional): Filtro de tipo de publicación; ejemplo gold_pro.
- `search_type` (query, opcional): Usar scan para búsquedas superiores a 1.000 registros; se omite offset.
- `scroll_id` (query, opcional): Token devuelto por scan; debe actualizarse en cada llamada y expira en 5 minutos.
- `limit` (query, opcional): En scan se devuelven 50 por defecto y se documenta un máximo de 100.
- `offset` (query, opcional): La fuente indica quitarlo al consultar con search_type=scan.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "documented_fields": [
    "seller_id",
    "query",
    "paging.limit",
    "paging.offset",
    "paging.total",
    "results",
    "orders",
    "available_orders"
  ],
  "conditional_fields": [
    "filters",
    "available_filters (al enviar include_filters=true)"
  ],
  "notes": [
    "Los resultados son IDs de publicaciones. La fuente incluye ejemplos de available_filters por estado, tipo de publicación, envío y otros."
  ],
  "status_codes": [
    200,
    206
  ],
  "status_notes": [
    "Para vendedores restringidos, include_filters=true produce HTTP 206; sin ese parámetro se documenta HTTP 200."
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/USER_ID/items/search?sku=$SELLER_CUSTOM_FIELD
- GET /users/USER_ID/items/search?seller_sku=$SELLER_SKU
- GET /users/USER_ID/items/search?missing_product_identifiers=true
- GET /users/USER_ID/items/search?search_type=scan

### Restricciones de búsqueda del vendedor

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items/search/restrictions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta si las agregaciones, consultas y ordenamientos están habilitados para el vendedor; la restricción por más de 200.000 publicaciones afecta los filtros de búsqueda.

**Parámetros**

- `user_id` (path, obligatorio): ID del vendedor.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": {
    "aggregations_allowed": "Indica si se permiten agregaciones; false se asocia a vendedores con más de 200.000 ítems.",
    "query_allowed": "Indica si la consulta está permitida.",
    "sort_allowed": "Indica si el ordenamiento está permitido."
  }
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/USER_ID/items/search/restrictions
- Ejemplo de respuesta: aggregations_allowed=false, query_allowed=true, sort_allowed=true

**Fuente:** [https://developers.mercadolibre.com.co/es_co/items-y-busquedas](https://developers.mercadolibre.com.co/es_co/items-y-busquedas)  
**Captura:** 2026-10-08T22:53:49.815Z

---
