# Phase 2 Context — Fichas normalizadas y grafo

## 1. Domain

Convertir 203 capturas públicas `es_co` en fichas concisas, registros JSONL de conceptos/operaciones y un grafo Graphify con fuente trazable por relación.

## 2. Decisions

- El portal oficial capturado en navegador es la autoridad factual; no completar campos ausentes por inferencia.
- Mantener los resúmenes en español y evitar reproducir pasajes extensos.
- Cada operación va en una fila JSONL por método/ruta; un concepto conserva una página sin operación HTTP concreta.
- Los registros deben incluir `page_id`, URL, fecha de fuente, captura y SHA-256.
- Graphify 0.9.55 corre en `.venv`, con la dependencia opcional MCP; no alterar la instalación global.

## 3. Canonical references

- `.planning/PROJECT.md`
- `.planning/REQUIREMENTS.md`
- `.planning/ROADMAP.md`
- `AGENTS.md`
- `data/manifest.json`
- `.cache/captures/{id}.json` (fuente local ignorada; se usa durante la extracción)
- `docs/markdown/{id}.md`
- `data/extracted/batch-*.jsonl`

## 4. Code context

- `scripts/merge_extractions.py` une las salidas por lote y comprueba referencias de fuente.
- `scripts/build_markdown.py` renderiza parámetros, requests, responses, errores y ejemplos desde el JSONL.
- `scripts/validate_corpus.py` verificará integridad de fichas, capturas y registros.
- `graphify-out/` debe contener grafo, visualización y reporte; nunca incluir `.cache/captures`.

## 5. Specifics

- Tipos de registro válidos: `operation` y `concept`.
- Los campos técnicos ausentes usan `null` o listas vacías; las fichas declaran “No documentado en la fuente”.
- Las relaciones del grafo deben distinguir EXTRACTED, INFERRED y AMBIGUOUS, con URL oficial de origen.

## 6. Deferred

La UI de búsqueda, configuración MCP para clientes, PDF, actualización manual y publicación se completan en las fases 3 y 4.
