from __future__ import annotations

import mimetypes
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "web"
DOCS = ROOT / "docs"
DATA = ROOT / "data"
GRAPH = ROOT / "graphify-out"


class Handler(BaseHTTPRequestHandler):
    server_version = "MercadoLibreLocalDocs/1.0"

    def resolve_path(self, path: str) -> Path | None:
        if path in ("", "/"):
            return None
        if path == "/web":
            path = "/web/"
        if path.startswith("/web/"):
            relative = path.removeprefix("/web/") or "index.html"
            root = WEB
        elif path == "/docs/markdown/INDEX.md":
            root, relative = DOCS / "markdown", "INDEX.md"
        elif path.startswith("/docs/markdown/") and path.endswith(".md"):
            name = path.removeprefix("/docs/markdown/")
            if not re.fullmatch(r"[a-z0-9-]+\.md", name):
                return None
            root = DOCS / "markdown"
            relative = name
        elif path.startswith("/docs/temas/") and path.endswith(".md"):
            name = path.removeprefix("/docs/temas/")
            if not re.fullmatch(r"[a-z0-9-]+\.md", name):
                return None
            root, relative = DOCS / "temas", name
        elif path == "/docs/mercadolibre-api-es-co.pdf":
            root, relative = DOCS, "mercadolibre-api-es-co.pdf"
        elif path == "/docs/ACTUALIZAR.md":
            root, relative = DOCS, "ACTUALIZAR.md"
        elif path == "/docs/MCP.md":
            root, relative = DOCS, "MCP.md"
        elif path in ("/data/operations.jsonl", "/data/pages.jsonl", "/data/manifest.json", "/data/link-audit-report.json"):
            root, relative = DATA, path.removeprefix("/data/")
        elif path in ("/graphify-out/graph.html", "/graphify-out/graph.json", "/graphify-out/GRAPH_REPORT.md"):
            root, relative = GRAPH, path.removeprefix("/graphify-out/")
        else:
            return None
        candidate = (root / relative).resolve()
        try:
            candidate.relative_to(root.resolve())
        except ValueError:
            return None
        return candidate

    def do_GET(self) -> None:
        path = unquote(urlsplit(self.path).path)
        if path in ("", "/", "/web"):
            self.send_response(302)
            self.send_header("Location", "/web/")
            self.end_headers()
            return
        candidate = self.resolve_path(path)
        if not candidate or not candidate.is_file():
            self.send_error(404, "Archivo no disponible")
            return
        content_type = mimetypes.guess_type(candidate.name)[0] or "application/octet-stream"
        if candidate.suffix in (".md", ".json", ".jsonl", ".js", ".css"):
            content_type += "; charset=utf-8"
        body = candidate.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt: str, *args: object) -> None:
        print(f"[{self.log_date_time_string()}] {fmt % args}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Sirve el buscador local y los artefactos documentales permitidos.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=4173)
    args = parser.parse_args()
    print(f"Buscador local en http://{args.host}:{args.port}/web/")
    ThreadingHTTPServer((args.host, args.port), Handler).serve_forever()
