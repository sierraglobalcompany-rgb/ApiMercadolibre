---
phase: 04-exportaciones-y-publicacion
subsystem: exports-refresh-publishing
tags: [mercado-libre, markdown, pdf, refresh, github]
requires: [02-fichas-y-grafo, 03-buscador-y-mcp]
provides:
  - Índice Markdown y documentos por área funcional.
  - PDF navegable con las 203 fichas y enlaces a las fuentes oficiales.
  - Flujo manual documentado de refresco y regeneración.
  - Repositorio público con corpus, grafo, buscador, MCP y exportaciones.
actuals:
  tokens: 0
  tasks: 3
  commits: 1
tech-stack:
  added: [ReportLab, PDF]
  patterns: [hash check before rebuild, capture cache excluded from publication]
key-files:
  created: [docs/mercadolibre-api-es-co.pdf, docs/ACTUALIZAR.md, scripts/build_pdf.py, scripts/refresh.py]
key-decisions:
  - "El repositorio publica los derivados atribuidos; las capturas HTML completas y el entorno virtual quedan locales."
requirements-completed: [EXP-01, EXP-02, EXP-03, REF-01, REF-02]
completed: 2026-10-08
status: complete
---

# Phase 4: Publicaciones y verificación

El Markdown y PDF cubren el mismo manifiesto de 203 páginas. El PDF generado tiene 864 páginas, 225 marcadores navegables y 410 enlaces externos a la documentación oficial. Se revisaron visualmente portada, tabla de contenidos, ficha y última página; los bloques JSON conservan su formato legible.

El refresco local clasificó las 203 capturas como sin cambio. Se calcularon hashes de 221 artefactos Markdown, JSONL, índice, grafo y PDF antes y después; todos permanecieron iguales. Publicación en GitHub: completar tras el push inicial.
