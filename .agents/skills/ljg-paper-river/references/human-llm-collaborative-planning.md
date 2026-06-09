# Human-LLM collaborative planning river notes

Session-derived reference notes for paper-river tasks around human-LLM co-planning, multi-agent plan DAGs, and process-level supervision.

## Target paper handled

- He, Kim, Zhang, Hruschka (2026), "How to Steer Your Multi-Agent System: Human-LLM Collaborative Planning", arXiv:2605.23023 / ACM CAIS 2026.
- Core contribution: formalizes human-LLM co-planning interactions for orchestrated MAS along three axes: mode (semantic vs structural), scope (global vs targeted), and level (low-level vs high-level edits). Implements AMBIPOM and studies user workflows plus LLM revision strategies.

## Useful lineage chain

Use this as a candidate main chain when a paper is about controllable LLM/MAS planning interfaces:

1. Shneiderman (1983), "Direct Manipulation: A Step Beyond Programming Languages"
   - Problem: command-style interaction distances user intent from visible objects.
   - Contribution: make objects visible and directly editable.

2. Horvitz (1999), "Principles of Mixed-Initiative User Interfaces"
   - Problem: pure automation and pure manual control both fail in complex tasks.
   - Contribution: frame interaction as initiative shifting between human and machine.

3. Wu, Terry, Cai (2022), "AI Chains: Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts"
   - Problem: one-shot LLM calls hide intermediate failure points in complex tasks.
   - Contribution: split tasks into inspectable/editable LLM chains with intermediate results.

4. Kim, Mitra, Shen, Zhang, Hruschka (2025), "AIPOM: Agent-aware Interactive Planning for Multi-Agent Systems"
   - Problem: multi-agent systems need explicit agent assignment, dataflow, and execution dependencies, not just prompt chains.
   - Contribution: plan as editable DAG with chat + graph interface for human-in-the-loop planning.

5. He, Kim, Zhang, Hruschka (2026), "AMBIPOM / How to Steer Your Multi-Agent System"
   - Problem: AIPOM-style interaction has mode choices but not a full account of global/local scope and low/high-level edit trade-offs.
   - Contribution: design space for plan steering; findings around effort-control-risk, hybrid workflows, boundary integration, and verification burden.

## Caveats

- Treat AI Chains -> AIPOM partly as problem inheritance, not necessarily a direct technical baseline: AIPOM cites AI Chains and related workflow systems, but shifts from LLM prompt chains to agent-aware DAG plans.
- MAPGEN and other mixed-initiative planning systems are useful historical context, but unless the target paper explicitly treats them as the direct baseline, avoid making them the main technical predecessor.
- For very recent target papers, downstream citation discovery may be empty. State the date and absence honestly, then discuss adjacent frontiers such as COCOA, Magentic-UI, plan diff preview, boundary contract checking, and verifier-centered plan change review.

## Narrative lens that worked

The strongest problem-axis framing was:

"AI output evolves from result object -> process object -> structured plan object -> governable change object."

This supports a readable Chinese explanation:

- AI Chains: expose intermediate LLM steps.
- AIPOM: objectify multi-agent plans as DAGs.
- AMBIPOM: compare intervention types and surface effort-control-risk trade-offs.
- Next step: verify and govern plan changes with diffs, boundary contracts, and risk-triggered checks.
