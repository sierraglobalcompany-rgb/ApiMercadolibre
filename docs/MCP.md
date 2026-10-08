# Consultar el grafo desde un cliente MCP

El grafo de esta base se sirve localmente por MCP sobre stdio mediante un adaptador que usa las consultas de Graphify. Cada respuesta incluye las URLs oficiales y fechas de captura que respaldan el contexto. El proceso no publica una API remota y solo lee `graphify-out/graph.json`.

## Requisitos

- Python instalado y dependencias del proyecto instaladas con `python -m pip install -r requirements.txt`.
- El archivo `graphify-out/graph.json` generado por `python scripts/build_graph.py`.
- Un cliente que admita servidores MCP locales por stdio.

## Configuración

Abre `mcp-config.example.json`, reemplaza la ruta de ejemplo por la ruta absoluta del repositorio y copia la entrada `mercadolibre-es-co` a la configuración de servidores MCP de tu cliente. En Windows, usa barras `/` o duplica las barras invertidas en JSON.

La configuración de ejemplo usa el Python aislado del repositorio y ejecuta `scripts/mcp_server.py` con la ruta absoluta del grafo. El cliente iniciará y cerrará el servidor cuando lo necesite. Si se mueve el repositorio o el entorno virtual, actualiza esas rutas.

## Consultas recomendadas

Pregunta por una operación, recurso, campo o error con términos concretos, por ejemplo:

- «¿Qué rutas consultan las publicaciones de un usuario?»
- «¿Qué errores se documentan para el endpoint de precios?»
- «¿Qué parámetros recibe la consulta de envíos?»

El servidor devuelve contexto del grafo con una lista de fuentes oficiales y sus fechas de captura. La herramienta `graph_stats` informa cobertura y tamaño. Cuando el cliente necesite texto completo, importa `docs/markdown/`, `docs/temas/` y `data/operations.jsonl` como corpus documental.

## Diagnóstico

Desde la raíz del proyecto ejecuta `python scripts/mcp_server.py --help` para revisar las opciones. Si el cliente no puede iniciar el proceso, confirma que `.venv/Scripts/python.exe` existe, que el grafo fue generado y que las rutas de la configuración apuntan al repositorio.
