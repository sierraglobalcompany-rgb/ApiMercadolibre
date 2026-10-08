from __future__ import annotations

import html
import json
import re
import unicodedata
from datetime import datetime
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import quoteattr

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "manifest.json"
MARKDOWN = ROOT / "docs" / "markdown"
OUTPUT = ROOT / "docs" / "mercadolibre-api-es-co.pdf"
PAGE_SIZE = A4


def register_fonts() -> tuple[str, str, str, str]:
    fonts_dir = Path("C:/Windows/Fonts")
    candidates = [
        ("Arial", fonts_dir / "arial.ttf"),
        ("Arial-Bold", fonts_dir / "arialbd.ttf"),
        ("Arial-Italic", fonts_dir / "ariali.ttf"),
        ("Consolas", fonts_dir / "consola.ttf"),
    ]
    loaded = []
    for name, path in candidates:
        if path.is_file():
            try:
                pdfmetrics.registerFont(TTFont(name, str(path)))
                loaded.append(name)
            except Exception:
                loaded.append("")
        else:
            loaded.append("")
    if all(loaded):
        pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold", italic="Arial-Italic", boldItalic="Arial-Bold")
        return "Arial", "Arial-Bold", "Arial-Italic", "Consolas"
    return "Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Courier"


BODY_FONT, BOLD_FONT, ITALIC_FONT, CODE_FONT = register_fonts()


def safe_pdf_text(value: str) -> str:
    return value.replace("\u2010", "-").replace("\u2011", "-").replace("\u2012", "-").replace("\u2013", "-").replace("\u2014", "-")


def inline_markup(value: str) -> str:
    value = safe_pdf_text(value)
    token = re.compile(r"(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*|\[[^\]]+\]\([^)]+\))")
    output = []
    cursor = 0
    for match in token.finditer(value):
        output.append(html.escape(value[cursor:match.start()]))
        item = match.group(0)
        if item.startswith("`"):
            output.append(f'<font name="{CODE_FONT}">{html.escape(item[1:-1])}</font>')
        elif item.startswith("**"):
            output.append(f"<b>{html.escape(item[2:-2])}</b>")
        elif item.startswith("*"):
            output.append(f"<i>{html.escape(item[1:-1])}</i>")
        else:
            anchor = re.match(r"\[([^\]]+)\]\(([^)]+)\)", item)
            if anchor:
                label, url = anchor.groups()
                url = html.unescape(url.strip())
                output.append(f'<link href={quoteattr(url)} color="#1769aa">{html.escape(label)}</link>')
        cursor = match.end()
    output.append(html.escape(value[cursor:]))
    return "".join(output).replace("\n", "<br/>")


def strip_frontmatter(content: str) -> str:
    if content.startswith("---\n"):
        _, _, content = content.partition("\n---\n")
    return content.strip()


def capture_date_labels(manifest: list[dict]) -> tuple[str, str]:
    dates = []
    for page in manifest:
        value = page.get("captured_at")
        if value:
            try:
                dates.append(datetime.fromisoformat(str(value).replace("Z", "+00:00")).date())
            except ValueError:
                continue
    if not dates:
        return "fecha no disponible", "fecha no disponible"
    capture_date = max(dates)
    month_names = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    long_date = f"{capture_date.day} de {month_names[capture_date.month - 1]} de {capture_date.year}"
    short_date = capture_date.strftime("%d/%m/%Y")
    return long_date, short_date


def styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "Title": ParagraphStyle("MLTitle", parent=base["Title"], fontName=BOLD_FONT, fontSize=28, leading=34, textColor=colors.HexColor("#14213d"), alignment=TA_LEFT, spaceAfter=8 * mm),
        "Subtitle": ParagraphStyle("MLSubtitle", parent=base["Normal"], fontName=BODY_FONT, fontSize=13, leading=19, textColor=colors.HexColor("#506078"), spaceAfter=4 * mm),
        "Section": ParagraphStyle("MLSection", parent=base["Heading1"], fontName=BOLD_FONT, fontSize=19, leading=24, textColor=colors.HexColor("#173a67"), spaceBefore=3 * mm, spaceAfter=6 * mm, keepWithNext=True),
        "PageTitle": ParagraphStyle("MLPageTitle", parent=base["Heading2"], fontName=BOLD_FONT, fontSize=16, leading=21, textColor=colors.HexColor("#102b4e"), spaceBefore=3 * mm, spaceAfter=4 * mm, keepWithNext=True),
        "H2": ParagraphStyle("MLH2", parent=base["Heading2"], fontName=BOLD_FONT, fontSize=13, leading=17, textColor=colors.HexColor("#174f86"), spaceBefore=4 * mm, spaceAfter=2 * mm, keepWithNext=True),
        "H3": ParagraphStyle("MLH3", parent=base["Heading3"], fontName=BOLD_FONT, fontSize=11, leading=15, textColor=colors.HexColor("#233f5d"), spaceBefore=3 * mm, spaceAfter=1.5 * mm, keepWithNext=True),
        "Body": ParagraphStyle("MLBody", parent=base["BodyText"], fontName=BODY_FONT, fontSize=9, leading=13, textColor=colors.HexColor("#263449"), spaceAfter=2.2 * mm, alignment=TA_LEFT, splitLongWords=True),
        "Small": ParagraphStyle("MLSmall", parent=base["BodyText"], fontName=BODY_FONT, fontSize=8, leading=11, textColor=colors.HexColor("#65748b"), spaceAfter=1.5 * mm),
        "Code": ParagraphStyle("MLCode", parent=base["Code"], fontName=CODE_FONT, fontSize=7.4, leading=10, textColor=colors.HexColor("#263449"), backColor=colors.HexColor("#f2f5f8"), borderColor=colors.HexColor("#dce3ea"), borderWidth=0.4, borderPadding=5, leftIndent=5, rightIndent=5, spaceBefore=1.5 * mm, spaceAfter=3 * mm),
        "Quote": ParagraphStyle("MLQuote", parent=base["BodyText"], fontName=ITALIC_FONT, fontSize=9, leading=13, textColor=colors.HexColor("#4a6078"), leftIndent=8 * mm, borderColor=colors.HexColor("#b9c8d8"), borderWidth=0, borderPadding=4, spaceAfter=2 * mm),
        "TOC0": ParagraphStyle("MLTOC0", parent=base["Normal"], fontName=BOLD_FONT, fontSize=10, leading=14, textColor=colors.HexColor("#173a67"), leftIndent=0, firstLineIndent=0, spaceBefore=2 * mm),
        "TOC1": ParagraphStyle("MLTOC1", parent=base["Normal"], fontName=BODY_FONT, fontSize=8.5, leading=11, textColor=colors.HexColor("#35475e"), leftIndent=6 * mm, firstLineIndent=0),
    }


class TocParagraph(Paragraph):
    def __init__(self, text: str, style: ParagraphStyle, bookmark: str, level: int, title: str):
        super().__init__(text, style)
        self.bookmark = bookmark
        self.toc_level = level
        self.toc_title = title


class ManualDocTemplate(SimpleDocTemplate):
    def afterFlowable(self, flowable):  # type: ignore[no-untyped-def]
        if isinstance(flowable, TocParagraph):
            self.canv.bookmarkPage(flowable.bookmark)
            self.canv.addOutlineEntry(flowable.toc_title, flowable.bookmark, level=flowable.toc_level, closed=False)
            self.notify("TOCEntry", (flowable.toc_level, flowable.toc_title, self.page, flowable.bookmark))


def draw_page(canvas, doc) -> None:  # type: ignore[no-untyped-def]
    canvas.saveState()
    if doc.page > 1:
        canvas.setStrokeColor(colors.HexColor("#dce3ea"))
        canvas.setLineWidth(0.5)
        canvas.line(18 * mm, PAGE_SIZE[1] - 14 * mm, PAGE_SIZE[0] - 18 * mm, PAGE_SIZE[1] - 14 * mm)
        canvas.setFont(BODY_FONT, 7.5)
        canvas.setFillColor(colors.HexColor("#66758a"))
        canvas.drawString(18 * mm, PAGE_SIZE[1] - 11 * mm, "Mercado Libre · documentación técnica es_co")
    canvas.setStrokeColor(colors.HexColor("#dce3ea"))
    canvas.setLineWidth(0.5)
    canvas.line(18 * mm, 13 * mm, PAGE_SIZE[0] - 18 * mm, 13 * mm)
    canvas.setFont(BODY_FONT, 7.5)
    canvas.setFillColor(colors.HexColor("#66758a"))
    canvas.drawString(18 * mm, 8.5 * mm, f"Fuente oficial enlazada en cada ficha · consulta {doc.capture_date_short}")
    canvas.drawRightString(PAGE_SIZE[0] - 18 * mm, 8.5 * mm, f"Página {doc.page}")
    canvas.restoreState()


