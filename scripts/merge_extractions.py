from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "manifest.json"
EXTRACTED = ROOT / "data" / "extracted"
OUTPUT = ROOT / "data" / "operations.jsonl"


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    pages = {row["id"]: row for row in manifest}
    order = {row["id"]: index for index, row in enumerate(manifest)}
    records: list[dict] = []
    seen: set[str] = set()
    for path in sorted(EXTRACTED.glob("batch-*.jsonl")):
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"JSON inválido en {path.name}:{line_no}: {exc}") from exc
            page_id = item.get("page_id")
            source = pages.get(page_id)
            if not source:
                raise SystemExit(f"{path.name}:{line_no}: page_id fuera del manifiesto: {page_id}")
            if item.get("id") in seen:
                raise SystemExit(f"ID duplicado en corpus: {item.get('id')}")
            seen.add(item.get("id"))
            if item.get("source_url") != source.get("url"):
                raise SystemExit(f"URL fuente incorrecta: {item.get('id')}")
            for key in ("source_updated_at", "captured_at", "sha256", "section", "subsection"):
                if item.get(key) != source.get(key):
                    raise SystemExit(f"{key} no coincide con el manifiesto: {item.get('id')}")
            if item.get("kind") not in ("operation", "concept"):
                raise SystemExit(f"Tipo no soportado: {item.get('id')}")
            if item["kind"] == "operation" and (not item.get("method") or not item.get("path")):
                raise SystemExit(f"Operación sin método/ruta: {item.get('id')}")
            if not item.get("name") or not item.get("summary"):
                raise SystemExit(f"Registro sin nombre/resumen: {item.get('id')}")
            item.setdefault("auth", None)
            for key in ("parameters", "errors", "examples"):
                item.setdefault(key, [])
            item.setdefault("request", None)
            item.setdefault("response", None)
            records.append(item)

    counts = Counter(item["page_id"] for item in records)
    missing = sorted(set(pages) - set(counts))
    if missing:
        raise SystemExit(f"No hay registros para {len(missing)} páginas; p. ej. {missing[:8]}")

    records.sort(key=lambda item: (order[item["page_id"]], 0 if item["kind"] == "concept" else 1, item["id"]))
    OUTPUT.write_text("".join(json.dumps(item, ensure_ascii=False) + "\n" for item in records), encoding="utf-8")
    kinds = Counter(item["kind"] for item in records)
    print(f"Unidos {len(records)} registros: {dict(kinds)}; {len(counts)}/{len(pages)} páginas con cobertura -> {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
