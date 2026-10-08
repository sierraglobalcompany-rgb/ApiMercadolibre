from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        fail(f"No existe {path.relative_to(ROOT)}")
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                fail(f"JSONL inválido en {path.relative_to(ROOT)}:{line_no}: {exc}")
    return rows


def main() -> None:
    manifest = json.loads((ROOT / "data" / "manifest.json").read_text(encoding="utf-8"))
    by_id = {row["id"]: row for row in manifest}
    if len(by_id) != len(manifest):
        fail("IDs duplicados en data/manifest.json")
    uncaptured = [row["id"] for row in manifest if row.get("status") != "captured"]
    if uncaptured:
        fail(f"Hay {len(uncaptured)} páginas sin captura: {uncaptured[:8]}")

    missing_docs, pending_docs, stale_docs = [], [], []
    for row in manifest:
        capture_path = ROOT / ".cache" / "captures" / f"{row['id']}.json"
        doc_path = ROOT / "docs" / "markdown" / f"{row['id']}.md"
        if not capture_path.is_file():
            fail(f"Falta captura local para {row['id']}")
        capture = json.loads(capture_path.read_text(encoding="utf-8"))
        digest = hashlib.sha256(capture.get("text", "").encode("utf-8")).hexdigest()
        if digest != row.get("sha256"):
            fail(f"La huella de captura no coincide: {row['id']}")
        if not doc_path.is_file():
            missing_docs.append(row["id"])
            continue
        markdown = doc_path.read_text(encoding="utf-8")
        if "PENDIENTE" in markdown:
            pending_docs.append(row["id"])
        for expected in (row["url"], row.get("captured_at"), row.get("sha256")):
            if expected and expected not in markdown:
                stale_docs.append(row["id"])
                break
    if missing_docs:
        fail(f"Faltan {len(missing_docs)} fichas Markdown; p. ej. {missing_docs[:8]}")
    if pending_docs:
        fail(f"Hay {len(pending_docs)} fichas pendientes; p. ej. {pending_docs[:8]}")
    if stale_docs:
        fail(f"Hay metadatos de fuente incompletos en {stale_docs[:8]}")

    operations = read_jsonl(ROOT / "data" / "operations.jsonl")
    ids = [item.get("id") for item in operations]
    duplicates = [key for key, count in Counter(ids).items() if not key or count > 1]
    if duplicates:
        fail(f"IDs de operación/concepto vacíos o duplicados: {duplicates[:8]}")
    by_page: Counter[str] = Counter()
    for item in operations:
        page_id = item.get("page_id")
        if page_id not in by_id:
            fail(f"Registro apunta a una página inexistente: {page_id}")
        source = by_id[page_id]
        if item.get("source_url") != source.get("url"):
            fail(f"URL de fuente no coincide para {item.get('id')}")
        for key in ("captured_at", "sha256"):
            if item.get(key) != source.get(key):
                fail(f"{key} no coincide para {item.get('id')}")
        if item.get("kind") not in ("operation", "concept"):
            fail(f"Tipo de registro no válido: {item.get('id')}")
        if item.get("kind") == "operation" and (not item.get("method") or not item.get("path")):
            fail(f"Operación sin método o ruta explícita: {item.get('id')}")
        if urlsplit(item["source_url"]).path.startswith("/es_co/") is False:
            fail(f"Fuente fuera de es_co: {item.get('id')}")
        by_page[page_id] += 1
    pages_without_records = sorted(set(by_id) - set(by_page))
    if pages_without_records:
        fail(f"Páginas sin registros consultables: {pages_without_records[:8]}")

    link_report_path = ROOT / "data" / "link-audit-report.json"
    link_report = json.loads(link_report_path.read_text(encoding="utf-8"))
    pending_links = [x for x in link_report.get("links", []) if x.get("status") == "review_required"]
    if pending_links:
        fail(f"Hay enlaces internos sin clasificar: {len(pending_links)}")

    print(f"Corpus válido: {len(manifest)} fichas, {len(operations)} registros ({dict(Counter(x['kind'] for x in operations))}), {len(link_report.get('links', []))} enlaces internos auditados.")


if __name__ == "__main__":
    main()
