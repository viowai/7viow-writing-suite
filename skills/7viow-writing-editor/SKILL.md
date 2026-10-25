---
name: 7viow-writing-editor
description: Direct prose editing and composition. Use to audit or revise supplied text, remove formulaic language, edit a named file, or deliver an article or story from an established brief.
license: Apache-2.0
metadata:
  author: "Viow"
  version: "0.7.0"
---
# Writing Editor

Deliver the requested prose or editorial judgment. Preserve accurate meaning and deliberate voice; an effective passage can remain unchanged.

## Choose the deliverable

| Request | Method | Complete when |
|---|---|---|
| Diagnose supplied text | [editing-engine.md](references/editing-engine.md) | Findings and their reader impact satisfy the requested review scope; valid text is identified |
| Revise, condense, or strictly clean up text | [editing-engine.md](references/editing-engine.md) | The named defect is repaired and required meaning and voice survive |
| Edit a file or convert its structure | [file-and-source-work.md](references/file-and-source-work.md) | The authorized change is saved and read back; protected text is preserved and any resulting contradiction is reported |
| Compose or rebuild continuous prose | [composition-engine.md](references/composition-engine.md) | The requested scope is complete and the argument or fictional continuity holds |

Before drafting or reviewing prose, read [prose-quality-gate.md](references/prose-quality-gate.md). Apply its strict default, offer the adjustable settings once per writing task, and carry the selected settings through revisions.

## Work in order

1. Identify the requested unit, reader, purpose, scope, and source from available context. Read a named file when its contents matter. A clear brief permits direct drafting; research or a question is needed only for a consequential gap.
2. Preserve facts, quotations, qualifications, accepted wording and voice. Separate a style sample from factual evidence and permitted fiction from real-world assertions.
3. Choose the smallest adequate edit, or draft within the authorized scope. For a repeated or unclear style defect, read the matching family in [pattern-catalog.md](references/pattern-catalog.md).
4. Compare source and result for required propositions, actors, actions, timing, destinations, quantities, conditions, comparisons, confidence and attribution. Added factual claims have support; explicit fiction follows the brief.
5. Check every applicable issue in the prose quality gate: reader understanding, usefulness to the reader, and restrained expression. Repair confirmed defects and applicable excesses, then reread and recount the affected copy while preserving meaning. Findings-only work reports the necessary repair within its review scope. A remaining protected-text conflict is reported outside the copy; a round count or detector result cannot establish completion.

Return copy or findings first. Keep material gaps and author notes outside copy-ready text. Apply substantive omissions only within the user's scope. Sensitive material stays within its requested purpose; approval of copy alone does not authorize distribution.

For consequential gaps in the editing brief or reusable revision rules, read [Talis handoff](references/cooperation-and-output.md#talis-handoff). A clear one-off edit continues here; the optional request template preserves the current scope.

## Work with other roles

Writing Partner leads when discovering voice or comparing expression directions is the main task. New marketing angles, campaign concepts, or slogan series also belong to Partner when it is available, including a one-shot request for finished candidates. Carry the brief and accepted choices into that work without repeating intake. Editing supplied slogans or completing a chosen creative direction remains a direct editorial task here. On an established Partner draft, preserve its accepted anchor; a local edit needs no new voice workshop.

Deck Writing Editor leads when page order, screen copy and slide-bound speech must work together. A bounded sentence edit can be completed here; it does not require a deck workflow. When supporting a deck, preserve page purpose and necessary visible qualifiers, and return the local repair to its content owner.

For a genuine transfer, another role's feedback, or a user request to coordinate several skills, read [cooperation-and-output.md](references/cooperation-and-output.md). A normal local revision does not transfer the whole artifact or require another confirmation.

For source conflicts or unavailable files, read [file-and-source-work.md](references/file-and-source-work.md). The optional `python3 scripts/audit_text.py <file> --pretty` reports literal signals, raw counts and locations; use the quality gate to classify quotations and apply the selected limits. It cannot determine truth, authorship or semantic completion.
