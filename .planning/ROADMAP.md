# Roadmap: Base de consulta de la API de Mercado Libre

## Milestone 1 — Corpus consultable `es_co`

### Phase 1 — Inventario y captura de fuentes

**Status:** Complete — verified in `.planning/phases/01-inventario-y-captura/01-VERIFICATION.md`.

**Goal:** Tener un manifiesto trazable de las páginas oficiales `es_co` y capturas accesibles desde el navegador interno.

**Requirements:** DOC-01, DOC-02, DOC-03, REF-01

**Success criteria:**
- El manifiesto normaliza y deduplica las URLs oficiales descubiertas en el índice.
- Cada entrada indica sección, título, URL canónica, fecha de captura, fecha publicada si existe, huella y estado.
- Las páginas que no se pudieron leer muestran el motivo y no se cuentan como cubiertas.

### Phase 2 — Fichas normalizadas y grafo

**Status:** Complete — verified in `.planning/phases/02-fichas-y-grafo/02-VERIFICATION.md`.

**Goal:** Convertir las capturas en fichas técnicas con operaciones y construir el grafo Graphify.

**Requirements:** DOC-04, GRF-01, AI-01

**Success criteria:**
- Hay una ficha Markdown atribuida por página capturada y registros JSONL para operaciones documentadas.
- Método, ruta, autenticación, parámetros, request/response y errores solo aparecen cuando se encontraron en la fuente.
- El grafo distingue relaciones extraídas de las inferidas/ambiguas e incluye referencias de origen.

### Phase 3 — Buscador local y MCP

**Status:** Complete — verified in `.planning/phases/03-buscador-y-mcp/03-VERIFICATION.md`.

**Goal:** Consultar el corpus desde el navegador local y desde clientes de IA compatibles con MCP.

**Requirements:** QRY-01, QRY-02, QRY-03, AI-01, AI-02

**Success criteria:**
- Búsqueda local tolera tildes y filtros por área, función, método y ruta.
- Cada resultado enlaza a la ficha y a la página oficial, e indica fecha de captura.
- El servidor MCP de stdio responde con nodos y relaciones que incluyen fuente.

### Phase 4 — Publicaciones y verificación

**Status:** In progress.

**Goal:** Generar el índice y manual PDF desde el corpus, auditar cobertura y preparar el repo público.

**Requirements:** EXP-01, EXP-02, EXP-03, REF-02

**Success criteria:**
- Markdown y PDF reflejan las mismas fichas y operaciones.
- El PDF incluye tabla de contenidos y enlaces oficiales.
- Un refresco sin cambios mantiene los hashes de salida; un cambio regenera sus derivados.
- Los artefactos finales están publicados en el repo acordado.
