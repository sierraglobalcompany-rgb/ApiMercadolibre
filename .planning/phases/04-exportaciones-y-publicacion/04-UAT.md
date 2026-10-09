---
status: testing
phase: 04-exportaciones-y-publicacion
source: [04-01-SUMMARY.md]
started: 2026-10-08T23:59:58Z
updated: 2026-10-08T23:59:58Z
---

## Current Test

number: 1
name: Confirmar la entrega publicada
expected: El índice, el buscador, el grafo MCP y el PDF están disponibles en el repositorio público; el PDF incluye las 203 fichas, navegación y fuentes oficiales.
awaiting: user response

## Tests

### 1. Cobertura de Markdown y PDF
expected: El índice Markdown y el PDF incluyen las 203 páginas oficiales en 11 áreas.
result: pass
source: automated

### 2. Navegación y enlaces del PDF
expected: El PDF tiene tabla de contenidos, marcadores navegables y enlaces oficiales.
result: pass
source: automated

### 3. Refresco sin cambios
expected: Las 203 páginas se clasifican como sin cambio y los hashes de los derivados permanecen iguales.
result: pass
source: automated

### 4. Publicación y exclusiones
expected: `main` apunta al commit publicado y no hay capturas, `.venv` ni cachés Graphify entre los archivos publicados.
result: pass
source: automated

### 5. Confirmar la entrega publicada
expected: El usuario puede consultar el PDF completo y los artefactos de búsqueda y grafo en el repositorio público.
result: [pending]

## Summary

total: 5
passed: 4
issues: 0
pending: 1
skipped: 0
blocked: 0

## Gaps

Ninguna.
