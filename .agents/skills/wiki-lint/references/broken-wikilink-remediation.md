# Broken wikilink remediation notes

Session pattern from `/Users/zenk/study/wiki`:

- `.env` may be absent even when the canonical wiki is obvious from repository context. In that case, scan `wiki/` if `wiki/index.md` and `wiki/log.md` exist.
- Broken links often come from migration residue:
  - old stable-page names, e.g. `[[学习方法论]]`
  - old source-layer paths, e.g. `[[pages/SDD]]`, `[[mobu/工具/认知天性]]`
- Remediation rule:
  - If the old link clearly maps to a current canonical wiki page, update it to the canonical path, e.g. `[[wiki/topics/Learning Methodology]]`.
  - If the old link is merely a raw/source-layer reference and no canonical wiki page exists, convert it to inline code, e.g. `` `mobu/工具/认知天性` ``. Do not leave it as a wikilink, and do not fabricate a page just to satisfy the lint.
- Verification should include:
  - broken wikilinks = 0
  - orphan pages unchanged or acceptable
  - self-links = 0, because replacement can accidentally map a legacy link to the page itself
- Log both audit and fix operations:
  - `LINT issues_found=... broken_links=...`
  - `LINT_FIX fixed=... category="broken_wikilinks" files_modified=... broken_links_remaining=0 orphans_remaining=0`
  - optional `LINT_FIX fixed=... category="self_wikilinks" ...`
