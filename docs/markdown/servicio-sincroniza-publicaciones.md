---
id: "servicio-sincroniza-publicaciones"
title: "Sincroniza publicaciones"
section: "Guía para servicios"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/servicio-sincroniza-publicaciones"
source_updated_at: "15/03/2023"
captured_at: "2026-10-08T22:53:10.446Z"
sha256: "897f252f6ceaf8af99a34bbe39560f4bd77da8d45b1d972b38de528811fc3d54"
---

# Sincroniza publicaciones

**Área:** Guía para servicios  
**Actualización indicada por la fuente:** 15/03/2023  
**Captura:** 2026-10-08T22:53:10.446Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/servicio-sincroniza-publicaciones](https://developers.mercadolibre.com.co/es_co/servicio-sincroniza-publicaciones)

## Resumen

Explica cómo mantener una publicación activa sincronizada con otros sistemas mediante cambios permitidos de contenido, precio, stock o estado.

## Contenido y conceptos documentados

- Los campos modificables dependen de ventas y estado; la página enumera title, available_quantity, price, video, pictures, description, shipping y category en su contexto. La descripción se agrega con POST.
- Con ventas no se pueden modificar condition, buying mode, métodos de pago distintos de Mercado Pago, dimensiones de envío ni warranty. El título tiene restricción adicional y el tipo de publicación solo se cambia una vez.
- Los estados se envían en minúscula: paused impide el contacto, closed finaliza y no se reactiva (puede republicarse), active reactiva un ítem pausado. Para eliminar, primero cierra y luego envía deleted=true; si aparece 409 optimistic_locking conflict, espera unos segundos antes de repetir.

## Operaciones de API
## Operaciones de API

### Actualizar publicación

**Método:** `PUT`  
**Ruta:** `/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Actualiza campos editables, estado, inventario o eliminación mediante PUT al recurso del ítem; las restricciones dependen de ventas y estado.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem.

**Solicitud**

Ejemplos: title y price; status=paused/closed; deleted=true tras cerrar; available_quantity. La página enumera title, available_quantity, price, video, pictures, description (solo agregar un post), shipping y category como editables en su contexto.

**Respuesta**

200 OK indicado en la actualización de título/precio; otras estructuras no documentadas.

**Errores documentados**

- ```json {   "status": 409,   "code": "optimistic_locking error: conflict",   "meaning": "El segundo PUT de eliminación puede tener conflicto; la fuente indica esperar unos segundos hasta actualizar la información." } ```

**Ejemplos**

- PUT /items/ITEM_ID para título/precio, estado y stock; eliminación requiere primero status=closed y luego deleted=true.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/servicio-sincroniza-publicaciones](https://developers.mercadolibre.com.co/es_co/servicio-sincroniza-publicaciones)  
**Captura:** 2026-10-08T22:53:10.446Z
