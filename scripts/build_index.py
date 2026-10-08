from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "manifest.json"
DOCS = ROOT / "docs" / "markdown"
OPERATIONS = ROOT / "data" / "operations.jsonl"
OUTPUT = ROOT / "web" / "search-index.json"


def plain_markdown(text: str) -> str:
    if text.startswith("---\n"):
        _, _, text = text.partition("\n---\n")
    text = re.sub(r"```[\s\S]*?```", lambda m: " " + re.sub(r"```[^\n]*|```", " ", m.group(0)) + " ", text)
    text = re.sub(r"!\[([^]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[`*_>#|]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"JSONL inválido en {path}:{line_no}: {exc}") from exc
    return rows


def searchable_value(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    documents: list[dict] = []
    page_records: list[dict] = []
    for row in manifest:
        if row.get("status") != "captured":
            continue
        path = DOCS / f"{row['id']}.md"
        markdown = path.read_text(encoding="utf-8") if path.exists() else ""
        body = plain_markdown(markdown)
        record = {
            "id": row["id"],
            "type": "page",
            "title": row["title"],
            "section": row.get("section", "Portal"),
            "subsection": row.get("subsection"),
            "source_url": row["url"],
            "source_updated_at": row.get("source_updated_at"),
            "captured_at": row.get("captured_at"),
            "sha256": row.get("sha256"),
            "content": body,
            "methods": [],
            "paths": [],
        }
        page_records.append(record)
        documents.append(record)

    operations = load_jsonl(OPERATIONS)
    for item in operations:
        method = str(item.get("method") or "").upper()
        path = str(item.get("path") or "")
        route_resource = "/" + path.strip("/").split("/")[0] if path else None
        title = str(item.get("name") or item.get("title") or path or "Operación")
        fields = [item.get("summary"), item.get("description"), item.get("auth"), item.get("parameters"), item.get("request"), item.get("response"), item.get("errors"), item.get("examples")]
        content = " ".join(plain_markdown(searchable_value(value)) for value in fields if value not in (None, "", [], {}))
        record_type = "operation" if item.get("kind", "operation") == "operation" else "concept"
        documents.append({
            "id": str(item.get("id") or f"{item.get('page_id','operation')}-{method.lower()}-{len(documents)}"),
            "type": record_type,
            "title": title,
            "page_id": item.get("page_id"),
            "section": item.get("section", "Portal"),
            "subsection": item.get("subsection"),
            "source_url": item.get("source_url"),
            "source_updated_at": item.get("source_updated_at"),
            "captured_at": item.get("captured_at"),
            "sha256": item.get("sha256"),
            "content": content,
            "name": item.get("name"),
            "method": method,
            "path": path,
            "resource": item.get("resource") or route_resource or item.get("page_id"),
            "methods": [method] if method else [],
            "paths": [path] if path else [],
        })

    (ROOT / "data" / "pages.jsonl").write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in page_records), encoding="utf-8")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({
        "schema_version": 1,
        "locale": "es_co",
        "page_count": len(page_records),
        "operation_count": len(operations),
        "documents": documents,
    }, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"Índice generado: {len(page_records)} páginas, {len(operations)} operaciones -> {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
