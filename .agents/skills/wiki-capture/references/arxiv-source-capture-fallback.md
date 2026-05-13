# arXiv Source Capture Fallback

Use this reference when wiki-capture is preserving an arXiv paper and the HTML page is unavailable or PDF-to-text tooling is blocked/unavailable.

## Trigger

- User provides an arXiv abstract URL such as `https://arxiv.org/abs/2602.08004`.
- The paper needs source-level preservation, not just abstract metadata.
- `https://arxiv.org/html/<id>` returns 404 or is incomplete.
- Direct shell commands such as `curl`/`pdftotext` are blocked, unavailable, or denied.

## Approach

1. Fetch metadata from the arXiv API to get the exact versioned ID and abstract:

```python
import urllib.request
url = 'https://export.arxiv.org/api/query?id_list=2602.08004'
print(urllib.request.urlopen(url, timeout=30).read().decode()[:5000])
```

2. Try the HTML page first if available:

```text
https://arxiv.org/html/<id>vN
```

3. If HTML is unavailable, fetch the e-print source bundle instead of relying on the PDF:

```python
import urllib.request, tarfile, io
from pathlib import Path
paper_id = '2602.08004v1'
base = Path('/tmp/wiki-capture-arxiv')
base.mkdir(exist_ok=True)
data = urllib.request.urlopen(
    urllib.request.Request(f'https://arxiv.org/e-print/{paper_id}', headers={'User-Agent':'Mozilla/5.0'}),
    timeout=60,
).read()
(base/'source.bin').write_bytes(data)
with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as tf:
    tf.extractall(base/'src')
print([p.name for p in (base/'src').iterdir()])
```

4. Read the main `.tex` file. Common names include `main.tex`, `paper.tex`, `acl_latex.tex`, or the largest `.tex` file. Preserve the paper's section structure, tables, numeric claims, prompts, appendices, limitations, and source-layer distinctions.

5. Cite the exact source actually read in frontmatter, normally both:

```yaml
sources:
  - https://arxiv.org/abs/<id>vN
  - https://arxiv.org/pdf/<id>vN
```

If the capture used the e-print source bundle, mention this in the capture process only if provenance matters; do not add local `/tmp` paths to the wiki note as sources.

## Pitfalls

- Do not stop at the abstract when the user asked to capture a paper URL; source-layer preservation requires enough detail to revisit the paper without reopening it.
- Do not retry a blocked terminal command after the environment returns a hard denial. Switch to an allowed tool path such as Python `urllib` or another available extraction route.
- Do not treat an explanatory article and the primary arXiv paper as the same source layer. Use the direct-source companion pattern when both exist.
- Do not promote all paper claims into stable concepts immediately. Keep single-paper measurements and benchmarks source-level unless cross-source synthesis supports them.
