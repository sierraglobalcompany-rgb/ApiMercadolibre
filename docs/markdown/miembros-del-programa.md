---
id: "miembros-del-programa"
title: "Miembros del Programa"
section: "Recursos de la API"
subsection: "Brand Protection Program"
url: "https://developers.mercadolibre.com.co/es_co/miembros-del-programa"
source_updated_at: "26/07/2026"
captured_at: "2026-10-08T22:53:51.200Z"
sha256: "2608bfdc8d390119a26de60a361b0bcdb7ecf00b6ffbc9a111f72d0d01b10c01"
---

# Miembros del Programa

**Área:** Recursos de la API  
**Actualización indicada por la fuente:** 26/07/2026  
**Captura:** 2026-10-08T22:53:51.200Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/miembros-del-programa](https://developers.mercadolibre.com.co/es_co/miembros-del-programa)

## Resumen

La página describe el flujo de Brand Protection Program (BPP) para que titulares de derechos o representantes autorizados consulten motivos habilitados, denuncien publicaciones y respondan a la documentación presentada por el vendedor. Su uso está restringido a miembros del programa.

## Contenido y conceptos documentados

Los motivos de denuncia tienen IDs, grupo, tipo y descripciones; el ejemplo incluye falsificación, uso ilegal de marca, libros, imágenes y otros derechos. Una denuncia devuelve un `denounce_id`; su consulta incluye estado, motivo, publicación, vendedor, fechas y documentos. La guía enumera estados desde `CREATED` hasta aprobación, rechazo o descarte. El vendedor dispone de 3 días (excepto domingos) para responder; el miembro tiene luego 3 días corridos. Solo se responde un caso en `DOCUMENTATION_PRESENTED`; para aprobar se envía `documentation_approved: "true"`, y para rechazar, `"false"` más `reject_member_id` tomado de `reject_option_member`.

## Operaciones de API

## Conceptos y recursos asociados

### Flujo de Brand Protection Program

Resume estados, plazos y restricción de uso del proceso de denuncias de propiedad intelectual.

**Respuesta**

No documentado en la fuente.

**Ejemplos documentados**

- Uso exclusivo de miembros; el vendedor dispone de 3 días excepto domingos y el miembro tiene 3 días corridos para responder.
## Operaciones de API

### Consultar caso de denuncia BPP

**Método:** `GET`  
**Ruta:** `/moderations/pppi/case/{denounce_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Obtiene estado, datos de ítem y vendedor, fechas y documentos del caso.

**Parámetros**

- `denounce_id` (path, obligatorio): ID de la denuncia.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Incluye item_info, last_updated, documents, reason_id/text, current_status, seller_id y datos de miembros.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

No documentado en la fuente.

### Denunciar publicación BPP

**Método:** `POST`  
**Ruta:** `/moderations/pppi/denounces/items/{item_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Crea una denuncia de propiedad intelectual contra una publicación.

**Parámetros**

- `item_id` (path, obligatorio): ID del ítem denunciado.

**Solicitud**

```json
{
  "report_reason_id": "ID de motivo habilitado.",
  "comment": "Comentario de la denuncia."
}
```

**Respuesta**

Respuesta con status y denounce_id.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- El ejemplo devuelve status 201.

### Consultar motivos de denuncia BPP

**Método:** `GET`  
**Ruta:** `/moderations/pppi/denounces/{site_id}/ITM/options`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Lista los motivos de denuncia que el miembro tiene habilitados para ítems del sitio.

**Parámetros**

- `site_id` (path, obligatorio): ID del sitio, por ejemplo MLA.

**Solicitud**

No documentado en la fuente.

**Respuesta**

Lista de motivos con id, group, type y descripciones/textos por idioma.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Disponible solo para miembros del Brand Protection Program.

### Responder documentación de caso BPP

**Método:** `POST`  
**Ruta:** `/moderations/pppi/case/{denounce_id}`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Aprueba o rechaza la documentación presentada por el vendedor en una denuncia.

**Parámetros**

- `denounce_id` (path, obligatorio): ID de la denuncia.

**Solicitud**

```json
{
  "documentation_approved": "true para aprobar; false para rechazar.",
  "member_quittance": "Texto o null.",
  "reject_member_id": "ID de motivo de rechazo obtenido en reject_option_member; usado al rechazar."
}
```

**Respuesta**

Respuesta del caso con current_status y datos de la denuncia, incluida la lista reject_option_member.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Solo se responde cuando el caso está en DOCUMENTATION_PRESENTED.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/miembros-del-programa](https://developers.mercadolibre.com.co/es_co/miembros-del-programa)  
**Captura:** 2026-10-08T22:53:51.200Z
