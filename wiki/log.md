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
updated: 2026-05-15T22:36:42+08:00
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
- [2026-05-06T22:24:21+08:00] INGEST source="https://martinfowler.com/articles/harness-engineering.html" pages_updated=10 pages_created=5 mode=append
- [2026-05-06T22:45:47+08:00] INGEST source="https://addyosmani.com/blog/agent-harness-engineering/" pages_updated=6 pages_created=0 mode=append
- [2026-05-07T00:00:00+08:00] QUERY query="『应用』和『创造』有什么区别" result_pages=4 mode=normal escalated=false
- [2026-05-07T10:18:04+08:00] QUERY query="『不是照着做』和『让抽象结构贴合现实约束』区别是什么" result_pages=2 mode=normal escalated=false
- [2026-05-07T10:47:40+08:00] WIKI_RESEARCH topic="应用和创造的区别" rounds=2 sources_fetched=7 pages_created=8 pages_updated=7
- [2026-05-07T12:44:36+08:00] INGEST source="https://x.com/GoogleCloudTech/article/2033953579824758855" pages_updated=6 pages_created=2 mode=append
- [2026-05-07T12:55:22+08:00] QUERY query="这篇文章是否和人类的常规工作流程有关系" result_pages=2 mode=normal escalated=false
- [2026-05-07T13:57:16+08:00] CAPTURE type=synthesis page="wiki/syntheses/Agent Skill Patterns as Human Workflow Control Structures.md" title="Agent Skill Patterns as Human Workflow Control Structures"
- [2026-05-07T10:31:25Z] QUERY query="harness有哪几根秩，参考技能ljg-rank关于秩的定义" result_pages=8 mode=normal escalated=false
- [2026-05-07T10:33:29Z] CAPTURE type=synthesis page="wiki/syntheses/harness-root-ranks.md" title="Harness Root Ranks"
- [2026-05-07T22:03:56+08:00] INGEST source="https://www.chrismdp.com/coding-with-ai/" pages_updated=11 pages_created=2 mode=append
- [2026-05-08T15:58:41+08:00] INGEST source="https://nanothoughts.substack.com/p/company-brain-why-most-companies" pages_updated=8 pages_created=6 mode=append
- [2026-05-08T20:38:05+08:00] INGEST source="https://open.substack.com/pub/nanothoughts/p/company-brain-part-2-factual-memory?utm_campaign=post&utm_medium=web" pages_updated=6 pages_created=2 mode=append
- [2026-05-08T20:54:16+08:00] INGEST source="https://open.substack.com/pub/nanothoughts/p/company-brain-part-3-interaction?utm_campaign=post&utm_medium=web" pages_updated=8 pages_created=2 mode=append
- [2026-05-08T22:24:16+08:00] INGEST source="https://nanothoughts.substack.com/p/company-brain-part-4-action-memory" pages_updated=11 pages_created=1 mode=append
- [2026-05-08T22:31:50+08:00] CAPTURE type=concept page="wiki/concepts/engineering-thinking.md" title="Engineering Thinking"
- [2026-05-08T23:09:47+08:00] CAPTURE type=synthesis page="wiki/syntheses/Reality-Refutable Engineering Systems.md" title="Reality-Refutable Engineering Systems"
- [2026-05-09T00:00:00+08:00] INGEST source="inline:life-of-a-token-2026-05-09" pages_updated=8 pages_created=6 mode=append
- [2026-05-09T20:15:00+08:00] INGEST source="https://donellameadows.org/wp-content/userfiles/iceberg-model.pdf" pages_updated=10 pages_created=2 mode=append

- [2026-05-09T20:42:04+08:00] INGEST source="https://mp.weixin.qq.com/s/64e7occeVSutUJzZAWVutg" pages_updated=10 pages_created=1 mode=append
- [2026-05-09T21:05:00+08:00] INGEST source="https://x.com/odysseus0z/status/2030416758138634583?s=46&t=GqNFmk6Xi41yVO4sAJf36g" pages_updated=9 pages_created=1 mode=append
- [2026-05-09T21:19:58+08:00] CAPTURE type=source page="wiki/sources/How LLMs Actually Work Source Guide.md" title="How LLMs Actually Work Source Guide"
- [2026-05-09T21:26:53+08:00] CAPTURE type=source page="wiki/sources/How to Use LLMs Source Guide.md" title="How to Use LLMs Source Guide"

