# arXiv Ingest Playbook

Use this when ingesting `https://arxiv.org/abs/<id>` sources into the wiki.

## Retrieval sequence

1. Keep the user-provided abs URL as the canonical source key and frontmatter source:
   - `https://arxiv.org/abs/<id>`
2. Fetch three representations when possible:
   - abs page: title, authors, abstract, arXiv version metadata
   - HTML page: `https://arxiv.org/html/<id>` for readable text and section structure
   - PDF: `https://arxiv.org/pdf/<id>` for canonical file bytes and stable hashing
3. Prefer HTML for reading/extraction if available. Fall back to PDF extraction when HTML is missing, incomplete, or malformed.
4. Use the PDF bytes for manifest `size_bytes`, `modified_at`, and `content_hash` unless the PDF is inaccessible and HTML is the only real source.
5. In the source guide, explicitly state:
   - which representation was read
   - which representation was hashed
   - whether any artifact/project page/repository was noted but not independently inspected

## Distillation pattern

- Create a source guide for paper-specific details: exact table numbers, benchmark rankings, limitations, appendix implementation notes, artifact URLs.
- Create or update concept/topic/synthesis pages only for durable conceptual contributions.
- When benchmark search and final evaluation use the same public benchmark, mark broad claims with `^[ambiguous]` or keep them source-level.
- If the paper introduces an engineering pattern, connect it to existing operational concepts (e.g. harness, trace logs, verification, context management) rather than creating isolated paper-only pages.

## Frontmatter pitfall

Some existing pages use `sources: []`. When adding a source, replace it with:

```yaml
sources:
  - https://arxiv.org/abs/<id>
```

Do not prepend another `sources:` key. Duplicate YAML keys may look harmless in markdown but break retrieval and validation semantics.

## Verification snippets

Check for duplicate frontmatter source keys in changed pages:

```bash
python3 - <<'PY'
from pathlib import Path
for p in Path('wiki').rglob('*.md'):
    s=p.read_text(errors='ignore')
    if not s.startswith('---\n'):
        continue
    fm=s.split('---\n',2)[1]
    if fm.count('sources:') > 1:
        print('duplicate sources:', p)
PY
```

Check that the arXiv URL appears in manifest and log:

```bash
grep -R "https://arxiv.org/abs/<id>" wiki/.manifest.json wiki/log.md wiki/index.md
```
