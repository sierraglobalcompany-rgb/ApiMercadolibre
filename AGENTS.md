# Project instructions

- Treat `developers.mercadolibre.com.co/es_co` as the authoritative documentation source.
- Read source pages through the Codex internal browser; do not fetch their content with HTTP clients.
- Keep all published records linked to an official source URL and capture date.
- Do not infer undocumented API behavior. Mark unavailable facts as `No documentado en la fuente`.
- Keep raw browser captures under `.cache/`; publish only attributed, structured reference material.
- Run Graphify over the normalized documentation corpus, not over `.cache/` or generated frontend files.
- Use GSD artifacts in `.planning/` to track requirements, phases, verification, and project state.

## L1 KISS + Ponytail
Antes de editar software, consulta `.agents/skills/kiss-ponytail/SKILL.md`: comprende el flujo/callers, elimina solo lo no requerido, reutiliza primero código existente, biblioteca estándar, capacidad nativa y dependencias actuales. Cambia lo mínimo completo preservando seguridad, datos, validaciones, UX, pruebas y L2–L6. `ponytail-audit` solo cuando se solicite/justifique. No confundir esta integración con el plugin global y sus hooks, que requieren instalación y confianza separadas.
