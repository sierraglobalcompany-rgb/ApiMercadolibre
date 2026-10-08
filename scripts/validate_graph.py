from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    manifest = json.loads((ROOT / "data" / "manifest.json").read_text(encoding="utf-8"))
    rows = read_jsonl(ROOT / "data" / "operations.jsonl")
    graph_path = ROOT / "graphify-out" / "graph.json"
    if not graph_path.is_file():
        fail("No existe graphify-out/graph.json")
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    nodes = graph.get("nodes")
    edges = graph.get("links", graph.get("edges", []))
    hyperedges = graph.get("hyperedges", graph.get("graph", {}).get("hyperedges", []))
    if not isinstance(nodes, list) or not nodes:
        fail("El grafo no contiene nodos")
    if not isinstance(edges, list):
        fail("El grafo no contiene una lista de relaciones")

    node_ids = {str(node.get("id")) for node in nodes if isinstance(node, dict)}
    if len(node_ids) != len(nodes):
        fail("Hay nodos sin ID o con ID duplicado")
    manifest_by_id = {row["id"]: row for row in manifest if row.get("status") == "captured"}
    by_page: dict[str, list[dict]] = {}

    def verify_provenance(item: dict, kind: str) -> str:
        page_id = str(item.get("page_id") or "")
        page = manifest_by_id.get(page_id)
        if not page:
            fail(f"{kind} {item.get('id') or item.get('source')} apunta a page_id desconocido: {page_id}")
        if urlsplit(str(page.get("url") or "")).path.startswith("/es_co/") is False:
            fail(f"Fuente fuera de es_co en página {page_id}")
        for key, source_key in (("source_url", "url"), ("captured_at", "captured_at"), ("sha256", "sha256")):
            if item.get(key) != page.get(source_key):
                fail(f"{kind} {item.get('id') or item.get('source')} tiene {key} divergente del manifiesto {page_id}")
        source_file = str(item.get("source_file") or "").replace("\\", "/")
        expected_file = f"docs/markdown/{page_id}.md"
        if source_file != expected_file:
            fail(f"{kind} {item.get('id') or item.get('source')} conserva una ruta ausente/local/no canónica: {source_file}")
        return page_id

    portable_dir = ROOT / "data" / "graph-extractions"
    portable_files = sorted(portable_dir.glob("batch-*.json"))
    if not portable_files:
        fail("No hay extracciones Graphify portables en data/graph-extractions")
    extracted_pages: set[str] = set()
    for fragment_path in portable_files:
        fragment = json.loads(fragment_path.read_text(encoding="utf-8"))
        for kind in ("nodes", "edges", "hyperedges"):
            for item in fragment.get(kind, []):
                page_id = verify_provenance(item, f"Extracción {kind}")
                if kind == "nodes":
                    extracted_pages.add(page_id)
                confidence = item.get("confidence")
                if kind != "nodes":
                    score = item.get("confidence_score")
                    valid_scores = {"EXTRACTED": {1.0}, "INFERRED": {0.95, 0.85, 0.75, 0.65, 0.55}, "AMBIGUOUS": {0.1, 0.2, 0.3}}
                    if confidence not in valid_scores or score not in valid_scores[confidence]:
                        fail(f"Extracción {kind} con confianza inválida en {fragment_path.name}: {confidence}/{score}")
    missing_extractions = sorted(set(manifest_by_id) - extracted_pages)
    if missing_extractions:
        fail(f"Las extracciones Graphify no cubren {len(missing_extractions)} páginas: {missing_extractions[:8]}")

    for node in nodes:
        if not isinstance(node, dict):
            fail("Hay un nodo con formato inválido")
        page_id = verify_provenance(node, "Nodo")
        by_page.setdefault(page_id, []).append(node)
    missing_pages = sorted(set(manifest_by_id) - set(by_page))
    if missing_pages:
        fail(f"El grafo omite {len(missing_pages)} páginas capturadas: {missing_pages[:8]}")
    for page_id, page in manifest_by_id.items():
        if not any(node.get("source_url") == page.get("url") and node.get("captured_at") == page.get("captured_at") and node.get("sha256") == page.get("sha256") for node in by_page[page_id]):
            fail(f"Ningún nodo de {page_id} conserva la procedencia exacta del manifiesto")

    node_rows = [node for node in nodes if node.get("kind") in {"operation", "concept"}]
    covered: Counter[tuple] = Counter()
    for node in node_rows:
        covered[(node.get("page_id"), node.get("kind"), str(node.get("method") or "").upper(), node.get("path") or "", node.get("name") or "")] += 1
    missing_records = []
    for row in rows:
        kind = row.get("kind")
        key = (row.get("page_id"), kind, str(row.get("method") or "").upper(), row.get("path") or "", row.get("name") or "")
        if not covered[key]:
            missing_records.append(row.get("id"))
        else:
            covered[key] -= 1
    if missing_records:
        fail(f"El grafo no contiene {len(missing_records)} registros normalizados; p. ej. {missing_records[:8]}")

    for edge in edges:
        if not isinstance(edge, dict):
            fail("Relación con formato inválido")
        source, target = edge.get("source"), edge.get("target")
        if source not in node_ids or target not in node_ids:
            fail(f"Relación colgante: {source} -> {target}")
        page_id = verify_provenance(edge, "Relación")
        confidence = edge.get("confidence")
        score = edge.get("confidence_score")
        if confidence not in {"EXTRACTED", "INFERRED", "AMBIGUOUS"}:
            fail(f"Relación {source} -> {target} con confianza inválida: {confidence}")
        valid_scores = {"EXTRACTED": {1.0}, "INFERRED": {0.95, 0.85, 0.75, 0.65, 0.55}, "AMBIGUOUS": {0.1, 0.2, 0.3}}
        if score not in valid_scores[confidence]:
            fail(f"Relación {source} -> {target} usa confidence_score incompatible: {score}")

    for edge in hyperedges:
        if not isinstance(edge, dict):
            fail(f"Hiperrrelación inválida: {edge}")
        verify_provenance(edge, "Hiperrrelación")
        confidence = edge.get("confidence")
        score = edge.get("confidence_score")
        valid_scores = {"EXTRACTED": {1.0}, "INFERRED": {0.95, 0.85, 0.75, 0.65, 0.55}}
        if confidence not in valid_scores or score not in valid_scores[confidence]:
            fail(f"Hiperrrelación {edge.get('id')} usa confianza inválida: {confidence}/{score}")
        unknown = set(edge.get("nodes", [])) - node_ids
        if unknown:
            fail(f"Hiperrrelación {edge.get('id')} referencia nodos inexistentes: {sorted(unknown)[:5]}")

    required = {"document", "operation", "concept", "resource"}
    if any("{" in str(row.get("path") or "") or row.get("parameters") or row.get("request") or row.get("response") for row in rows):
        required.add("field")
    if any(row.get("errors") not in (None, "", [], {}) for row in rows):
        required.add("error")
    kinds: Counter[str] = Counter()
    for node in nodes:
        if node.get("file_type"):
            kinds[str(node["file_type"])] += 1
        if node.get("kind"):
            kinds[str(node["kind"])] += 1
    absent = sorted(required - set(kinds))
    if absent:
        fail(f"Faltan tipos de nodo esperados: {absent}")
    print(f"Grafo válido: {len(nodes)} nodos, {len(edges)} relaciones, {len(hyperedges)} hiperrrelaciones; {len(manifest_by_id)} páginas y {len(rows)} registros cubiertos. Tipos: {dict(kinds)}")


if __name__ == "__main__":
    main()
