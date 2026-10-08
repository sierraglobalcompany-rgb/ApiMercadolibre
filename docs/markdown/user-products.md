---
id: "user-products"
title: "User Products"
section: "Guía para productos"
subsection: "User Products"
url: "https://developers.mercadolibre.com.co/es_co/user-products"
source_updated_at: "17/06/2026"
captured_at: "2026-10-08T22:52:56.795Z"
sha256: "5310d6f53588b13eac1f0de06ab5f6fc16e9efb1d75dfe1b4c82d03fcadca59e"
---

# User Products

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 17/06/2026  
**Captura:** 2026-10-08T22:52:56.795Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/user-products](https://developers.mercadolibre.com.co/es_co/user-products)

## Resumen

Describe el modelo User Product (UP), que separa la entidad del producto de las condiciones comerciales de sus publicaciones y permite gestionar precio por variante, stock distribuido y multi-origen. La guía explica las relaciones entre ítem, UP y familia.

## Contenido y conceptos documentados

### Modelo y consultas

- Un ítem es la publicación visible; el User Product agrupa productos/variantes y la familia relaciona UPs. Los cambios de propiedades del UP enviados mediante `PUT /items` pueden propagarse de forma asíncrona a los ítems relacionados.
- Para resolver relaciones, la página indica consultar el ítem para obtener `user_product_id`, consultar el UP para `family_id`, consultar la familia del sitio y buscar ítems de un seller por `user_product_id`. El buscador puede recibir varios IDs como lista.
- La captura también señala que `child_pk` y `parent_pk` read-only no se consideran para generar la familia. Cambios/campos no detallados en esta página: No documentado en la fuente.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /categories

La fuente menciona la ruta /categories, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/categories`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Obtener user_product_id

**Método:** `GET`  
**Ruta:** `/items`  
**Autenticación:** No documentado en la fuente

Consulta un ítem para resolver el User Product asociado.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- user_product_id

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar familia de User Products

**Método:** `GET`  
**Ruta:** `/sites/$SITE_ID/user-products-families/$FAMILY_ID`  
**Autenticación:** No documentado en la fuente

Obtiene User Products asociados a una familia del sitio.

**Parámetros**

- `SITE_ID` (path, obligatorio)
- `FAMILY_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- family_id
- user_products

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Consultar User Product

**Método:** `GET`  
**Ruta:** `/user-products/$USER_PRODUCT_ID`  
**Autenticación:** No documentado en la fuente

Consulta el UP para obtener la familia a la que pertenece.

**Parámetros**

- `USER_PRODUCT_ID` (path, obligatorio)

**Solicitud**

No documentado en la fuente.

**Respuesta**

- user_product_id
- family_id
- attributes

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Buscar ítems asociados a UP

**Método:** `GET`  
**Ruta:** `/users/$SELLER_ID/items/search`  
**Autenticación:** No documentado en la fuente

Busca ítems de un seller por uno o varios identificadores de User Product.

**Parámetros**

- `SELLER_ID` (path, obligatorio)
- `user_product_id` (query, obligatorio): La página ejemplifica lista de IDs.

**Solicitud**

No documentado en la fuente.

**Respuesta**

- results
- user_product_id

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente da ejemplo con varios IDs separados por coma.

### Modificar características de User Product

**Método:** `PUT`  
**Ruta:** `/items`  
**Autenticación:** No documentado en la fuente

Modifica características de los ítems asociadas al User Product; la propagación descrita es asíncrona.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "content_type": "application/json",
  "fields": [
    "title",
    "family_name",
    "attributes"
  ]
}
```

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- No se consideran child_pk y parent_pk read_only para generar la familia.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/user-products](https://developers.mercadolibre.com.co/es_co/user-products)  
**Captura:** 2026-10-08T22:52:56.795Z
