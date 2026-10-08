from __future__ import annotations

import json
import hashlib
import re
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

from graphify.analyze import god_nodes, suggest_questions, surprising_connections
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.detect import detect
from graphify.diagnostics import diagnose_extraction
from graphify.export import to_json
from graphify.report import generate

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "graphify-out"
DOCS = ROOT / "docs" / "markdown"
MANIFEST_PATH = ROOT / "data" / "manifest.json"
OPERATIONS_PATH = ROOT / "data" / "operations.jsonl"
CHUNKS = ROOT / "data" / "graph-extractions"
GRAPH_PATH = OUT / "graph.json"


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "_", value).strip("_") or "concept"


def graph_id(source_file: Path, label: str, identity: str | None = None) -> str:
    rel = source_file.resolve().relative_to(ROOT).with_suffix("").as_posix()
    entity = identity if identity is not None else label
    suffix = hashlib.sha256(entity.encode("utf-8")).hexdigest()[:10] if identity is not None else ""
    identity_part = f"record_{normalized(entity)}_{suffix}" if identity is not None else normalized(label)
    return f"{normalized(rel.replace('/', '_'))}_{identity_part}"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def resolve_source_path(value: str) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (ROOT / path).resolve()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    CHUNKS.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    pages = {row["id"]: row for row in manifest if row.get("status") == "captured"}
    docs_by_path = {str((DOCS / f"{page_id}.md").resolve()): page for page_id, page in pages.items()}
    docs_by_path[str((DOCS / "INDEX.md").resolve())] = {"id": "documentation-index", "title": "Índice de documentación", "url": "https://developers.mercadolibre.com.co/es_co/guia-para-producto", "captured_at": None, "sha256": None, "section": "Portal"}

    fragments = sorted(CHUNKS.glob("batch-*.json"))
    if not fragments:
        raise SystemExit(f"No hay extracciones semánticas de Graphify en {CHUNKS}. Completa primero la extracción por agentes de los Markdown.")
    nodes_by_id: dict[str, dict] = {}
    edges_by_key: dict[tuple, dict] = {}
    hyperedges: dict[str, dict] = {}
    for fragment in fragments:
        content = json.loads(fragment.read_text(encoding="utf-8"))
        for node in content.get("nodes", []):
            if not isinstance(node, dict) or not node.get("id") or not node.get("label") or not node.get("source_file"):
                raise SystemExit(f"Nodo sin id/label/source_file en {fragment.name}")
            key = str(resolve_source_path(node["source_file"]))
            page = docs_by_path.get(key)
            if page:
                node.setdefault("source_url", page.get("url"))
                node.setdefault("captured_at", page.get("captured_at"))
                node.setdefault("sha256", page.get("sha256"))
                node.setdefault("page_id", page.get("id"))
            nodes_by_id[node["id"]] = node
        for edge in content.get("edges", []):
            if not isinstance(edge, dict) or not edge.get("source") or not edge.get("target") or not edge.get("source_file"):
                raise SystemExit(f"Relación sin extremos/source_file en {fragment.name}")
            if edge["source"] == edge["target"]:
                # A reference from a document node to itself adds no searchable
                # relationship and can appear after semantic ID normalization.
                continue
            key = (edge["source"], edge["target"], edge.get("relation"), edge.get("source_file"))
            edges_by_key[key] = edge
        for hyperedge in content.get("hyperedges", []):
            if isinstance(hyperedge, dict) and hyperedge.get("id"):
                source_file = str(resolve_source_path(hyperedge.get("source_file") or ""))
                source_page = docs_by_path.get(source_file)
                if source_page:
                    hyperedge.setdefault("source_url", source_page.get("url"))
                    hyperedge.setdefault("captured_at", source_page.get("captured_at"))
                    hyperedge.setdefault("sha256", source_page.get("sha256"))
                    hyperedge.setdefault("page_id", source_page.get("id"))
                hyperedges[hyperedge["id"]] = hyperedge

    def add_node(source_file: Path, label: str, identity: str | None = None, **attrs: object) -> str:
        page = docs_by_path.get(str(source_file.resolve()), {})
        node_id = graph_id(source_file, label, identity)
        existing = nodes_by_id.get(node_id, {})
        nodes_by_id[node_id] = {
            **existing,
            "id": node_id,
            "label": label,
            "file_type": existing.get("file_type") or "concept",
            "source_file": str(source_file.resolve()),
            "source_url": existing.get("source_url") or page.get("url"),
            "captured_at": existing.get("captured_at") or page.get("captured_at"),
            "sha256": existing.get("sha256") or page.get("sha256"),
            "page_id": existing.get("page_id") or page.get("id"),
            "section": existing.get("section") or page.get("section"),
            **{key: value for key, value in attrs.items() if value is not None},
        }
        return node_id

    def add_edge(source: str, target: str, source_file: Path, relation: str = "references", confidence: str = "EXTRACTED") -> None:
        if source == target:
            return
        page = docs_by_path.get(str(source_file.resolve()), {})
        edge = {
            "source": source,
            "target": target,
            "relation": relation,
            "confidence": confidence,
            "confidence_score": 1.0 if confidence == "EXTRACTED" else 0.75,
            "source_file": str(source_file.resolve()),
            "source_url": page.get("url"),
            "captured_at": page.get("captured_at"),
            "sha256": page.get("sha256"),
            "page_id": page.get("id"),
            "weight": 1.0,
        }
        edges_by_key[(source, target, relation, edge["source_file"])] = edge

    # Add deterministic resource, operation, field, and error nodes from the
    # normalized records so Graphify always contains the technical index.
    records = load_jsonl(OPERATIONS_PATH)
    for row in records:
        page_id = row["page_id"]
        source_file = DOCS / f"{page_id}.md"
        page = pages[page_id]
        page_node = add_node(source_file, page["title"], file_type="document", kind="page", summary=row.get("summary"))
        if row.get("kind") == "operation":
            method = str(row.get("method") or "").upper()
            route = str(row.get("path") or "")
            record_tag = hashlib.sha256(str(row["id"]).encode("utf-8")).hexdigest()[:8]
            label = f"{row.get('name') or 'Operación'} — {method} {route} · {record_tag}".strip(" —")
            operation_id = add_node(source_file, label, identity=f"operation-{row['id']}", kind="operation", method=method, path=route, name=row.get("name"), summary=row.get("summary"), auth=row.get("auth"), parameters=row.get("parameters"), request=row.get("request"), response=row.get("response"), errors=row.get("errors"), examples=row.get("examples"))
            add_edge(page_node, operation_id, source_file)
            resource = row.get("resource")
            if not resource and route:
                resource = "/" + route.strip("/").split("/")[0]
            if resource:
                resource_label = f"Recurso: {resource}"
                resource_id = add_node(source_file, resource_label, kind="resource", resource=resource)
                add_edge(operation_id, resource_id, source_file, "references", "INFERRED" if not row.get("resource") else "EXTRACTED")

            fields: set[str] = set()
            fields.update(re.findall(r"\{([^}]+)\}", route))
            for field_key in ("parameters", "request", "response"):
                value = row.get(field_key)
                if isinstance(value, list):
                    def collect(items: object, prefix: str = "") -> None:
                        if isinstance(items, list):
                            for element in items:
                                collect(element, prefix)
                        elif isinstance(items, dict):
                            for key, child in items.items():
                                field_path = f"{prefix}.{key}" if prefix else str(key)
                                fields.add(field_path)
                                collect(child, field_path)
                        elif isinstance(items, str) and items:
                            # Structured parameter names and explicit property tables often arrive as lists of objects.
                            return
                    collect(value)
                elif isinstance(value, dict):
                    def collect_object(items: dict, prefix: str = "") -> None:
                        for key, child in items.items():
                            field_path = f"{prefix}.{key}" if prefix else str(key)
                            fields.add(field_path)
                            if isinstance(child, dict):
                                collect_object(child, field_path)
                            elif isinstance(child, list):
                                collect(child, field_path)
                    collect_object(value)
            for field in sorted(fields):
                field_id = add_node(source_file, f"Campo: {field}", identity=f"field-{row['id']}-{field}", kind="field", field=field, operation_path=route)
                add_edge(operation_id, field_id, source_file, "conceptually_related_to")

            errors = row.get("errors")
            error_items = errors if isinstance(errors, list) else [errors] if errors not in (None, "", {}) else []
            for error in error_items:
                if isinstance(error, dict):
                    error_code = error.get("code") or error.get("status") or error.get("name")
                    description = error.get("message") or error.get("description") or error.get("detail")
                    error_label = f"Error {error_code}: {description}" if error_code and description else str(error_code or description or json.dumps(error, ensure_ascii=False, sort_keys=True))
                else:
                    error_label = str(error)
                error_label = error_label[:220]
                error_id = add_node(source_file, f"Error: {error_label}", identity=f"error-{row['id']}-{error_label}", kind="error", code=error.get("code") if isinstance(error, dict) else None, description=error_label)
                add_edge(operation_id, error_id, source_file)
        else:
            record_tag = hashlib.sha256(str(row["id"]).encode("utf-8")).hexdigest()[:8]
            concept_id = add_node(source_file, f"{row['name']} · {record_tag}", identity=f"concept-{row['id']}", kind="concept", name=row.get("name"), summary=row.get("summary"), method=row.get("method"), path=row.get("path"), auth=row.get("auth"), parameters=row.get("parameters"), request=row.get("request"), response=row.get("response"), errors=row.get("errors"), examples=row.get("examples"))
            add_edge(page_node, concept_id, source_file)

    # Stamp provenance on every semantic edge/node, keyed by its originating Markdown.
    for edge in edges_by_key.values():
        source_file = str(resolve_source_path(edge["source_file"]))
        page = docs_by_path.get(source_file)
        if page:
            edge.setdefault("source_url", page.get("url"))
            edge.setdefault("captured_at", page.get("captured_at"))
            edge.setdefault("sha256", page.get("sha256"))
            edge.setdefault("page_id", page.get("id"))

    extraction = {
        "nodes": list(nodes_by_id.values()),
        "edges": list(edges_by_key.values()),
        "hyperedges": list(hyperedges.values()),
        "input_tokens": 0,
        "output_tokens": 0,
    }
    dangling = [edge for edge in extraction["edges"] if edge["source"] not in nodes_by_id or edge["target"] not in nodes_by_id]
    if dangling:
        raise SystemExit(f"Hay {len(dangling)} relaciones Graphify sin nodo de origen/destino; corrige fragmentos antes de construir.")
    diag = diagnose_extraction(extraction, directed=True, root=ROOT)
    (OUT / ".graphify_diagnostics.json").write_text(json.dumps(diag, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    graph = build_from_json(extraction, directed=True, root=ROOT)
    communities = cluster(graph)
    scores = score_all(graph, communities)
    sections: dict[int, Counter] = defaultdict(Counter)
    node_community = {node_id: community for community, members in communities.items() for node_id in members}
    for node_id, attrs in graph.nodes(data=True):
        community = node_community.get(node_id)
        source_page = docs_by_path.get(str((ROOT / attrs.get("source_file", "")).resolve()), {})
        section = attrs.get("section") or source_page.get("section") or "API Mercado Libre"
        if community is not None:
            sections[community][section] += 1
    labels = {community: "Mercado Libre — " + sections[community].most_common(1)[0][0] for community in communities if sections[community]}
    hubs = god_nodes(graph, top_n=15)
    surprises = surprising_connections(graph, communities=communities, top_n=12)
    questions = suggest_questions(graph, communities, labels, top_n=12)
    if not to_json(graph, communities, str(GRAPH_PATH), force=True, community_labels=labels):
        raise SystemExit("Graphify no guardó graph.json.")

    # Graphify can retain the original edge endpoint attributes alongside
    # NetworkX's endpoints. During node-link serialization, a document twin
    # remap may therefore surface one redundant document-to-itself link even
    # though the in-memory graph has no self-loop. Such a link carries no
    # context and makes MCP lookups noisier, so remove it from the published
    # graph artifact before exporting HTML or serving it over MCP.
    graph_data = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    graph_data["links"] = [
        link for link in graph_data.get("links", [])
        if link.get("source") != link.get("target")
    ]
    GRAPH_PATH.write_text(json.dumps(graph_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    detection = detect(DOCS)
    (OUT / ".graphify_detect.json").write_text(json.dumps(detection, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = generate(graph, communities, scores, labels, hubs, surprises, detection, {"input_tokens": 0, "output_tokens": 0}, str(ROOT), suggested_questions=questions)
    (OUT / "GRAPH_REPORT.md").write_text(report.rstrip() + "\n", encoding="utf-8")
    cli = ROOT / ".venv" / "Scripts" / "graphify.exe"
    subprocess.run([str(cli), "export", "html", "--graph", str(GRAPH_PATH)], cwd=ROOT, check=True)
    print(f"Graphify: {graph.number_of_nodes()} nodos, {graph.number_of_edges()} relaciones, {len(communities)} comunidades; diagnóstico en graphify-out/.graphify_diagnostics.json")


if __name__ == "__main__":
    main()
