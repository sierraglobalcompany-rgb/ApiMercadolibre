---
id: "configuracion-o-requisitos-previos"
title: "Configuración o requisitos previos"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/configuracion-o-requisitos-previos"
source_updated_at: "06/11/2025"
captured_at: "2026-10-08T22:50:33.208Z"
sha256: "0807ae45cf9523e21819f623368f6aaae2df6b19be717bc3c89ffa7fc5f6d677"
---

# Configuración o requisitos previos

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 06/11/2025  
**Captura:** 2026-10-08T22:50:33.208Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/configuracion-o-requisitos-previos](https://developers.mercadolibre.com.co/es_co/configuracion-o-requisitos-previos)

## Resumen

Guía inicial para cuenta, aplicación, credenciales, token y primera petición.

## Contenido y conceptos documentados

- La prueba GET /users/me debe retornar HTTP 200; se recomienda continuar con usuario test.

## Operaciones de API

## Conceptos y recursos asociados

### Configuración o requisitos previos

Guía inicial para cuenta, aplicación, credenciales, token y primera petición.
## Operaciones de API

### Comprobar token

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Retorna usuario asociado al token; la guía espera HTTP 200.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "datos del usuario"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/configuracion-o-requisitos-previos](https://developers.mercadolibre.com.co/es_co/configuracion-o-requisitos-previos)  
**Captura:** 2026-10-08T22:50:33.208Z
