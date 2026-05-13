# X Article Capture Fallback

Use this reference when a wiki capture target is an X/Twitter article or long post and `xurl` is unavailable, unauthenticated, rate-limited, or returns only partial metadata.

## Workflow

1. Try the normal social/X read path first if available and authenticated.
2. If `xurl` is missing or unusable, open the URL in a browser without logging in.
3. Extract the article body from the rendered page rather than from memory:
   - Use the article element text if the page renders: `Array.from(document.querySelectorAll('article')).map((a,i)=>({i,len:a.innerText.length,text:a.innerText}))`.
   - X may show the status as only a short `x.com/i/article/...` card in the accessibility snapshot while the full article text is still present in `article.innerText`; trust DOM extraction over the visible snapshot when they differ.
   - If the article link is hidden or truncated, discover it from anchors: `Array.from(document.querySelectorAll('a')).map(a=>({text:a.innerText,href:a.href})).filter(x=>x.href.includes('article')||x.href.includes('status/<id>'))`.
   - Keep the author, handle, visible title, publication timestamp, and engagement metadata only if visible in the DOM/browser-rendered page.
4. Extract media URLs separately and inspect article images/diagrams with vision/OCR when they carry substantive content:
   - Use `browser_get_images` to collect `pbs.twimg.com/media/...` URLs.
   - Ignore profile images and generic cover images unless they contain argument content.
   - Run OCR/vision on every substantive diagram/table image and preserve the diagram title, subtitle, cards/rows, arrows, footer notes, and any product-specific claims.
5. Preserve image-derived structure in the source guide as diagrams/tables, marking uncertain OCR or cropped text as inferred/ambiguous when needed.
6. If the same source guide already exists, prefer expanding or correcting that page instead of creating a duplicate. Update `updated`, `summary`, provenance, `log.md`, `hot.md`, and the relevant map.

## What to preserve

For X Articles, preserve more than the tweet-like opening text:

- title and source identity;
- opening thesis;
- section headings and argument flow;
- named examples and product/system names;
- diagrams and comparison tables from images;
- timing/update-mode distinctions;
- source-level claims that should not yet be promoted without corroboration;
- integration decisions linking source-level claims to stable concepts/topics.

## Pitfalls

- X may show an unauthenticated shell while still rendering the article body; do not stop just because login prompts are visible.
- `browser_snapshot` can truncate long pages; use DOM extraction from `article.innerText` to get the full rendered body.
- Image `alt="Image"` is not enough. Run vision/OCR on `pbs.twimg.com/media/...` images when diagrams are part of the argument.
- Do not create a second source guide for a URL already captured unless the new page is a deliberate companion layer; otherwise expand the existing guide.
