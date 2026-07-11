---
title: >-
  COLLEAGUE.SKILL Paper Source Guide
category: sources
type: source
status: draft
tags: [paper, arxiv, agents, skills, workflow]
sources:
  - https://arxiv.org/abs/2605.31264
  - conversation:2026-06-01
created: 2026-06-01T16:18:53+0800
updated: 2026-06-01T16:18:53+0800
summary: >-
  Direct paper guide for COLLEAGUE.SKILL, preserving its person-grounded trace-to-skill artifact model, dual tracks, lifecycle, deployment surface, and evaluation limits.
provenance:
  extracted: 0.99
  inferred: 0.01
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-06-01
aliases:
  - COLLEAGUE.SKILL
  - Automated AI Skill Generation via Expert Knowledge Distillation
---
# COLLEAGUE.SKILL Paper Source Guide

> Source: "COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation", arXiv:2605.31264, submitted 2026-05-29.

## Capture Policy

This page preserves the primary-paper layer for COLLEAGUE.SKILL. It should be used for paper-grounded claims about the artifact contract, generation workflow, correction lifecycle, deployment surface, and stated limitations; broader interpretations about skill infrastructure should be promoted later into [[wiki/concepts/Agent Skill]], [[wiki/topics/AI Skills Workflow]], or a synthesis page.

The conversation also produced a longer personal reading note at `/Users/zenk/Documents/notes/20260601T104435--paper-colleague-skill__paper.org`; this wiki page preserves the durable source guide rather than the full reading artifact.

## What It Covers

COLLEAGUE.SKILL frames person-grounded agent customization as an artifact problem rather than as unrestricted persona simulation. The paper's core claim is narrow: selected traces of a person or role can be distilled into a portable, inspectable, correctable skill package with explicit files, metadata, lifecycle state, and deployment boundaries.

The colleague setting is the main case. A departing teammate may leave behind review standards, incident heuristics, design preferences, and communication norms scattered across code comments, chat decisions, documents, and postmortems. The paper argues that this material should not remain a hidden retrieval store or a single persona prompt. It should become a bounded skill artifact that can be read, installed, corrected, rolled back, withheld, deleted, or shared under user control.

## Preserved Content

### Problem Frame

The paper starts from the practical need for agents that carry bounded representations of human expertise, judgment, and interaction style. Existing memory and persona systems capture fragments of evidence, while skill frameworks provide portable packaging formats. The missing workflow is end-to-end trace-to-skill distillation: heterogeneous traces become inspectable, correctable, agent-usable skills.

The useful target is not identity replacement. In the paper's framing, a generated skill does not claim to be a faithful model of a person. It claims to preserve selected evidence about how a person or role weighs evidence, detects risk, follows procedures, expresses constraints, and interacts within stated boundaries.

### Person-Grounded Skill Formulation

A person-grounded skill is grounded in evidence about a person or role while remaining bounded by source, usage, and governance constraints. The paper describes the generated package as three kinds of state: generated files, machine-readable metadata, and lifecycle state.

This formulation narrows the claim below behavioral cloning. The artifact can be inspected for structure, provenance, source boundaries, update behavior, and deployment compatibility even before task-level human studies exist.

### System Overview

The pipeline begins with traces of a target person or role. In the colleague preset, these traces may be work documents, code-review comments, chat decisions, incident notes, and lightweight profile fields. In public-figure settings, they may be first-person writings, long-form interviews, documented decisions, and public reception. In relationship settings, they may include sensitive private interaction records, which makes consent and local control first-order technical concerns.

The implemented architecture is:

```text
raw traces
  |
  v
collectors and parsers
  |
  v
local knowledge directories
  |
  v
analyzers extract capability, mental models, and bounded interaction style
  |
  v
builders render structured Markdown
  |
  v
writer emits a versioned skill package
  |
  +--> invoke / install
  +--> correct / rollback
  +--> keep local / prepare for gallery
```

The paper's Figure 1 is the main overview diagram. It shows a shared distillation core plus domain presets that add source requirements, evidence checks, consent assumptions, lifecycle metadata, and gallery metadata.

### Application Presets

The repository defines three presets:

- `colleague`: the primary preset for distilling work practices, standards, review criteria, and communication norms;
- `celebrity`: a public-figure preset that emphasizes public evidence, citations, mental models, expression patterns, external reception, and source boundaries;
- `relationship`: a private-interaction preset that stresses consent, retention, local control, deletion, and non-public defaults.

The presets are domain specializations of the same artifact workflow rather than separate systems. A future `self`, `author`, or `team` preset could be added through configuration and prompt design rather than by rebuilding the pipeline.

### Dual Representation

The generated artifact separates capability from bounded behavior.

The capability track captures responsibilities, workflows, technical standards, review criteria, decision heuristics, and lessons from past work. In a workplace example, this is the teammate's actual review judgment: what risks to inspect first, what failures require escalation, and which patterns should block approval.

The behavior track is stored in `persona.md`, but the paper gives it a narrower role than open-ended persona simulation. It captures expression preferences, interaction rules, boundaries, and correction records. The runtime rule is to select relevant behavior constraints, apply the capability or mental-model track, and stay within the artifact's stated limits.

This split is important because persona systems often conflate factual knowledge, procedural judgment, and surface tone. COLLEAGUE.SKILL exposes full, capability-only, and behavior-only variants, so users can preserve work judgment without always invoking style transfer.

### Artifact Contract

The writer emits a versioned schema. The paper states that the current implementation uses schema version 3.

The runtime contract includes:

