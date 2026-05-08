# Web Article Fallbacks

Use this reference when a user asks to ingest a web article but the supplied URL is not directly readable, especially X/Twitter articles, login-walled pages, or JavaScript shell HTML.

## X/Twitter article fallback pattern

Observed case: `https://x.com/GoogleCloudTech/article/2033953579824758855` returned a large unauthenticated HTML shell. The page contained generic X/Grok/bootstrap content but did not expose the article body or article ID in a useful way.

Useful probe sequence:

1. Fetch the URL and inspect for body markers rather than trusting HTTP 200:
   - page length alone is not enough;
   - check for the account, article ID, title, `og:title`, and structured state markers.
2. Try Jina Reader forms:
   - `https://r.jina.ai/http://r.jina.ai/http://<url>` is wrong; avoid double-reader nesting.
   - Try the normal reader wrapper for the original URL, then inspect whether the output is real article text or only a login-wall summary.
3. Search exact identifiers and likely title/account terms:
   - article/post ID;
   - account name;
   - quoted article title if snippets reveal one.
4. Prefer an accessible canonical or expanded version by the same author/organization. In the observed case, the readable expanded source was `https://lavinigam.com/posts/adk-skill-design-patterns/`.
5. Preserve provenance carefully:
   - keep the user-provided URL as the manifest/source identity when that is what the user asked to ingest;
   - state in the source guide that the original page was not directly readable unauthenticated;
   - list the accessible extraction URL used for content;
   - hash the extracted readable content for the manifest `content_hash`.
6. Keep manifest entries schema-clean. If the manifest schema has no field for extraction notes, put the note in the source guide page rather than adding ad-hoc manifest keys.

## Substack direct-HTML extraction pattern

Observed case: `https://nanothoughts.substack.com/p/company-brain-why-most-companies` exposed the article body inside the directly fetched Substack HTML even though generic reader extraction timed out or was unnecessary.

Useful probe sequence:

1. Fetch the original URL with a browser-like user agent and store the response locally:
   - `curl -L --max-time 30 -A 'Mozilla/5.0' -sS "$url" -o /tmp/wiki-ingest/<slug>/direct.html`
2. Inspect the HTML for embedded post fields before assuming a paywall or JavaScript shell:
   - search for the title, `body_html`, `subtitle`, `description`, and `og:title`;
   - Substack often serializes post data as JSON-escaped HTML inside a large script payload.
3. If `body_html` is present, extract only that field and decode it as JSON string content. Do not execute scripts from the page.
4. Convert the decoded HTML to text/markdown by stripping tags and preserving paragraph/list/heading boundaries. Keep the original user URL as the manifest key and source frontmatter entry.
5. In the source guide, note the extraction method explicitly, e.g. "the directly fetched Substack HTML contained the article body, extracted from embedded `body_html`."
   - For `open.substack.com/pub/.../p/...` share URLs, the fetch may redirect to the publication's canonical subdomain with `triedRedirect=true`. Preserve the user-provided `open.substack.com` URL as the manifest/source identity, but record the canonical redirected URL as the accessible extraction URL in the source guide.
6. Hash the extracted readable text for manifest `content_hash` when that text is what was ingested. Keep manifest schema clean; extraction notes belong in the source guide.

Minimal Python extraction sketch after saving `direct.html`:

```python
from pathlib import Path
import re, json, html
s = Path('direct.html').read_text(errors='ignore')
m = re.search(r'\\"body_html\\":\\"(.*?)\\",\\"truncated_body_text\\"', s)
if not m:
    m = re.search(r'"body_html":"(.*?)","truncated_body_text"', s)
body = json.loads('"' + m.group(1) + '"')
text = re.sub(r'<(h[1-6]|p|li|blockquote|figcaption|br)[^>]*>', '\n', body, flags=re.I)
text = re.sub(r'<[^>]+>', '', text)
text = html.unescape(text)
```

## Quality risk

A mirror or expanded repost may not be byte-identical to the original social article. Treat same-author canonical pages as high-confidence; treat third-party mirrors as access aids that need explicit attribution and, when possible, corroboration.
