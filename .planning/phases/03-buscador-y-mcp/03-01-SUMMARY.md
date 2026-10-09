---
phase: 03-buscador-y-mcp
subsystem: local-search-mcp
tags: [mercado-libre, search, browser, mcp, graphify]
requires: [02-fichas-y-grafo]
provides:
  - Buscador local con filtros y búsqueda tolerante a tildes.
  - Adaptador MCP Graphify con URLs oficiales y fecha de captura.
  - Instrucciones y configuración de ejemplo para clientes MCP.
affects: [04-exportaciones-y-publicacion]
actuals:
  tokens: 0
  tasks: 2
  commits: 0
tech-stack:
  added: [HTML/CSS/JavaScript local, MCP stdio SDK]
  patterns: [JSON index desde corpus, MCP graph query con citas de fuente]
key-files:
  created: [web/, scripts/serve_search.py, scripts/mcp_server.py, docs/MCP.md, mcp-config.example.json]
key-decisions:
  - "El MCP envuelve consultas de Graphify para devolver la URL oficial y la fecha de captura en cada consulta."
requirements-completed: [QRY-01, QRY-02, QRY-03, AI-01, AI-02]
coverage:
  - id: Q1
    description: "Buscar por texto, método y ruta desde el navegador local."
    requirement: QRY-01
    verification:
      - kind: other
        ref: "Navegador interno: GET /users/me, filtros GET/ruta y coincidencia de términos"
        status: pass
    human_judgment: false
  - id: Q2
    description: "La búsqueda ignora tildes y conserva fragmento, ficha, fuente y fecha."
    requirement: QRY-02
    verification:
      - kind: other
        ref: "Navegador interno: autenticación y autenticacion mostraron la misma lista principal; resultados incluyen fuente/captura"
        status: pass
    human_judgment: false
  - id: Q3
    description: "El MCP consulta Graphify y devuelve las referencias oficiales con fechas."
    requirement: AI-02
    verification:
      - kind: other
        ref: "Cliente MCP stdio: list_tools y query_graph GET /users/me autenticación; respuesta incluye URL oficial/captured_at"
        status: pass
    human_judgment: false
completed: 2026-10-08
status: complete
---

# Phase 3: Buscador local y MCP

El buscador local consulta un índice JSON del corpus y permite filtrar resultados por área, recurso, método y ruta. Se verificó en el navegador interno la consulta `GET /users/me`, búsqueda de “autenticación” con y sin tilde y búsqueda de respuestas `429 rate limit`.

El servidor MCP de stdio usa el grafo Graphify; las pruebas de cliente confirmaron que `query_graph` devuelve contexto junto con URLs oficiales y fechas de captura. La configuración de cliente y los pasos de instalación están documentados.
