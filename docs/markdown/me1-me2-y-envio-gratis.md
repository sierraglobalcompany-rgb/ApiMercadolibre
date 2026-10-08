---
id: "me1-me2-y-envio-gratis"
title: "ME1 / ME2 y envío gratis"
section: "FAQs"
subsection: null
url: "https://developers.mercadolibre.com.co/es_co/me1-me2-y-envio-gratis"
source_updated_at: "14/08/2026"
captured_at: "2026-10-08T22:50:02.383Z"
sha256: "45e21fce635e65ae6bf2ffe32dba92857010e5e462812b3e384b65fa3542cfb5"
---

# ME1 / ME2 y envío gratis

**Área:** FAQs  
**Actualización indicada por la fuente:** 14/08/2026  
**Captura:** 2026-10-08T22:50:02.383Z
**Fuente oficial:** [https://developers.mercadolibre.com.co/es_co/me1-me2-y-envio-gratis](https://developers.mercadolibre.com.co/es_co/me1-me2-y-envio-gratis)

## Resumen

Aclara cómo ME1/ME2, preferencias de cuenta y elegibilidad del mercado afectan envío gratis.

## Contenido y conceptos documentados

- La guía atribuye beneficios automáticos principalmente a ME2 y señala que no se puede forzar envío gratis nacional solo por API.

## Operaciones de API

## Conceptos y recursos asociados

### ME1 / ME2 y envío gratis

Aclara cómo ME1/ME2, preferencias de cuenta y elegibilidad del mercado afectan envío gratis.
## Operaciones de API

### Actualizar modo de envío

**Método:** `PUT`  
**Ruta:** `/items`  
**Autenticación:** No documentado en la fuente.

Ejemplo shipping.mode=me1; preferencias de cuenta pueden prevalecer.

**Parámetros**

No documentado en la fuente.

**Solicitud**

```json
{
  "fields": [
    "shipping.mode",
    "free_shipping"
  ]
}
```

**Respuesta**

```json
{
  "fields": [
    "logistic_type"
  ]
}
```

**Errores documentados**

No documentado en la fuente.

**Ejemplos**

- {"shipping":{"mode":"me1"},"free_shipping":true

**Fuente:** [https://developers.mercadolibre.com.co/es_co/me1-me2-y-envio-gratis](https://developers.mercadolibre.com.co/es_co/me1-me2-y-envio-gratis)  
**Captura:** 2026-10-08T22:50:02.383Z
