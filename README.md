# API de Mercado Libre — base de consulta `es_co`

Base documental en español para consultar la documentación pública del portal de desarrolladores de Mercado Libre Colombia. Incluye fichas técnicas enlazadas a sus fuentes, un buscador local, un grafo Graphify con servidor MCP y exportaciones en Markdown y PDF.

## Abrir el buscador

1. Crea un entorno e instala las dependencias: `py -3 -m venv .venv` y luego `.venv/Scripts/python.exe -m pip install -r requirements.txt` (en macOS/Linux usa `.venv/bin/python`).
2. Desde la raíz del repositorio ejecuta `.venv/Scripts/python.exe scripts/serve_search.py` (o `.venv/bin/python scripts/serve_search.py` en macOS/Linux).
3. Abre `http://127.0.0.1:4173/web/`.

El buscador funciona localmente y no requiere una base de datos alojada.

## Actualizar la documentación

Consulta [docs/ACTUALIZAR.md](docs/ACTUALIZAR.md) para capturar cambios con el navegador interno y regenerar índices, grafo y PDF.

## Consultar desde una IA

El corpus normalizado está disponible en `docs/markdown/`, `docs/temas/`, `data/pages.jsonl` y `data/operations.jsonl`. El servidor MCP local usa el grafo de Graphify. Revisa [`mcp-config.example.json`](mcp-config.example.json) y [docs/MCP.md](docs/MCP.md) para configurarlo en un cliente compatible.

## Exportaciones

- Índice y fichas por página: [`docs/markdown/INDEX.md`](docs/markdown/INDEX.md)
- Documentación agrupada por área: [`docs/temas/`](docs/temas/)
- Manual PDF: [`docs/mercadolibre-api-es-co.pdf`](docs/mercadolibre-api-es-co.pdf)
- Grafo Graphify: [`graphify-out/graph.json`](graphify-out/graph.json)
- Extracciones semánticas Graphify portables: [`data/graph-extractions/`](data/graph-extractions/)

Para actualizar el corpus, sigue [docs/ACTUALIZAR.md](docs/ACTUALIZAR.md).

## Fuentes y alcance

- [Portal de desarrolladores `es_co`](https://developers.mercadolibre.com.co/es_co/guia-para-producto)
- [Repositorio del proyecto](https://github.com/sierraglobalcompany-rgb/ApiMercadolibre)

La cobertura de cada página y sus detalles técnicos se documenta con redacción propia, fecha de captura y enlace oficial. La fecha de actualización publicada por Mercado Libre se conserva cuando la página la muestra.
