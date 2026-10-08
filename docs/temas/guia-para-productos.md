# Guía para productos

100 páginas del portal oficial en esta área.

## [Agrupación de paquetes para la Colecta](../markdown/agrupacion-de-paquetes-para-la-colecta.md)

Actualización indicada por la fuente: 19/05/2026. Captura: 2026-10-08T22:51:00.906Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/agrupacion-de-paquetes-para-la-colecta](https://developers.mercadolibre.com.co/es_co/agrupacion-de-paquetes-para-la-colecta)

# Agrupación de paquetes para la Colecta

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 19/05/2026  
**Captura:** 2026-10-08T22:51:00.906Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/agrupacion-de-paquetes-para-la-colecta](https://developers.mercadolibre.com.co/es_co/agrupacion-de-paquetes-para-la-colecta)

## Resumen

Esta guía permite predeclarar shipments y agruparlos como bundles y volumes (sacas, cajas o palets) para la colecta. La API cubre validación del usuario, creación/búsqueda/actualización de bundles, gestión de volúmenes y descarga de archivos o etiquetas.

## Contenido y conceptos documentados

- En desarrollo se debe enviar x-scope: test en todas las llamadas. Crear un bundle recibe name y, opcionalmente, volumes; la respuesta entrega un ID y un hash requerido para operaciones posteriores. La creación documenta un límite máximo de 450 shipments.
- Los endpoints de búsqueda admiten ID, bundle_reference, bundle_id y volume_reference. La actualización permite cambiar name y usar status CLOSED o DELETED; DELETED elimina el bundle y sus volúmenes.
- Para agregar o remover volúmenes se envían volumes y hash. La etiqueta acepta bundle_id y format pdf o zpl; si no se especifica, se usa la preferencia del vendedor. El archivo de bundle es CSV.
- Estados de bundle: OPENED, CLOSED, IN_PROCESS, FINISHED, CANCELLED y DELETED; estados de volume: ADDED, PICKED_UP, EXTERNAL_PICKED_UP y EXTERNAL_CANCELLED.

## Operaciones de API

## Conceptos y recursos asociados

### Estados de Bundle y Volume

Bundle usa OPENED, CLOSED, IN_PROCESS, FINISHED, CANCELLED y DELETED; Volume usa ADDED, PICKED_UP, EXTERNAL_PICKED_UP y EXTERNAL_CANCELLED. Las transiciones restringen edición, asociación y descargas.
## Operaciones de API

### Actualizar o eliminar bundle

**Método:** `PUT`  
**Ruta:** `/soe/bundles/{bundleId}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza nombre/estado; status DELETED elimina definitivamente bundle y volúmenes.

**Parámetros**

- `bundleId` (path, obligatorio): ID positivo del bundle.

**Solicitud**

```json
{
  "name": "Nombre opcional",
  "status": "CLOSED o DELETED"
}
```

**Respuesta**

Respuesta vacía con DELETED; en otro caso, datos del bundle.

**Errores documentados**

- 400 path/body inválido.
- 401 token inválido/ausente.
- 404 bundle no encontrado.
- 409 conflicto con el estado.
- 424 dependencia externa.
- 500 error interno.
- ERR_USER_WITH_FEATURE_DISABLED, ERR_BUNDLE_FINISHED, ERR_DELETING_BUNDLE, ERR_DATA_NOT_FOUND, ERR_BUNDLE_IS_DELETED, ERR_TRANSITION_BUNDLE_STATUS, ERR_TRANSITION_STATUS_CLOSED_WITH_BUNDLE_EMPTY, ERR_TRANSITION_BUNDLE_STATUS_WITH_ALL_VOLUMES_CANCELLED, ERR_TRANSITION_BUNDLE_TEST_USER y ERR_CLOSING_BUNDLE.

**Ejemplos**

No documentado en la fuente.

### Agregar volúmenes al bundle

**Método:** `PUT`  
**Ruta:** `/soe/bundles/{bundle_id}/volumes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Asocia shipments a un bundle existente.

**Parámetros**

- `bundle_id` (path, obligatorio): ID positivo.

**Solicitud**

```json
{
  "volumes": "Lista de IDs de shipments",
  "hash": "Hash del bundle"
}
```

**Respuesta**

Datos de asociación.

**Errores documentados**

- 400 path/body inválido.
- 401 no autorizado.
- 404 bundle no encontrado.
- 409 asociación/conflicto de estado.
- 424 dependencia externa.
- 500 error interno.
- Validaciones: ERR_SHIPMENT_INVALID, ERR_SHIPMENT_CANCELLED, ERR_SHIPMENT_NOT_FOUND, ERR_BUNDLE_HASH_MISMATCH, ERR_SHIPMENT_FEATURE_DISABLED, ERR_LOGISTIC, ERR_NOT_READY_FOR_PICKUP_OR_NOT_PRINTED, ERR_SHIPMENT_ALREADY_EXIST_IN_THE_BUNDLE y ERR_SHIPMENT_EXIST_IN_OTHER_BUNDLE.

**Ejemplos**

No documentado en la fuente.

### Buscar bundle por referencia

**Método:** `GET`  
**Ruta:** `/soe/bundles/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca por parte del nombre o código bipeable.

**Parámetros**

- `bundle_reference` (query, obligatorio): Parte del nombre o código bipeable.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de bundles coincidentes.

**Errores documentados**

- 400 referencia vacía o inválida.
- 401 token inválido/ausente.
- 404 bundle/usuario no encontrado.
- 424 dependencia externa.
- 500 error interno.

**Ejemplos**

No documentado en la fuente.

### Buscar volúmenes por referencia

**Método:** `GET`  
**Ruta:** `/soe/bundles/{bundle_id}/volumes/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca por referencia parcial de shipment dentro del bundle.

**Parámetros**

- `bundle_id` (path, obligatorio): ID del bundle.
- `volume_reference` (query, obligatorio): Parte del ID del shipment.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Volúmenes coincidentes.

**Errores documentados**

- 400 bundle_id o volume_reference inválido/vacío.
- 401 token inválido/ausente.
- 404 volumen/usuario no encontrado.
- 424 dependencia externa.
- 500 error interno.

**Ejemplos**

No documentado en la fuente.

### Crear Bundle

**Método:** `POST`  
**Ruta:** `/soe/bundles`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea bundle a partir de name y, opcionalmente, shipments; devuelve ID y hash para operaciones posteriores.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "name": "Nombre del bundle",
  "volumes": "IDs de shipment opcionales"
}
```

**Respuesta**

Datos de bundle, ID y hash.

**Errores documentados**

- 201 creado.
- 400 JSON inválido.
- 401 aplicación no autorizada.
- 409 conflicto.
- 424 dependencia externa.
- 500 error interno.

**Ejemplos**

- Límite documentado: 450 shipments.

### Descargar archivo del bundle

**Método:** `GET`  
**Ruta:** `/soe/bundles/{bundleId}/file`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Descarga CSV con datos del bundle y contenerización.

**Parámetros**

- `bundleId` (path, obligatorio): ID positivo.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Archivo CSV y headers de respuesta.

**Errores documentados**

- 400 bundleId inválido.
- 401 no autorizado.
- 404 bundle/usuario no encontrado.
- 424 fallo de generación.
- 500 error interno.

**Ejemplos**

No documentado en la fuente.

### Generar/descargar etiqueta

**Método:** `POST`  
**Ruta:** `/soe/bundles/label`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Genera etiqueta imprimible para bundle.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "bundle_id": "ID del bundle",
  "format": "pdf o zpl; opcional/null usa preferencia del usuario"
}
```

**Respuesta**

Archivo de etiqueta.

**Errores documentados**

- 400 body inválido.
- 401 no autorizado.
- 404 bundle no encontrado.
- 424 fallo de generación.
- 500 error interno.

**Ejemplos**

No documentado en la fuente.

### Listar bundles del usuario

**Método:** `GET`  
**Ruta:** `/soe/bundles`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista bundles abiertos, cerrados, finalizados y cancelados; no incluye volúmenes.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de bundles del usuario.

**Errores documentados**

- 401 token inválido/ausente.
- 404 usuario no encontrado.
- 424 dependencia externa.
- 500 error interno.

**Ejemplos**

No documentado en la fuente.

### Listar volúmenes del bundle

**Método:** `GET`  
**Ruta:** `/soe/bundles/{bundle_id}/volumes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista paquetes asociados a un bundle.

**Parámetros**

- `bundle_id` (path, obligatorio): ID del bundle.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Volumes vinculados.

**Errores documentados**

- 400 bundle_id inválido/vacío.
- 401 token inválido/ausente.
- 404 usuario no encontrado.
- 424 dependencia externa.
- 500 error interno.

**Ejemplos**

No documentado en la fuente.

### Remover volúmenes del bundle

**Método:** `DELETE`  
**Ruta:** `/soe/bundles/{bundle_id}/volumes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Desvincula shipments de un bundle.

**Parámetros**

- `bundle_id` (path, obligatorio): ID positivo.

**Solicitud**

```json
{
  "volumes": "IDs de shipments a eliminar",
  "hash": "Hash del bundle"
}
```

**Respuesta**

Respuesta de la operación.

**Errores documentados**

- 400 path inválido.
- 401 no autorizado.
- 404 bundle no encontrado.
- 409 no removible por estado actual.
- 424 dependencia externa.
- 500 error interno.

**Ejemplos**

No documentado en la fuente.

### Buscar bundle por ID

**Método:** `GET`  
**Ruta:** `/soe/bundles/{bundle_id}/summary`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene resumen, datos de contenerización, volúmenes y estado.

**Parámetros**

- `bundle_id` (path, obligatorio): ID del bundle.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Bundle Summary y Volume.

**Errores documentados**

- 401 token inválido/ausente.
- 404 bundle o usuario no encontrado.
- 424 dependencia externa.
- 500 error interno.

**Ejemplos**

No documentado en la fuente.

### Validar habilitación del usuario

**Método:** `GET`  
**Ruta:** `/soe/bundles/users/validate`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Comprueba si el vendedor puede usar agrupación de paquetes.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

active y, si está inactivo, reason.

**Errores documentados**

- 403: permisos de Shipments and Sales faltantes o función deshabilitada.
- 424: dependencia externa.
- 500: error interno.

**Ejemplos**

- En desarrollo enviar x-scope: test.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/agrupacion-de-paquetes-para-la-colecta](https://developers.mercadolibre.com.co/es_co/agrupacion-de-paquetes-para-la-colecta)  
**Captura:** 2026-10-08T22:51:00.906Z

---

## [Automatizaciones de precios](../markdown/automatizaciones-de-precios.md)

Actualización indicada por la fuente: 01/10/2026. Captura: 2026-10-08T22:51:01.963Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/automatizaciones-de-precios](https://developers.mercadolibre.com.co/es_co/automatizaciones-de-precios)

# Automatizaciones de precios

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 01/10/2026  
**Captura:** 2026-10-08T22:51:01.963Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/automatizaciones-de-precios](https://developers.mercadolibre.com.co/es_co/automatizaciones-de-precios)

## Resumen

Documenta cómo consultar, asignar, modificar y retirar reglas de automatización de precios, además de revisar el historial. Si un ítem tiene automatización activa, las actualizaciones de precio por la API de ítems se rechazan.

## Contenido y conceptos documentados

- Las reglas se identifican con `rule_id`; la fuente también muestra `min_price`, `max_price`, `status` (`ACTIVE` o `PAUSED`) y `status_detail`.
- Antes de modificar el precio de un ítem, consulta si tiene automatización. El cambio del campo `price` mediante `PUT /items/{item_id}` puede responder `item.price.not_modifiable` (400).
- También se documentan historial de precios y reglas disponibles a nivel de producto de catálogo.
- Errores de automatización documentados incluyen `item_not_found` (404), `user_not_authorized` (412), `item_not_automatizable` (412), `automation_already_created` (412), `automation_operation_not_allowed` (412) y errores de procesamiento de regla/estrategia (422).

**Campos y respuestas:** `rule_id`, `min_price`, `max_price`, `status`, `status_detail`, `item_id` y `price`; la estructura depende de cada operación.

**Ejemplos documentados:** consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

## Operaciones de API

## Conceptos y recursos asociados

### Automatizaciones de precios

Documenta cómo consultar, asignar, modificar y retirar reglas de automatización de precios, además de revisar el historial. Si un ítem tiene automatización activa, las actualizaciones de precio por la API de ítems se rechazan.

**Respuesta**

```json
{
  "fields": "`rule_id`, `min_price`, `max_price`, `status`, `status_detail`, `item_id` y `price`; la estructura depende de cada operación."
}
```

**Ejemplos documentados**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.
## Operaciones de API

### Elimina la automatización del ítem

**Método:** `DELETE`  
**Ruta:** `/pricing-automation/items/{item_id}/automation`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la automatización del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### Consulta la automatización del ítem

**Método:** `GET`  
**Ruta:** `/pricing-automation/items/{item_id}/automation`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la automatización del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### Consulta el historial de cambios de precio automatizados

**Método:** `GET`  
**Ruta:** `/pricing-automation/items/{item_id}/price/history`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el historial de cambios de precio automatizados.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### Consulta reglas disponibles para un ítem

**Método:** `GET`  
**Ruta:** `/pricing-automation/items/{item_id}/rules`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta reglas disponibles para un ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### Consulta reglas para un producto de catálogo

**Método:** `GET`  
**Ruta:** `/pricing-automation/products/{catalog_product_id}/rules`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta reglas para un producto de catálogo.

**Parámetros**

- `catalog_product_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### Lista ítems del usuario con automatizaciones; admite `offset` y `limit`

**Método:** `GET`  
**Ruta:** `/pricing-automation/users/{user_id}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista ítems del usuario con automatizaciones; admite `offset` y `limit`.

**Parámetros**

- `user_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `offset` (query): Parámetro de paginación.
- `limit` (query): Parámetro de paginación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### Asigna una regla (`rule_id`)

**Método:** `POST`  
**Ruta:** `/pricing-automation/items/{item_id}/automation`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Asigna una regla (`rule_id`).

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

```json
{
  "fields": [
    "rule_id"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### Asigna automatización indicando producto de catálogo

**Método:** `POST`  
**Ruta:** `/pricing-automation/items/{item_id}/automation/by-product/{catalog_product_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Asigna automatización indicando producto de catálogo.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `catalog_product_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### La guía advierte que cambiar el precio se rechaza si la automatización está activa

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La guía advierte que cambiar el precio se rechaza si la automatización está activa.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

```json
{
  "fields": [
    "price"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400 item.price.not_modifiable: precio no editable cuando la automatización está activa.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

### Actualiza la regla asignada

**Método:** `PUT`  
**Ruta:** `/pricing-automation/items/{item_id}/automation`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza la regla asignada.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

```json
{
  "fields": [
    "rule_id"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de reglas, asignación con `rule_id`, paginación `offset`/`limit` e historial para un ítem.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/automatizaciones-de-precios](https://developers.mercadolibre.com.co/es_co/automatizaciones-de-precios)  
**Captura:** 2026-10-08T22:51:01.963Z

---

## [Buenas Prácticas para el Consumo de las APIs de Reportes de Facturación](../markdown/buenas-practicas-para-el-consumo-de-las-apis-de-reportes-de-facturacion.md)

Actualización indicada por la fuente: 08/06/2026. Captura: 2026-10-08T22:51:03.392Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-el-consumo-de-las-apis-de-reportes-de-facturacion](https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-el-consumo-de-las-apis-de-reportes-de-facturacion)

# Buenas Prácticas para el Consumo de las APIs de Reportes de Facturación

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 08/06/2026  
**Captura:** 2026-10-08T22:51:03.392Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-el-consumo-de-las-apis-de-reportes-de-facturacion](https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-el-consumo-de-las-apis-de-reportes-de-facturacion)

## Resumen

Explica el consumo de reportes de facturación de Mercado Libre y Mercado Pago para conciliación fiscal y posventa. Recomienda consultar períodos, documentos y detalles con paginación y caché, sin usar estos recursos para operaciones en tiempo real.

## Contenido y conceptos documentados

- Los grupos de facturación son `ML` (Mercado Libre) y `MP` (Mercado Pago). La guía indica el parámetro global `group`; también señala que, al omitirlo, se obtiene información de ambos grupos.
- Los documentos admiten filtros `document_id` y `document_type` (`BILL` o `CREDIT_NOTE`). Para detalles se muestran `offset`, `limit`, `from_id`, `sort_by` y `order_by`.
- La clave mensual sigue `YYYY-MM-01`. Se recomienda consultar períodos una vez, derivar la clave y usar caché; evitar polling y lotes masivos.
- El flujo propuesto es obtener el período, recuperar documentos y consultar detalles por grupo. El resumen se recomienda consumir secuencialmente una vez al día.
- Para órdenes en tiempo real la guía remite a recursos operativos distintos. El error 429 indica exceso de solicitudes/bloqueo preventivo por IP; reducir frecuencia, usar caché y evitar batch.

**Campos y respuestas:** la guía describe períodos, documentos, detalles de facturación y descargas de documentos/reportes; los esquemas completos de respuesta no están documentados aquí.

**Ejemplos documentados:** paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

## Operaciones de API

## Conceptos y recursos asociados

### Buenas Prácticas para el Consumo de las APIs de Reportes de Facturación

Explica el consumo de reportes de facturación de Mercado Libre y Mercado Pago para conciliación fiscal y posventa. Recomienda consultar períodos, documentos y detalles con paginación y caché, sin usar estos recursos para operaciones en tiempo real.

**Respuesta**

```json
{
  "fields": "la guía describe períodos, documentos, detalles de facturación y descargas de documentos/reportes; los esquemas completos de respuesta no están documentados aquí."
}
```

**Errores documentados**

- 429 Too Many Requests: bloqueo preventivo por IP; reducir frecuencia, implementar caché y evitar batch masivo.

**Ejemplos documentados**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.
## Operaciones de API

### Consulta detalles por orden o pack

**Método:** `GET`  
**Ruta:** `/billing/integration/group/ML/order/details`  
**Autenticación:** No documentado en la fuente.

Consulta detalles por orden o pack.

**Parámetros**

- `order_ids` (query): Parámetro documentado.
- `group` (query): Grupo ML/MP; al omitirlo retorna ambos grupos según la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Descarga documento legal

**Método:** `GET`  
**Ruta:** `/billing/integration/legal_document/{file_id}`  
**Autenticación:** No documentado en la fuente.

Descarga documento legal.

**Parámetros**

- `file_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Lista períodos de facturación

**Método:** `GET`  
**Ruta:** `/billing/integration/monthly/periods`  
**Autenticación:** No documentado en la fuente.

Lista períodos de facturación.

**Parámetros**

- `group` (query): Grupo ML/MP; al omitirlo retorna ambos grupos según la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Lista documentos del período; admite tipo, identificador y paginación

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/{key}/documents`  
**Autenticación:** No documentado en la fuente.

Lista documentos del período; admite tipo, identificador y paginación.

**Parámetros**

- `key` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `group` (query): Grupo ML/MP; al omitirlo retorna ambos grupos según la fuente.
- `document_id` (query): Parámetro documentado.
- `document_type` (query): Tipo BILL o CREDIT_NOTE.
- `offset` (query): Paginación.
- `limit` (query): Paginación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Consulta detalles ML con paginación

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/{key}/group/ML/details`  
**Autenticación:** No documentado en la fuente.

Consulta detalles ML con paginación.

**Parámetros**

- `key` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `document_type` (query): Tipo BILL o CREDIT_NOTE.
- `limit` (query): Paginación.
- `from_id` (query): Cursor de paginación.
- `sort_by` (query): Ordenamiento documentado.
- `order_by` (query): Ordenamiento documentado.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Consulta detalles de pagos ML

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/{key}/group/ML/payment/details`  
**Autenticación:** No documentado en la fuente.

Consulta detalles de pagos ML.

**Parámetros**

- `key` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `document_type` (query): Tipo BILL o CREDIT_NOTE.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Consulta detalles MP con paginación

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/{key}/group/MP/details`  
**Autenticación:** No documentado en la fuente.

Consulta detalles MP con paginación.

**Parámetros**

- `key` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `document_type` (query): Tipo BILL o CREDIT_NOTE.
- `limit` (query): Paginación.
- `from_id` (query): Cursor de paginación.
- `sort_by` (query): Ordenamiento documentado.
- `order_by` (query): Ordenamiento documentado.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Resumen de percepciones, exclusivo para MLA

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/{key}/perceptions/summary`  
**Autenticación:** No documentado en la fuente.

Resumen de percepciones, exclusivo para MLA.

**Parámetros**

- `key` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Consulta resumen del período

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/{key}/summary/details`  
**Autenticación:** No documentado en la fuente.

Consulta resumen del período.

**Parámetros**

- `key` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `group` (query): Grupo ML/MP; al omitirlo retorna ambos grupos según la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Descarga reporte CSV/XLSX generado previamente

**Método:** `GET`  
**Ruta:** `/billing/integration/reports/{file_id}`  
**Autenticación:** No documentado en la fuente.

Descarga reporte CSV/XLSX generado previamente.

**Parámetros**

- `file_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Consulta el precio de venta de un ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}/sale_price`  
**Autenticación:** No documentado en la fuente.

Consulta el precio de venta de un ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Consulta datos de órdenes en tiempo real

**Método:** `GET`  
**Ruta:** `/orders`  
**Autenticación:** No documentado en la fuente.

Consulta datos de órdenes en tiempo real.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Consulta descuentos aplicados a una orden

**Método:** `GET`  
**Ruta:** `/orders/{id}/discounts`  
**Autenticación:** No documentado en la fuente.

Consulta descuentos aplicados a una orden.

**Parámetros**

- `id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Identifica órdenes agrupadas en packs

**Método:** `GET`  
**Ruta:** `/packs`  
**Autenticación:** No documentado en la fuente.

Identifica órdenes agrupadas en packs.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

### Consulta costos de envío

**Método:** `GET`  
**Ruta:** `/shipments`  
**Autenticación:** No documentado en la fuente.

Consulta costos de envío.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- paginación de detalles con `limit=1000&from_id=0`, avanzando desde el último identificador procesado.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-el-consumo-de-las-apis-de-reportes-de-facturacion](https://developers.mercadolibre.com.co/es_co/buenas-practicas-para-el-consumo-de-las-apis-de-reportes-de-facturacion)  
**Captura:** 2026-10-08T22:51:03.392Z

---

## [Buscador de productos](../markdown/buscador-de-productos.md)

Actualización indicada por la fuente: 29/12/2025. Captura: 2026-10-08T22:51:04.446Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/buscador-de-productos](https://developers.mercadolibre.com.co/es_co/buscador-de-productos)

# Buscador de productos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:51:04.446Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/buscador-de-productos](https://developers.mercadolibre.com.co/es_co/buscador-de-productos)

## Resumen

Describe cómo buscar productos de catálogo para asociar una publicación con la página de producto correcta. Permite buscar por identificador universal, texto o atributos, consultar el producto y revisar elegibilidad antes de publicar.

## Contenido y conceptos documentados

- `site_id` identifica el país y es obligatorio. La guía indica disponibilidad en Argentina, México, Brasil, Colombia, Chile, Uruguay, Perú y Ecuador.
- La búsqueda admite `product_identifier` (p. ej., GTIN/EAN/UPC/ISBN) o `q`; si no se envía `q`, `product_identifier` es obligatorio. Puede acotarse con `domain_id`.
- `status=active` devuelve productos elegibles para asociar; `status=inactive` devuelve productos aún no elegibles. Si se omite, se incluyen ambos estados.
- La búsqueda POST permite precisar la consulta mediante atributos. Los ejemplos cubren part number, product ID y atributos de catálogo.
- Para validar un producto se consultan campos como `id`, `status`, `attributes`, `pictures`, `pickers`, `main_features`, `short_description`, `permalink`, `children_ids`, `parent_id` y `buy_box_winner`. En productos inactivos algunos campos pueden ser nulos o vacíos.
- `catalog_product_id` de una publicación sirve para verificar la asociación adecuada antes de publicarla en catálogo; la fuente distingue productos padre no específicos y productos hijos.

**Campos y respuestas:** `catalog_product_id`, `id`, `status`, `domain_id`, `attributes`, `pictures`, `pickers`, `main_features`, `short_description`, `permalink`, `children_ids`, `parent_id` y `buy_box_winner`.

**Ejemplos documentados:** búsquedas GET por identificador, texto y dominio; búsqueda POST por atributos; consulta GET de un producto.

## Operaciones de API

## Conceptos y recursos asociados

### Buscador de productos

Describe cómo buscar productos de catálogo para asociar una publicación con la página de producto correcta. Permite buscar por identificador universal, texto o atributos, consultar el producto y revisar elegibilidad antes de publicar.

**Respuesta**

```json
{
  "fields": "`catalog_product_id`, `id`, `status`, `domain_id`, `attributes`, `pictures`, `pickers`, `main_features`, `short_description`, `permalink`, `children_ids`, `parent_id` y `buy_box_winner`."
}
```

**Ejemplos documentados**

- búsquedas GET por identificador, texto y dominio; búsqueda POST por atributos; consulta GET de un producto.
## Operaciones de API

### La guía usa esta lectura para validar `catalog_product_id` antes de crear una publicación de catálogo

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La guía usa esta lectura para validar `catalog_product_id` antes de crear una publicación de catálogo.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- búsquedas GET por identificador, texto y dominio; búsqueda POST por atributos; consulta GET de un producto.

### Consulta los datos del producto de catálogo

**Método:** `GET`  
**Ruta:** `/products/{product_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta los datos del producto de catálogo.

**Parámetros**

- `product_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "status",
    "domain_id",
    "attributes",
    "pictures",
    "pickers",
    "main_features",
    "short_description",
    "permalink",
    "children_ids",
    "parent_id",
    "buy_box_winner"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- búsquedas GET por identificador, texto y dominio; búsqueda POST por atributos; consulta GET de un producto.

### Busca por texto o identificador universal y filtros de catálogo

**Método:** `GET`  
**Ruta:** `/products/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca por texto o identificador universal y filtros de catálogo.

**Parámetros**

- `site_id` (query, obligatorio): La guía lo indica obligatorio.
- `status` (query): active/inactive; al omitirlo se incluyen ambos.
- `q` (query)
- `product_identifier` (query): Identificador universal; requerido cuando no se envía q.
- `domain_id` (query)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "results",
    "paging",
    "id",
    "status",
    "product_identifier",
    "domain_id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- búsquedas GET por identificador, texto y dominio; búsqueda POST por atributos; consulta GET de un producto.

### Realiza una búsqueda más específica basada en atributos

**Método:** `POST`  
**Ruta:** `/products/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Realiza una búsqueda más específica basada en atributos.

**Parámetros**

- `site_id` (query, obligatorio): La guía lo indica obligatorio.
- `status` (query): active/inactive; al omitirlo se incluyen ambos.
- `q` (query)
- `product_identifier` (query): Identificador universal; requerido cuando no se envía q.
- `domain_id` (query)

**Solicitud**

```json
{
  "fields": [
    "atributos de búsqueda"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "results",
    "paging",
    "id",
    "status",
    "product_identifier",
    "domain_id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- búsquedas GET por identificador, texto y dominio; búsqueda POST por atributos; consulta GET de un producto.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/buscador-de-productos](https://developers.mercadolibre.com.co/es_co/buscador-de-productos)  
**Captura:** 2026-10-08T22:51:04.446Z

---

## [Calidad de publicaciones](../markdown/calidad-de-publicaciones.md)

Actualización indicada por la fuente: 31/01/2025. Captura: 2026-10-08T22:51:07.212Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones](https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones)

# Calidad de publicaciones

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 31/01/2025  
**Captura:** 2026-10-08T22:51:07.212Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones](https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones)

## Resumen

Documenta el recurso de performance para presentar calidad de publicaciones y acciones pendientes o completadas que pueden mejorarla. Incluye consultas para ítems y User Products, niveles por sitio y la transición desde `/health`.

## Contenido y conceptos documentados

- El nivel se presenta con métricas y acciones. `level_wording` varía por sitio; la guía enumera niveles básico, medio y bueno con etiquetas localizadas.
- Las respuestas incluyen datos como `entity_id`, `entity_type`, `level`, `level_wording`, `score`, `progress`, `rules`, `status`, `title`, `label`, `link`, `wordings` y `calculated_at`.
- El estado de una acción/regla es `PENDING` si requiere acciones y `COMPLETED` si ya se realizaron.
- La guía indica que `/health` será descontinuado el 7 de febrero y sustituido por `/performance`; no indica el año en esa afirmación.
- Errores documentados: 400 solicitud inválida; 401 la entidad no pertenece al vendedor del token; 403 permisos insuficientes; 404 datos de performance no generados; 500 error interno.

**Campos y respuestas:** `entity_id`, `entity_type`, `level`, `level_wording`, `score`, `progress`, `rules`, `status`, `title`, `label`, `link`, `wordings` y `calculated_at`.

**Ejemplos documentados:** consultas GET para un ítem y un User Product.

## Operaciones de API

## Conceptos y recursos asociados

### Calidad de publicaciones

Documenta el recurso de performance para presentar calidad de publicaciones y acciones pendientes o completadas que pueden mejorarla. Incluye consultas para ítems y User Products, niveles por sitio y la transición desde `/health`.

**Respuesta**

```json
{
  "fields": "`entity_id`, `entity_type`, `level`, `level_wording`, `score`, `progress`, `rules`, `status`, `title`, `label`, `link`, `wordings` y `calculated_at`."
}
```

**Errores documentados**

- Errores documentados: 400 solicitud inválida; 401 la entidad no pertenece al vendedor del token; 403 permisos insuficientes; 404 datos de performance no generados; 500 error interno.

**Ejemplos documentados**

- consultas GET para un ítem y un User Product.
## Operaciones de API

### Obtiene calidad y acciones de mejora para una publicación

**Método:** `GET`  
**Ruta:** `/item/{item_id}/performance`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene calidad y acciones de mejora para una publicación.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "entity_id",
    "entity_type",
    "level",
    "level_wording",
    "score",
    "progress",
    "rules",
    "status",
    "calculated_at"
  ]
}
```

**Errores documentados**

- 400: solicitud inválida.
- 401: la entidad no pertenece al vendedor del token.
- 403: permisos insuficientes.
- 404: performance no generado.
- 500: error interno.

**Ejemplos**

- consultas GET para un ítem y un User Product.

### Obtiene calidad y acciones asociadas al User Product

**Método:** `GET`  
**Ruta:** `/user-product/{user_product_id}/performance`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene calidad y acciones asociadas al User Product.

**Parámetros**

- `user_product_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "entity_id",
    "entity_type",
    "level",
    "level_wording",
    "score",
    "progress",
    "rules",
    "status",
    "calculated_at"
  ]
}
```

**Errores documentados**

- 400: solicitud inválida.
- 401: la entidad no pertenece al vendedor del token.
- 403: permisos insuficientes.
- 404: performance no generado.
- 500: error interno.

**Ejemplos**

- consultas GET para un ítem y un User Product.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones](https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones)  
**Captura:** 2026-10-08T22:51:07.212Z

---

## [Cambios](../markdown/changes.md)

Actualización indicada por la fuente: 04/02/2026. Captura: 2026-10-08T22:51:08.170Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/changes](https://developers.mercadolibre.com.co/es_co/changes)

# Cambios

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 04/02/2026  
**Captura:** 2026-10-08T22:51:08.170Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/changes](https://developers.mercadolibre.com.co/es_co/changes)

## Resumen

Describe la consulta de cambios asociados a una venta y el flujo de reemplazo de productos en una reclamación. La elegibilidad se comprueba en la reclamación antes de enviar la acción `allow_replace`.

## Contenido y conceptos documentados

- La guía cubre cambios para envíos Full y Cross Docking, con Cross Docking Drop Off indicado como próximo; reemplazos para Full y próximos para Cross Docking/Cross Docking Drop Off.
- El recurso de cambios relaciona la reclamación con la compra y expone identificadores, estados, ítems, fechas y datos de nuevas órdenes/envíos.
- Para ofrecer un reemplazo, consulta la reclamación y verifica que esté disponible la acción `allow_replace`; solo entonces envía el POST de resolución esperada.
- La respuesta exitosa se documenta como estado abierto. Si la acción no está permitida, la fuente muestra error 400. Estados de fallo incluyen `purchase_pay_failed` y `purchase_failed`.

**Campos y respuestas:** `claim_id`, `status`, `status_detail`, `items`, `expected_resolution`, `new_orders_ids`, `new_orders_shipments`, `date_created` y `last_updated`.

**Ejemplos documentados:** consulta GET de cambios, consulta GET de reclamación y POST de `allow_replace`, con casos de elegibilidad y rechazo.

## Operaciones de API

## Conceptos y recursos asociados

### Cambios

Describe la consulta de cambios asociados a una venta y el flujo de reemplazo de productos en una reclamación. La elegibilidad se comprueba en la reclamación antes de enviar la acción `allow_replace`.

**Respuesta**

```json
{
  "fields": "`claim_id`, `status`, `status_detail`, `items`, `expected_resolution`, `new_orders_ids`, `new_orders_shipments`, `date_created` y `last_updated`."
}
```

**Errores documentados**

- La respuesta exitosa se documenta como estado abierto. Si la acción no está permitida, la fuente muestra error 400. Estados de fallo incluyen `purchase_pay_failed` y `purchase_failed`.

**Ejemplos documentados**

- consulta GET de cambios, consulta GET de reclamación y POST de `allow_replace`, con casos de elegibilidad y rechazo.
### Ruta mencionada /claims/{CLAIM_ID}

La fuente menciona la ruta /claims/{CLAIM_ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/{CLAIM_ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Permite verificar si la reclamación ofrece la acción `allow_replace`

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/{claim_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Permite verificar si la reclamación ofrece la acción `allow_replace`.

**Parámetros**

- `claim_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta GET de cambios, consulta GET de reclamación y POST de `allow_replace`, con casos de elegibilidad y rechazo.

### Consulta cambios asociados a una reclamación

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/{claim_id}/changes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta cambios asociados a una reclamación.

**Parámetros**

- `claim_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "claim_id",
    "status",
    "status_detail",
    "items",
    "new_orders_ids",
    "new_orders_shipments",
    "date_created",
    "last_updated"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta GET de cambios, consulta GET de reclamación y POST de `allow_replace`, con casos de elegibilidad y rechazo.

### Inicia la oferta de reemplazo si está disponible

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/{claim_id}/expected-resolutions/allow-replace`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Inicia la oferta de reemplazo si está disponible.

**Parámetros**

- `claim_id` (path, obligatorio): Variable de ruta mostrada por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: acción de reemplazo no permitida para esta reclamación.

**Ejemplos**

- consulta GET de cambios, consulta GET de reclamación y POST de `allow_replace`, con casos de elegibilidad y rechazo.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/changes](https://developers.mercadolibre.com.co/es_co/changes)  
**Captura:** 2026-10-08T22:51:08.170Z

---

## [Campaña co-fondeada para PIX](../markdown/pix.md)

Actualización indicada por la fuente: 25/04/2025. Captura: 2026-10-08T22:51:09.102Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/pix](https://developers.mercadolibre.com.co/es_co/pix)

# Campaña co-fondeada para PIX

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 25/04/2025  
**Captura:** 2026-10-08T22:51:09.102Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/pix](https://developers.mercadolibre.com.co/es_co/pix)

## Resumen

Documenta la participación en campañas cofinanciadas de pagos PIX. El tipo de promoción es `BANK`, el subtipo `COFINANCED` y la disponibilidad indicada por la fuente es exclusivamente para el sitio brasileño MLB.

## Contenido y conceptos documentados

- El detalle de campaña identifica `type`, `sub_type`, `status`, fechas y `payment_method` (`PIX`).
- Se consulta la campaña y sus ítems; los ítems candidatos pueden sumarse y una oferta pendiente o activa puede eliminarse.
- La respuesta de oferta incluye `price`, `original_price` y `offer_id`; la campaña muestra porcentajes de cofinanciación del vendedor y Mercado Libre.
- Se documenta el estado de ítem `candidate` y estados de campaña como `candidate`, `started` y `pending`. La sección de errores registra 400 Bad Request.

**Campos y respuestas:** `id`, `type`, `sub_type`, `status`, `start_date`, `finish_date`, `deadline_date`, `name`, `payment_method`, `seller_percentage`, `meli_percentage`, `price`, `original_price` y `offer_id`.

**Ejemplos documentados:** consulta con `promotion_type=BANK&app_version=v2`, respuesta de campaña y ejemplo de oferta.

## Operaciones de API

## Conceptos y recursos asociados

### Campaña co-fondeada para PIX

Documenta la participación en campañas cofinanciadas de pagos PIX. El tipo de promoción es `BANK`, el subtipo `COFINANCED` y la disponibilidad indicada por la fuente es exclusivamente para el sitio brasileño MLB.

**Respuesta**

```json
{
  "fields": "`id`, `type`, `sub_type`, `status`, `start_date`, `finish_date`, `deadline_date`, `name`, `payment_method`, `seller_percentage`, `meli_percentage`, `price`, `original_price` y `offer_id`."
}
```

**Errores documentados**

- 400 Bad Request: la fuente lo enumera como error de la operación.

**Ejemplos documentados**

- consulta con `promotion_type=BANK&app_version=v2`, respuesta de campaña y ejemplo de oferta.
## Operaciones de API

### Elimina una oferta identificando promoción y oferta

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina una oferta identificando promoción y oferta.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: BANK
- `promotion_id` (query)
- `offer_id` (query)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta con `promotion_type=BANK&app_version=v2`, respuesta de campaña y ejemplo de oferta.

### Consulta detalle de campaña PIX

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalle de campaña PIX.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: BANK
- `app_version` (query): Valor mostrado: v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "type",
    "status",
    "start_date",
    "finish_date",
    "deadline_date",
    "name"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta con `promotion_type=BANK&app_version=v2`, respuesta de campaña y ejemplo de oferta.

### Lista los ítems de la campaña

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista los ítems de la campaña.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: BANK
- `app_version` (query): Valor mostrado: v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "results",
    "paging",
    "status",
    "offer_id",
    "price",
    "original_price"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta con `promotion_type=BANK&app_version=v2`, respuesta de campaña y ejemplo de oferta.

### Agrega una oferta del ítem a la campaña

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega una oferta del ítem a la campaña.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: BANK
- `promotion_id` (query)
- `offer_id` (query)

**Solicitud**

```json
{
  "fields": [
    "price"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta con `promotion_type=BANK&app_version=v2`, respuesta de campaña y ejemplo de oferta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/pix](https://developers.mercadolibre.com.co/es_co/pix)  
**Captura:** 2026-10-08T22:51:09.102Z

---

## [Campañas co-fondeadas](../markdown/campanas-co-fondeadas.md)

Actualización indicada por la fuente: 22/01/2025. Captura: 2026-10-08T22:51:10.088Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/campanas-co-fondeadas](https://developers.mercadolibre.com.co/es_co/campanas-co-fondeadas)

# Campañas co-fondeadas

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 22/01/2025  
**Captura:** 2026-10-08T22:51:10.088Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/campanas-co-fondeadas](https://developers.mercadolibre.com.co/es_co/campanas-co-fondeadas)

## Resumen

Explica cómo consultar y gestionar campañas cofinanciadas a las que Mercado Libre invita al vendedor. Mercado Libre aporta una parte del descuento; se consultan campañas e ítems, se incorporan ofertas y se eliminan cuando corresponda.

## Contenido y conceptos documentados

- La campaña usa `promotion_type=MARKETPLACE_CAMPAIGN` y `app_version=v2`; la respuesta contiene tipo, estado, fechas, nombre y beneficios.
- Los ítems comienzan como `candidate` y sin `offer_id`. Al incorporarlos reciben un identificador de oferta y cambia su estado.
- El filtro `status_item` admite `active` o `paused`. La fuente expone `benefits` y porcentajes de participación del vendedor y Mercado Libre.
- Los ejemplos muestran respuesta 200 OK al eliminar una oferta.

**Campos y respuestas:** `id`, `type`, `status`, `start_date`, `finish_date`, `deadline_date`, `name`, `benefits`, `seller_percentage`, `meli_percentage`, `offer_id`, `price` y `original_price`.

**Ejemplos documentados:** consulta de campaña e ítems, incorporación de un ítem y eliminación de una oferta.

## Operaciones de API

## Conceptos y recursos asociados

### Campañas co-fondeadas

Explica cómo consultar y gestionar campañas cofinanciadas a las que Mercado Libre invita al vendedor. Mercado Libre aporta una parte del descuento; se consultan campañas e ítems, se incorporan ofertas y se eliminan cuando corresponda.

**Respuesta**

```json
{
  "fields": "`id`, `type`, `status`, `start_date`, `finish_date`, `deadline_date`, `name`, `benefits`, `seller_percentage`, `meli_percentage`, `offer_id`, `price` y `original_price`."
}
```

**Ejemplos documentados**

- consulta de campaña e ítems, incorporación de un ítem y eliminación de una oferta.
## Operaciones de API

### Elimina la oferta usando tipo, ID de campaña y oferta

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la oferta usando tipo, ID de campaña y oferta.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query)
- `promotion_id` (query)
- `offer_id` (query)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de campaña e ítems, incorporación de un ítem y eliminación de una oferta.

### Consulta campaña cofinanciada y sus beneficios

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta campaña cofinanciada y sus beneficios.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: MARKETPLACE_CAMPAIGN
- `app_version` (query): Valor mostrado: v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "type",
    "status",
    "start_date",
    "finish_date",
    "deadline_date",
    "name"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de campaña e ítems, incorporación de un ítem y eliminación de una oferta.

### Lista los ítems; admite `status_item` (`active` o `paused`)

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista los ítems; admite `status_item` (`active` o `paused`).

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: MARKETPLACE_CAMPAIGN
- `app_version` (query): Valor mostrado: v2
- `status_item` (query): active o paused.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "results",
    "paging",
    "status",
    "offer_id",
    "price",
    "original_price"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de campaña e ítems, incorporación de un ítem y eliminación de una oferta.

### Agrega un ítem candidato a la campaña

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega un ítem candidato a la campaña.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query)
- `promotion_id` (query)
- `offer_id` (query)

**Solicitud**

```json
{
  "fields": [
    "price"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de campaña e ítems, incorporación de un ítem y eliminación de una oferta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/campanas-co-fondeadas](https://developers.mercadolibre.com.co/es_co/campanas-co-fondeadas)  
**Captura:** 2026-10-08T22:51:10.088Z

---

## [Campañas con descuento por cantidad](../markdown/campanas-con-descuento-por-cantidad.md)

Actualización indicada por la fuente: 13/03/2026. Captura: 2026-10-08T22:51:11.035Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/campanas-con-descuento-por-cantidad](https://developers.mercadolibre.com.co/es_co/campanas-con-descuento-por-cantidad)

# Campañas con descuento por cantidad

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/03/2026  
**Captura:** 2026-10-08T22:51:11.035Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/campanas-con-descuento-por-cantidad](https://developers.mercadolibre.com.co/es_co/campanas-con-descuento-por-cantidad)

## Resumen

Documenta campañas de descuento por cantidad/volumen, donde el comprador obtiene un descuento al alcanzar una combinación de unidades compradas y pagadas. Incluye creación y administración de campañas y ofertas asociadas.

## Contenido y conceptos documentados

- La campaña define `sub_type`, cantidades de compra/pago, porcentaje de descuento, fechas y posibilidad de combinación (`allow_combination`).
- El antiguo mecanismo de descuento por volumen de Mercado Livre fue descontinuado; las campañas existentes continúan hasta su finalización.
- Los ítems aplicables comienzan como `candidate` sin `offer_id`; al agregarlos reciben un identificador de oferta.
- El filtro `status_item` admite `active` o `paused`; las ofertas usan `promotion_type=VOLUME` y `app_version=v2`.
- La fuente documenta respuestas 200 OK al actualizar o eliminar según operación; al eliminar la campaña, el cuerpo puede ser nulo.

**Campos y respuestas:** `promotion_id`, `promotion_type`, `status`, `sub_type`, `buy_quantity`, `pay_quantity`, `discount_percentage`, `allow_combination`, `start_date`, `finish_date`, `offer_id`, `price` y `original_price`.

**Ejemplos documentados:** crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.

## Operaciones de API

## Conceptos y recursos asociados

### Campañas con descuento por cantidad

Documenta campañas de descuento por cantidad/volumen, donde el comprador obtiene un descuento al alcanzar una combinación de unidades compradas y pagadas. Incluye creación y administración de campañas y ofertas asociadas.

**Respuesta**

```json
{
  "fields": "`promotion_id`, `promotion_type`, `status`, `sub_type`, `buy_quantity`, `pay_quantity`, `discount_percentage`, `allow_combination`, `start_date`, `finish_date`, `offer_id`, `price` y `original_price`."
}
```

**Ejemplos documentados**

- crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.
## Operaciones de API

### Elimina una oferta indicando tipo, campaña y oferta

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina una oferta indicando tipo, campaña y oferta.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: VOLUME
- `promotion_id` (query)
- `offer_id` (query)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.

### Elimina una campaña VOLUME

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina una campaña VOLUME.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: VOLUME
- `app_version` (query): Valor mostrado: v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.

### Consulta detalle y estado de campaña

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalle y estado de campaña.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: VOLUME
- `app_version` (query): Valor mostrado: v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "type",
    "status",
    "start_date",
    "finish_date",
    "deadline_date",
    "name"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.

### Lista ítems y ofertas; admite `status_item`

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista ítems y ofertas; admite `status_item`.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: VOLUME
- `app_version` (query): Valor mostrado: v2
- `status_item` (query): active o paused.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "results",
    "paging",
    "status",
    "offer_id",
    "price",
    "original_price"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.

### Agrega un ítem candidato

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega un ítem candidato.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: VOLUME
- `promotion_id` (query)
- `offer_id` (query)

**Solicitud**

```json
{
  "fields": [
    "price"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.

### Crea una campaña VOLUME

**Método:** `POST`  
**Ruta:** `/seller-promotions/promotions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una campaña VOLUME.

**Parámetros**

- `app_version` (query): Valor mostrado: v2

**Solicitud**

```json
{
  "fields": [
    "name",
    "sub_type",
    "buy_quantity",
    "pay_quantity",
    "discount_percentage",
    "allow_combination",
    "start_date",
    "finish_date"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.

### Actualiza una campaña

**Método:** `PUT`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza una campaña.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: VOLUME
- `app_version` (query): Valor mostrado: v2

**Solicitud**

```json
{
  "fields": [
    "campos editables"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- crear/actualizar/eliminar campaña, consultar detalle/ítems y agregar o retirar ítems.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/campanas-con-descuento-por-cantidad](https://developers.mercadolibre.com.co/es_co/campanas-con-descuento-por-cantidad)  
**Captura:** 2026-10-08T22:51:11.035Z

---

## [Campañas del vendedor](../markdown/campanas-del-vendedor.md)

Actualización indicada por la fuente: 13/03/2026. Captura: 2026-10-08T22:51:11.980Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/campanas-del-vendedor](https://developers.mercadolibre.com.co/es_co/campanas-del-vendedor)

# Campañas del vendedor

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/03/2026  
**Captura:** 2026-10-08T22:51:11.980Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/campanas-del-vendedor](https://developers.mercadolibre.com.co/es_co/campanas-del-vendedor)

## Resumen

Describe cómo crear y administrar campañas de descuento propias del vendedor. Incluye criterios de elegibilidad, duración máxima y operaciones para gestionar la campaña y sus ofertas.

## Contenido y conceptos documentados

- La duración máxima indicada es de 14 días. Se requiere reputación verde; el ítem debe estar activo, ser nuevo y no tener exposición gratuita.
- El aviso indica que el subtipo `FIXED_PERCENTAGE` dejará de estar disponible desde julio de 2025. La creación usa `SELLER_CAMPAIGN` y la guía muestra `FLEXIBLE_PERCENTAGE`.
- El filtro `status_item` admite `active` o `paused`. Las ofertas pueden contener `deal_price`, `top_deal_price`, `original_price` y `price`.
- La fuente restringe cambios de `top_deal_price` después de iniciar la campaña y presenta errores de validación 400, incluido el bloqueo de cambios de fecha de inicio.

**Campos y respuestas:** `id`, `type`, `status`, `sub_type`, `start_date`, `finish_date`, `promotion_id`, `price`, `original_price`, `deal_price` y `top_deal_price`.

**Ejemplos documentados:** alta, modificación, eliminación y consulta de campaña y ofertas.

## Operaciones de API

## Conceptos y recursos asociados

### Campañas del vendedor

Describe cómo crear y administrar campañas de descuento propias del vendedor. Incluye criterios de elegibilidad, duración máxima y operaciones para gestionar la campaña y sus ofertas.

**Respuesta**

```json
{
  "fields": "`id`, `type`, `status`, `sub_type`, `start_date`, `finish_date`, `promotion_id`, `price`, `original_price`, `deal_price` y `top_deal_price`."
}
```

**Errores documentados**

- 400 bad request: validación; la fuente muestra límites de porcentaje y restricciones de start_date para campañas iniciadas.

**Ejemplos documentados**

- alta, modificación, eliminación y consulta de campaña y ofertas.
## Operaciones de API

### Retira la oferta indicando campaña y tipo

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Retira la oferta indicando campaña y tipo.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: SELLER_CAMPAIGN
- `promotion_id` (query)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- alta, modificación, eliminación y consulta de campaña y ofertas.

### Elimina una campaña del vendedor

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina una campaña del vendedor.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: SELLER_CAMPAIGN
- `app_version` (query): Valor mostrado: v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- alta, modificación, eliminación y consulta de campaña y ofertas.

### Consulta detalle y estado

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalle y estado.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: SELLER_CAMPAIGN
- `app_version` (query): Valor mostrado: v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "type",
    "status",
    "start_date",
    "finish_date",
    "deadline_date",
    "name"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- alta, modificación, eliminación y consulta de campaña y ofertas.

### Lista ítems; admite `status_item`

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista ítems; admite `status_item`.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: SELLER_CAMPAIGN
- `app_version` (query): Valor mostrado: v2
- `status_item` (query): active o paused.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "results",
    "paging",
    "status",
    "offer_id",
    "price",
    "original_price"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- alta, modificación, eliminación y consulta de campaña y ofertas.

### Agrega una oferta para el ítem

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega una oferta para el ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: SELLER_CAMPAIGN
- `promotion_id` (query)

**Solicitud**

```json
{
  "fields": [
    "price"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- alta, modificación, eliminación y consulta de campaña y ofertas.

### Crea una campaña `SELLER_CAMPAIGN`

**Método:** `POST`  
**Ruta:** `/seller-promotions/promotions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una campaña `SELLER_CAMPAIGN`.

**Parámetros**

- `app_version` (query): Valor mostrado: v2

**Solicitud**

```json
{
  "fields": [
    "promotion_type",
    "name",
    "sub_type",
    "start_date",
    "finish_date"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- alta, modificación, eliminación y consulta de campaña y ofertas.

### Modifica precios de la oferta

**Método:** `PUT`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica precios de la oferta.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: SELLER_CAMPAIGN
- `promotion_id` (query)

**Solicitud**

```json
{
  "fields": [
    "deal_price",
    "top_deal_price"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- alta, modificación, eliminación y consulta de campaña y ofertas.

### Actualiza una campaña existente

**Método:** `PUT`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza una campaña existente.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: SELLER_CAMPAIGN
- `app_version` (query): Valor mostrado: v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- alta, modificación, eliminación y consulta de campaña y ofertas.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/campanas-del-vendedor](https://developers.mercadolibre.com.co/es_co/campanas-del-vendedor)  
**Captura:** 2026-10-08T22:51:11.980Z

---

## [Campañas tradicionales](../markdown/deals.md)

Actualización indicada por la fuente: 09/06/2026. Captura: 2026-10-08T22:51:12.858Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/deals](https://developers.mercadolibre.com.co/es_co/deals)

# Campañas tradicionales

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 09/06/2026  
**Captura:** 2026-10-08T22:51:12.858Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/deals](https://developers.mercadolibre.com.co/es_co/deals)

## Resumen

Documenta campañas tradicionales DEAL organizadas por Mercado Libre para vendedores invitados. El flujo permite consultar la campaña y precios sugeridos, aceptar la invitación con una oferta, ajustarla o retirarla.

## Contenido y conceptos documentados

- Los ítems candidatos pueden tener estado `candidate`; el filtro `status_item` admite `active` o `paused`.
- La consulta de ítems puede incluir `min_discounted_price`, `max_discounted_price` y `suggested_discounted_price`, calculados por Mercado Libre como referencia para definir el precio.
- Las ofertas pueden exponer `deal_price`, `top_deal_price`, `top_price` y `original_price`. Si `boosted_offer` es true, pueden aparecer `discount_meli_boosted_percentage`, `discount_meli_boost_amount` y `total_price_for_boosted_offer`.
- Un `deal_price` que no cumple el precio sugerido puede producir 400 `ERROR_CREDIBILITY_DISCOUNTED_PRICE`. La guía también enumera errores generales 400, 401, 403, 404, 422, 429 y 500.

**Campos y respuestas:** `promotion_id`, `promotion_type`, `status`, `deal_price`, `top_deal_price`, `top_price`, `original_price`, precios mínimo/máximo/sugerido y campos `boosted_offer`.

**Ejemplos documentados:** consulta de campaña e ítems, alta, modificación y baja de ofertas.

## Operaciones de API

## Conceptos y recursos asociados

### Campañas tradicionales

Documenta campañas tradicionales DEAL organizadas por Mercado Libre para vendedores invitados. El flujo permite consultar la campaña y precios sugeridos, aceptar la invitación con una oferta, ajustarla o retirarla.

**Respuesta**

```json
{
  "fields": "`promotion_id`, `promotion_type`, `status`, `deal_price`, `top_deal_price`, `top_price`, `original_price`, precios mínimo/máximo/sugerido y campos `boosted_offer`."
}
```

**Errores documentados**

- 400 ERROR_CREDIBILITY_DISCOUNTED_PRICE: el precio de descuento no es creíble/no cumple precio sugerido.
- 401 Unauthorized: token inválido o vencido.
- 403 Forbidden: operación sin permiso.
- 404 Not Found: recurso inexistente.
- 422 Unprocessable Entity: datos inválidos o inconsistentes.
- 429 Too Many Requests: límite excedido.
- 500 Internal Server Error: error interno.

**Ejemplos documentados**

- consulta de campaña e ítems, alta, modificación y baja de ofertas.
## Operaciones de API

### Elimina una oferta indicando tipo y campaña

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina una oferta indicando tipo y campaña.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: DEAL
- `promotion_id` (query)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de campaña e ítems, alta, modificación y baja de ofertas.

### Consulta una campaña tradicional DEAL

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta una campaña tradicional DEAL.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: DEAL
- `app_version` (query): Valor mostrado: v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "type",
    "status",
    "start_date",
    "finish_date",
    "deadline_date",
    "name"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de campaña e ítems, alta, modificación y baja de ofertas.

### Lista ítems y precios sugeridos; admite `status_item`

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista ítems y precios sugeridos; admite `status_item`.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `promotion_type` (query): Valor mostrado: DEAL
- `app_version` (query): Valor mostrado: v2
- `status_item` (query): active o paused.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "results",
    "paging",
    "status",
    "offer_id",
    "price",
    "original_price"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta de campaña e ítems, alta, modificación y baja de ofertas.

### Agrega una oferta a la campaña

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega una oferta a la campaña.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: DEAL
- `promotion_id` (query)

**Solicitud**

```json
{
  "fields": [
    "price",
    "top_price",
    "original_price"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400 ERROR_CREDIBILITY_DISCOUNTED_PRICE: el precio no cumple los requisitos de precio sugerido.

**Ejemplos**

- consulta de campaña e ítems, alta, modificación y baja de ofertas.

### Modifica la oferta del ítem

**Método:** `PUT`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica la oferta del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta mostrada por la fuente.
- `app_version` (query): Valor mostrado: v2
- `promotion_type` (query): Valor mostrado: DEAL
- `promotion_id` (query)

**Solicitud**

```json
{
  "fields": [
    "price",
    "top_price",
    "original_price"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400 ERROR_CREDIBILITY_DISCOUNTED_PRICE: el precio no cumple los requisitos de precio sugerido.

**Ejemplos**

- consulta de campaña e ítems, alta, modificación y baja de ofertas.

### Referencia HTTP GET /seller-promotions/items/{ITEM_ID}

**Método:** `GET`  
**Ruta:** `/seller-promotions/items/{ITEM_ID}`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /seller-promotions/items/{ITEM_ID}. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/deals](https://developers.mercadolibre.com.co/es_co/deals)  
**Captura:** 2026-10-08T22:51:12.858Z

---

## [Carga de atributos](../markdown/conoce-como-estan-los-vendedores-frente-la-carga-de-atributos.md)

Actualización indicada por la fuente: 13/11/2023. Captura: 2026-10-08T22:51:13.773Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/conoce-como-estan-los-vendedores-frente-la-carga-de-atributos](https://developers.mercadolibre.com.co/es_co/conoce-como-estan-los-vendedores-frente-la-carga-de-atributos)

# Carga de atributos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/11/2023  
**Captura:** 2026-10-08T22:51:13.773Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/conoce-como-estan-los-vendedores-frente-la-carga-de-atributos](https://developers.mercadolibre.com.co/es_co/conoce-como-estan-los-vendedores-frente-la-carga-de-atributos)

## Resumen

Explica cómo consultar la calidad de carga de atributos de un vendedor o de una publicación. La respuesta presenta el nivel de completitud y las brechas de atributos; para una lectura por publicación se consulta su `item_id`.

## Contenido y conceptos documentados

- La guía diferencia la consulta agregada del vendedor (`seller_id`) y la consulta de completitud/calidad por publicación (`item_id`); el mensaje de validación también menciona `groups` como alternativa.
- `include_items` determina si la respuesta incluye el apartado con granularidad por ítem; su valor predeterminado es `false`. `include_incomplete_items` solicita publicaciones incompletas y `domain_id` filtra un dominio. La versión se indica mediante `v`.
- Se requiere `access_token` al llamar la API. La fuente presenta error 400 si se envía `seller_id` en el caso de consulta por ítem o si falta `item_id`; también indica 403 si `seller_id` no coincide con el vendedor asociado al token.
- La respuesta tiene datos de completitud/calidad y, cuando se solicita, desglose por ítem. Los nombres y niveles se explican en el glosario de la fuente.

**Campos y respuestas:** `seller_id`, `item_id`, `groups`, `include_items`, `include_incomplete_items`, `domain_id`, `v`, `status`, `adoption_status` y `quality_reason`; los demás campos de respuesta se describen en la página.

**Ejemplos documentados:** consulta de estado de vendedor y consulta del estado de una publicación.

## Operaciones de API

## Conceptos y recursos asociados

### Carga de atributos

Explica cómo consultar la calidad de carga de atributos de un vendedor o de una publicación. La respuesta presenta el nivel de completitud y las brechas de atributos; para una lectura por publicación se consulta su `item_id`.

**Respuesta**

```json
{
  "fields": "`seller_id`, `item_id`, `groups`, `include_items`, `include_incomplete_items`, `domain_id`, `v`, `status`, `adoption_status` y `quality_reason`; los demás campos de respuesta se describen en la página."
}
```

**Errores documentados**

- 400: falta una alternativa requerida entre seller_id, item_id o groups.
- 403: seller_id no coincide con el vendedor identificado por access_token.

**Ejemplos documentados**

- consulta de estado de vendedor y consulta del estado de una publicación.
## Operaciones de API

### Consulta calidad/carga agregada por `seller_id` o por publicación con `item_id`; admite `include_items` y `v`

**Método:** `GET`  
**Ruta:** `/catalog_quality/status`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta calidad/carga agregada por `seller_id` o por publicación con `item_id`; admite `include_items` y `v`.

**Parámetros**

- `seller_id` (query): Requerido para la consulta agregada; la fuente también acepta item_id o groups.
- `item_id` (query): Requerido para consulta por publicación; alternativa a seller_id/groups.
- `groups` (query): Alternativa mencionada por el mensaje de validación.
- `include_items` (query): Por defecto false.
- `include_incomplete_items` (query): Incluye publicaciones incompletas.
- `domain_id` (query): Filtro opcional por dominio.
- `v` (query, opcional): Versión opcional recomendada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "status",
    "adoption_status",
    "item_id",
    "quality_reason",
    "quality_level",
    "incomplete_items"
  ]
}
```

**Errores documentados**

- 400: debe proporcionarse seller_id o item_id (la fuente también menciona groups).
- 403: seller_id no coincide con el usuario del access token.

**Ejemplos**

- consulta de estado de vendedor y consulta del estado de una publicación.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/conoce-como-estan-los-vendedores-frente-la-carga-de-atributos](https://developers.mercadolibre.com.co/es_co/conoce-como-estan-los-vendedores-frente-la-carga-de-atributos)  
**Captura:** 2026-10-08T22:51:13.773Z

---

## [Cargar y Obtener Facturas - Emisión Propia](../markdown/cargar-factura.md)

Actualización indicada por la fuente: 16/03/2026. Captura: 2026-10-08T22:51:15.123Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/cargar-factura](https://developers.mercadolibre.com.co/es_co/cargar-factura)

# Cargar y Obtener Facturas - Emisión Propia

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 16/03/2026  
**Captura:** 2026-10-08T22:51:15.123Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/cargar-factura](https://developers.mercadolibre.com.co/es_co/cargar-factura)

## Resumen

Documenta la carga, consulta y eliminación de facturas fiscales asociadas a un pack/orden. La integración permite adjuntar archivos, recuperar sus identificadores y descargar el documento asociado.

## Contenido y conceptos documentados

- La carga utiliza el recurso del pack; si `pack_id` es nulo, la guía indica usar el `order_id` como valor, conservando el recurso `/packs`.
- Se documentan facturas en PDF y XML (`application/pdf`, `application/xml`, `text/xml`). La página describe validaciones de autorización, tipo, tamaño, archivo vacío, cantidad de adjuntos y modalidad de envío.
- La respuesta de carga entrega una lista `ids`; cada identificador se usa para consultar un documento. También se documenta consultar los IDs asociados y eliminar facturas del pack.
- Códigos mostrados en las respuestas: 400 por archivo/datos vacíos o inválidos; 403 por autorización/acceso; 404 por pack o documento inexistente; 406 por texto de consulta no aceptable; 409 por conflicto con archivos ya adjuntos; 500 al recuperar el body de una solicitud de datos fiscales.

**Campos y respuestas:** `pack_id`, `fiscal_document_id` y respuesta de carga `ids`.

**Ejemplos documentados:** carga de factura, consulta de IDs, descarga de factura y eliminación del documento del pack.

## Operaciones de API

## Conceptos y recursos asociados

### Cargar y Obtener Facturas - Emisión Propia

Documenta la carga, consulta y eliminación de facturas fiscales asociadas a un pack/orden. La integración permite adjuntar archivos, recuperar sus identificadores y descargar el documento asociado.

**Respuesta**

```json
{
  "fields": "`pack_id`, `fiscal_document_id` y respuesta de carga `ids`."
}
```

**Errores documentados**

- 400: archivo/datos vacíos o inválidos.
- 403: autorización/acceso denegados.
- 404: pack o documento inexistente.
- 406: texto de consulta no aceptable.
- 409: conflicto con archivos ya adjuntos.
- 500: error al recuperar el body en solicitud de datos fiscales.

**Ejemplos documentados**

- carga de factura, consulta de IDs, descarga de factura y eliminación del documento del pack.
### Ruta mencionada /orders/

La fuente menciona la ruta /orders/, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/orders/`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Elimina facturas asociadas al pack

**Método:** `DELETE`  
**Ruta:** `/packs/{pack_id}/fiscal_documents`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina facturas asociadas al pack.

**Parámetros**

- `pack_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 403: usuario no autorizado.
- 404: el pack no tiene factura adjunta.

**Ejemplos**

- carga de factura, consulta de IDs, descarga de factura y eliminación del documento del pack.

### Obtiene los IDs de las facturas asociadas

**Método:** `GET`  
**Ruta:** `/packs/{pack_id}/fiscal_documents`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los IDs de las facturas asociadas.

**Parámetros**

- `pack_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "ids"
  ]
}
```

**Errores documentados**

- 403: usuario no autorizado.
- 404: pack sin documentos o sin factura del usuario.

**Ejemplos**

- carga de factura, consulta de IDs, descarga de factura y eliminación del documento del pack.

### Recupera una factura específica

**Método:** `GET`  
**Ruta:** `/packs/{pack_id}/fiscal_documents/{fiscal_document_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera una factura específica.

**Parámetros**

- `pack_id` (path, obligatorio): Variable de ruta documentada.
- `fiscal_document_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: identificador de documento inexistente.
- 403: usuario no autorizado.
- 404: documento no recuperable del almacenamiento.

**Ejemplos**

- carga de factura, consulta de IDs, descarga de factura y eliminación del documento del pack.

### Adjunta factura(s) al pack

**Método:** `POST`  
**Ruta:** `/packs/{pack_id}/fiscal_documents`  
**Autenticación:** No documentado en la fuente.

Adjunta factura(s) al pack.

**Parámetros**

- `pack_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

```json
{
  "content_types": [
    "application/pdf",
    "application/xml",
    "text/xml"
  ],
  "note": "Adjunto fiscal; nombre y límite exacto dependen de las validaciones descritas."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: archivo vacío, tipo/tamaño/nombre no válido.
- 403: falta de autorización o sitio no habilitado.
- 409: ya existe adjunto o se excede cantidad por tipo.

**Ejemplos**

- carga de factura, consulta de IDs, descarga de factura y eliminación del documento del pack.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/cargar-factura](https://developers.mercadolibre.com.co/es_co/cargar-factura)  
**Captura:** 2026-10-08T22:51:15.123Z

---

## [Categorización de productos](../markdown/categoriza-productos.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:51:18.330Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/categoriza-productos](https://developers.mercadolibre.com.co/es_co/categoriza-productos)

# Categorización de productos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:51:18.330Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/categoriza-productos](https://developers.mercadolibre.com.co/es_co/categoriza-productos)

## Resumen

Describe cómo identificar el dominio/categoría más adecuado para un producto y consultar la taxonomía de un sitio. Incluye predicción por texto, conversión de dominio a categorías y consulta de categorías y su ruta desde la raíz.

## Contenido y conceptos documentados

- El predictor requiere `site_id` y `q`; el texto debe estar en el idioma del sitio. `limit` es opcional (por defecto 4, máximo 8) y `target` puede ser `core` o `classified`.
- Para mapear un dominio de catálogo a categorías se consulta `catalog_domains/{domain_id}/categories`; para recorrer la taxonomía del sitio se obtienen sus categorías y luego el detalle por `category_id`.
- La respuesta de categorías incluye `id` y `name`; la página también muestra datos de atributos y restricciones, por ejemplo `max_description_length`.
- Un error documentado para variaciones es 400 cuando se supera el máximo permitido de 100.

**Campos y respuestas:** `site_id`, `q`, `limit`, `target`, `domain_id`, `domain_name`, `category_id`, `category_name`, `attributes`, `id`, `name` y, en los datos de categoría, `max_description_length`.

**Ejemplos documentados:** predicción de dominio para una búsqueda de celulares, categorías por dominio, categorías del sitio y detalle de categoría.

## Operaciones de API

## Conceptos y recursos asociados

### Categorización de productos

Describe cómo identificar el dominio/categoría más adecuado para un producto y consultar la taxonomía de un sitio. Incluye predicción por texto, conversión de dominio a categorías y consulta de categorías y su ruta desde la raíz.

**Respuesta**

```json
{
  "fields": "`site_id`, `q`, `limit`, `target`, `domain_id`, `domain_name`, `category_id`, `category_name`, `attributes`, `id`, `name` y, en los datos de categoría, `max_description_length`."
}
```

**Errores documentados**

- 400: las variaciones no deben superar el máximo de 100.

**Ejemplos documentados**

- predicción de dominio para una búsqueda de celulares, categorías por dominio, categorías del sitio y detalle de categoría.
## Operaciones de API

### Consulta categorías asociadas a un dominio de catálogo

**Método:** `GET`  
**Ruta:** `/catalog_domains/{domain_id}/categories`  
**Autenticación:** No documentado en la fuente.

Consulta categorías asociadas a un dominio de catálogo.

**Parámetros**

- `domain_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "name"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- predicción de dominio para una búsqueda de celulares, categorías por dominio, categorías del sitio y detalle de categoría.

### Consulta detalle de una categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalle de una categoría.

**Parámetros**

- `category_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- predicción de dominio para una búsqueda de celulares, categorías por dominio, categorías del sitio y detalle de categoría.

### Lista categorías de un sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/categories`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista categorías de un sitio.

**Parámetros**

- `site_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- predicción de dominio para una búsqueda de celulares, categorías por dominio, categorías del sitio y detalle de categoría.

### Predice dominios a partir de una búsqueda `q`; admite `limit`

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/domain_discovery/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Predice dominios a partir de una búsqueda `q`; admite `limit`.

**Parámetros**

- `site_id` (path, obligatorio): Sitio donde se realiza la publicación.
- `q` (query, obligatorio): Título a predecir; debe estar en el idioma del sitio.
- `limit` (query, opcional): Por defecto 4; máximo 8.
- `target` (query, opcional): Puede ser core o classified.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "domain_id",
    "domain_name",
    "category_id",
    "category_name",
    "attributes"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- predicción de dominio para una búsqueda de celulares, categorías por dominio, categorías del sitio y detalle de categoría.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/categoriza-productos](https://developers.mercadolibre.com.co/es_co/categoriza-productos)  
**Captura:** 2026-10-08T22:51:18.330Z

---

## [Catálogo reacondicionados](../markdown/catalogo-reacondicionados.md)

Actualización indicada por la fuente: 29/12/2025. Captura: 2026-10-08T22:51:16.468Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/catalogo-reacondicionados](https://developers.mercadolibre.com.co/es_co/catalogo-reacondicionados)

# Catálogo reacondicionados

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:51:16.468Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/catalogo-reacondicionados](https://developers.mercadolibre.com.co/es_co/catalogo-reacondicionados)

## Resumen

Documenta la publicación de productos reacondicionados en catálogo. La condición y el grado de reacondicionamiento se expresan en atributos; el grado determina la elegibilidad y la asociación con la página de producto reacondicionado.

## Contenido y conceptos documentados

- `ITEM_CONDITION` debe indicar `refurbished` (reacondicionado). El atributo obligatorio `GRADING` admite `Excelente`, `Bueno` o `Aceptable` según la fuente.
- Sin `GRADING`, el ítem no es elegible para catálogo. Tras agregarlo, se debe consultar nuevamente la elegibilidad.
- Para publicar, la guía indica enviar `catalog_product_id` (PDP tradicional) y `catalog_listing: true`; también menciona la publicación mediante `/items/catalog_listings`.
- Los campos `picker_id` y `attribute_id` identifican `GRADING` en los ejemplos.

**Campos y respuestas:** `ITEM_CONDITION`, `GRADING`, `catalog_product_id`, `catalog_listing`, `picker_id` y `attribute_id`.

**Ejemplos documentados:** valores de grado y solicitud de publicación en catálogo reacondicionado.

## Operaciones de API

## Conceptos y recursos asociados

### Catálogo reacondicionados

Documenta la publicación de productos reacondicionados en catálogo. La condición y el grado de reacondicionamiento se expresan en atributos; el grado determina la elegibilidad y la asociación con la página de producto reacondicionado.

**Respuesta**

```json
{
  "fields": "`ITEM_CONDITION`, `GRADING`, `catalog_product_id`, `catalog_listing`, `picker_id` y `attribute_id`."
}
```

**Ejemplos documentados**

- valores de grado y solicitud de publicación en catálogo reacondicionado.
### Ruta mencionada /products/search

La fuente menciona la ruta /products/search, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/products/search`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Crea el ítem de catálogo con `catalog_product_id` y `catalog_listing: true`

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** No documentado en la fuente.

Crea el ítem de catálogo con `catalog_product_id` y `catalog_listing: true`.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "ITEM_CONDITION",
    "GRADING",
    "catalog_product_id",
    "catalog_listing"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- valores de grado y solicitud de publicación en catálogo reacondicionado.

### Publica el ítem reacondicionado en catálogo

**Método:** `POST`  
**Ruta:** `/items/catalog_listings`  
**Autenticación:** No documentado en la fuente.

Publica el ítem reacondicionado en catálogo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "catalog_product_id",
    "GRADING"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "id",
    "status"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- valores de grado y solicitud de publicación en catálogo reacondicionado.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/catalogo-reacondicionados](https://developers.mercadolibre.com.co/es_co/catalogo-reacondicionados)  
**Captura:** 2026-10-08T22:51:16.468Z

---

## [Co-fondeada automatizada y precios competitivos](../markdown/campanas-smart-price-matching.md)

Actualización indicada por la fuente: 09/06/2026. Captura: 2026-10-08T22:51:19.909Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/campanas-smart-price-matching](https://developers.mercadolibre.com.co/es_co/campanas-smart-price-matching)

# Co-fondeada automatizada y precios competitivos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 09/06/2026  
**Captura:** 2026-10-08T22:51:19.909Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/campanas-smart-price-matching](https://developers.mercadolibre.com.co/es_co/campanas-smart-price-matching)

## Resumen

Explica la gestión de campañas automatizadas y de precios competitivos: SMART, PRICE_MATCHING y PRICE_MATCHING_MELI_ALL. Permite consultar campañas e ítems, incorporar ofertas y retirarlas, e identificar descuentos adicionales aplicados por Mercado Libre.

## Contenido y conceptos documentados

- Los ejemplos usan `promotion_type` para diferenciar los tipos de campaña y `app_version=v2`. Las campañas pueden ser cofinanciadas o financiadas al 100 % por Mercado Libre, según el tipo.
- En los ítems, `status_item` filtra `active` o `paused`; los estados de oferta incluyen `candidate` y ofertas activas. La oferta contiene `offer_id`, `price` y `original_price`.
- Si `boosted_offer` es `true`, la respuesta puede incluir `discount_meli_boosted_percentage`, `discount_meli_boost_amount` y `total_price_for_boosted_offer`.
- La fuente muestra respuestas 200 OK al retirar ofertas.

**Campos y respuestas:** `promotion_id`, `promotion_type`, `status`, `offer_id`, `price`, `original_price`, `boosted_offer`, `discount_meli_boosted_percentage`, `discount_meli_boost_amount` y `total_price_for_boosted_offer`.

**Ejemplos documentados:** detalle e ítems para los tres tipos; alta y eliminación de ofertas.

## Operaciones de API

## Conceptos y recursos asociados

### Co-fondeada automatizada y precios competitivos

Explica la gestión de campañas automatizadas y de precios competitivos: SMART, PRICE_MATCHING y PRICE_MATCHING_MELI_ALL. Permite consultar campañas e ítems, incorporar ofertas y retirarlas, e identificar descuentos adicionales aplicados por Mercado Libre.

**Respuesta**

```json
{
  "fields": "`promotion_id`, `promotion_type`, `status`, `offer_id`, `price`, `original_price`, `boosted_offer`, `discount_meli_boosted_percentage`, `discount_meli_boost_amount` y `total_price_for_boosted_offer`."
}
```

**Ejemplos documentados**

- detalle e ítems para los tres tipos; alta y eliminación de ofertas.
## Operaciones de API

### Retira la oferta usando tipo, campaña y `offer_id`

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Retira la oferta usando tipo, campaña y `offer_id`.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `app_version` (query): La guía muestra v2.
- `promotion_type` (query): Tipo de campaña indicado en cada ejemplo.
- `promotion_id` (query): Identificador de campaña.
- `offer_id` (query): Identificador de oferta.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- detalle e ítems para los tres tipos; alta y eliminación de ofertas.

### Consulta la oferta de un ítem

**Método:** `GET`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la oferta de un ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `app_version` (query): La guía muestra v2.
- `promotion_type` (query): Tipo de campaña indicado en cada ejemplo.
- `promotion_id` (query): Identificador de campaña.
- `offer_id` (query): Identificador de oferta.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "type",
    "sub_type",
    "status",
    "start_date",
    "finish_date",
    "deadline_date",
    "name",
    "offer_id",
    "price",
    "original_price"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- detalle e ítems para los tres tipos; alta y eliminación de ofertas.

### Consulta detalle de campaña SMART o PRICE_MATCHING

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalle de campaña SMART o PRICE_MATCHING.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta documentada.
- `promotion_type` (query): Tipo de campaña indicado en cada ejemplo.
- `app_version` (query): La guía muestra v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "type",
    "sub_type",
    "status",
    "start_date",
    "finish_date",
    "deadline_date",
    "name",
    "offer_id",
    "price",
    "original_price"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- detalle e ítems para los tres tipos; alta y eliminación de ofertas.

### Lista ítems asociados a la campaña

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{promotion_id}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista ítems asociados a la campaña.

**Parámetros**

- `promotion_id` (path, obligatorio): Variable de ruta documentada.
- `promotion_type` (query): Tipo de campaña indicado en cada ejemplo.
- `app_version` (query): La guía muestra v2.
- `status_item` (query): Filtro active o paused.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "type",
    "sub_type",
    "status",
    "start_date",
    "finish_date",
    "deadline_date",
    "name",
    "offer_id",
    "price",
    "original_price"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- detalle e ítems para los tres tipos; alta y eliminación de ofertas.

### Agrega una oferta a la campaña

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega una oferta a la campaña.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `app_version` (query): La guía muestra v2.
- `promotion_type` (query): Tipo de campaña indicado en cada ejemplo.
- `promotion_id` (query): Identificador de campaña.
- `offer_id` (query): Identificador de oferta.

**Solicitud**

```json
{
  "fields": [
    "price"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- detalle e ítems para los tres tipos; alta y eliminación de ofertas.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/campanas-smart-price-matching](https://developers.mercadolibre.com.co/es_co/campanas-smart-price-matching)  
**Captura:** 2026-10-08T22:51:19.909Z

---

## [Compatibilidades entre ítems y productos de Autopartes](../markdown/compatibilidades-entre-items-y-productos.md)

Actualización indicada por la fuente: 14/07/2026. Captura: 2026-10-08T22:51:21.176Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/compatibilidades-entre-items-y-productos](https://developers.mercadolibre.com.co/es_co/compatibilidades-entre-items-y-productos)

# Compatibilidades entre ítems y productos de Autopartes

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 14/07/2026  
**Captura:** 2026-10-08T22:51:21.176Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/compatibilidades-entre-items-y-productos](https://developers.mercadolibre.com.co/es_co/compatibilidades-entre-items-y-productos)

## Resumen

Reúne las operaciones para buscar, consultar, agregar, copiar y eliminar compatibilidades entre ítems/User Products y productos de autopartes. Distingue compatibilidades del vendedor (`SELLER`) de las generadas por catálogo (`CATALOGO`), con restricciones específicas de lectura y escritura para cada origen.

## Contenido y conceptos documentados

- Las compatibilidades pueden incluir dominios, productos, notas y restricciones de posición. `source` diferencia `SELLER` y `CATALOGO`; `restrictions_required` indica si se deben informar posiciones.
- La lectura extendida expone información adicional. Para compatibilidades de catálogo, el detalle por ID no está disponible y la fuente indica que `id` y `catalog_product_id` pueden ser `null`.
- DELETE solo permite eliminar compatibilidades `SELLER`; las de catálogo se gestionan desde Mercado Libre. Desde el 15/07/2026, copiar y pegar desde User Product excluye compatibilidades `CATALOGO`.
- Las operaciones POST/PUT pueden guardar hasta 200 compatibilidades sincrónicamente y procesar el resto de forma asíncrona. Una compatibilidad universal no admite enviar simultáneamente productos/familias.
- La fuente informa límites de 100 RPM por APP_ID para el conteo de productos por familia. Errores de compatibilidad incluyen 400 por validación/formato, 403 por token/permisos y 404 por ítem, compatibilidad, producto o dominio inexistente. Para snapshots: 400 orden no encontrada, 401 token inválido y 403 orden sin reclamo o seller distinto.
- También se documentan excepciones de compatibilidad, conteo de sugerencias/reclamos, snapshots de compatibilidad de órdenes y búsqueda de vehículos agregados al catálogo.

**Campos y respuestas:** `source`, `id`, `catalog_product_id`, `restrictions_required`, `extended_information`, `item_to_copy`, `note`, `restrictions`, `created_compatibilities_count`, `reason_id`, `compatibilities_count`, `compatibilities_claims_count`, `notes_count`, `restrictions_count` y filtros `tags`.

**Ejemplos documentados:** consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

## Operaciones de API

## Conceptos y recursos asociados

### Compatibilidades entre ítems y productos de Autopartes

Reúne las operaciones para buscar, consultar, agregar, copiar y eliminar compatibilidades entre ítems/User Products y productos de autopartes. Distingue compatibilidades del vendedor (`SELLER`) de las generadas por catálogo (`CATALOGO`), con restricciones específicas de lectura y escritura para cada origen.

**Respuesta**

```json
{
  "fields": "`source`, `id`, `catalog_product_id`, `restrictions_required`, `extended_information`, `item_to_copy`, `note`, `restrictions`, `created_compatibilities_count`, `reason_id`, `compatibilities_count`, `compatibilities_claims_count`, `notes_count`, `restrictions_count` y filtros `tags`."
}
```

**Errores documentados**

- 400: validaciones de consistencia/formato y límites.
- 401: token inválido para consulta de snapshot.
- 403: token/permisos, orden sin claim o seller distinto.
- 404: ítem, producto, dominio o compatibilidad inexistente.

**Ejemplos documentados**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.
## Operaciones de API

### Elimina compatibilidades SELLER del ítem

**Método:** `DELETE`  
**Ruta:** `/items/{item_id}/compatibilities`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina compatibilidades SELLER del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `extended` (query): La lectura extendida incluye información adicional.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Elimina una compatibilidad SELLER por ID

**Método:** `DELETE`  
**Ruta:** `/items/{item_id}/compatibilities/{compatibility_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina una compatibilidad SELLER por ID.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `compatibility_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Elimina compatibilidades del User Product

**Método:** `DELETE`  
**Ruta:** `/user-products/{up_id}/compatibilities`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina compatibilidades del User Product.

**Parámetros**

- `up_id` (path, obligatorio): Variable de ruta documentada.
- `main_domain_id` (query): Dominio principal de compatibilidad.
- `extended` (query): La lectura extendida incluye información adicional.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Busca productos/vehículos nuevos añadidos al catálogo por `categoryId`

**Método:** `GET`  
**Ruta:** `/catalog_compatibilities/products_search/new`  
**Autenticación:** No documentado en la fuente.

Busca productos/vehículos nuevos añadidos al catálogo por `categoryId`.

**Parámetros**

- `categoryId` (query): Categoría de catálogo.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Obtiene valores de restricciones para dominios principal y secundario

**Método:** `GET`  
**Ruta:** `/catalog_compatibilities/restrictions/values`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene valores de restricciones para dominios principal y secundario.

**Parámetros**

- `main_domain_id` (query): Dominio principal de compatibilidad.
- `secondary_domain_id` (query): Dominio secundario de compatibilidad.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Descarga compatibilidades de catálogo por sitio

**Método:** `GET`  
**Ruta:** `/catalog/dumps/domains/{site_id}/compatibilities`  
**Autenticación:** No documentado en la fuente.

Descarga compatibilidades de catálogo por sitio.

**Parámetros**

- `site_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Consulta el vehículo elegido por el comprador para una orden

**Método:** `GET`  
**Ruta:** `/compats-snapshots/orders/{order_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el vehículo elegido por el comprador para una orden.

**Parámetros**

- `order_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: snapshot no encontrado para la orden.
- 401: token inválido.
- 403: la orden no tiene claim o el caller no es el seller de la publicación.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Consulta datos del ítem usados por el flujo de compatibilidades

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta datos del ítem usados por el flujo de compatibilidades.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Lista compatibilidades; admite `extended=true`

**Método:** `GET`  
**Ruta:** `/items/{item_id}/compatibilities`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista compatibilidades; admite `extended=true`.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `extended` (query): La lectura extendida incluye información adicional.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Consulta detalle por ID, sujeto a las limitaciones de origen de catálogo

**Método:** `GET`  
**Ruta:** `/items/{item_id}/compatibilities/{compatibility_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalle por ID, sujeto a las limitaciones de origen de catálogo.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `compatibility_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Consulta la nota de una compatibilidad

**Método:** `GET`  
**Ruta:** `/items/{item_id}/compatibilities/{compatibility_id}/note`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la nota de una compatibilidad.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `compatibility_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Consulta la excepción del ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}/compatibilities/exception`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la excepción del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Lista compatibilidades; admite `main_domain_id` y `extended=true`

**Método:** `GET`  
**Ruta:** `/user-products/{up_id}/compatibilities`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista compatibilidades; admite `main_domain_id` y `extended=true`.

**Parámetros**

- `up_id` (path, obligatorio): Variable de ruta documentada.
- `main_domain_id` (query): Dominio principal de compatibilidad.
- `extended` (query): La lectura extendida incluye información adicional.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Consulta la excepción del User Product

**Método:** `GET`  
**Ruta:** `/user-products/{user_product_id}/compatibilities/exception`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la excepción del User Product.

**Parámetros**

- `user_product_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Busca publicaciones por `tags` o por estado y presencia de compatibilidades

**Método:** `GET`  
**Ruta:** `/users/{seller_id}/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca publicaciones por `tags` o por estado y presencia de compatibilidades.

**Parámetros**

- `seller_id` (path, obligatorio): Variable de ruta documentada.
- `tags` (query): Filtro por tipo/estado de compatibilidad.
- `status` (query): Estado de publicación.
- `has_compatibilities` (query): Filtra publicaciones con compatibilidades.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Busca reclamos por incompatibilidad mediante `reason_id`

**Método:** `GET`  
**Ruta:** `/v1/claims/search`  
**Autenticación:** No documentado en la fuente.

Busca reclamos por incompatibilidad mediante `reason_id`.

**Parámetros**

- `reason_id` (query): Identificador de motivo de reclamo.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Cuenta productos de una familia que cumplen atributos

**Método:** `POST`  
**Ruta:** `/catalog_compatibilities/products_search/count_family_products`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cuenta productos de una familia que cumplen atributos.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Consulta/genera tarjetas de compatibilidades para el dominio

**Método:** `POST`  
**Ruta:** `/items/catalog_domains/{domain_id}/compatibilities/cards`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta/genera tarjetas de compatibilidades para el dominio.

**Parámetros**

- `domain_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

```json
{
  "fields": [
    "item_id",
    "filters",
    "product_id (opcional)"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "title",
    "subtitle",
    "filter",
    "quantity"
  ]
}
```

**Errores documentados**

- 400: validaciones de consistencia.
- 403: token/permisos.
- 404: ítem/producto/dominio inexistente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Obtiene resumen de sugerencias/reclamos de compatibilidad

**Método:** `POST`  
**Ruta:** `/items/compatibilities_summary`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene resumen de sugerencias/reclamos de compatibilidad.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "domain_id",
    "items"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "item_id",
    "item_title",
    "compatibilities_count",
    "compatibilities_claims_count",
    "notes_count",
    "restrictions_count"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Agrega compatibilidades a un ítem

**Método:** `POST`  
**Ruta:** `/items/{item_id}/compatibilities`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega compatibilidades a un ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `extended` (query): La lectura extendida incluye información adicional.

**Solicitud**

```json
{
  "fields": [
    "compatibilities, item_to_copy, extended_information, note, restrictions"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Registra una excepción para el ítem

**Método:** `POST`  
**Ruta:** `/items/{item_id}/compatibilities/exception`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Registra una excepción para el ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

```json
{
  "fields": [
    "comment"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Agrega compatibilidades a un User Product

**Método:** `POST`  
**Ruta:** `/user-products/{up_id}/compatibilities`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega compatibilidades a un User Product.

**Parámetros**

- `up_id` (path, obligatorio): Variable de ruta documentada.
- `main_domain_id` (query): Dominio principal de compatibilidad.
- `extended` (query): La lectura extendida incluye información adicional.

**Solicitud**

```json
{
  "fields": [
    "compatibilities, item_to_copy, extended_information, note, restrictions"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Copia compatibilidades entre User Products/ítems

**Método:** `POST`  
**Ruta:** `/user-products/{up_id}/compatibilities/copy-paste`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Copia compatibilidades entre User Products/ítems.

**Parámetros**

- `up_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

```json
{
  "fields": [
    "item_to_copy, extended_information"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Registra una excepción para el User Product

**Método:** `POST`  
**Ruta:** `/user-products/{user_product_id}/compatibilities/exception`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Registra una excepción para el User Product.

**Parámetros**

- `user_product_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

```json
{
  "fields": [
    "comment"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Crea, actualiza o elimina entradas; la acción debe indicarse explícitamente

**Método:** `PUT`  
**Ruta:** `/items/{item_id}/compatibilities`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea, actualiza o elimina entradas; la acción debe indicarse explícitamente.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `extended` (query): La lectura extendida incluye información adicional.

**Solicitud**

```json
{
  "fields": [
    "create/update/delete, item_to_copy, extended_information, note, restrictions"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Actualiza compatibilidades de un User Product

**Método:** `PUT`  
**Ruta:** `/user-products/{up_id}/compatibilities`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza compatibilidades de un User Product.

**Parámetros**

- `up_id` (path, obligatorio): Variable de ruta documentada.
- `main_domain_id` (query): Dominio principal de compatibilidad.
- `extended` (query): La lectura extendida incluye información adicional.

**Solicitud**

```json
{
  "fields": [
    "item_to_copy, extended_information, note, restrictions"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- consulta paginada/extendida, alta y actualización de compatibilidades, copia entre ítems/User Products, excepciones y consultas de snapshots.

### Referencia HTTP POST /catalog_domains/MLB-CARS_AND_VANS/compatibilities/cards

**Método:** `POST`  
**Ruta:** `/catalog_domains/MLB-CARS_AND_VANS/compatibilities/cards`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /catalog_domains/MLB-CARS_AND_VANS/compatibilities/cards. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/compatibilidades-entre-items-y-productos](https://developers.mercadolibre.com.co/es_co/compatibilidades-entre-items-y-productos)  
**Captura:** 2026-10-08T22:51:21.176Z

---

## [Competencia](../markdown/competencia-en-catalogo.md)

Actualización indicada por la fuente: 21/07/2026. Captura: 2026-10-08T22:51:22.908Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/competencia-en-catalogo](https://developers.mercadolibre.com.co/es_co/competencia-en-catalogo)

# Competencia

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 21/07/2026  
**Captura:** 2026-10-08T22:51:22.908Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/competencia-en-catalogo](https://developers.mercadolibre.com.co/es_co/competencia-en-catalogo)

## Resumen

Describe cómo consultar la posición competitiva de una publicación en una página de producto de catálogo y el precio sugerido para competir. La respuesta identifica estados, motivos y datos de la publicación ganadora.

## Contenido y conceptos documentados

- La consulta se realiza por `item_id`; la guía muestra `version=v2`.
- Los estados ejemplificados incluyen `winning`, `competing`, `sharing_first_place` y `listed`. `boosts` describe oportunidades/beneficios; cada boost puede tener estado `boosted`, `not_boosted`, `opportunity` o `not_apply`.
- `price_to_win` expresa el precio sugerido en la moneda de la publicación. La fuente señala que al actualizar el precio del ítem con ese valor, la publicación puede ser más competitiva.
- La respuesta también puede identificar `catalog_product_id` y datos acotados de la publicación ganadora. La página menciona notificaciones ante cambios de estado.

**Campos y respuestas:** `item_id`, `current_price`, `currency_id`, `price_to_win`, `boosts`, `status`, `consistent`, `visit_share`, `competitors_sharing_first_place`, `reason`, `catalog_product_id` y `winner`.

**Ejemplos documentados:** publicación perdiendo/ganando, compartiendo el primer lugar y publicación listada sin competir.

## Operaciones de API

## Conceptos y recursos asociados

### Competencia

Describe cómo consultar la posición competitiva de una publicación en una página de producto de catálogo y el precio sugerido para competir. La respuesta identifica estados, motivos y datos de la publicación ganadora.

**Respuesta**

```json
{
  "fields": "`item_id`, `current_price`, `currency_id`, `price_to_win`, `boosts`, `status`, `consistent`, `visit_share`, `competitors_sharing_first_place`, `reason`, `catalog_product_id` y `winner`."
}
```

**Ejemplos documentados**

- publicación perdiendo/ganando, compartiendo el primer lugar y publicación listada sin competir.
### Ruta mencionada /products/{product_id}

La fuente menciona la ruta /products/{product_id}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/products/{product_id}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consulta el estado competitivo, las razones y el precio sugerido; la guía muestra `version=v2`

**Método:** `GET`  
**Ruta:** `/items/{item_id}/price_to_win`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el estado competitivo, las razones y el precio sugerido; la guía muestra `version=v2`.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `version` (query): La guía muestra version=v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "item_id",
    "current_price",
    "currency_id",
    "price_to_win",
    "boosts",
    "status",
    "consistent",
    "visit_share",
    "competitors_sharing_first_place",
    "reason",
    "catalog_product_id",
    "winner"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- publicación perdiendo/ganando, compartiendo el primer lugar y publicación listada sin competir.

### Aplicar el precio sugerido

**Método:** `PUT`  
**Ruta:** `/items`  
**Autenticación:** No documentado en la fuente.

La fuente indica enviar el precio sugerido mediante PUT al recurso /items para mejorar la competitividad; la ruta detallada no está especificada.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente lo describe como el paso posterior a consultar price_to_win.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/competencia-en-catalogo](https://developers.mercadolibre.com.co/es_co/competencia-en-catalogo)  
**Captura:** 2026-10-08T22:51:22.908Z

---

## [Convivencia Full/Flex (MLA y MLC)](../markdown/convivencia-full-y-flex.md)

Actualización indicada por la fuente: 15/05/2026. Captura: 2026-10-08T22:51:24.144Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/convivencia-full-y-flex](https://developers.mercadolibre.com.co/es_co/convivencia-full-y-flex)

# Convivencia Full/Flex (MLA y MLC)

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 15/05/2026  
**Captura:** 2026-10-08T22:51:24.144Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/convivencia-full-y-flex](https://developers.mercadolibre.com.co/es_co/convivencia-full-y-flex)

## Resumen

Explica la lectura y modificación de stock para User Products en convivencia Full/Flex en MLA y MLC. La modificación depende de la versión de la entidad devuelta en el encabezado `x-version`.

## Contenido y conceptos documentados

- La consulta de stock tiene un límite indicado de 100 RPM.
- La lectura devuelve el encabezado `x-version`; debe enviarse en el PUT de actualización. Si falta, la fuente indica 400; si ya no es la versión más reciente, indica 409.
- La ruta `selling_address` no es válida en algunos escenarios de fulfillment/stock. Para vendedores con un único depósito tipo seller warehouse, la recomendación es operar con `seller_warehouse`.
- La guía enumera errores 400 por ausencia de inventario, falta de stock fulfillment, necesidad de inbound previo, falta de `x-version` y configuración de depósito único.

**Campos y respuestas:** identificador User Product, tipo de stock y encabezado `x-version`.

**Ejemplos documentados:** lectura de stock y actualización del stock `selling_address`.

## Operaciones de API

## Conceptos y recursos asociados

### Convivencia Full/Flex (MLA y MLC)

Explica la lectura y modificación de stock para User Products en convivencia Full/Flex en MLA y MLC. La modificación depende de la versión de la entidad devuelta en el encabezado `x-version`.

**Respuesta**

```json
{
  "fields": "identificador User Product, tipo de stock y encabezado `x-version`."
}
```

**Errores documentados**

- 400: no se puede actualizar selling_address en los escenarios descritos o falta X-Version.
- 409: la versión enviada no es la más reciente.

**Ejemplos documentados**

- lectura de stock y actualización del stock `selling_address`.
### Ruta mencionada /user-product

La fuente menciona la ruta /user-product, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/user-product`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consulta stock; la respuesta incluye `x-version`

**Método:** `GET`  
**Ruta:** `/user-products/{user_product_id}/stock`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta stock; la respuesta incluye `x-version`.

**Parámetros**

- `user_product_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "x-version"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- lectura de stock y actualización del stock `selling_address`.

### Ruta recomendada para gestionar stock de seller warehouse en la condición descrita

**Método:** `PUT`  
**Ruta:** `/user-products/{id}/stock/type/seller_warehouse`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Ruta recomendada para gestionar stock de seller warehouse en la condición descrita.

**Parámetros**

- `id` (path, obligatorio): Variable de ruta documentada.
- `x-version` (header, obligatorio): Versión devuelta por la consulta GET de stock.

**Solicitud**

```json
{
  "fields": [
    "x-version header",
    "stock"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: falta x-version o no puede modificarse ese tipo de stock.
- 409: x-version no es la versión más reciente.

**Ejemplos**

- lectura de stock y actualización del stock `selling_address`.

### Actualiza stock de dirección de venta y requiere `x-version`

**Método:** `PUT`  
**Ruta:** `/user-products/{user_product_id}/stock/type/selling_address`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza stock de dirección de venta y requiere `x-version`.

**Parámetros**

- `user_product_id` (path, obligatorio): Variable de ruta documentada.
- `x-version` (header, obligatorio): Versión devuelta por la consulta GET de stock.

**Solicitud**

```json
{
  "fields": [
    "x-version header",
    "stock"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: falta x-version o no puede modificarse ese tipo de stock.
- 409: x-version no es la versión más reciente.

**Ejemplos**

- lectura de stock y actualización del stock `selling_address`.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/convivencia-full-y-flex](https://developers.mercadolibre.com.co/es_co/convivencia-full-y-flex)  
**Captura:** 2026-10-08T22:51:24.144Z

---

## [Costos de envío](../markdown/costos-de-envios.md)

Actualización indicada por la fuente: 13/02/2026. Captura: 2026-10-08T22:51:25.439Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/costos-de-envios](https://developers.mercadolibre.com.co/es_co/costos-de-envios)

# Costos de envío

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/02/2026  
**Captura:** 2026-10-08T22:51:25.439Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/costos-de-envios](https://developers.mercadolibre.com.co/es_co/costos-de-envios)

## Resumen

Documenta la información de envío para publicar/editar un ítem y las opciones/costos estimados durante la compra. Distingue la obligación de envío gratis de la simulación de costo y permite cotizar el destino por código postal o ciudad.

## Contenido y conceptos documentados

- Para publicación/edición, consulta el ítem y revisa `shipping.free_shipping` y `mandatory_free_shipping`; si este último aparece, la condición es obligatoria.
- La cotización previa de costo usa `/users/{user_id}/shipping_options/free`. La fuente exige al menos uno de `item_id` o `dimensions`; acepta además precio, tipo de publicación, modalidad, condición, logística y opción de envío gratis.
- La cotización es aproximada, considera una sola unidad y aplica a ítems disponibles en Marketplace. Se describen tipos logísticos como `cross_docking`, `drop_off`, `fulfillment`, `xd_drop_off` y `self_service`.
- Para la etapa de compra, `/items/{item_id}/shipping_options` consulta opciones adaptadas al destino mediante `zip_code` o `city_to`.
- Errores documentados incluyen 400 por `seller_id` o código postal inválido, 403 por error/ítem inválido y 404 por ítem o área de cobertura no encontrada.

**Campos y respuestas:** `mandatory_free_shipping`, `free_shipping`, `dimensions`, `item_price`, `listing_type_id`, `mode`, `condition`, `logistic_type`, `zip_code` y `city_to`.

**Ejemplos documentados:** cotización por dimensiones con datos del ítem, por código postal y por ciudad.

## Operaciones de API

## Conceptos y recursos asociados

### Costos de envío

Documenta la información de envío para publicar/editar un ítem y las opciones/costos estimados durante la compra. Distingue la obligación de envío gratis de la simulación de costo y permite cotizar el destino por código postal o ciudad.

**Respuesta**

```json
{
  "fields": "`mandatory_free_shipping`, `free_shipping`, `dimensions`, `item_price`, `listing_type_id`, `mode`, `condition`, `logistic_type`, `zip_code` y `city_to`."
}
```

**Errores documentados**

- 400: seller_id sin valor o zip_code inválido.
- 403: error de API/ítem inválido.
- 404: ítem o área de cobertura no encontrada.

**Ejemplos documentados**

- cotización por dimensiones con datos del ítem, por código postal y por ciudad.
## Operaciones de API

### Consulta la configuración de envío gratis del ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la configuración de envío gratis del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: seller_id sin valor o zip_code inválido.
- 403: ítem inválido.
- 404: ítem o cobertura no encontrada.

**Ejemplos**

- cotización por dimensiones con datos del ítem, por código postal y por ciudad.

### Obtiene opciones y costos de envío para la compra con `zip_code` o `city_to`

**Método:** `GET`  
**Ruta:** `/items/{item_id}/shipping_options`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene opciones y costos de envío para la compra con `zip_code` o `city_to`.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `zip_code` (query): Destino por código postal.
- `city_to` (query): Destino por ciudad.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: seller_id sin valor o zip_code inválido.
- 403: ítem inválido.
- 404: ítem o cobertura no encontrada.

**Ejemplos**

- cotización por dimensiones con datos del ítem, por código postal y por ciudad.

### Estima el costo de envío para publicar/editar; requiere `item_id` o `dimensions`

**Método:** `GET`  
**Ruta:** `/users/{user_id}/shipping_options/free`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Estima el costo de envío para publicar/editar; requiere `item_id` o `dimensions`.

**Parámetros**

- `user_id` (path, obligatorio): Variable de ruta documentada.
- `item_id` (query): La fuente requiere item_id o dimensions.
- `dimensions` (query): La fuente requiere item_id o dimensions.
- `verbose` (query): Parámetro de detalle mostrado en la fuente.
- `item_price` (query): Precio del ítem.
- `listing_type_id` (query): Tipo de publicación.
- `mode` (query): Modo de envío.
- `condition` (query): Condición.
- `logistic_type` (query): Tipo logístico.
- `free_shipping` (query): Indica la configuración de envío gratis.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: seller_id sin valor o zip_code inválido.
- 403: ítem inválido.
- 404: ítem o cobertura no encontrada.

**Ejemplos**

- cotización por dimensiones con datos del ítem, por código postal y por ciudad.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/costos-de-envios](https://developers.mercadolibre.com.co/es_co/costos-de-envios)  
**Captura:** 2026-10-08T22:51:25.439Z

---

## [Costos por vender](../markdown/comision-por-vender.md)

Actualización indicada por la fuente: 03/09/2026. Captura: 2026-10-08T22:51:29.334Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/comision-por-vender](https://developers.mercadolibre.com.co/es_co/comision-por-vender)

# Costos por vender

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 03/09/2026  
**Captura:** 2026-10-08T22:51:29.334Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/comision-por-vender](https://developers.mercadolibre.com.co/es_co/comision-por-vender)

## Resumen

Explica cómo estimar costos por venta mediante los precios de publicación del sitio, considerando precio, categoría/producto, moneda, tipo de publicación, logística, envío y tags de campañas. Incluye parámetros para Supermarket y cargos adicionales.

## Contenido y conceptos documentados

- El recurso `listing_prices` calcula componentes de costos para combinaciones de precio y atributos. La fuente destaca `fixed_fee`, `financing_add_on_fee`, `gross_amount` y `meli_percentage_fee`.
- `price` es el parámetro de entrada para calcular costos. Para aproximar el costo real se recomienda enviar `shipping_mode`, `logistic_type` y `billable_weight`; el peso facturable se expresa en gramos y es obligatorio para Argentina.
- `category_id` puede sustituirse por `catalog_product_id` para un cálculo más preciso. Se documentan `listing_type_id`, `currency_id`, `quantity`, `tags`, `shipping_modes` y campos relacionados con Supermarket.
- Para cotizar envíos en la estructura nueva, la respuesta y solicitud dependen de logística; la página indica que la ausencia de datos logísticos/peso puede provocar una comisión fija distinta de la cobrada.
- La fuente muestra error 400 `bad_request` para una solicitud incorrecta.

**Campos y respuestas:** `fixed_fee`, `financing_add_on_fee`, `gross_amount`, `meli_percentage_fee`, `price`, `category_id`, `catalog_product_id`, `currency_id`, `listing_type_id`, `logistic_type`, `shipping_mode(s)`, `billable_weight`, `tags` y `quantity`.

**Ejemplos documentados:** cálculo solo con precio, con categoría, moneda/tipo de publicación, logística y peso, y cálculo para Supermarket.

## Operaciones de API

## Conceptos y recursos asociados

### Costos por vender

Explica cómo estimar costos por venta mediante los precios de publicación del sitio, considerando precio, categoría/producto, moneda, tipo de publicación, logística, envío y tags de campañas. Incluye parámetros para Supermarket y cargos adicionales.

**Respuesta**

```json
{
  "fields": "`fixed_fee`, `financing_add_on_fee`, `gross_amount`, `meli_percentage_fee`, `price`, `category_id`, `catalog_product_id`, `currency_id`, `listing_type_id`, `logistic_type`, `shipping_mode(s)`, `billable_weight`, `tags` y `quantity`."
}
```

**Errores documentados**

- 400 bad_request: solicitud incorrecta.

**Ejemplos documentados**

- cálculo solo con precio, con categoría, moneda/tipo de publicación, logística y peso, y cálculo para Supermarket.
## Operaciones de API

### Consulta costos de publicación/venta con filtros como precio, categoría o producto, moneda, tipo de publicación y logística

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/listing_prices`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta costos de publicación/venta con filtros como precio, categoría o producto, moneda, tipo de publicación y logística.

**Parámetros**

- `site_id` (path, obligatorio): Variable de ruta documentada.
- `price` (query, obligatorio): Precio de venta del ítem.
- `category_id` (query): Categoría; puede usarse catalog_product_id para precisión de producto.
- `currency_id` (query): Moneda del sitio.
- `logistic_type` (query): Tipo logístico.
- `shipping_modes` (query): Modos de envío.
- `shipping_mode` (query): Modo de envío.
- `listing_type_id` (query): Tipo de publicación.
- `quantity` (query): Cantidad consultada.
- `tags` (query): Tag de campaña/elegibilidad; incluye supermarket_eligible.
- `billable_weight` (query): Peso facturable en gramos; obligatorio para Argentina.
- `catalog_product_id` (query): Producto de catálogo para cálculo más preciso.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "currency_id",
    "listing_type_id",
    "listing_fee_amount",
    "listing_fee_details",
    "fixed_fee",
    "gross_amount",
    "sale_fee_amount",
    "sale_fee_details",
    "financing_add_on_fee",
    "meli_percentage_fee",
    "percentage_fee"
  ]
}
```

**Errores documentados**

- 400 bad_request: solicitud inválida.

**Ejemplos**

- cálculo solo con precio, con categoría, moneda/tipo de publicación, logística y peso, y cálculo para Supermarket.

### Referencia HTTP GET /sites/MLA/listing_pricesprice=10345&listing_type_id=gold_special&category_id=MLA120350

**Método:** `GET`  
**Ruta:** `/sites/MLA/listing_pricesprice=10345&listing_type_id=gold_special&category_id=MLA120350`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /sites/MLA/listing_pricesprice=10345&listing_type_id=gold_special&category_id=MLA120350. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/comision-por-vender](https://developers.mercadolibre.com.co/es_co/comision-por-vender)  
**Captura:** 2026-10-08T22:51:29.334Z

---

## [Cupones del vendedor](../markdown/cupones-del-vendedor.md)

Actualización indicada por la fuente: 13/03/2026. Captura: 2026-10-08T22:51:30.604Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/cupones-del-vendedor](https://developers.mercadolibre.com.co/es_co/cupones-del-vendedor)

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

---

## [Datos de Facturación](../markdown/facturacion.md)

Actualización indicada por la fuente: 16/06/2026. Captura: 2026-10-08T22:51:32.170Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/facturacion](https://developers.mercadolibre.com.co/es_co/facturacion)

# Datos de Facturación

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 16/06/2026  
**Captura:** 2026-10-08T22:51:32.170Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/facturacion](https://developers.mercadolibre.com.co/es_co/facturacion)

## Resumen

Documenta cómo recuperar la información de facturación del comprador para emitir documentos fiscales. Primero se consulta la orden para obtener buyer.billing_info.id; luego se consulta el recurso de facturación con site_id y ese identificador. La respuesta cambia según país y tipo de persona.

## Contenido y conceptos documentados

- La respuesta de la orden incluye buyer.billing_info.id, que se usa como billing_info_id en la consulta posterior.
- Los datos documentados incluyen identificación, nombre, clasificación tributaria, inscripciones y dirección. Entre los campos de dirección aparecen calle, número, ciudad, barrio, comentario, código postal, estado y país; los atributos tributarios varían según el sitio.
- Los ejemplos muestran información para personas naturales y jurídicas y campos regionales como taxpayer_type, state_registration, iibb_number, economic_activity, contributor y cfdi, según el país.
- Autenticación mostrada: Bearer. No hay cuerpo de solicitud para estas consultas.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar datos fiscales del comprador

**Método:** `GET`  
**Ruta:** `/orders/billing-info/{site_id}/{billing_info_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene datos de facturación para el sitio y el identificador extraído de la orden.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `billing_info_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Datos de comprador y facturación: identificación, datos tributarios e información de domicilio; los campos dependen del sitio y de la persona.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos regionales para personas físicas y jurídicas.

### Obtener identificador de facturación de una orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Consulta la orden y extrae buyer.billing_info.id para la llamada de facturación.

**Parámetros**

- `order_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Orden con buyer.id y buyer.billing_info.id, además de otros datos de la orden.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de una orden con billing_info.id.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/facturacion](https://developers.mercadolibre.com.co/es_co/facturacion)  
**Captura:** 2026-10-08T22:51:32.170Z

---

## [Descargas](../markdown/reportes-descargas.md)

Actualización indicada por la fuente: 25/04/2024. Captura: 2026-10-08T22:51:33.064Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/reportes-descargas](https://developers.mercadolibre.com.co/es_co/reportes-descargas)

# Descargas

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 25/04/2024  
**Captura:** 2026-10-08T22:51:33.064Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/reportes-descargas](https://developers.mercadolibre.com.co/es_co/reportes-descargas)

## Resumen

Describe el ciclo de generación, consulta y descarga de reportes de facturación, además de la descarga del PDF de un documento legal. La generación devuelve un file_id; el cliente debe consultar su estado y descargar el archivo cuando figure READY.

## Contenido y conceptos documentados

- La generación recibe group, document_type y report_format. La página enumera grupos ML, MP, FLEX, FULL, INSURTECH y PAYMENT; el ejemplo usa BILL y CSV.
- Los estados documentados son PROCESSING, READY y ERROR. Si la generación falla, la fuente indica volver a consultar; la descarga del reporte se realiza después de READY.
- La descarga de documentos legales requiere el file_id obtenido mediante otro recurso; esta página no detalla aquí la operación que entrega ese identificador.
- Autenticación mostrada: Bearer. Los ejemplos de consulta y descarga usan document_type=BILL como parámetro de consulta.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Descargar documento legal

**Método:** `GET`  
**Ruta:** `/billing/integration/legal_document/{file_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Descarga un documento legal en formato PDF usando su file_id.

**Parámetros**

- `file_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Archivo PDF.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta indicada como descarga del PDF.

### Descargar reporte

**Método:** `GET`  
**Ruta:** `/billing/integration/reports/{file_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Descarga el archivo generado cuando su estado es READY.

**Parámetros**

- `file_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `document_type` (query, opcional): document_type (ejemplo: BILL)

**Solicitud**

No documentado en la fuente.

**Respuesta**

Archivo del reporte; el formato se define al generarlo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de descarga de reporte CSV.

### Consultar estado de generación

**Método:** `GET`  
**Ruta:** `/billing/integration/reports/{file_id}/status`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Devuelve el estado del reporte solicitado.

**Parámetros**

- `file_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `document_type` (query, opcional): document_type (ejemplo: BILL)

**Solicitud**

No documentado en la fuente.

**Respuesta**

status: PROCESSING, READY o ERROR.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta de ejemplo con status PROCESSING.

### Solicitar reporte de facturación

**Método:** `POST`  
**Ruta:** `/billing/integration/periods/key/{key}/reports`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Solicita generar un reporte para una clave de período.

**Parámetros**

- `key` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `group` (body, obligatorio): Grupo de reporte.
- `document_type` (body, obligatorio): Tipo de documento, ejemplo BILL.
- `report_format` (body, obligatorio): Formato, ejemplo CSV.

**Solicitud**

JSON con group, document_type y report_format.

**Respuesta**

Identificador fileId para seguir el proceso.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo group=ML, document_type=BILL, report_format=CSV.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/reportes-descargas](https://developers.mercadolibre.com.co/es_co/reportes-descargas)  
**Captura:** 2026-10-08T22:51:33.064Z

---

## [Descripción de productos](../markdown/descripcion-de-articulos.md)

Actualización indicada por la fuente: 13/03/2026. Captura: 2026-10-08T22:51:34.084Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/descripcion-de-articulos](https://developers.mercadolibre.com.co/es_co/descripcion-de-articulos)

# Descripción de productos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/03/2026  
**Captura:** 2026-10-08T22:51:34.084Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/descripcion-de-articulos](https://developers.mercadolibre.com.co/es_co/descripcion-de-articulos)

## Resumen

La guía cubre consulta y edición de la descripción de un ítem. La API trabaja con texto plano en plain_text; admite saltos de línea con \n y recomienda una descripción concisa, legible y sin duplicar información de atributos.

## Contenido y conceptos documentados

- La respuesta de consulta incluye text, plain_text, last_updated, date_created y snapshot.
- POST sirve para crear la descripción; intentar crearla cuando ya existe devuelve error. PUT actualiza la descripción y la variante api_version=2 informa la posición de caracteres no válidos.
- El campo de escritura documentado es plain_text. La fuente muestra el error HTTP 400 item.description.type.invalid cuando la descripción no es texto plano.
- Autenticación mostrada: Bearer.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar descripción

**Método:** `GET`  
**Ruta:** `/items/{item_id}/description`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene la descripción vigente del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

text, plain_text, last_updated, date_created y snapshot.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta de ejemplo con los campos de descripción.

### Crear descripción

**Método:** `POST`  
**Ruta:** `/items/{item_id}/description`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Crea una descripción para el ítem cuando todavía no tiene una.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `plain_text` (body, obligatorio): Descripción en texto plano.

**Solicitud**

plain_text con texto plano; los saltos de línea se representan con \n.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: item.description.type.invalid si no es texto plano; POST sobre una descripción existente produce error.

**Ejemplos**

- Ejemplo de plain_text.

### Actualizar descripción

**Método:** `PUT`  
**Ruta:** `/items/{item_id}/description`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Reemplaza la descripción existente; api_version=2 permite obtener detalle de posición inválida.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `api_version` (query, opcional): api_version=2 (variante mostrada por la fuente)
- `plain_text` (body, obligatorio): Descripción en texto plano.

**Solicitud**

plain_text con texto plano.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400 item.description.type.invalid; la versión 2 indica el índice de carácter inválido.

**Ejemplos**

- Ejemplo de actualización de plain_text.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/descripcion-de-articulos](https://developers.mercadolibre.com.co/es_co/descripcion-de-articulos)  
**Captura:** 2026-10-08T22:51:34.084Z

---

## [Descuento individual](../markdown/descuento-individual.md)

Actualización indicada por la fuente: 09/06/2026. Captura: 2026-10-08T22:51:34.905Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/descuento-individual](https://developers.mercadolibre.com.co/es_co/descuento-individual)

# Descuento individual

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 09/06/2026  
**Captura:** 2026-10-08T22:51:34.905Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/descuento-individual](https://developers.mercadolibre.com.co/es_co/descuento-individual)

## Resumen

Documenta la consulta, creación y eliminación de descuentos individuales PRICE_DISCOUNT sobre publicaciones. La oferta se aplica a un segmento de compradores y debe respetar condiciones de reputación, estado, condición y precio de la publicación.

## Contenido y conceptos documentados

- La fuente indica descuentos generales de 5–80 % y una duración máxima de 14 días. Las fechas se envían como fecha y hora; subir el precio puede retirar el descuento.
- Se documentan deal_price requerido, top_deal_price opcional, start_date, finish_date y promotion_type=PRICE_DISCOUNT. Una oferta DEAL en conflicto puede postergar el inicio hasta que termine.
- La respuesta de creación incluye price y original_price. La consulta puede incluir datos de boosted_offer como discount_meli_boosted_percentage, discount_meli_boost_amount y total_price_for_boosted_offer cuando aplica.
- Autenticación mostrada: Bearer. La fuente menciona restricciones para vendedores/items no elegibles y para libros en MLA.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Eliminar descuento individual

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Elimina la oferta indicada para el ítem.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `promotion_type` (query, opcional): promotion_type
- `app_version` (query, opcional): app_version=v2

**Solicitud**

No documentado en la fuente.

**Respuesta**

HTTP 200 OK.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta 200 OK documentada.

### Consultar promociones de un ítem

**Método:** `GET`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene el estado promocional del ítem, incluido el descuento vigente o datos de oferta impulsada.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Datos de promociones y precio; si boosted_offer=true pueden aparecer discount_meli_boosted_percentage, discount_meli_boost_amount y total_price_for_boosted_offer.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra campos de boosted_offer.

### Crear descuento individual

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{item_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Crea una oferta de tipo PRICE_DISCOUNT para el ítem.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `app_version` (query, opcional): app_version=v2
- `deal_price` (body, obligatorio): Precio con descuento para todos.
- `top_deal_price` (body, opcional): Precio opcional para compradores leales nivel 3–6.
- `start_date` (body, obligatorio): Fecha de inicio.
- `finish_date` (body, obligatorio): Fecha final.
- `promotion_type` (body, obligatorio): PRICE_DISCOUNT.

**Solicitud**

deal_price (precio con descuento para todos), top_deal_price (opcional; para compradores Mercado Puntos niveles 3–6), start_date, finish_date y promotion_type=PRICE_DISCOUNT.

**Respuesta**

price y original_price.

**Errores documentados**

- buyer_discount_not_in_range: descuento general fuera del rango 5%–80%.
- best_buyer_discount_not_in_range: descuento para mejores compradores fuera del rango 5%–80%.
- discount_below_10_percent_difference: si el descuento general supera 35%, la diferencia para niveles 3–6 debe ser al menos 10%.
- discount_below_5_percent_difference: diferencia entre descuento general y niveles 3–6 inferior al 5%.
- error_credibility_price: el descuento no es suficiente para considerarse creíble; aplicar uno mayor.

**Ejemplos**

- Ejemplo de deal_price y fechas.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/descuento-individual](https://developers.mercadolibre.com.co/es_co/descuento-individual)  
**Captura:** 2026-10-08T22:51:34.905Z

---

## [Devoluciones](../markdown/gestionar-devoluciones.md)

Actualización indicada por la fuente: 22/12/2025. Captura: 2026-10-08T22:51:35.863Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/gestionar-devoluciones](https://developers.mercadolibre.com.co/es_co/gestionar-devoluciones)

# Devoluciones

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 22/12/2025  
**Captura:** 2026-10-08T22:51:35.863Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestionar-devoluciones](https://developers.mercadolibre.com.co/es_co/gestionar-devoluciones)

## Resumen

La guía describe la consulta y revisión de devoluciones asociadas a reclamos, la obtención de razones para una revisión fallida, la carga de adjuntos y la consulta de costos de devolución. Las acciones y la evidencia se relacionan con claim_id o return_id según el recurso.

## Contenido y conceptos documentados

- La consulta de devoluciones de un reclamo devuelve identificadores, estado de devolución y dinero, logística, envío y seguimiento; entre los campos visibles aparecen id, last_updated, shipment_id, status, tracking_number, destination, address, refund_at, date_closed, claim_id y resource_id.
- La revisión del triage se consulta por return_id. Para enviar una revisión fallida se utiliza return-review y las razones dependen de flow y claim_id; la página muestra seller_return_failed.
- Los adjuntos se envían como archivo multipart con el campo file y devuelven user_id y file_name. La revisión fallida requiere reason y message; attachments es requerido para SRF2 y SRF4, y order_id solo aplica a una orden concreta en casos carrito. return-cost admite calculate_amount_usd=true.
- Autenticación mostrada: Bearer. La fuente incluye respuestas de reviews y costos, pero algunos detalles de reglas de negocio dependen del flujo del reclamo.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /claims/{CLAIMS}

La fuente menciona la ruta /claims/{CLAIMS}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/{CLAIMS}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /claims/{CLAIM_ID}

La fuente menciona la ruta /claims/{CLAIM_ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/{CLAIM_ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /claims/{CLAIM_ID}/returns/attachments

La fuente menciona la ruta /claims/{CLAIM_ID}/returns/attachments, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/{CLAIM_ID}/returns/attachments`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /shipments/{SHIPMENT_ID}/costs

La fuente menciona la ruta /shipments/{SHIPMENT_ID}/costs, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/shipments/{SHIPMENT_ID}/costs`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar costo de devolución

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/{claim_id}/charges/return-cost`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene información de cargos asociados a la devolución.

**Parámetros**

- `claim_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `calculate_amount_usd` (query, opcional): calculate_amount_usd opcional: true

**Solicitud**

No documentado en la fuente.

**Respuesta**

currency_id y amount; amount_usd aparece cuando calculate_amount_usd=true.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con calculate_amount_usd=true.

### Obtener razones para revisar devolución

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/returns/reasons`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Consulta razones aplicables al flujo del reclamo.

**Parámetros**

- `flow` (query, obligatorio): flow requerido
- `claim_id` (query, obligatorio): claim_id requerido

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista con id, name, detail, position y apply.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo flow=seller_return_failed.

### Consultar revisiones de una devolución

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/returns/{return_id}/reviews`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lee las revisiones o decisiones del triage asociadas a la devolución.

**Parámetros**

- `return_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista reviews con resource, status u otros datos presentados en el ejemplo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta de ejemplo con reviews.

### Consultar devoluciones de un reclamo

**Método:** `GET`  
**Ruta:** `/post-purchase/v2/claims/{claim_id}/returns`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene la devolución asociada al reclamo.

**Parámetros**

- `claim_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Datos de devolución, envío, tracking, dirección, fechas, estado y referencias del reclamo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de objeto de devolución.

### Adjuntar evidencia a devolución

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/{claim_id}/returns/attachments`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Carga evidencia para una revisión fallida.

**Parámetros**

- `claim_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

Multipart/form-data con archivo en campo file.

**Respuesta**

user_id y file_name; file_name identifica la evidencia que se referencia en la revisión.

**Errores documentados**

- 404 not_found_error: claim inexistente.
- bad_request: error al recuperar archivo cargado (por ejemplo, archivo no válido).
- 404 not_found: no se puede obtener el adjunto.

**Ejemplos**

- Ejemplo de carga de archivo PNG.

### Enviar revisión de devolución

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/returns/{return_id}/return-review`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Envía una revisión a la decisión del triage; la fuente muestra el caso conforme y la revisión fallida.

**Parámetros**

- `return_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `reason` (body, opcional): Identificador devuelto por /returns/reasons para la revisión fallida.
- `message` (body, opcional): Mensaje del vendedor requerido para revisión fallida.
- `attachments` (body, opcional): Nombres de archivos; requerido para las razones SRF2 y SRF4.
- `order_id` (body, opcional): Usar solo al revisar una orden específica dentro de un caso carrito.

**Solicitud**

Para revisión OK, {}. Para revisión fallida, arreglo(s) con reason y message; attachments es requerido para SRF2 y SRF4. order_id se usa solo para revisión de una orden en casos carrito.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de revisión conforme con body vacío.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestionar-devoluciones](https://developers.mercadolibre.com.co/es_co/gestionar-devoluciones)  
**Captura:** 2026-10-08T22:51:35.863Z

---

## [Elegibilidad de catálogo](../markdown/elegibilidad-catalogo.md)

Actualización indicada por la fuente: 29/12/2025. Captura: 2026-10-08T22:51:36.682Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/elegibilidad-catalogo](https://developers.mercadolibre.com.co/es_co/elegibilidad-catalogo)

# Elegibilidad de catálogo

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:51:36.682Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/elegibilidad-catalogo](https://developers.mercadolibre.com.co/es_co/elegibilidad-catalogo)

## Resumen

Explica cómo localizar publicaciones de catálogo, publicaciones de marketplace y artículos elegibles para catálogo, y cómo consultar la elegibilidad individual o por lote. El flujo diferencia la publicación de catálogo vinculada a catalog_product_id de la publicación estándar.

## Contenido y conceptos documentados

- El recurso de búsqueda admite catalog_listing=true o false; también permite filtrar por tags=catalog_listing_eligible y combinar otros filtros como status.
- La consulta individual devuelve id, site_id, domain_id, buy_box_eligible, status y, cuando existen, datos de variaciones. La fuente menciona estados READY_FOR_OPTIN, ALREADY_OPTED_IN y CLOSED.
- La búsqueda masiva recibe ids separados por coma. La guía lista disponibilidad en Argentina, México, Brasil, Colombia, Chile, Uruguay, Perú y Ecuador.
- Autenticación mostrada: Bearer.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar elegibilidad de publicación

**Método:** `GET`  
**Ruta:** `/items/{item_id}/catalog_listing_eligibility`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Devuelve si una publicación puede incorporarse al catálogo y sus datos relacionados.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, site_id, domain_id, buy_box_eligible, status y variaciones cuando aplica.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos de publicación con y sin variaciones.

### Consultar elegibilidad por lote

**Método:** `GET`  
**Ruta:** `/multiget/catalog_listing_eligibility`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene elegibilidad de varios ítems en una sola consulta.

**Parámetros**

- `ids` (query, opcional): ids: identificadores de ítem separados por coma

**Solicitud**

No documentado en la fuente.

**Respuesta**

Resultados de elegibilidad por ítem.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con dos ids.

### Buscar publicaciones y elegibilidad de catálogo

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items/search`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lista publicaciones del vendedor filtrando por modalidad de catálogo o etiqueta de elegibilidad.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `catalog_listing` (query, opcional): catalog_listing=true|false
- `catalog_listing` (query, opcional): tags=catalog_listing_eligible
- `status` (query, opcional): status opcional como filtro

**Solicitud**

No documentado en la fuente.

**Respuesta**

seller_id y publicaciones; la respuesta distingue marketplace y catálogo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos con catalog_listing=true, false y tags=catalog_listing_eligible.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/elegibilidad-catalogo](https://developers.mercadolibre.com.co/es_co/elegibilidad-catalogo)  
**Captura:** 2026-10-08T22:51:36.682Z

---

## [Envíos](../markdown/envios.md)

Actualización indicada por la fuente: 18/09/2026. Captura: 2026-10-08T22:51:37.708Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/envios](https://developers.mercadolibre.com.co/es_co/envios)

# Envíos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 18/09/2026  
**Captura:** 2026-10-08T22:51:37.708Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/envios](https://developers.mercadolibre.com.co/es_co/envios)

## Resumen

Referencia de recursos de Mercado Envíos para consultar estados, detalle, artículos, costos, pagos, transportista, demoras, tiempo estimado, historial y órdenes relacionadas, además de dividir un envío. Las respuestas pueden requerir el formato nuevo; la operación de órdenes usa X-New-Domain.

## Contenido y conceptos documentados

- Los ejemplos usan Authorization Bearer. La consulta del detalle solicita x-format-new: true; varias rutas de subrecurso también muestran ese header. La consulta de órdenes asociadas requiere X-New-Domain:true.
- La documentación expone recursos de tracking, etiquetas de estado/subestado, transportista, SLA, lead time y retrasos. Los campos varían por recurso y la guía incluye fechas, costos y datos de ítems/pagos.
- La operación de split recibe un motivo y una lista de paquetes; el ejemplo usa DIMENSIONS_EXCEEDED. No se debe asumir el mismo encabezado o cuerpo para los demás recursos.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Listar estados y subestados

**Método:** `GET`  
**Ruta:** `/shipment_statuses`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Devuelve el catálogo de estados de envío y sus subestados.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de id, name y substatuses.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de estados to_be_agreed y pending.

### Consultar envío

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene el detalle general del envío; usar x-format-new: true en el ejemplo documentado.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Detalle del envío; el formato incluye campos de estado, etiquetas y datos de logística.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con x-format-new: true.

### Consultar transportista

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/carrier`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Recupera URL de seguimiento y nombre del transportista.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

url y name.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con nombre y URL de tracking.

### Consultar costos

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/costs`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene los importes y participantes vinculados al costo del envío.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

gross_amount y desglose receiver/cost, entre otros campos del ejemplo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con x-format-new: true.

### Consultar demoras

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/delays`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene demoras registradas para un envío.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

shipment_id y lista delays con tipo/detalle.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con x-format-new: true.

### Consultar historial de estados

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/history`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lista transiciones de estado y subestado del envío.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

status, substatus y fechas de evento.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con x-format-new: true.

### Consultar ítems del envío

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/items`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lista los productos incluidos en el envío.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

item_id, description y quantity.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de lista de ítems.

### Consultar tiempos de entrega

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/lead_time`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Recupera información de plazo y método logístico asociado.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

option_id, shipping_method y datos de tiempos del ejemplo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con x-format-new: true.

### Consultar órdenes asociadas

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/orders`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene órdenes vinculadas al envío; el ejemplo agrega X-New-Domain:true.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `X-New-Domain` (header, obligatorio): Header X-New-Domain: true

**Solicitud**

No documentado en la fuente.

**Respuesta**

Órdenes asociadas al shipment.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con header X-New-Domain:true.

### Consultar pagos del envío

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/payments`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lista pagos asociados al envío.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

payment_id, user_id y datos de pago del ejemplo.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con x-format-new: true.

### Consultar SLA del envío

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}/sla`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Devuelve el estado de cumplimiento del SLA y el servicio.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

status y service.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de status on_time.

### Dividir envío

**Método:** `POST`  
**Ruta:** `/shipments/{shipment_id}/split`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Solicita dividir un envío en paquetes según el motivo indicado.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `reason` (body, obligatorio): Motivo de división; el ejemplo usa DIMENSIONS_EXCEEDED.
- `packs` (body, obligatorio): Paquetes que resultan de la división.

**Solicitud**

reason y packs; el ejemplo usa reason=DIMENSIONS_EXCEEDED.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de solicitud de split.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/envios](https://developers.mercadolibre.com.co/es_co/envios)  
**Captura:** 2026-10-08T22:51:37.708Z

---

## [Envíos Colecta y Places](../markdown/envios-colectas-places.md)

Actualización indicada por la fuente: 25/09/2026. Captura: 2026-10-08T22:51:38.852Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/envios-colectas-places](https://developers.mercadolibre.com.co/es_co/envios-colectas-places)

# Envíos Colecta y Places

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 25/09/2026  
**Captura:** 2026-10-08T22:51:38.852Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/envios-colectas-places](https://developers.mercadolibre.com.co/es_co/envios-colectas-places)

## Resumen

Documenta la consulta y configuración de capacidad de despacho, tiempos de preparación y horarios para vendedores y nodos de Places. El flujo cambia a node_id cuando hay Multi-Origin, y las rutas dependen del tipo logístico o de servicio.

## Contenido y conceptos documentados

- Cobertura descrita: Argentina, Brasil, México, Chile, Colombia y Uruguay; Perú aparece con drop_off. La página menciona Colecta rápida en Brasil como xd_same_day.
- La capacidad se representa por día con capacity_min, capacity_max y capacity.value. Para actualizar, maximum debe ser false y value no puede exceder capacity_max; la fuente documenta errores 400 por formato, máximo e infinito y 404 por logística no válida.
- El tiempo de preparación usa SERVICE_TYPE=carrier_pickup y header X-Version:v3. Los tiempos tienen formato HH:MM; si processing_times va vacío se aplican valores por defecto de la logística documentada, los días bloqueados se ignoran y el cambio del día vigente aplica a la semana siguiente.
- El horario incluye schedule por día, work y detail con from, to, cutoff, milkrun_same_day y otros campos. En Multi-Origin se debe consultar/configurar por NETWORK_NODE_ID.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar horario de nodo

**Método:** `GET`  
**Ruta:** `/nodes/{network_node_id}/schedule/{logistic_type}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Consulta horarios de despacho en un nodo.

**Parámetros**

- `network_node_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `logistic_type` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

seller_id y schedule por día.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo xd_drop_off.

### Consultar preparación de nodo

**Método:** `GET`  
**Ruta:** `/nodes/{network_node_id}/service/{service_type}/processing_time_tool`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lee tiempos de preparación del nodo.

**Parámetros**

- `network_node_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_type` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `X-Version` (header, obligatorio): Header X-Version: v3 según llamada por servicio

**Solicitud**

No documentado en la fuente.

**Respuesta**

Opciones de tiempo y estado por día.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de nodo con carrier_pickup.

### Consultar capacidad de nodo

**Método:** `GET`  
**Ruta:** `/nodes/{node_id}/capacity_middleend`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lee la capacidad por día en un nodo de Places.

**Parámetros**

- `node_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

peak_season_mode y capacities por día.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con node_id.

### Consultar capacidad de vendedor

**Método:** `GET`  
**Ruta:** `/users/{user_id}/capacity_middleend/{logistic_type}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lee los límites y configuración de capacidad por día para la logística.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `logistic_type` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

peak_season_mode y capacities con day, capacity_min, capacity_max, capacity.value, maximum, source, can_add_capacity, can_subtract_capacity e intervention.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo logistic_type=cross_docking.

### Consultar preparación de vendedor

**Método:** `GET`  
**Ruta:** `/users/{user_id}/service/{service_type}/processing_time_tool`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lee opciones y tiempos de preparación por día.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_type` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `X-Version` (header, obligatorio): Header X-Version: v3

**Solicitud**

No documentado en la fuente.

**Respuesta**

Por día: modified_by_meli, intervention_type, visible, enabled, current_processing_time y available_options.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- service_type documentado: carrier_pickup.

### Consultar horario de vendedor

**Método:** `GET`  
**Ruta:** `/users/{user_id}/shipping/schedule/{logistic_type}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Consulta horarios de despacho por día y logística.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `logistic_type` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

seller_id y schedule por día con work y detail (from, to, cutoff, SLA y datos logísticos).

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo cross_docking.

### Actualizar capacidad de nodo

**Método:** `PUT`  
**Ruta:** `/nodes/{network_node_id}/capacity_middleend`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Actualiza la capacidad de despacho por nodo.

**Parámetros**

- `network_node_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `capacities` (body, obligatorio): Lista de capacidades por día.

**Solicitud**

Mismo formato capacities[] que la actualización por vendedor; maximum=false.

**Respuesta**

Mensaje de éxito o error documentado.

**Errores documentados**

- 400: error de parseo; excede capacidad máxima; capacidad infinita no permitida. 404: tipo logístico no válido.

**Ejemplos**

- La fuente indica reutilizar el JSON de usuario.

### Actualizar preparación de nodo

**Método:** `PUT`  
**Ruta:** `/nodes/{network_node_id}/service/{service_type}/processing_time_tool`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Guarda tiempos por día del nodo.

**Parámetros**

- `network_node_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_type` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `X-Version` (header, obligatorio): Header X-Version: v3
- `processing_times` (body, obligatorio): Tiempos de preparación HH:MM por día.

**Solicitud**

Mismo objeto processing_times con valores HH:MM.

**Respuesta**

message de confirmación.

**Errores documentados**

- 400: invalid processing time configuration.

**Ejemplos**

- La página indica utilizar el mismo JSON de vendedor.

### Actualizar capacidad de vendedor

**Método:** `PUT`  
**Ruta:** `/users/{user_id}/capacity_middleend/{logistic_type}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Actualiza la capacidad por día del vendedor.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `logistic_type` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `capacities` (body, obligatorio): Lista de capacidades por día.

**Solicitud**

capacities[] con day y capacity.value; maximum debe ser false.

**Respuesta**

Mensaje de éxito o error documentado.

**Errores documentados**

- 400: error al parsear body; capacity value exceeds maximum allowed capacity; infinite capacity is not allowed. 404: not valid logistic type.

**Ejemplos**

- Ejemplo con capacidades para días de la semana.

### Actualizar preparación de vendedor

**Método:** `PUT`  
**Ruta:** `/users/{user_id}/service/{service_type}/processing_time_tool`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Guarda tiempos por día para el servicio.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_type` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `X-Version` (header, obligatorio): Header X-Version: v3
- `processing_times` (body, obligatorio): Tiempos de preparación HH:MM por día.

**Solicitud**

processing_times con días y processing_time en HH:MM.

**Respuesta**

message de confirmación.

**Errores documentados**

- 400: invalid processing time configuration.

**Ejemplos**

- Ejemplo con lunes a sábado.

### Referencia HTTP GET /users/123456789/capacity_middleend/cross_docking

**Método:** `GET`  
**Ruta:** `/users/123456789/capacity_middleend/cross_docking`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/123456789/capacity_middleend/cross_docking. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /users/123456789/service/carrier_pickup/processing_time_tool

**Método:** `GET`  
**Ruta:** `/users/123456789/service/carrier_pickup/processing_time_tool`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/123456789/service/carrier_pickup/processing_time_tool. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /users/123456789/shipping/schedule/cross_docking

**Método:** `GET`  
**Ruta:** `/users/123456789/shipping/schedule/cross_docking`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/123456789/shipping/schedule/cross_docking. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /nodes/MXP20157465171/service/carrier_pickup/processing_time_tool

**Método:** `GET`  
**Ruta:** `/nodes/MXP20157465171/service/carrier_pickup/processing_time_tool`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /nodes/MXP20157465171/service/carrier_pickup/processing_time_tool. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /nodes/MXP20157465171/schedule/xd_drop_off

**Método:** `GET`  
**Ruta:** `/nodes/MXP20157465171/schedule/xd_drop_off`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /nodes/MXP20157465171/schedule/xd_drop_off. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP PUT /users/123456789/service/carrier_pickup/processing_time_tool

**Método:** `PUT`  
**Ruta:** `/users/123456789/service/carrier_pickup/processing_time_tool`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud PUT a /users/123456789/service/carrier_pickup/processing_time_tool. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP PUT /users/123456789/capacity_middleend/cross_docking

**Método:** `PUT`  
**Ruta:** `/users/123456789/capacity_middleend/cross_docking`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud PUT a /users/123456789/capacity_middleend/cross_docking. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP PUT /nodes/MXP20157465171/service/carrier_pickup/processing_time_tool

**Método:** `PUT`  
**Ruta:** `/nodes/MXP20157465171/service/carrier_pickup/processing_time_tool`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud PUT a /nodes/MXP20157465171/service/carrier_pickup/processing_time_tool. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/envios-colectas-places](https://developers.mercadolibre.com.co/es_co/envios-colectas-places)  
**Captura:** 2026-10-08T22:51:38.852Z

---

## [Envíos en feriados opcionales](../markdown/dias-no-laborables.md)

Actualización indicada por la fuente: 24/02/2025. Captura: 2026-10-08T22:51:39.656Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/dias-no-laborables](https://developers.mercadolibre.com.co/es_co/dias-no-laborables)

# Envíos en feriados opcionales

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 24/02/2025  
**Captura:** 2026-10-08T22:51:39.656Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/dias-no-laborables](https://developers.mercadolibre.com.co/es_co/dias-no-laborables)

## Resumen

Permite consultar y configurar fechas en las que un vendedor no trabajará o desea operar en un feriado opcional. Una segunda consulta devuelve los días no laborables configurados y puede filtrarse por fecha.

## Contenido y conceptos documentados

- La configuración de fechas contiene dates con finalized, closed, enabled, checked, description y date.
- Para guardar fechas, se envían site_id y una lista dates con checked, description y date. La consulta optout devuelve los días no laborables; date es opcional.
- Autenticación mostrada: Bearer.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar feriados opcionales

**Método:** `GET`  
**Ruta:** `/shipping/seller/{seller_id}/working_day_middleend`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lista fechas habilitadas/configurables para la operación del vendedor.

**Parámetros**

- `seller_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

dates[] con finalized, closed, enabled, checked, description y date.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con dates.

### Consultar días no laborables

**Método:** `GET`  
**Ruta:** `/shipping/seller/{seller_id}/working_day_middleend/optout`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Recupera los días no laborables configurados, con filtro opcional por fecha.

**Parámetros**

- `seller_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `date` (query, opcional): date opcional: AAAA-MM-DD

**Solicitud**

No documentado en la fuente.

**Respuesta**

dates[] con fechas y descripción.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos con y sin date.

### Configurar días de trabajo

**Método:** `PUT`  
**Ruta:** `/shipping/seller/{seller_id}/working_day_middleend`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Guarda las fechas seleccionadas por el vendedor.

**Parámetros**

- `seller_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `site_id` (body, obligatorio): Identificador del sitio.
- `dates` (body, obligatorio): Fechas seleccionadas y sus descripciones.

**Solicitud**

site_id y dates[] con checked, description y date.

**Respuesta**

HTTP 200 en la actualización exitosa.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de actualización.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/dias-no-laborables](https://developers.mercadolibre.com.co/es_co/dias-no-laborables)  
**Captura:** 2026-10-08T22:51:39.656Z

---

## [Envíos Flex](../markdown/envios-flex.md)

Actualización indicada por la fuente: 22/09/2026. Captura: 2026-10-08T22:51:40.878Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/envios-flex](https://developers.mercadolibre.com.co/es_co/envios-flex)

# Envíos Flex

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 22/09/2026  
**Captura:** 2026-10-08T22:51:40.878Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/envios-flex](https://developers.mercadolibre.com.co/es_co/envios-flex)

## Resumen

Referencia para comprobar la compatibilidad Flex de categorías e ítems, consultar suscripciones y administrar cobertura por zonas, feriados y rangos de entrega. También cubre asociación de envíos de mensajería y asignación de conductores.

## Contenido y conceptos documentados

- Para determinar si una categoría soporta Flex, la respuesta de shipping_preferences debe incluir self_service en logistics. La habilitación puede variar por país y dominio; activar Flex convierte la publicación a ME2.
- La suscripción expone service_id, mode, origin, status y configuración. El service_id es necesario para configurar el servicio; habilitar Flex y Turbo puede producir suscripciones separadas.
- La lectura de zonas y rangos admite show_availables. La configuración de feriados y delivery-ranges se realiza para site_id, user_id y service_id. La página documenta un 422 para una configuración con rango de entrega extendido activo.
- La asociación de envíos de courier requiere vincular el usuario courier con el vendedor; sin vínculo, la fuente señala respuesta 403. Las consultas usan Bearer en sus ejemplos.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Desactivar Flex en un ítem

**Método:** `DELETE`  
**Ruta:** `/flex/sites/{site_id}/items/{item_id}/v2`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Retira el ítem de Flex.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Estado de la operación; la página documenta códigos de respuesta.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de desactivación.

### Consultar compatibilidad de categoría

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/shipping_preferences`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Comprueba si la categoría incluye self_service entre sus tipos logísticos ME2.

**Parámetros**

- `category_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

category_id y logistics[].types/mode.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta de ejemplo con self_service.

### Consultar Flex de un ítem

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/items/{item_id}/v2`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Indica si el ítem se ofrece con Flex.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

has_flex boolean.

**Errores documentados**

- 400: dato inválido; 401: autorización inválida; 403: access token incorrecto; 404: ítem inexistente; 500: error interno.

**Ejemplos**

- Respuesta compacta {has_flex:true|false}.

### Consultar asignación del envío

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/shipments/{shipment_id}/assignment/v2`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene el conductor asignado al envío.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

driver_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta de ejemplo con driver_id.

### Consultar zonas de cobertura

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/coverage/zones/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lee zonas y opciones de cobertura Flex.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `show_availables` (query, opcional): show_availables opcional

**Solicitud**

No documentado en la fuente.

**Respuesta**

zones[] con id y cutoff (week, saturday, sunday); availables incluye las zonas disponibles cuando show_availables=true.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de consulta con show_availables.

### Consultar rangos de entrega Flex

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/delivery-ranges/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lee ventanas y rangos horarios de entrega.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `show_availables` (query, opcional): show_availables opcional

**Solicitud**

No documentado en la fuente.

**Respuesta**

delivery_window, delivery_ranges y availables cuando se solicitan.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con show_availables.

### Consultar feriados Flex

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/holidays/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene fechas de feriado configuradas para el servicio.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

holidays y datos de fecha/selección.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta con holidays.

### Consultar suscripciones Flex

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/subscriptions/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lista suscripciones del usuario, modo y service_id.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

site_id, user_id, service_id, mode, origin, status y configuration.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con datos de Flex.

### Consultar estado de envío Flex

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Consulta estados y subestados del flujo Flex.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Estado/subestado y tags del envío.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de envío Flex.

### Activar Flex en un ítem

**Método:** `POST`  
**Ruta:** `/flex/sites/{site_id}/items/{item_id}/v2`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Realiza el opt-in Flex para el ítem.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Estado de la operación; la página documenta códigos de respuesta.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de activación.

### Asociar envío a courier

**Método:** `POST`  
**Ruta:** `/flex/sites/{site_id}/users/{courier_user_id}/courier-shipment/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Asocia shipment_id al usuario de mensajería que gestiona la entrega.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `courier_user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `shipment_id` (body, obligatorio): Identificador del envío asignado al courier.

**Solicitud**

shipment_id.

**Respuesta**

204 No Content en el caso exitoso; la fuente indica 403 si courier y vendedor no están vinculados.

**Errores documentados**

- 403: falta vinculación entre la cuenta courier y vendedor.

**Ejemplos**

- Ejemplo de asociación de shipment.

### Actualizar zonas de cobertura

**Método:** `PUT`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/coverage/zones/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Actualiza las zonas donde presta servicio el vendedor.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `zones` (body, obligatorio): Zonas con id y cutoff opcional.

**Solicitud**

zones[] con id y cutoff opcional; cutoff contiene week, saturday y sunday. Si se define cutoff por zona, cada zona puede usar valores distintos.

**Respuesta**

zones[] con id y cutoff; availables.zones[] puede mostrar id, label y barrios disponibles cuando se consulta con show_availables.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de request con zonas.

### Actualizar rangos de entrega Flex

**Método:** `PUT`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/delivery-ranges/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Actualiza ventanas y rangos de entrega.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `delivery_window` (body, obligatorio): Ventana de entrega.
- `delivery_ranges` (body, obligatorio): Rangos por día con capacidad, from, to y cutoff cuando corresponda.

**Solicitud**

delivery_window y delivery_ranges según ejemplo de la página.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 422: no se puede procesar mientras esté activo un rango extendido de entrega.

**Ejemplos**

- Ejemplo de body con rangos.

### Actualizar feriados Flex

**Método:** `PUT`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/holidays/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Actualiza los feriados del servicio.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `holidays` (body, obligatorio): Fechas de feriados y selección.

**Solicitud**

Lista holidays; la fuente indica selected=true para marcar días laborables habilitados.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de configuración de feriados.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/envios-flex](https://developers.mercadolibre.com.co/es_co/envios-flex)  
**Captura:** 2026-10-08T22:51:40.878Z

---

## [Envíos Fulfillment](../markdown/envios-fulfillment.md)

Actualización indicada por la fuente: 05/10/2026. Captura: 2026-10-08T22:51:41.912Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/envios-fulfillment](https://developers.mercadolibre.com.co/es_co/envios-fulfillment)

# Envíos Fulfillment

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 05/10/2026  
**Captura:** 2026-10-08T22:51:41.912Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/envios-fulfillment](https://developers.mercadolibre.com.co/es_co/envios-fulfillment)

## Resumen

Guía de consultas de inventario Full: recuperar el inventory_id desde una publicación, revisar stock disponible/no disponible y buscar operaciones de stock. Full se indica disponible en Argentina, Brasil, México, Chile y Colombia.

## Contenido y conceptos documentados

- Cada variación puede tener su propio inventory_id. El stock incluye total, available_quantity, not_available_quantity, not_available_detail y external_references.
- Con include_attributes=conditions se muestran condiciones adicionales de stock no disponible, como daños o productos no soportados.
- La búsqueda de operaciones requiere seller_id e inventory_id; permite filtrar por fecha, tipo, external_references.shipment_id, paginación y scroll. El intervalo máximo documentado es 60 días y, si no se especifican fechas, el default son los últimos 15 días. La fuente informa disponibilidad de datos por últimos 12 meses.
- Errores documentados incluyen seller_product_not_found, validation_error, forbidden, unauthorized, too_many_request e internal_error; HTTP 400 por rango mayor a 60 días o filtros inválidos, 401/403 por autorización, 404 por inventario, 429 por límite y 500 interno.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar stock Full

**Método:** `GET`  
**Ruta:** `/inventories/{inventory_id}/stock/fulfillment`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene cantidades disponibles y no disponibles del inventario.

**Parámetros**

- `inventory_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `include_attributes` (query, opcional): include_attributes=conditions opcional

**Solicitud**

No documentado en la fuente.

**Respuesta**

inventory_id, total, available_quantity, not_available_quantity, not_available_detail y external_references; conditions si se solicita.

**Errores documentados**

- 400 validation_error; 401 unauthorized; 403 forbidden; 404 seller_product_not_found; 429 too_many_request; 500 internal_error.

**Ejemplos**

- Ejemplo de stock y ejemplo con include_attributes=conditions.

### Obtener inventory_id

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Consulta la publicación para recuperar inventory_id necesario para leer stock Full.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, site_id y inventory_id; en publicaciones con variaciones existe inventory_id por variación.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de publicación con inventory_id.

### Buscar operaciones de stock Full

**Método:** `GET`  
**Ruta:** `/stock/fulfillment/operations/search`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Lista movimientos de inventario para vendedor e inventario con filtros y scroll.

**Parámetros**

- `seller_id` (query, obligatorio): seller_id requerido
- `inventory_id` (query, opcional): inventory_id (lista separada por coma)
- `date_from` (query, opcional): date_from/date_to opcionales
- `type` (query, opcional): type
- `external_references.shipment_id` (query, opcional): external_references.shipment_id
- `limit` (query, opcional): limit
- `sort` (query, opcional): sort
- `scroll` (query, opcional): scroll

**Solicitud**

No documentado en la fuente.

**Respuesta**

paging y results; cada resultado incluye id, seller_id, inventory_id, date_created, type, detail, result y external_references.

**Errores documentados**

- 400 validation_error por seller_id ausente, tipo/limit inválidos o rango superior a 60 días; 401 unauthorized; 403 forbidden; 429 too_many_request; 500 internal_error.

**Ejemplos**

- Ejemplos con rango de fechas, filtros type/shipment_id y scroll.

### Referencia HTTP GET /stock/fulfillment/operations/{OPERATION_ID}

**Método:** `GET`  
**Ruta:** `/stock/fulfillment/operations/{OPERATION_ID}`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /stock/fulfillment/operations/{OPERATION_ID}. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /stock/fulfillment/operations/329663159

**Método:** `GET`  
**Ruta:** `/stock/fulfillment/operations/329663159`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /stock/fulfillment/operations/329663159. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/envios-fulfillment](https://developers.mercadolibre.com.co/es_co/envios-fulfillment)  
**Captura:** 2026-10-08T22:51:41.912Z

---

## [Envíos Personalizados](../markdown/envios-personalizados.md)

Actualización indicada por la fuente: 13/03/2026. Captura: 2026-10-08T22:51:42.998Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/envios-personalizados](https://developers.mercadolibre.com.co/es_co/envios-personalizados)

# Envíos Personalizados

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/03/2026  
**Captura:** 2026-10-08T22:51:42.998Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/envios-personalizados](https://developers.mercadolibre.com.co/es_co/envios-personalizados)

## Resumen

Explica el modo custom, donde el vendedor define costos y gestiona la logística, y not_specified, donde comprador y vendedor acuerdan detalles y no existe shipment_id. También describe cómo consultar opciones y reportar tracking, promesa, entrega o cancelación.

## Contenido y conceptos documentados

- Al crear un ítem se configura shipping.mode=custom con costos y descripciones; not_specified puede usarse para acordar el envío. El envío personalizado gratuito solo se permite en categorías que no aceptan Mercado Envíos.
- La respuesta shipping_options muestra options con id, option_hash, name, currency_id, list_cost, cost, base_cost, display y speed.
- Estados documentados: Pending puede pasar a Shipped, Delivered o Cancelled; Shipped admite actualizar tracking/promesa; Delivered puede volver a Pending o Shipped; Cancelled es terminal.
- Para actualizar envío se envían receiver_id y, según el escenario, status, speed, tracking_number o comments. tracking_number es requerido por API en el flujo indicado aunque la página aclara que no aparece en listados/detalles de venta. Auth Bearer.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar opciones de costo

**Método:** `GET`  
**Ruta:** `/items/{item_id}/shipping_options`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Devuelve la tabla de costos custom para un código postal.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `zip_code` (query, obligatorio): zip_code requerido

**Solicitud**

No documentado en la fuente.

**Respuesta**

destination, options[{id,option_hash,name,currency_id,list_cost,cost,base_cost,display,speed}], buyer y custom_message.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con zip_code.

### Crear publicación con envío personalizado

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Crea un ítem cuyo shipping se configura como custom y contiene tabla de costos.

**Parámetros**

- `title` (body, obligatorio): Título de la publicación.
- `category_id` (body, obligatorio): Categoría.
- `price` (body, obligatorio): Precio.
- `shipping` (body, obligatorio): Modo, modalidad local, gratuidad, métodos y costos.

**Solicitud**

Cuerpo de publicación con shipping.mode=custom, local_pick_up, free_shipping, methods y costs[{description,cost}].

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo completo compacto con dos costos.

### Cancelar envío personalizado

**Método:** `POST`  
**Ruta:** `/shipments/{shipment_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Informa cancelación de la venta/envío.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `status` (body, obligatorio): Debe ser cancelled en el ejemplo.
- `receiver_id` (body, obligatorio): Identificador del receptor.

**Solicitud**

status=cancelled y receiver_id.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de cancelación.

### Actualizar envío de publicación

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Configura envío custom o envío gratis not_specified cuando la categoría no admite Mercado Envíos.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `shipping` (body, obligatorio): Modo custom o not_specified, gratuidad y costos.

**Solicitud**

shipping.mode, local_pick_up, free_shipping, methods y costs; para gratuito usa free_shipping=true y costs vacío.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo para costos custom y ejemplo de envío gratis.

### Actualizar tracking o estado

**Método:** `PUT`  
**Ruta:** `/shipments/{shipment_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Actualiza número de seguimiento, promesa o estado según la transición del envío.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `receiver_id` (body, obligatorio): Identificador del receptor.
- `status` (body, opcional): Estado enviado según transición.
- `speed` (body, opcional): Horas para promesa de entrega.
- `tracking_number` (body, opcional): Número de seguimiento.
- `comments` (body, opcional): Comentario opcional.

**Solicitud**

tracking_number y receiver_id; en escenarios de estado puede incluir status, speed, comments.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos para shipped, actualizar speed y delivered.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/envios-personalizados](https://developers.mercadolibre.com.co/es_co/envios-personalizados)  
**Captura:** 2026-10-08T22:51:42.998Z

---

## [Envíos Turbo](../markdown/envios-turbo.md)

Actualización indicada por la fuente: 11/02/2026. Captura: 2026-10-08T22:51:43.948Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/envios-turbo](https://developers.mercadolibre.com.co/es_co/envios-turbo)

# Envíos Turbo

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 11/02/2026  
**Captura:** 2026-10-08T22:51:43.948Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/envios-turbo](https://developers.mercadolibre.com.co/es_co/envios-turbo)

## Resumen

Describe Turbo como entregas rápidas de menos de tres horas basadas en la logística Flex. La página enumera áreas metropolitanas cubiertas, configuración de suscripciones, radio y rangos de entrega, así como identificación Turbo en los envíos.

## Contenido y conceptos documentados

- La fuente declara disponibilidad para AMBA (Argentina), São Paulo (Brasil) y Santiago (Chile), aunque la introducción destaca AMBA y São Paulo. Es requisito previo tener Flex activo y cumplir condiciones de cuenta de prueba descritas en la guía.
- Las llamadas de Flex/Turbo comparten límite de 1000 rpm. Las dimensiones y peso máximos se detallan en la sección de configuración/ítems; consultar las restricciones de producto antes de activar.
- La suscripción devuelve mode TURBO/FLEX, service_id, origin, status y configuration. Para el radio, la fuente da límites disponibles por respuesta; para rangos, los valores From/To se toman de configuration.accurate_ranges y deben enviarse todos los rangos activos al actualizar.
- La consulta de shipment identifica Turbo por la etiqueta turbo. En algunos recursos relacionados la fuente advierte diferencias de tags; no convierte esas menciones en operaciones documentadas aquí.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar radio de cobertura Turbo

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/coverage/radius/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene radio vigente y, con show_availables, límites disponibles.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `show_availables` (query, opcional): show_availables boolean opcional

**Solicitud**

No documentado en la fuente.

**Respuesta**

radius y availables.radius.min/max.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo radius=5000.

### Consultar rangos de entrega Turbo

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/delivery-ranges/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Obtiene ventanas y rangos configurados y opciones disponibles.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `show_availables` (query, opcional): show_availables boolean opcional

**Solicitud**

No documentado en la fuente.

**Respuesta**

delivery_window, delivery_ranges por día y availables (capacity, rangos, ventanas y días).

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con varios rangos horarios.

### Consultar suscripciones Turbo/Flex

**Método:** `GET`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/subscriptions/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Recupera suscripciones y service_id del usuario.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

site_id, user_id, service_id, mode, origin, status y configuration.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con modos TURBO y FLEX.

### Identificar envío Turbo

**Método:** `GET`  
**Ruta:** `/shipments/{shipment_id}`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Consulta el envío para reconocer la etiqueta Turbo.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

tags incluye turbo para identificar el tipo logístico.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de envío con tag turbo.

### Actualizar radio Turbo

**Método:** `PUT`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/coverage/radius/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Actualiza el radio de cobertura del servicio.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `radius` (body, obligatorio): Radio de cobertura configurado.

**Solicitud**

radius.

**Respuesta**

Códigos 200, 400, 401, 403, 404 y 500 documentados.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo request radius.

### Actualizar rangos Turbo

**Método:** `PUT`  
**Ruta:** `/flex/sites/{site_id}/users/{user_id}/services/{service_id}/configurations/delivery-ranges/v1`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Actualiza la configuración de rangos del vendedor.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `user_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `service_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `delivery_window` (body, opcional): Ventana de entrega.
- `delivery_ranges` (body, obligatorio): Rangos activos; deben enviarse todos los activos.

**Solicitud**

delivery_window y delivery_ranges; para conservar rangos se deben enviar todos los activos.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente exige rangos disponibles exactos de configuration.accurate_ranges.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/envios-turbo](https://developers.mercadolibre.com.co/es_co/envios-turbo)  
**Captura:** 2026-10-08T22:51:43.948Z

---

## [Errores](../markdown/errores.md)

Actualización indicada por la fuente: 10/02/2025. Captura: 2026-10-08T22:51:44.739Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/errores](https://developers.mercadolibre.com.co/es_co/errores)

# Errores

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 10/02/2025  
**Captura:** 2026-10-08T22:51:44.739Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/errores](https://developers.mercadolibre.com.co/es_co/errores)

## Resumen

Referencia de interpretación de errores del flujo de reclamos y postcompra. Agrupa fallos frecuentes de recursos, permisos, límites, disponibilidad del servicio y acciones no habilitadas; orienta si se debe corregir la solicitud, validar el usuario/documento o reintentar más tarde.

## Contenido y conceptos documentados

- La página describe situaciones como recurso no encontrado, usuario no autorizado, error interno, exceso de solicitudes, mantenimiento y timeout.
- Los errores funcionales incluyen adjunto inexistente y acciones no disponibles para el actor, entre ellas enable_partial_refund, refund, open_dispute, enable_return, send_message_to_complainant y send_message_to_mediator.
- La metadata puede tener tipos info, warning o error y acciones sugeridas como retry, check_user, check_documentation y wait_to_retry.
- La página no documenta una operación HTTP concreta; los códigos exactos dependen del endpoint que produjo el error.

La página no documenta autenticación de una operación HTTP.

## Operaciones de API

## Conceptos y recursos asociados

### Errores

Referencia de interpretación de errores del flujo de reclamos y postcompra. Agrupa fallos frecuentes de recursos, permisos, límites, disponibilidad del servicio y acciones no habilitadas; orienta si se debe corregir la solicitud, validar el usuario/documento o reintentar más tarde.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/errores](https://developers.mercadolibre.com.co/es_co/errores)  
**Captura:** 2026-10-08T22:51:44.739Z

---

## [Estados de órdenes y seguimiento](../markdown/estados-de-ordenes-me1.md)

Actualización indicada por la fuente: 17/09/2026. Captura: 2026-10-08T22:51:45.719Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/estados-de-ordenes-me1](https://developers.mercadolibre.com.co/es_co/estados-de-ordenes-me1)

# Estados de órdenes y seguimiento

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 17/09/2026  
**Captura:** 2026-10-08T22:51:45.719Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/estados-de-ordenes-me1](https://developers.mercadolibre.com.co/es_co/estados-de-ordenes-me1)

## Resumen

Explica cómo relacionar una orden con su envío y notificar cambios de estado para Mercado Envíos 1. La guía recomienda la ruta V2 seller_notifications; la V1 se marca como antigua y con descontinuación indicada para el 31/10.

## Contenido y conceptos documentados

- GET orders/{order_id}/shipments entrega el id del envío que se utilizará para notificar.
- La notificación V2 recibe status, substatus y campos de seguimiento, además de payload.service_id, comment y date. La fecha debe estar en ISO 8601 con zona horaria; tracking_number y tracking_url son opcionales pero deben enviarse juntos. service_id varía por país (MLB 11, MLA 154, MLM 231876, MLC 282578, MCO 282579, MLU 282604, MPE 361180).
- Antes de reportar un subestado de Shipped, la fuente exige registrar primero el evento con status null (en camino); si no, el shipment no se actualiza.
- La fuente advierte que la operación V1 está planificada para descontinuarse el 31/10 y recomienda V2. Para subestados de Shipped, primero debe notificarse el evento con status null (en camino). Errores documentados incluyen fecha previa al envío, remitente incorrecto, modo distinto de ME1, combinación de estado/subestado inválida, JSON inválido, rate limit, indisponibilidad temporal y error interno.

En los ejemplos de API se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Obtener envío de la orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}/shipments`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Recupera el shipment asociado a una orden ME1.

**Parámetros**

- `order_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id (shipment_id), mode, created_by, order_id, status y substatus.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con mode=me1.

### Notificar estado de envío V1 (antigua)

**Método:** `POST`  
**Ruta:** `/shipments/{shipment_id}/seller_notifications`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Ruta antigua de notificaciones; la fuente indica descontinuación para 31/10.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente identifica esta ruta como V1 antigua.

### Notificar estado de envío V2

**Método:** `POST`  
**Ruta:** `/v2/shipments/{shipment_id}/seller_notifications`  
**Autenticación:** Authorization: Bearer access token (según los ejemplos de la fuente).

Registra una actualización de estado/tracking de ME1.

**Parámetros**

- `shipment_id` (path, obligatorio): Identificador o tipo indicado en la ruta de la operación.
- `payload` (body, obligatorio): Objeto con service_id, comment y date.
- `tracking_number` (body, opcional): Opcional; debe acompañarse con tracking_url.
- `tracking_url` (body, opcional): Opcional; debe acompañarse con tracking_number.
- `status` (body, obligatorio): shipped, delivered o not_delivered.
- `substatus` (body, obligatorio): Debe enviarse; JSON null si no aplica.

**Solicitud**

payload.service_id requerido; payload.date requerido en ISO 8601 con zona horaria; payload.comment opcional; tracking_number y tracking_url opcionales pero deben enviarse juntos; status requerido (shipped, delivered o not_delivered); substatus debe estar presente y puede ser JSON null. service_id por site: MLB=11, MLA=154, MLM=231876, MLC=282578, MCO=282579, MLU=282604, MPE=361180.

**Respuesta**

HTTP 200 con {status: OK}; error con status_code, error_code, message, timestamp y request_id.

**Errores documentados**

- 400 event_date_before_shipment_creation_date: fecha anterior a la creación del envío.
- 403 forbidden_client: caller.id no corresponde al remitente del envío.
- 400 shipment_mode_is_not_me1: el envío no pertenece a ME1.
- 403 bad_request: combinación status-substatus no permitida.
- 400 invalid_seller_json_format: formato JSON inválido.
- 429: límite de tasa alcanzado.
- 503: servicio temporalmente no disponible.
- 500: error interno de procesamiento.

**Ejemplos**

- Ejemplo de notificación delivered con payload y tracking.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/estados-de-ordenes-me1](https://developers.mercadolibre.com.co/es_co/estados-de-ordenes-me1)  
**Captura:** 2026-10-08T22:51:45.719Z

---

## [Experiencia de compra](../markdown/experiencia-de-compra.md)

Actualización indicada por la fuente: 03/02/2026. Captura: 2026-10-08T22:51:47.114Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/experiencia-de-compra](https://developers.mercadolibre.com.co/es_co/experiencia-de-compra)

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

---

## [Feedback de una venta](../markdown/feedback-sobre-venta.md)

Actualización indicada por la fuente: 29/12/2025. Captura: 2026-10-08T22:51:48.833Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/feedback-sobre-venta](https://developers.mercadolibre.com.co/es_co/feedback-sobre-venta)

# Feedback de una venta

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:51:48.833Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/feedback-sobre-venta](https://developers.mercadolibre.com.co/es_co/feedback-sobre-venta)

## Resumen

Documenta cómo consultar y gestionar la opinión de una venta: registrar feedback, responderlo, recuperar el feedback de una orden y consultar o actualizar un feedback individual. Distingue ventas concretadas y no concretadas y explica las restricciones relacionadas con el estado y la vigencia de la orden.

## Contenido y conceptos documentados

### Flujo y campos

- Las llamadas muestran autenticación `Bearer`. La fuente ejemplifica feedback con `fulfilled`, `rating`, `message`, `reason` y `restock_item`; el texto del mensaje debe ser menor a 160 caracteres. Para feedback no concretado (`fulfilled=false`) se documenta `reason`.
- El vendedor no puede registrar un feedback no concretado una vez expirada la orden. En envíos personalizados o ME1, se recomienda esperar certeza de entrega antes de informar el resultado. El feedback de una venta no afecta la reputación del vendedor.
- El recurso de una orden presenta información de compra y venta, incluidos identificadores, rol, fecha, calificación, mensaje, motivo y estado de concreción. El vendedor puede consultar feedback hasta cinco años, según la página.
- Si se intenta enviar feedback repetido, la página indica HTTP 400; también menciona `not_fulfilled_feedback_in_order_expired`. Los demás detalles de autenticación, cuerpos y respuestas no visibles para cada llamada: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Consultar feedback

**Método:** `GET`  
**Ruta:** `/feedback/$FEEDBACK_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera los datos de un feedback individual.

**Parámetros**

- `FEEDBACK_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- order_id
- reason
- item
- role
- extended_feedback
- date_created
- fulfilled
- rating
- message

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página presenta un ejemplo de consulta por ID.

### Consultar feedback de orden

**Método:** `GET`  
**Ruta:** `/orders/$ORDER_ID/feedback`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera feedback relacionado con una orden para comprador y vendedor.

**Parámetros**

- `ORDER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- sale
- purchase
- id
- order_id
- reason
- item
- role
- extended_feedback
- date_created
- fulfilled
- rating
- message

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La documentación indica consulta por el vendedor hasta cinco años.

### Responder feedback

**Método:** `POST`  
**Ruta:** `/feedback/$FEEDBACK_ID/reply`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Publica una respuesta del vendedor a un feedback recibido.

**Parámetros**

- `FEEDBACK_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "reply"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La solicitud se ejemplifica con reply.

### Crear feedback de una venta

**Método:** `POST`  
**Ruta:** `/orders/$ORDER_ID/feedback`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Registra la calificación y comentario del vendedor sobre una orden.

**Parámetros**

- `ORDER_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "fulfilled",
    "rating",
    "message (menos de 160 caracteres)",
    "reason (si fulfilled=false)",
    "restock_item"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": 400,   "meaning": "not_fulfilled_feedback_in_order_expired: la orden expiró para feedback no concretado." } ```
- ```json {   "code": 400,   "meaning": "El feedback repetido no se acepta." } ```

**Ejemplos**

- El texto recomienda esperar confirmación de entrega en envíos personalizados o ME1.

### Actualizar feedback

**Método:** `PUT`  
**Ruta:** `/feedback/$FEEDBACK_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza los campos permitidos de un feedback existente.

**Parámetros**

- `FEEDBACK_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "fulfilled",
    "rating",
    "message"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/feedback-sobre-venta](https://developers.mercadolibre.com.co/es_co/feedback-sobre-venta)  
**Captura:** 2026-10-08T22:51:48.833Z

---

## [Flete dinámico](../markdown/flete-dinamico.md)

Actualización indicada por la fuente: 02/09/2026. Captura: 2026-10-08T22:51:50.332Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/flete-dinamico](https://developers.mercadolibre.com.co/es_co/flete-dinamico)

# Flete dinámico

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 02/09/2026  
**Captura:** 2026-10-08T22:51:50.332Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/flete-dinamico](https://developers.mercadolibre.com.co/es_co/flete-dinamico)

## Resumen

La documentación presenta Flete Dinámico para integradores de Mercado Envíos 1 (ME1): métricas de integración, descarga y actualización de tarifas, consulta del procesamiento y simulación de cotizaciones. El flujo de actualización es asíncrono y comunica su resultado mediante un callback.

## Contenido y conceptos documentados

### Flujo, campos y restricciones

- Las rutas usan `Bearer`; las operaciones de tarifas y cotización indican que el token debe contener `caller_id`. La consulta de métricas está restringida a integradores habilitados/validados como partner.
- Las métricas requieren `site_id`, `ts_from` y `ts_to` en ISO-8601 UTC; `seller_id` es opcional. Se listan sitios `MLA`, `MLB`, `MCO`, `MLC`, `MLM`, `MLU`, `MBO`, `MPE` y `MLV`. La respuesta agrega latencia, disponibilidad, contingencias, caché, revalidaciones y conteos/errores. La fuente atribuye 400 a parámetros/formato inválido, 401 a token o client ID inválido y 403 a cliente no autorizado o seller fuera del partner; también lista 500 y 503 para errores del partner/upstream y autenticación.
- La plantilla se descarga con `site`. La actualización usa archivo XLSX en `multipart/form-data` (máximo 7 MB), `site`, `service` y `callback_url` HTTPS. El callback no debe usar localhost ni IP privada. La fuente señala respuesta con `resource_id`, webhook y estados/errores/advertencias de procesamiento.
- Para simular, `declared_value`, ancho, alto, largo y peso deben ser positivos; las dimensiones se expresan en cm y el peso en gramos. `destination.type` acepta `zipcode` o `city`. Se documenta un límite de 50 solicitudes por minuto; los errores incluyen 400 por datos inválidos, 401 por token/client/caller inválido, 403 si ME1 no está habilitado, 404 si no existe el recurso, 429 por límite, 500 por error de cálculo/datos y 503 por autenticación o calculadora.
- Para la plantilla se documentan 400 por `site` inválido/ausente, 401 por token inválido, 404 si no existe para el sitio, 500 al leer/codificar y 503 si falla autenticación. Para carga, 400 cubre parámetros, callback o archivo inválido, 401 token/caller ausente, 403 ME1 deshabilitado, 404 vendedor inexistente, 429 límite, 500 error interno y 503 autenticación. La consulta por `resource_id` documenta 400/401/403/404/500/503 con causas de recurso, caller, habilitación ME1, vendedor o descarga/codificación. La página también establece restricciones para tablas de contingencia (rangos no duplicados, solapados, invertidos o inválidos). Campos no descritos: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Métricas de ME1

**Método:** `GET`  
**Ruta:** `/shipping/me1/sites/{site_id}/metrics`  
**Autenticación:** Bearer token; la autenticación valida acceso de partner

Consulta indicadores de desempeño de la integración ME1 para un sitio y período.

**Parámetros**

- `site_id` (path, obligatorio): Sitio habilitado; la página enumera MLA, MLB, MCO, MLC, MLM, MLU, MBO, MPE y MLV.
- `ts_from` (query, obligatorio): Inicio ISO-8601 en UTC.
- `ts_to` (query, obligatorio): Fin ISO-8601 en UTC.
- `seller_id` (query, opcional): Filtra por vendedor.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- site_id
- seller_id
- partner
- from
- to
- summary.latency_avg_ms
- summary.latency_max_ms
- summary.uptime_pct
- summary.contingency_pct
- summary.cache_pct
- summary.revalidation_pct
- summary.errors[].item
- summary.errors[].pct
- summary.totals.req_count
- summary.totals.error_count
- summary.totals.contingency_count
- summary.totals.revalidation_count
- summary.totals.cache_hit_count

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Parámetros inválidos, falta site_id o el timestamp/seller_id tiene formato inválido." } ```
- ```json {   "code": 401,   "meaning": "Token o client ID inválido." } ```
- ```json {   "code": 403,   "meaning": "Cliente no autorizado o seller_id no permitido para el partner." } ```
- ```json {   "code": 500,   "meaning": "Error del partner o del servicio upstream." } ```
- ```json {   "code": 503,   "meaning": "Servicio de autenticación no disponible." } ```

**Ejemplos**

- Ejemplo de consulta mensual para MLB, con y sin seller_id.

### Consultar procesamiento de tarifas

**Método:** `GET`  
**Ruta:** `/shipping/me1/v1/tariff/{resource_id}`  
**Autenticación:** Bearer token; el token debe identificar caller_id

Consulta el estado y contenido de una carga de tarifas por su identificador de recurso.

**Parámetros**

- `resource_id` (path, obligatorio): Identificador UUID del recurso.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- resource_id
- status
- filename
- content (Base64)
- encoding
- mimetype

**Errores documentados**

- ```json {   "code": 400,   "meaning": "resource_id ausente o formato de caller_id inválido." } ```
- ```json {   "code": 401,   "meaning": "Token, client ID o caller_id inválido/ausente." } ```
- ```json {   "code": 403,   "meaning": "El vendedor no tiene ME1 habilitado." } ```
- ```json {   "code": 404,   "meaning": "No se encontró el tarifario para resource_id." } ```
- ```json {   "code": 500,   "meaning": "Error al recuperar el tarifario, descargar el archivo o codificar su contenido." } ```
- ```json {   "code": 503,   "meaning": "Servicio de autenticación no disponible." } ```

**Ejemplos**

- Estados documentados: Active, Created, Validating, Error e Inactive.

### Descargar plantilla de tarifas

**Método:** `GET`  
**Ruta:** `/shipping/me1/v1/tariff/template`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Descarga la plantilla XLSX de tarifas correspondiente al sitio.

**Parámetros**

- `site` (query, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Parámetro site ausente o inválido." } ```
- ```json {   "code": 401,   "meaning": "Token inválido." } ```
- ```json {   "code": 404,   "meaning": "Plantilla no encontrada para el site." } ```
- ```json {   "code": 500,   "meaning": "Error al leer o codificar el archivo." } ```
- ```json {   "code": 503,   "meaning": "Servicio de autenticación no disponible." } ```

**Ejemplos**

- Ejemplo con site=MLB.

### Simular cotización

**Método:** `POST`  
**Ruta:** `/shipping/me1/v1/quotation/simulate`  
**Autenticación:** Bearer token; el token debe identificar caller_id

Calcula cotizaciones ME1 para valor declarado, paquete y destino.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "declared_value (> 0)",
    "dimensions.width, dimensions.height, dimensions.length (cm, > 0)",
    "weight (gramos, entero positivo)",
    "destination.type (zipcode o city)",
    "destination.value"
  ]
}
```

**Respuesta**

- quotations[]: price
- quotations[]: speed
- quotations[]: service
- quotations[]: shipping_time
- quotations[]: handling_time
- quotations[]: promise

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Parámetros ausentes o inválidos; valores, dimensiones positivos y destino válido." } ```
- ```json {   "code": 401,   "meaning": "Token, client ID o caller_id inválido/ausente." } ```
- ```json {   "code": 403,   "meaning": "El vendedor no tiene ME1 habilitado." } ```
- ```json {   "code": 404,   "meaning": "Recurso no encontrado." } ```
- ```json {   "code": 429,   "meaning": "Límite de tasa excedido (50 RPM)." } ```
- ```json {   "code": 500,   "meaning": "Error al simular la cotización o recuperar datos del vendedor." } ```
- ```json {   "code": 503,   "meaning": "Autenticación o calculadora no disponible." } ```

**Ejemplos**

- Límite publicado: 50 solicitudes por minuto; el token debe contener caller_id.

### Actualizar tarifas ME1

**Método:** `POST`  
**Ruta:** `/shipping/me1/v1/tariff/update`  
**Autenticación:** Bearer token; el token debe identificar caller_id

Envía un archivo de tarifas para validación y actualización asíncrona.

**Parámetros**

- `site` (form-data, obligatorio)
- `service` (form-data, obligatorio)
- `file` (form-data, obligatorio): Archivo XLSX de máximo 7 MB.
- `callback_url` (form-data, obligatorio): URL HTTPS; no localhost ni IP privada.

**Solicitud**

```json
{
  "content_type": "multipart/form-data",
  "fields": [
    "site",
    "service",
    "file (.xlsx, máximo 7 MB)",
    "callback_url"
  ]
}
```

**Respuesta**

- resource_id
- callback webhook: event
- timestamp
- data.resource_id
- data.seller_id
- data.site_id
- data.service
- data.status
- data.errors
- data.warnings

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Parámetros inválidos, callback_url inválido o archivo mayor de 7 MB." } ```
- ```json {   "code": 401,   "meaning": "Token inválido o caller_id ausente." } ```
- ```json {   "code": 403,   "meaning": "El vendedor no tiene ME1 habilitado." } ```
- ```json {   "code": 404,   "meaning": "Vendedor no encontrado." } ```
- ```json {   "code": 429,   "meaning": "Límite de tasa excedido." } ```
- ```json {   "code": 500,   "meaning": "Error interno del servidor." } ```
- ```json {   "code": 503,   "meaning": "Servicio de autenticación no disponible." } ```

**Ejemplos**

- El token debe contener caller_id; la respuesta y procesamiento se notifican en forma asíncrona.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/flete-dinamico](https://developers.mercadolibre.com.co/es_co/flete-dinamico)  
**Captura:** 2026-10-08T22:51:50.332Z

---

## [Gestionar evidencia de reclamos](../markdown/gestionar-evidencia-de-reclamos.md)

Actualización indicada por la fuente: 13/04/2025. Captura: 2026-10-08T22:51:53.737Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/gestionar-evidencia-de-reclamos](https://developers.mercadolibre.com.co/es_co/gestionar-evidencia-de-reclamos)

# Gestionar evidencia de reclamos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/04/2025  
**Captura:** 2026-10-08T22:51:53.737Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestionar-evidencia-de-reclamos](https://developers.mercadolibre.com.co/es_co/gestionar-evidencia-de-reclamos)

## Resumen

Describe la gestión de evidencias de envío en reclamos: consultar evidencias, subir y descargar archivos, registrar datos de despacho/entrega y declarar una gestión o promesa de envío. El recurso se organiza por identificador de reclamo.

## Contenido y conceptos documentados

### Evidencias y restricciones

- Las llamadas documentan autenticación `Bearer`. Los adjuntos admiten JPG, PNG o PDF de hasta 5 MB; la subida devuelve metadatos del archivo y un identificador que se usa en la ruta de consulta/descarga. La solicitud de ejemplo incluye el encabezado `x-public: true`.
- La evidencia de envío contiene datos como tipo, método/empresa de envío, agencia de destino, fechas, datos del receptor, número de seguimiento y adjuntos. La página distingue entrega por correo, encomienda, entrega personal y correo electrónico, con requisitos de datos según modalidad.
- Las fechas pueden seguir formato largo o corto según el ejemplo. No se deben remitir evidencias de envío en una mediación/disputa; una evidencia enviada no se puede modificar.
- Los códigos de error por operación y los cuerpos de respuesta que la captura no detalla: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /claims/actions/evidences

La fuente menciona la ruta /claims/actions/evidences, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/actions/evidences`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar adjunto de evidencia

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/attachments-evidences/$ATTACHMENT_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene metadatos del archivo adjunto a una evidencia.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)
- `ATTACHMENT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- filename
- original_filename
- size
- date_created
- type

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Descargar adjunto de evidencia

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/attachments-evidences/$ATTACHMENTS_ID/download`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Descarga el archivo asociado a la evidencia.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)
- `ATTACHMENTS_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Listar evidencias del reclamo

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/evidences`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera las evidencias de envío asociadas a un reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- attachments
- type
- date_shipped
- date_delivered
- destination_agency
- receiver_email
- receiver_id
- receiver_name
- shipping_company_name
- shipping_method
- tracking_number
- handling_date

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de consulta de evidencias por reclamo.

### Registrar evidencia de envío

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/actions/evidences`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Registra evidencia de despacho o entrega para el reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "type",
    "shipping_method",
    "shipping_company_name",
    "destination_agency",
    "date_shipped",
    "date_delivered",
    "receiver_email",
    "receiver_id",
    "receiver_name",
    "tracking_number",
    "attachments"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra ejemplos diferenciados por modalidad: mail, entrusted, personal_delivery y email; los campos requeridos dependen del tipo.

### Cargar adjunto de evidencia

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/attachments-evidences`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Carga un archivo para asociarlo como evidencia del reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "multipart/form-data",
  "fields": [
    "file (JPG, PNG o PDF; máximo 5 MB)"
  ]
}
```

**Respuesta**

- user_id
- file_name
- attachment_id (file_name)

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El ejemplo de carga usa el encabezado x-public: true.

### Registrar gestión de envío

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/evidences`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Registra una gestión/promesa de envío del reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "type: handling_shipping_evidence",
    "handling_date"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Referencia HTTP POST /claims/actions/evidences

**Método:** `POST`  
**Ruta:** `/claims/actions/evidences`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /claims/actions/evidences. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP POST /post-purchase/v1/claims/949903015/act

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/949903015/act`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /post-purchase/v1/claims/949903015/act. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestionar-evidencia-de-reclamos](https://developers.mercadolibre.com.co/es_co/gestionar-evidencia-de-reclamos)  
**Captura:** 2026-10-08T22:51:53.737Z

---

## [Gestionar guía de talles](../markdown/guias-de-talles.md)

Actualización indicada por la fuente: 09/07/2026. Captura: 2026-10-08T22:51:54.750Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/guias-de-talles](https://developers.mercadolibre.com.co/es_co/guias-de-talles)

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

---

## [Gestionar mensajes de un reclamo](../markdown/gestionar-mensaje-de-un-reclamo.md)

Actualización indicada por la fuente: 14/07/2024. Captura: 2026-10-08T22:51:55.861Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/gestionar-mensaje-de-un-reclamo](https://developers.mercadolibre.com.co/es_co/gestionar-mensaje-de-un-reclamo)

# Gestionar mensajes de un reclamo

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 14/07/2024  
**Captura:** 2026-10-08T22:51:55.861Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestionar-mensaje-de-un-reclamo](https://developers.mercadolibre.com.co/es_co/gestionar-mensaje-de-un-reclamo)

## Resumen

Documenta el intercambio de mensajes y archivos adjuntos de un reclamo: consultar mensajes propios, cargar adjuntos, enviar un mensaje según las acciones disponibles y consultar o descargar archivos vinculados.

## Contenido y conceptos documentados

### Reglas de mensajería

- Las llamadas usan autenticación `Bearer`. Los adjuntos permitidos son JPG, PNG y PDF hasta 5 MB; el nombre debe tener como máximo 125 caracteres y ajustarse a `[a-zA-Z0-9._-]`.
- Para enviar mensajes, el reclamo debe ofrecer la acción `send_message`. El cuerpo documenta `receiver_role`, `message` y, opcionalmente, los nombres devueltos al cargar adjuntos. El ejemplo de envío devuelve HTTP 201.
- Solo se muestran los mensajes moderados propios. La respuesta incluye remitente/destinatario, mensaje y traducción, fechas, adjuntos, estado, etapa, moderación, repetición y motivo. Se documentan estados `available`, `moderated`, `rejected`, `pending_translation` y resultados de moderación `clean`, `rejected`, `pending`, `non_moderated`; la fuente también presenta `OUT_OF_PLACE_LANGUAGE`.
- Los roles posibles dependen del reclamo; la página indica que `warehouse_dispatcher` no puede enviar mensajes. Los códigos de error por operación: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /claims/{CLAIMS_ID}/messages

La fuente menciona la ruta /claims/{CLAIMS_ID}/messages, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/{CLAIMS_ID}/messages`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar adjunto de mensaje

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/attachments/$ATTACHMENTS_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera metadatos de un archivo adjunto.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)
- `ATTACHMENTS_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- filename
- original_filename
- size
- date_created
- type

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Descargar adjunto de mensaje

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/attachments/$ATTACHMENTS_ID/download`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Descarga un archivo adjunto al reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)
- `ATTACHMENTS_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar mensajes del reclamo

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/messages`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista los mensajes visibles asociados al reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- sender_role
- receiver_role
- message
- translated_message
- date_created
- date_read
- attachments
- status
- stage
- message_moderation
- repeated

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La respuesta considera estados available, moderated, rejected y pending_translation; moderación clean, rejected, pending o non_moderated.

### Enviar mensaje en reclamo

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/actions/send-message`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Envía un mensaje a un rol participante si la acción está disponible para el reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "receiver_role",
    "message",
    "attachments (nombres de archivos, opcional)"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente indica HTTP 201 Created; requiere acción send_message y warehouse_dispatcher no puede enviar.

### Cargar adjunto del mensaje

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/attachments`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Carga un archivo para adjuntarlo a un mensaje del reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "multipart/form-data",
  "fields": [
    "file (JPG, PNG o PDF; máximo 5 MB)",
    "filename (hasta 125 caracteres; patrón [a-zA-Z0-9._-])"
  ]
}
```

**Respuesta**

- filename

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Referencia HTTP GET /claims/{CLAIMS_ID}/messages

**Método:** `GET`  
**Ruta:** `/claims/{CLAIMS_ID}/messages`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /claims/{CLAIMS_ID}/messages. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP POST /post-purchase/v1/claims/5204934310/act

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/5204934310/act`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /post-purchase/v1/claims/5204934310/act. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP POST /post-purchase/v1/claims/{CLAIM_ID}/actions/se

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/{CLAIM_ID}/actions/se`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /post-purchase/v1/claims/{CLAIM_ID}/actions/se. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestionar-mensaje-de-un-reclamo](https://developers.mercadolibre.com.co/es_co/gestionar-mensaje-de-un-reclamo)  
**Captura:** 2026-10-08T22:51:55.861Z

---

## [Gestionar promociones](../markdown/central-de-promociones.md)

Actualización indicada por la fuente: 09/06/2026. Captura: 2026-10-08T22:51:58.602Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/central-de-promociones](https://developers.mercadolibre.com.co/es_co/central-de-promociones)

# Gestionar promociones

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 09/06/2026  
**Captura:** 2026-10-08T22:51:58.602Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/central-de-promociones](https://developers.mercadolibre.com.co/es_co/central-de-promociones)

## Resumen

La Central de promociones unifica consultas y acciones sobre campañas, candidatos, ofertas, promociones asociadas a ítems y listas de exclusión de vendedores o publicaciones. Las solicitudes documentadas usan la versión de aplicación `v2`.

## Contenido y conceptos documentados

### Parámetros y restricciones

- Las llamadas muestran `Authorization: Bearer $ACCESS_TOKEN` y el query `app_version=v2`. Las rutas de detalle/listado también requieren `USER_ID`, `CANDIDATE_ID`, `OFFERS_ID`, `PROMOTION_ID` o `ITEM_ID` según el recurso; la consulta de promoción recibe `promotion_type`.
- El listado de ítems de una promoción admite filtros `item_id`, `status` (`started`, `pending`, `candidate`) y `status_item` (`active`, `paused`, por defecto `active`). Paginación: `limit` predeterminado 50 y máximo 50, más `search_after` (la documentación indica el alias anterior `searchAfter`), con cursor válido por cinco minutos y navegación hacia adelante.
- El borrado masivo de ofertas no aplica a DOD/LIGHTNING. La página señala errores `423_ENTITY_LOCKED` y `400_BAD_REQUEST`; la respuesta incluye `successful_ids` y `errors`.
- La lista de exclusión usa `exclusion_status` como texto `true`/`false`; la operación por ítem usa además `item_id`. Para pruebas se requieren usuarios/publicaciones de prueba y query `version=test`. Los cupones de campaña para vendedores se indican solo para MLB.
- En fichas de promoción se muestran estados, precios y, para ciertas ofertas, campos de boost como `boosted_offer`, `discount_meli_boosted_percentage`, `discount_meli_boost_amount` y `total_price_for_boosted_offer`. Detalles no especificados por cada ruta: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Eliminar ofertas del ítem

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina en bloque ofertas promocionales admitidas para el ítem.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- successful_ids
- errors

**Errores documentados**

- ```json {   "code": "423_ENTITY_LOCKED",   "meaning": "Entidad bloqueada." } ```
- ```json {   "code": "400_BAD_REQUEST",   "meaning": "Solicitud inválida." } ```

**Ejemplos**

- No aplica a ofertas DOD ni LIGHTNING.

### Consultar candidato

**Método:** `GET`  
**Ruta:** `/seller-promotions/candidates/$CANDIDATE_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el artículo candidato, promoción asociada y estado.

**Parámetros**

- `CANDIDATE_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- type
- status
- item_id
- promotion_id
- start_date
- finish_date
- deadline_date
- name
- benefits

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El identificador se recibe mediante notificación pública de candidatos.

### Consultar exclusiones del vendedor

**Método:** `GET`  
**Ruta:** `/seller-promotions/exclusion-list/seller`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista publicaciones excluidas del vendedor y sus estados.

**Parámetros**

- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- excluded
- not_excluded
- paging

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar exclusión de ítem del vendedor

**Método:** `GET`  
**Ruta:** `/seller-promotions/exclusion-list/seller/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta si un ítem está incluido en la lista de exclusión del vendedor.

**Parámetros**

- `item_id` (path, obligatorio)
- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- item_id
- exclusion_status

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Promociones del ítem

**Método:** `GET`  
**Ruta:** `/seller-promotions/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista las promociones asociadas a una publicación.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- results[].id
- results[].type
- results[].status
- results[].price
- results[].boosted_offer
- results[].discount_meli_boosted_percentage
- results[].discount_meli_boost_amount
- results[].total_price_for_boosted_offer

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Incluye tipos de promoción de ofertas y campos de boost cuando apliquen.

### Consultar oferta

**Método:** `GET`  
**Ruta:** `/seller-promotions/offers/$OFFERS_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta una oferta promocional, artículo asociado y estado.

**Parámetros**

- `OFFERS_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- offer_id
- id
- type
- status
- item_id
- promotion_id
- start_date
- finish_date
- deadline_date
- name
- benefits
- ref_id

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La oferta se identifica a partir de la notificación pública correspondiente.

### Detalle de promoción

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/$PROMOTION_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalle de una campaña por identificador y tipo.

**Parámetros**

- `PROMOTION_ID` (path, obligatorio)
- `promotion_type` (query, obligatorio)
- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- type
- status
- start_date
- finish_date
- deadline_date
- name
- benefits
- meli_percent
- seller_percent
- buy_quantity
- pay_quantity
- item_discount_percent

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Ítems de promoción

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/$PROMOTION_ID/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista artículos participantes y permite filtrar por artículo, estado y paginar.

**Parámetros**

- `PROMOTION_ID` (path, obligatorio)
- `promotion_type` (query, obligatorio)
- `item_id` (query, opcional)
- `status` (query, opcional): started, pending o candidate.
- `status_item` (query, opcional): active o paused; por defecto active.
- `app_version` (query, obligatorio): La página usa v2.
- `limit` (query, opcional): Predeterminado 50; máximo 50.
- `search_after` (query, opcional): Cursor hacia adelante con vigencia de cinco minutos; anteriormente se aceptaba searchAfter.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- results[].item_id
- results[].status
- results[].price
- results[].original_price
- results[].min_discounted_price
- results[].max_discounted_price
- results[].suggested_discounted_price
- paging

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Parámetros inválidos, por ejemplo status_item no permitido." } ```

**Ejemplos**

- La fuente muestra ejemplos con item_id, status=started y status_item=active.

### Promociones del usuario

**Método:** `GET`  
**Ruta:** `/seller-promotions/users/$USER_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista campañas y promociones relacionadas con el vendedor.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- results
- paging

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Solicitud de ejemplo con app_version=v2.

### Actualizar exclusión del ítem

**Método:** `POST`  
**Ruta:** `/seller-promotions/exclusion-list/item`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega o actualiza el estado de exclusión de una publicación.

**Parámetros**

- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "item_id",
    "exclusion_status (texto true o false)"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Actualizar exclusión del vendedor

**Método:** `POST`  
**Ruta:** `/seller-promotions/exclusion-list/seller`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza el estado de exclusión del vendedor.

**Parámetros**

- `app_version` (query, obligatorio): La página usa v2.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "exclusion_status (texto true o false)"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/central-de-promociones](https://developers.mercadolibre.com.co/es_co/central-de-promociones)  
**Captura:** 2026-10-08T22:51:58.602Z

---

## [Gestionar reclamos](../markdown/que-es-un-reclamo.md)

Actualización indicada por la fuente: 20/08/2026. Captura: 2026-10-08T22:52:00.017Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/que-es-un-reclamo](https://developers.mercadolibre.com.co/es_co/que-es-un-reclamo)

# Gestionar reclamos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 20/08/2026  
**Captura:** 2026-10-08T22:52:00.017Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/que-es-un-reclamo](https://developers.mercadolibre.com.co/es_co/que-es-un-reclamo)

## Resumen

Presenta el modelo de reclamos posventa y las consultas para recuperar un reclamo, personalizar su búsqueda, consultar motivos, revisar historial de acciones y estados, y saber si afecta la reputación. La guía relaciona estos recursos con notificaciones de reclamos y acciones.

## Contenido y conceptos documentados

### Modelo, búsqueda y campos

- Las operaciones documentan `Bearer`. Un reclamo reúne `id`, `resource_id`, `status`, `type`, `stage`, versión/cantidad, recurso, motivo, participantes y acciones disponibles, resolución, fechas, cobertura, sitio y entidades relacionadas. Los estados incluyen `opened`/`closed`; tipos visibles incluyen mediación, devolución, fulfillment, caso ML, cancelación, cambio y servicio.
- La búsqueda requiere al menos un filtro real: offset/limit/sort solos producen HTTP 400. `resource_id` depende de `resource`; `players.user_id` depende de `players.role`; `order_id` y `pack_id` son mutuamente excluyentes. `offset` por defecto 0 y máximo 9999; `limit` por defecto 30 y máximo 100; `offset + limit` debe ser menor que 10000. Las fechas se expresan con milisegundos. Se recomienda acotar por rol y usuario; buscar solo por estado puede ser costoso y sujeto a límites.
- Los filtros documentados incluyen `id`, `type`, `stage`, `status`, recurso e ID, `reason_id`, `site_id`, jugador/rol, orden o paquete, pago, reclamo padre y rangos de fechas de creación/actualización.
- `detail` añade `due_date`, responsable, título, descripción y problema. Motivos, historial de acciones/estados y `affects-reputation` tienen sus propios campos; la respuesta de reputación puede indicar `affected`, `not_affected` o `not_applies`, además de incentivo y vencimiento. Errores de las llamadas individuales: No documentado en la fuente salvo la búsqueda inválida HTTP 400.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /claims/{CLAIM_ID}/detail

La fuente menciona la ruta /claims/{CLAIM_ID}/detail, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/{CLAIM_ID}/detail`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /v1/claims/search

La fuente menciona la ruta /v1/claims/search, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/v1/claims/search`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /claims/reasons/{REASON_ID}

La fuente menciona la ruta /claims/reasons/{REASON_ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/reasons/{REASON_ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /claims/{CLAIM_ID}

La fuente menciona la ruta /claims/{CLAIM_ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/{CLAIM_ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /claims/affects-reputation

La fuente menciona la ruta /claims/affects-reputation, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/affects-reputation`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /claims/detail

La fuente menciona la ruta /claims/detail, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/detail`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /claims/actions-history

La fuente menciona la ruta /claims/actions-history, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/actions-history`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar reclamo

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene información principal, participantes, acciones disponibles y resolución del reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- resource_id
- status
- type
- stage
- claim_version
- claimed_quantity
- parent_id
- resource
- reason_id
- fulfilled
- quantity_type
- players
- available_actions
- resolution
- reason
- date_created
- last_updated
- benefited
- closed_by
- applied_coverage
- site_id
- related_entities

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Estados: opened y closed; tipos documentados incluyen mediations, return, fulfillment, ml_case, cancel_sale, cancel_purchase, change y service.

### Historial de acciones

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/actions-history`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta las acciones registradas y sus participantes.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- action_name
- player_role
- action_reason_id
- claim_stage
- claim_status
- date_created

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar impacto en reputación

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/affects-reputation`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Determina si el reclamo afecta la reputación del vendedor.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- affects_reputation (affected, not_affected o not_applies)
- has_incentive
- due_date

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Detalle de reclamo

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/detail`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta datos de vencimiento, responsable y descripción del problema.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- due_date
- action_responsible
- title
- description
- problem

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Historial de estados

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/status-history`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta las transiciones de estado y etapa del reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- stage
- status
- date
- change_by

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar motivo de reclamo

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/reasons/$REASON_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene definición, configuración y flujos permitidos de un motivo.

**Parámetros**

- `REASON_ID` (path, obligatorio)
- `flow` (query, opcional)
- `delivered` (query, opcional)
- `deep` (query, opcional)
- `name` (query, opcional)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- flow
- name
- detail
- position
- group
- site_id
- settings
- allowed_flows
- expected_resolutions
- rules_engine_triage
- parent
- children_title
- status
- date_created

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra ejemplo de reason_id PDD9939.

### Buscar reclamos

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca reclamos mediante filtros dependientes y paginación acotada.

**Parámetros**

- `id` (query, opcional)
- `type` (query, opcional)
- `stage` (query, opcional)
- `status` (query, opcional)
- `resource` (query, opcional)
- `resource_id` (query, opcional): Requiere resource.
- `reason_id` (query, opcional)
- `site_id` (query, opcional)
- `players.role` (query, opcional)
- `players.user_id` (query, opcional): Requiere players.role.
- `order_id` (query, opcional): Mutuamente excluyente con pack_id.
- `pack_id` (query, opcional): Mutuamente excluyente con order_id.
- `payment_id` (query, opcional)
- `parent_id` (query, opcional)
- `date_created` (query, opcional)
- `last_updated` (query, opcional)
- `offset` (query, opcional): Por defecto 0; máximo 9999.
- `limit` (query, opcional): Por defecto 30; máximo 100; offset+limit menor que 10000.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- paging.total
- paging.offset
- paging.limit
- data[]

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Sin filtro real; dependencias inválidas; paginación sin filtro o parámetros incompatibles." } ```

**Ejemplos**

- Los filtros de fecha usan timestamps con milisegundos. La fuente recomienda filtrar por rol y usuario; desaconseja consulta amplia solo por status.

### Referencia HTTP GET /claims/affects-reputation

**Método:** `GET`  
**Ruta:** `/claims/affects-reputation`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /claims/affects-reputation. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /claims/{CLAIM_ID}

**Método:** `GET`  
**Ruta:** `/claims/{CLAIM_ID}`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /claims/{CLAIM_ID}. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /claims/reasons/{REASON_ID}

**Método:** `GET`  
**Ruta:** `/claims/reasons/{REASON_ID}`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /claims/reasons/{REASON_ID}. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /claims/detail

**Método:** `GET`  
**Ruta:** `/claims/detail`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /claims/detail. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /v1/claims/search

**Método:** `GET`  
**Ruta:** `/v1/claims/search`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /v1/claims/search. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /claims/actions-history

**Método:** `GET`  
**Ruta:** `/claims/actions-history`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /claims/actions-history. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/que-es-un-reclamo](https://developers.mercadolibre.com.co/es_co/que-es-un-reclamo)  
**Captura:** 2026-10-08T22:52:00.017Z

---

## [Gestionar resolución de reclamos](../markdown/gestionar-resolucion-de-reclamos.md)

Actualización indicada por la fuente: 08/09/2025. Captura: 2026-10-08T22:52:01.135Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/gestionar-resolucion-de-reclamos](https://developers.mercadolibre.com.co/es_co/gestionar-resolucion-de-reclamos)

# Gestionar resolución de reclamos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 08/09/2025  
**Captura:** 2026-10-08T22:52:01.135Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestionar-resolucion-de-reclamos](https://developers.mercadolibre.com.co/es_co/gestionar-resolucion-de-reclamos)

## Resumen

Describe las opciones del vendedor para escalar un reclamo a mediación y consultar o proponer resoluciones: devolución, reembolso completo o parcial y devolución del producto. Las acciones permitidas dependen del estado, la etapa y las resoluciones esperadas del reclamo.

## Contenido y conceptos documentados

### Resoluciones y condiciones

- Las llamadas documentan autenticación `Bearer`. Abrir una disputa inicia mediación; desde ese momento cesa el contacto directo con el comprador y el rol receptor pasa a ser `mediator`.
- La consulta de resoluciones esperadas informa el estado de la resolución y el participante. Los tipos citados incluyen `product`, `refund`, `change_product` y `return_product`, relacionados con flujos PNR/PDD.
- La oferta de reembolso parcial muestra moneda, importe y porcentaje recomendado, con restricciones. La página enumera 400 por parámetro inválido o porcentaje por debajo del mínimo, 403 cuando el ClaimId no existe, 404 cuando el usuario no está autorizado y 422 cuando el reclamo no es apto para el flujo (por ejemplo, CBT o sin etiqueta de devolución).
- Para solicitar reembolso parcial, el reclamo debe corresponder a PDD, tener `return_product` pendiente y permitir `allow_partial_refund` en `available_actions`; se elige un porcentaje disponible, no 100%. La fuente indica 50% como valor por defecto si se omite y que al aceptarse se cierra el reclamo.
- Reembolso total requiere que esté disponible la acción `refund`. `allow-return` permite aceptar la devolución del producto y sustituye el flujo anterior de aceptación/carga de resolución. Los detalles de cuerpo y códigos para rutas no especificados: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /claims/partial-refund/available-offers-resolutions

La fuente menciona la ruta /claims/partial-refund/available-offers-resolutions, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/partial-refund/available-offers-resolutions`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /claims/expected-resolutions

La fuente menciona la ruta /claims/expected-resolutions, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/claims/expected-resolutions`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /v1/claims/{claim_id}/partial-refund/available-offers

La fuente menciona la ruta /v1/claims/{claim_id}/partial-refund/available-offers, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/v1/claims/{claim_id}/partial-refund/available-offers`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar resoluciones esperadas

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/expected-resolutions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista las resoluciones y el estado/participante asociado al reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- expected_resolution
- details
- player_role
- status
- labels

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La guía menciona product, refund, change_product y return_product, además de flujos PNR/PDD.

### Consultar ofertas de reembolso parcial

**Método:** `GET`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/partial-refund/available-offers`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene importes y porcentajes disponibles o recomendados para una devolución parcial.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- currency_id
- available_offers[].amount
- available_offers[].percentage
- recommendations
- restrictions

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Parámetro inválido o intento por debajo del mínimo." } ```
- ```json {   "code": 403,   "meaning": "ClaimId no existe (así lo describe la fuente)." } ```
- ```json {   "code": 404,   "meaning": "Usuario no autorizado (así lo describe la fuente)." } ```
- ```json {   "code": 422,   "meaning": "Reclamo no apto para el flujo, por ejemplo CBT o sin etiqueta de devolución." } ```

**Ejemplos**

No documentado en la fuente.

### Abrir disputa

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/actions/open-dispute`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Inicia la mediación para un reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Tras abrirla cesa el mensaje directo al comprador y el rol receptor es mediator.

### Aceptar devolución

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/expected-resolutions/allow-return`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Acepta la devolución del producto como resolución del reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La guía presenta esta operación como reemplazo del flujo anterior de aceptación/carga de resolución.

### Solicitar reembolso parcial

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/expected-resolutions/partial-refund`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Solicita un porcentaje disponible de reembolso parcial para el reclamo.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Requiere PDD, return_product pendiente y available_actions con allow_partial_refund; no admite 100%; 50% por defecto si se omite.

### Solicitar reembolso completo

**Método:** `POST`  
**Ruta:** `/post-purchase/v1/claims/$CLAIM_ID/expected-resolutions/refund`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Propone el reembolso completo cuando el reclamo permite la acción refund.

**Parámetros**

- `CLAIM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página requiere que refund figure entre las acciones disponibles.

### Referencia HTTP GET /v1/claims/{claim_id}/partial-refund/available-offers

**Método:** `GET`  
**Ruta:** `/v1/claims/{claim_id}/partial-refund/available-offers`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /v1/claims/{claim_id}/partial-refund/available-offers. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /claims/expected-resolutions

**Método:** `GET`  
**Ruta:** `/claims/expected-resolutions`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /claims/expected-resolutions. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP GET /claims/partial-refund/available-offers-resolutions

**Método:** `GET`  
**Ruta:** `/claims/partial-refund/available-offers-resolutions`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /claims/partial-refund/available-offers-resolutions. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestionar-resolucion-de-reclamos](https://developers.mercadolibre.com.co/es_co/gestionar-resolucion-de-reclamos)  
**Captura:** 2026-10-08T22:52:01.135Z

---

## [Gestión de mensajes](../markdown/mensajeria-post-venta.md)

Actualización indicada por la fuente: 27/04/2026. Captura: 2026-10-08T22:51:51.425Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/mensajeria-post-venta](https://developers.mercadolibre.com.co/es_co/mensajeria-post-venta)

# Gestión de mensajes

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 27/04/2026  
**Captura:** 2026-10-08T22:51:51.425Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/mensajeria-post-venta](https://developers.mercadolibre.com.co/es_co/mensajeria-post-venta)

## Resumen

La documentación describe la mensajería posventa para consultar conversaciones de un pack, obtener un mensaje individual, responder al comprador y adjuntar archivos. Indica que la transición a la nueva arquitectura no incorpora nuevos endpoints públicos ni exige una migración obligatoria; cuando pack_id no está disponible, se conserva la ruta de packs usando order_id como identificador. La fecha de captura y la fecha declarada por la fuente se conservan en esta ficha.

## Contenido y conceptos documentados

- El flujo se identifica con `tag=post_sale`; para listar mensajes se admiten `limit` y `offset`. Los mensajes del comprador moderados no se muestran; los mensajes del vendedor permanecen visibles aunque hayan sido moderados. La página también documenta identificadores de agentes por país y consideraciones de transición.
- Los anexos se cargan como `multipart/form-data` con el campo `file`; la respuesta proporciona el identificador que luego se consulta. La página incluye ejemplos para listar, enviar, consultar mensajes y cargar/obtener anexos.
- Autenticación mostrada: `Authorization: Bearer $ACCESS_TOKEN`. La fuente lista errores 400 por paginación o cuerpo inválido y texto no permitido o mayor a 350 caracteres; 403 por falta de acceso, mediación o envío Full no entregado; 404 por mensaje no encontrado; 422 por clave de anexo inválida y 500 por falla al guardar archivos.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /packs/2000000089077943/seller/415458330

La fuente menciona la ruta /packs/2000000089077943/seller/415458330, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/packs/2000000089077943/seller/415458330`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /packs

La fuente menciona la ruta /packs, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/packs`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /packs/{pack_id}/sellers/{seller_id}/conversations/{type}

La fuente menciona la ruta /packs/{pack_id}/sellers/{seller_id}/conversations/{type}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/packs/{pack_id}/sellers/{seller_id}/conversations/{type}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### GET /messages/attachments/{ATTACHMENT_ID}

**Método:** `GET`  
**Ruta:** `/messages/attachments/{ATTACHMENT_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera un anexo previamente cargado.

**Parámetros**

- `ATTACHMENT_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.
- `site_id` (query, obligatorio): Sitio asociado al anexo.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "summary": "La fuente indica que devuelve el archivo solicitado."
}
```

**Errores documentados**

- ```json {   "code": "422",   "meaning": "Clave de anexo inexistente, inaccesible o ajena al usuario." } ```

**Ejemplos**

- La página incluye ejemplos de llamada y respuesta para este recurso.

### GET /messages/{MESSAGE_ID}

**Método:** `GET`  
**Ruta:** `/messages/{MESSAGE_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el detalle de un mensaje por identificador.

**Parámetros**

- `MESSAGE_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "message_id",
    "date_created",
    "from",
    "to",
    "text",
    "attachments"
  ],
  "summary": "Detalle del mensaje según campos descritos."
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "El identificador de mensaje no existe." } ```
- ```json {   "code": "403",   "meaning": "El usuario no tiene acceso al mensaje." } ```
- ```json {   "code": "404",   "meaning": "El mensaje no puede recuperarse del almacenamiento." } ```

**Ejemplos**

- La página incluye ejemplos de llamada y respuesta para este recurso.

### GET /messages/packs/{PACK_ID}/sellers/{USER_ID}

**Método:** `GET`  
**Ruta:** `/messages/packs/{PACK_ID}/sellers/{USER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista mensajes de la conversación posventa de un pack; la fuente muestra paginación con `limit` y `offset`.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `USER_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa; los ejemplos usan post_sale.
- `limit` (query, opcional): Cantidad de mensajes solicitados.
- `offset` (query, opcional): Desplazamiento de paginación.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "messages",
    "paging"
  ],
  "summary": "Lista de mensajes del pack y paginación."
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "limit debe ser mayor que cero; limit u offset inválidos." } ```
- ```json {   "code": "403",   "meaning": "El token no tiene acceso al recurso/orden." } ```

**Ejemplos**

- La página incluye ejemplos de llamada y respuesta para este recurso.

### POST /messages/attachments

**Método:** `POST`  
**Ruta:** `/messages/attachments`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Carga un anexo para el sitio indicado; usa multipart y `file`.

**Parámetros**

- `tag` (query, obligatorio): Identifica el flujo posventa.
- `site_id` (query, obligatorio): Sitio para la carga del anexo.

**Solicitud**

```json
{
  "fields": [
    "file"
  ],
  "content_type": "multipart/form-data"
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Archivo vacío, nombre inválido, más de 25 MB o más de 25 anexos; parámetros/cuerpo inválidos." } ```
- ```json {   "code": "500",   "meaning": "El archivo no se pudo guardar temporalmente." } ```

**Ejemplos**

- La página incluye ejemplos de llamada y respuesta para este recurso.

### POST /messages/packs/{PACK_ID}/sellers/{USER_ID}

**Método:** `POST`  
**Ruta:** `/messages/packs/{PACK_ID}/sellers/{USER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Envía un mensaje al comprador dentro del pack.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `USER_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.

**Solicitud**

```json
{
  "fields": [
    "from",
    "to",
    "text",
    "attachments"
  ],
  "summary": "Cuerpo JSON de mensaje; errores documentan los campos from y to.site_id."
}
```

**Respuesta**

```json
{
  "fields": [
    "message_id",
    "status",
    "text",
    "message_moderation"
  ]
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Texto/cuerpo/receptor/remitente/recurso/site_id inválido; texto máximo 350 caracteres." } ```
- ```json {   "code": "403",   "meaning": "Sin acceso a la orden, mediación activa o envío Full aún no entregado." } ```
- ```json {   "code": "422",   "meaning": "Clave de anexo inexistente, inaccesible o ajena al usuario." } ```

**Ejemplos**

- La página incluye ejemplos de llamada y respuesta para este recurso.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/mensajeria-post-venta](https://developers.mercadolibre.com.co/es_co/mensajeria-post-venta)  
**Captura:** 2026-10-08T22:51:51.425Z

---

## [Gestión Mercado Envíos](../markdown/mercado-envios.md)

Actualización indicada por la fuente: 23/04/2026. Captura: 2026-10-08T22:51:52.527Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/mercado-envios](https://developers.mercadolibre.com.co/es_co/mercado-envios)

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

---

## [Identificadores de productos](../markdown/identificadores-de-productos.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:52:02.036Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/identificadores-de-productos](https://developers.mercadolibre.com.co/es_co/identificadores-de-productos)

# Identificadores de productos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:52:02.036Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/identificadores-de-productos](https://developers.mercadolibre.com.co/es_co/identificadores-de-productos)

## Resumen

Explica cómo manejar identificadores de producto, especialmente GTIN, al crear o actualizar publicaciones y variaciones, y cómo consultar los atributos devueltos. La lógica depende de si el identificador aplica al producto y de las razones documentadas para no enviarlo.

## Contenido y conceptos documentados

- La página distingue identificadores GTIN y describe su lógica de uso como atributo. En publicación se muestra `attributes` con `id: GTIN`; en publicaciones con variaciones el dato se informa en la variación correspondiente. También documenta razones por las que puede omitirse el GTIN y cómo consultar todos los atributos.
- Los ejemplos incluyen alta de ítems, actualización de atributos y variaciones y consulta con `include_attributes=all`. Si falta un GTIN marcado como `conditional_required`, se documenta el error 400 `item.attribute.missing_conditional_required` (cause_id 7810). Si no existe GTIN, puede enviarse `EMPTY_GTIN_REASON` en los casos permitidos; la fuente también muestra este atributo como condicionalmente requerido.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /items/y

La fuente menciona la ruta /items/y, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/items/y`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /categories/{CATEGORY_ID}/attributes

La fuente menciona la ruta /categories/{CATEGORY_ID}/attributes, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/categories/{CATEGORY_ID}/attributes`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### GET /items/{ITEM_ID}

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la publicación con `include_attributes=all` para revisar sus identificadores.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `include_attributes` (query, opcional): El ejemplo usa all para incluir todos los atributos.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "attributes",
    "GTIN",
    "variations"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /items

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una publicación con atributos de producto, incluido GTIN cuando corresponda.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "attributes",
    "GTIN"
  ],
  "summary": "Ejemplos de creación con GTIN en atributos."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "validation_error, cause_id 7810 y código item.attribute.missing_conditional_required cuando falta GTIN o EMPTY_GTIN_REASON requerido condicionalmente." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### PUT /items/{ITEM_ID}

**Método:** `PUT`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza atributos de una publicación para agregar o corregir GTIN.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "attributes",
    "GTIN",
    "variations"
  ],
  "summary": "Los ejemplos actualizan GTIN en atributos o variaciones."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "validation_error, cause_id 7810 y código item.attribute.missing_conditional_required cuando falta GTIN o EMPTY_GTIN_REASON requerido condicionalmente." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/identificadores-de-productos](https://developers.mercadolibre.com.co/es_co/identificadores-de-productos)  
**Captura:** 2026-10-08T22:52:02.036Z

---

## [Imágenes](../markdown/trabajar-con-imagenes.md)

Actualización indicada por la fuente: 24/03/2026. Captura: 2026-10-08T22:52:03.544Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/trabajar-con-imagenes](https://developers.mercadolibre.com.co/es_co/trabajar-con-imagenes)

# Imágenes

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 24/03/2026  
**Captura:** 2026-10-08T22:52:03.544Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/trabajar-con-imagenes](https://developers.mercadolibre.com.co/es_co/trabajar-con-imagenes)

## Resumen

Documenta recomendaciones para preparar imágenes de publicaciones, cargarlas, asociarlas a un ítem, reemplazarlas y consultar errores de procesamiento o moderación. La página enfatiza que el endpoint de carga directa admite archivos multipart para ítems.

## Contenido y conceptos documentados

- El flujo mostrado carga el archivo y luego usa el identificador de imagen para vincularlo a la publicación; también puede enviarse una fuente de imagen en `pictures`. Para reemplazar imágenes se actualiza el arreglo `pictures` de la publicación.
- Se mencionan tamaño, formatos de imagen (incluidos JPG/JPEG/PNG), problemas de conexión o bloqueo y moderación. La carga directa solo soporta multipart de datos y está destinada a ítems. La respuesta de errores puede incluir `id`, `source` y `error.message`; la fuente muestra errores de descarga 401/403/404, HTTP 301 por redirección, 400 por límite de solicitudes y validaciones 508 (imagen no activa) y 509 (tamaño inferior al mínimo). Recomienda validar acceso, Content-Type y URL final.

## Operaciones de API
## Operaciones de API

### GET /pictures/{PICTURE_ID}/errors

**Método:** `GET`  
**Ruta:** `/pictures/{PICTURE_ID}/errors`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta errores asociados al procesamiento de una imagen.

**Parámetros**

- `PICTURE_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "source",
    "error",
    "items"
  ]
}
```

**Errores documentados**

- ```json {   "code": "403/404",   "meaning": "El servidor externo bloquea la descarga o no encuentra la imagen." } ```
- ```json {   "code": "301",   "meaning": "La imagen redirige; la fuente recomienda enviar su URL final." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /items/{ITEM_ID}/pictures

**Método:** `POST`  
**Ruta:** `/items/{ITEM_ID}/pictures`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Asocia una imagen cargada al ítem mediante su identificador.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "id"
  ],
  "summary": "El ejemplo vincula el identificador de una imagen."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "validation_error cause_id 508: imagen no está en estado ACTIVE o PENDING." } ```
- ```json {   "code": "400",   "meaning": "validation_error cause_id 509: imagen por debajo del tamaño mínimo." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /pictures/items/upload

**Método:** `POST`  
**Ruta:** `/pictures/items/upload`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Sube una imagen mediante multipart (`file`) para obtener su identificador.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "file"
  ],
  "content_type": "multipart/form-data"
}
```

**Respuesta**

```json
{
  "fields": [
    "id"
  ]
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Bad request por cuota de solicitudes o archivo inválido." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### PUT /items/{ITEM_ID}

**Método:** `PUT`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza las imágenes de la publicación usando el campo `pictures`.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "pictures",
    "source",
    "id"
  ],
  "summary": "El ejemplo modifica el arreglo pictures."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "validation_error cause_id 508: imagen no está en estado ACTIVE o PENDING." } ```
- ```json {   "code": "400",   "meaning": "validation_error cause_id 509: imagen por debajo del tamaño mínimo." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/trabajar-con-imagenes](https://developers.mercadolibre.com.co/es_co/trabajar-con-imagenes)  
**Captura:** 2026-10-08T22:52:03.544Z

---

## [Introducción](../markdown/guia-para-producto.md)

Actualización indicada por la fuente: 29/12/2025. Captura: 2026-10-08T22:52:04.602Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/guia-para-producto](https://developers.mercadolibre.com.co/es_co/guia-para-producto)

# Introducción

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:52:04.602Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/guia-para-producto](https://developers.mercadolibre.com.co/es_co/guia-para-producto)

## Resumen

La página de introducción presenta la guía para integradores de productos de Mercado Libre y funciona como punto de entrada a sus temas de publicaciones, catálogo, envíos, ventas y otras capacidades. El contenido capturado es introductorio y remite a las secciones especializadas.

## Contenido y conceptos documentados

- La fuente organiza la documentación por temas y enlaza guías específicas para trabajar con productos. No desarrolla parámetros, autenticación, solicitudes, respuestas ni errores de API en esta página: No documentado en la fuente.
- Para detalles de operaciones se deben consultar las fichas temáticas enlazadas desde el portal oficial.

## Operaciones de API

## Conceptos y recursos asociados

### Introducción

La página de introducción presenta la guía para integradores de productos de Mercado Libre y funciona como punto de entrada a sus temas de publicaciones, catálogo, envíos, ventas y otras capacidades. El contenido capturado es introductorio y remite a las secciones especializadas.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/guia-para-producto](https://developers.mercadolibre.com.co/es_co/guia-para-producto)  
**Captura:** 2026-10-08T22:52:04.602Z

---

## [Kits virtuales](../markdown/kits-virtuales.md)

Actualización indicada por la fuente: 17/09/2026. Captura: 2026-10-08T22:52:05.798Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/kits-virtuales](https://developers.mercadolibre.com.co/es_co/kits-virtuales)

# Kits virtuales

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 17/09/2026  
**Captura:** 2026-10-08T22:52:05.798Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/kits-virtuales](https://developers.mercadolibre.com.co/es_co/kits-virtuales)

## Resumen

Describe la búsqueda de productos componentes, creación y modificación de kits virtuales, configuración de precios, consulta del precio de venta, stock y órdenes relacionadas. El kit se representa como un bundle y sus componentes conservan sus propios productos/órdenes.

## Contenido y conceptos documentados

- El flujo comienza buscando componentes y luego crea el kit con la estructura `bundle`; la fuente diferencia la creación con y sin sincronización de precios. Para cambios permitidos se actualiza el ítem del kit (por ejemplo, `price`).
- Para precios se consulta `/sale_price` y su bloque `bundle`; la automatización se gestiona con `bundle/prices_configuration`. Para una orden de un componente, `/bundle` permite recuperar las órdenes relacionadas. También se documenta stock calculado del kit.
- La estructura de búsqueda contempla `active_channels`, `main_product_id`, `added_products` y `search_filters`; `bundle.type=kit` identifica el kit y `bundle.components` contiene productos y cantidades, con el primer componente como principal. El precio de venta puede exponer `amount`, `regular_amount` y distribución por componente (`component_price`, `unit_amount`, `total_amount`). Tras publicar, componentes y cantidades no se pueden cambiar; solo son modificables campos permitidos como título/precio sujeto a configuración. La fuente muestra 400 `Updating the bundle node is not allowed`, 404 de componente inexistente y 429 por cuota excedida. También menciona `searchText`, `limit` y `context=channel_marketplace`.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /flex

La fuente menciona la ruta /flex, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/flex`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### GET /items/{ITEM_ID}/bundle/prices_configuration

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/bundle/prices_configuration`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta esa configuración.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /items/{ITEM_ID}/sale_price

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}/sale_price`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el precio de venta y desglose del kit; el ejemplo usa `context=channel_marketplace`.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `context` (query, obligatorio): El ejemplo usa channel_marketplace.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "amount",
    "regular_amount",
    "bundle",
    "metadata"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /orders/{ORDER_ID}

**Método:** `GET`  
**Ruta:** `/orders/{ORDER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el detalle de una orden.

**Parámetros**

- `ORDER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /orders/{ORDER_ID}/bundle

**Método:** `GET`  
**Ruta:** `/orders/{ORDER_ID}/bundle`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera las órdenes de los componentes relacionadas con la venta del kit.

**Parámetros**

- `ORDER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "summary": "Órdenes relacionadas con los componentes del kit."
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /user-products/{USER_PRODUCT_ID}

**Método:** `GET`  
**Ruta:** `/user-products/{USER_PRODUCT_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta información de un User Product.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "bundle.type",
    "bundle.components"
  ],
  "summary": "Permite identificar el kit y sus User Products componentes."
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /user-products/{USER_PRODUCT_ID}/bundles

**Método:** `GET`  
**Ruta:** `/user-products/{USER_PRODUCT_ID}/bundles`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta los kits asociados a un User Product.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "summary": "Kits en los que está asociado el User Product consultado."
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /user-products/{USER_PRODUCT_ID}/stock

**Método:** `GET`  
**Ruta:** `/user-products/{USER_PRODUCT_ID}/stock`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el stock calculado del kit.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "summary": "Stock calculado del kit a partir del stock de sus componentes."
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /items/kits

**Método:** `POST`  
**Ruta:** `/items/kits`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea un kit virtual con sus componentes y configuración de precios.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "bundle",
    "components"
  ],
  "summary": "La solicitud crea un kit virtual con componentes."
}
```

**Respuesta**

```json
{
  "fields": [
    "id",
    "bundle",
    "components",
    "price"
  ]
}
```

**Errores documentados**

- ```json {   "code": "404",   "meaning": "UserProductComponent not found." } ```
- ```json {   "code": "429",   "meaning": "client.id over quota." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /users/{SELLER_ID}/kits/components/search

**Método:** `POST`  
**Ruta:** `/users/{SELLER_ID}/kits/components/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca productos candidatos a componente; usa `searchText` y `limit`.

**Parámetros**

- `SELLER_ID` (path, obligatorio)
- `searchText` (query, obligatorio): Texto de búsqueda de componentes.
- `limit` (query, opcional): Límite de resultados.

**Solicitud**

```json
{
  "fields": [
    "active_channels",
    "main_product_id",
    "added_products",
    "search_filters",
    "filters"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "404",   "meaning": "UserProductComponent not found." } ```
- ```json {   "code": "429",   "meaning": "client.id over quota." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### PUT /items/{ITEM_ID}

**Método:** `PUT`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica campos permitidos del ítem kit.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "price"
  ],
  "summary": "Ejemplo de modificación del precio del kit."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Updating the bundle node is not allowed." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### PUT /items/{ITEM_ID}/bundle/prices_configuration

**Método:** `PUT`  
**Ruta:** `/items/{ITEM_ID}/bundle/prices_configuration`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica la configuración de automatización de precios.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/kits-virtuales](https://developers.mercadolibre.com.co/es_co/kits-virtuales)  
**Captura:** 2026-10-08T22:52:05.798Z

---

## [Mensajes bloqueados](../markdown/mensajes-bloqueados.md)

Actualización indicada por la fuente: 10/07/2026. Captura: 2026-10-08T22:52:06.557Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/mensajes-bloqueados](https://developers.mercadolibre.com.co/es_co/mensajes-bloqueados)

# Mensajes bloqueados

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 10/07/2026  
**Captura:** 2026-10-08T22:52:06.557Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/mensajes-bloqueados](https://developers.mercadolibre.com.co/es_co/mensajes-bloqueados)

## Resumen

Explica cómo consultar una conversación de posventa y leer el estado que indica por qué la mensajería está bloqueada. La respuesta permite distinguir estados y subestados, con motivos que incluyen mediaciones, cancelaciones, reembolsos, restricciones, revisiones, devoluciones y situaciones de asistentes de IA.

## Contenido y conceptos documentados

- La consulta se hace por pack y vendedor, usando `tag=post_sale`. La respuesta incluye `status`, `substatus` y `status_date`; la documentación enumera razones concretas de bloqueo, que determinan si la conversación no está disponible o bajo qué condición.
- La página presenta ejemplos con status/substatus, pero no documenta una operación para desbloquear ni enviar mensajes desde este recurso. Autenticación mostrada: OAuth Bearer. Otros parámetros y errores: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /packs/22175467/sellers/32086568493

La fuente menciona la ruta /packs/22175467/sellers/32086568493, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/packs/22175467/sellers/32086568493`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### GET /messages/packs/{PACK_ID}/sellers/{SELLER_ID}

**Método:** `GET`  
**Ruta:** `/messages/packs/{PACK_ID}/sellers/{SELLER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta los mensajes y el estado de bloqueo de la conversación posventa.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `SELLER_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "paging",
    "conversation_status",
    "status",
    "substatus",
    "status_date",
    "status_update_allowed",
    "claim_ids",
    "shipping_id",
    "messages"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/mensajes-bloqueados](https://developers.mercadolibre.com.co/es_co/mensajes-bloqueados)  
**Captura:** 2026-10-08T22:52:06.557Z

---

## [Mensajes pendientes](../markdown/mensajes-pendientes.md)

Actualización indicada por la fuente: 11/09/2025. Captura: 2026-10-08T22:52:07.457Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/mensajes-pendientes](https://developers.mercadolibre.com.co/es_co/mensajes-pendientes)

# Mensajes pendientes

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 11/09/2025  
**Captura:** 2026-10-08T22:52:07.457Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/mensajes-pendientes](https://developers.mercadolibre.com.co/es_co/mensajes-pendientes)

## Resumen

Documenta la consulta de mensajes posventa pendientes de lectura, tanto a partir de un recurso recibido por notificación como para un rol. Incluye el flujo para obtener la conversación y marcar como leídos los mensajes.

## Contenido y conceptos documentados

- La consulta específica por recurso usa `/messages/unread/{RESOURCE}`; la consulta general usa `/messages/unread` y exige `role` (`seller` o `buyer`); la consulta por recurso devuelve `user_id` y `results` con `resource` y `count`. El ejemplo incluye `tag=post_sale`. Para ver la conversación se consulta el recurso de mensajes del pack.
- La página explica el flujo desde notificaciones y el marcado de lectura, pero no muestra una ruta HTTP separada para dicha acción. Autenticación mostrada: OAuth Bearer. Errores documentados: 400 por IDs vacíos/inválidos, mensajes de órdenes distintas o mensaje inexistente; 404 cuando el mensaje no puede recuperarse del almacenamiento.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /packs/1234/sellers/2345

La fuente menciona la ruta /packs/1234/sellers/2345, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/packs/1234/sellers/2345`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /packs/1977056109/sellers/378136913

La fuente menciona la ruta /packs/1977056109/sellers/378136913, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/packs/1977056109/sellers/378136913`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /packs/2000000089077943/seller/415458330

La fuente menciona la ruta /packs/2000000089077943/seller/415458330, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/packs/2000000089077943/seller/415458330`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### GET /messages/packs/{PACK_ID}/sellers/{SELLER_ID}

**Método:** `GET`  
**Ruta:** `/messages/packs/{PACK_ID}/sellers/{SELLER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los mensajes de la conversación para procesar el recurso pendiente.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `SELLER_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "paging",
    "conversation_status",
    "messages"
  ]
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "IDs vacíos/inválidos, ID inexistente o IDs de mensajes de órdenes distintas." } ```
- ```json {   "code": "404",   "meaning": "El mensaje no puede recuperarse del almacenamiento." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /messages/unread

**Método:** `GET`  
**Ruta:** `/messages/unread`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta mensajes no leídos por rol; `role` es obligatorio y admite `seller` o `buyer`.

**Parámetros**

- `role` (query, obligatorio): Rol consultado: seller o buyer.
- `tag` (query, opcional): Identifica el flujo posventa.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "user_id",
    "results",
    "resource",
    "count"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /messages/unread/{RESOURCE}

**Método:** `GET`  
**Ruta:** `/messages/unread/{RESOURCE}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta mensajes pendientes de lectura para el recurso de una notificación.

**Parámetros**

- `RESOURCE` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "user_id",
    "results",
    "resource",
    "count"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### Referencia HTTP GET /messages/unread/packs/1234/sellers/2345

**Método:** `GET`  
**Ruta:** `/messages/unread/packs/1234/sellers/2345`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /messages/unread/packs/1234/sellers/2345. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

**Parámetros**

- `tag` (query): Aparece en una URL de la fuente; su obligatoriedad no está documentada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La referencia de método y ruta se encontró en el texto capturado de la página.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/mensajes-pendientes](https://developers.mercadolibre.com.co/es_co/mensajes-pendientes)  
**Captura:** 2026-10-08T22:52:07.457Z

---

## [Mercado Envíos 1](../markdown/mercadoenvios-modo-1.md)

Actualización indicada por la fuente: 06/02/2026. Captura: 2026-10-08T22:52:08.527Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-1](https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-1)

# Mercado Envíos 1

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 06/02/2026  
**Captura:** 2026-10-08T22:52:08.527Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-1](https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-1)

## Resumen

Explica cómo habilitar Mercado Envíos 1 para vendedores, publicar un ítem con esa modalidad, activarla en una publicación existente y consultar sus envíos. También presenta alertas relacionadas con fraude.

## Contenido y conceptos documentados

- Para publicar, los ejemplos configuran `shipping.mode` como `me1`; la activación sobre ítems existentes se realiza actualizando el ítem. La consulta de envíos se hace por `SHIPMENT_ID`.
- La documentación separa activación a nivel vendedor y a nivel ítem. Los ejemplos de publicación usan `shipping.mode=me1`, `local_pick_up` y `dimensions`. Una orden con tag `fraud_risk_detected` no debe enviarse al comprador. Autenticación mostrada: OAuth Bearer.

## Operaciones de API
## Operaciones de API

### GET /shipments/{SHIPMENT_ID}

**Método:** `GET`  
**Ruta:** `/shipments/{SHIPMENT_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el envío asociado a ME1.

**Parámetros**

- `SHIPMENT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "status",
    "substatus",
    "mode",
    "logistic_type"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /items

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Publica un ítem configurado con ME1.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "shipping.mode"
  ],
  "summary": "El ejemplo configura shipping.mode como me1."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /items/{ITEM_ID}

**Método:** `POST`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Publica/configura ME1 según el flujo ejemplificado para un ítem.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### PUT /items/{ITEM_ID}

**Método:** `PUT`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Activa ME1 en un ítem existente.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "shipping.mode"
  ],
  "summary": "El ejemplo actualiza la modalidad a me1."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-1](https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-1)  
**Captura:** 2026-10-08T22:52:08.527Z

---

## [Mercado Envíos 2](../markdown/mercadoenvios-modo-2.md)

Actualización indicada por la fuente: 06/07/2026. Captura: 2026-10-08T22:52:09.574Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-2](https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-2)

# Mercado Envíos 2

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 06/07/2026  
**Captura:** 2026-10-08T22:52:09.574Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-2](https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-2)

## Resumen

Reúne el flujo de Mercado Envíos 2: agregar la modalidad a publicaciones, validar preferencias y atributos del dominio, consultar envíos y obtener etiquetas; también explica cómo consultar órdenes y calcular el total con envío.

## Contenido y conceptos documentados

- Para publicar se informa `shipping.mode` y se consultan preferencias del usuario/categoría; para atributos dependientes de dominio se usa `shipping_attributes`. La información adicional del envío se obtiene de `/shipments`, pues la orden conserva la identificación del envío.
- Las etiquetas admiten `response_type=pdf` o `zpl2` y `shipment_ids`. Para consultas con nueva estructura se muestra `X-Format-New: true`. La fuente lista errores 400 por validaciones/campos obligatorios o formato de ID, 401 por token inválido, 403 por falta de permisos y 404 cuando ítem/producto/dominio no existe. Para etiquetas se documentan medidas de impresión por país y estados que permiten reimpresión.
- Autenticación mostrada: OAuth Bearer. Otros campos no detallados: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### GET /catalog_domains/{DOMAIN_ID}/shipping_attributes

**Método:** `GET`  
**Ruta:** `/catalog_domains/{DOMAIN_ID}/shipping_attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta atributos requeridos por dominio.

**Parámetros**

- `DOMAIN_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Validación de consistencia, campos obligatorios o formato de IDs." } ```
- ```json {   "code": "401",   "meaning": "Token inválido." } ```
- ```json {   "code": "403",   "meaning": "Falta de permisos." } ```
- ```json {   "code": "404",   "meaning": "Ítem, producto o dominio no encontrado." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /categories/{CATEGORY_ID}/shipping_preferences

**Método:** `GET`  
**Ruta:** `/categories/{CATEGORY_ID}/shipping_preferences`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta requisitos/preferencias de envío de la categoría.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Validación de consistencia, campos obligatorios o formato de IDs." } ```
- ```json {   "code": "401",   "meaning": "Token inválido." } ```
- ```json {   "code": "403",   "meaning": "Falta de permisos." } ```
- ```json {   "code": "404",   "meaning": "Ítem, producto o dominio no encontrado." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /orders/{ORDER_ID}

**Método:** `GET`  
**Ruta:** `/orders/{ORDER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la orden y su identificador de envío.

**Parámetros**

- `ORDER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "shipping.id",
    "pack_id"
  ],
  "summary": "La orden contiene la identificación del envío; sus detalles adicionales se consultan en shipments."
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /shipment_labels

**Método:** `GET`  
**Ruta:** `/shipment_labels`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Genera/obtiene etiquetas para `shipment_ids`; admite `response_type=pdf` o `zpl2`.

**Parámetros**

- `shipment_ids` (query, obligatorio): Uno o varios identificadores de envío separados por coma.
- `response_type` (query, obligatorio): Formato documentado: pdf o zpl2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Validación de consistencia, campos obligatorios o formato de IDs." } ```
- ```json {   "code": "401",   "meaning": "Token inválido." } ```
- ```json {   "code": "403",   "meaning": "Falta de permisos." } ```
- ```json {   "code": "404",   "meaning": "Ítem, producto o dominio no encontrado." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /shipments/{SHIPMENT_ID}

**Método:** `GET`  
**Ruta:** `/shipments/{SHIPMENT_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalles del envío; el ejemplo nuevo usa `X-Format-New: true`.

**Parámetros**

- `SHIPMENT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "status",
    "substatus",
    "mode",
    "logistic_type"
  ]
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Validación de consistencia, campos obligatorios o formato de IDs." } ```
- ```json {   "code": "401",   "meaning": "Token inválido." } ```
- ```json {   "code": "403",   "meaning": "Falta de permisos." } ```
- ```json {   "code": "404",   "meaning": "Ítem, producto o dominio no encontrado." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /users/{USER_ID}/shipping_preferences

**Método:** `GET`  
**Ruta:** `/users/{USER_ID}/shipping_preferences`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta preferencias de envío del vendedor.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Validación de consistencia, campos obligatorios o formato de IDs." } ```
- ```json {   "code": "401",   "meaning": "Token inválido." } ```
- ```json {   "code": "403",   "meaning": "Falta de permisos." } ```
- ```json {   "code": "404",   "meaning": "Ítem, producto o dominio no encontrado." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /items

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Publica un ítem con configuración de ME2.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "shipping.mode"
  ],
  "summary": "El ejemplo publica con configuración ME2."
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Validación de consistencia, campos obligatorios o formato de IDs." } ```
- ```json {   "code": "401",   "meaning": "Token inválido." } ```
- ```json {   "code": "403",   "meaning": "Falta de permisos." } ```
- ```json {   "code": "404",   "meaning": "Ítem, producto o dominio no encontrado." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-2](https://developers.mercadolibre.com.co/es_co/mercadoenvios-modo-2)  
**Captura:** 2026-10-08T22:52:09.574Z

---

## [Motivos para comunicarse](../markdown/motivos-para-comunicarse.md)

Actualización indicada por la fuente: 29/09/2026. Captura: 2026-10-08T22:52:10.373Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/motivos-para-comunicarse](https://developers.mercadolibre.com.co/es_co/motivos-para-comunicarse)

# Motivos para comunicarse

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/09/2026  
**Captura:** 2026-10-08T22:52:10.373Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/motivos-para-comunicarse](https://developers.mercadolibre.com.co/es_co/motivos-para-comunicarse)

## Resumen

Documenta el catálogo de motivos y opciones de comunicación posventa, la cantidad de mensajes disponibles y el envío de mensajes con plantillas o texto libre. También incluye la promesa de entrega y plantillas que dependen del país.

## Contenido y conceptos documentados

- El flujo consulta opciones para un pack, revisa las capacidades disponibles y envía la opción seleccionada. Los cuerpos usan `option_id`; según el caso también `template_id`, `text` o datos de promesa de entrega. Después de la respuesta del comprador, los mensajes siguientes se envían por el recurso de mensajería habitual. Las opciones exponen `option_id`, `template_id`, `char_limit`, `child_options` y `cap_available`; algunas plantillas requieren variables `vars`.
- La disponibilidad puede ser cero, caso en el que no se permiten mensajes. Se muestran templates localizados por sitio y ejemplos de errores. Autenticación mostrada: OAuth Bearer; el ejemplo usa `tag=post_sale`.

## Operaciones de API
## Operaciones de API

### GET /messages/action_guide/packs/{PACK_ID}

**Método:** `GET`  
**Ruta:** `/messages/action_guide/packs/{PACK_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta los motivos/opciones de comunicación disponibles para el pack.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "options",
    "option_id",
    "template_id",
    "char_limit",
    "child_options",
    "cap_available"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /messages/action_guide/packs/{PACK_ID}/caps_available

**Método:** `GET`  
**Ruta:** `/messages/action_guide/packs/{PACK_ID}/caps_available`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la capacidad disponible para enviar mensajes.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "cap_available"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /messages/action_guide/packs/{PACK_ID}/option

**Método:** `POST`  
**Ruta:** `/messages/action_guide/packs/{PACK_ID}/option`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Envía una opción; el cuerpo puede incluir `option_id`, `template_id` y, para opción libre, `text`.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `tag` (query, obligatorio): Identifica el flujo posventa.

**Solicitud**

```json
{
  "fields": [
    "option_id",
    "template_id",
    "text",
    "vars"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "id",
    "status",
    "text",
    "message_date",
    "message_moderation"
  ]
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "Texto supera el límite; errores de solicitud por caso exceptuado." } ```
- ```json {   "code": "403",   "meaning": "Cap no disponible o conversación bloqueada." } ```
- ```json {   "code": "404",   "meaning": "option_id no válido." } ```
- ```json {   "code": "409",   "meaning": "Otra solicitud está bloqueando la operación." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/motivos-para-comunicarse](https://developers.mercadolibre.com.co/es_co/motivos-para-comunicarse)  
**Captura:** 2026-10-08T22:52:10.373Z

---

## [Notas de Packs](../markdown/notas-de-packs.md)

Actualización indicada por la fuente: 12/09/2025. Captura: 2026-10-08T22:52:11.192Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/notas-de-packs](https://developers.mercadolibre.com.co/es_co/notas-de-packs)

# Notas de Packs

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 12/09/2025  
**Captura:** 2026-10-08T22:52:11.192Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/notas-de-packs](https://developers.mercadolibre.com.co/es_co/notas-de-packs)

## Resumen

Documenta la creación, actualización, consulta individual y búsqueda de notas informativas asociadas a un pack. Las notas registran texto y metadatos de origen/autoría para que los actores de venta y posventa compartan información contextual.

## Contenido y conceptos documentados

- `note` es el campo de texto; al crear una nota la fuente indica longitud máxima de 300 caracteres. Las respuestas incluyen `id`, `date_created`, `date_last_updated`, `note`, `seller_id` y, cuando aplica, `source_bu` y `operator_id`; la búsqueda devuelve `pack_id` y `results`.
- Los ejemplos incluyen `X-Public: true`, `Content-Type: application/json` y OAuth Bearer. Las tablas identifican `packID`, `noteID` y `accessToken` como parámetros. Errores: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### GET /packs/{PACK_ID}/notes

**Método:** `GET`  
**Ruta:** `/packs/{PACK_ID}/notes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca/lista las notas del pack.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `access_token` (query, obligatorio): Token de acceso documentado también como parámetro.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "pack_id",
    "results"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /packs/{PACK_ID}/notes/{NOTE_ID}

**Método:** `GET`  
**Ruta:** `/packs/{PACK_ID}/notes/{NOTE_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta una nota por pack e identificador.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `NOTE_ID` (path, obligatorio)
- `access_token` (query, obligatorio): Token de acceso documentado también como parámetro.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "date_created",
    "date_last_updated",
    "note",
    "source_bu",
    "seller_id",
    "operator_id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /packs/{PACK_ID}/notes

**Método:** `POST`  
**Ruta:** `/packs/{PACK_ID}/notes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una nota informativa; cuerpo `note` obligatorio, máximo 300 caracteres.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `access_token` (query, obligatorio): Token de acceso documentado también como parámetro.

**Solicitud**

```json
{
  "fields": [
    "note"
  ],
  "constraints": {
    "note": "Obligatorio; máximo 300 caracteres."
  }
}
```

**Respuesta**

```json
{
  "fields": [
    "id",
    "date_created",
    "date_last_updated",
    "note",
    "source_bu",
    "seller_id",
    "operator_id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### PUT /packs/{PACK_ID}/notes/{NOTE_ID}

**Método:** `PUT`  
**Ruta:** `/packs/{PACK_ID}/notes/{NOTE_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza el texto de una nota existente.

**Parámetros**

- `PACK_ID` (path, obligatorio)
- `NOTE_ID` (path, obligatorio)
- `access_token` (query, obligatorio): Token de acceso documentado también como parámetro.

**Solicitud**

```json
{
  "fields": [
    "note"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "id",
    "date_created",
    "date_last_updated",
    "note",
    "source_bu",
    "seller_id",
    "operator_id"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/notas-de-packs](https://developers.mercadolibre.com.co/es_co/notas-de-packs)  
**Captura:** 2026-10-08T22:52:11.192Z

---

## [Notas en órdenes](../markdown/notas-en-ordenes.md)

Actualización indicada por la fuente: 29/12/2025. Captura: 2026-10-08T22:52:12.230Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/notas-en-ordenes](https://developers.mercadolibre.com.co/es_co/notas-en-ordenes)

# Notas en órdenes

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:52:12.230Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/notas-en-ordenes](https://developers.mercadolibre.com.co/es_co/notas-en-ordenes)

## Resumen

Documenta las operaciones para agregar, consultar, modificar y eliminar notas internas de órdenes. También describe el bloqueo de ofertas para un usuario específico mediante una lista negra del comprador.

## Contenido y conceptos documentados

- Las notas usan el campo `note` en el cuerpo y se identifican con `ORDER_ID` y `NOTE_ID`. El bloqueo se dirige al endpoint de usuario con `user_id` en el cuerpo.
- Los ejemplos usan OAuth Bearer y JSON. Los campos de respuesta, límites de texto y errores: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### DELETE /orders/{ORDER_ID}/notes/{NOTE_ID}

**Método:** `DELETE`  
**Ruta:** `/orders/{ORDER_ID}/notes/{NOTE_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina una nota.

**Parámetros**

- `ORDER_ID` (path, obligatorio)
- `NOTE_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /orders/{ORDER_ID}/notes

**Método:** `GET`  
**Ruta:** `/orders/{ORDER_ID}/notes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta las notas de una orden.

**Parámetros**

- `ORDER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /orders/{ORDER_ID}/notes

**Método:** `POST`  
**Ruta:** `/orders/{ORDER_ID}/notes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega una nota a la orden.

**Parámetros**

- `ORDER_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "note"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /users/{CUST_ID}/order_blacklist

**Método:** `POST`  
**Ruta:** `/users/{CUST_ID}/order_blacklist`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Bloquea ofertas del usuario indicado; el cuerpo contiene `user_id`.

**Parámetros**

- `CUST_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "user_id"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### PUT /orders/{ORDER_ID}/notes/{NOTE_ID}

**Método:** `PUT`  
**Ruta:** `/orders/{ORDER_ID}/notes/{NOTE_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica una nota existente.

**Parámetros**

- `ORDER_ID` (path, obligatorio)
- `NOTE_ID` (path, obligatorio)

**Solicitud**

```json
{
  "fields": [
    "note"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/notas-en-ordenes](https://developers.mercadolibre.com.co/es_co/notas-en-ordenes)  
**Captura:** 2026-10-08T22:52:12.230Z

---

## [Ofertas del día](../markdown/ofertas-del-dia.md)

Actualización indicada por la fuente: 22/01/2025. Captura: 2026-10-08T22:52:13.326Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/ofertas-del-dia](https://developers.mercadolibre.com.co/es_co/ofertas-del-dia)

# Ofertas del día

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 22/01/2025  
**Captura:** 2026-10-08T22:52:13.326Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/ofertas-del-dia](https://developers.mercadolibre.com.co/es_co/ofertas-del-dia)

## Resumen

Describe cómo consultar los ítems de una campaña de Oferta del día, indicar una publicación para participar y retirar el ítem. La campaña se identifica como tipo `DOD` dentro de la API de promociones.

## Contenido y conceptos documentados

- Para consultar ítems se envían `promotion_type=DOD` y `app_version=v2`. La indicación usa `deal_price` y `promotion_type`; la eliminación envía el tipo de promoción en la consulta.
- La respuesta documenta estados del ítem y campos de campaña. Autenticación mostrada: OAuth Bearer. La respuesta puede incluir `id`, fechas, `status`, `price`, `original_price`, `max_discounted_price`, `min_discounted_price` y `stock`. Una oferta ya activada no se elimina durante su ciclo; si se quiere dejar de ofrecerla, se pausa el ítem. Errores: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### DELETE /seller-promotions/items/{ITEM_ID}

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina el ítem de la promoción; usa `app_version=v2` y `promotion_type`.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La fuente usa v2.
- `promotion_type` (query, obligatorio): Tipo de promoción; en esta página DOD.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /seller-promotions/promotions/{PROMOTION_ID}/items

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{PROMOTION_ID}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta ítems de la campaña con `promotion_type=DOD` y `app_version=v2`.

**Parámetros**

- `PROMOTION_ID` (path, obligatorio)
- `promotion_type` (query, obligatorio): Tipo de campaña DOD.
- `app_version` (query, obligatorio): La fuente usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "start_date",
    "finish_date",
    "status",
    "price",
    "original_price",
    "max_discounted_price",
    "min_discounted_price",
    "stock",
    "paging"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /seller-promotions/items/{ITEM_ID}

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Indica un ítem para una promoción con `deal_price` y `promotion_type`.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La fuente usa v2.

**Solicitud**

```json
{
  "fields": [
    "deal_price",
    "promotion_type"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "price",
    "original_price"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/ofertas-del-dia](https://developers.mercadolibre.com.co/es_co/ofertas-del-dia)  
**Captura:** 2026-10-08T22:52:13.326Z

---

## [Ofertas relámpago](../markdown/ofertas-relampago.md)

Actualización indicada por la fuente: 09/06/2026. Captura: 2026-10-08T22:52:14.750Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/ofertas-relampago](https://developers.mercadolibre.com.co/es_co/ofertas-relampago)

# Ofertas relámpago

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 09/06/2026  
**Captura:** 2026-10-08T22:52:14.750Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/ofertas-relampago](https://developers.mercadolibre.com.co/es_co/ofertas-relampago)

## Resumen

Documenta la consulta, incorporación y retiro de ítems en campañas Lightning. También explica el descuento adicional opcional (boost) que Mercado Libre puede aplicar sobre la oferta base.

## Contenido y conceptos documentados

- La consulta de ítems usa `promotion_type=LIGHTNING` y `app_version=v2`; la incorporación muestra `deal_price` y `stock`. La consulta por ítem puede incluir `boosted_offer`, `discount_meli_boosted_percentage`, `discount_meli_boost_amount` y `total_price_for_boosted_offer`, únicamente cuando `boosted_offer` es verdadero.
- Se describen estados de los ítems y respuestas de campaña. La respuesta de campaña incluye `id`, fechas, `status`, `price`, `original_price`, límites de precio y rango de `stock`. Las ofertas activadas no se eliminan durante el ciclo; la fuente indica pausarlas si se desea dejar de ofrecerlas. Autenticación mostrada: OAuth Bearer.

## Operaciones de API
## Operaciones de API

### DELETE /seller-promotions/items/{ITEM_ID}

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Retira el ítem de la campaña con `promotion_type=LIGHTNING`.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La fuente usa v2.
- `promotion_type` (query, obligatorio): Tipo de promoción LIGHTNING.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /seller-promotions/items/{ITEM_ID}

**Método:** `GET`  
**Ruta:** `/seller-promotions/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la oferta del ítem, incluidos campos de boost cuando aplica.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "boosted_offer",
    "discount_meli_boosted_percentage",
    "discount_meli_boost_amount",
    "total_price_for_boosted_offer"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /seller-promotions/promotions/{PROMOTION_ID}/items

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{PROMOTION_ID}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta ítems de la campaña Lightning.

**Parámetros**

- `PROMOTION_ID` (path, obligatorio)
- `promotion_type` (query, obligatorio): Tipo de campaña LIGHTNING.
- `app_version` (query, obligatorio): La fuente usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "start_date",
    "finish_date",
    "status",
    "price",
    "original_price",
    "max_discounted_price",
    "min_discounted_price",
    "stock",
    "paging"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /seller-promotions/items/{ITEM_ID}

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Incorpora el ítem con `deal_price` y `stock`.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `app_version` (query, obligatorio): La fuente usa v2.

**Solicitud**

```json
{
  "fields": [
    "deal_price",
    "stock",
    "promotion_type"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "price",
    "original_price"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/ofertas-relampago](https://developers.mercadolibre.com.co/es_co/ofertas-relampago)  
**Captura:** 2026-10-08T22:52:14.750Z

---

## [Opiniones de productos](../markdown/opiniones-sobre-producto.md)

Actualización indicada por la fuente: 18/09/2026. Captura: 2026-10-08T22:52:15.922Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/opiniones-sobre-producto](https://developers.mercadolibre.com.co/es_co/opiniones-sobre-producto)

# Opiniones de productos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 18/09/2026  
**Captura:** 2026-10-08T22:52:15.922Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/opiniones-sobre-producto](https://developers.mercadolibre.com.co/es_co/opiniones-sobre-producto)

## Resumen

Explica cómo mostrar a compradores las evaluaciones de un producto. El flujo parte del `item_id` y consulta las reseñas del ítem; para productos de catálogo puede enviarse `catalog_product_id`. La API es de solo lectura y no genera notificaciones/webhooks en tiempo real. `offset` inicia en 0 y `limit` tiene valor predeterminado 5; `catalog_product_id` filtra evaluaciones de un producto de catálogo. la respuesta de paginación contiene `total`, `limit`, `offset` y `total_pageable`. Errores documentados: 400 por ID/limit/offset inválido, 401 token inválido, 403 permisos, 404 ítem inexistente/eliminado y 429 rate limit.

## Contenido y conceptos documentados

- La fuente describe paginación y campos raíz de las evaluaciones, además de campos de uso interno y sensibles. También detalla disponibilidad por sitio, restricciones por país y casos de usuarios CBT.
- El endpoint de reseñas está disponible para los sitios MLB, MLA, MLM, MLC, MCO, MPE y MLU. El identificador del ítem puede obtenerse previamente mediante la API de ítems. Respuesta/errores no transcritos en esta ficha: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### GET /items/{ITEM_ID}

**Método:** `GET`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el identificador de publicación para el flujo descrito.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### GET /reviews/item/{ITEM_ID}

**Método:** `GET`  
**Ruta:** `/reviews/item/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta evaluaciones de un ítem; admite `catalog_product_id` para producto de catálogo.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `catalog_product_id` (query, opcional): Identificador de producto de catálogo; aparece en el ejemplo opcional.
- `offset` (query, opcional): Posición inicial; predeterminado 0.
- `limit` (query, opcional): Cantidad por página; predeterminado 5.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": "400",   "meaning": "ID, limit u offset inválido." } ```
- ```json {   "code": "401",   "meaning": "Token inválido, expirado o mal formado." } ```
- ```json {   "code": "403",   "meaning": "El token no tiene permisos necesarios." } ```
- ```json {   "code": "404",   "meaning": "El ítem no existe, se eliminó o pertenece a otro sitio." } ```
- ```json {   "code": "429",   "meaning": "Se excedió el rate limit." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/opiniones-sobre-producto](https://developers.mercadolibre.com.co/es_co/opiniones-sobre-producto)  
**Captura:** 2026-10-08T22:52:15.922Z

---

## [Packs](../markdown/gestion-packs.md)

Actualización indicada por la fuente: 29/12/2025. Captura: 2026-10-08T22:52:18.512Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/gestion-packs](https://developers.mercadolibre.com.co/es_co/gestion-packs)

# Packs

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:52:18.512Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestion-packs](https://developers.mercadolibre.com.co/es_co/gestion-packs)

## Resumen

Describe la relación entre packs, órdenes, pagos y envíos para gestionar ventas agrupadas. El flujo consulta primero el pack, luego sus órdenes, y obtiene los detalles de envío desde el recurso de shipments.

## Contenido y conceptos documentados

- Los cupones y descuentos no deben interpretarse solo desde `discount` en el nodo de pagos de la orden; la fuente recomienda los recursos específicos de descuentos/promociones. Para despachar, el vendedor puede marcar que ya tiene el producto mediante `ready_to_ship`.
- Los ejemplos usan OAuth Bearer. Los esquemas completos de pack y orden: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /api.mercadopago.com/v1/payments/{id}

La fuente menciona la ruta /api.mercadopago.com/v1/payments/{id}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/api.mercadopago.com/v1/payments/{id}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /orders/{ORDER_ID}/discounts

La fuente menciona la ruta /orders/{ORDER_ID}/discounts, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/orders/{ORDER_ID}/discounts`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### GET /orders/{ORDER_ID}

**Método:** `GET`  
**Ruta:** `/orders/{ORDER_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el detalle de una orden del pack.

**Parámetros**

- `ORDER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "order_items",
    "payments",
    "shipping"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /packs/{PACK_ID}

**Método:** `GET`  
**Ruta:** `/packs/{PACK_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el pack y sus órdenes vinculadas.

**Parámetros**

- `PACK_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "orders"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /shipments/{SHIPMENT_ID}/process/ready_to_ship

**Método:** `POST`  
**Ruta:** `/shipments/{SHIPMENT_ID}/process/ready_to_ship`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Marca disponibilidad del producto para iniciar el despacho.

**Parámetros**

- `SHIPMENT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestion-packs](https://developers.mercadolibre.com.co/es_co/gestion-packs)  
**Captura:** 2026-10-08T22:52:18.512Z

---

## [Pagos](../markdown/pagos.md)

Actualización indicada por la fuente: 29/12/2025. Captura: 2026-10-08T22:52:19.350Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/pagos](https://developers.mercadolibre.com.co/es_co/pagos)

# Pagos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:52:19.350Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/pagos](https://developers.mercadolibre.com.co/es_co/pagos)

## Resumen

La página orienta sobre la gestión de pagos mediante Mercado Pago y explica la suscripción al tópico de notificaciones `payments`. También presenta el flujo de devolución de dinero en cuenta para ciertas ventas canceladas.

## Contenido y conceptos documentados

- Para recibir eventos de pago, la aplicación debe suscribirse al tópico `payments`; la página remite a la documentación de Mercado Pago para integración de pagos.
- El flujo de devolución descrito aplica a vendedores de México y se anuncia próximamente para Argentina y Brasil. Para compradores elegibles que paguen con tarjeta, la devolución puede acreditarse como dinero en cuenta; la orden conserva estado `paid`, aparece el tag `unfulfilled` y el pago incluye `refund_account_money`.
- Esta página no documenta una operación HTTP concreta ni el esquema de una solicitud de API.

## Operaciones de API

## Conceptos y recursos asociados

### Pagos

La página orienta sobre la gestión de pagos mediante Mercado Pago y explica la suscripción al tópico de notificaciones `payments`. También presenta el flujo de devolución de dinero en cuenta para ciertas ventas canceladas.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/pagos](https://developers.mercadolibre.com.co/es_co/pagos)  
**Captura:** 2026-10-08T22:52:19.350Z

---

## [Pagos](../markdown/reportes-pagos.md)

Actualización indicada por la fuente: 20/05/2025. Captura: 2026-10-08T22:52:20.308Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/reportes-pagos](https://developers.mercadolibre.com.co/es_co/reportes-pagos)

# Pagos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 20/05/2025  
**Captura:** 2026-10-08T22:52:20.308Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/reportes-pagos](https://developers.mercadolibre.com.co/es_co/reportes-pagos)

## Resumen

Documenta la consulta de pagos de facturas de un vendedor dentro de un período y la consulta del detalle de cargos y percepciones asociados a un pago.

## Contenido y conceptos documentados

- El período usa la clave `YYYY-mm-dd`. La consulta admite `sort_by` (`ID` o `DATE`), `order_by` (`ASC` o `DESC`), `offset` (0–10000) y `limit` (1–1000; valor predeterminado 150).
- `payment_id` es de tipo string para admitir identificadores alfanuméricos. El resumen puede incluir `credit_note_number`, fechas, tipo/método/estado, montos aplicados en este u otros períodos, saldo y devolución. El detalle incluye `association_amount`, `payment_amount`, `detail_id`, descripción y fecha del cargo.
- OAuth Bearer aparece en los ejemplos; errores: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### GET /billing/integration/payment/{PAYMENT_ID}/charges

**Método:** `GET`  
**Ruta:** `/billing/integration/payment/{PAYMENT_ID}/charges`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta cargos y percepciones asociados a un pago.

**Parámetros**

- `PAYMENT_ID` (path, obligatorio)
- `sort_by` (query, opcional): Valores ID o DATE.
- `order_by` (query, opcional): Orden ascendente o descendente.
- `offset` (query, opcional): Desplazamiento de resultados.
- `limit` (query, opcional): Límite de resultados; máximo 1000.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "payment_info",
    "charge_info",
    "detail_id",
    "detail_description",
    "detail_date"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /billing/integration/periods/key/{KEY}/group/ML/payment/details

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/{KEY}/group/ML/payment/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalle de facturas/pagos para un período.

**Parámetros**

- `KEY` (path, obligatorio)
- `sort_by` (query, opcional): Valores ID o DATE; predeterminado ID.
- `order_by` (query, opcional): Valores ASC o DESC; predeterminado ASC.
- `offset` (query, opcional): Rango documentado 0 a 10000; predeterminado 0.
- `limit` (query, opcional): Rango 1 a 1000; predeterminado 150.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "payment_id",
    "credit_note_number",
    "payment_date",
    "payment_type",
    "payment_method",
    "payment_status",
    "payment_amount",
    "amount_in_this_period",
    "amount_in_other_period",
    "remaining_amount",
    "return_amount"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/reportes-pagos](https://developers.mercadolibre.com.co/es_co/reportes-pagos)  
**Captura:** 2026-10-08T22:52:20.308Z

---

## [Percepciones](../markdown/resumen-percepciones.md)

Actualización indicada por la fuente: 12/03/2026. Captura: 2026-10-08T22:52:21.229Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/resumen-percepciones](https://developers.mercadolibre.com.co/es_co/resumen-percepciones)

# Percepciones

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 12/03/2026  
**Captura:** 2026-10-08T22:52:21.229Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/resumen-percepciones](https://developers.mercadolibre.com.co/es_co/resumen-percepciones)

## Resumen

Permite consultar el resumen de percepciones de un período y luego recuperar el detalle de una percepción de Mercado Libre o Mercado Pago. La fuente aclara que esta funcionalidad aplica solamente a Argentina.

## Contenido y conceptos documentados

- El resumen puede filtrarse por grupo de facturación (`ML` o `MP`) y moneda (`USD` o `ARS`). Sus campos incluyen `document_id`, `society`, `legal_document_number`, condición fiscal, monto, tipo/régimen impositivo, base imponible, alícuota, coeficiente, fecha y estado.
- En el detalle se usan datos del resumen: `tax_type` y `document_id`; para Mercado Pago también `tax_id`. El detalle puede variar por régimen e incluye datos como `detail_id`, `taxable_amount`, `tax_amount`, transacción, importes y moneda.
- Autenticación mostrada: OAuth Bearer. Errores no especificados: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### GET /billing/integration/group/ML/perceptions/details

**Método:** `GET`  
**Ruta:** `/billing/integration/group/ML/perceptions/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el detalle de percepciones de Mercado Libre; admite `document_id`, `tax_type`, paginación y moneda.

**Parámetros**

- `document_id` (query, obligatorio): Documento que se consulta.
- `tax_type` (query, obligatorio): Código del tipo de impuesto.
- `offset` (query, opcional): Desplazamiento.
- `limit` (query, opcional): Cantidad de resultados.
- `currency` (query, opcional): Moneda: USD o ARS.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "offset",
    "limit",
    "total",
    "results",
    "detail_id",
    "date_created",
    "taxable_amount",
    "tax_amount",
    "amount",
    "gross_amount",
    "currency",
    "errors"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /billing/integration/group/MP/perceptions/details

**Método:** `GET`  
**Ruta:** `/billing/integration/group/MP/perceptions/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el detalle de percepciones de Mercado Pago; admite además `tax_id`.

**Parámetros**

- `document_id` (query, obligatorio): Documento que se consulta.
- `tax_type` (query, obligatorio): Código del tipo de impuesto.
- `tax_id` (query, obligatorio): Identificador del impuesto requerido en el flujo MP.
- `offset` (query, opcional): Desplazamiento.
- `limit` (query, opcional): Cantidad de resultados.
- `currency` (query, opcional): Moneda: USD o ARS.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "offset",
    "limit",
    "total",
    "results",
    "detail_id",
    "movement_id",
    "reference_id",
    "taxable_amount",
    "tax_amount",
    "amount",
    "gross_amount",
    "currency",
    "errors"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /billing/integration/periods/key/{KEY}/perceptions/summary

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/{KEY}/perceptions/summary`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el resumen de percepciones del período; se muestra filtro `group` y `currency`.

**Parámetros**

- `KEY` (path, obligatorio)
- `group` (query, opcional): Grupo de facturación; ejemplos ML y MP.
- `currency` (query, opcional): Moneda: USD o ARS.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "summary",
    "document_id",
    "society",
    "legal_document_number",
    "amount",
    "tax_type",
    "taxable_amount",
    "aliquot",
    "currency",
    "errors"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/resumen-percepciones](https://developers.mercadolibre.com.co/es_co/resumen-percepciones)  
**Captura:** 2026-10-08T22:52:21.229Z

---

## [Planes de reposición para fulfilment](../markdown/planes-de-reposicion-para-fulfilment.md)

Actualización indicada por la fuente: 17/09/2026. Captura: 2026-10-08T22:52:22.464Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/planes-de-reposicion-para-fulfilment](https://developers.mercadolibre.com.co/es_co/planes-de-reposicion-para-fulfilment)

# Planes de reposición para fulfilment

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 17/09/2026  
**Captura:** 2026-10-08T22:52:22.464Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/planes-de-reposicion-para-fulfilment](https://developers.mercadolibre.com.co/es_co/planes-de-reposicion-para-fulfilment)

## Resumen

El recurso entrega para un User Product información consolidada de identificación, producto, stock, ventas, beneficios y recomendación de reposición en Full. La recomendación es informativa: no reserva capacidad y el seller decide qué cantidad enviar.

## Contenido y conceptos documentados

- Requiere OAuth2 con token del seller propietario, `user_product_id` con prefijo admitido y `country` obligatorio en mayúsculas. El límite documentado es 500 solicitudes por 60 segundos por seller, variable por instancia; sobre el límite responde 429. Repeticiones idénticas frecuentes pueden causar bloqueo temporal.
- La respuesta 200 puede incluir `identifiers`, `product`, `stock`, `sales`, `recommendation` y `eligibility_benefits`; los campos dinámicos describen urgencia, cantidades exactas o rangos, períodos de ventas y tags. Si hay datos complementarios parciales, devuelve 206 y `X-Content-Missing`.
- Errores documentados: 400 `invalid_request`, 403 `access_denied`, 404 `not_found`, 429 `too_many_requests`, 500 `internal_error`, 503 `service_unavailable`.

## Operaciones de API
## Operaciones de API

### GET /marketplace/fbm/user-products/{user_product_id}/replenishment

**Método:** `GET`  
**Ruta:** `/marketplace/fbm/user-products/{user_product_id}/replenishment`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la recomendación de reposición; requiere query `country`.

**Parámetros**

- `user_product_id` (path, obligatorio)
- `country` (query, obligatorio): Código de país de dos letras en mayúsculas.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "identifiers",
    "product",
    "stock",
    "sales",
    "recommendation",
    "eligibility_benefits",
    "X-Content-Missing"
  ],
  "summary": "La fuente documenta estructuras distintas en respuestas 200 y 206."
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "invalid_request: parámetros, tipos o headers inválidos." } ```
- ```json {   "code": "403",   "meaning": "access_denied: seller/caller no autorizado." } ```
- ```json {   "code": "404",   "meaning": "not_found: recurso, recomendación o vínculo inexistente." } ```
- ```json {   "code": "429",   "meaning": "too_many_requests: se excedió el límite." } ```
- ```json {   "code": "500",   "meaning": "internal_error." } ```
- ```json {   "code": "503",   "meaning": "service_unavailable." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/planes-de-reposicion-para-fulfilment](https://developers.mercadolibre.com.co/es_co/planes-de-reposicion-para-fulfilment)  
**Captura:** 2026-10-08T22:52:22.464Z

---

## [Pre-acordado por ítem y liquidación stock Full](../markdown/descuento-pre-acordado-por-item.md)

Actualización indicada por la fuente: 09/06/2026. Captura: 2026-10-08T22:52:23.677Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/descuento-pre-acordado-por-item](https://developers.mercadolibre.com.co/es_co/descuento-pre-acordado-por-item)

# Pre-acordado por ítem y liquidación stock Full

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 09/06/2026  
**Captura:** 2026-10-08T22:52:23.677Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/descuento-pre-acordado-por-item](https://developers.mercadolibre.com.co/es_co/descuento-pre-acordado-por-item)

## Resumen

Documenta campañas de descuento pre-acordado por ítem (`PRE_NEGOTIATED`) y de liquidación de stock Full (`UNHEALTHY_STOCK`), que comparten la lógica de consulta, aceptación y retiro de ofertas.

## Contenido y conceptos documentados

- Los detalles de campaña incluyen `id`, `type`, `status`, fechas, nombre y ofertas con precio original/final, estado, fechas y `benefits` (`type`, `meli_percent`, `seller_percent`). El filtro `status_item` admite `active` o `paused`.
- Puede existir boost adicional: `boosted_offer`, `discount_meli_boosted_percentage`, `discount_meli_boost_amount` y `total_price_for_boosted_offer`, solo cuando `boosted_offer=true`. La página incluye vista de vendedor, estados y parámetros de aceptación/eliminación.
- Autenticación mostrada: OAuth Bearer. Detalles no listados: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### DELETE /seller-promotions/items/{ITEM_ID}

**Método:** `DELETE`  
**Ruta:** `/seller-promotions/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la oferta; se identifican `promotion_type`, `promotion_id` y `offer_id` en la consulta.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `promotion_type` (query, obligatorio): Tipo de campaña.
- `promotion_id` (query, obligatorio): Identificador de campaña.
- `offer_id` (query, obligatorio): Identificador de oferta.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /seller-promotions/items/{ITEM_ID}

**Método:** `GET`  
**Ruta:** `/seller-promotions/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la oferta del ítem; puede devolver los campos condicionales de boost.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `promotion_type` (query, obligatorio): Tipo de promoción; PRE_NEGOTIATED o UNHEALTHY_STOCK.
- `app_version` (query, obligatorio): La fuente usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "boosted_offer",
    "discount_meli_boosted_percentage",
    "discount_meli_boost_amount",
    "total_price_for_boosted_offer"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente indica consultar los campos boost a través del endpoint de ítem.

### GET /seller-promotions/promotions/{PROMOTION_ID}

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{PROMOTION_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta detalles de una campaña; usa `promotion_type` y `app_version=v2`.

**Parámetros**

- `PROMOTION_ID` (path, obligatorio)
- `promotion_type` (query, obligatorio): PRE_NEGOTIATED o UNHEALTHY_STOCK.
- `app_version` (query, obligatorio): La fuente usa v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "type",
    "status",
    "start_date",
    "finish_date",
    "deadline_date",
    "name",
    "offers"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### GET /seller-promotions/promotions/{PROMOTION_ID}/items

**Método:** `GET`  
**Ruta:** `/seller-promotions/promotions/{PROMOTION_ID}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta ofertas de la campaña; admite `promotion_type`, `app_version` y `status_item`.

**Parámetros**

- `PROMOTION_ID` (path, obligatorio)
- `promotion_type` (query, obligatorio): PRE_NEGOTIATED o UNHEALTHY_STOCK.
- `app_version` (query, obligatorio): La fuente usa v2.
- `status_item` (query, opcional): Filtro; admite active o paused.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "results",
    "id",
    "offer_id",
    "price",
    "original_price",
    "status",
    "benefits",
    "paging"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

### POST /seller-promotions/items/{ITEM_ID}

**Método:** `POST`  
**Ruta:** `/seller-promotions/items/{ITEM_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Acepta/indica el descuento para el ítem.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/descuento-pre-acordado-por-item](https://developers.mercadolibre.com.co/es_co/descuento-pre-acordado-por-item)  
**Captura:** 2026-10-08T22:52:23.677Z

---

## [Precio por cantidad](../markdown/precio-por-cantidad.md)

Actualización indicada por la fuente: 25/08/2026. Captura: 2026-10-08T22:52:24.852Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/precio-por-cantidad](https://developers.mercadolibre.com.co/es_co/precio-por-cantidad)

# Precio por cantidad

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 25/08/2026  
**Captura:** 2026-10-08T22:52:24.852Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/precio-por-cantidad](https://developers.mercadolibre.com.co/es_co/precio-por-cantidad)

## Resumen

Gestiona precios mayoristas absolutos B2B mediante rangos de cantidad mínima. La guía señala que el endpoint heredado será discontinuado desde el 27/10/2026 para PxQ absoluto; seguirá destinado a Precios netos por cantidad. La disponibilidad descrita es MLB, MLM, MLC y MLA, para vendedores habilitados con tag business.

## Contenido y conceptos documentados

- Cada rango se representa como un precio standard con conditions.min_purchase_unit y context_restrictions que incluyen channel_marketplace y user_type_business. Una publicación admite una única tabla y hasta cinco rangos, con precio decreciente al aumentar la cantidad.
- Al modificar la tabla, enviar solo el id conserva el nodo; omitir un id existente lo elimina; enviar un nodo sin id crea precio. La respuesta puede asignar un id diferente al enviado. Moneda debe coincidir con el precio estándar; la guía indica error 404 si difiere.
- Los vendedores habilitados se identifican con tag business en /users; las publicaciones con la configuración usan standard_price_by_quantity. Los cambios notifican el tópico items prices.
- La consulta de precios puede usar el header show-all-prices; sale_price recibe context y quantity para resolver el precio por canal, tipo de comprador y cantidad.

En los ejemplos de la fuente se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /orders

La fuente menciona la ruta /orders, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/orders`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Identificar publicación con PxQ

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el ítem para detectar la etiqueta standard_price_by_quantity.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

tags de la publicación; se identifica standard_price_by_quantity.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de publicación con la etiqueta PxQ.

### Consultar tabla de precios

**Método:** `GET`  
**Ruta:** `/items/{item_id}/prices`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve precios vigentes; show-all-prices permite solicitar la vista ampliada de PxQ.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `show-all-prices` (header, opcional): TRUE/FALSE, opcional para ver todos los rangos.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id y prices[] con tipo, importe, moneda, condiciones y restricciones de contexto.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de prices con show-all-prices: TRUE.

### Calcular precio de venta por cantidad

**Método:** `GET`  
**Ruta:** `/items/{item_id}/sale_price`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Resuelve el precio ganador para canal y comprador con la cantidad solicitada.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `context` (query, opcional): Canales y contexto de comprador; el ejemplo usa channel_marketplace,user_type_business.
- `quantity` (query, opcional): Cantidad solicitada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Precio de venta calculado para el contexto y la cantidad.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con channel_marketplace,user_type_business y cantidad.

### Consultar tag Business

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Permite comprobar si el vendedor tiene el tag business asociado a PxQ.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, tags y demás datos de usuario.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La respuesta incluye business en tags.

### Definir precios absolutos por cantidad

**Método:** `POST`  
**Ruta:** `/items/{item_id}/prices/standard/quantity`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea, conserva o elimina nodos standard de la tabla PxQ.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `prices` (body, obligatorio): Lista de precios por cantidad.
- `id` (body, opcional): Si se envía conserva un nodo existente; omitirlo lo elimina; sin id crea un precio.
- `amount` (body, opcional): Monto del precio.
- `currency_id` (body, opcional): Moneda, igual a la del precio estándar.
- `conditions` (body, opcional): Incluye context_restrictions y min_purchase_unit.

**Solicitud**

prices[] con id para conservar un nodo; para crear, amount, currency_id y conditions.context_restrictions/min_purchase_unit.

**Respuesta**

id del ítem y prices[] con id, amount, currency_id y conditions.

**Errores documentados**

- 404: la moneda del PxQ y la del precio estándar son distintas.
- La omisión de un id existente elimina ese nodo; más de cinco rangos no está permitido.

**Ejemplos**

- Ejemplos con una tabla y con cinco rangos.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/precio-por-cantidad](https://developers.mercadolibre.com.co/es_co/precio-por-cantidad)  
**Captura:** 2026-10-08T22:52:24.852Z

---

## [Precio por variación](../markdown/precio-variacion.md)

Actualización indicada por la fuente: 13/08/2026. Captura: 2026-10-08T22:52:28.176Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/precio-variacion](https://developers.mercadolibre.com.co/es_co/precio-variacion)

# Precio por variación

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 13/08/2026  
**Captura:** 2026-10-08T22:52:28.176Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/precio-variacion](https://developers.mercadolibre.com.co/es_co/precio-variacion)

## Resumen

Describe la migración al modelo User Products, donde las condiciones de venta y los ítems de una misma familia se gestionan como productos relacionados. La activación es gradual; los vendedores nuevos se identifican por user_product_seller. La guía incluye publicación, edición de familias y variantes, consulta y migración de publicaciones antiguas.

## Contenido y conceptos documentados

- En el modelo nuevo, family_name es obligatorio al publicar; title se genera y no debe enviarse. El array variations deja de ser la representación de variantes y aparecen family_id y user_product_id. Cada User Product admite hasta 30 condiciones de venta (ítems).
- Las variantes comparten atributos parent PK; child PK identifican variaciones. La edición de familia separa common_content compartido y atributos específicos por user_product. Las tareas de edición de familia/variantes se procesan de forma asíncrona; hay que incluir todos los productos existentes de la familia cuando se actualizan variantes.
- Agregar una variante requiere todos los child PKs de la familia e imágenes; PARENT_PK, family_name y domain_id no se envían en esa operación. Actualizar familia admite family_name, domain_id y atributos parent PK/ITEM_CONDITION; KIT no es compatible con el recurso de actualización de familia.
- Para agregar una condición de venta a User Product se envían precio, categoría, moneda, modo de compra y tipo de publicación. title, domain_id, family_name, imágenes, atributos y stock se heredan/generan; no deben enviarse.
- UPtin migra cada variación a un nuevo ítem de manera asíncrona; se valida elegibilidad, se inicia una migración por ítem y se consulta su estado. El ítem origen permanece activo durante el proceso y luego se cierra.

En los ejemplos de la fuente se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar estado de migración

**Método:** `GET`  
**Ruta:** `/items/{item_original}/migration_live_listing`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el progreso y los nuevos ítems creados por la migración.

**Parámetros**

- `item_original` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

item_id, migration_completed, activation_completed, date_created, last_updated y new_items[] con new_item_id, variation_id, migration_status.

**Errores documentados**

- 200: consulta; 404: no fue posible realizar la migración.

**Ejemplos**

- Estados de migración pending/created.

### Validar elegibilidad de migración UPtin

**Método:** `GET`  
**Ruta:** `/items/{item_original}/user_product_listings/validate`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Determina si un ítem antiguo puede migrarse al formato User Products.

**Parámetros**

- `item_original` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

is_valid y cause[] con code, message y reference.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Elegibilidad requiere user_product_id, item multivariante y que no exista duplicado.

### Consultar productos de una familia por sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/user-products-families/{family_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve User Products asociados a la familia y el sitio.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `family_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

user_products_ids, family_id, site_id y user_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo para site MLA.

### Consultar familia

**Método:** `GET`  
**Ruta:** `/user-products-families/{family_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lee datos compartidos de la familia y sus atributos.

**Parámetros**

- `family_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

family_id, family_name, user_id, domain_id, attributes, child_attributes_ids y custom_attributes_names.

**Errores documentados**

- 200: OK; 404: no existe family_id.

**Ejemplos**

- Respuesta con BRAND, MODEL e ITEM_CONDITION.

### Listar variantes de familia

**Método:** `GET`  
**Ruta:** `/user-products-families/{family_id}/user-products`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve User Product IDs de la familia.

**Parámetros**

- `family_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

family_id y user_products_ids.

**Errores documentados**

- 200: OK; 404: no hay asociación para family_id.

**Ejemplos**

- Se recomienda consultar antes del PUT de variantes.

### Consultar tarea de familia

**Método:** `GET`  
**Ruta:** `/user-products-families/tasks/{task_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera estado y resultado por producto de una tarea asíncrona.

**Parámetros**

- `task_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

task_id, status, user-products[] con id, status, processed_date, last_updated y reasons.

**Errores documentados**

- 200: consulta; 404: Task not found.

**Ejemplos**

- Respuesta con productos succeeded, pending o failed.

### Consultar User Product

**Método:** `GET`  
**Ruta:** `/user-products/{user_product_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalle del producto, atributos, imágenes y familia.

**Parámetros**

- `user_product_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, name, user_id, domain_id, attributes, pictures, thumbnail, catalog_product_id, family_id, tags y fechas.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de User Product con memoria y condición.

### Buscar ítems asociados a User Product

**Método:** `GET`  
**Ruta:** `/users/{seller_id}/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Filtra ítems del vendedor mediante user_product_id.

**Parámetros**

- `seller_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `user_product_id` (query, obligatorio): Identificador del User Product.

**Solicitud**

No documentado en la fuente.

**Respuesta**

seller_id, results y paging.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de búsqueda por user_product_id.

### Consultar activación de User Products

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Comprueba el tag user_product_seller que identifica vendedores encendidos.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id y tags del usuario.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Respuesta con user_product_seller.

### Publicar ítem en modelo User Products

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una publicación con family_name; la plataforma genera title y user_product_id.

**Parámetros**

- `family_name` (body, obligatorio): Nombre genérico de la familia.
- `category_id` (body, obligatorio): Categoría del producto.
- `price` (body, obligatorio): Precio; puede diferir por condición de venta.
- `currency_id` (body, obligatorio): Moneda.
- `available_quantity` (body, obligatorio): Stock inicial.
- `attributes` (body, obligatorio): Atributos de familia/variante.

**Solicitud**

Datos de ítem: family_name, category_id, price, currency_id, available_quantity, sale_terms, buying_mode, listing_type_id, condition, pictures y attributes. No enviar title.

**Respuesta**

Ítem con title generado, family_name, user_product_id y datos de publicación.

**Errores documentados**

- 400: el modelo anterior de publicación no es aceptado tras activar el seller.

**Ejemplos**

- Ejemplos de dos ítems de distinto color agrupados por family_name.

### Iniciar migración UPtin

**Método:** `POST`  
**Ruta:** `/sites/{site_id}/items/user_product_listings`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Solicita migración de un ítem antiguo; se realiza de forma asíncrona.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `item_id` (body, obligatorio): Ítem origen que se migrará.

**Solicitud**

item_id.

**Respuesta**

200 OK; inicio del proceso asíncrono.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Un POST por cada ítem a migrar.

### Actualizar datos de familia y variantes mediante tarea

**Método:** `POST`  
**Ruta:** `/user-products-families/{family_id}/tasks`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Envía common_content y atributos por User Product en una tarea asíncrona.

**Parámetros**

- `family_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `common_content` (body, opcional): family_name, domain_id y atributos compartidos.
- `user_products` (body, obligatorio): Debe incluir todos los User Products existentes.
- `attributes` (body, obligatorio): Atributos diferenciados por cada producto.

**Solicitud**

common_content compartido y user_products[] con id y attributes. Incluir todos los User Products de la familia; no duplicar atributos entre niveles.

**Respuesta**

task_id, status y date_created.

**Errores documentados**

- 202: tarea aceptada; 400: formato, campos faltantes o producto ajeno a familia; 401: token; 404: familia inexistente.
- Errores de tarea incluyen fields.to_update.missing, user_products.null/incomplete, atributos faltantes o duplicados y conflicto entre common_content y atributos del producto.
- cause_id 31 fields.to_update.missing: no se enviaron cambios.
- cause_id 32 common_content.family_name.null: family_name no puede ser null.
- cause_id 33 common_content.domain_id.null: domain_id no puede ser null.
- cause_id 34 common_content.attributes.null: attributes compartidos no pueden ser null.
- cause_id 35 user_products.null: el array no puede ser null ni vacío.
- cause_id 36 user_products.id.null: falta id en user_products.
- cause_id 37 user_products.attributes.null: attributes por producto no pueden ser null.
- cause_id 38 user_products.incomplete: faltan productos de la familia.
- cause_id 39 user_products.family_not_exist: familia inexistente.
- cause_id 40 user_products.attribute_id.missing: falta attribute_id.
- cause_id 41 user_products.attribute_name.missing: falta attribute_name.
- cause_id 42 user_products.attribute_values.missing: faltan values del atributo.
- cause_id 43 user_products.attribute_value_id.missing: falta value_id.
- cause_id 44 user_products.attribute_value_name.missing: falta value_name.
- cause_id 45 user_products.duplicated_attribute: atributo duplicado en un producto.
- cause_id 46 user_products.update.failed: fallo inesperado en la actualización.
- cause_id 47 user_products.miss_match_attribute: child PK/custom no enviado a todos los productos cuando corresponde.
- cause_id 48 user_products.duplicated_attribute.by_common_content_and_by_user_product: atributo duplicado entre common_content y producto.
- cause_id 51 user_products.attributes.number_unit: unidad en value_name incorrecta.
- cause_id 55 family_id.collision: actualización produciría una familia ya mapeada.

**Ejemplos**

- Ejemplo con atributos comunes y atributos específicos por producto.

### Agregar variante a familia

**Método:** `POST`  
**Ruta:** `/user-products-families/{family_id}/user-products`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una variante dentro de una familia existente sin cambiar family_id.

**Parámetros**

- `family_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `attributes` (body, obligatorio): Todos los child PKs de la familia; no enviar parent PK ni domain_id.
- `pictures` (body, obligatorio): Al menos una imagen.
- `main_features` (body, opcional): Características; origin se envía en minúscula seller.

**Solicitud**

attributes con todos los child PKs; pictures con al menos una imagen; main_features opcional.

**Respuesta**

User Product con id, name, family_name, domain_id, attributes, pictures, family_id y main_features.

**Errores documentados**

- 201: creada; 400: falta campo/child PK, parent PK o campos no permitidos; 401: token; 404: familia inexistente.

**Ejemplos**

- Ejemplo de variante con COLOR y SIZE.

### Agregar condición de venta

**Método:** `POST`  
**Ruta:** `/user-products/{user_product_id}/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea un ítem/publicación que representa una condición de venta del User Product.

**Parámetros**

- `user_product_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `price` (body, obligatorio): Precio.
- `category_id` (body, obligatorio): Categoría.
- `currency_id` (body, obligatorio): Moneda.
- `buying_mode` (body, obligatorio): buy_it_now en ejemplo.
- `listing_type_id` (body, obligatorio): Tipo de publicación.
- `catalog_product_id` (body, opcional): Solo si catalog_listing=true.

**Solicitud**

price, category_id, currency_id, buying_mode y listing_type_id requeridos; shipping, channels, tags, sale_terms, catalog_listing, catalog_product_id y official_store_id opcionales/condicionales.

**Respuesta**

HTTP 201 con el ítem y user_product_id/family_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos básicos, de catálogo y con campos opcionales.

### Editar atributos de ítem asociado

**Método:** `PUT`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La guía indica continuar actualizando ítems mediante PUT /items; cambios en atributos compartidos se replican al User Product de forma asíncrona.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente enumera atributos sincronizables como family_name, domain_id, catalog_product_id, pictures y tags.

### Actualizar datos comunes de familia

**Método:** `PUT`  
**Ruta:** `/user-products-families/{family_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza family_name, domain_id y atributos parent PK/ITEM_CONDITION; los productos se replican después de forma asíncrona.

**Parámetros**

- `family_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `family_name` (body, opcional): No puede ser null ni vacío.
- `domain_id` (body, opcional): No puede ser null.
- `attributes` (body, opcional): Atributos parent PK o ITEM_CONDITION; no admite custom.

**Solicitud**

family_name, domain_id y/o attributes de tipo PARENT_PK o ITEM_CONDITION.

**Respuesta**

201 con family_id, family_name, domain_id, attributes, child_attributes_ids y custom_attributes_names.

**Errores documentados**

- 400: payload vacío, nombre inválido, atributo custom/duplicado o ITEM_CONDITION vacío; 403: caller no coincide con dueño; 404: familia inexistente/sin productos; 409: bloqueada o hash de otra familia.

**Ejemplos**

- La semántica de values permite conservar, eliminar o modificar atributos según esté ausente, vacío o contenga valores.

### Actualizar variantes de familia

**Método:** `PUT`  
**Ruta:** `/user-products-families/{family_id}/user-products`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica, agrega o elimina atributos child PK/custom para las variantes; procesamiento asíncrono.

**Parámetros**

- `family_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `user_products` (body, obligatorio): Debe incluir todas las variantes existentes.
- `attributes` (body, obligatorio): Atributos child PK o custom, con name en cada objeto.

**Solicitud**

user_products[] con id y attributes[]; todos los productos de familia y cada atributo con name. No enviar parent PK, family_name, domain_id ni ITEM_CONDITION.

**Respuesta**

202 con task_id, status pending y date_created.

**Errores documentados**

- 400: campos faltantes o atributos no permitidos; 401: token; 404: familia inexistente. La tarea puede reportar user_products.incomplete.

**Ejemplos**

- Ejemplo de actualización de COLOR/SIZE con task_id.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/precio-variacion](https://developers.mercadolibre.com.co/es_co/precio-variacion)  
**Captura:** 2026-10-08T22:52:28.176Z

---

## [Precios de productos](../markdown/api-de-precios.md)

Actualización indicada por la fuente: 26/02/2026. Captura: 2026-10-08T22:52:29.260Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/api-de-precios](https://developers.mercadolibre.com.co/es_co/api-de-precios)

# Precios de productos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 26/02/2026  
**Captura:** 2026-10-08T22:52:29.260Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/api-de-precios](https://developers.mercadolibre.com.co/es_co/api-de-precios)

## Resumen

Presenta los recursos para resolver el precio de venta ganador y consultar todos los precios vigentes de un ítem. La guía recomienda estos endpoints en lugar de los campos price, base_price y original_price de /items; para creación/edición de ítems se mantiene /items. La edición de precios mediante /prices/standard figura como no disponible todavía en la fuente.

## Contenido y conceptos documentados

- GET sale_price calcula el importe final para un contexto de canal y nivel de comprador; el metadata de promoción solo se entrega si el token pertenece al vendedor del ítem.
- context admite channel_marketplace; channel_proximity, mp_merchants y mp_links se describen como no habilitados aún. Los niveles buyer_loyalty_3 a buyer_loyalty_6 no están disponibles en MLU ni MPE.
- GET prices lista nodos standard y promotion con amount, regular_amount, currency_id, last_updated y conditions.context_restrictions/start_time/end_time. Datos sensibles de promoción pueden ocultarse para token ajeno.
- Antes de cambiar precio por PUT /items, revisar automatización de precio. La guía indica que desde el 18/03/2026 cambiar solo price con automatización produce 400; con otros atributos, el campo price puede ignorarse con warning.
- La operación POST /items/{item_id}/prices/standard se documenta como propuesta todavía no disponible; exige enviar los canales donde está publicado el precio y conditions.context_restrictions.

En los ejemplos de la fuente se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar precios vigentes

**Método:** `GET`  
**Ruta:** `/items/{item_id}/prices`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista precios standard y promocionales del ítem por canal/contexto.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id del ítem y prices[] con id, type, amount, regular_amount, currency_id, last_updated y conditions.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con nodos standard y promotion.

### Consultar precio de venta ganador

**Método:** `GET`  
**Ruta:** `/items/{item_id}/sale_price`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve el precio calculado para el contexto de canal y nivel de comprador.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `context` (query, opcional): Filtro de canal/nivel; la fuente recomienda al menos un canal.

**Solicitud**

No documentado en la fuente.

**Respuesta**

price_id, amount, regular_amount, currency_id, reference_date y metadata de promoción si el token pertenece al seller.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo channel_marketplace,buyer_loyalty_3.

### Editar precios standard (aún no disponible)

**Método:** `POST`  
**Ruta:** `/items/{item_id}/prices/standard`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La fuente describe la futura sustitución del PUT de ítems para editar precios; el recurso aún no está habilitado.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `prices` (body, obligatorio): Lista de precios por canal.
- `conditions.context_restrictions` (body, obligatorio): Canal de venta correspondiente.
- `amount` (body, obligatorio): Nuevo precio.
- `currency_id` (body, obligatorio): Moneda local.

**Solicitud**

prices[] con conditions.context_restrictions, amount y currency_id; incluir canales donde existe precio standard.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- 400: mezcla inválida de nodo sin restricción con otros restringidos; múltiples nodos sin restricción; canales inválidos o canales publicados omitidos.

**Ejemplos**

- Ejemplo con channel_marketplace y channel_mshops.

### Actualizar precio mediante ítem

**Método:** `PUT`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

La guía mantiene la edición mediante PUT en el recurso /items y advierte sobre el efecto de la automatización de precios. La página no muestra aquí el formato completo de URL ni del cuerpo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- Desde 18/03/2026: si hay automatización, una solicitud que actualiza solo price se rechaza con HTTP 400; si price se envía junto con otros atributos, se procesa con HTTP 200 pero price se ignora y se devuelve warning.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/api-de-precios](https://developers.mercadolibre.com.co/es_co/api-de-precios)  
**Captura:** 2026-10-08T22:52:29.260Z

---

## [Precios netos por cantidad](../markdown/precios-netos.md)

Actualización indicada por la fuente: 16/09/2026. Captura: 2026-10-08T22:52:30.357Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/precios-netos](https://developers.mercadolibre.com.co/es_co/precios-netos)

# Precios netos por cantidad

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 16/09/2026  
**Captura:** 2026-10-08T22:52:30.357Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/precios-netos](https://developers.mercadolibre.com.co/es_co/precios-netos)

## Resumen

Permite a vendedores B2B elegibles de Brasil que pertenecen al Régimen Normal y usan el facturador fijar un valor neto por unidad. Mercado Libre calcula el precio final según ubicación del comprador y reglas fiscales. Esta configuración se integra en el flujo PxQ.

## Contenido y conceptos documentados

- El vendedor y el ítem deben ser elegibles: vendedor bajo Régimen Normal con facturador Mercado Libre y publicación con datos fiscales completos. El endpoint devuelve is_user_eligible, is_item_eligible, pending_actions y, si corresponde, causa/message.
- Los nodos se envían como prices[] standard con amount, currency_id, amount_tax_inclusion_type=net y conditions.context_restrictions channel_marketplace/user_type_business más min_purchase_unit. El rango inicial usa min_purchase_unit=1; hasta cinco rangos, con importe decreciente.
- Para reemplazar PxQ porcentual por precios netos, usar remove_percentage_pxq=true; de lo contrario la fuente indica incompatibilidad. La consulta de precios puede usar show-all-prices y x-calculate-net-taxes en sale_price.
- Errores de validación documentados usan invalid.price_per_quantity para tipo fiscal net ausente, min_purchase_unit inicial ausente/cero y orden de importes incoherente.

En los ejemplos de la fuente se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar elegibilidad de usuario e ítem

**Método:** `GET`  
**Ruta:** `/business/v1/sites/{site_id}/users/{user_id}/items/{item_id}/options/net-prices/seller/eligibility`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Valida requisitos fiscales y comerciales para configurar precios netos.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `user_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

user_id, item_id, is_user_eligible, is_item_eligible y pending_actions; puede incluir cause_id/message.

**Errores documentados**

- B2BSO-502: item has no tax information (publicación sin datos fiscales).
- Mensaje documentado: user ineligible for net prices by fiscal identities.

**Ejemplos**

- Ejemplos de usuario e ítem elegibles y de casos no elegibles.

### Identificar publicación con precios netos

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el ítem para encontrar el tag net_taxes_amount_prices.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

tags de publicación.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La guía usa net_taxes_amount_prices para reconocer la configuración.

### Consultar precios netos

**Método:** `GET`  
**Ruta:** `/items/{item_id}/prices`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista precios del ítem, incluidos rangos netos con show-all-prices.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `show-all-prices` (header, opcional): TRUE/FALSE, opcional para obtener los rangos.

**Solicitud**

No documentado en la fuente.

**Respuesta**

prices[] con amount_tax_inclusion_type y condiciones PxQ netas.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de consulta con show-all-prices: TRUE.

### Calcular precio neto por cantidad y destino

**Método:** `GET`  
**Ruta:** `/items/{item_id}/sale_price`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve el precio de venta contextualizado para la cantidad y destino del comprador.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `context` (query, obligatorio): Ejemplo incluye channel_marketplace,user_type_business.
- `quantity` (query, opcional): Cantidad solicitada.
- `destination_states` (query, opcional): Estado de destino; el ejemplo usa código BR-SP.
- `buyer_id` (query, opcional): Identificador del comprador.
- `x-calculate-net-taxes` (header, opcional): El ejemplo lo envía en true para cálculo neto.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Precio de venta calculado y componentes fiscales mostrados en la respuesta.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con comprador, cantidad y destination_states.

### Configurar precios netos por cantidad

**Método:** `POST`  
**Ruta:** `/items/{item_id}/prices/standard/quantity`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea o reemplaza nodos netos standard para compradores B2B.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `remove_percentage_pxq` (query, opcional): Si true elimina nodos PxQ porcentuales y los reemplaza por rangos netos.
- `prices` (body, obligatorio): Nodos de precios netos.
- `amount_tax_inclusion_type` (body, obligatorio): Debe ser net.
- `conditions.min_purchase_unit` (body, obligatorio): El nodo inicial requiere unidad mínima 1; otros nodos aumentan cantidad.
- `conditions.context_restrictions` (body, obligatorio): channel_marketplace y user_type_business.

**Solicitud**

prices[] con type=standard, amount, currency_id, amount_tax_inclusion_type=net y conditions.context_restrictions/min_purchase_unit.

**Respuesta**

id del ítem y prices[] con id, type, amount, currency_id y conditions.

**Errores documentados**

- 400 invalid.price_per_quantity: Net prices require a 'net' tax type across all prices per quantity.
- 400 invalid.price_per_quantity: Net prices require a price per unit amount.
- 400 invalid.price_per_quantity: Price per quantity min purchase unit below the minimum.
- 400 invalid.price_per_quantity: Price per quantity invalid coherence order.

**Ejemplos**

- Ejemplo con remove_percentage_pxq=true y rangos netos.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/precios-netos](https://developers.mercadolibre.com.co/es_co/precios-netos)  
**Captura:** 2026-10-08T22:52:30.357Z

---

## [Precios por cantidad B2C](../markdown/precios-por-cantidad-b2c.md)

Actualización indicada por la fuente: 18/09/2026. Captura: 2026-10-08T22:52:31.595Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/precios-por-cantidad-b2c](https://developers.mercadolibre.com.co/es_co/precios-por-cantidad-b2c)

# Precios por cantidad B2C

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 18/09/2026  
**Captura:** 2026-10-08T22:52:31.595Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/precios-por-cantidad-b2c](https://developers.mercadolibre.com.co/es_co/precios-por-cantidad-b2c)

## Resumen

Documenta los descuentos porcentuales por cantidad para compradores B2C en neumáticos. La guía describe disponibilidad MLB/MLM/MLA con fechas de activación indicadas por país, máximo de dos rangos y cantidades mínimas 2 y 4. Para escribir se requiere la versión actual del precio mediante el header x-version.

## Contenido y conceptos documentados

- Los nodos están en price_per_quantity[] como type=discount_percentage, percentage y conditions con channel_marketplace, min_purchase_unit y eligible=true. No usan user_type_business.
- El POST reemplaza la lista completa: omitir un id existente elimina ese nodo; para modificar un precio se elimina y se crea uno nuevo. No hay actualización in situ.
- Antes de escribir, GET /items/{item_id}/prices?display_version=true devuelve version; enviar esa versión como x-version en la escritura. En Automotive Tires solo se permiten dos rangos, min_purchase_unit 2 y 4.
- Los precios B2C aparecen en price_per_quantity, mientras prices[] conserva los nodos estándar. El precio final se consulta con sale_price?quantity=...; el metadata puede marcar is_price_per_quantity=true.

En los ejemplos de la fuente se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Identificar ítem con precio por cantidad

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la publicación y su tag standard_price_by_quantity.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id y tags.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de ítem con tag de PxQ.

### Leer precios y versión

**Método:** `GET`  
**Ruta:** `/items/{item_id}/prices`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene la configuración y version actual antes de escribir PxQ B2C.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `display_version` (query, obligatorio): Enviar true para incluir version.
- `show-all-prices` (header, obligatorio): true en el ejemplo para incluir rangos.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, prices[], version.

**Errores documentados**

- Si el header x-version no se envía en escritura, la API devuelve error.

**Ejemplos**

- Ejemplo display_version=true y show-all-prices=true.

### Consultar precio ganador por cantidad

**Método:** `GET`  
**Ruta:** `/items/{item_id}/sale_price`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene precio unitario aplicable para una cantidad dada.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `quantity` (query, opcional): Cantidad consultada; el ejemplo usa 5.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Precio de venta y metadata; is_price_per_quantity=true cuando el ganador es PxQ B2C.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con quantity=5.

### Configurar PxQ porcentual B2C

**Método:** `POST`  
**Ruta:** `/items/{item_id}/prices/price-per-quantity`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Sustituye la lista de rangos de descuentos por cantidad del ítem.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `x-version` (header, obligatorio): Versión actual obtenida del GET prices.
- `price_per_quantity` (body, obligatorio): Lista completa; omitir id existente lo elimina y nodos sin id crean precio.
- `type` (body, obligatorio): discount_percentage.
- `percentage` (body, obligatorio): Porcentaje mayor que 0 y menor que 100.
- `conditions.min_purchase_unit` (body, obligatorio): Solo 2 o 4 para neumáticos.
- `conditions.eligible` (body, obligatorio): Debe ser true.

**Solicitud**

price_per_quantity[] de tipo discount_percentage con percentage y conditions.context_restrictions=[channel_marketplace], min_purchase_unit 2/4 y eligible=true.

**Respuesta**

Objeto de precios con version y price_per_quantity[] con id, percentage y conditions.

**Errores documentados**

- 400 bad.request: se permiten como máximo 2 entries para channel_marketplace.
- 400 bad.request: falta version (header x-version).
- 409 item.version: versión enviada no es la actual.
- 400: porcentaje fuera de rango o conditions.eligible distinto de true.

**Ejemplos**

- Ejemplo de dos rangos al 15% y 17,5%.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/precios-por-cantidad-b2c](https://developers.mercadolibre.com.co/es_co/precios-por-cantidad-b2c)  
**Captura:** 2026-10-08T22:52:31.595Z

---

## [Precios por cantidad porcentaje B2B](../markdown/pxq-porcentaje-b2b.md)

Actualización indicada por la fuente: 01/10/2026. Captura: 2026-10-08T22:52:32.943Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/pxq-porcentaje-b2b](https://developers.mercadolibre.com.co/es_co/pxq-porcentaje-b2b)

# Precios por cantidad porcentaje B2B

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 01/10/2026  
**Captura:** 2026-10-08T22:52:32.943Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/pxq-porcentaje-b2b](https://developers.mercadolibre.com.co/es_co/pxq-porcentaje-b2b)

## Resumen

Explica PxQ B2B porcentual: rangos de descuento progresivos calculados sobre el precio vigente, de modo que el porcentaje se conserva cuando cambia el precio base o hay promoción. Disponible en MLB, MLM, MLC y MLA para vendedores business habilitados; la fuente indica la futura discontinuación del modelo absoluto el 27/10/2026.

## Contenido y conceptos documentados

- Cada ítem admite una tabla de hasta cinco rangos; min_purchase_unit puede ir de 1 a 100 y el porcentaje debe aumentar al aumentar la cantidad mínima. Para la mayoría de dominios B2B se exige user_type_business en context_restrictions; Automotive Tires tiene condiciones específicas.
- Las recomendaciones previas calculan cantidades, precios sugeridos, descuento, margen y costo logístico; el request admite hasta cinco cantidades. La guía dice consultar recomendaciones antes de configurar PxQ.
- Para escribir, primero consultar prices con display_version=true y enviar la versión en X-Version. price_per_quantity[] usa discount_percentage, percentage y conditions con channel_marketplace, user_type_business, min_purchase_unit y eligible=true.
- Los cambios agregan, conservan o quitan nodos según ids; quitar todos requiere array vacío. remove-absolute-pxq=true sustituye nodos absolutos por los nuevos porcentuales. Automotive Tires en MLA tiene bloqueo indicado para PxQ B2B desde 21/07/2026.
- Los errores descritos cubren X-Version ausente/obsoleta, id inexistente, porcentaje inválido, eligible ausente, orden de descuentos, precio recomendado, cantidades incoherentes, máximo de rangos y dominio de neumáticos.

En los ejemplos de la fuente se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /items/{ITEM_ID}/prices/standard/quantity

La fuente menciona la ruta /items/{ITEM_ID}/prices/standard/quantity, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/items/{ITEM_ID}/prices/standard/quantity`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /orders

La fuente menciona la ruta /orders, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/orders`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Identificar ítem con tabla PxQ

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta tag standard_price_by_quantity.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id y tags.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de publicación con precio por cantidad.

### Consultar precios y versión

**Método:** `GET`  
**Ruta:** `/items/{item_id}/prices`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene nodos de precio, rangos B2B y version actual.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `display_version` (query, obligatorio): true para obtener version.
- `show-all-prices` (header, obligatorio): true en ejemplo para exponer todos los rangos.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, prices[], version y price_per_quantity[] con condiciones.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de lectura de versión y tabla de precios.

### Consultar precio unitario B2B

**Método:** `GET`  
**Ruta:** `/items/{item_id}/sale_price`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Resuelve el precio aplicado a contexto business y cantidad.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `context` (query, obligatorio): Debe incluir user_type_business; ejemplo agrega channel_marketplace.
- `quantity` (query, opcional): Cantidad consultada.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Precio ganador contextualizado para cantidad.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con contexto business y quantity.

### Consultar habilitación B2B

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Verifica tag business del usuario.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id y tags; la etiqueta business identifica usuarios habilitados.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de usuario con tag business.

### Configurar PxQ porcentual B2B

**Método:** `POST`  
**Ruta:** `/items/{item_id}/prices/price-per-quantity`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea, conserva o elimina la tabla porcentual por cantidad.

**Parámetros**

- `item_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `remove-absolute-pxq` (query, opcional): true reemplaza rangos absolutos existentes.
- `X-Version` (header, obligatorio): Versión actual del ítem, obligatoria.
- `price_per_quantity` (body, obligatorio): Lista de rangos; puede ser [] para eliminarlos todos.
- `type` (body, obligatorio): discount_percentage.
- `percentage` (body, obligatorio): Mayor que 0 y menor que 100; aumenta según cantidad.
- `conditions.context_restrictions` (body, obligatorio): channel_marketplace y user_type_business en los casos documentados.
- `conditions.min_purchase_unit` (body, obligatorio): Cantidad mínima; rango general documentado 1–100.
- `conditions.eligible` (body, obligatorio): Debe ser true.

**Solicitud**

price_per_quantity[] con type=discount_percentage, percentage y conditions (context_restrictions, min_purchase_unit, eligible=true).

**Respuesta**

prices[] y price_per_quantity[] con porcentajes, id, last_updated y conditions.

**Errores documentados**

- 400 bad.request: falta X-Version, id PxQ inexistente, porcentaje inválido o eligible distinto de true.
- 409 item.version: la versión no es la actual.
- Otros errores documentados: descuentos no crecientes, precio resultante sobre recomendado, cantidad incoherente, exceso de rangos y Automotive Tires.

**Ejemplos**

- Ejemplo de tabla porcentual con X-Version y de eliminación con array vacío.

### Solicitar recomendaciones de precios

**Método:** `POST`  
**Ruta:** `/prices-per-quantity/v1/recommendations`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Calcula rangos sugeridos en función de cantidad, precio estándar, moneda y ahorro logístico.

**Parámetros**

- `item_id` (body, obligatorio): ID de ítem con prefijo de sitio.
- `range_item_quantities` (body, opcional): Cantidades a calcular; máximo cinco.
- `price.standard_amount` (body, obligatorio): Precio estándar.
- `price.currency` (body, obligatorio): Moneda.

**Solicitud**

item_id, range_item_quantities opcional (hasta 5, cada una >=1) y price.standard_amount/currency.

**Respuesta**

site_id, item_id, seller_id, precio y recommendations[] con cantidad, importe, descuentos, profit y shipping.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con cantidades 2, 5 y 10.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/pxq-porcentaje-b2b](https://developers.mercadolibre.com.co/es_co/pxq-porcentaje-b2b)  
**Captura:** 2026-10-08T22:52:32.943Z

---

## [Preguntas y respuestas](../markdown/gestiona-preguntas-respuestas.md)

Actualización indicada por la fuente: 29/09/2023. Captura: 2026-10-08T22:52:34.051Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/gestiona-preguntas-respuestas](https://developers.mercadolibre.com.co/es_co/gestiona-preguntas-respuestas)

# Preguntas y respuestas

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/09/2023  
**Captura:** 2026-10-08T22:52:34.051Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestiona-preguntas-respuestas](https://developers.mercadolibre.com.co/es_co/gestiona-preguntas-respuestas)

## Resumen

Referencia para buscar preguntas recibidas por vendedor o por ítem, consultar una pregunta, formular o responder preguntas, medir el tiempo de respuesta y eliminar preguntas. La búsqueda usa api_version=4; la fuente limita a 2.000 caracteres el texto de pregunta/respuesta.

## Contenido y conceptos documentados

- La búsqueda por vendedor o ítem devuelve preguntas con estado, fecha, texto, respuesta y remitente. Estados descritos incluyen UNANSWERED, ANSWERED, BANNED y CLOSED_UNANSWERED; preguntas sin respuesta con más de siete meses se eliminan.
- La búsqueda soporta filtros y ordenamiento, entre ellos seller_id, item/item_id, from, status, offset, limit, sort_fields y sort_types. sort_fields acepta item_id, seller_id, from_id y date_created; sort_types ASC o DESC.
- Las preguntas y respuestas se limitan a 2.000 caracteres. La respuesta debe incluir question_id y text; formular pregunta usa text e item_id.
- El tiempo de respuesta ofrece períodos weekdays_working_hours, weekdays_extra_hours y weekend. La guía recomienda notificaciones para eventos de preguntas; el estado BANNED puede investigarse en moderations/infractions.

En los ejemplos de la fuente se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /my/questions/hidden

La fuente menciona la ruta /my/questions/hidden, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/my/questions/hidden`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /moderations/infractions

La fuente menciona la ruta /moderations/infractions, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/moderations/infractions`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /items

La fuente menciona la ruta /items, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/items`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Eliminar pregunta

**Método:** `DELETE`  
**Ruta:** `/questions/{question_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la pregunta usando su ID y token del usuario.

**Parámetros**

- `question_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de llamada DELETE.

### Consultar pregunta

**Método:** `GET`  
**Ruta:** `/questions/{question_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalle de una pregunta por su identificador.

**Parámetros**

- `question_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `api_version` (query, obligatorio): La guía muestra api_version=4.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, seller_id, buyer_id, item_id, status, text, fechas, answer y from.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente incluye respuesta de Vehículos con datos de contacto.

### Buscar preguntas

**Método:** `GET`  
**Ruta:** `/questions/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca preguntas por vendedor, publicación o usuario remitente.

**Parámetros**

- `seller_id` (query, opcional): Filtro de preguntas recibidas por vendedor.
- `item` (query, opcional): Filtro por publicación.
- `item_id` (query, opcional): Filtro por publicación en ejemplo de flujo de respuesta.
- `from` (query, opcional): ID de usuario remitente.
- `api_version` (query, obligatorio): La guía recomienda versión 4.
- `sort_fields` (query, opcional): Campos item_id,seller_id,from_id,date_created separados por coma.
- `sort_types` (query, opcional): ASC o DESC para los campos ordenados.
- `limit` (query, opcional): Tamaño de página.
- `offset` (query, opcional): Desplazamiento de resultados.

**Solicitud**

No documentado en la fuente.

**Respuesta**

total, limit, questions[] con date_created, item_id, seller_id, status, text, id, flags, answer y from; filtros y paginación.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos por seller_id, item, from y sort.

### Consultar tiempos de respuesta

**Método:** `GET`  
**Ruta:** `/users/{user_id}/questions/response_time`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve estadísticas de tiempo de respuesta por período.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

user_id y métricas de tiempo/porcentaje de respuesta por periodos de días laborales y fin de semana.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con periods de respuesta.

### Responder pregunta

**Método:** `POST`  
**Ruta:** `/answers`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Registra una respuesta para una pregunta recibida.

**Parámetros**

- `question_id` (body, obligatorio): ID de la pregunta.
- `text` (body, obligatorio): Respuesta, máximo 2.000 caracteres.

**Solicitud**

question_id y text.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de respuesta a una pregunta.

### Formular pregunta

**Método:** `POST`  
**Ruta:** `/questions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una pregunta sobre una publicación.

**Parámetros**

- `text` (body, obligatorio): Texto de la pregunta; máximo 2.000 caracteres.
- `item_id` (body, obligatorio): Publicación consultada.

**Solicitud**

text e item_id; UTF-8 recomendado.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo JSON con text e item_id.

### Referencia HTTP POST /my/questions/hidden

**Método:** `POST`  
**Ruta:** `/my/questions/hidden`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /my/questions/hidden. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestiona-preguntas-respuestas](https://developers.mercadolibre.com.co/es_co/gestiona-preguntas-respuestas)  
**Captura:** 2026-10-08T22:52:34.051Z

---

## [Primeros pasos](../markdown/primeros-pasos-es.md)

Actualización indicada por la fuente: 14/08/2024. Captura: 2026-10-08T22:52:34.957Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/primeros-pasos-es](https://developers.mercadolibre.com.co/es_co/primeros-pasos-es)

# Primeros pasos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 14/08/2024  
**Captura:** 2026-10-08T22:52:34.957Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/primeros-pasos-es](https://developers.mercadolibre.com.co/es_co/primeros-pasos-es)

## Resumen

Guía el flujo inicial para vincular publicaciones de moda con guías de talles: determinar dominio, consultar dominios habilitados, obtener la ficha técnica, buscar guías disponibles y reconocer qué tipo aplicar. Expone guías BRAND, STANDARD y SPECIFIC; en Uruguay, Colombia, Perú, Ecuador y Chile la fuente menciona solo SPECIFIC.

## Contenido y conceptos documentados

- El domain_id se obtiene con el predictor de categorías; los atributos marcados grid_template_required determinan los filtros requeridos para buscar una guía. La ficha técnica del dominio expone atributos grid_id y grid_row_id usados al asociar la guía al ítem.
- GET active_domains lista dominios habilitados por site. Si no hay configuración, la fuente muestra 404 config_not_found.
- POST technical_specs?section=grids consulta la estructura requerida para una guía específica usando atributos del dominio; la respuesta sirve como especificación del JSON de creación de guías personalizadas.
- POST catalog/charts/search requiere domain_id, site_id, seller_id y los atributos requeridos por la ficha; type permite SPECIFIC, STANDARD o BRAND. offset/limit paginan más de 100 registros.
- POST catalog/charts/domains/search devuelve dominios con experiencia de guía según site_id y type BRAND o STANDARD.

En los ejemplos de la fuente se usa `Authorization: Bearer $ACCESS_TOKEN`.

## Operaciones de API
## Operaciones de API

### Consultar dominios habilitados

**Método:** `GET`  
**Ruta:** `/catalog/charts/{site_id}/configurations/active_domains`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista dominios con experiencia de guía de talles activa para un sitio.

**Parámetros**

- `site_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

domains[] con domain_id.

**Errores documentados**

- 404 config_not_found: el sitio no tiene dominios activados.

**Ejemplos**

- Ejemplo para MLA.

### Consultar ficha técnica del dominio

**Método:** `GET`  
**Ruta:** `/domains/{domain_id}/technical_specs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los atributos y especificación de un dominio.

**Parámetros**

- `domain_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ficha técnica del dominio; se identifican value_type grid_id/grid_row_id y tag grid_template_required.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo MLA-SNEAKERS.

### Buscar dominios por tipo de guía

**Método:** `POST`  
**Ruta:** `/catalog/charts/domains/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve dominios configurados para una guía BRAND o STANDARD.

**Parámetros**

- `site_id` (body, obligatorio): Sitio.
- `type` (body, obligatorio): BRAND o STANDARD.

**Solicitud**

site_id y type.

**Respuesta**

domains[] con domain_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos de guías por marca y estándar.

### Buscar guías de talles

**Método:** `POST`  
**Ruta:** `/catalog/charts/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca guías sugeridas para publicación por dominio, sitio, seller, atributos y tipo.

**Parámetros**

- `offset` (query, opcional): Desplazamiento de resultados.
- `limit` (query, opcional): Límite; la guía permite paginar más de cien.
- `domain_id` (body, obligatorio): Dominio.
- `site_id` (body, obligatorio): Sitio.
- `seller_id` (body, obligatorio): Vendedor.
- `attributes` (body, obligatorio): Atributos definidos por grid_template_required.
- `type` (body, opcional): Tipo de guía BRAND, STANDARD o SPECIFIC.

**Solicitud**

domain_id, site_id, seller_id y attributes[]; type opcional: SPECIFIC, STANDARD o BRAND.

**Respuesta**

paging y charts[] con id, names, domain_id, type y atributos/filas.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo BRAND Adidas para mujer en SNEAKERS.

### Consultar esquema de guía de talles

**Método:** `POST`  
**Ruta:** `/domains/{domain_id}/technical_specs`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la sección grids enviando los atributos requeridos para obtener la ficha de guía.

**Parámetros**

- `domain_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.
- `section` (query, obligatorio): Debe ser grids.
- `attributes` (body, obligatorio): Atributos necesarios para resolver la guía, por ejemplo BRAND y GENDER.

**Solicitud**

attributes[] con los atributos de ficha técnica marcados grid_template_required.

**Respuesta**

Estructura input/groups/components para la guía, que define la especificación de creación.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con dominio MLA-SNEAKERS, marca Nike y género mujer.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/primeros-pasos-es](https://developers.mercadolibre.com.co/es_co/primeros-pasos-es)  
**Captura:** 2026-10-08T22:52:34.957Z

---

## [Programa de Despegue y Beneficio de Reputación](../markdown/recuperacion-reputacion.md)

Actualización indicada por la fuente: 04/02/2025. Captura: 2026-10-08T22:52:35.924Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/recuperacion-reputacion](https://developers.mercadolibre.com.co/es_co/recuperacion-reputacion)

# Programa de Despegue y Beneficio de Reputación

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 04/02/2025  
**Captura:** 2026-10-08T22:52:35.924Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/recuperacion-reputacion](https://developers.mercadolibre.com.co/es_co/recuperacion-reputacion)

## Resumen

Documenta consulta, activación, cancelación y descarga de documentos de los programas NEWBIE_GRNTEE y RECOVERY_GRNTEE. Están dirigidos a vendedores sin reputación o con nivel rojo, naranja o amarillo en MLA, MLB, MLM, MLC y MCO; los niveles verdes están excluidos. El programa congela temporalmente el nivel de reputación y opera con una garantía.

## Contenido y conceptos documentados

- GET seller_recovery/status expone disponibilidad/estado, límites de problemas y días, importe de garantía y Ads, fechas de protección y ventas/reclamos/cancelaciones/demoras. El límite de rate documentado es 100 RPM por user_id.
- Para activar, el vendedor debe tener saldo suficiente en Mercado Pago para la garantía; al hacer opt-in comienza el periodo de protección. La cancelación usa cancellation_reason con valores business_not_ready, program_not_useful, need_money, goal_achieved y without_reason.
- La descarga legal es obligatoria para México y Colombia. type=preview se permite cuando status=AVAILABLE y garantía OFF; type=complete requiere protección ACTIVE o FINISHED_BY_*. La respuesta documentada contiene PDF codificado en base64.
- La página recomienda usar /communications/notices para informar al vendedor de invitaciones; no detalla aquí método HTTP ni URL completa para esa referencia.

En los ejemplos de la fuente se usa `Authorization: Bearer Token`.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /communications/notices

La fuente menciona la ruta /communications/notices, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/communications/notices`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Descargar documento legal

**Método:** `GET`  
**Ruta:** `/users/reputation/seller_recovery/legal-document`  
**Autenticación:** Authorization: Bearer Token

Descarga versión preliminar o completa de la domiciliación legal.

**Parámetros**

- `type` (query, obligatorio): PREVIEW o COMPLETE; condiciones dependen de status y garantía.

**Solicitud**

No documentado en la fuente.

**Respuesta**

document codificado en base64 que representa un PDF.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra ejemplo de decodificación Base64.

### Consultar programa y garantía

**Método:** `GET`  
**Ruta:** `/users/reputation/seller_recovery/status`  
**Autenticación:** Authorization: Bearer Token

Obtiene disponibilidad, estado, límites, garantía, protección y beneficios asociados.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

seller_id, current_level, status, type, site_id, protection_limits, guarantee_limits, guarantee_detail, protection_detail y sales_detail.

**Errores documentados**

- Límite de 100 RPM por vendedor (user_id).

**Ejemplos**

- Respuesta con AVAILABLE, límites y guarantee_status OFF.

### Consultar reputación del vendedor

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer Token

Lee seller_reputation para verificar elegibilidad preliminar.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

seller_reputation.level_id, power_seller_status y transactions.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente excluye niveles verdes 4_light_green y 5_green.

### Activar programa

**Método:** `POST`  
**Ruta:** `/users/reputation/seller_recovery/activate`  
**Autenticación:** Authorization: Bearer Token

Realiza opt-in para iniciar periodo de protección.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

message=ok.

**Errores documentados**

- Error si el vendedor no tiene disponible el dinero de garantía en Mercado Pago.

**Ejemplos**

- Ejemplo de activación.

### Cancelar programa

**Método:** `PUT`  
**Ruta:** `/users/reputation/seller_recovery/cancel_guarantee`  
**Autenticación:** Authorization: Bearer Token

Solicita cancelación del programa con motivo.

**Parámetros**

- `cancellation_reason` (body, obligatorio): Motivo obligatorio para Programa de Despegue; la fuente dice que no se requiere para Recovery Color.

**Solicitud**

cancellation_reason: business_not_ready, program_not_useful, need_money, goal_achieved o without_reason.

**Respuesta**

message=ok.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo cancellation_reason=goal_achieved.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/recuperacion-reputacion](https://developers.mercadolibre.com.co/es_co/recuperacion-reputacion)  
**Captura:** 2026-10-08T22:52:35.924Z

---

## [Provisiones](../markdown/provisiones.md)

Actualización indicada por la fuente: 08/06/2026. Captura: 2026-10-08T22:52:37.232Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/provisiones](https://developers.mercadolibre.com.co/es_co/provisiones)

# Provisiones

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 08/06/2026  
**Captura:** 2026-10-08T22:52:37.232Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/provisiones](https://developers.mercadolibre.com.co/es_co/provisiones)

## Resumen

Explica cómo obtener el detalle de cargos y notas fiscales de un período, grupo de facturación y unidad de negocio: Mercado Libre, Mercado Pago, Flex, Full e Insurtech. La API admite facturas (`BILL`) y notas de crédito (`CREDIT_NOTE`), además de búsquedas de cargos asociados a órdenes o paquetes.

## Contenido y conceptos documentados

### Parámetros y uso

- Las rutas usan `Authorization: Bearer $ACCESS_TOKEN`. Las llamadas de detalle por período reciben una `KEY` mensual y permiten `group` y `document_type`.
- La página describe paginación de detalles con `limit` (por defecto 150, máximo 1000) y `from_id` (por defecto 0; la siguiente página usa `last_id`). Para ordenamiento menciona `sort_by` (`ID` o `DATE`) y `order_by` (`ASC` o `DESC`). El endpoint por órdenes limita `order_ids` a 60 por consulta y también permite filtrar por `pack_id`.
- Las respuestas documentadas contienen identificadores, cargos, ventas, pagos, envíos, artículos, descuentos, movimientos e información del documento; algunos datos cambian según el grupo/negocio. Para relacionar cargos con la operación, la fuente remite a recursos de órdenes, packs, envíos, descuentos, precio de venta y ofertas promocionales.
- Los cuerpos de solicitud y códigos de error específicos por ruta: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Detalle de facturación por orden o pack

**Método:** `GET`  
**Ruta:** `/billing/integration/group/ML/order/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Filtra detalles de facturación de Mercado Libre por órdenes o paquete.

**Parámetros**

- `order_ids` (query, opcional): Uno o varios IDs; máximo 60 por consulta.
- `pack_id` (query, opcional)
- `sort_by` (query, opcional): ID o DATE.
- `order_by` (query, opcional): ASC o DESC.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de consulta con order_ids.

### Detalle de facturación Mercado Libre

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/$KEY/group/ML/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta cargos y notas fiscales de Mercado Libre para la clave del período.

**Parámetros**

- `KEY` (path, obligatorio): Clave del período mensual.
- `document_type` (query): BILL o CREDIT_NOTE.
- `limit` (query, opcional): Por defecto 150; máximo 1000.
- `from_id` (query, opcional): Por defecto 0; continuar con last_id.
- `sort_by` (query, opcional): ID o DATE.
- `order_by` (query, opcional): ASC o DESC.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- charge_info
- legal_document_number
- legal_document_status
- creation_date_time
- detail_id
- transaction_detail
- detail_amount
- detail_type
- sales_info
- shipping_info
- items_info
- document_info
- marketplace_info

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra paginación por from_id y last_id.

### Detalle de facturación Flex

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/$KEY/group/ML/flex/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta cobros, bonificaciones y datos de envíos Flex por período.

**Parámetros**

- `KEY` (path, obligatorio): Clave del período mensual.
- `document_type` (query): BILL o CREDIT_NOTE.
- `limit` (query, opcional): Por defecto 150; máximo 1000.
- `from_id` (query, opcional): Por defecto 0; continuar con last_id.
- `sort_by` (query, opcional): ID o DATE.
- `order_by` (query, opcional): ASC o DESC.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- shipping_info
- shipping_id
- pack_id
- receiver_shipping_cost
- item_id
- movement_id
- operation_info
- detail_amount

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Detalle de facturación Full

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/$KEY/group/ML/full/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta cobros y bonificaciones por recolección y almacenamiento de productos.

**Parámetros**

- `KEY` (path, obligatorio): Clave del período mensual.
- `document_type` (query): BILL o CREDIT_NOTE.
- `limit` (query, opcional): Por defecto 150; máximo 1000.
- `from_id` (query, opcional): Por defecto 0; continuar con last_id.
- `sort_by` (query, opcional): ID o DATE.
- `order_by` (query, opcional): ASC o DESC.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- fulfillment_info
- inbound_id
- volume_type
- volume_unit
- amount_per_volume_unit
- volume
- volume_total
- items_info

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Detalle de facturación Insurtech

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/$KEY/group/ML/insurtech/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta cobros/bonificaciones de garantías aplicadas sobre productos.

**Parámetros**

- `KEY` (path, obligatorio): Clave del período mensual.
- `document_type` (query): BILL o CREDIT_NOTE.
- `limit` (query, opcional): Por defecto 150; máximo 1000.
- `from_id` (query, opcional): Por defecto 0; continuar con last_id.
- `sort_by` (query, opcional): ID o DATE.
- `order_by` (query, opcional): ASC o DESC.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- warranty_info
- warranty_id
- certificate_id
- warranty_product
- order_items

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Detalle de facturación Mercado Pago

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/$KEY/group/MP/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta movimientos, medios de pago y cobros de Mercado Pago por período.

**Parámetros**

- `KEY` (path, obligatorio): Clave del período mensual.
- `document_type` (query): BILL o CREDIT_NOTE.
- `limit` (query, opcional): Por defecto 150; máximo 1000.
- `from_id` (query, opcional): Por defecto 0; continuar con last_id.
- `sort_by` (query, opcional): ID o DATE.
- `order_by` (query, opcional): ASC o DESC.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- payment_info
- payment_id
- date_approved
- money_release_date
- payer_id
- payment_method_id
- tax_details
- transaction_amount
- document_info

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Precio de venta del ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}/sale_price`  
**Autenticación:** No documentado en la fuente.

Referencia para identificar el precio de venta del ítem.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Datos del pedido

**Método:** `GET`  
**Ruta:** `/orders`  
**Autenticación:** No documentado en la fuente.

Referencia para obtener datos de la orden vinculada al detalle de facturación.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Descuentos de la orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}/discounts`  
**Autenticación:** No documentado en la fuente.

Referencia para consultar descuentos y campañas aplicados a la orden.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Orders de un pack

**Método:** `GET`  
**Ruta:** `/packs`  
**Autenticación:** No documentado en la fuente.

Referencia para identificar las órdenes dentro de un pack.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Estado de oferta promocional

**Método:** `GET`  
**Ruta:** `/seller-promotions/offers/{offer_id}`  
**Autenticación:** No documentado en la fuente.

Referencia para consultar cambios y estado de una oferta.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Costo del envío

**Método:** `GET`  
**Ruta:** `/shipments`  
**Autenticación:** No documentado en la fuente.

Referencia para consultar el costo de envío.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/provisiones](https://developers.mercadolibre.com.co/es_co/provisiones)  
**Captura:** 2026-10-08T22:52:37.232Z

---

## [Publicaciones requeridas](../markdown/publicaciones-requeridas-en-catalogo.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:52:38.143Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/publicaciones-requeridas-en-catalogo](https://developers.mercadolibre.com.co/es_co/publicaciones-requeridas-en-catalogo)

# Publicaciones requeridas

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:52:38.143Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/publicaciones-requeridas-en-catalogo](https://developers.mercadolibre.com.co/es_co/publicaciones-requeridas-en-catalogo)

## Resumen

Define cuándo una publicación debe migrar o publicarse en catálogo. La elegibilidad requiere el tag `catalog_listing_eligible` y un producto cuyo `listing_strategy` sea `catalog_required`; los dominios `catalog_only` restringen la publicación tradicional.

## Contenido y conceptos documentados

### Elegibilidad y flujo

- Consulta los dumps `catalog_required` y `catalog_only` del sitio antes de publicar. La fuente advierte que ignorarlos puede causar moderaciones `opt_obey` o `catalog_only_restricted`.
- La búsqueda de productos permite filtrar publicaciones activas por sitio, estrategia y texto; para una búsqueda sin caché el ejemplo agrega `skip_cache=true`.
- Los vendedores pueden listar ítems con `catalog_forewarning`, consultar la fecha asociada a una publicación y revisar infracciones de moderación por usuario.
- Las llamadas de API usan Bearer salvo las descargas de dumps, cuyos ejemplos no muestran autorización. Cuerpos, errores y algunos esquemas completos: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Dominios catalog_only

**Método:** `GET`  
**Ruta:** `/catalog/dumps/domains/$SITE_ID/catalog_only`  
**Autenticación:** No documentado en la fuente.

Descarga dominios donde solo se admite publicar en catálogo.

**Parámetros**

- `SITE_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- generation_date
- domains[].id
- domains[].date

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de dump para MLB.

### Dominios catalog_required

**Método:** `GET`  
**Ruta:** `/catalog/dumps/domains/$SITE_ID/catalog_required`  
**Autenticación:** No documentado en la fuente.

Descarga dominios con venta obligatoria en catálogo para el sitio.

**Parámetros**

- `SITE_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- generation_date
- domains[].id
- domains[].date

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de dump para MLB.

### Fecha de forewarning

**Método:** `GET`  
**Ruta:** `/items/$ITEM_ID/catalog_forewarning/date`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la fecha asociada a la advertencia de catálogo del ítem.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- date

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Infracciones del usuario

**Método:** `GET`  
**Ruta:** `/moderations/infractions/$USER_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta infracciones de moderación asociadas al usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- infractions
- date_created
- user_id
- related_item_id
- element_id
- element_type
- reason
- remedy

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Buscar productos de catálogo requeridos

**Método:** `GET`  
**Ruta:** `/products/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca productos activos que corresponden a una estrategia de publicación de catálogo.

**Parámetros**

- `status` (query, opcional): Ejemplo: active.
- `site_id` (query, obligatorio)
- `listing_strategy` (query, obligatorio): catalog_required.
- `q` (query, opcional)
- `skip_cache` (query, opcional)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- paging
- results[].id
- results[].domain_id
- results[].status
- results[].listing_strategy

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra una consulta con skip_cache=true.

### Ítems con aviso de catálogo

**Método:** `GET`  
**Ruta:** `/users/$USER_ID/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca ítems del vendedor con tag de advertencia de catálogo.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `tags` (query, obligatorio): catalog_forewarning.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- paging
- results

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/publicaciones-requeridas-en-catalogo](https://developers.mercadolibre.com.co/es_co/publicaciones-requeridas-en-catalogo)  
**Captura:** 2026-10-08T22:52:38.143Z

---

## [Publicar en catálogo](../markdown/publicacion-en-catalogo.md)

Actualización indicada por la fuente: 02/01/2026. Captura: 2026-10-08T22:52:39.215Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/publicacion-en-catalogo](https://developers.mercadolibre.com.co/es_co/publicacion-en-catalogo)

# Publicar en catálogo

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 02/01/2026  
**Captura:** 2026-10-08T22:52:39.215Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/publicacion-en-catalogo](https://developers.mercadolibre.com.co/es_co/publicacion-en-catalogo)

## Resumen

Documenta tres flujos: creación directa de una publicación de catálogo, opt-in desde una publicación tradicional y opt-in automático. También explica cómo comprobar o recuperar la sincronización entre el ítem tradicional y el de catálogo.

## Contenido y conceptos documentados

### Flujos y restricciones

- Para creación directa, el `catalog_product_id` debe corresponder a un producto activo (la excepción indicada para productos inactivos se limita a Autopartes) y se envía `catalog_listing: true`. El vendedor debe verificar que la ficha del producto coincida con lo que publicará.
- El opt-in tradicional asocia el `item_id` al `catalog_product_id`; para publicaciones con variaciones puede indicarse también `variation_id`.
- La consulta y corrección de sincronización de Buy Box usan el encabezado `x-public: true`. La solicitud de sincronización envía `item_id`; se documentan HTTP 200 para éxito y 422/500 para errores.
- El tag `catalog_boost` identifica publicaciones optineadas automáticamente y puede buscarse por vendedor. No todos los dominios admiten la misma modalidad; la guía señala limitaciones para IDs inactivos y el impacto de asociar una ficha incorrecta. Parámetros y respuestas no descritos: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Consultar ejemplo de ítem optineado

**Método:** `GET`  
**Ruta:** `/items/MLM1881484643`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Ejemplo de lectura de un ítem de catálogo optineado automáticamente.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- catalog_product_id
- catalog_listing
- tags
- item_relations

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura utiliza el ID de ejemplo MLM1881484643.

### Consultar sincronización de catálogo

**Método:** `GET`  
**Ruta:** `/public/buybox/sync/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Verifica la sincronización entre el ítem tradicional y el ítem de catálogo.

**Parámetros**

- `ITEM_ID` (path, obligatorio)
- `x-public` (header, obligatorio): El ejemplo usa true.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La llamada de ejemplo incluye x-public: true.

### Buscar ítems catalog_boost

**Método:** `GET`  
**Ruta:** `/users/$SELLER_ID/items/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca publicaciones activas del vendedor optineadas automáticamente.

**Parámetros**

- `SELLER_ID` (path, obligatorio)
- `status` (query, obligatorio): active.
- `tags` (query, obligatorio): catalog_boost.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- paging
- results

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Crear ítem directamente en catálogo

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una publicación directa asociada a un producto de catálogo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "site_id",
    "title",
    "category_id",
    "price",
    "currency_id",
    "available_quantity",
    "buying_mode",
    "listing_type_id",
    "catalog_product_id",
    "catalog_listing=true",
    "attributes",
    "pictures"
  ]
}
```

**Respuesta**

- id
- site_id
- title
- seller_id
- category_id
- price
- currency_id
- catalog_product_id
- catalog_listing
- status
- item_relations

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La ficha exige confirmar catalog_product_id y enviar catalog_listing=true.

### Opt-in de publicación tradicional

**Método:** `POST`  
**Ruta:** `/items/catalog_listings`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Asocia un ítem tradicional con un producto del catálogo.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "item_id",
    "catalog_product_id",
    "variation_id (si corresponde)"
  ]
}
```

**Respuesta**

- item_id
- variation_id
- catalog_product_id
- status

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra ejemplos para publicaciones con y sin variaciones.

### Sincronizar ítem de catálogo

**Método:** `POST`  
**Ruta:** `/public/buybox/sync`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Solicita corregir sincronización enviando el identificador de ítem.

**Parámetros**

- `x-public` (header, obligatorio): El ejemplo usa true.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "item_id"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "meaning": "La página enumera HTTP 422 como error, sin detallar su significado.",   "code": 422 } ```
- ```json {   "meaning": "La página enumera HTTP 500 como error, sin detallar su significado.",   "code": 500 } ```

**Ejemplos**

- La fuente documenta 200 para éxito y 422/500 en error.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/publicacion-en-catalogo](https://developers.mercadolibre.com.co/es_co/publicacion-en-catalogo)  
**Captura:** 2026-10-08T22:52:39.215Z

---

## [Publicar productos](../markdown/publica-productos.md)

Actualización indicada por la fuente: 09/01/2026. Captura: 2026-10-08T22:52:40.362Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/publica-productos](https://developers.mercadolibre.com.co/es_co/publica-productos)

# Publicar productos

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 09/01/2026  
**Captura:** 2026-10-08T22:52:40.362Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/publica-productos](https://developers.mercadolibre.com.co/es_co/publica-productos)

## Resumen

Guía general para consultar y crear publicaciones, con ejemplos de atributos, condiciones, términos de venta, variaciones, envío y pago inmediato. Recomienda a los nuevos flujos considerar el modelo User Products.

## Contenido y conceptos documentados

### Reglas de publicación

- Para consultar una publicación se usa el recurso de ítems; las fichas de categoría permiten conocer atributos y términos de venta antes de crearla.
- La creación se hace con `POST /items`. La fuente incluye campos como título, categoría, precio, moneda, cantidad, modo de compra, tipo de publicación, imágenes, atributos, términos de venta, envío y variaciones, según el ejemplo.
- `exclusive_channel` ya no se admite: debe usarse `channels`. Para nuevas implementaciones, la condición se especifica como `item_condition` en `attributes`; `condition` sigue por compatibilidad. La consulta de valores por categoría se vincula a la ficha técnica.
- Se puede publicar con cantidad cero para Fulfillment en Argentina, México y Brasil. Las categorías con pago inmediato se consultan mediante el recurso de categorías; la publicación usa el tag `immediate_payment` cuando corresponda.
- La fuente también indica que el título puede cambiarse vía PUT mientras `sold_quantity=0`. Los cuerpos completos y códigos de error: No documentado en la fuente salvo los ejemplos y la tabla de códigos enlazada.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /domains/{DOMAIN_ID}/technical_specs

La fuente menciona la ruta /domains/{DOMAIN_ID}/technical_specs, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/domains/{DOMAIN_ID}/technical_specs`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /users

La fuente menciona la ruta /users, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/users`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar atributos de categoría

**Método:** `GET`  
**Ruta:** `/categories/$CATEGORY_ID/attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene atributos y metadatos que aplican al publicar en una categoría.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- name
- value_type
- values
- attribute_group_id
- attribute_group_name
- required
- conditional_required

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar términos de venta

**Método:** `GET`  
**Ruta:** `/categories/$CATEGORY_ID/sale_terms`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene términos que pueden enviarse en una publicación de la categoría.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- name
- value_id
- value_name
- value_type

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página describe términos de garantía.

### Consultar publicación

**Método:** `GET`  
**Ruta:** `/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene la ficha de una publicación.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- site_id
- title
- category_id
- seller_id
- price
- currency_id
- available_quantity
- sold_quantity
- listing_type_id
- attributes
- variations
- sale_terms
- shipping
- channels

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar pago inmediato de categoría

**Método:** `GET`  
**Ruta:** `/sites/categories/$CATEGORY_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta si una categoría exige Mercado Pago como única opción.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- immediate_payment
- item_conditions

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Crear publicación

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea un ítem con los datos comerciales, atributos y opciones de logística permitidos.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "title",
    "category_id",
    "price",
    "currency_id",
    "available_quantity",
    "buying_mode",
    "listing_type_id",
    "pictures",
    "attributes",
    "sale_terms",
    "shipping",
    "tags",
    "variations",
    "channels",
    "item_condition"
  ]
}
```

**Respuesta**

- id
- site_id
- title
- seller_id
- category_id
- price
- currency_id
- available_quantity
- status
- permalink

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Incluye ejemplos para Argentina y Brasil, incluido tag immediate_payment.

### Actualizar publicación

**Método:** `PUT`  
**Ruta:** `/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica el título en el flujo descrito cuando sold_quantity es cero.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "title (solo cuando sold_quantity=0, según la página)"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Referencia HTTP POST /items/{ITEM_ID}

**Método:** `POST`  
**Ruta:** `/items/{ITEM_ID}`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud POST a /items/{ITEM_ID}. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/publica-productos](https://developers.mercadolibre.com.co/es_co/publica-productos)  
**Captura:** 2026-10-08T22:52:40.362Z

---

## [Qué es catálogo](../markdown/que-es-catalogo.md)

Actualización indicada por la fuente: 29/12/2025. Captura: 2026-10-08T22:52:41.373Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/que-es-catalogo](https://developers.mercadolibre.com.co/es_co/que-es-catalogo)

# Qué es catálogo

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:52:41.373Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/que-es-catalogo](https://developers.mercadolibre.com.co/es_co/que-es-catalogo)

## Resumen

Describe la publicación de catálogo como una oferta que reutiliza contenido y ficha técnica provistos por Mercado Libre. El vendedor puede crear una publicación desde una publicación existente o iniciar una nueva, compitiendo por exposición en la Página de Producto. La fuente enumera disponibilidad en Argentina, México, Brasil, Colombia, Chile, Uruguay, Perú y Ecuador.

## Contenido y conceptos documentados

### Conceptos

- El catálogo centraliza título, fotos, descripción y datos técnicos del producto; la oferta del vendedor conserva sus condiciones comerciales.
- La guía deriva a los flujos de catálogo para elegibilidad, opt-in y creación directa. La página conceptual no detalla parámetros, autenticación ni esquemas de respuesta: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Modelo de catálogo

Concepto de publicación de catálogo con contenido y ficha técnica provistos por Mercado Libre; permite oferta directa o asociada a una publicación existente en ocho países.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/que-es-catalogo](https://developers.mercadolibre.com.co/es_co/que-es-catalogo)  
**Captura:** 2026-10-08T22:52:41.373Z

---

## [Qué es mensajería](../markdown/que-es-mensajeria.md)

Actualización indicada por la fuente: 20/02/2024. Captura: 2026-10-08T22:52:42.485Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/que-es-mensajeria](https://developers.mercadolibre.com.co/es_co/que-es-mensajeria)

# Qué es mensajería

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 20/02/2024  
**Captura:** 2026-10-08T22:52:42.485Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/que-es-mensajeria](https://developers.mercadolibre.com.co/es_co/que-es-mensajeria)

## Resumen

Presenta la mensajería posventa como un canal privado para que vendedor y comprador se comuniquen después de una venta. El vendedor inicia el contacto seleccionando un motivo; después puede crear, enviar y consultar mensajes asociados a paquetes que contienen una o varias órdenes.

## Contenido y conceptos documentados

### Flujo y restricciones

- La página distingue el inicio de conversación por parte del vendedor, que requiere elegir un motivo, de la comunicación iniciada por el comprador, que puede recibir respuesta normal sin seleccionar motivo.
- El objetivo descrito es facilitar la gestión posventa y reducir comunicaciones automáticas. La página conceptual no especifica rutas, autenticación, parámetros ni formato de mensajes: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Mensajería posventa

Canal privado posterior a la venta: el vendedor inicia contacto seleccionando motivo y puede crear/enviar/consultar mensajes asociados a paquetes; el comprador puede iniciar conversación y recibir respuesta sin selección de motivo.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/que-es-mensajeria](https://developers.mercadolibre.com.co/es_co/que-es-mensajeria)  
**Captura:** 2026-10-08T22:52:42.485Z

---

## [Referencias de dominios, productos y atributos para Autopartes](../markdown/referencias-de-dominios-productos-y-atributos-para-autopartes.md)

Actualización indicada por la fuente: 15/06/2026. Captura: 2026-10-08T22:52:43.356Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/referencias-de-dominios-productos-y-atributos-para-autopartes](https://developers.mercadolibre.com.co/es_co/referencias-de-dominios-productos-y-atributos-para-autopartes)

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

---

## [Referencias de precios](../markdown/referencias-de-precios.md)

Actualización indicada por la fuente: 17/12/2025. Captura: 2026-10-08T22:52:44.247Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/referencias-de-precios](https://developers.mercadolibre.com.co/es_co/referencias-de-precios)

# Referencias de precios

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 17/12/2025  
**Captura:** 2026-10-08T22:52:44.247Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/referencias-de-precios](https://developers.mercadolibre.com.co/es_co/referencias-de-precios)

## Resumen

Explica las referencias de precios que Mercado Libre calcula para orientar el precio competitivo de un producto. Permite obtener los ítems del vendedor que cuentan con referencia y consultar el detalle asociado a un ítem.

## Contenido y conceptos documentados

### Consulta y restricciones

- La consulta por vendedor requiere que el usuario exista; el detalle requiere que el ítem exista. Ambas llamadas muestran autenticación Bearer.
- La lista devuelve `total` e `items`. El detalle incluye estado, moneda, precio actual/sugerido, niveles de precio, costos, diferencia porcentual, comparables y datos de promociones, cuando estén disponibles.
- La página documenta respuestas de error 401 para token inválido o ítem ajeno al vendedor y 404 para recurso no encontrado. El cuerpo de solicitud: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Detalle de referencia por ítem

**Método:** `GET`  
**Ruta:** `/suggestions/items/$ITEM_ID/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene precios sugeridos, comparables y datos de costos/promociones para el ítem.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- item_id
- status
- currency_id
- ratio
- current_price
- suggested_price
- lowest_price
- internal_price
- costs
- selling_fees
- shipping_fees
- applicable_suggestion
- percent_difference
- metadata
- graph
- compared_values
- promotion_detail

**Errores documentados**

- ```json {   "code": 401,   "meaning": "Caller no es propietario del ítem o access token inválido." } ```
- ```json {   "code": 404,   "meaning": "Referencia/ítem no encontrado." } ```

**Ejemplos**

- Precondición: el ítem debe existir.

### Ítems del usuario con referencia de precio

**Método:** `GET`  
**Ruta:** `/suggestions/user/$USER_ID/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista los ítems del vendedor que tienen referencias de precio.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- total
- items[]

**Errores documentados**

- ```json {   "code": 401,   "meaning": "El token no es del propietario del ítem o es inválido." } ```
- ```json {   "code": 404,   "meaning": "Ítem/recurso no encontrado." } ```

**Ejemplos**

- Precondición: el usuario debe existir.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/referencias-de-precios](https://developers.mercadolibre.com.co/es_co/referencias-de-precios)  
**Captura:** 2026-10-08T22:52:44.247Z

---

## [Reportes de Facturación](../markdown/reportes-de-facturacion.md)

Actualización indicada por la fuente: 03/03/2026. Captura: 2026-10-08T22:52:45.129Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/reportes-de-facturacion](https://developers.mercadolibre.com.co/es_co/reportes-de-facturacion)

# Reportes de Facturación

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 03/03/2026  
**Captura:** 2026-10-08T22:52:45.129Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/reportes-de-facturacion](https://developers.mercadolibre.com.co/es_co/reportes-de-facturacion)

## Resumen

Documenta la consulta de períodos mensuales, documentos de facturación y resumen/detalle de cargos para Mercado Libre y Mercado Pago. Los informes permiten consultar facturas y notas de crédito y paginar sus resultados.

## Contenido y conceptos documentados

### Parámetros y uso

- Las llamadas usan Bearer y el parámetro `group` (`ML` o `MP`); la página indica que si se omite se puede obtener información de ambos grupos. `document_type` acepta `BILL` y `CREDIT_NOTE`.
- Los períodos admiten `offset` y `limit`; la consulta de períodos devuelve seis por defecto y permite hasta doce. Para documentos, `limit` tiene máximo 1000; la página recomienda paginar y no repetir consultas innecesarias.
- La respuesta de documentos agrega estado/IDs de documentos, importes, períodos, monedas, cantidades y archivos. El resumen puede incluir cargos, pagos cobrados, descuentos, créditos y deuda.
- Se documentan HTTP 206 (respuesta parcial/incompleta) y 429 (bloqueo preventivo por exceso de solicitudes desde IP). La página recomienda usar paginación y evitar llamadas repetitivas.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /billing/monthly/periods

La fuente menciona la ruta /billing/monthly/periods, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/billing/monthly/periods`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Períodos mensuales de facturación

**Método:** `GET`  
**Ruta:** `/billing/integration/monthly/periods`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista períodos recientes por grupo y tipo de documento.

**Parámetros**

- `group` (query): ML o MP; la página indica ambos grupos si se omite.
- `document_type` (query, obligatorio): BILL o CREDIT_NOTE.
- `offset` (query, opcional)
- `limit` (query, opcional): La página indica períodos por defecto y máximo de 12.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- offset
- limit
- total
- results[].amount
- results[].period.date_from
- results[].period.date_to
- results[].period.key
- results[].period.period_status

**Errores documentados**

- ```json {   "code": 206,   "meaning": "Respuesta parcial/incompleta." } ```
- ```json {   "code": 429,   "meaning": "Bloqueo preventivo por límite de solicitudes desde IP." } ```

**Ejemplos**

- El ejemplo solicita group=MP, document_type=BILL, offset y limit.

### Documentos de un período

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/$KEY/documents`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista facturas o notas de crédito del período indicado.

**Parámetros**

- `KEY` (path, obligatorio)
- `group` (query): ML o MP.
- `document_type` (query, obligatorio): BILL o CREDIT_NOTE.
- `offset` (query, opcional)
- `limit` (query, opcional): Máximo 1000.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- offset
- limit
- total
- results[].id
- results[].document_type
- results[].document_status
- results[].associated_document_id
- results[].currency_id
- results[].files

**Errores documentados**

- ```json {   "code": 206,   "meaning": "Respuesta parcial/incompleta." } ```
- ```json {   "code": 429,   "meaning": "Bloqueo preventivo por límite de solicitudes desde IP." } ```

**Ejemplos**

- La página incluye ejemplo de documentos de un período mensual.

### Resumen y detalle de facturación

**Método:** `GET`  
**Ruta:** `/billing/integration/periods/key/$KEY/summary/details`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera cargos, pagos, créditos, cobros y deuda del período.

**Parámetros**

- `KEY` (path, obligatorio)
- `group` (query): ML o MP.
- `document_type` (query): BILL o CREDIT_NOTE, cuando aplique.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- user
- nickname
- bill_includes
- total_amount
- total_perceptions
- bonuses
- charges
- payment_collected
- operation_discount
- total_payment
- total_credit_note
- total_collected
- total_debt

**Errores documentados**

- ```json {   "code": 206,   "meaning": "Respuesta parcial/incompleta." } ```
- ```json {   "code": 429,   "meaning": "Bloqueo preventivo por límite de solicitudes desde IP." } ```

**Ejemplos**

- La fuente recomienda consumo secuencial, no batch, y una consulta diaria por usuario.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/reportes-de-facturacion](https://developers.mercadolibre.com.co/es_co/reportes-de-facturacion)  
**Captura:** 2026-10-08T22:52:45.129Z

---

## [Republicar ítems](../markdown/re-publica.md)

Actualización indicada por la fuente: 29/12/2025. Captura: 2026-10-08T22:52:45.965Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/re-publica](https://developers.mercadolibre.com.co/es_co/re-publica)

# Republicar ítems

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:52:45.965Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/re-publica](https://developers.mercadolibre.com.co/es_co/re-publica)

## Resumen

Explica cómo volver a publicar un ítem cerrado conservando relaciones de ventas, preguntas y variantes cuando las reglas lo permiten. El flujo consulta primero su estado/fecha de cierre, lo cierra si es necesario y luego usa el recurso `relist` para crear una publicación nueva.

## Contenido y conceptos documentados

### Reglas y restricciones

- La página indica que el ítem padre debe haberse cerrado como máximo 60 días antes de la republicación. Los ítems `free` no trasladan visitas ni cantidad vendida; para vehículos, inmuebles y servicios se aplica el plazo de 60 días para mantener visitas.
- El ejemplo de cierre usa `PUT /items/$ITEM_ID` con `status: closed`. La republicación usa `POST /items/$ITEM_ID/relist` con `price`, `quantity` y `listing_type_id`; cuando hay variantes, el ejemplo conserva `variations`.
- Las llamadas muestran Bearer. Respuesta y errores específicos de la republicación: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Consultar estado de publicación

**Método:** `GET`  
**Ruta:** `/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene estado, fecha de cierre y datos del ítem padre.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- status
- stop_time
- expiration_time
- listing_type_id
- variations
- automatic_relist

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página consulta status y stop_time antes de relistar.

### Republicar ítem

**Método:** `POST`  
**Ruta:** `/items/$ITEM_ID/relist`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una publicación nueva a partir del ítem cerrado.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "price",
    "quantity",
    "listing_type_id",
    "variations (si aplica)"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El ítem debe haberse cerrado dentro de los 60 días previos, según la página.

### Cerrar ítem padre

**Método:** `PUT`  
**Ruta:** `/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Cambia el estado del ítem a closed antes de republicarlo.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "status: closed"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo de actualización para cerrar el ítem.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/re-publica](https://developers.mercadolibre.com.co/es_co/re-publica)  
**Captura:** 2026-10-08T22:52:45.965Z

---

## [Reputación de vendedores](../markdown/reputacion-de-vendedores.md)

Actualización indicada por la fuente: 11/08/2025. Captura: 2026-10-08T22:52:47.063Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/reputacion-de-vendedores](https://developers.mercadolibre.com.co/es_co/reputacion-de-vendedores)

# Reputación de vendedores

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 11/08/2025  
**Captura:** 2026-10-08T22:52:47.063Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/reputacion-de-vendedores](https://developers.mercadolibre.com.co/es_co/reputacion-de-vendedores)

## Resumen

Explica la reputación como indicador de confianza y ofrece una consulta del usuario que contiene nivel, estado de vendedor profesional y métricas históricas y recientes de transacciones.

## Contenido y conceptos documentados

### Respuesta

- La consulta requiere el identificador del usuario y se muestra con autenticación Bearer.
- `seller_reputation` puede contener `level_id`, `power_seller_status`, `real_level`, `protection_end_date`, transacciones y calificaciones, además de métricas de ventas, reclamos, demoras de despacho y cancelaciones.
- Parámetros de consulta, cuerpo y errores: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Consultar reputación de vendedor

**Método:** `GET`  
**Ruta:** `/users/$USER_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene reputación, transacciones y métricas del usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- seller_reputation.level_id
- seller_reputation.power_seller_status
- seller_reputation.real_level
- seller_reputation.protection_end_date
- seller_reputation.transactions.canceled
- seller_reputation.transactions.completed
- seller_reputation.transactions.ratings.negative
- seller_reputation.transactions.ratings.neutral
- seller_reputation.transactions.ratings.positive
- seller_reputation.metrics.sales
- seller_reputation.metrics.claims
- seller_reputation.metrics.delayed_handling_time
- seller_reputation.metrics.cancellations

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/reputacion-de-vendedores](https://developers.mercadolibre.com.co/es_co/reputacion-de-vendedores)  
**Captura:** 2026-10-08T22:52:47.063Z

---

## [Sincroniza y modifica publicaciones](../markdown/producto-sincroniza-modifica-publicaciones.md)

Actualización indicada por la fuente: 24/03/2026. Captura: 2026-10-08T22:52:48.068Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/producto-sincroniza-modifica-publicaciones](https://developers.mercadolibre.com.co/es_co/producto-sincroniza-modifica-publicaciones)

# Sincroniza y modifica publicaciones

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 24/03/2026  
**Captura:** 2026-10-08T22:52:48.068Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/producto-sincroniza-modifica-publicaciones](https://developers.mercadolibre.com.co/es_co/producto-sincroniza-modifica-publicaciones)

## Resumen

Describe cómo sincronizar cambios de publicaciones activas con otros sistemas, actualizar atributos permitidos y gestionar precio, stock, imágenes, descripción, envío y términos de venta. Incluye restricciones por ventas, variantes, promociones y automatización de precios.

## Contenido y conceptos documentados

### Reglas de actualización

- Para cambiar un ítem se usa `PUT /items/$ITEM_ID`; campos editables dependen de su estado. Con ventas no se permite cambiar título, modo de compra ni ciertos métodos de pago; sin ventas (`sold_quantity=0`) sí puede cambiarse el título. El tipo de publicación solo se puede modificar una vez.
- Desde el 18/03/2026, una actualización que solo envía `price` se rechaza con HTTP 400 cuando hay automatización de precios activa; si se envía junto con otros campos, la página indica que se procesa pero el precio se ignora y se devuelve un warning.
- La fuente documenta errores 409 por optimistic locking al actualizar rápidamente; se recomienda esperar unos segundos antes de repetir. También muestra cambio de `MANUFACTURING_TIME` y límites de `PURCHASE_MAX_QUANTITY`.
- La categoría determina los `sale_terms` válidos. Los cuerpos completos y códigos distintos a los ejemplos: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Consultar términos de venta

**Método:** `GET`  
**Ruta:** `/categories/$CATEGORY_ID/sale_terms`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene los términos de venta permitidos en la categoría.

**Parámetros**

- `CATEGORY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- name
- value_type
- value_id
- value_name

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página usa MANUFACTURING_TIME como ejemplo.

### Crear publicación de prueba

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea un ítem de prueba para validar cambios y sincronización.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "site_id",
    "title",
    "category_id",
    "price",
    "currency_id",
    "pictures"
  ]
}
```

**Respuesta**

- id
- seller_id
- category_id
- price
- status

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo para MLA.

### Actualizar publicación

**Método:** `PUT`  
**Ruta:** `/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza campos permitidos de un ítem, incluidas propiedades comerciales y términos de venta.

**Parámetros**

- `ITEM_ID` (path, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "title",
    "price",
    "available_quantity",
    "sale_terms",
    "status",
    "condition",
    "attributes"
  ]
}
```

**Respuesta**

- message
- warning

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Actualización solo de price rechazada cuando aplica automatización de precio." } ```
- ```json {   "code": 409,   "meaning": "item optimistic locking error: conflict; esperar antes de repetir." } ```

**Ejemplos**

- La fuente indica que si price se envía junto con otros atributos puede ignorarse y producir warning.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/producto-sincroniza-modifica-publicaciones](https://developers.mercadolibre.com.co/es_co/producto-sincroniza-modifica-publicaciones)  
**Captura:** 2026-10-08T22:52:48.068Z

---

## [Stock distribuido](../markdown/stock-distribuido.md)

Actualización indicada por la fuente: 20/04/2026. Captura: 2026-10-08T22:52:49.284Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/stock-distribuido](https://developers.mercadolibre.com.co/es_co/stock-distribuido)

# Stock distribuido

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 20/04/2026  
**Captura:** 2026-10-08T22:52:49.284Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/stock-distribuido](https://developers.mercadolibre.com.co/es_co/stock-distribuido)

## Resumen

Introduce el stock distribuido para un User Product mediante ubicaciones (`stock_locations`). Distingue stock gestionado por Mercado Libre en Full de ubicaciones controladas por el vendedor y describe la concurrencia mediante la versión del stock.

## Contenido y conceptos documentados

### Tipos de ubicación y control de versión

- `meli_facility` representa depósitos Full y no admite modificación por API; `selling_address` representa el depósito del vendedor para logísticas como cross docking, drop-off o Flex; `seller_warehouse` representa depósitos del vendedor en multi-origen.
- La respuesta de consulta contiene ubicaciones con tipo, cantidad y datos de usuario/nodo/tienda. El GET devuelve el encabezado `x-version` (entero largo); debe enviarse al modificar stock.
- Sin `x-version`, la modificación devuelve HTTP 400; con versión desactualizada, devuelve 409. Ante 409 se vuelve a consultar el stock y se usa la nueva versión.
- La fuente indica edición de `selling_address` solo en MLA/MLC cuando la experiencia está activa; `seller_warehouse` requiere que el seller esté habilitado y tenga el tag `warehouse_management`. Campos de request y errores adicionales: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /stock/type/seller_warehouse

La fuente menciona la ruta /stock/type/seller_warehouse, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/stock/type/seller_warehouse`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /stock/

La fuente menciona la ruta /stock/, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/stock/`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /stock/type/selling_address

La fuente menciona la ruta /stock/type/selling_address, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/stock/type/selling_address`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /items

La fuente menciona la ruta /items, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/items`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar stock distribuido

**Método:** `GET`  
**Ruta:** `/user-products/$USER_PRODUCT_ID/stock`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene ubicaciones de stock del User Product y su versión.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- locations[].type
- locations[].quantity
- locations[].user_id
- locations[].id
- locations[].network_node_id
- locations[].store_id

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La respuesta envía el encabezado x-version.

### Actualizar stock seller_warehouse

**Método:** `PUT`  
**Ruta:** `/user-products/$USER_PRODUCT_ID/stock/type/seller_warehouse`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica stock de la ubicación seller warehouse.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)
- `x-version` (header, obligatorio): Versión devuelta por GET /stock.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Falta x-version." } ```
- ```json {   "code": 409,   "meaning": "Versión desactualizada; consultar nuevamente el stock." } ```

**Ejemplos**

No documentado en la fuente.

### Actualizar stock selling_address

**Método:** `PUT`  
**Ruta:** `/user-products/$USER_PRODUCT_ID/stock/type/selling_address`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Modifica stock de la ubicación del vendedor compatible con el site.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)
- `x-version` (header, obligatorio): Versión devuelta por GET /stock.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Falta el header x-version." } ```
- ```json {   "code": 409,   "meaning": "La versión no coincide; consultar de nuevo el stock." } ```

**Ejemplos**

No documentado en la fuente.

### Referencia HTTP PUT /stock/type/seller_warehouse

**Método:** `PUT`  
**Ruta:** `/stock/type/seller_warehouse`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud PUT a /stock/type/seller_warehouse. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

### Referencia HTTP PUT /stock/type/selling_address

**Método:** `PUT`  
**Ruta:** `/stock/type/selling_address`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud PUT a /stock/type/selling_address. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/stock-distribuido](https://developers.mercadolibre.com.co/es_co/stock-distribuido)  
**Captura:** 2026-10-08T22:52:49.284Z

---

## [Stock multi origen](../markdown/stock-multi-origen.md)

Actualización indicada por la fuente: 15/05/2026. Captura: 2026-10-08T22:52:50.281Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/stock-multi-origen](https://developers.mercadolibre.com.co/es_co/stock-multi-origen)

# Stock multi origen

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 15/05/2026  
**Captura:** 2026-10-08T22:52:50.281Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/stock-multi-origen](https://developers.mercadolibre.com.co/es_co/stock-multi-origen)

## Resumen

Explica cómo habilitar y gestionar depósitos de vendedor para distribuir el stock entre tiendas y nodos logísticos. El flujo identifica las capacidades del seller, localiza sus tiendas, crea publicaciones con ubicaciones de stock y después consulta/actualiza stock en User Products.

## Contenido y conceptos documentados

### Flujo, campos y restricciones

- Los sellers con `warehouse_management` gestionan un depósito; al sumar `multiwarehouse` pueden gestionar varios. En Brasil la página indica que los depósitos no pueden estar en estados distintos al del CNPJ. La habilitación de usuarios de prueba se solicita mediante un formulario y se procesa periódicamente.
- La búsqueda de tiendas usa el tag `stock_location`; sus resultados incluyen `store_id` y `network_node_id`. La creación envía `stock_locations` y devuelve `user_product_id`; luego se usa la API de stock de UP.
- La actualización de stock requiere el encabezado `x-version` obtenido al consultar. La fuente enumera errores 400 por ausencia de `stock_locations`, tienda inexistente/ajena/no configurada, `available_quantity` inválido, ausencia de `x-version` y configuración de depósito único con nodos múltiples; 409 corresponde a mismatch de versión.
- Las llamadas muestran Bearer. Los cuerpos completos y códigos no listados aquí: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /user-product

La fuente menciona la ruta /user-product, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/user-product`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /stock/

La fuente menciona la ruta /stock/, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/stock/`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar stock de User Product

**Método:** `GET`  
**Ruta:** `/user-products/$USER_PRODUCT_ID/stock`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene stock distribuido para la publicación y el header de versión.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- locations[].type
- locations[].quantity
- locations[].store_id
- locations[].network_node_id

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La respuesta incluye x-version.

### Consultar tags del vendedor

**Método:** `GET`  
**Ruta:** `/users/$USER_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene tags para identificar habilitación warehouse_management/multiwarehouse.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- id
- nickname
- tags

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Tags determinan si se admite depósito único o múltiples.

### Buscar tiendas del vendedor

**Método:** `GET`  
**Ruta:** `/users/$USER_ID/stores/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca tiendas configuradas como stock_location.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `tags` (query, obligatorio): stock_location.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- paging
- results[].store_id
- results[].network_node_id
- results[].address_id
- results[].location

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Crear ítem multi-origen

**Método:** `POST`  
**Ruta:** `/items/multiwarehouse`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una publicación asociada a ubicaciones de stock del vendedor.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "site_id",
    "title",
    "category_id",
    "price",
    "currency_id",
    "listing_type_id",
    "stock_locations[].store_id",
    "stock_locations[].network_node_id",
    "stock_locations[].quantity"
  ]
}
```

**Respuesta**

- id
- user_product_id
- stock_locations

**Errores documentados**

- ```json {   "code": 400,   "meaning": "stock_locations ausente, tienda inexistente/ajena o available_quantity no permitido para el seller." } ```

**Ejemplos**

- La fuente presenta estado 201 para éxito.

### Actualizar stock de warehouse

**Método:** `PUT`  
**Ruta:** `/user-products/$USER_PRODUCT_ID/stock/type/seller_warehouse`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza inventario por ubicación con control optimista de versión.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)
- `x-version` (header, obligatorio)

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "locations[].store_id",
    "locations[].network_node_id",
    "locations[].quantity"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Missing X-Version header; seller de depósito único no puede enviar varios network_node_id; store ajeno/inexistente/no configurado o vacío." } ```
- ```json {   "code": 409,   "meaning": "Version mismatch; volver a consultar el stock y usar x-version actual." } ```

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/stock-multi-origen](https://developers.mercadolibre.com.co/es_co/stock-multi-origen)  
**Captura:** 2026-10-08T22:52:50.281Z

---

## [Tendencias](../markdown/tendencias.md)

Actualización indicada por la fuente: 27/05/2025. Captura: 2026-10-08T22:52:51.417Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/tendencias](https://developers.mercadolibre.com.co/es_co/tendencias)

# Tendencias

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 27/05/2025  
**Captura:** 2026-10-08T22:52:51.417Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/tendencias](https://developers.mercadolibre.com.co/es_co/tendencias)

## Resumen

Expone las 50 tendencias de productos más populares por sitio y permite acotar la consulta a una categoría. La información se actualiza semanalmente y está disponible en Argentina, Brasil, Chile, México, Colombia, Uruguay y Perú.

## Contenido y conceptos documentados

### Consulta

- Las llamadas muestran Bearer. La primera usa `SITE_ID`; la segunda añade `CATEGORY_ID` para filtrar por categoría.
- La fuente agrupa tendencias como búsquedas con mayor crecimiento, más deseadas y más populares, con base en la actividad reciente. La respuesta presenta `keyword` y `url`.
- La página no detalla cuerpo, paginación ni códigos de error: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Consultar tendencias por sitio

**Método:** `GET`  
**Ruta:** `/trends/$SITE_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene tendencias populares del sitio.

**Parámetros**

- `SITE_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- keyword
- url

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente indica 50 productos, actualización semanal y criterios de crecimiento, deseabilidad/popularidad.

### Consultar tendencias por categoría

**Método:** `GET`  
**Ruta:** `/trends/$SITE_ID/$CATEGORY_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Filtra las tendencias por sitio y categoría.

**Parámetros**

- `SITE_ID` (path, obligatorio)
- `CATEGORY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- keyword
- url

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/tendencias](https://developers.mercadolibre.com.co/es_co/tendencias)  
**Captura:** 2026-10-08T22:52:51.417Z

---

## [Tiendas Oficiales](../markdown/tienda-oficial.md)

Actualización indicada por la fuente: 27/02/2026. Captura: 2026-10-08T22:52:52.494Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/tienda-oficial](https://developers.mercadolibre.com.co/es_co/tienda-oficial)

# Tiendas Oficiales

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 27/02/2026  
**Captura:** 2026-10-08T22:52:52.494Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/tienda-oficial](https://developers.mercadolibre.com.co/es_co/tienda-oficial)

## Resumen

Documenta cómo consultar las marcas asociadas a un usuario de Tienda Oficial y cómo recuperar los datos de una marca concreta. Un usuario puede tener una o varias marcas; en publicaciones, la tienda se identifica mediante `official_store_id`.

## Contenido y conceptos documentados

### Marcas y respuestas

- Ambas consultas muestran `Authorization: Bearer $ACCESS_TOKEN`. La lista incluye estado del vínculo, sitio y marcas, con `official_store_id`, nombre, estado, nombre de fantasía, reputación, URLs, palabras clave e imágenes.
- Para consultar una marca, se envían `USER_ID` y `BRAND` en la ruta. La página muestra 400 cuando el identificador contiene caracteres distintos de dígitos.
- Para sellers multimarca, la publicación debe incluir un `official_store_id` válido: omitirlo puede producir `item.official_store_id.invalid` (400); usar uno no permitido en el sitio puede producir 403. Cuerpos y errores restantes: No documentado en la fuente.

## Operaciones de API
## Operaciones de API

### Listar marcas de Tienda Oficial

**Método:** `GET`  
**Ruta:** `/users/$USER_ID/brands`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene marcas vinculadas a un usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- status
- cust_id
- shield_id
- site_id
- user_type
- brands[].site_id
- brands[].official_store_id
- brands[].name
- brands[].type
- brands[].status
- brands[].fantasy_name
- brands[].date_created
- brands[].landing_permalink
- brands[].keywords
- brands[].pictures

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Un usuario puede tener varias marcas.

### Consultar marca del usuario

**Método:** `GET`  
**Ruta:** `/users/$USER_ID/brands/$BRAND`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalle de una marca vinculada al usuario.

**Parámetros**

- `USER_ID` (path, obligatorio)
- `BRAND` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- official_store_id
- name
- type
- status
- brand_id
- brand_name
- brand_registry

**Errores documentados**

- ```json {   "code": 400,   "meaning": "officialStoreId debe contener solo dígitos." } ```

**Ejemplos**

- La página muestra 400 para identificador no numérico.

### Referencia HTTP GET /users/1477536226/brands/aaaaa

**Método:** `GET`  
**Ruta:** `/users/1477536226/brands/aaaaa`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /users/1477536226/brands/aaaaa. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/tienda-oficial](https://developers.mercadolibre.com.co/es_co/tienda-oficial)  
**Captura:** 2026-10-08T22:52:52.494Z

---

## [Tipos de publicación](../markdown/tipos-de-publicacion-y-actualizaciones-de-articulos.md)

Actualización indicada por la fuente: 01/06/2026. Captura: 2026-10-08T22:52:53.651Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/tipos-de-publicacion-y-actualizaciones-de-articulos](https://developers.mercadolibre.com.co/es_co/tipos-de-publicacion-y-actualizaciones-de-articulos)

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

---

## [User Products](../markdown/user-products.md)

Actualización indicada por la fuente: 17/06/2026. Captura: 2026-10-08T22:52:56.795Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/user-products](https://developers.mercadolibre.com.co/es_co/user-products)

# User Products

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 17/06/2026  
**Captura:** 2026-10-08T22:52:56.795Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/user-products](https://developers.mercadolibre.com.co/es_co/user-products)

## Resumen

Describe el modelo User Product (UP), que separa la entidad del producto de las condiciones comerciales de sus publicaciones y permite gestionar precio por variante, stock distribuido y multi-origen. La guía explica las relaciones entre ítem, UP y familia.

## Contenido y conceptos documentados

### Modelo y consultas

- Un ítem es la publicación visible; el User Product agrupa productos/variantes y la familia relaciona UPs. Los cambios de propiedades del UP enviados mediante `PUT /items` pueden propagarse de forma asíncrona a los ítems relacionados.
- Para resolver relaciones, la página indica consultar el ítem para obtener `user_product_id`, consultar el UP para `family_id`, consultar la familia del sitio y buscar ítems de un seller por `user_product_id`. El buscador puede recibir varios IDs como lista.
- La captura también señala que `child_pk` y `parent_pk` read-only no se consideran para generar la familia. Cambios/campos no detallados en esta página: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /categories

La fuente menciona la ruta /categories, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/categories`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Obtener user_product_id

**Método:** `GET`  
**Ruta:** `/items`  
**Autenticación:** No documentado en la fuente

Consulta un ítem para resolver el User Product asociado.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- user_product_id

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar familia de User Products

**Método:** `GET`  
**Ruta:** `/sites/$SITE_ID/user-products-families/$FAMILY_ID`  
**Autenticación:** No documentado en la fuente

Obtiene User Products asociados a una familia del sitio.

**Parámetros**

- `SITE_ID` (path, obligatorio)
- `FAMILY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- family_id
- user_products

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar User Product

**Método:** `GET`  
**Ruta:** `/user-products/$USER_PRODUCT_ID`  
**Autenticación:** No documentado en la fuente

Consulta el UP para obtener la familia a la que pertenece.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- user_product_id
- family_id
- attributes

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Buscar ítems asociados a UP

**Método:** `GET`  
**Ruta:** `/users/$SELLER_ID/items/search`  
**Autenticación:** No documentado en la fuente

Busca ítems de un seller por uno o varios identificadores de User Product.

**Parámetros**

- `SELLER_ID` (path, obligatorio)
- `user_product_id` (query, obligatorio): La página ejemplifica lista de IDs.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- results
- user_product_id

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente da ejemplo con varios IDs separados por coma.

### Modificar características de User Product

**Método:** `PUT`  
**Ruta:** `/items`  
**Autenticación:** No documentado en la fuente

Modifica características de los ítems asociadas al User Product; la propagación descrita es asíncrona.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "title",
    "family_name",
    "attributes"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- No se consideran child_pk y parent_pk read_only para generar la familia.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/user-products](https://developers.mercadolibre.com.co/es_co/user-products)  
**Captura:** 2026-10-08T22:52:56.795Z

---

## [Validaciones](../markdown/validaciones.md)

Actualización indicada por la fuente: 29/12/2025. Captura: 2026-10-08T22:52:58.854Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/validaciones](https://developers.mercadolibre.com.co/es_co/validaciones)

# Validaciones

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 29/12/2025  
**Captura:** 2026-10-08T22:52:58.854Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/validaciones](https://developers.mercadolibre.com.co/es_co/validaciones)

## Resumen

Describe la respuesta de validación que puede acompañar la creación de una publicación para advertir o bloquear inconsistencias de datos, moderaciones, envío, imágenes u otros dominios.

## Contenido y conceptos documentados

### Estructura y tratamiento

- El objeto de error incluye `message`, `error`, `status` y `cause[]`. Cada causa identifica `department`, `cause_id`, `type` (`warning` o `error`), `code`, `references` y `message`; los warnings informan y no bloquean, mientras que los errores requieren acción.
- La tabla de la fuente asocia códigos con causa, atributo afectado y solución. Entre los ejemplos aparecen atributos condicionales, vendedor no autorizado para marca/categoría, normalización de valores, imágenes menores a 500 píxeles y validación del GTIN/código universal.
- Para validar un identificador universal, la página referencia `/product-identifier/validator?product_identifier=$UNIVERSAL_CODE_FIELD`, pero no indica el método HTTP. El resto de parámetros, autenticación y respuestas de ese recurso: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Validaciones de publicaciones

Describe el objeto validation_error/cause usado para reportar warnings y errores de publicación; incluye department, cause_id, type, code, references y message, así como ejemplos de validación de atributos, autorización, normalización, imágenes y GTIN.

**Errores documentados**

- ```json {   "code": 400,   "meaning": "Validation error; cause[] puede contener validaciones de tipo warning o error." } ```
### Ruta mencionada /categories/{CATEGORY_ID}/{TYPE_ID}

La fuente menciona la ruta /categories/{CATEGORY_ID}/{TYPE_ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/categories/{CATEGORY_ID}/{TYPE_ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /categories/{CATEGORY_ID}

La fuente menciona la ruta /categories/{CATEGORY_ID}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/categories/{CATEGORY_ID}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /categories/{CATEGORY_ID}/attributes

La fuente menciona la ruta /categories/{CATEGORY_ID}/attributes, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/categories/{CATEGORY_ID}/attributes`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

La página no documenta una operación HTTP concreta.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/validaciones](https://developers.mercadolibre.com.co/es_co/validaciones)  
**Captura:** 2026-10-08T22:52:58.854Z

---

## [Validación de guía de talles](../markdown/validacion-de-guia-de-talles.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:52:57.692Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/validacion-de-guia-de-talles](https://developers.mercadolibre.com.co/es_co/validacion-de-guia-de-talles)

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

---

## [Variaciones](../markdown/variaciones.md)

Actualización indicada por la fuente: 30/12/2025. Captura: 2026-10-08T22:53:01.331Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/variaciones](https://developers.mercadolibre.com.co/es_co/variaciones)

# Variaciones

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:01.331Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/variaciones](https://developers.mercadolibre.com.co/es_co/variaciones)

## Resumen

Explica cómo reunir variantes de un mismo producto en una publicación y administrar su stock por combinación. El comprador selecciona atributos como color y talle, que aparecen asociados a la orden.

## Contenido y conceptos documentados

- Identifica en la categoría los atributos allow_variations; envíalos en attribute_combinations de todas las variantes. Los atributos variation_attribute describen propiedades particulares. Los requeridos se identifican con required=true.
- La fuente indica un máximo de 100 variantes por categoría y 250 para Moda, Accesorios para celulares y Autopartes. Cada variante requiere price, available_quantity, pictures y attribute_combinations; max_pictures_per_item_var indica el máximo de imágenes. No repitas combinaciones; un atributo ajeno a la categoría puede ser ignorado.
- El SKU de variante debe guardarse en SELLER_SKU dentro de attributes. Para consultar atributos de variantes, agrega include_attributes=all. Al actualizar, envía las variantes a conservar; con ventas solo se pueden sumar atributos. Se permite un atributo personalizado cuando no está definido por la categoría. La fuente recomienda el mismo precio para todas las variantes; si se envían precios distintos, la publicación y el pago consideran el precio más alto.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /orders

La fuente menciona la ruta /orders, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/orders`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Reglas de datos de variaciones

Las combinaciones deben ser válidas para la categoría, iguales en estructura entre variantes y no repetir combinaciones. SELLER_SKU identifica el stock de cada variante; seller_custom_field es distinto. La página indica límites de cantidad por categoría, atributos requeridos, máximo de imágenes configurable y restricciones para variantes vendidas. La fuente recomienda mantener el mismo precio entre variantes y advierte que la VIP y el pago consideran el valor más alto si difieren.

**Errores documentados**

- ```json {   "code": "variation_limit",   "meaning": "La fuente indica 100 variantes por categoría y 250 para Moda, Accesorios para celulares y Autopartes." } ```

**Ejemplos documentados**

- Ejemplos de color, talle, EAN/UPC, voltaje y un atributo personalizado.
## Operaciones de API

### Eliminar variación

**Método:** `DELETE`  
**Ruta:** `/items/{item_id}/variations/{variation_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Elimina la variante indicada; también se muestra como alternativa un PUT al ítem conservando solo los IDs deseados.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.
- `variation_id` (path, obligatorio): ID de la variante.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo devuelve información del ítem; no documenta un esquema reducido.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- DELETE /items/MLA599099879/variations/10449631060.

### Consultar atributos de categoría para variaciones

**Método:** `GET`  
**Ruta:** `/categories/{category_id}/attributes`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Comprueba los tags allow_variations y variation_attribute de atributos de una categoría.

**Parámetros**

- `category_id` (path, obligatorio): ID de categoría.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de atributos con id, name, tags, value_type y values.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /categories/MLA126186/attributes; COLOR aparece con allow_variations.

### Consultar variaciones dentro del ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta un ítem; attributes=variations permite filtrar la respuesta a esa propiedad.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.
- `attributes` (query): El ejemplo usa variations.
- `include_attributes` (query): La fuente muestra all para incluir attributes de las variantes.

**Solicitud**

No documentado en la fuente.

**Respuesta**

La sección variations puede contener id, attribute_combinations, price, available_quantity, sold_quantity, picture_ids, seller_custom_field y catalog_product_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /items/MLA658778048?attributes=variations; también se documenta include_attributes=all.

### Listar variaciones de un ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}/variations`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve directamente el array de variantes de la publicación.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Array con id, attribute_combinations, price, available_quantity, sold_quantity, picture_ids, seller_custom_field y catalog_product_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /items/MLA658778048/variations.

### Consultar una variación

**Método:** `GET`  
**Ruta:** `/items/{item_id}/variations/{variation_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el detalle de una variante concreta.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.
- `variation_id` (path, obligatorio): ID de la variante.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo incluye id, attribute_combinations, price, available_quantity, sold_quantity, picture_ids y attributes (EAN/UPC).

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /items/MLA658778048/variations/15092589430.

### Crear publicación con variaciones

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea un ítem con variaciones y sus combinaciones de atributos, stock e imágenes.

**Parámetros**

- `category_id` (body): Categoría.
- `site_id` (body): Sitio.
- `title` (body): Título.
- `listing_type_id` (body): Tipo de publicación.
- `variations` (body): Combinaciones de atributos, precio, stock, atributos e imágenes por variante.

**Solicitud**

JSON con listing_type_id, pictures, title, available_quantity, category_id, buying_mode, currency_id, condition, site_id, price y variations. Cada variante incluye attribute_combinations, price, available_quantity, attributes, sold_quantity y picture_ids.

**Respuesta**

Ejemplo de respuesta de publicación con id, site_id, title y sold_quantity.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- POST http://api.mercadolibre.com/items con variantes por color y EAN.

### Agregar variación

**Método:** `POST`  
**Ruta:** `/items/{item_id}/variations`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrega una variante con combinación, precio, stock e imágenes. La prosa dice PUT al ítem, pero el ejemplo de solicitud usa POST al recurso /variations.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

JSON de variante: attribute_combinations (id/value_id), price, available_quantity, sold_quantity y picture_ids.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- POST /items/MLA658778048/variations.

### Actualizar variaciones del ítem

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza variantes y atributos enviando la propiedad variations.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

JSON con variations; la fuente muestra id, attribute_combinations, attributes, price y available_quantity. Envíe las variantes a conservar. Con ventas, solo se pueden sumar atributos, no cambiar ni quitar los existentes.

**Respuesta**

Ejemplo devuelve el ítem y su lista variations.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- PUT /items/{item_id} para agregar combinaciones COLOR/VOLTAGE o modificar stock.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/variaciones](https://developers.mercadolibre.com.co/es_co/variaciones)  
**Captura:** 2026-10-08T22:53:01.331Z

---

## [Visitas](../markdown/recurso-de-visitas.md)

Actualización indicada por la fuente: 02/01/2026. Captura: 2026-10-08T22:53:02.514Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/recurso-de-visitas](https://developers.mercadolibre.com.co/es_co/recurso-de-visitas)

# Visitas

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 02/01/2026  
**Captura:** 2026-10-08T22:53:02.514Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/recurso-de-visitas](https://developers.mercadolibre.com.co/es_co/recurso-de-visitas)

## Resumen

Permite consultar visitas de usuarios y publicaciones por fechas o ventanas de tiempo. Al republicar un artículo, las visitas históricas se heredan del parent_item.

## Contenido y conceptos documentados

- Parámetros descritos: user_id, item_id, date_from/date_to ISO (máximo 150 días), ending opcional YYYY-MM-DD, unit con valor day y last para delimitar la ventana.
- Las respuestas incluyen total_visits y visits_detail; las consultas time_window agregan results por intervalo. /visits/items se describe como total de los últimos dos años.
- Errores documentados incluyen site inválido, fechas mal formadas o ausentes, ventana mayor a 150 días, ending inválido, más de un item, formato incorrecto de ID, token no autorizado y artículo inexistente en time_window.

## Operaciones de API
## Operaciones de API

### Consultar ventana de visitas por artículo

**Método:** `GET`  
**Ruta:** `/items/{item_id}/visits/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrupa visitas de un artículo por intervalos de tiempo.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.
- `last` (query, opcional): Cantidad de unidades hacia atrás.
- `unit` (query, obligatorio): Unidad; la fuente enumera day.
- `ending` (query, opcional): Fecha YYYY-MM-DD; por defecto fecha/hora actual.

**Solicitud**

No documentado en la fuente.

**Respuesta**

item_id, fechas, total_visits, last, unit y results por fecha.

**Errores documentados**

- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid Site ID: usuario o ítem no pertenece a un site local válido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "unknown date format: date_from/date_to faltante o inválido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid time window: rango máximo 150 días." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid date format for ending date: solo YYYY-MM-DD." } ```
- ```json {   "status": 400,   "code": "validation_parameters",   "meaning": "maximum amount of items to query is 1." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid item ID format." } ```
- ```json {   "status": 403,   "code": "PA_UNAUTHORIZED_RESULT_FROM_POLICIES",   "meaning": "Token inválido, vencido o sin permisos." } ```
- ```json {   "status": 404,   "code": "not_found",   "meaning": "Item not found en time_window." } ```

**Ejemplos**

- GET /items/MCO471870973/visits/time_window?last=2&unit=day&ending=2021-08-06.

### Consultar visitas de artículo por fechas

**Método:** `GET`  
**Ruta:** `/items/visits`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera visitas de un artículo en fechas determinadas y por site.

**Parámetros**

- `ids` (query, obligatorio): ID de artículo; máximo documentado uno.
- `date_from` (query, obligatorio): Fecha inicial ISO; máximo documentado 150 días.
- `date_to` (query, obligatorio): Fecha final ISO; máximo documentado 150 días.

**Solicitud**

No documentado en la fuente.

**Respuesta**

item_id, date_from, date_to, total_visits y visits_detail.

**Errores documentados**

- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid Site ID: usuario o ítem no pertenece a un site local válido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "unknown date format: date_from/date_to faltante o inválido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid time window: rango máximo 150 días." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid date format for ending date: solo YYYY-MM-DD." } ```
- ```json {   "status": 400,   "code": "validation_parameters",   "meaning": "maximum amount of items to query is 1." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid item ID format." } ```
- ```json {   "status": 403,   "code": "PA_UNAUTHORIZED_RESULT_FROM_POLICIES",   "meaning": "Token inválido, vencido o sin permisos." } ```
- ```json {   "status": 404,   "code": "not_found",   "meaning": "Item not found en time_window." } ```

**Ejemplos**

- GET /items/visits?ids=MCO473861358&date_from=2021-01-01&date_to=2021-02-01.

### Consultar visitas totales de usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items_visits`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera visitas de publicaciones de un usuario en un intervalo.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario.
- `date_from` (query, obligatorio): Fecha inicial ISO; máximo documentado 150 días.
- `date_to` (query, obligatorio): Fecha final ISO; máximo documentado 150 días.

**Solicitud**

No documentado en la fuente.

**Respuesta**

user_id, date_from, date_to, total_visits y visits_detail (company, quantity).

**Errores documentados**

- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid Site ID: usuario o ítem no pertenece a un site local válido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "unknown date format: date_from/date_to faltante o inválido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid time window: rango máximo 150 días." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid date format for ending date: solo YYYY-MM-DD." } ```
- ```json {   "status": 400,   "code": "validation_parameters",   "meaning": "maximum amount of items to query is 1." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid item ID format." } ```
- ```json {   "status": 403,   "code": "PA_UNAUTHORIZED_RESULT_FROM_POLICIES",   "meaning": "Token inválido, vencido o sin permisos." } ```
- ```json {   "status": 404,   "code": "not_found",   "meaning": "Item not found en time_window." } ```

**Ejemplos**

- GET /users/1000011398/items_visits?date_from=2021-01-01&date_to=2021-02-01.

### Consultar ventana de visitas por usuario

**Método:** `GET`  
**Ruta:** `/users/{user_id}/items_visits/time_window`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Agrupa visitas de un usuario por intervalos dentro de una ventana.

**Parámetros**

- `user_id` (path, obligatorio): ID de usuario.
- `last` (query, opcional): Cuántos días hacia atrás.
- `unit` (query, obligatorio): Unidad; la fuente enumera day.
- `ending` (query, opcional): Fecha YYYY-MM-DD; por defecto fecha/hora actual.

**Solicitud**

No documentado en la fuente.

**Respuesta**

user_id, fechas, total_visits, last, unit y results agrupados por día.

**Errores documentados**

- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid Site ID: usuario o ítem no pertenece a un site local válido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "unknown date format: date_from/date_to faltante o inválido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid time window: rango máximo 150 días." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid date format for ending date: solo YYYY-MM-DD." } ```
- ```json {   "status": 400,   "code": "validation_parameters",   "meaning": "maximum amount of items to query is 1." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid item ID format." } ```
- ```json {   "status": 403,   "code": "PA_UNAUTHORIZED_RESULT_FROM_POLICIES",   "meaning": "Token inválido, vencido o sin permisos." } ```
- ```json {   "status": 404,   "code": "not_found",   "meaning": "Item not found en time_window." } ```

**Ejemplos**

- GET /users/1000011398/items_visits/time_window?last=2&unit=day.

### Consultar visitas totales de artículo

**Método:** `GET`  
**Ruta:** `/visits/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve las visitas acumuladas del artículo; la guía lo describe para los últimos dos años.

**Parámetros**

- `ids` (query, obligatorio): ID del artículo; la fuente limita esta consulta a uno.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto indexado por ID de ítem con el total.

**Errores documentados**

- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid Site ID: usuario o ítem no pertenece a un site local válido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "unknown date format: date_from/date_to faltante o inválido." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid time window: rango máximo 150 días." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "invalid date format for ending date: solo YYYY-MM-DD." } ```
- ```json {   "status": 400,   "code": "validation_parameters",   "meaning": "maximum amount of items to query is 1." } ```
- ```json {   "status": 400,   "code": "bad_request",   "meaning": "Invalid item ID format." } ```
- ```json {   "status": 403,   "code": "PA_UNAUTHORIZED_RESULT_FROM_POLICIES",   "meaning": "Token inválido, vencido o sin permisos." } ```
- ```json {   "status": 404,   "code": "not_found",   "meaning": "Item not found en time_window." } ```

**Ejemplos**

- GET /visits/items?ids=MLB9992242141.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/recurso-de-visitas](https://developers.mercadolibre.com.co/es_co/recurso-de-visitas)  
**Captura:** 2026-10-08T22:53:02.514Z

---

## [Órdenes](../markdown/gestiona-ventas.md)

Actualización indicada por la fuente: 21/09/2026. Captura: 2026-10-08T22:52:16.978Z.

Fuente: [https://developers.mercadolibre.com.co/es_co/gestiona-ventas](https://developers.mercadolibre.com.co/es_co/gestiona-ventas)

# Órdenes

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 21/09/2026  
**Captura:** 2026-10-08T22:52:16.978Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/gestiona-ventas](https://developers.mercadolibre.com.co/es_co/gestiona-ventas)

## Resumen

Describe consulta y búsqueda de órdenes, detalle de productos, pagos, descuentos y envíos. La orden agrupa condiciones de compra visibles para comprador y vendedor.

## Contenido y conceptos documentados

- /orders/{order_id} incluye estado, fechas, artículos, pagos, feedback, envío y participantes; para feedback, la fuente remite a su recurso específico.
- /orders/search filtra por seller, buyer, item, tags/tags.not, q, estados, fechas, mediaciones y feedback. q busca ID de orden, ID/título del ítem y nickname de contraparte, no nombres ni email. Se muestran paginación y sort=date_desc.
- La consulta de envíos puede devolver varios registros. Hosted View siempre produce array; identifica el envío de compra por type=forward. La fuente advierte que el contrato de la vista actual (objeto por defecto) difiere del array de Hosted View y marca la vista actual como deprecada desde finales de septiembre de 2026.
- También se documentan conversión de moneda, atributos de productos y descuentos. La guía enumera estados confirmed, payment_required, payment_in_process, partially_paid, paid, partially_refunded, pending_cancel y cancelled.

## Operaciones de API

## Conceptos y recursos asociados

### Ciclo y estados de órdenes

La guía cubre consulta, búsqueda, pagos, descuentos, feedback y envíos. Indica retención de órdenes hasta 12 meses y exclusión de canceladas al buscar como vendedor; enumera estados confirmed, payment_required, payment_in_process, partially_paid, paid, partially_refunded, pending_cancel y cancelled.

**Ejemplos documentados**

- Ejemplos de orden pagada y de filtros por estado/fecha.
### Ruta mencionada /orders/{order_id}/feedback

La fuente menciona la ruta /orders/{order_id}/feedback, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/orders/{order_id}/feedback`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /discounts

La fuente menciona la ruta /discounts, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/discounts`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /shipments

La fuente menciona la ruta /shipments, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/shipments`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /packs

La fuente menciona la ruta /packs, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/packs`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
### Ruta mencionada /shipments/shipping.id

La fuente menciona la ruta /shipments/shipping.id, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/shipments/shipping.id`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar conversión de moneda

**Método:** `GET`  
**Ruta:** `/currency_conversions/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene la tasa entre moneda de origen y destino.

**Parámetros**

- `from` (query, obligatorio): Código de moneda de origen.
- `to` (query, obligatorio): Código de moneda destino.

**Solicitud**

No documentado en la fuente.

**Respuesta**

ratio.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /currency_conversions/search?from=ARS&to=BRL.

### Consultar orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve estado, fechas, productos, pagos, compradores/vendedores, feedback, envío y etiquetas.

**Parámetros**

- `order_id` (path, obligatorio): ID de orden.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Ejemplo: id, status, status_detail, date_created, date_closed, order_items, total_amount, currency_id, buyer, seller, payments, feedback, context, shipping, static_tags y tags.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /orders/2000003508419013.

### Consultar descuentos de una orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}/discounts`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve descuentos que incidieron en la venta, incluidos cupón, campañas y cashback.

**Parámetros**

- `order_id` (path, obligatorio): ID de orden.

**Solicitud**

No documentado en la fuente.

**Respuesta**

details con type, coupon/supplier e items con quantity y amounts (total/seller).

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /orders/2000003508419013/discounts.

### Consultar atributos de productos de una orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}/product`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve los atributos registrados para los productos de una orden.

**Parámetros**

- `order_id` (path, obligatorio): ID de orden.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto con attributes; cada elemento puede contener name, value e id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo con atributos IMEI y entry_date.

### Consultar envíos asociados a orden

**Método:** `GET`  
**Ruta:** `/orders/{order_id}/shipments`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene IDs/tipos de envíos. Hosted View siempre devuelve array; recorrer resultados y filtrar type=forward para identificar envío de compra. La vista actual se marca deprecada desde finales de septiembre de 2026.

**Parámetros**

- `order_id` (path, obligatorio): ID de orden.
- `hosted` (query, opcional): Default false; vista APICore sin detalle de envíos.
- `list_all` (query, opcional): En la vista actual, true devuelve array forward y return.
- `X-New-Domain` (header, opcional): Necesario en llamadas públicas para enrutar a Hosted View.
- `X-Api-Version` (header, opcional): Valor 2 solicita receiver_name y receiver_phone completos en receiver_address en la vista actual.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Hosted View: array de objetos {id,type}; se ejemplifican forward, return y return_to_buyer. Vista actual: objeto con datos del shipment, estado, modalidad, tracking, historial, shipping_items y dirección.

**Errores documentados**

- ```json {   "status": 200,   "meaning": "Envíos encontrados." } ```
- ```json {   "status": 204,   "meaning": "La orden no tiene envíos o están en propagación asíncrona." } ```
- ```json {   "status": 400,   "meaning": "Parámetros inválidos, como order_id no numérico." } ```
- ```json {   "status": 401,   "meaning": "Autenticación fallida o caller no identificado." } ```
- ```json {   "status": 403,   "meaning": "Permisos insuficientes." } ```
- ```json {   "status": 404,   "meaning": "order_id inexistente." } ```
- ```json {   "status": 500,   "meaning": "Error interno." } ```
- ```json {   "status": 503,   "meaning": "Servicio no disponible." } ```

**Ejemplos**

- GET /orders/{order_id}/shipments; ejemplos con X-New-Domain:true y list_all=true.

### Buscar órdenes

**Método:** `GET`  
**Ruta:** `/orders/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Filtra órdenes por usuario, ítem, estado, fechas, tags, mediaciones y feedback.

**Parámetros**

- `seller` (query): ID vendedor; aparece en ejemplos.
- `buyer` (query): ID comprador.
- `item` (query): ID o título.
- `tags` (query): Estados separados por coma.
- `tags.not` (query): Estados excluidos separados por coma.
- `q` (query): Busca ID de orden, ID/título de ítem o nickname de contraparte; no busca first_name, last_name ni email.
- `order.status` (query): Filtro u ordenamiento enumerado en la guía.
- `order.date_last_updated.from` (query): Filtro u ordenamiento enumerado en la guía.
- `order.date_last_updated.to` (query): Filtro u ordenamiento enumerado en la guía.
- `order.date_created.from` (query): Filtro u ordenamiento enumerado en la guía.
- `order.date_created.to` (query): Filtro u ordenamiento enumerado en la guía.
- `order.date_closed.from` (query): Filtro u ordenamiento enumerado en la guía.
- `order.date_closed.to` (query): Filtro u ordenamiento enumerado en la guía.
- `mediations.stage` (query): Filtro u ordenamiento enumerado en la guía.
- `mediations.status` (query): Filtro u ordenamiento enumerado en la guía.
- `feedback.status` (query): Filtro u ordenamiento enumerado en la guía.
- `feedback.sale.rating` (query): Filtro u ordenamiento enumerado en la guía.
- `feedback.sale.fulfilled` (query): Filtro u ordenamiento enumerado en la guía.
- `feedback.purchase.rating` (query): Filtro u ordenamiento enumerado en la guía.
- `feedback.purchase.fulfilled` (query): Filtro u ordenamiento enumerado en la guía.
- `sort` (query): Filtro u ordenamiento enumerado en la guía.

**Solicitud**

No documentado en la fuente.

**Respuesta**

query, results, sort, available_sorts, filters, paging y display; resultados con orden, pagos, compradores, vendedores, envíos e ítems.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Filtros order.status=paid, q y order.date_created.from/to; orden sort=date_desc.

### Referencia HTTP GET /shipments

**Método:** `GET`  
**Ruta:** `/shipments`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /shipments. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/gestiona-ventas](https://developers.mercadolibre.com.co/es_co/gestiona-ventas)  
**Captura:** 2026-10-08T22:52:16.978Z

---
