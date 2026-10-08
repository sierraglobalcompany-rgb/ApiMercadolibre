const state = { documents: [], query: "", section: "", method: "", sort: "relevance" };
const $ = (selector) => document.querySelector(selector);

function normalize(value) {
  return String(value || "").normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase().replace(/[^a-z0-9/_{}-]+/g, " ").trim();
}

function searchableText(doc) {
  return normalize([doc.title, doc.name, doc.resource, doc.section, doc.subsection, doc.method, doc.path, doc.content].filter(Boolean).join(" "));
}

function normalizedWithOffsets(value) {
  const original = String(value || "");
  let text = "";
  const offsets = [];
  for (let index = 0; index < original.length;) {
    const point = original.codePointAt(index);
    const character = String.fromCodePoint(point);
    const normalized = character.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
    for (const part of normalized) {
      text += /[a-z0-9/_{}-]/.test(part) ? part : " ";
      offsets.push(index);
    }
    index += character.length;
  }
  return { text, offsets };
}

function score(doc, terms) {
  const title = normalize(doc.title);
  const route = normalize(doc.path);
  const body = searchableText(doc);
  let total = 0;
  for (const term of terms) {
    if (title.includes(term)) total += 9;
    if (route.includes(term)) total += 12;
    if (normalize(doc.method).includes(term)) total += 8;
    const count = body.split(term).length - 1;
    total += Math.min(count, 5);
  }
  if (terms.length > 1 && terms.every((term) => body.includes(term))) total += 5;
  return total;
}

function snippet(doc, terms) {
  const text = String(doc.content || doc.title || "").replace(/\s+/g, " ").trim();
  if (!text) return "Sin descripción adicional en la ficha.";
  if (!terms.length) return text.slice(0, 230) + (text.length > 230 ? "…" : "");
  const mapped = normalizedWithOffsets(text);
  const positions = terms.map((term) => mapped.text.indexOf(term)).filter((n) => n >= 0);
  const match = positions.length ? Math.min(...positions) : 0;
  const start = Math.max(0, (mapped.offsets[match] ?? 0) - 75);
  const excerpt = text.slice(start, start + 250).trim();
  return (start > 0 ? "…" : "") + excerpt + (start + 250 < text.length ? "…" : "");
}

function addMeta(parent, value, href) {
  const node = href ? document.createElement("a") : document.createElement("span");
  if (href) {
    node.href = href;
    node.target = "_blank";
    node.rel = "noopener noreferrer";
  }
  node.textContent = value;
  parent.append(node);
}

function renderCard(doc, terms) {
  const card = document.createElement("article");
  card.className = "result-card";
  const top = document.createElement("div");
  top.className = "result-top";
  const type = document.createElement("span");
  type.className = "type-badge";
  type.textContent = doc.type === "operation" ? "Operación" : (doc.type === "concept" ? "Concepto" : (doc.section || "Guía"));
  top.append(type);
  if (doc.method) {
    const method = document.createElement("span");
    method.className = "method-badge";
    method.textContent = doc.method;
    top.append(method);
  }
  if (doc.path) {
    const route = document.createElement("code");
    route.className = "route";
    route.textContent = doc.path;
    top.append(route);
  }
  card.append(top);
  const heading = document.createElement("h3");
  const title = document.createElement("a");
  title.textContent = doc.title || "Documento sin título";
  const pageId = doc.type === "page" ? doc.id : (doc.page_id || doc.id);
  title.href = `../docs/markdown/${encodeURIComponent(pageId)}.md`;
  heading.append(title);
  card.append(heading);
  const description = document.createElement("p");
  description.textContent = snippet(doc, terms);
  card.append(description);
  const meta = document.createElement("div");
  meta.className = "result-meta";
  addMeta(meta, doc.section || "Portal");
  if (doc.source_updated_at) addMeta(meta, `Fuente actualizada: ${doc.source_updated_at}`);
  if (doc.captured_at) addMeta(meta, `Capturada: ${new Date(doc.captured_at).toLocaleDateString("es-CO")}`);
  if (doc.source_url) addMeta(meta, "Abrir fuente oficial ↗", doc.source_url);
  card.append(meta);
  return card;
}

function refresh() {
  const terms = normalize(state.query).split(/\s+/).filter(Boolean);
  let results = state.documents.filter((doc) => {
    if (state.section && doc.section !== state.section) return false;
    if (state.method && !(doc.methods || []).includes(state.method)) return false;
    if (!terms.length) return true;
    const text = searchableText(doc);
    return terms.every((term) => text.includes(term));
  }).map((doc) => ({ doc, score: score(doc, terms) }));
  if (state.sort === "title") results.sort((a, b) => String(a.doc.title).localeCompare(String(b.doc.title), "es"));
  else if (state.sort === "updated") results.sort((a, b) => String(b.doc.source_updated_at || "").localeCompare(String(a.doc.source_updated_at || "")));
  else results.sort((a, b) => b.score - a.score || String(a.doc.title).localeCompare(String(b.doc.title), "es"));

  const list = $("#results");
  list.replaceChildren(...results.slice(0, 100).map(({ doc }) => renderCard(doc, terms)));
  $("#result-count").textContent = `${results.length.toLocaleString("es-CO")} resultados`;
  $("#result-context").textContent = state.query ? `para “${state.query}”` : "en el corpus";
  $("#empty-state").hidden = results.length > 0;
}

function populateFilters() {
  const sections = [...new Set(state.documents.map((doc) => doc.section).filter(Boolean))].sort((a, b) => a.localeCompare(b, "es"));
  for (const section of sections) {
    const option = document.createElement("option");
    option.value = section;
    option.textContent = section;
    $("#section-filter").append(option);
  }
  const methods = [...new Set(state.documents.flatMap((doc) => doc.methods || []).filter(Boolean))].sort();
  for (const method of methods) {
    const option = document.createElement("option");
    option.value = method;
    option.textContent = method;
    $("#method-filter").append(option);
  }
}

async function main() {
  try {
    const response = await fetch("./search-index.json", { cache: "no-store" });
    if (!response.ok) throw new Error(`No se pudo cargar el índice (${response.status}).`);
    const index = await response.json();
    state.documents = index.documents || [];
    populateFilters();
    $("#result-count").textContent = `${state.documents.length.toLocaleString("es-CO")} registros indexados`;
    refresh();
  } catch (error) {
    $("#load-error").textContent = `${error.message} Ejecuta el servidor local desde la carpeta del proyecto.`;
    $("#load-error").hidden = false;
    $("#result-count").textContent = "Índice no disponible";
  }
}

$("#query").addEventListener("input", (event) => { state.query = event.target.value; refresh(); });
$("#section-filter").addEventListener("change", (event) => { state.section = event.target.value; refresh(); });
$("#method-filter").addEventListener("change", (event) => { state.method = event.target.value; refresh(); });
$("#sort").addEventListener("change", (event) => { state.sort = event.target.value; refresh(); });
$("#clear-filters").addEventListener("click", () => { state.section = ""; state.method = ""; $("#section-filter").value = ""; $("#method-filter").value = ""; refresh(); });
document.querySelectorAll("[data-query]").forEach((button) => button.addEventListener("click", () => { $("#query").value = button.dataset.query; state.query = button.dataset.query; refresh(); $("#query").focus(); }));
main();
