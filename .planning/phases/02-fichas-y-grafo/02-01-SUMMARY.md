---
phase: 02-fichas-y-grafo
plan: 01
subsystem: documentation-graph
tags: [mercado-libre, markdown, jsonl, graphify, provenance]
requires: [01-inventario-y-captura]
provides:
  - 203 fichas Markdown y un índice por área.
  - 1.072 registros JSONL: 874 operaciones y 198 conceptos.
  - Grafo Graphify con 6.968 nodos, 7.427 relaciones y 12 hiperrrelaciones.
  - Auditoría de cobertura de rutas con cero referencias sin representar.
affects: [03-buscador-y-mcp, 04-exportaciones-y-publicacion]
actuals:
  tokens: 0
  tasks: 3
  commits: 0
tech-stack:
  added: [Graphify 0.9.55, Python]
  patterns: [registros JSONL con URL/fecha/huella, fragmentos Graphify portables]
key-files:
  created: [data/operations.jsonl, data/graph-extractions/, docs/markdown/, scripts/build_graph.py, scripts/validate_graph.py]
  modified: [data/endpoint-coverage-report.json]
key-decisions:
  - "Los campos no hallados en la página se conservan como no documentados."
  - "El grafo normaliza ids con sufijo estable para preservar operaciones homónimas."
  - "Se excluyen auto-relaciones residuales de Graphify del artefacto consultable."
requirements-completed: [DOC-04, GRF-01, AI-01]
completed: 2026-10-08
status: complete
---

# Phase 2: Fichas normalizadas y grafo

Se generaron 203 fichas y 1.072 registros estructurados a partir del corpus capturado. La auditoría estricta encontró 1.579 referencias de ruta y las reconcilió por completo con los registros; ningún método, parámetro, error o respuesta ausente se inventó.

El grafo final contiene 6.968 nodos, 7.427 relaciones y 12 hiperrrelaciones. La validación confirma cobertura de todas las páginas y registros, procedencia por relación y cero auto-relaciones, duplicados de arista o extremos colgantes.
