---
id: "realiza-pruebas"
title: "Realiza pruebas"
section: "Primeros pasos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/realiza-pruebas"
source_updated_at: "30/12/2025"
captured_at: "2026-10-08T22:53:35.894Z"
sha256: "623af404a28b58f26178901304d8aac550659ddbdd46a4576b4f9ac62b2c1f9b"
---

# Realiza pruebas

**Área:** Primeros pasos  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:53:35.894Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/realiza-pruebas](https://developers.mercadolibre.com.co/es_co/realiza-pruebas)

## Resumen

Mercado Libre no ofrece un sandbox: la guía recomienda probar en producción con usuarios de test, que pueden simular acciones entre sí sin cargos ni sanciones para cuentas reales. Todas las operaciones de prueba deben usar usuarios y publicaciones de test; las credenciales se reciben al crear la cuenta y deben guardarse.

## Contenido y conceptos documentados

Se necesita un access token para crear un usuario de test y el body documentado contiene `site_id`. Se recomienda crear al menos un vendedor y un comprador de prueba. La guía indica un máximo de 10 usuarios de test por cuenta, eliminación de usuarios sin actividad durante 60 días y caducidad de estas cuentas. Para las publicaciones aconseja el título “Item de Prueba - Por favor, NO OFERTAR”, usar la categoría “Otros” cuando sea posible y no utilizar los tipos `gold` ni `gold_premium`. Para compras se usan tarjetas de prueba; el nombre y apellido del titular permite simular el resultado del pago (por ejemplo, `APRO APRO` para aprobación).

## Operaciones de API
## Operaciones de API

### Consultar usuario autenticado

**Método:** `GET`  
**Ruta:** `/users/me`  
**Autenticación:** Authorization: Bearer ACCESS_TOKEN

Ejemplo de llamada a /users/me que envía el access token en el header Authorization.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente para esta llamada.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo curl con token Bearer en el header.

### Crear usuario de test

**Método:** `POST`  
**Ruta:** `/users/test_user`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea un usuario de prueba para el sitio indicado.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "site_id": "Identificador del sitio donde operará el usuario de prueba."
}
```

**Respuesta**

Respuesta de ejemplo: id, nickname, password y site_status.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El ejemplo usa site_id MLA.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/realiza-pruebas](https://developers.mercadolibre.com.co/es_co/realiza-pruebas)  
**Captura:** 2026-10-08T22:53:35.894Z
