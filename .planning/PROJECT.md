# Base de consulta de la API de Mercado Libre

## What This Is

Una base documental en español colombiano (`es_co`) para buscar, relacionar y consultar las funciones y operaciones documentadas en el portal público de Mercado Libre. El proyecto sirve a desarrolladores y a otros asistentes de IA mediante Markdown, JSON, un buscador local y Graphify MCP.

## Core Value

Encontrar una respuesta técnica atribuida a una fuente oficial en segundos, sin confundir datos documentados con inferencias.

## Requirements

### Validated

- ✓ Cubrir el portal público de desarrolladores en `es_co` — confirmado por el usuario.
- ✓ Consultar páginas y operaciones por función, recurso, método, ruta y texto — confirmado.
- ✓ Usar el navegador interno para leer las páginas oficiales — confirmado.
- ✓ Mantener corpus Markdown/JSON y un grafo Graphify consultable por MCP — confirmado.
- ✓ Generar un índice Markdown y un PDF único en español con referencias a fuentes — confirmado.
- ✓ Mantener el repo público indicado como destino y habilitar actualización manual — confirmado.

### Active

- [ ] Inventariar enlaces oficiales `es_co`, capturar fecha, título y huella por página.
- [ ] Extraer operaciones y detalles técnicos disponibles sin inventar datos ausentes.
- [ ] Construir índices de búsqueda, relaciones Graphify y el servidor MCP local.
- [ ] Generar documentación Markdown y PDF con cobertura verificable.

### Out of Scope

- Llamar endpoints privados de Mercado Libre o usar credenciales de vendedores.
- Exponer consultas mediante una API remota o una base de datos alojada.
- Publicar una copia literal extensa del portal oficial.
- Incluir contenido de otros locales que no sea `es_co`, salvo enlaces de referencia conservados como fuente.

## Context

El directorio de trabajo y el repo público enlazado estaban vacíos al inicio. El índice visible del portal tenía aproximadamente 200 enlaces antes de deduplicarse. La página de introducción mostraba actualización 29/12/2025; una página individual consultada durante la revisión mostraba 15/07/2026. Por eso cada captura distingue fecha de fuente y fecha de consulta.

El runtime local tenía Graphify 0.9.37, mientras que la skill disponible documenta 0.9.55. Graphify incluye `graphify.serve`, pero falta la dependencia opcional MCP. La implementación fijará dependencias en un entorno virtual propio del repo.

## Constraints

- La documentación fuente se recopila desde el navegador interno, no por solicitudes HTTP directas.
- La salida pública debe atribuir cada ficha a la página oficial y registrar su fecha de captura.
- El grafo y el índice se derivan del mismo corpus normalizado para evitar discrepancias.
- Una página inaccesible o sin fecha de actualización se marca explícitamente; no se completa por suposición.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Repo público indicado como destino | Acordado por el usuario | Decidido |
| Cobertura integral del portal `es_co` | Acordado por el usuario | Decidido |
| Índice JSON local + grafo Graphify | Sin servicio externo y compatible con consulta offline | Decidido |
| MCP local por stdio y archivos portables | Permite conexión desde clientes MCP y uso mediante importación | Decidido |
| Cobertura técnica completa con redacción propia | Conserva operaciones y hechos con citas sin hacer una copia literal extensa | Decidido |

---
*Last updated: 2026-10-08 after project initialization.*
