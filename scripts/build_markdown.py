from __future__ import annotations

import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "manifest.json"
RECORDS = ROOT / "data" / "operations.jsonl"
MARKDOWN = ROOT / "docs" / "markdown"
TOPICS = ROOT / "docs" / "temas"


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-") or "tema"


def markdown_text(value: object) -> str:
    if value is None or value == "" or value == [] or value == {}:
        return "No documentado en la fuente."
    if isinstance(value, str):
        return value.strip() or "No documentado en la fuente."
    if isinstance(value, list):
        if not value:
            return "No documentado en la fuente."
        return "\n".join(f"- {markdown_text(item).replace(chr(10), ' ')}" for item in value)
    return "```json\n" + json.dumps(value, ensure_ascii=False, indent=2) + "\n```"


def parameters_text(value: object) -> str:
    if not isinstance(value, list) or not value:
        return "No documentado en la fuente."
    lines = []
    for item in value:
        if not isinstance(item, dict):
            lines.append(f"- {markdown_text(item)}")
            continue
        name = item.get("name") or "Parámetro"
        location = item.get("location")
        required = item.get("required")
        qualifiers = [str(location)] if location else []
        if required is not None:
            qualifiers.append("obligatorio" if required is True else "opcional")
        detail = f" ({', '.join(qualifiers)})" if qualifiers else ""
        description = item.get("description")
        suffix = f": {description}" if description else ""
        extras = {key: val for key, val in item.items() if key not in ("name", "location", "required", "description") and val not in (None, "")}
        if extras:
            suffix += " " + json.dumps(extras, ensure_ascii=False, sort_keys=True)
        lines.append(f"- `{name}`{detail}{suffix}")
    return "\n".join(lines)


def render_operation(item: dict) -> str:
    lines = [
        f"### {item['name']}",
        "",
        f"**Método:** `{item.get('method') or 'No documentado'}`  ",
        f"**Ruta:** `{item.get('path') or 'No documentada'}`  ",
        f"**Autenticación:** {markdown_text(item.get('auth'))}",
        "",
        item["summary"],
        "",
        "**Parámetros**",
        "",
        parameters_text(item.get("parameters")),
        "",
        "**Solicitud**",
        "",
        markdown_text(item.get("request")),
        "",
        "**Respuesta**",
        "",
        markdown_text(item.get("response")),
        "",
        "**Errores documentados**",
        "",
        markdown_text(item.get("errors")),
        "",
        "**Ejemplos**",
        "",
        markdown_text(item.get("examples")),
        "",
    ]
    return "\n".join(lines)


def render_concept(item: dict) -> str:
    lines = [f"### {item['name']}", "", item["summary"], ""]
    if item.get("path"):
        lines += ["**Ruta mencionada:** `" + str(item["path"]) + "`  ", "**Método HTTP:** No documentado en la fuente.", ""]
    if item.get("auth"):
        lines += ["**Autenticación:** " + markdown_text(item["auth"]), ""]
    if item.get("parameters"):
        lines += ["**Parámetros documentados**", "", parameters_text(item["parameters"]), ""]
    if item.get("request"):
        lines += ["**Solicitud**", "", markdown_text(item["request"]), ""]
    if item.get("response"):
        lines += ["**Respuesta**", "", markdown_text(item["response"]), ""]
    if item.get("errors"):
        lines += ["**Errores documentados**", "", markdown_text(item["errors"]), ""]
    if item.get("examples"):
        lines += ["**Ejemplos documentados**", "", markdown_text(item["examples"]), ""]
    return "\n".join(lines)


def strip_frontmatter(content: str) -> str:
    if content.startswith("---\n"):
        _, _, content = content.partition("\n---\n")
    return content.strip()


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    records = [json.loads(line) for line in RECORDS.read_text(encoding="utf-8").splitlines() if line.strip()]
    by_page: dict[str, list[dict]] = defaultdict(list)
    for row in records:
        by_page[row["page_id"]].append(row)

    grouped: dict[str, list[dict]] = defaultdict(list)
    for page in manifest:
        doc_path = MARKDOWN / f"{page['id']}.md"
        content = doc_path.read_text(encoding="utf-8")
        marker = "## Operaciones de API\n"
        base, found, _ = content.partition(marker)
        if not found:
            base = content.rstrip() + "\n\n"
        rows = by_page.get(page["id"], [])
        concepts = [row for row in rows if row["kind"] == "concept"]
        operations = [row for row in rows if row["kind"] == "operation"]
        section = marker
        if concepts:
            section += "\n## Conceptos y recursos asociados\n\n"
            for concept in concepts:
                section += render_concept(concept)
        section += "## Operaciones de API\n\n"
        if operations:
            section += "\n".join(render_operation(row) for row in operations)
        else:
            section += "La página no documenta una operación HTTP concreta.\n"
        source = page.get("url")
        section += f"\n**Fuente:** [{source}]({source})  \n**Captura:** {page.get('captured_at') or 'No documentada'}\n"
        doc_path.write_text(base.rstrip() + "\n\n" + section, encoding="utf-8")
        grouped[page.get("section") or "Portal"].append({**page, "markdown": strip_frontmatter(base + section)})

    TOPICS.mkdir(parents=True, exist_ok=True)
    index_lines = [
        "# Índice de la documentación Mercado Libre `es_co`",
        "",
        "Corpus de consulta basado en el portal público de desarrolladores. Las fichas están resumidas con redacción propia y enlazan a sus fuentes oficiales.",
        "",
        f"Páginas: **{len(manifest)}** · Registros operativos y conceptuales: **{len(records)}**",
        "",
        "## Áreas",
        "",
    ]
    for section_name in sorted(grouped, key=str.casefold):
        rows = grouped[section_name]
        topic_file = slugify(section_name) + ".md"
        topic_path = TOPICS / topic_file
        topic_lines = [
            f"# {section_name}",
            "",
            f"{len(rows)} páginas del portal oficial en esta área.",
            "",
        ]
        index_lines += [f"## {section_name}", "", f"[Abrir documentación del tema](../temas/{topic_file}) — {len(rows)} páginas", ""]
        for page in rows:
            page_id = page["id"]
            title = page["title"]
            source_url = page["url"]
            source_date = page.get("source_updated_at") or "No documentada"
            topic_lines += [
                f"## [{title}](../markdown/{page_id}.md)",
                "",
                f"Actualización indicada por la fuente: {source_date}. Captura: {page.get('captured_at') or 'No documentada'}.",
                "",
                f"Fuente: [{source_url}]({source_url})",
                "",
                page["markdown"],
                "",
                "---",
                "",
            ]
            index_lines.append(f"- [{title}](./{page_id}.md) · actualización de fuente: {source_date}")
        topic_path.write_text("\n".join(topic_lines), encoding="utf-8")
        index_lines.append("")

    INDEX = MARKDOWN / "INDEX.md"
    INDEX.write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")
    print(f"Markdown generado: {len(manifest)} fichas, {len(grouped)} temas, {len(records)} registros.")


if __name__ == "__main__":
    main()
