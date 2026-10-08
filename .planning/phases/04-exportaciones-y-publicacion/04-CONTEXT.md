# Phase 4 Context — Exportaciones y publicación

## 1. Domain

Generar las vistas Markdown, el PDF único y el índice desde la fuente normalizada; proporcionar un refresco manual trazable y publicar el corpus en el repositorio público indicado.

## 2. Decisions

- El Markdown y el PDF comparten las mismas fichas y operaciones.
- El PDF incluye tabla de contenidos enlazada, referencias oficiales y fechas por página.
- La actualización es manual; compara hashes y regenera derivados del corpus cambiado.
- El repositorio público recibe resúmenes con redacción propia y atribución, nunca las capturas extensas.

## 3. Canonical references

- `.planning/PROJECT.md`, `.planning/REQUIREMENTS.md`, `.planning/ROADMAP.md`
- `data/manifest.json`, `data/operations.jsonl`, `docs/markdown/`
- `data/link-audit-report.json`, `graphify-out/graph.json`
- `https://github.com/sierraglobalcompany-rgb/ApiMercadolibre`

## 4. Code context

- `scripts/build_markdown.py`, `scripts/build_pdf.py`, `scripts/refresh.py`
- `docs/ACTUALIZAR.md`, `docs/MCP.md`, `README.md`

## 5. Specifics

- PDF en `docs/mercadolibre-api-es-co.pdf`.
- Índice raíz en `docs/markdown/INDEX.md`; un documento temático por área.
- Capturas `.cache/` y el entorno `.venv/` deben permanecer excluidos de Git.
- El repo remoto ya fue seleccionado por el usuario como destino público del resultado.

## 6. Deferred

No hay publicación automatizada; el envío inicial al repositorio se realiza al completar la auditoría local.
