---
id: "pasos-rapidos-para-publicar-un-inmueble-de-prueba"
title: "Pasos rápidos para publicar un inmueble de prueba"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/pasos-rapidos-para-publicar-un-inmueble-de-prueba"
source_updated_at: "05/01/2026"
captured_at: "2026-10-08T22:50:47.235Z"
sha256: "a15d79fa35c95ccebbbfb9eaac060d3f4a7cd4c7c9bf0fac865c3ef95252f80f"
---

# Pasos rápidos para publicar un inmueble de prueba

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 05/01/2026  
**Captura:** 2026-10-08T22:50:47.235Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/pasos-rapidos-para-publicar-un-inmueble-de-prueba](https://developers.mercadolibre.com.co/es_co/pasos-rapidos-para-publicar-un-inmueble-de-prueba)

## Resumen

La guía recorre la puesta en marcha de una cuenta de pruebas inmobiliaria: crear el usuario de prueba, registrarlo como empresa inmobiliaria y solicitar su activación, obtener credenciales/tokens, validar la cuenta, activar un paquete y publicar un inmueble para luego consultar su estado.

## Contenido y conceptos documentados

- La fuente recomienda realizar las pruebas con un usuario de prueba y verificar /users/me antes de publicar.
- El flujo publica con POST /items y usa el ID devuelto para GET /items/$ITEM_ID.
- Se remite a las guías de token, configuración de usuario, paquetes y publicación inmobiliaria para los requisitos que dependen de la cuenta.

## Operaciones de API

## Conceptos y recursos asociados

### Flujo para publicar inmueble de prueba

El recorrido incluye crear usuario de prueba, registrarlo y activarlo como inmobiliaria, obtener token, validar cuenta, activar paquete, publicar y consultar el ítem.
## Operaciones de API

### Consultar publicación de prueba

**Método:** `GET`  
**Ruta:** `/items/$ITEM_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Verifica el estado con el identificador devuelto por POST /items.

**Parámetros**

- `ITEM_ID` (path, obligatorio): ID recibido al publicar.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Detalle de publicación para verificar estado.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Publicar inmueble de prueba

**Método:** `POST`  
**Ruta:** `/items`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una publicación de prueba con el JSON inmobiliario tras configurar y habilitar la cuenta.

**Parámetros**

- `body` (body, obligatorio): JSON con title, category_id, price, currency_id, available_quantity, buying_mode, listing_type_id, condition, description, location, pictures, attributes y seller_contact.

**Solicitud**

JSON de publicación inmobiliaria.

**Respuesta**

La respuesta proporciona el ID del ítem para consultar su estado.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Realizar las pruebas con usuario de prueba.

### Consultar usuario autenticado

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Valida que el token corresponde al usuario de prueba configurado.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Datos del usuario autenticado; verificar coincidencia con la cuenta de prueba.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/pasos-rapidos-para-publicar-un-inmueble-de-prueba](https://developers.mercadolibre.com.co/es_co/pasos-rapidos-para-publicar-un-inmueble-de-prueba)  
**Captura:** 2026-10-08T22:50:47.235Z
