---
phase: 04-exportaciones-y-publicacion
subsystem: exports-refresh-publishing
tags: [mercado-libre, markdown, pdf, refresh, github]
requires: [02-fichas-y-grafo, 03-buscador-y-mcp]
provides:
  - Índice Markdown y documentos por área funcional.
  - PDF navegable con las 203 fichas y enlaces a las fuentes oficiales.
  - Flujo manual documentado de refresco y regeneración.
  - Repositorio público publicado en la rama `main` con corpus, grafo, buscador, MCP y exportaciones.
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
coverage:
  - id: X1
    description: "El índice Markdown y el PDF cubren las 203 páginas del manifiesto."
    requirement: EXP-01
    verification:
      - kind: other
        ref: "Índice/temas: 203 fichas en 11 áreas; build_pdf.py reporta 203 fichas"
        status: pass
    human_judgment: false
  - id: X2
    description: "El PDF tiene tabla navegable, marcadores y enlaces a la fuente oficial."
    requirement: EXP-02
    verification:
      - kind: other
        ref: "pypdf: 864 páginas, 225 marcadores, 410 enlaces externos; 0 entidades HTML en el texto"
        status: pass
    human_judgment: false
  - id: X3
    description: "Un refresco sin cambios conserva los artefactos generados."
    requirement: REF-01
    verification:
      - kind: other
        ref: "refresh.py: 203 unchanged; 221/221 hashes iguales antes y después"
        status: pass
    human_judgment: false
  - id: X4
    description: "El repositorio público contiene los artefactos en main y excluye capturas/entorno local."
    requirement: REF-02
    verification:
      - kind: other
        ref: "git ls-remote origin main coincide con HEAD a3941fb; 0 rutas cache/.venv staged"
        status: pass
    human_judgment: false
completed: 2026-10-08
status: complete
---

# Phase 4: Publicaciones y verificación

El Markdown y PDF cubren el mismo manifiesto de 203 páginas. El PDF generado tiene 864 páginas, 225 marcadores navegables y 410 enlaces externos a la documentación oficial. Se revisaron visualmente portada, tabla de contenidos, ficha y última página; los bloques JSON conservan su formato legible.

El refresco local clasificó las 203 capturas como sin cambio. Se calcularon hashes de 221 artefactos Markdown, JSONL, índice, grafo y PDF antes y después; todos permanecieron iguales. La publicación inicial está en `https://github.com/sierraglobalcompany-rgb/ApiMercadolibre`, rama `main`, commit `a3941fb`.
