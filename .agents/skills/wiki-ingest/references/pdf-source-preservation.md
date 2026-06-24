# PDF Source Preservation and Source-Key Promotion

When a local PDF is ingested and the user wants the PDF "extracted to md", preserve a source-level Markdown file inside the wiki `sources/` directory and make that Markdown file the manifest source key.

## Pattern

1. Extract the PDF into `wiki/sources/<source-title>.md`.
2. Preserve page boundaries with `## Page N` headings.
3. If the user asks to "保持排版" / preserve layout, use a layout-preserving text extraction mode when available (for example `pypdf` `extract_text(extraction_mode="layout")`) and place each page inside fenced `text` blocks so Markdown rendering does not collapse whitespace.
4. Add frontmatter to the extracted Markdown source, for example:

```yaml
---
title: <source title>
source_pdf: /absolute/path/original.pdf
extracted_at: <ISO timestamp>
updated: <ISO timestamp>
source_type: pdf_text_extract
extraction_mode: pypdf_layout
layout_preserved: true
---
```

5. Update all distilled pages' `sources:` entries to point to the extracted Markdown file, not the original PDF path.
6. Update `.manifest.json` by moving the source entry key from the PDF path to the extracted Markdown path:
   - recompute `size_bytes` from the Markdown file
   - recompute `content_hash` from the Markdown file
   - update `modified_at`
   - include the extracted Markdown file itself in `pages_created`
7. Keep the original PDF path in the extracted Markdown frontmatter (`source_pdf`) for auditability.
8. Update `log.md` and any source guide notes so the recorded source key matches the extracted Markdown file.

## Pitfall

A plain PDF text extraction can flatten or reflow article layout. If the user asks to keep layout, do not just write normal paragraphs. Use layout extraction and fenced text blocks; otherwise Obsidian/Markdown may collapse spacing and lose the visual structure the user asked to preserve.