- `SKILL.md`: combined invokable skill with frontmatter, capability track, behavior track, and operating rules;
- `work.md`: editable capability document for procedures, standards, heuristics, and task patterns;
- `persona.md`: editable behavior document for style, posture, boundaries, and correction logs;
- `work_skill.md`: capability-only entrypoint generated from `work.md`;
- `persona_skill.md`: behavior-only entrypoint generated from `persona.md`;
- `manifest.json`: entrypoints, artifact list, compatible runtimes, slash commands, and toolchain metadata;
- `meta.json`: schema, provenance, lifecycle version, correction count, and compatibility fields.

This contract aligns with the broader Agent Skills standard: a root skill entrypoint can expose metadata first and load deeper instructions only when the skill is invoked. That connects COLLEAGUE.SKILL directly to [[wiki/concepts/Agent Skill]] and [[wiki/topics/AI Skills Workflow]].

### Creation Workflow

Creation starts when the user provides an alias, optional profile fields, and source material. Supported collection paths include Feishu, DingTalk, Slack, WeChat SQLite exports, email archives, PDFs, screenshots, Markdown, and direct paste.

Generation then runs two conceptual tracks: the capability track extracts durable work methods, expert heuristics, or source-grounded mental models; the behavior track extracts expression and interaction patterns under the preset's boundaries. Builders render structured Markdown, and the writer packages the results into the artifact contract.

### Correction and Update Workflow

The paper assumes generated artifacts will be imperfect. The correction handler recognizes natural-language feedback such as "he would not say that" or "she would push back here."

If the correction concerns expert work, the system produces a Markdown patch for a relevant section. Patches with matching level-2 headings replace the corresponding section; unmatched sections are appended. If the correction concerns expression or interaction behavior, it produces a normalized correction record containing scene, wrong behavior, and correct behavior.

The writer then archives the current version, applies the patch or correction, increments lifecycle version, and regenerates all derived artifacts. The version manager can list archived versions, back up current artifacts, roll back to a previous version, and clean old archives. The paper treats this lifecycle as part of the research object, not as after-sales maintenance.

### Public-Figure and Relationship Extensions

The public-figure extension prioritizes first-person works, long-form interviews, documented decisions, expression style, external reception, and timeline evidence. Its quality checker looks for mental-model coverage, limitations, expression patterns, internal tensions, grounding URLs, and copyright-safety signals. The extension records evidence limits and should downgrade confidence when evidence is thin rather than filling gaps with generic persona text.

The relationship extension applies the same package workflow to a more sensitive domain. Its value is not replacing a person; it is representing interaction traces as local, editable, deletable state rather than as an opaque prompt or hidden memory. It requires stronger assumptions about consent, retention, access control, local ownership, and optional sharing.

### Deployment Surface

The system is deployed as an open-source repository, public site, and gallery. The paper reports the following observed public counters:

- approximately 18.5k GitHub stars for the public repository at the time of writing;
- 215 skills in the gallery on 2026-05-28;
- 55 meta-skills in the gallery on 2026-05-28;
- 165 contributors in the gallery on 2026-05-28;
- more than 100k cumulative gallery stars across listed skill cards.

The authors explicitly limit these numbers to deployment and distribution surface. They are not evidence of task performance, behavioral fidelity, or adoption quality.

### Main Limitation

The paper's claims are artifact-level claims. It defines a package format, implements a generation and update workflow, exposes correction and rollback state, supports multiple agent hosts, and shows the same mechanism across colleague, public-figure, relationship, and gallery settings.

It does not prove that generated skills faithfully reproduce a person or improve downstream work. Future evaluation must test whether colleague skills catch the same review issues as source experts, whether capability-only variants preserve utility without persona risk, whether relationship skills encourage overattachment, whether corrections improve behavior without regressions, and whether public-figure skills cite evidence instead of hallucinating motives.

## Integration Decisions

This paper strengthens the local definition of [[wiki/concepts/Agent Skill]] in one specific direction: skills are not only reusable capability bundles; in person-grounded settings they become governed artifacts with provenance, correction records, rollback, deletion, and distribution boundaries.

It also extends [[wiki/topics/AI Skills Workflow]] by adding a lifecycle view for human-trace distillation. The workflow is not complete when a skill first runs; the artifact must support inspection, natural-language correction, regeneration, and rollback.

Claims about public repository stars, gallery scale, and contributor counts should remain source-level. They demonstrate distribution surface, not skill quality.

The paper is adjacent to [[wiki/sources/Agent Skills Survey Paper Source Guide]] and [[wiki/sources/Agent Skills Data-Driven Analysis Paper Source Guide]], but it contributes a different layer. The survey organizes the field; the data-driven paper measures public Claude skills; COLLEAGUE.SKILL proposes a concrete person-grounded generation and governance pipeline.

The reading note's title, "人去，手艺留下", captures a useful local interpretation: the durable object is not the person, but a bounded part of their craft. This phrase is an interpretation from the reading conversation, not a paper claim. ^[inferred]

## Open Questions

- How accurately do generated colleague skills reproduce expert review judgment on held-out work tasks?
- When does the behavior track add useful interaction continuity, and when does it create unnecessary persona risk?
- Who is authorized to correct a person-grounded skill, especially when traces are contested or socially sensitive?
- Can correction records improve the artifact without encoding editor bias or making weak evidence appear settled?
- What evaluation protocol best compares full, capability-only, and behavior-only artifacts under matched source evidence?

## Related

- [[wiki/concepts/Agent Skill]]
- [[wiki/topics/AI Skills Workflow]]
- [[wiki/concepts/Skill Self-Evolution]]
- [[wiki/topics/AI Harness]]
- [[wiki/sources/Agent Skills Survey Paper Source Guide]]
- [[wiki/sources/Agent Skills Data-Driven Analysis Paper Source Guide]]
- [[wiki/sources/Designing Refining and Maintaining Agent Skills at Perplexity Source Guide]]
- [[wiki/sources/默会知识 AI 永远都不可能替代的技能 Source Guide]]
