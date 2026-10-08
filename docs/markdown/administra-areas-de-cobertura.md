---
id: "administra-areas-de-cobertura"
title: "Administra áreas de cobertura"
section: "Guía para servicios"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/administra-areas-de-cobertura"
source_updated_at: "15/03/2023"
captured_at: "2026-10-08T22:53:03.494Z"
sha256: "7395c3bc5ad9129fbcf605d55596c2e7732ea5d7e95d99c771de653a52028cc9"
---

# Administra áreas de cobertura

**Área:** Guía para servicios  
**Actualización indicada por la fuente:** 15/03/2023  
**Captura:** 2026-10-08T22:53:03.494Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/administra-areas-de-cobertura](https://developers.mercadolibre.com.co/es_co/administra-areas-de-cobertura)

## Resumen

Explica cómo descubrir IDs predefinidos de cobertura y asociarlos a una publicación de servicio.

## Contenido y conceptos documentados

- El listado por sitio devuelve id, description, zone y type; se muestran áreas de Argentina y un ID nacional.
- El detalle se obtiene por ID de área. Para asignar cobertura, la fuente envía una lista de IDs bajo coverage_areas mediante PUT al ítem.

## Operaciones de API
## Operaciones de API

### Consultar área de cobertura por ID

**Método:** `GET`  
**Ruta:** `/coverage_areas/{coverage_area_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene detalle de un área identificada por su ID.

**Parámetros**

- `coverage_area_id` (path, obligatorio): ID preestablecido del área.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, description, zone y type.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /coverage_areas/TUxBUEpVSnk3YmUz.

### Listar áreas de cobertura

**Método:** `GET`  
**Ruta:** `/sites/{site_id}/coverage_areas`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista áreas disponibles para el sitio/país.

**Parámetros**

- `site_id` (path, obligatorio): Código del sitio.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Array con id, description, zone y type.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /sites/MLA/coverage_areas.

### Asignar áreas de cobertura

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza el ítem con las áreas geográficas atendidas por el servicio.

**Parámetros**

- `item_id` (path, obligatorio): ID de publicación.

**Solicitud**

JSON con coverage_areas como lista de IDs de cobertura.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- PUT /items/ITEM_ID con dos IDs de área.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/administra-areas-de-cobertura](https://developers.mercadolibre.com.co/es_co/administra-areas-de-cobertura)  
**Captura:** 2026-10-08T22:53:03.494Z
