# Actualizar la base documental

La captura se realiza con el navegador interno para respetar el acceso al portal de desarrolladores. El refresco separa la lectura de fuentes de la regeneración local para conservar la trazabilidad y detectar cambios antes de actualizar resúmenes.

## Flujo manual

1. Inicia el receptor local desde la raíz del repositorio: `python scripts/capture_server.py`.
2. Abre `http://127.0.0.1:8765/manifest` en el navegador interno para consultar la lista de URLs. Mantén abierto el formulario en `http://127.0.0.1:8765` en otra pestaña. Para cada URL `es_co`, abre la página oficial, copia el texto principal visible y envíalo en el formulario **Guardar captura** con un objeto como este:

   ```json
   {
     "source_url": "https://developers.mercadolibre.com.co/es_co/consulta-usuarios",
     "final_url": "https://developers.mercadolibre.com.co/es_co/consulta-usuarios",
     "title": "Consulta de usuarios",
     "source_updated_at": "2026-08-28",
     "captured_at": "2026-10-08T12:00:00-05:00",
     "text": "Texto principal copiado de la página oficial...",
     "blocks": [],
     "links": []
   }
   ```

   Conserva la URL de destino si hay redirección y deja `source_updated_at` como `null` cuando la página no publique fecha. Si descubres páginas o enlaces nuevos, usa el formulario **Guardar manifiesto** con `{ "documents": [...] }` y **Guardar auditoría de enlaces** con `{ "links": [...] }`; incluye solo URLs del dominio oficial y el idioma `es_co`. El receptor calcula SHA-256 y guarda el texto completo únicamente en `.cache/captures/`, excluido de Git.
3. Ejecuta `.venv/Scripts/python.exe scripts/refresh.py` (en macOS/Linux: `.venv/bin/python scripts/refresh.py`). El informe compara las huellas de las capturas nuevas con las documentadas, enumera páginas nuevas, modificadas y no disponibles, y no cambia los derivados cuando no hay cambios.
4. Revisa cada página modificada. Actualiza su ficha y sus registros `data/extracted/batch-*.jsonl` con redacción propia, sin rellenar campos ausentes. Si cambió el significado técnico, vuelve a extraer con Graphify el grupo que contiene esa ficha; guarda los fragmentos temporales en `graphify-out/semantic-chunks/` y ejecuta `scripts/normalize_graph_extractions.py` para actualizar las copias portables de `data/graph-extractions/`. Si se descubre una página nueva, crea su ficha, registros y fragmento semántico con su URL, fecha y huella de origen.
5. Ejecuta `.venv/Scripts/python.exe scripts/refresh.py --rebuild` (en macOS/Linux: `.venv/bin/python scripts/refresh.py --rebuild`) para validar el corpus y regenerar las fichas finales, el índice web, `data/pages.jsonl`, el grafo Graphify, el reporte, los documentos temáticos y el PDF. Si trabajas desde un clon limpio, Graphify construye el grafo usando las extracciones portables versionadas de `data/graph-extractions/`.

El paso de revisión semántica es necesario cuando la fuente cambió: los resúmenes y las relaciones del grafo requieren comparar el nuevo texto con los hechos de la ficha. El modo normal nunca sobrescribe esas decisiones; `--rebuild` las toma de los registros revisados.

## Archivos de estado

- `data/manifest.json`: URLs, metadatos de fuente, huellas y estado de captura.
- `data/refresh-report.json`: diferencias del último análisis.
- `.cache/captures/`: capturas completas locales; no se publican.
- `docs/markdown/`: fichas atribuidas, una por página.
- `data/extracted/`: extracción estructurada por lotes, antes de combinarse.
- `data/graph-extractions/`: fragmentos semánticos Graphify portables, con rutas relativas y procedencia por página.
- `data/operations.jsonl`: operaciones y conceptos normalizados.

Si una captura falla, el informe conserva el motivo y la página no se considera actualizada. Corrige el acceso desde el navegador interno y vuelve a capturarla antes de regenerar.
