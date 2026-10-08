---
phase: 01-inventario-y-captura
plan: 01
subsystem: documentation
tags: [mercado-libre, browser-capture, es_co, provenance]
requires: []
provides:
  - Manifiesto con 203 páginas oficiales es_co capturadas.
  - Capturas locales con contenido principal, fecha y SHA-256.
  - Auditoría clasificada de 400 enlaces internos documentales.
affects: [02-fichas-y-grafo, 03-buscador-y-mcp, 04-exportaciones]
actuals:
  tokens: 0
  tasks: 2
  commits: 0
tech-stack:
  added: [Python stdlib HTTPServer, navegador interno]
  patterns: [capturas locales ignoradas, metadatos de fuente por página]
key-files:
  created: [data/manifest.json, data/link-audit.json, data/link-audit-report.json, scripts/capture_server.py, scripts/audit_links.py]
  modified: []
key-decisions:
  - "Las capturas completas quedan en .cache/captures y no se publican en el repositorio."
  - "Variantes de locale que coinciden por slug se vinculan a la ficha es_co ya capturada."
patterns-established:
  - "Cada hecho público mantiene URL oficial, fecha de captura y huella de contenido."
requirements-completed: [DOC-01, DOC-02, DOC-03, REF-01]
coverage:
  - id: D1
    description: "Inventario y captura de páginas es_co"
    requirement: DOC-01
    verification:
      - kind: other
        ref: "data/manifest.json; comprobación de 203 filas y 203 capturas"
        status: pass
    human_judgment: false
  - id: D2
    description: "Procedencia de página y fecha por URL"
    requirement: DOC-02
    verification:
      - kind: other
        ref: "data/manifest.json y .cache/captures/{id}.json; SHA-256 comparado"
        status: pass
    human_judgment: false
  - id: D3
    description: "Auditoría de enlaces internos y exclusiones"
    requirement: DOC-03
    verification:
      - kind: other
        ref: "python scripts/audit_links.py; 400 enlaces, 0 review_required"
        status: pass
    human_judgment: false
duration: 0min
completed: 2026-10-08
status: complete
---

# Phase 1: Inventario y captura de fuentes

El manifiesto contiene 203 páginas capturadas desde el navegador interno. Cada entrada conserva su fecha de fuente cuando está publicada, la fecha de captura y su huella SHA-256; las capturas completas están en `.cache` e ignoradas por Git.

La auditoría reunió 400 referencias internas de artículos: 107 coinciden con la ruta canónica es_co, 233 coinciden con una variante de locale por slug y 60 se excluyen por ruta mal formada, marcador incompleto o alcance distinto. No quedan referencias pendientes de clasificación.

## Verificación

- Capturas completadas: 203 de 203.
- Fallos de lectura: 0.
- Enlaces sin clasificar: 0.
- Fuente oficial y fechas preservadas por página.
