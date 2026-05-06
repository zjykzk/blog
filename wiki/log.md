---
title: LLM Wiki Log
type: source
status: growing
category: meta
summary: 建立 wiki/ 作为稳定知识层入口。 明确目标结构： raw/ 为原始材料层， wiki/ 为复利知识层。 首批试点选择 AI / Agent 知识簇。 保留 pages/ 、 journals/ 、 mobu/ 、 content/posts/ 作为迁移来源。
sources: []
created: 2026-04-20
base_confidence: 0.20
lifecycle: draft
lifecycle_changed: 2026-05-05
source_count: 0
updated: 2026-05-06T21:40:37+08:00
aliases:
  - Wiki Log
tags:
  - llm-wiki
  - log
---

# LLM Wiki Log

## 2026-04-20 | bootstrap

- 建立 `wiki/` 作为稳定知识层入口。
- 明确目标结构：`raw/` 为原始材料层，`wiki/` 为复利知识层。
- 首批试点选择 AI / Agent 知识簇。
- 保留 `pages/`、`journals/`、`mobu/`、`content/posts/` 作为迁移来源。

## 2026-05-03 | dashboard

- [2026-05-03T09:41:13Z] WIKI_DASHBOARD name="content-index" view=table filter="folder:wiki"
- [2026-05-03T09:41:13Z] WIKI_DASHBOARD_FIX name="content-index" reason="update Bases syntax to filters.and/views schema"

## 2026-05-04 | ingest

- [2026-05-04T04:24:22Z] INGEST source="https://arxiv.org/abs/2604.17091" pages_updated=6 pages_created=2 mode=append
- [2026-05-04T00:00:00+08:00] LINT issues_found=413 orphans=6 broken_links=38 stale=0 contradictions=0 prov_issues=8 missing_summary=90 fragmented_clusters=2 visibility_issues=0 promotion_candidates=0 synthesis_gaps=8 lifecycle_issues=192
- [2026-05-05T00:00:00+08:00] LINT issues_found=10 orphans=0 broken_links=0 stale=0 contradictions=0 prov_issues=0 missing_summary=0 fragmented_clusters=2 visibility_issues=0 promotion_candidates=0 synthesis_gaps=8 lifecycle_issues=0
- [2026-05-05T00:00:00+08:00] CROSS_LINK pages_scanned=104 links_added=33 pages_modified=14 orphans_remaining=0 misc_affinity_updated=0 promotion_candidates=0
- [2026-05-05T00:00:00+08:00] WIKI_SYNTHESIZE pages_scanned=104 synthesis_created=2 candidates_skipped=0
- [2026-05-05T00:00:00+08:00] LINT issues_found=0 orphans=0 broken_links=0 stale=0 contradictions=0 prov_issues=0 missing_summary=0 fragmented_clusters=0 visibility_issues=0 promotion_candidates=0 synthesis_gaps=0 lifecycle_issues=0
- [2026-05-05T00:00:00+08:00] INGEST source="https://x.com/_avichawla/article/2044670188998803855" pages_updated=6 pages_created=3 mode=append
- [2026-05-05T00:00:00+08:00] QUERY query="LLM的context放入的内容原则有哪些" result_pages=5 mode=normal escalated=false
- [2026-05-05T13:58:10+08:00] INGEST source="https://x.com/trq212/status/2024574133011673516" pages_updated=8 pages_created=0 mode=append
- [2026-05-05T14:03:13+08:00] INGEST source="https://x.com/akshay_pachaar/status/2041146899319971922" pages_updated=8 pages_created=2 mode=append
- [2026-05-05T14:18:28+08:00] INGEST source="https://x.com/ihtesham2005/status/2030214970353602806" pages_updated=8 pages_created=2 mode=append
- [2026-05-05T14:40:00+08:00] INGEST source="/Users/zenk/Downloads/How to Get Rich (without getting lucky).pdf" pages_updated=7 pages_created=6 mode=append
- [2026-05-05T15:10:00+08:00] INGEST source="https://addyosmani.com/blog/agent-harness-engineering/" pages_updated=10 pages_created=2 mode=append
- [2026-05-05T15:45:00+08:00] INGEST source="https://arxiv.org/abs/2307.03172" pages_updated=8 pages_created=2 mode=append
- [2026-05-05T16:25:00+08:00] INGEST source="https://baijia.online/homepage/survey/Survey%20on%20AI%20Memory.pdf" pages_updated=8 pages_created=3 mode=append
- [2026-05-05T17:05:00+08:00] INGEST source="https://martinfowler.com/articles/reduce-friction-ai/" pages_updated=10 pages_created=2 mode=append
- [2026-05-05T17:15:00+08:00] INGEST source="https://martinfowler.com/articles/reduce-friction-ai/knowledge-priming.html#ThisPatternInLattice" pages_updated=8 pages_created=1 mode=append
- [2026-05-05T17:25:00+08:00] INGEST source="https://martinfowler.com/articles/reduce-friction-ai/design-first-collaboration.html" pages_updated=11 pages_created=1 mode=append
- [2026-05-05T17:35:00+08:00] INGEST source="https://martinfowler.com/articles/reduce-friction-ai/context-anchoring.html" pages_updated=10 pages_created=1 mode=append
- [2026-05-05T17:45:00+08:00] INGEST source="https://martinfowler.com/articles/reduce-friction-ai/encoding-team-standards.html" pages_updated=11 pages_created=1 mode=append
- [2026-05-05T17:55:00+08:00] INGEST source="https://martinfowler.com/articles/reduce-friction-ai/feedback-flywheel.html" pages_updated=12 pages_created=1 mode=append
- [2026-05-06T10:51:47+08:00] INGEST source="https://x.com/trq212/status/2033949937936085378" pages_updated=6 pages_created=2 mode=append
- [2026-05-06T11:10:34+08:00] INGEST source="https://x.com/trq212/status/2027463795355095314" pages_updated=10 pages_created=2 mode=append
- [2026-05-06T12:17:59+08:00] INGEST source="https://www.aleksagordic.com/blog/vllm" pages_updated=6 pages_created=7 mode=append
- [2026-05-06T19:18:40+08:00] INGEST source="inline:understanding-cloud-2026-05-06" pages_updated=7 pages_created=2 mode=append
- [2026-05-06T19:34:46+08:00] INGEST source="inline:hofstadter-frame-discussion-2026-05-06" pages_updated=7 pages_created=1 mode=append
- [2026-05-06T19:50:40+08:00] INGEST source="/Users/zenk/Documents/notes/20260506T194300--概念解剖-分析__concept.org" pages_updated=7 pages_created=2 mode=append
- [2026-05-06T20:17:19+08:00] INGEST source="/Users/zenk/Documents/notes/20260506T201315--概念解剖-应用__concept.org" pages_updated=6 pages_created=2 mode=append
- [2026-05-06T20:58:15+08:00] INGEST source="/Users/zenk/Documents/notes/20260506T204024--概念解剖-评价__concept.org" pages_updated=4 pages_created=2 mode=append
- [2026-05-06T21:23:05+08:00] INGEST source="/Users/zenk/Documents/notes/20260506T211953--概念解剖-创造__concept.org" pages_updated=7 pages_created=2 mode=append
- [2026-05-06T21:35:29+08:00] CAPTURE type=concept page="wiki/concepts/Knowledge Types.md" title="Knowledge Types"
- [2026-05-06T21:40:37+08:00] CAPTURE type=concept page="wiki/concepts/Knowledge Types.md" title="Judgment Knowledge"
