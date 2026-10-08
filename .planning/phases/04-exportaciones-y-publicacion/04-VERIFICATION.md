---
phase: 04-exportaciones-y-publicacion
verified: 2026-10-08T23:58:00Z
status: passed
score: 5/5 must-haves verified
behavior_unverified: 0
---

# Verificación — Phase 4: Exportaciones y refresco

| Criterio | Resultado | Evidencia |
|---|---:|---|
| Índice Markdown por área | PASS — 11 áreas; 203 fichas | `docs/markdown/INDEX.md`, `docs/temas/` |
| PDF con cobertura y navegación | PASS — 864 páginas, 225 marcadores, 410 enlaces | `docs/mercadolibre-api-es-co.pdf`, inspección con pypdf y render de páginas |
| PDF con código legible | PASS — 0 entidades HTML en texto extraído | Verificación del texto PDF y render final |
| Refresco sin cambios conserva los derivados | PASS — 203 sin cambio; hashes idénticos 221/221 | `data/refresh-report.json`; hashes temporales en `.cache` |
| Archivos locales excluidos | PASS | `.gitignore` cubre `.cache/`, `.venv/` y cachés Graphify |
