---
id: "recuperacion-reputacion"
title: "Programa de Despegue y Beneficio de Reputación"
section: "Guía para productos"
subsection: "Métricas y Tendencias"
url: "https://developers.mercadolibre.com.co/es_co/recuperacion-reputacion"
source_updated_at: "04/02/2025"
captured_at: "2026-10-08T22:52:35.924Z"
sha256: "89700639130ce1e25f77e868ffcbaf05445e694fc267117f7662b311947cbf2f"
---

# Programa de Despegue y Beneficio de Reputación

**Área:** Guía para productos  
**Actualización indicada por la fuente:** 04/02/2025  
**Captura:** 2026-10-08T22:52:35.924Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/recuperacion-reputacion](https://developers.mercadolibre.com.co/es_co/recuperacion-reputacion)

## Resumen

Documenta consulta, activación, cancelación y descarga de documentos de los programas NEWBIE_GRNTEE y RECOVERY_GRNTEE. Están dirigidos a vendedores sin reputación o con nivel rojo, naranja o amarillo en MLA, MLB, MLM, MLC y MCO; los niveles verdes están excluidos. El programa congela temporalmente el nivel de reputación y opera con una garantía.

## Contenido y conceptos documentados

- GET seller_recovery/status expone disponibilidad/estado, límites de problemas y días, importe de garantía y Ads, fechas de protección y ventas/reclamos/cancelaciones/demoras. El límite de rate documentado es 100 RPM por user_id.
- Para activar, el vendedor debe tener saldo suficiente en Mercado Pago para la garantía; al hacer opt-in comienza el periodo de protección. La cancelación usa cancellation_reason con valores business_not_ready, program_not_useful, need_money, goal_achieved y without_reason.
- La descarga legal es obligatoria para México y Colombia. type=preview se permite cuando status=AVAILABLE y garantía OFF; type=complete requiere protección ACTIVE o FINISHED_BY_*. La respuesta documentada contiene PDF codificado en base64.
- La página recomienda usar /communications/notices para informar al vendedor de invitaciones; no detalla aquí método HTTP ni URL completa para esa referencia.

En los ejemplos de la fuente se usa `Authorization: Bearer Token`.

## Operaciones de API

## Conceptos y recursos asociados

### Ruta mencionada /communications/notices

La fuente menciona la ruta /communications/notices, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa.

**Ruta mencionada:** `/communications/notices`  
**Método HTTP:** No documentado en la fuente.

**Ejemplos documentados**

- La referencia de método y ruta se encontró en el texto capturado de la página.
## Operaciones de API

### Descargar documento legal

**Método:** `GET`  
**Ruta:** `/users/reputation/seller_recovery/legal-document`  
**Autenticación:** Authorization: Bearer Token

Descarga versión preliminar o completa de la domiciliación legal.

**Parámetros**

- `type` (query, obligatorio): PREVIEW o COMPLETE; condiciones dependen de status y garantía.

**Solicitud**

No documentado en la fuente.

**Respuesta**

document codificado en base64 que representa un PDF.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La página muestra ejemplo de decodificación Base64.

### Consultar programa y garantía

**Método:** `GET`  
**Ruta:** `/users/reputation/seller_recovery/status`  
**Autenticación:** Authorization: Bearer Token

Obtiene disponibilidad, estado, límites, garantía, protección y beneficios asociados.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

seller_id, current_level, status, type, site_id, protection_limits, guarantee_limits, guarantee_detail, protection_detail y sales_detail.

**Errores documentados**

- Límite de 100 RPM por vendedor (user_id).

**Ejemplos**

- Respuesta con AVAILABLE, límites y guarantee_status OFF.

### Consultar reputación del vendedor

**Método:** `GET`  
**Ruta:** `/users/{user_id}`  
**Autenticación:** Authorization: Bearer Token

Lee seller_reputation para verificar elegibilidad preliminar.

**Parámetros**

- `user_id` (path, obligatorio): Identificador o valor señalado en la ruta por la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

seller_reputation.level_id, power_seller_status y transactions.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- La fuente excluye niveles verdes 4_light_green y 5_green.

### Activar programa

**Método:** `POST`  
**Ruta:** `/users/reputation/seller_recovery/activate`  
**Autenticación:** Authorization: Bearer Token

Realiza opt-in para iniciar periodo de protección.

**Parámetros**

No documentado en la fuente.

**Solicitud**

No documentado en la fuente.

**Respuesta**

message=ok.

**Errores documentados**

- Error si el vendedor no tiene disponible el dinero de garantía en Mercado Pago.

**Ejemplos**

- Ejemplo de activación.

### Cancelar programa

**Método:** `PUT`  
**Ruta:** `/users/reputation/seller_recovery/cancel_guarantee`  
**Autenticación:** Authorization: Bearer Token

Solicita cancelación del programa con motivo.

**Parámetros**

- `cancellation_reason` (body, obligatorio): Motivo obligatorio para Programa de Despegue; la fuente dice que no se requiere para Recovery Color.

**Solicitud**

cancellation_reason: business_not_ready, program_not_useful, need_money, goal_achieved o without_reason.

**Respuesta**

message=ok.

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- Ejemplo cancellation_reason=goal_achieved.

**Fuente:** [https://developers.mercadolibre.com.co/es_co/recuperacion-reputacion](https://developers.mercadolibre.com.co/es_co/recuperacion-reputacion)  
**Captura:** 2026-10-08T22:52:35.924Z
