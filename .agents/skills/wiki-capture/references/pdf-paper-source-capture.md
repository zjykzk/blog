# PDF Paper Source Capture Fallback

Use this when the user gives a direct PDF URL for a paper/report and asks to wiki-capture it.

## Pattern

1. Treat the PDF as a `source` capture unless the user explicitly asks for a distilled concept/synthesis.
2. Search the existing wiki first for source guides or syntheses about the same object. If a secondary article/page already exists, create a companion primary-source guide rather than overwriting it. State this source-layer distinction in `Capture Policy` and `Integration Decisions`.
3. Download the PDF to a temp path with `curl -L --fail <url> -o /tmp/wiki-capture/<name>.pdf`.
4. Try local PDF tooling first (`pdfinfo`, `pdftotext`). If missing, do not stop:
   - Create a temp venv: `python3 -m venv /tmp/wiki-capture/venv`
   - Install a PDF extractor inside it: `/tmp/wiki-capture/venv/bin/pip install pypdf -q`
   - Extract with pypdf:
     ```python
     from pypdf import PdfReader
     r = PdfReader('/tmp/wiki-capture/file.pdf')
     text = []
     for i, page in enumerate(r.pages):
         text.append(f'\n\n--- PAGE {i+1} ---\n' + (page.extract_text() or ''))
     open('/tmp/wiki-capture/file.txt', 'w').write('\n'.join(text))
     ```
   - This avoids modifying the system Python and handles PEP 668 / externally-managed Homebrew Python environments.
5. Preserve the paper's structure: bibliographic metadata, problem statement, definitions, model/framework, evidence/experiments, caveats/limitations, comparisons to prior theories, and future/open questions.
6. For long papers, use extracted text search and line slices rather than reading all text at once. Search section headings and key terms, then preserve a structured source guide in the user's/source language when requested.
7. Update `index.md`, `log.md`, `hot.md`, and the most relevant map page. If verification reveals a widely-used tag missing from taxonomy, treat it as taxonomy drift: add it to `_meta/taxonomy.md`, update its timestamp, and rerun verification.

## Pitfalls

- Missing `pdfinfo`/`pdftotext` is not a blocker.
- `python3 -m pip install --user ...` may fail under PEP 668 on macOS/Homebrew Python; use a temp venv instead.
- Do not collapse primary paper content into an existing secondary article guide. Keep primary and secondary layers separate and cross-linked.
