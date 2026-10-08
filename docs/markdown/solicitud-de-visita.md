---
id: "solicitud-de-visita"
title: "Solicitud de visita"
section: "Guía para inmuebles"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/solicitud-de-visita"
source_updated_at: "08/11/2025"
captured_at: "2026-10-08T22:50:51.129Z"
sha256: "d58a94954242e455352efe419fdfdb82d638e0ecc884b3d76314b12f951fd290"
---

# Solicitud de visita

**Área:** Guía para inmuebles  
**Actualización indicada por la fuente:** 08/11/2025  
**Captura:** 2026-10-08T22:50:51.129Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/solicitud-de-visita](https://developers.mercadolibre.com.co/es_co/solicitud-de-visita)

## Resumen

La guía explica cómo habilitar y gestionar solicitudes de visita para publicaciones inmobiliarias. La funcionalidad descrita está disponible en Chile (MLC) y requiere una cuenta inmobiliaria/profesional, autorización, publicaciones con CONTACT_SCHEDULE y configuración del tópico de notificaciones VIS Leads.

## Contenido y conceptos documentados

- Las notificaciones de solicitudes usan el topic vis_leads y la acción visit_request; incluyen recurso, usuario, aplicación, fechas de envío/recepción e intentos.
- La agenda se genera desde la experiencia del sitio; la fuente dice que no existe endpoint API para crear agendas directamente. El vendedor puede recuperar el detalle del lead/schedule con su LEAD_ID.
- La publicación puede perder la opción automáticamente ante disminución de reputación, cancelación de más del 50 % de visitas o republicación de anuncios existentes.

## Operaciones de API

## Conceptos y recursos asociados

### Flujo y notificaciones de solicitudes de visita

Requiere cuenta inmobiliaria/profesional, token, publicación con CONTACT_SCHEDULE y notificaciones VIS Leads; agenda se gestiona en el sitio, no mediante creación directa por API.
## Operaciones de API

### Obtener detalle de solicitud de visita

**Método:** `GET`  
**Ruta:** `/vis/leads/$LEAD_ID`  
**Autenticación:** Authorization: Bearer $ACCESS_TOKEN

Recupera una agenda usando el ID de lead de visita recibido por VIS Leads.

**Parámetros**

- `LEAD_ID` (path, obligatorio): ID del lead/schedule.

**Solicitud**

No documentado en la fuente.

**Respuesta**

id, item_id, created_at, contact_type, external_id, status, buyer_id y datos del comprador disponibles.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página dice que no existe endpoint API para crear agendas directamente. La disponibilidad descrita es MLC.
- Topic vis_leads y acción visit_request.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/solicitud-de-visita](https://developers.mercadolibre.com.co/es_co/solicitud-de-visita)  
**Captura:** 2026-10-08T22:50:51.129Z
