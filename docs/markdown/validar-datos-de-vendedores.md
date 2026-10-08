---
id: "validar-datos-de-vendedores"
title: "Validar datos de vendedores"
section: "Recursos de la API"
subsection: "Usuarios"
url: "https://developers.mercadolibre.com.co/es_co/validar-datos-de-vendedores"
source_updated_at: "30/12/2025"
captured_at: "2026-10-08T22:54:03.236Z"
sha256: "94bf5ead0243841d4bd4d1c6eeb17e9020d29c1130c173ffc5b18716aa3a64cd"
---

# Validar datos de vendedores

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 30/12/2025  
**Captura:** 2026-10-08T22:54:03.236Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/validar-datos-de-vendedores](https://developers.mercadolibre.com.co/es_co/validar-datos-de-vendedores)

## Resumen

Permite que integradores revisen si un vendedor tiene la cuenta habilitada y los datos completos para vender, recibir pagos o usar la tarjeta prepaga.

## Contenido y conceptos documentados

- GET /users/{user_id}?attributes=status permite observar permisos de operación, códigos de bloqueo y acciones requeridas.
- La fuente recomienda que la validación la realice la persona titular o el representante legal y dice que puede tardar hasta tres días hábiles. En el ejemplo, list.allow=false y rejected_by_regulations señalan que faltan datos regulatorios.

## Operaciones de API
## Operaciones de API

### Consultar estado regulatorio de vendedor

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene el estado del usuario para identificar permisos de venta, cobro y acciones regulatorias pendientes.

**Parámetros**

- `user_id` (path, obligatorio): ID del usuario.
- `attributes` (query, obligatorio): El ejemplo filtra la respuesta a status.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Objeto status con billing, buy, sell, required_action, site_status, mercado_pago, permisos list/immediate_payment y códigos asociados.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /users/123456789?attributes=status.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/validar-datos-de-vendedores](https://developers.mercadolibre.com.co/es_co/validar-datos-de-vendedores)  
**Captura:** 2026-10-08T22:54:03.236Z
