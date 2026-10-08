---
id: "trabajar-con-imagenes"
title: "Imágenes"
section: "Guía para productos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/trabajar-con-imagenes"
source_updated_at: "24/03/2026"
captured_at: "2026-10-08T22:52:03.544Z"
sha256: "76405248491b1fb96f06cdf061482f5e28b4a816db56204aff321be4baf0fd42"
---

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
