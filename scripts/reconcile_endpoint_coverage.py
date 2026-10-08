from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "manifest.json"
REPORT = ROOT / "data" / "endpoint-coverage-report.json"
BATCHES = ROOT / "data" / "extracted"
BATCH_MANIFESTS = ROOT / ".cache" / "extraction-batches"


def normalized_path(value: str) -> str:
    value = re.sub(r"\$([A-Za-z0-9_]+)", r"{\1}", value)
    value = re.sub(r":([A-Za-z_][A-Za-z0-9_]*)", r"{\1}", value)
    return re.sub(r"/+", "/", value.split("?", 1)[0].rstrip(".,;:!?")).rstrip("/").casefold() or "/"


def main() -> None:
    parser = argparse.ArgumentParser(description="Añade a los lotes las rutas detectadas en capturas que aún no tienen registro.")
    parser.add_argument("--apply", action="store_true", help="Escribe registros atribuidos en los lotes de extracción.")
    args = parser.parse_args()
    if not args.apply:
        raise SystemExit("Usa --apply para añadir las referencias de ruta detectadas.")

    manifest = {row["id"]: row for row in json.loads(MANIFEST.read_text(encoding="utf-8"))}
    coverage = json.loads(REPORT.read_text(encoding="utf-8"))
    batch_for_page: dict[str, int] = {}
    for batch_file in sorted(BATCH_MANIFESTS.glob("batch-*.json")):
        batch = json.loads(batch_file.read_text(encoding="utf-8"))
        for page in batch.get("pages", []):
            batch_for_page[page["id"]] = batch["batch"]

    rows_by_batch: dict[int, list[dict]] = {}
    existing: set[tuple[str, str, str]] = set()
    for batch_file in sorted(BATCHES.glob("batch-*.jsonl")):
        batch_no = int(re.search(r"batch-(\d+)", batch_file.stem).group(1))
        rows = [json.loads(line) for line in batch_file.read_text(encoding="utf-8").splitlines() if line.strip()]
        rows_by_batch[batch_no] = rows
        for row in rows:
            existing.add((row["page_id"], str(row.get("method") or "").upper(), normalized_path(str(row.get("path") or ""))))

    added = []
    for candidate in coverage.get("candidates", []):
        if candidate.get("status") not in ("unrepresented", "method_not_represented"):
            continue
        page_id = candidate["page_id"]
        source = manifest[page_id]
        batch_no = batch_for_page[page_id]
        method = str(candidate.get("method") or "").upper() or None
        raw_path = str(candidate.get("path") or "").strip().rstrip(".,;:!?")
        split = urlsplit(raw_path)
        path = split.path or raw_path
        path = re.sub(r"\$([A-Za-z0-9_]+)", r"{\1}", path)
        path = re.sub(r":([A-Za-z_][A-Za-z0-9_]*)", r"{\1}", path)
        key = (page_id, method or "", normalized_path(path))
        if key in existing:
            continue

        query_params = [
            {
                "name": name,
                "location": "query",
                "required": None,
                "description": "Aparece en una URL de la fuente; su obligatoriedad no está documentada.",
            }
            for name, _value in parse_qsl(split.query, keep_blank_values=True)
        ]
        label = f"{method} {path}" if method else path
        digest = hashlib.sha256(label.encode("utf-8")).hexdigest()[:10]
        record_id = f"{page_id}--referencia-{method.lower() if method else 'ruta'}-{digest}"
        if method:
            kind = "operation"
            name = f"Referencia HTTP {method} {path}"
            summary = f"La captura muestra la solicitud {method} a {path}. La fuente no documenta otros detalles técnicos en esta referencia; consulta la ficha oficial para el contexto completo."
        else:
            kind = "concept"
            name = f"Ruta mencionada {path}"
            summary = f"La fuente menciona la ruta {path}, pero no documenta explícitamente el método HTTP ni describe aquí una operación completa."
        record = {
            "id": record_id,
            "page_id": page_id,
            "kind": kind,
            "name": name,
            "summary": summary,
            "method": method,
            "path": path,
            "auth": None,
            "parameters": query_params,
            "request": None,
            "response": None,
            "errors": [],
            "examples": ["La referencia de método y ruta se encontró en el texto capturado de la página."],
            "section": source.get("section"),
            "subsection": source.get("subsection"),
            "source_url": source.get("url"),
            "source_updated_at": source.get("source_updated_at"),
            "captured_at": source.get("captured_at"),
            "sha256": source.get("sha256"),
        }
        rows_by_batch[batch_no].append(record)
        existing.add(key)
        added.append(record)

    for batch_no, rows in rows_by_batch.items():
        output = BATCHES / f"batch-{batch_no:02}.jsonl"
        rows.sort(key=lambda row: (row["page_id"], row["id"]))
        output.write_text("".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows), encoding="utf-8")

    by_kind: dict[str, int] = {}
    for row in added:
        by_kind[row["kind"]] = by_kind.get(row["kind"], 0) + 1
    print(f"Rutas añadidas desde referencias explícitas de la fuente: {len(added)}; {by_kind}")


if __name__ == "__main__":
    main()
