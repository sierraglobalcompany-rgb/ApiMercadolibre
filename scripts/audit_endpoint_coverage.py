from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "manifest.json"
OPERATIONS = ROOT / "data" / "operations.jsonl"
CAPTURES = ROOT / ".cache" / "captures"
OUTPUT = ROOT / "data" / "endpoint-coverage-report.json"
METHODS = ("GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS")
SEGMENT = r"[A-Za-z0-9_.$~{}-]+"
PATH = rf"/{SEGMENT}(?:/{SEGMENT}){{0,10}}"
METHOD_ROUTE = re.compile(rf"\b(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\s+(?:(?:al|a la|el|la)\s+)?(?:(?:recurso|ruta|endpoint|resource)\s+)?({PATH})", re.IGNORECASE)
METHOD_AFTER_PATH = re.compile(rf"({PATH})[^\n]{{0,100}}?\b(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\b")
CURL_METHOD = re.compile(r"-X\s+(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\b", re.IGNORECASE)
API_URL = re.compile(r"https?://api\.mercadolibre\.com(/[^\s\"'<>`]+)", re.IGNORECASE)
PATH_TOKEN = re.compile(rf"(?<![\w])({PATH})(?:\?[^\s\"'<>`]+)?")
COMMON_API_ROOTS = {
    "users", "items", "orders", "shipments", "sites", "categories", "questions", "answers", "messages", "visits", "payments", "claims", "pictures", "catalog", "products", "brands", "shipping", "packs", "billing", "invoices", "sellers", "price", "pricing-automation", "listing_types", "domains", "moderations", "currencies", "discounts", "coupons", "campaigns", "promotions", "sale_events", "sales", "subscriptions", "applications", "oauth", "notifications", "post-purchase", "advertising", "advertisers", "public-offers", "user-products", "inventory", "stock", "flex", "vis", "leads", "motor", "vehicle", "reviews", "reputation", "feedback", "questions", "shipments", "inbounds", "fiscal_documents", "billing-info", "seller-promotions", "deals", "preferences", "sites", "users", "items", "catalog_products", "seller", "order", "shipment", "item", "payment", "api",
}


def normalize_path(value: str) -> str:
    value = value.strip().rstrip(".,;:!?")
    if "?" in value:
        value = value.split("?", 1)[0]
    value = re.sub(r"\$([A-Za-z0-9_]+)", r"{\1}", value)
    value = re.sub(r":([A-Za-z_][A-Za-z0-9_]*)", r"{\1}", value)
    return re.sub(r"/+", "/", value).rstrip("/").casefold() or "/"


def path_shape(value: str) -> str:
    shaped = []
    for part in normalize_path(value).split("/"):
        if not part:
            continue
        if part.startswith("{") or part.endswith("_id"):
            shaped.append("{id}")
        elif part in {"mla", "mlb", "mlm", "mco", "mlu", "mlc", "mlv"}:
            shaped.append("{id}")
        elif re.fullmatch(r"\d+", part) or re.fullmatch(r"\d{4}-\d{2}-\d{2}", part):
            shaped.append("{id}")
        elif re.search(r"\d", part) and (len(part) >= 6 or part.startswith(("p-ml", "c-ml", "offer-ml", "dod-ml", "lgh-ml"))):
            shaped.append("{id}")
        elif re.fullmatch(r"[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}", part, re.IGNORECASE):
            shaped.append("{id}")
        elif re.match(r"^ml[a-z]-", part):
            shaped.append("{id}")
        else:
            shaped.append(part)
    return "/" + "/".join(shaped)


