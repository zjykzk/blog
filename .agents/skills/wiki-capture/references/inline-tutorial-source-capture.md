# Inline Tutorial Source Capture Pattern

Use this reference when the capture target is an inline educational/tutorial explanation pasted directly in chat, especially Chinese prose with code examples and an explicit `不用翻译` constraint.

## Classification

- Default to `source` when the pasted material is itself a teaching artifact: a structured explanation, walkthrough, comparison, or code tutorial.
- Do not promote directly to `concept` just because the tutorial contains clear mental models. Preserve the teaching sequence first; later concept pages can lift the stable abstractions.
- If the tutorial extends an existing domain cluster, link to the stable concept/topic/synthesis pages rather than creating duplicate concept pages.

## Preservation

Preserve the source-level shape:

- the initial framing problem;
- the named mental models;
- code examples;
- comparison tables;
- warnings / judgment standards;
- bottom-layer explanation;
- one-sentence summaries.

For `不用翻译`, keep Chinese prose in the body, summary, index entry, hot entry, map note, and final confirmation. English filenames are acceptable when local naming conventions or duplicate avoidance make them clearer, but the readable source layer should stay Chinese.

## Integration

For code/tutorial sources, the `Integration Decisions` section should state:

- which claims remain source-level teaching material;
- which abstractions are promotable later;
- which existing concept/topic/synthesis pages this source strengthens;
- whether any new concept page is needed now or should remain a plain future question.

## Verification nuance

After writing the source guide, verify not only the new note but also the practical entrypoint. For frontend/code tutorials, this often means adding the source to `CS Map` or another relevant domain map so it is not only present in `index.md` but discoverable from the domain cluster.
