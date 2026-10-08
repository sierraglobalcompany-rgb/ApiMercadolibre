from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / ".cache" / "captures"
MANIFEST_PATH = ROOT / "data" / "manifest.json"
LINK_AUDIT_PATH = ROOT / "data" / "link-audit.json"
MAX_BODY = 12 * 1024 * 1024


def canonical_url(value: str) -> str:
    parts = urlsplit(value.strip())
    return urlunsplit((parts.scheme, parts.netloc, parts.path.rstrip("/") or "/", "", ""))


def valid_source(value: str) -> bool:
    parts = urlsplit(value)
    return parts.scheme == "https" and parts.hostname == "developers.mercadolibre.com.co" and parts.path.startswith("/es_co/")


def slug_for(url: str) -> str:
    part = urlsplit(canonical_url(url)).path.rstrip("/").split("/")[-1]
    return re.sub(r"[^a-z0-9-]+", "-", part.lower()).strip("-") or "pagina"


def load_manifest() -> list[dict]:
    if not MANIFEST_PATH.exists():
        return []
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def save_manifest(rows: list[dict]) -> None:
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class Handler(BaseHTTPRequestHandler):
    server_version = "MercadoLibreDocsCapture/1.0"

    def send_json(self, status: int, value: object) -> None:
        data = json.dumps(value, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:
        if self.path == "/health":
            rows = load_manifest()
            captured = sum(row.get("status") == "captured" for row in rows)
            return self.send_json(200, {"ok": True, "total": len(rows), "captured": captured})
        if self.path == "/manifest":
            return self.send_json(200, load_manifest())
        if self.path == "/link-audit":
            if LINK_AUDIT_PATH.exists():
                return self.send_json(200, json.loads(LINK_AUDIT_PATH.read_text(encoding="utf-8")))
            return self.send_json(200, {"links": []})
        if self.path != "/":
            return self.send_json(404, {"error": "not_found"})
        html = """<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Captura local de documentación</title><style>body{font:16px system-ui;max-width:850px;margin:3rem auto;padding:0 1rem;color:#17223b}textarea{width:100%;height:24rem;font:13px ui-monospace,monospace}button{margin:.8rem .5rem 0 0;padding:.7rem 1rem}#status{white-space:pre-wrap;margin-top:1rem}</style><h1>Receptor local de capturas</h1><p>Guarda en este equipo el texto extraído desde el navegador interno.</p><label for="payload">JSON</label><textarea id="payload" required></textarea><br><button id="save-capture" type="button">Guardar captura</button><button id="save-manifest" type="button">Guardar manifiesto</button><button id="save-links" type="button">Guardar auditoría de enlaces</button><div id="status" role="status"></div><script>async function send(path){const s=document.querySelector('#status');s.textContent='Guardando…';try{const r=await fetch(path,{method:'POST',headers:{'content-type':'application/json'},body:document.querySelector('#payload').value});const j=await r.json();s.textContent=JSON.stringify(j,null,2)}catch(err){s.textContent=String(err)}}document.querySelector('#save-capture').addEventListener('click',()=>send('/capture'));document.querySelector('#save-manifest').addEventListener('click',()=>send('/manifest'));document.querySelector('#save-links').addEventListener('click',()=>send('/links'))</script></html>"""
        data = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self) -> None:
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > MAX_BODY:
                return self.send_json(413, {"error": "invalid_body_size", "max_bytes": MAX_BODY})
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
        except (ValueError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            return self.send_json(400, {"error": "invalid_json", "detail": str(exc)})

        if self.path == "/manifest":
            incoming = payload.get("documents") if isinstance(payload, dict) else None
            if not isinstance(incoming, list):
                return self.send_json(400, {"error": "documents_must_be_an_array"})
            old = {canonical_url(row["url"]): row for row in load_manifest() if row.get("url")}
            for item in incoming:
                url = item.get("url", "")
                if not valid_source(url):
                    continue
                canon = canonical_url(url)
                previous = old.get(canon, {})
                old[canon] = {
                    **previous,
                    "id": slug_for(canon),
                    "title": str(item.get("title") or previous.get("title") or canon),
                    "url": canon,
                    "section": str(item.get("section") or previous.get("section") or "Portal"),
                    "subsection": item.get("subsection") or previous.get("subsection"),
                    "status": previous.get("status", "pending"),
                    "source_updated_at": previous.get("source_updated_at"),
                    "captured_at": previous.get("captured_at"),
                    "sha256": previous.get("sha256"),
                    "reason": previous.get("reason"),
                }
            rows = sorted(old.values(), key=lambda row: (row["section"].casefold(), row["title"].casefold()))
            save_manifest(rows)
            return self.send_json(200, {"ok": True, "total": len(rows)})

        if self.path == "/links":
            links = payload.get("links") if isinstance(payload, dict) else None
            if not isinstance(links, list):
                return self.send_json(400, {"error": "links_must_be_an_array"})
            normalized = []
            seen = set()
            for item in links:
                if not isinstance(item, dict):
                    continue
                url = str(item.get("url") or "").strip()
                if not url.startswith("https://developers.mercadolibre.com.co/"):
                    continue
                key = (str(item.get("source_url") or ""), url, str(item.get("link_text") or ""))
                if key in seen:
                    continue
                seen.add(key)
                normalized.append({
                    "source_url": str(item.get("source_url") or ""),
                    "source_page_id": str(item.get("source_page_id") or ""),
                    "link_text": str(item.get("link_text") or ""),
                    "url": url,
                    "locale_scope": "es_co" if url.startswith("https://developers.mercadolibre.com.co/es_co/") else "outside_es_co",
                })
            result = {"captured_at": datetime.now(timezone.utc).isoformat(), "links": normalized}
            LINK_AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
            LINK_AUDIT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            return self.send_json(200, {"ok": True, "links": len(normalized), "es_co": sum(link["locale_scope"] == "es_co" for link in normalized), "outside_es_co": sum(link["locale_scope"] == "outside_es_co" for link in normalized)})

        if self.path != "/capture" or not isinstance(payload, dict):
            return self.send_json(404, {"error": "not_found"})

        source_url = str(payload.get("source_url") or payload.get("url") or "")
        final_url = str(payload.get("final_url") or source_url)
        canon = canonical_url(source_url)
        if not valid_source(source_url):
            return self.send_json(400, {"error": "source_url_outside_es_co", "url": source_url})
        rows = load_manifest()
        row = next((entry for entry in rows if canonical_url(entry["url"]) == canon), None)
        if row is None:
            return self.send_json(409, {"error": "url_not_in_manifest", "url": canon})

        if not valid_source(final_url):
            row.update({"status": "redirected", "reason": f"Destino fuera de es_co: {final_url}", "captured_at": payload.get("captured_at")})
            save_manifest(rows)
            return self.send_json(200, {"ok": True, "status": "redirected", "url": canon})

        text = str(payload.get("text") or "")
        if len(text.strip()) < 80:
            row.update({"status": "failed", "reason": str(payload.get("reason") or "Contenido principal vacío o demasiado corto"), "captured_at": payload.get("captured_at")})
            save_manifest(rows)
            return self.send_json(200, {"ok": True, "status": "failed", "url": canon})

        captured_at = str(payload.get("captured_at") or datetime.now(timezone.utc).isoformat())
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        record = {
            "id": row["id"],
            "title": str(payload.get("title") or row["title"]),
            "section": row["section"],
            "subsection": row.get("subsection"),
            "source_url": canon,
            "final_url": canonical_url(final_url),
            "locale": "es_co",
            "source_updated_at": payload.get("source_updated_at"),
            "captured_at": captured_at,
            "sha256": digest,
            "text": text,
            "blocks": payload.get("blocks") or [],
            "links": payload.get("links") or [],
        }
        CACHE.mkdir(parents=True, exist_ok=True)
        (CACHE / f"{row['id']}.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        row.update({"title": record["title"], "status": "captured", "source_updated_at": record["source_updated_at"], "captured_at": captured_at, "sha256": digest, "reason": None})
        save_manifest(rows)
        return self.send_json(200, {"ok": True, "status": "captured", "id": row["id"], "sha256": digest, "chars": len(text)})

    def log_message(self, fmt: str, *args: object) -> None:
        print(f"[{self.log_date_time_string()}] {fmt % args}")


if __name__ == "__main__":
    CACHE.mkdir(parents=True, exist_ok=True)
    print("Local capture receiver on http://127.0.0.1:8765")
    HTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
