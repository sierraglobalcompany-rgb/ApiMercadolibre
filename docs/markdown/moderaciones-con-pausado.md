---
id: "moderaciones-con-pausado"
title: "Moderaciones con pausado"
section: "Recursos de la API"
subsection: "Moderaciones"
url: "https://developers.mercadolibre.com.co/es_co/moderaciones-con-pausado"
source_updated_at: "12/06/2026"
captured_at: "2026-10-08T22:53:52.153Z"
sha256: "da078f054da90da3fcbc24aa20b58be26c4a1047b6851d3282c3013c6cd6b3c0"
---

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