def markdown_flowables(content: str, style_map: dict[str, ParagraphStyle]) -> list:
    story = []
    lines = strip_frontmatter(content).splitlines()
    code_lines: list[str] | None = None
    bullet_lines: list[str] = []

    def flush_bullets() -> None:
        if bullet_lines:
            items = [ListItem(Paragraph(inline_markup(re.sub(r"^(?:[-*]|\d+\.)\s+", "", line)), style_map["Body"]), leftIndent=4) for line in bullet_lines]
            story.append(ListFlowable(items, bulletType="bullet", start="circle", leftIndent=13, bulletFontName=BODY_FONT, bulletFontSize=7, bulletColor=colors.HexColor("#3476a7"), spaceAfter=2 * mm))
            bullet_lines.clear()

    for raw_line in lines:
        line = raw_line.rstrip()
        if line.strip().startswith("```"):
            flush_bullets()
            if code_lines is None:
                code_lines = []
            else:
                text = "\n".join(code_lines)
                story.append(Preformatted(safe_pdf_text(text), style_map["Code"], maxLineLength=94))
                code_lines = None
            continue
        if code_lines is not None:
            code_lines.append(line)
            continue
        if re.match(r"^\s*[-*]\s+|^\s*\d+\.\s+", line):
            bullet_lines.append(line)
            continue
        flush_bullets()
        if not line.strip():
            story.append(Spacer(1, 0.7 * mm))
            continue
        if line.strip() == "---":
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#dce3ea"), spaceBefore=1 * mm, spaceAfter=2 * mm))
            continue
        header = re.match(r"^(#{1,4})\s+(.*)$", line)
        if header:
            level, title = len(header.group(1)), header.group(2)
            key = {1: "PageTitle", 2: "H2", 3: "H3", 4: "H3"}[level]
            story.append(Paragraph(inline_markup(title), style_map[key]))
            continue
        if line.startswith("> "):
            story.append(Paragraph(inline_markup(line[2:]), style_map["Quote"]))
        else:
            story.append(Paragraph(inline_markup(line), style_map["Body"]))
    flush_bullets()
    if code_lines is not None:
        story.append(Preformatted(safe_pdf_text("\n".join(code_lines)), style_map["Code"], maxLineLength=94))
    return story


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    capture_date_long, capture_date_short = capture_date_labels(manifest)
    grouped: dict[str, list[dict]] = {}
    for page in manifest:
        grouped.setdefault(page.get("section") or "Portal", []).append(page)
    style_map = styles()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = ManualDocTemplate(
        str(OUTPUT),
        pagesize=PAGE_SIZE,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=19 * mm,
        title="Documentación de la API de Mercado Libre · es_co",
        author="Base documental API Mercado Libre",
        subject="Referencia técnica resumida con fuentes oficiales del portal público es_co",
    )
    doc.capture_date_short = capture_date_short

    toc = TableOfContents()
    toc.levelStyles = [style_map["TOC0"], style_map["TOC1"]]
    toc.dotsMinLevel = 0
    story = [
        Spacer(1, 35 * mm),
        Paragraph("API de Mercado Libre", style_map["Title"]),
        Paragraph("Documentación técnica del portal público de desarrolladores · es_co", style_map["Subtitle"]),
        Spacer(1, 8 * mm),
        Paragraph("Manual de consulta por área, recurso y operación", style_map["H2"]),
        Spacer(1, 4 * mm),
        Paragraph(f"{len(manifest)} páginas oficiales capturadas hasta el {capture_date_long}. Cada ficha conserva la fecha de actualización indicada por Mercado Libre, la fecha de captura, su huella de contenido y un enlace directo a la fuente.", style_map["Body"]),
        Spacer(1, 3 * mm),
        Paragraph("El contenido es una síntesis en español con redacción propia. Los parámetros, métodos, rutas, solicitudes, respuestas y errores se incluyen cuando la fuente los documenta; los datos ausentes se señalan expresamente.", style_map["Body"]),
        Spacer(1, 8 * mm),
        Paragraph(f"Alcance: portal de desarrolladores `es_co` · fecha de consulta: {capture_date_short}", style_map["Small"]),
        PageBreak(),
        Paragraph("Tabla de contenidos", style_map["Section"]),
        toc,
    ]

    section_names = sorted(grouped, key=str.casefold)
    for section_index, section in enumerate(section_names):
        story.append(PageBreak())
        section_key = "section_" + re.sub(r"[^a-z0-9]+", "_", unicodedata.normalize("NFKD", section).encode("ascii", "ignore").decode().lower()).strip("_")
        story.append(TocParagraph(html.escape(section), style_map["Section"], section_key, 0, section))
        pages = sorted(grouped[section], key=lambda row: row.get("title", "").casefold())
        for page_index, page in enumerate(pages):
            story.append(PageBreak())
            title = page.get("title") or page["id"]
            key = "page_" + page["id"].replace("-", "_")
            story.append(TocParagraph(html.escape(title), style_map["PageTitle"], key, 1, title))
            doc_path = MARKDOWN / f"{page['id']}.md"
            content = doc_path.read_text(encoding="utf-8")
            story.extend(markdown_flowables(content, style_map))

    doc.multiBuild(story)
    print(f"PDF generado: {OUTPUT.relative_to(ROOT)} ({OUTPUT.stat().st_size:,} bytes; {len(manifest)} fichas en {len(grouped)} áreas)")


if __name__ == "__main__":
    main()