- [2026-05-09T21:39:04+08:00] CAPTURE type=synthesis page="wiki/syntheses/LLM Training Stages.md" title="LLM Training Stages"

- [2026-05-09T22:17:54+08:00] INGEST source="https://x.com/hwchase17/status/2040467997022884194" pages_updated=7 pages_created=2 mode=append
- [2026-05-09T22:42:07+08:00] INGEST source="https://arxiv.org/abs/2603.28052" pages_updated=6 pages_created=2 mode=append
- [2026-05-09T23:00:43+08:00] CAPTURE type=source page="wiki/sources/Cognitive Load Theory Source Guide.md" title="Cognitive Load Theory Source Guide"
- [2026-05-09T22:55:00+08:00] CAPTURE type=source page="wiki/sources/ICAP Learning Framework Source Guide.md" title="ICAP Learning Framework Source Guide"

- [2026-05-09T23:24:53+08:00] LINT issues_found=220 orphans=0 broken_links=29 stale=19 contradictions=0 prov_issues=83 missing_summary=0 fragmented_clusters=4 visibility_issues=1 promotion_candidates=0 synthesis_gaps=0 lifecycle_issues=84

- [2026-05-09T23:28:26+08:00] LINT_FIX fixed=29 category="broken_wikilinks" files_modified=16 broken_links_remaining=0 orphans_remaining=0
- [2026-05-09T23:30:20+08:00] LINT_FIX fixed=2 category="self_wikilinks" files_modified=2 self_links_remaining=0
- [2026-05-09T23:35:01+08:00] CROSS_LINK pages_scanned=206 links_added=2 pages_modified=2 orphans_remaining=0 misc_affinity_updated=0 promotion_candidates=0 target="systems tag cluster"
- [2026-05-09T23:35:56+08:00] CROSS_LINK pages_scanned=206 links_added=2 pages_modified=2 orphans_remaining=0 misc_affinity_updated=0 promotion_candidates=0 target="systems source guides"
- [2026-05-09T23:36:55+08:00] CROSS_LINK pages_scanned=206 links_added=1 pages_modified=1 orphans_remaining=0 misc_affinity_updated=0 promotion_candidates=0 target="systems tag cluster"
- [2026-05-09T23:37:31+08:00] LINT_REVIEW category="visibility" reviewed=1 false_positive=1 unresolved=0 note="Life of a Token title contains Token: but no credential-like value"
- [2026-05-10T14:21:35+08:00] CAPTURE type=concept page="wiki/concepts/System.md" title="System"
- [2026-05-10T14:23:25+08:00] CROSS_LINK pages_scanned=206 links_added=2 pages_modified=2 orphans_remaining=0 misc_affinity_updated=0 promotion_candidates=0 target="paper tag cluster"
- [2026-05-10T14:24:45+08:00] SYNTHESIS_REFRESH pages_updated=2 pages="React UI Organization Model; Business Analysis to Software Design" reason="clear stale synthesis and fold in source-page refinements"
- [2026-05-10T14:29:55+08:00] STALE_REFRESH pages_updated=6 pages="Component-Based Architecture; Declarative Programming; State Management; Frontend Development; Evaluation; Evaluation Concept Anatomy Source Guide" reason="source mtimes newer than updated metadata"
- [2026-05-10T14:31:32+08:00] LINT issues_found=112 orphans=0 broken_links=0 stale=4 contradictions=0 prov_issues=38 missing_summary=0 fragmented_clusters=2 visibility_issues=2 promotion_candidates=0 synthesis_gaps=0 lifecycle_issues=66
- [2026-05-10T14:32:02+08:00] STALE_REFRESH pages_updated=1 pages="React UI Organization Model" reason="source pages were updated during stale refresh"
- [2026-05-10T14:33:06+08:00] LINT issues_found=87 orphans=0 broken_links=0 stale=0 contradictions=0 prov_issues=19 missing_summary=0 fragmented_clusters=2 visibility_issues=0 promotion_candidates=0 synthesis_gaps=0 lifecycle_issues=66 note="supersedes prior same-session LINT with corrected provenance/PII/stale checks"
- [2026-05-10T15:49:39+08:00] LINT_FIX rule=12e base_confidence_drift_fixed=54 mode="--fix"
- [2026-05-10T15:57:18+08:00] LINT_FIX rule=7 provenance_drift_fixed=19 mode="normalize-frontmatter"
- [2026-05-10T15:57:59+08:00] LINT issues_found=2 orphans=0 broken_links=0 stale=0 contradictions=0 prov_issues=0 missing_summary=0 fragmented_clusters=2 visibility_issues=0 promotion_candidates=0 synthesis_gaps=0 lifecycle_issues=0 note="post provenance normalize verification"
- [2026-05-10T16:02:23+08:00] TAG_NORMALIZE tags_renamed=146 pages_modified=119 new_tags_added=0 retired_tags="ai,source" taxonomy_created=true
- [2026-05-10T16:08:07+08:00] TAG_NORMALIZE index_tags_synced=true hot_updated=true
- [2026-05-10T16:08:44+08:00] LINT issues_found=5 orphans=0 broken_links=0 stale=5 contradictions=0 prov_issues=0 missing_summary=0 fragmented_clusters=0 visibility_issues=0 promotion_candidates=0 synthesis_gaps=0 lifecycle_issues=0 note="post tag taxonomy normalization"
- [2026-05-10T16:09:04+08:00] STALE_REFRESH pages_updated=5 reason="source tag normalization changed React source guide mtime"
- [2026-05-10T16:09:44+08:00] LINT issues_found=4 orphans=0 broken_links=0 stale=4 contradictions=0 prov_issues=0 missing_summary=0 fragmented_clusters=0 visibility_issues=0 promotion_candidates=0 synthesis_gaps=0 lifecycle_issues=0 index_issues=0 note="final post tag/stale verification"
- [2026-05-10T16:10:19+08:00] STALE_REFRESH pages_updated=1 pages="React UI Organization Model" reason="dependent source pages updated moments earlier"
- [2026-05-10T16:11:01+08:00] LINT issues_found=0 orphans=0 broken_links=0 stale=0 contradictions=0 prov_issues=0 missing_summary=0 fragmented_clusters=0 visibility_issues=0 promotion_candidates=0 synthesis_gaps=0 lifecycle_issues=0 index_issues=0 note="clean final verification"
- [2026-05-10T16:21:01+08:00] CAPTURE type=source page="wiki/sources/Narrative as First Principle Source Guide.md" title="Narrative as First Principle Source Guide"
- [2026-05-10T16:21:01+08:00] CAPTURE type=concept page="wiki/concepts/Narrative.md" title="Narrative"
- [2026-05-10T16:27:44+08:00] CAPTURE type=source page="wiki/sources/Heavy-Tailed World Source Guide.md" title="Heavy-Tailed World Source Guide"
- [2026-05-10T16:27:44+08:00] CAPTURE type=concept page="wiki/concepts/Heavy-Tailed Distribution.md" title="Heavy-Tailed Distribution"
- [2026-05-10T16:27:44+08:00] CAPTURE type=concept page="wiki/concepts/Multiplicative World.md" title="Multiplicative World"
- [2026-05-10T16:32:29+08:00] CAPTURE type=source page="wiki/sources/能动与稳态生存逻辑 Source Guide.md" title="能动与稳态生存逻辑 Source Guide"
- [2026-05-10T16:32:29+08:00] CAPTURE type=concept page="wiki/concepts/Human Agency.md" title="Human Agency"
- [2026-05-10T21:43:57+08:00] CAPTURE type=source page="wiki/sources/Hard Constraints Source Guide.md" title="Hard Constraints Source Guide"
- [2026-05-10T21:43:57+08:00] CAPTURE type=concept page="wiki/concepts/Hard Constraint.md" title="Hard Constraint"
- [2026-05-10T22:20:21+08:00] CAPTURE type=source page="wiki/sources/可能：不确定性是意义的燃料 Source Guide.md" title="可能：不确定性是意义的燃料 Source Guide"
- [2026-05-10T22:20:21+08:00] CAPTURE type=concept page="wiki/concepts/Uncertainty as Meaning Fuel.md" title="Uncertainty as Meaning Fuel"
- [2026-05-10T22:51:54+08:00] CAPTURE type=source page="wiki/sources/内核 你的三个自我 Source Guide.md" title="内核：你的三个自我 Source Guide"
- [2026-05-10T22:51:54+08:00] CAPTURE type=concept page="wiki/concepts/三个自我模型.md" title="三个自我模型"
- [2026-05-10T23:07:11+08:00] QUERY query="什么是加法世界、乘法世界" result_pages=5 mode=normal escalated=false
- [2026-05-10T23:12:22+08:00] WIKI_UPDATE pages_updated=4 pages_created=1 note="补充加法世界 gap：新增 Additive World 概念页，并从 Multiplicative World 拆出别名与双向链接"
- [2026-05-11T10:27:21+08:00] CAPTURE type=source page="wiki/sources/Memory Is State Not a Service Source Guide.md" title="Memory Is State Not a Service Source Guide"
- [2026-05-11T12:08:45+08:00] INGEST source="https://arxiv.org/abs/2604.27488" pages_updated=9 pages_created=2 mode=append
- [2026-05-11T21:13:33+08:00] CAPTURE type=synthesis page="wiki/syntheses/深度思考 高阶思维与本质理解.md" title="深度思考、高阶思维与本质理解"
- [2026-05-11T21:19:31+08:00] CAPTURE type=source page="wiki/sources/思维圆桌 Source Guide.md" title="思维圆桌 Source Guide"
- [2026-05-11T21:26:10+08:00] CAPTURE type=source page="wiki/sources/深度思考与高阶思维对话 Source Guide.md" title="深度思考与高阶思维对话 Source Guide"
- [2026-05-11T21:29:38+08:00] UPDATE type=source pages="wiki/sources/思维圆桌 Source Guide.md,wiki/sources/深度思考与高阶思维对话 Source Guide.md" reason="expand source captures beyond summary per user preference"
- [2026-05-11T22:24:44+0800] QUERY query="ICAP学习框架，对学习任何知识都是一样的吗，还是只适用于某类知识" result_pages=5 mode=normal escalated=false
- [2026-05-11T22:30:16+0800] CAPTURE type=synthesis page="wiki/syntheses/ICAP 与知识类型的适用边界.md" title="ICAP 与知识类型的适用边界"
- [2026-05-11 23:47:09+0800] QUERY query="有哪些『机制模型』" result_pages=10 mode=normal escalated=true
- [2026-05-11 23:49:26+0800] QUERY query="goon / 继续机制模型" result_pages=10 mode=normal escalated=false
- [2026-05-11 23:59:06+0800] QUERY query="很好，请继续 / 机制模型继续深化" result_pages=5 mode=normal escalated=false
- [2026-05-12T00:14:41+08:00] CAPTURE type=concept page="wiki/concepts/Mechanism Model.md" title="Mechanism Model"
- [2026-05-12T00:14:41+08:00] CAPTURE type=map page="wiki/maps/Mechanism Models Map.md" title="Mechanism Models Map"
- [2026-05-12T10:35:38+08:00] CAPTURE type=source page="wiki/sources/SkillOS Source Guide.md" title="SkillOS Source Guide"
- [2026-05-12T10:45:54+08:00] CAPTURE type=source page="wiki/sources/SkillOS Paper Source Guide.md" title="SkillOS Paper Source Guide"
- [2026-05-12T11:05:11+08:00] CAPTURE type=source page="wiki/sources/Agent Skills Data-Driven Analysis Paper Source Guide.md" title="Agent Skills Data-Driven Analysis Paper Source Guide"
- [2026-05-12T11:36:33+08:00] UPDATE type=source page="wiki/sources/Continual Learning for AI Agents Source Guide.md" title="Continual Learning for AI Agents Source Guide" reason="expand Harrison Chase continual-learning source guide with full source-level article structure and diagrams"
- [2026-05-12T12:20:47+08:00] CAPTURE type=source page="wiki/sources/Agent Observability Needs Feedback Source Guide.md" title="Agent Observability Needs Feedback Source Guide"
- [2026-05-12T15:50:12+08:00] CAPTURE type=source page="wiki/sources/React Hooks useRef useContext useMemo Source Guide.md" title="React Hooks useRef useContext useMemo Source Guide"
- [2026-05-12T16:36:46+08:00] CAPTURE type=source page="wiki/sources/React Hooks useState useEffect Source Guide.md" title="React Hooks useState useEffect Source Guide"
- [2026-05-12T16:51:48+08:00] CAPTURE type=source page="wiki/sources/The ICAP Framework Paper Source Guide.md" title="The ICAP Framework Paper Source Guide"
- [2026-05-12T17:04:17+08:00] CAPTURE type=source page="wiki/sources/架构文档与图示之道 Source Guide.md" title="架构文档与图示之道 Source Guide"
- [2026-05-12T17:58:27+0800] QUERY query="useMemo和useRef生成的对象生命周期" result_pages=3 mode=normal escalated=false
- [2026-05-12T18:36:10+0800] QUERY query="解释下组件的生命周期，在一个生命周期内可以渲染多次吗" result_pages=2 mode=normal escalated=false
- [2026-05-12T20:53:26+0800] QUERY query="组件什么时候mount，什么时候unmount" result_pages=2 mode=normal escalated=false
- [2026-05-12T20:56:53+08:00] CAPTURE type=source page="wiki/sources/React Component Lifecycle Source Guide.md" title="React Component Lifecycle Source Guide"
- [2026-05-12T21:05:21+08:00] CAPTURE type=source page="wiki/sources/Compounding Engineering Source Guide.md" title="Compounding Engineering Source Guide"
- [2026-05-13T00:06:14+08:00] INGEST source="mobu/读书/架构师启示录-知识模型、落地方法与思维模式*" pages_updated=9 pages_created=6 mode=append

