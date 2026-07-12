# Local PDF overview extraction

Use this when a user provides a local PDF and the paper has a central overview / architecture figure, but the PDF does not expose it as an embedded image.

## Pattern

1. Extract text with an available PDF library or binary.
   - If Python already has PyMuPDF (`fitz`), use it directly.
   - Otherwise follow the main SKILL.md fallback: create a task-local venv and install `pypdf` rather than writing global packages.
2. Render likely figure pages to PNG for visual inspection.
   - With PyMuPDF, render early pages at 2x scale: `page.get_pixmap(matrix=fitz.Matrix(2,2), alpha=False)`.
   - Save pages into a temp task directory such as `/tmp/<paper-slug>/page-2.png`.
3. Inspect the rendered page and identify the overview figure bounding box.
   - Prefer the figure that carries the paper's core mental model, usually Figure 1.
   - Include the caption if it helps the note remain self-contained.
4. Crop the figure into `~/Documents/notes/images/{identifier}--paper-{short-title}-overview.png`.
   - Example with ImageMagick: `magick page-2.png -crop WIDTHxHEIGHT+X+Y +repage "$OUT"`.
5. Verify the crop visually.
   - Check that no important label or caption text is cut off.
   - If clipped, recrop and overwrite the same output path.

## Pitfalls

- A PDF may report `images 0` even when it contains diagrams; vector drawings need page rendering + crop, not embedded-image extraction.
- Do not save every chart. Save only the one overview figure that will help a future reader reconstruct the story.
- Do not preserve environment-specific missing-tool failures as rules. The durable workflow is: render page -> inspect -> crop -> verify.