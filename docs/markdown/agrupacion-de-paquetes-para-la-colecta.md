---
id: "agrupacion-de-paquetes-para-la-colecta"
title: "Agrupación de paquetes para la Colecta"
section: "Guía para productos"
subsection: "Mercado Envíos 2"
url: "https://developers.mercadolibre.com.co/es_co/agrupacion-de-paquetes-para-la-colecta"
source_updated_at: "19/05/2026"
captured_at: "2026-10-08T22:51:00.906Z"
sha256: "456070bc9b893474fdc02acc8f656c5d279dac8b87b82ac3b017c305a534c974"
---

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
