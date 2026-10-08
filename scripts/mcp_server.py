"""Graphify-backed MCP server that includes official source citations."""
from __future__ import annotations

import argparse
import asyncio
import re
from pathlib import Path

from mcp import types
from mcp.server import Server
from mcp.server.stdio import stdio_server

from graphify import serve as graphify_serve


def build_server(graph_path: Path) -> Server:
    resolved = graph_path.resolve()
    graph = graphify_serve._load_graph(str(resolved))
    graphify_serve._get_trigram_index(graph)

    async def list_tools() -> list[types.Tool]:
        return [
            types.Tool(
                name="query_graph",
                description=(
                    "Consulta el grafo Graphify de la documentación de Mercado Libre. "
                    "Devuelve nodos, relaciones y URLs oficiales con fecha de captura."
                ),
                inputSchema={
                    "type": "object",
                    "properties": {
                        "question": {"type": "string", "description": "Términos, operación, recurso, campo o error que se desea consultar."},
                        "mode": {"type": "string", "enum": ["bfs", "dfs"], "default": "bfs"},
                        "depth": {"type": "integer", "minimum": 1, "maximum": 6, "default": 3},
                        "token_budget": {"type": "integer", "default": 4000},
                    },
                    "required": ["question"],
                },
            ),
            types.Tool(
                name="graph_stats",
                description="Devuelve el tamaño y las fechas de cobertura del grafo documental.",
                inputSchema={"type": "object", "properties": {}},
            ),
        ]

    async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
        if name == "query_graph":
            question = str(arguments.get("question", "")).strip()
            if not question:
                raise ValueError("question es obligatorio")
            depth = max(1, min(6, int(arguments.get("depth", 3))))
            mode = "dfs" if arguments.get("mode") == "dfs" else "bfs"
            token_budget = max(500, min(12000, int(arguments.get("token_budget", 4000))))
            context = graphify_serve._query_graph_text(
                graph,
                question,
                mode=mode,
                depth=depth,
                token_budget=token_budget,
                graph_path=str(resolved),
            )
            source_files = sorted(set(re.findall(r"\[src=([^\s\]]+)", context)))
            sources: dict[str, tuple[str, str]] = {}
            for _, attrs in graph.nodes(data=True):
                source_file = attrs.get("source_file")
                source_url = attrs.get("source_url")
                captured_at = attrs.get("captured_at") or "no registrada"
                if source_file in source_files and source_url:
                    sources[source_file] = (str(source_url), str(captured_at))
            source_lines = [
                f"- {url} (captura: {captured_at}) — `{source_file}`"
                for source_file, (url, captured_at) in sorted(sources.items())
            ]
            if source_lines:
                context += "\n\nFUENTES OFICIALES\n" + "\n".join(source_lines)
            elif source_files:
                context += "\n\nFUENTES\n" + "\n".join(f"- `{source_file}`" for source_file in source_files)
            return [types.TextContent(type="text", text=context)]

        if name == "graph_stats":
            pages = {
                str(attrs.get("source_url"))
                for _, attrs in graph.nodes(data=True)
                if attrs.get("kind") == "page" and attrs.get("source_url")
            }
            captures = sorted({
                str(attrs.get("captured_at"))
                for _, attrs in graph.nodes(data=True)
                if attrs.get("kind") == "page" and attrs.get("captured_at")
            })
            summary = (
                f"Nodos: {graph.number_of_nodes()}\n"
                f"Relaciones: {graph.number_of_edges()}\n"
                f"Páginas con fuente: {len(pages)}\n"
                f"Capturas: {', '.join(captures) if captures else 'sin fecha'}"
            )
            return [types.TextContent(type="text", text=summary)]

        raise ValueError(f"Herramienta desconocida: {name}")

    async def on_list_tools(ctx, params) -> types.ListToolsResult:
        return types.ListToolsResult(tools=await list_tools())

    async def on_call_tool(ctx, params) -> types.CallToolResult:
        try:
            content = await call_tool(params.name, dict(params.arguments or {}))
        except Exception as exc:
            return types.CallToolResult(
                content=[types.TextContent(type="text", text=f"Error: {exc}")],
                isError=True,
            )
        return types.CallToolResult(content=content)

    return Server(
        "mercadolibre-es-co-graphify",
        version="1.0.0",
        on_list_tools=on_list_tools,
        on_call_tool=on_call_tool,
    )


async def run(graph_path: Path) -> None:
    server = build_server(graph_path)
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph", type=Path, default=Path("graphify-out/graph.json"))
    args = parser.parse_args()
    asyncio.run(run(args.graph))


if __name__ == "__main__":
    main()
