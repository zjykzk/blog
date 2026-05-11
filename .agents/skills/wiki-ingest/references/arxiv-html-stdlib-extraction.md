# arXiv HTML extraction without extra dependencies

Use this when ingesting an arXiv paper and the environment lacks `bs4`, `pandoc`, `lynx`, `w3m`, or `pdftotext`.

## Pattern

1. Fetch three representations into a temp directory:
   - `https://arxiv.org/abs/<id>` for title, authors, abstract, DOI, submission metadata.
   - `https://arxiv.org/html/<id>` for readable body text when available.
   - `https://arxiv.org/pdf/<id>` for canonical bytes to hash in the manifest.
2. Hash the PDF bytes for `.manifest.json` even if the readable extraction uses HTML.
3. If Python HTML libraries are unavailable, use a small `html.parser.HTMLParser` subclass to strip `script`, `style`, `nav`, `header`, and `footer`, insert newlines around block tags, and collapse whitespace.
4. Extract enough section text to identify: abstract, method/modules, benchmark setup, headline results, limitations/open questions, and what should stay source-level.
5. In the source guide, explicitly record: “The arXiv HTML and PDF were both accessible. The wiki extraction used arXiv HTML for readable text and the PDF bytes for the manifest content hash.”

## Minimal extractor sketch

```python
from html.parser import HTMLParser
import re

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.skip=0
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style','nav','header','footer'):
            self.skip += 1
        if tag in ('p','div','section','article','h1','h2','h3','h4','li','tr','blockquote','br') and not self.skip:
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style','nav','header','footer') and self.skip:
            self.skip -= 1
        if tag in ('p','div','section','article','h1','h2','h3','h4','li','tr','blockquote') and not self.skip:
            self.parts.append('\n')
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

def extract(html):
    p = TextExtractor(); p.feed(html)
    text = ''.join(p.parts)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n[ \t]+', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()
```

## Pitfalls

- Do not hash the cleaned text if the PDF is available; manifest hash should represent canonical source bytes.
- Do not promote single-paper benchmark numbers into global concepts as stable facts; keep exact values in the source guide and promote only the durable conceptual contribution.
- If HTML text extraction creates noisy line breaks, use it for evidence gathering, then write clean wiki prose rather than preserving extraction artifacts.
