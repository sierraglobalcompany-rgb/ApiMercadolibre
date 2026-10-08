---
id: "moderaciones-de-imagenes"
title: "Moderaciones de imágenes"
section: "Recursos de la API"
subsection: "Moderaciones"
url: "https://developers.mercadolibre.com.co/es_co/moderaciones-de-imagenes"
source_updated_at: "21/07/2025"
captured_at: "2026-10-08T22:53:53.123Z"
sha256: "1c6b575adad42e37a17cab38052f5ca4a5abd65e506f37ec10b3add674d59c9b"
---

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