- [2026-05-13T09:59:22+08:00] INGEST source="https://arxiv.org/abs/2603.07670" pages_updated=8 pages_created=4 mode=append
- [2026-05-13T10:37:07+08:00] INGEST source="https://arxiv.org/abs/2601.12560v1" pages_updated=7 pages_created=5 mode=append
- [2026-05-13T10:38:00+08:00] CAPTURE type=source page="wiki/sources/What Happens Inside Agent Memory Paper Source Guide.md" title="What Happens Inside Agent Memory Paper Source Guide"
- [2026-05-13T11:10:03+08:00] QUERY query="如何构建知识体系" result_pages=7 mode=normal escalated=false
- [2026-05-13T16:38:27+08:00] QUERY query="结合知识管理专家经验补充如何构建知识体系" result_pages=7 mode=normal escalated=false
- [2026-05-13T16:50:00+08:00] CAPTURE type=source page="wiki/sources/从知识堆积到结构化记忆 Source Guide.md" title="从知识堆积到结构化记忆 Source Guide"
- [2026-05-13T11:18:00+08:00] CAPTURE type=synthesis page="wiki/syntheses/Knowledge System Construction.md" title="Knowledge System Construction"
- [2026-05-13T23:20:00+08:00] CAPTURE type=synthesis page="wiki/syntheses/Quality Engineering Three Generators.md" title="Quality Engineering Three Generators"
- [2026-05-14T00:28:21+08:00] CAPTURE type=synthesis page="wiki/syntheses/Requirements Expression Beyond Use Cases.md" title="Requirements Expression Beyond Use Cases"
- [2026-05-14T00:29:01+08:00] CAPTURE type=source page="wiki/sources/Use Case 开发管理 Source Guide.md" title="Use Case 开发管理 Source Guide"
- [2026-05-14T00:58:10+08:00] CAPTURE type=synthesis page="wiki/syntheses/Use Cases as AI Coding Traceability Anchors.md" title="Use Cases as AI Coding Traceability Anchors"
- [2026-05-14T10:53:14+08:00] CAPTURE type=source page="wiki/sources/表征 图式 心智模型和解释框架 Source Guide.md" title="表征、图式、心智模型和解释框架 Source Guide"
- [2026-05-14T11:07:48+08:00] UPDATE type=source page="wiki/sources/表征 图式 心智模型和解释框架 Source Guide.md" reason="add applicability boundary across theory, judgment, procedural, factual, perceptual, and experiential learning materials"
- [2026-05-14T12:00:10+08:00] UPDATE type=source page="wiki/sources/表征 图式 心智模型和解释框架 Source Guide.md" reason="add AI learning flow for balancing high compression with long-term retention, recall, spacing, application, and feedback"
- [2026-05-14T12:32:46+08:00] CAPTURE type=source page="wiki/sources/综合调研 在没有教科书的地方挖掘真知 Source Guide.md" title="综合调研：在没有教科书的地方挖掘真知 Source Guide"
- [2026-05-15T17:48:18+0800] QUERY query="设计模式和设计原则区别" result_pages=4 mode=normal escalated=false
- [2026-05-15T20:33:52+0800] QUERY query="设计模式和设计原则区别与 Iceberg Model 的联系" result_pages=4 mode=normal escalated=false
- [2026-05-15T20:43:09+0800] QUERY query="信息流和状态流转的区别是什么" result_pages=5 mode=normal escalated=false
- [2026-05-15T20:48:22+0800] CAPTURE type=source page="wiki/sources/设计模式 设计原则与系统思维 Source Guide.md" title="设计模式、设计原则与系统思维 Source Guide"
- [2026-05-15T20:53:47+0800] CAPTURE type=synthesis page="wiki/syntheses/软件设计作为系统诊断.md" title="软件设计作为系统诊断"
- [2026-05-15T20:56:12+08:00] UPDATE type=source page="wiki/sources/表征 图式 心智模型和解释框架 Source Guide.md" reason="append ljg-qa extraction chain generated from the learning compression source guide"
- [2026-05-15T21:04:58+08:00] CAPTURE type=synthesis page="wiki/syntheses/信息流与状态流转设计原则.md" title="信息流与状态流转设计原则"
- [2026-05-15T21:19:51+08:00] CAPTURE type=source page="wiki/sources/LLM Wiki Source Guide.md" title="LLM Wiki Source Guide"
- [2026-05-15T21:28:17+08:00] LINT issues_found=35 orphans=1 broken_links=0 stale=4 contradictions=0 prov_issues=24 missing_summary=0 fragmented_clusters=4 visibility_issues=1 promotion_candidates=0 synthesis_gaps=0 lifecycle_issues=0
- [2026-05-15T21:35:01+08:00] LINT_FIX broken_count=0 selflink_count=0 orphan_count=0 stale=0 visibility_issues=0 prov_issues=0 files_modified=27
- [2026-05-15T22:33:09+08:00] CAPTURE type=source page="wiki/sources/配置 钩子 代码库与技能放置决策 Source Guide.md" title="配置 钩子 代码库与技能放置决策 Source Guide"
- [2026-05-15T22:36:42+08:00] CAPTURE type=source page="wiki/sources/Chatham House Rule Source Guide.md" title="Chatham House Rule Source Guide"
- [2026-05-15T23:34:56+08:00] CAPTURE type=source page="wiki/sources/表达清晰圆桌 Source Guide.md" title="表达清晰圆桌 Source Guide"