def main() -> None:
    parser = argparse.ArgumentParser(description="Reconcilia rutas HTTP detectables en capturas con operaciones y conceptos JSONL.")
    parser.add_argument("--strict", action="store_true", help="Falla si hay rutas detectables sin representar en los registros.")
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    rows = [json.loads(line) for line in OPERATIONS.read_text(encoding="utf-8").splitlines() if line.strip()]
    by_page_records: dict[str, list[dict]] = defaultdict(list)
    roots = set(COMMON_API_ROOTS)
    for row in rows:
        by_page_records[row["page_id"]].append(row)
        route = row.get("path") or ""
        if route.startswith("/"):
            roots.add(route.strip("/").split("/")[0].casefold())

    candidates: dict[tuple[str, str, str], dict] = {}
    for page in manifest:
        if page.get("status") != "captured":
            continue
        capture_path = CAPTURES / f"{page['id']}.json"
        if not capture_path.is_file():
            continue
        source_text = json.loads(capture_path.read_text(encoding="utf-8")).get("text", "")
        page_records = by_page_records.get(page["id"], [])
        recorded_ops = {(str(row.get("method") or "").upper(), normalize_path(str(row.get("path") or ""))) for row in page_records if row.get("kind") == "operation" and row.get("path")}
        recorded_paths = {normalize_path(str(row.get("path") or "")) for row in page_records if row.get("path")}
        recorded_op_shapes = {(method, path_shape(path)) for method, path in recorded_ops}
        recorded_path_shapes = {path_shape(path) for path in recorded_paths}

        mentions: Counter[tuple[str, str]] = Counter()
        raw_mentions: dict[tuple[str, str], str] = {}

        def note(method: str, raw_path: str) -> None:
            normalized = normalize_path(raw_path)
            if normalized == "/" or normalized.startswith(("/es_co/", "/es_ar/")):
                return
            key = (method, normalized)
            mentions[key] += 1
            raw_mentions.setdefault(key, raw_path)

        for match in METHOD_ROUTE.finditer(source_text):
            method, path = match.groups()
            note(method.upper(), path)
        for match in METHOD_AFTER_PATH.finditer(source_text):
            path, method = match.groups()
            note(method.upper(), path)
        for match in CURL_METHOD.finditer(source_text):
            method = match.group(1).upper()
            context = source_text[match.end():match.end() + 300]
            url = API_URL.search(context)
            if url:
                note(method, url.group(1))
        for match in PATH_TOKEN.finditer(source_text):
            path = normalize_path(match.group(1))
            if path == "/" or path.startswith(("/es_co/", "/es_ar/", "/images/", "/static/", "/assets/")):
                continue
            root = path.lstrip("/").split("/")[0].casefold()
            if root in roots:
                note("", match.group(1))

        for (method, path), count in mentions.items():
            root = path.lstrip("/").split("/")[0].casefold()
            segments = [segment for segment in path.split("/") if segment]
            if root not in roots and len(segments) < 2:
                continue
            if root not in roots and (root.isdigit() or root in {"a", "json", "xlsx", "eliminar"}):
                continue
            if re.search(r"\.(?:png|jpe?g|pdf|xlsx?|csv|zip)$", path, re.IGNORECASE):
                continue
            if re.match(r"^/users/(?:user|test|nombre|documents|desktop|downloads)(?:/|$)", path, re.IGNORECASE):
                continue
            shape = path_shape(path)
            candidate_key = (page["id"], method, path)
            if method and ((method, path) in recorded_ops or (method, shape) in recorded_op_shapes):
                status = "covered_operation"
                reason = None
            elif not method and (path in recorded_paths or shape in recorded_path_shapes):
                status = "covered_path_reference"
                reason = None
            elif not method and (
                any(recorded.startswith(path.rstrip("/") + "/") or recorded.startswith(path.rstrip("/") + "{") for recorded in recorded_paths if path != "/")
                or any(recorded.startswith(shape.rstrip("/") + "/") or recorded.startswith(shape.rstrip("/") + "{") for recorded in recorded_path_shapes if shape != "/")
            ):
                status = "covered_prefix_reference"
                reason = "La fuente menciona el recurso base; el corpus contiene rutas específicas bajo ese recurso."
            elif method and (
                any(recorded_method == method and recorded.startswith(path.rstrip("/") + "/") for recorded_method, recorded in recorded_ops if path != "/")
                or any(recorded_method == method and recorded.startswith(shape.rstrip("/") + "/") for recorded_method, recorded in recorded_op_shapes if shape != "/")
            ):
                status = "covered_prefix_operation"
                reason = "La fuente menciona una ruta base con método; el corpus contiene una operación más específica con el mismo método."
            elif method and (path in recorded_paths or shape in recorded_path_shapes):
                status = "method_not_represented"
                reason = "La captura muestra el método, pero el JSONL conserva la ruta sin una operación con ese método."
            else:
                status = "unrepresented"
                reason = "Ruta candidata detectada en el texto de la captura; revisar y añadir como operación, concepto o exclusión justificada."
            candidates[candidate_key] = {
                "page_id": page["id"],
                "title": page.get("title"),
                "source_url": page.get("url"),
                "source_updated_at": page.get("source_updated_at"),
                "captured_at": page.get("captured_at"),
                "method": method or None,
                "path": raw_mentions.get((method, path), path),
                "normalized_path": path,
                "mentions": count,
                "status": status,
                "reason": reason,
            }

    found = sorted(candidates.values(), key=lambda row: (row["page_id"], row["path"], row["method"] or ""))
    counts = Counter(row["status"] for row in found)
    report = {
        "scope": "Capturas públicas es_co y registros normalizados por página",
        "method_tokens": list(METHODS),
        "candidate_count": len(found),
        "status_counts": dict(counts),
        "unrepresented_count": counts.get("unrepresented", 0) + counts.get("method_not_represented", 0),
        "candidates": found,
    }
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Cobertura de rutas candidatas: {len(found)} referencias; {dict(counts)} -> {OUTPUT.relative_to(ROOT)}")
    if args.strict and report["unrepresented_count"]:
        raise SystemExit(f"{report['unrepresented_count']} rutas o métodos detectados sin registro equivalente.")


if __name__ == "__main__":
    main()
