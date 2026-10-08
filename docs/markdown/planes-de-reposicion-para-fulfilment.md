---
id: "planes-de-reposicion-para-fulfilment"
title: "Planes de reposición para fulfilment"
section: "Guía para productos"
subsection: "Mercado Envíos 2"
url: "https://developers.mercadolibre.com.co/es_co/planes-de-reposicion-para-fulfilment"
source_updated_at: "17/09/2026"
captured_at: "2026-10-08T22:52:22.464Z"
sha256: "6c547e990b1856473a070f68efcf78ed6b4ab3e820787184a83f226fcf1fd1e8"
---

# Planes de reposición para fulfilment

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 17/09/2026  
**Captura:** 2026-10-08T22:52:22.464Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/planes-de-reposicion-para-fulfilment](https://developers.mercadolibre.com.co/es_co/planes-de-reposicion-para-fulfilment)

## Resumen

El recurso entrega para un User Product información consolidada de identificación, producto, stock, ventas, beneficios y recomendación de reposición en Full. La recomendación es informativa: no reserva capacidad y el seller decide qué cantidad enviar.

## Contenido y conceptos documentados

- Requiere OAuth2 con token del seller propietario, `user_product_id` con prefijo admitido y `country` obligatorio en mayúsculas. El límite documentado es 500 solicitudes por 60 segundos por seller, variable por instancia; sobre el límite responde 429. Repeticiones idénticas frecuentes pueden causar bloqueo temporal.
- La respuesta 200 puede incluir `identifiers`, `product`, `stock`, `sales`, `recommendation` y `eligibility_benefits`; los campos dinámicos describen urgencia, cantidades exactas o rangos, períodos de ventas y tags. Si hay datos complementarios parciales, devuelve 206 y `X-Content-Missing`.
- Errores documentados: 400 `invalid_request`, 403 `access_denied`, 404 `not_found`, 429 `too_many_requests`, 500 `internal_error`, 503 `service_unavailable`.

## Operaciones de API
## Operaciones de API

### GET /marketplace/fbm/user-products/{user_product_id}/replenishment

**Método:** `GET`  
**Ruta:** `/marketplace/fbm/user-products/{user_product_id}/replenishment`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta la recomendación de reposición; requiere query `country`.

**Parámetros**

- `user_product_id` (path, obligatorio)
- `country` (query, obligatorio): Código de país de dos letras en mayúsculas.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "identifiers",
    "product",
    "stock",
    "sales",
    "recommendation",
    "eligibility_benefits",
    "X-Content-Missing"
  ],
  "summary": "La fuente documenta estructuras distintas en respuestas 200 y 206."
}
```

**Errores documentados**

- ```json {   "code": "400",   "meaning": "invalid_request: parámetros, tipos o headers inválidos." } ```
- ```json {   "code": "403",   "meaning": "access_denied: seller/caller no autorizado." } ```
- ```json {   "code": "404",   "meaning": "not_found: recurso, recomendación o vínculo inexistente." } ```
- ```json {   "code": "429",   "meaning": "too_many_requests: se excedió el límite." } ```
- ```json {   "code": "500",   "meaning": "internal_error." } ```
- ```json {   "code": "503",   "meaning": "service_unavailable." } ```

**Ejemplos**

- Ejemplo de llamada documentado en la fuente.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/planes-de-reposicion-para-fulfilment](https://developers.mercadolibre.com.co/es_co/planes-de-reposicion-para-fulfilment)  
**Captura:** 2026-10-08T22:52:22.464Z
