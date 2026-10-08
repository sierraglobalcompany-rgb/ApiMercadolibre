---
id: "diagnostico-imagenes"
title: "Diagnóstico de imágenes"
section: "Recursos de la API"
subsection: "Moderaciones"
url: "https://developers.mercadolibre.com.co/es_co/diagnostico-imagenes"
source_updated_at: "29/12/2025"
captured_at: "2026-10-08T22:53:44.400Z"
sha256: "c573525825e4085983e2b2de11fbbf8c539d519c2d59e893d9a18524ac33c6bf"
---

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
