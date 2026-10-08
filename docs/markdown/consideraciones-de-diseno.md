---
id: "consideraciones-de-diseno"
title: "Consideraciones de diseño"
section: "Primeros pasos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/consideraciones-de-diseno"
source_updated_at: "30/12/2025"
captured_at: "2026-10-08T22:53:29.373Z"
sha256: "9553f44331ba40bd1476d97a6eee9321c6589d074af2dd85b2728331443907d6"
---

# Consideraciones de diseño

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:29.373Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/consideraciones-de-diseno](https://developers.mercadolibre.com.co/es_co/consideraciones-de-diseno)

## Resumen

Describe convenciones comunes de las APIs de Mercado Libre: JSON, JSONP, selección de atributos, documentación con OPTIONS, manejo de errores y paginación.

## Contenido y conceptos documentados

- Las respuestas estándar de error contienen `message`, `error`, `status` y `cause`. Con `attributes` se limitan los campos devueltos. JSONP usa `callback` y presenta status, headers y body junto con la respuesta.
- La paginación usa `offset` y `limit`, con valores predeterminados 0 y 50. La página muestra `OPTIONS` para obtener metadatos del recurso.

## Operaciones de API
## Operaciones de API

### GET /currencies

**Método:** `GET`  
**Ruta:** `/currencies`  
**Autenticación:** No documentado en la fuente.

Lista monedas; el ejemplo admite `attributes=id` y `callback` para JSONP.

**Parámetros**

- `attributes` (query, opcional): Campos de respuesta a conservar.
- `callback` (query, opcional): Nombre de función para JSONP.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura incluye un ejemplo de llamada.

### GET /currencies/{CURRENCY_ID}

**Método:** `GET`  
**Ruta:** `/currencies/{CURRENCY_ID}`  
**Autenticación:** No documentado en la fuente.

Consulta datos de una moneda, por ejemplo `/currencies/ARS`.

**Parámetros**

- `CURRENCY_ID` (path, obligatorio)
- `attributes` (query, opcional): Campos de respuesta a conservar.
- `callback` (query, opcional): Nombre de función para JSONP.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura incluye un ejemplo de llamada.

### OPTIONS /currencies

**Método:** `OPTIONS`  
**Ruta:** `/currencies`  
**Autenticación:** No documentado en la fuente.

Obtiene documentación en JSON sobre el recurso de monedas.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "name",
    "description",
    "attributes"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La captura incluye un ejemplo de llamada.

### Referencia HTTP GET /currencies/ARS

**Método:** `GET`  
**Ruta:** `/currencies/ARS`  
**Autenticación:** No documentado en la fuente.

La captura muestra la solicitud GET a /currencies/ARS. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo.

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

**Fuente:** [https://developers.mercadolibre.com.co/es_co/consideraciones-de-diseno](https://developers.mercadolibre.com.co/es_co/consideraciones-de-diseno)  
**Captura:** 2026-10-08T22:53:29.373Z
