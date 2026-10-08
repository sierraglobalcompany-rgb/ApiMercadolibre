# Phase 3 Context — Buscador local y MCP

## 1. Domain

Exponer el mismo corpus normalizado a desarrolladores y asistentes de IA mediante búsqueda local en navegador y Graphify MCP por stdio.

## 2. Decisions

- No usar API remota ni base de datos alojada.
- El buscador carga un JSON generado localmente y tolera diferencias de mayúsculas, acentos y puntuación.
- Cada resultado enlaza su ficha Markdown, fuente oficial, sección y fechas.
- Graphify MCP opera sobre el grafo local y responde con nodos/relaciones con referencias.

## 3. Canonical references

- `.planning/PROJECT.md`, `.planning/REQUIREMENTS.md`, `.planning/ROADMAP.md`
- `data/manifest.json`, `data/operations.jsonl`, `web/search-index.json`
- `graphify-out/graph.json`, `mcp-config.example.json`

## 4. Code context

- `web/index.html`, `web/app.js`, `web/styles.css`
- `scripts/build_index.py`, `scripts/serve_search.py`
- `docs/MCP.md`

## 5. Specifics

- Buscar por término, función/recurso, método HTTP y ruta.
- Mostrar fragmento coincidente y enlace a la fuente oficial.
- Servir solo rutas explícitamente autorizadas desde `scripts/serve_search.py`.
- La configuración MCP debe apuntar al Python del entorno virtual y al `graph.json` local.

## 6. Deferred

El PDF único, los índices temáticos, el comando de refresco y la publicación final se completan en la fase 4.
