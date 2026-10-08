---
id: "tendencias"
title: "Tendencias"
section: "Guía para productos"
subsection: "Métricas y Tendencias"
url: "https://developers.mercadolibre.com.co/es_co/tendencias"
source_updated_at: "27/05/2025"
captured_at: "2026-10-08T22:52:51.417Z"
sha256: "2753f4db91b028d737edc9fdb7b47662a22e585dd8504986486b177a0bbc1315"
---

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
