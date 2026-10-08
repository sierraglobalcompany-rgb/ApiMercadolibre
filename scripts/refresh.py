from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "manifest.json"
CAPTURES = ROOT / ".cache" / "captures"
REPORT = ROOT / "data" / "refresh-report.json"


def read_doc_sha(path: Path) -> str | None:
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    match = re.search(r"(?m)^sha256:\s*['\"]?([a-f0-9]{64})['\"]?\s*$", text)
    return match.group(1) if match else None


def analyze() -> dict:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    groups: dict[str, list[dict]] = {key: [] for key in ("unchanged", "changed", "new", "unavailable", "capture_mismatch")}
    for row in manifest:
        page_id = row.get("id", "")
        capture_path = CAPTURES / f"{page_id}.json"
        doc_path = ROOT / "docs" / "markdown" / f"{page_id}.md"
        detail = {"id": page_id, "title": row.get("title"), "url": row.get("url"), "status": row.get("status")}
        if row.get("status") != "captured":
            groups["unavailable"].append({**detail, "reason": row.get("reason") or f"Estado: {row.get('status', 'desconocido')}"})
            continue
        if not capture_path.is_file():
            groups["capture_mismatch"].append({**detail, "reason": "No existe captura local en .cache/captures"})
            continue
        capture = json.loads(capture_path.read_text(encoding="utf-8"))
        observed_hash = hashlib.sha256(str(capture.get("text") or "").encode("utf-8")).hexdigest()
        if observed_hash != row.get("sha256"):
            groups["capture_mismatch"].append({**detail, "reason": "La huella del archivo de captura no coincide con el manifiesto"})
            continue
        previous_hash = read_doc_sha(doc_path)
        if previous_hash is None:
            groups["new"].append({**detail, "sha256": row.get("sha256")})
        elif previous_hash == row.get("sha256"):
            groups["unchanged"].append({**detail, "sha256": row.get("sha256")})
        else:
            groups["changed"].append({**detail, "previous_sha256": previous_hash, "sha256": row.get("sha256")})
    return {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "manifest_path": "data/manifest.json",
        "counts": {key: len(value) for key, value in groups.items()},
        "pages": groups,
    }


def rebuild(report: dict) -> None:
    blocking = report["pages"]["new"] + report["pages"]["changed"] + report["pages"]["unavailable"] + report["pages"]["capture_mismatch"]
    if blocking:
        names = ", ".join(item["id"] for item in blocking[:12])
        raise SystemExit(f"No regeneré los derivados: hay {len(blocking)} páginas nuevas, modificadas, inaccesibles o con captura inconsistente. Actualiza las fichas/registros y resuelve capturas primero. Ejemplos: {names}")
    commands = [
        [sys.executable, "scripts/merge_extractions.py"],
        [sys.executable, "scripts/audit_endpoint_coverage.py"],
        [sys.executable, "scripts/reconcile_endpoint_coverage.py", "--apply"],
        [sys.executable, "scripts/merge_extractions.py"],
        [sys.executable, "scripts/build_markdown.py"],
        [sys.executable, "scripts/validate_corpus.py"],
        [sys.executable, "scripts/audit_endpoint_coverage.py", "--strict"],
        [sys.executable, "scripts/build_index.py"],
        [sys.executable, "scripts/normalize_graph_extractions.py"],
        [sys.executable, "scripts/build_graph.py"],
        [sys.executable, "scripts/validate_graph.py"],
        [sys.executable, "scripts/build_pdf.py"],
    ]
    for command in commands:
        subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Compara las capturas con el corpus y, opcionalmente, regenera los artefactos locales.")
    parser.add_argument("--rebuild", action="store_true", help="Regenera todos los derivados si las fuentes coinciden con las fichas revisadas.")
    args = parser.parse_args()
    report = analyze()
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Informe de refresco:", report["counts"])
    if args.rebuild:
        rebuild(report)
        print("Derivados regenerados desde el corpus revisado.")
    elif sum(report["counts"][key] for key in ("changed", "new", "unavailable", "capture_mismatch")) == 0:
        print("Sin cambios. No se modificaron índices, grafo ni exportaciones.")
    else:
        print("Revisa data/refresh-report.json, actualiza las fichas y los registros afectados, y vuelve a ejecutar con --rebuild.")


if __name__ == "__main__":
    main()
