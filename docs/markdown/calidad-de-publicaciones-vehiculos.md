---
id: "calidad-de-publicaciones-vehiculos"
title: "Calidad de publicaciones (vehículos)"
section: "Guía para vehículos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones-vehiculos"
source_updated_at: "19/06/2026"
captured_at: "2026-10-08T22:53:11.313Z"
sha256: "b7306767c1d8c32e491213ba1c7ab525b3dcd59def0e18d325b21dee6f2ed264"
---

# Calidad de publicaciones (vehículos)

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 19/06/2026  
**Captura:** 2026-10-08T22:53:11.313Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones-vehiculos](https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones-vehiculos)

## Resumen

Describe consultas para conocer la puntuación de calidad vehicular, nivel y acciones pendientes que pueden elevar la exposición.

## Contenido y conceptos documentados

- Los rangos por sitio usan level, health_min y health_max. /health calcula la puntuación a partir de objetivos aplicables y devuelve goals con progress, progress_max, apply, completed y data. technical_specification puede indicar atributos faltantes.
- /health/actions presenta acciones pendientes. La fuente nombra picture, price, technical_specification, video, upgrade_listing y publish; indica que whatsapp ya no se contabiliza como objetivo de calidad aunque aún puede beneficiar conversiones.

## Operaciones de API
## Operaciones de API

### Consultar calidad de un ítem

**Método:** `GET`  
**Ruta:** `/items/{item_id}/health`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Devuelve puntuación, nivel y progreso de los objetivos de calidad aplicables.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

item_id, health, level y goals; cada objetivo puede contener progress, progress_max, id, name, apply, completed y data.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /items/MLM735814032/health.

### Consultar acciones para mejorar calidad

**Método:** `GET`  
**Ruta:** `/items/{item_id}/health/actions`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista tareas pendientes que pueden mejorar el nivel/exposición de la publicación.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

No documentado en la fuente.

**Respuesta**

item_id, health y actions con id/name.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /items/MLM735814032/health/actions.

### Consultar niveles de calidad por sitio

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/health_levels`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene rangos de puntaje para niveles de calidad en un sitio.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de level, health_min y health_max; ejemplo basic, standard y professional.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLB/health_levels.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones-vehiculos](https://developers.mercadolibre.com.co/es_co/calidad-de-publicaciones-vehiculos)  
**Captura:** 2026-10-08T22:53:11.313Z
