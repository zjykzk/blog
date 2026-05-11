# Wiki Capture Verification Pattern

Use this after creating or updating wiki capture pages.

## What to verify

- Created notes have required frontmatter: `title`, `category`, `tags`, `sources`, `created`, `updated`, `summary`, `provenance`, `base_confidence`, `lifecycle`, `lifecycle_changed`.
- New tags are present in `_meta/taxonomy.md`. If an already-used tag is missing from taxonomy, add it to taxonomy and update taxonomy's timestamp.
- Every wikilink in the new note resolves against the vault. For path-qualified links like `[[wiki/concepts/Foo]]`, strip the leading `wiki/` before checking relative to the vault root.
- `index.md`, `log.md`, and `hot.md` contain the new page reference; `log.md` contains the capture timestamp.
- Any updated map page contains the new page reference.

## Minimal Python verifier

```python
from pathlib import Path
import re, yaml
vault = Path('/path/to/vault/wiki')
notes = [vault/'sources/Example Source Guide.md', vault/'concepts/Example Concept.md']
required = ['title','category','tags','sources','created','updated','summary','provenance','base_confidence','lifecycle','lifecycle_changed']
tax = (vault/'_meta/taxonomy.md').read_text() if (vault/'_meta/taxonomy.md').exists() else ''
allowed = set(re.findall(r'`([^`]+)`', tax)) | {'article','paper','blog','arxiv','survey','book'}
errors = []
for p in notes:
    text = p.read_text()
    fm_text = re.match(r'^---\n(.*?)\n---\n', text, re.S).group(1)
    fm = yaml.safe_load(fm_text)
    missing = [k for k in required if k not in fm]
    if missing:
        errors.append(f'{p.name}: missing frontmatter {missing}')
    bad = [t for t in (fm.get('tags') or []) if t not in allowed]
    if bad:
        errors.append(f'{p.name}: tags not in taxonomy {bad}')
    for link in re.findall(r'\[\[([^\]|#]+)', text):
        rel = link[5:] if link.startswith('wiki/') else link
        if not (vault/(rel + '.md')).exists():
            errors.append(f'{p.name}: broken wikilink [[{link}]]')
print('VERIFICATION_OK' if not errors else '\n'.join(errors))
```

Adapt the `notes` list and add tracking-file checks for the capture timestamp and map coverage before reporting success.
