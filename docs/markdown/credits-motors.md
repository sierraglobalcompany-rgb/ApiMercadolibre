---
id: "credits-motors"
title: "Créditos pre aprobados"
section: "Guía para vehículos"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/credits-motors"
source_updated_at: "15/03/2023"
captured_at: "2026-10-08T22:53:14.542Z"
sha256: "7e30d34a525774ad2d262e6c2f7c425afabc37490315c731b945dd109542c28e"
---

# Créditos pre aprobados

**Área:** Guía para vehículos  
**Actualización indicada por la fuente:** 15/03/2023  
**Captura:** 2026-10-08T22:53:14.542Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/credits-motors](https://developers.mercadolibre.com.co/es_co/credits-motors)

## Resumen

Describe las notificaciones de nuevos leads de crédito, la consulta de créditos disponibles para ítems del vendedor y el detalle de una propuesta. La funcionalidad aplica a vehículos en Brasil e inmuebles en Chile.

## Contenido y conceptos documentados

- La búsqueda puede filtrar por `item_id`, `status` (`approved`, `rejected`, `in_analysis`, `all`) y `financial_entity_id` (`MERCADO_PAGO`, `VOTORANTIM`, `SANTANDER`, `SCOTIA`). Si no se indica status, la fuente indica que devuelve los aprobados.
- El resumen incluye `id`, `item_id`, anticipo y cuotas, seller/buyer, entidad, fecha y `expired`; `proposal_id` depende de que la entidad financiera lo publique. El detalle puede incluir `buyer.full_name`, email y teléfono.
- Para datos de prueba se documenta `x-sandbox: true`. Errores incluyen 401 sin token y 400 por seller distinto al token, fechas inválidas/rango mayor a tres meses, entidad o ítem inválidos.

## Operaciones de API
## Operaciones de API

### GET /vis/loans/{CREDIT_ID}

**Método:** `GET`  
**Ruta:** `/vis/loans/{CREDIT_ID}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el detalle del crédito y los datos de contacto disponibles del comprador.

**Parámetros**

- `CREDIT_ID` (path, obligatorio)
- `seller_id` (query, obligatorio): Vendedor del token

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "id",
    "item_id",
    "buyer.id",
    "buyer.full_name",
    "buyer.email",
    "buyer.phone",
    "status"
  ]
}
```

**Errores documentados**

- ```json {   "code": "401",   "meaning": "Unauthorized: falta access token." } ```
- ```json {   "code": "400",   "meaning": "Seller no coincide con el token o CREDIT_ID no tiene formato UUID." } ```
- ```json {   "code": "404",   "meaning": "No se encontró el detalle del crédito." } ```
- ```json {   "code": "410",   "meaning": "El crédito expiró." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

### GET /vis/loans/search

**Método:** `GET`  
**Ruta:** `/vis/loans/search`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Busca créditos disponibles para los ítems del vendedor.

**Parámetros**

- `seller_id` (query, obligatorio): ID vendedor
- `date_from` (query, obligatorio): Fecha inicial ISO
- `date_to` (query, obligatorio): Fecha final ISO; rango máximo tres meses
- `item_id` (query, opcional): Ítem
- `status` (query, opcional): approved, rejected, in_analysis o all; default approved
- `financial_entity_id` (query, opcional): MERCADO_PAGO, VOTORANTIM, SANTANDER o SCOTIA

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "results",
    "id",
    "item_id",
    "down_payment_amount",
    "installments_number",
    "installments_amount",
    "seller_id",
    "buyer_id",
    "proposal_id",
    "date_created",
    "financial_entity_id",
    "expired",
    "paging"
  ]
}
```

**Errores documentados**

- ```json {   "code": "401",   "meaning": "Unauthorized: falta access token." } ```
- ```json {   "code": "400",   "meaning": "Seller no coincide con el token; fecha inválida o rango mayor a tres meses; entidad financiera o item inválidos." } ```

**Ejemplos**

- La captura contiene ejemplo de llamada para este recurso.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/credits-motors](https://developers.mercadolibre.com.co/es_co/credits-motors)  
**Captura:** 2026-10-08T22:53:14.542Z
