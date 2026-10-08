from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "graphify-out" / "semantic-chunks"
OUTPUT = ROOT / "data" / "graph-extractions"
MANIFEST = ROOT / "data" / "manifest.json"
DOCS = ROOT / "docs" / "markdown"


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def main() -> None:
    pages = {row["id"]: row for row in json.loads(MANIFEST.read_text(encoding="utf-8")) if row.get("status") == "captured"}
    by_source = {str((DOCS / f"{page_id}.md").resolve()): page for page_id, page in pages.items()}
    raw_files = sorted(RAW.glob(".graphify_chunk_*.json")) if RAW.is_dir() else []
    if not raw_files:
        if OUTPUT.is_dir() and any(OUTPUT.glob("batch-*.json")):
            print("Sin fragmentos locales nuevos; se conservan las extracciones portables existentes.")
            return
        fail("No hay fragmentos Graphify. Genera un chunk semántico por cada grupo de fichas antes de construir el grafo.")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    total_nodes = total_edges = total_hyperedges = 0
    for raw_path in raw_files:
        match = re.fullmatch(r"\.graphify_chunk_(\d+)\.json", raw_path.name)
        if not match:
            continue
        data = json.loads(raw_path.read_text(encoding="utf-8"))
        if not all(isinstance(data.get(key, []), list) for key in ("nodes", "edges", "hyperedges")):
            fail(f"Estructura Graphify inválida: {raw_path.name}")
        files_seen: set[str] = set()
        for kind in ("nodes", "edges", "hyperedges"):
            for item in data.get(kind, []):
                source = item.get("source_file")
                if not source:
                    fail(f"{kind} sin source_file en {raw_path.name}")
                source_path = Path(str(source))
                resolved = source_path.resolve() if source_path.is_absolute() else (ROOT / source_path).resolve()
                page = by_source.get(str(resolved))
                if not page:
                    fail(f"{kind} apunta a un Markdown fuera del manifiesto en {raw_path.name}: {source}")
                page_id = page["id"]
                files_seen.add(page_id)
                if kind == "nodes":
                    # The raw Graphify fragment must still match the exact source
                    # snapshot. Never relabel a stale extraction with new metadata.
                    if item.get("source_url") != page.get("url") or item.get("captured_at") != page.get("captured_at"):
                        fail(f"El nodo {item.get('id')} está desactualizado para {page_id}; vuelve a extraer esa ficha con Graphify.")
                item["source_file"] = f"docs/markdown/{page_id}.md"
                item["source_url"] = page["url"]
                item["captured_at"] = page["captured_at"]
                item["sha256"] = page["sha256"]
                item["page_id"] = page_id
                item["section"] = page.get("section")
        if len(files_seen) == 0:
            fail(f"El chunk {raw_path.name} no menciona páginas del manifiesto")
        output_path = OUTPUT / f"batch-{int(match.group(1)):02}.json"
        output_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        total_nodes += len(data.get("nodes", []))
        total_edges += len(data.get("edges", []))
        total_hyperedges += len(data.get("hyperedges", []))

    print(f"Extracciones Graphify portables: {total_nodes} nodos, {total_edges} relaciones y {total_hyperedges} hiperrrelaciones en {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
