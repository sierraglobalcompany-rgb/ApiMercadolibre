from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "manifest.json"
LINKS = ROOT / "data" / "link-audit.json"
OUTPUT = ROOT / "data" / "link-audit-report.json"


def canonical_path(url: str) -> str:
    parts = urlsplit(url)
    return unquote(parts.path.rstrip("/"))


def main() -> None:
    pages = json.loads(MANIFEST.read_text(encoding="utf-8"))
    link_payload = json.loads(LINKS.read_text(encoding="utf-8"))
    known = {canonical_path(row["url"]): row for row in pages if row.get("url")}
    by_slug = {str(row.get("id")): row for row in pages if row.get("id")}
    report: list[dict] = []
    counts: Counter[str] = Counter()

    for link in link_payload.get("links", []):
        parsed = urlsplit(link.get("url", ""))
        path = canonical_path(link.get("url", ""))
        target = known.get(path)
        slug_target = by_slug.get(path.rstrip("/").split("/")[-1])
        if target:
            status = "captured"
            reason = "La ruta ya aparece en el manifiesto y su página fue capturada."
            target_id = target.get("id")
        elif slug_target and parsed.netloc == "developers.mercadolibre.com.co":
            status = "captured_locale_variant"
            reason = "El enlace usa otra variante de locale o una ruta sin locale, pero el mismo slug documental ya fue capturado desde el índice es_co."
            target_id = slug_target.get("id")
        elif "/es_co/es_ar/" in path or "/es_co/pt_br/" in path:
            status = "excluded_invalid_locale_path"
            reason = "La URL mezcla el prefijo es_co con otra ruta de locale; no es una ruta documental canónica."
            target_id = None
        elif "%E2%80%9C" in link.get("url", "").upper() or "%E2%80%9D" in link.get("url", "").upper():
            status = "excluded_malformed_url"
            reason = "El enlace contiene comillas tipográficas codificadas en la propia ruta."
            target_id = None
        elif path.rstrip("/").split("/")[-1].startswith("AGREGAR_LINK"):
            status = "excluded_placeholder"
            reason = "La fuente contiene un marcador AGREGAR_LINK en vez de una página documental."
            target_id = None
        elif parsed.netloc == "developers.mercadolibre.com.co" and not path.startswith("/es_co/"):
            status = "excluded_out_of_scope"
            reason = "El destino está fuera del alcance del portal de documentación es_co."
            target_id = None
        else:
            status = "review_required"
            reason = "No se encontró una página capturada equivalente; revisar manualmente antes de ampliar el corpus."
            target_id = None

        counts[status] += 1
        report.append({
            **link,
            "status": status,
            "reason": reason,
            "target_page_id": target_id,
        })

    result = {
        "schema_version": 1,
        "source_pages": len(pages),
        "article_links": len(report),
        "status_counts": dict(sorted(counts.items())),
        "links": report,
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Auditoría: {len(report)} enlaces; {dict(counts)} -> {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
