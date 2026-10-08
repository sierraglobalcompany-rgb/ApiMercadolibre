---
id: "competencia-en-catalogo"
title: "Competencia"
section: "Guía para productos"
subsection: "Catálogo"
url: "https://developers.mercadolibre.com.co/es_co/competencia-en-catalogo"
source_updated_at: "21/07/2026"
captured_at: "2026-10-08T22:51:22.908Z"
sha256: "2e49c4e78022f3899289fcc40cbfd633f049b320c255076b82f66a917c6e22bc"
---

# Competencia

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 21/07/2026  
**Captura:** 2026-10-08T22:51:22.908Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/competencia-en-catalogo](https://developers.mercadolibre.com.co/es_co/competencia-en-catalogo)

## Resumen

Describe cómo consultar la posición competitiva de una publicación en una página de producto de catálogo y el precio sugerido para competir. La respuesta identifica estados, motivos y datos de la publicación ganadora.

## Contenido y conceptos documentados

- La consulta se realiza por `item_id`; la guía muestra `version=v2`.
- Los estados ejemplificados incluyen `winning`, `competing`, `sharing_first_place` y `listed`. `boosts` describe oportunidades/beneficios; cada boost puede tener estado `boosted`, `not_boosted`, `opportunity` o `not_apply`.
- `price_to_win` expresa el precio sugerido en la moneda de la publicación. La fuente señala que al actualizar el precio del ítem con ese valor, la publicación puede ser más competitiva.
- La respuesta también puede identificar `catalog_product_id` y datos acotados de la publicación ganadora. La página menciona notificaciones ante cambios de estado.

**Campos y respuestas:** `item_id`, `current_price`, `currency_id`, `price_to_win`, `boosts`, `status`, `consistent`, `visit_share`, `competitors_sharing_first_place`, `reason`, `catalog_product_id` y `winner`.

**Ejemplos documentados:** publicación perdiendo/ganando, compartiendo el primer lugar y publicación listada sin competir.

## Operaciones de API

## Conceptos y recursos asociados

### Competencia

Describe cómo consultar la posición competitiva de una publicación en una página de producto de catálogo y el precio sugerido para competir. La respuesta identifica estados, motivos y datos de la publicación ganadora.

**Respuesta**

```json
{
  "fields": "`item_id`, `current_price`, `currency_id`, `price_to_win`, `boosts`, `status`, `consistent`, `visit_share`, `competitors_sharing_first_place`, `reason`, `catalog_product_id` y `winner`."
}
```

**Ejemplos documentados**

- publicación perdiendo/ganando, compartiendo el primer lugar y publicación listada sin competir.
### Ruta mencionada /products/{product_id}

La fuente menciona la ruta /products/{product_id}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/products/{product_id}`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consulta el estado competitivo, las razones y el precio sugerido; la guía muestra `version=v2`

**Método:** `GET`  
**Ruta:** `/items/{item_id}/price_to_win`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Consulta el estado competitivo, las razones y el precio sugerido; la guía muestra `version=v2`.

**Parámetros**

- `item_id` (path, obligatorio): Variable de ruta documentada.
- `version` (query): La guía muestra version=v2.

**Solicitud**

No documentado en la fuente.

**Respuesta**

```json
{
  "fields": [
    "item_id",
    "current_price",
    "currency_id",
    "price_to_win",
    "boosts",
    "status",
    "consistent",
    "visit_share",
    "competitors_sharing_first_place",
    "reason",
    "catalog_product_id",
    "winner"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- publicación perdiendo/ganando, compartiendo el primer lugar y publicación listada sin competir.

### Aplicar el precio sugerido

**Método:** `PUT`  
**Ruta:** `/items`  
**Autenticación:** No documentado en la fuente.

La fuente indica enviar el precio sugerido mediante PUT al recurso /items para mejorar la competitividad; la ruta detallada no está especificada.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente lo describe como el paso posterior a consultar price_to_win.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/competencia-en-catalogo](https://developers.mercadolibre.com.co/es_co/competencia-en-catalogo)  
**Captura:** 2026-10-08T22:51:22.908Z
