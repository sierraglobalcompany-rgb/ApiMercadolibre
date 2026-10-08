---
id: "publicaciones-denunciadas"
title: "Publicaciones denunciadas"
section: "Recursos de la API"
subsection: "Brand Protection Program"
url: "https://developers.mercadolibre.com.co/es_co/publicaciones-denunciadas"
source_updated_at: "26/07/2026"
captured_at: "2026-10-08T22:54:00.163Z"
sha256: "d9aecaff94f3856a6369ce45a812cabaae89cc47a1cd479b0a11d05192755617"
---

# Publicaciones denunciadas

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 26/07/2026  
**Captura:** 2026-10-08T22:54:00.163Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/publicaciones-denunciadas](https://developers.mercadolibre.com.co/es_co/publicaciones-denunciadas)

## Resumen

Describe consultas y respuestas a denuncias de propiedad intelectual asociadas a publicaciones y vendedores.

## Contenido y conceptos documentados

- GET de casos filtra por offset, fecha y estado; la tabla llama current_status al campo, aunque los ejemplos usan query status. El detalle muestra item_info, reason_id, due_date, documentos e imágenes denunciadas; is_rollbackable solo es true en ciertos estados.
- Para adjuntar evidencia, se acepta PDF, JPG o PNG de hasta 5 MB; file_name devuelto se usa como document_name en la respuesta.
- La respuesta puede incluir seller_quittance, document_name, photos_new/photos_removed y variations con picture_ids. La fuente distingue respuesta por derechos de imágenes, imágenes a reemplazar y documentación.
- Estados descritos incluyen CREATED, PENDING_MODERATION, WAITING_DOCUMENTATION, ROLLBACK, DOCUMENTATION_PRESENTED, WAITING_FOR_PATCH_PDP, DOCUMENTATION_APPROVED, DOCUMENTATION_NOT_APPROVED, DOCUMENTATION_NOT_PRESENTED, MEMBER_NOT_RESPOND y ACUERDO. Se enumeran motivos PPPI1 a PPPI23 con algunos códigos omitidos.

## Operaciones de API

## Conceptos y recursos asociados

### Estados y motivos de denuncias

La fuente lista estados y reason_id para tipos de infracción. El plazo due_date depende del caso; publicaciones pueden pausarse, reactivarse o eliminarse conforme a la respuesta y revisión.

**Ejemplos documentados**

- Reason IDs documentados incluyen PPPI1-PPPI23 con algunos saltos y ACUERDO; ejemplos de estados incluyen WAITING_DOCUMENTATION y DOCUMENTATION_APPROVED.
### Ruta mencionada /pictures

La fuente menciona la ruta /pictures, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/pictures`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Consultar detalle de denuncia

**Método:** `GET`  
**Ruta:** `/moderations/pppi/case/{case_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene denuncia, ítem, documentos e imágenes asociadas a un caso.

**Parámetros**

- `case_id` (path, obligatorio): Identificador de denuncia.

**Solicitud**

No documentado en la fuente.

**Respuesta**

case_id, current_status, item_info, reason_id, public_member_name, date_created, due_date, last_updated, is_rollbackable, documents, document_name/url, photos_denounced, photos_new, element_related_count, member_quittance, seller_quittance y user_product_ids.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET /moderations/pppi/case/37168941.

### Consultar denuncias de publicaciones

**Método:** `GET`  
**Ruta:** `/moderations/pppi/cases`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista casos por vendedor, fecha y estado de la denuncia.

**Parámetros**

- `offset` (query, obligatorio): Paginación; máximo 50 resultados por página.
- `date_created` (query, obligatorio): Fecha inicial hasta la fecha actual; se puede enviar vacía según el ejemplo.
- `status` (query, obligatorio): Estado de denuncia; ejemplo DOCUMENTATION_APPROVED. La tabla de la fuente lo nombra current_status.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Array de casos con case_id, item_id, current_status, date_created, due_date, element_related_count, reason_text, user_product_ids; incluye total, offset y limit.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- GET con offset=0, date_created y status=DOCUMENTATION_APPROVED.

### Responder denuncia

**Método:** `POST`  
**Ruta:** `/moderations/pppi/case/{case_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Envía comentario, documento o cambios de imágenes para responder a un caso.

**Parámetros**

- `case_id` (path, obligatorio): ID de denuncia.

**Solicitud**

JSON de ejemplo con seller_quittance, document_name, photos_new, photos_removed y variations (id/picture_ids) cuando hay variantes. La documentación puede ser obligatoria u opcional según el tipo de denuncia.

**Respuesta**

No documentado en la fuente.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplos sin variantes, con variaciones y respuesta solo con documento.

### Cargar archivo probatorio

**Método:** `PUT`  
**Ruta:** `/moderations/pppi/case/files`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Sube archivo PDF, JPG o PNG como evidencia para responder una denuncia.

**Parámetros**

- `case_id` (query, obligatorio): ID de denuncia.
- `name` (query, obligatorio): Nombre del archivo.
- `form` (body, obligatorio): Archivo probatorio; máximo 5 MB.

**Solicitud**

Carga multipart del archivo en el campo descrito como form.

**Respuesta**

file_name para usar luego en document_name.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- PUT con case_id, name y archivo JPG.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/publicaciones-denunciadas](https://developers.mercadolibre.com.co/es_co/publicaciones-denunciadas)  
**Captura:** 2026-10-08T22:54:00.163Z
