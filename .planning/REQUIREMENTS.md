# Requirements: Base de consulta de la API de Mercado Libre

**Defined:** 2026-10-08  
**Core Value:** Buscar y reutilizar información técnica oficial de la API de Mercado Libre con procedencia verificable.

## v1 Requirements

### Captura y documentación

- [x] **DOC-01**: El sistema descubre y deduplica enlaces del portal público `es_co` usando el navegador interno.
- [x] **DOC-02**: Cada página guarda título, sección, URL, fecha de captura, huella de contenido y fecha de fuente cuando aparece.
- [x] **DOC-03**: Cada página inaccesible queda en el manifiesto con un estado y motivo; nunca se marca como cubierta si no fue capturada.
- [x] **DOC-04**: Las fichas cubren operaciones y detalles técnicos que la página documenta, manteniendo enlace y procedencia.

### Búsqueda y acceso para IA

- [x] **QRY-01**: La web local permite búsquedas tolerantes a mayúsculas, acentos y puntuación.
- [x] **QRY-02**: Los resultados se pueden filtrar por área, función/recurso, método HTTP y ruta.
- [x] **QRY-03**: Cada resultado muestra fragmento coincidente, fuente oficial y fecha de captura.
- [x] **AI-01**: El corpus se puede consumir como Markdown y JSONL sin depender de un servicio externo.
- [x] **AI-02**: Un servidor Graphify MCP local expone consultas del grafo y conserva referencias a las fuentes.

### Grafo y exportaciones

- [x] **GRF-01**: Graphify construye nodos y relaciones a partir de documentos normalizados; las relaciones no documentadas se marcan como inferidas o ambiguas.
- [x] **EXP-01**: El índice Markdown organiza las páginas por área funcional.
- [x] **EXP-02**: Un PDF único incluye tabla de contenidos, las fichas disponibles y enlaces oficiales.
- [x] **EXP-03**: Markdown, PDF, buscador, índice y grafo se regeneran desde la misma fuente normalizada.

### Refresco

- [x] **REF-01**: El refresco manual compara huellas de contenido y marca páginas nuevas, cambiadas y sin cambios.
- [x] **REF-02**: Una actualización con cambios regenera los derivados desde el corpus revisado y conserva fechas y estados de captura.

## v2 Requirements

No hay requisitos diferidos para esta entrega.

## Out of Scope

| Feature | Reason |
|---------|--------|
| API remota alojada | La búsqueda y consulta MCP se ejecutan en el equipo del usuario. |
| Copia literal extensa del portal | El repo público publica síntesis atribuida para consulta y evita republicar artículos completos. |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| DOC-01 | Phase 1 | Complete |
| DOC-02 | Phase 1 | Complete |
| DOC-03 | Phase 1 | Complete |
| DOC-04 | Phase 2 | Complete |
| GRF-01 | Phase 2 | Complete |
| AI-01 | Phase 2 | Complete |
| QRY-01 | Phase 3 | Complete |
| QRY-02 | Phase 3 | Complete |
| QRY-03 | Phase 3 | Complete |
| AI-02 | Phase 3 | Complete |
| EXP-01 | Phase 4 | Complete |
| EXP-02 | Phase 4 | Complete |
| EXP-03 | Phase 4 | Complete |
| REF-01 | Phase 1 | Complete |
| REF-02 | Phase 4 | Complete |

**Coverage:** 15 requirements; 15 mapped; 0 unmapped.

---
*Requirements defined: 2026-10-08*  
*Last updated: 2026-10-08 after implementation and verification*
