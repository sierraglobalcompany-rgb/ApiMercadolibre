---
id: "marcadores"
title: "Favoritos"
section: "Recursos de la API"
subsection: "Usuarios"
url: "https://developers.mercadolibre.com.co/es_co/marcadores"
source_updated_at: "30/12/2025"
captured_at: "2026-10-08T22:53:47.588Z"
sha256: "8cfdd31c4dee307480239f50f6a4aed0ce75e8d3d07c4856ff6176670aa6f76c"
---

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
