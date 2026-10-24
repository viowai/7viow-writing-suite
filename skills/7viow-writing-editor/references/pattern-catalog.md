# Contextual Style Patterns

Use a pattern to locate a possible defect, then decide from the passage's purpose. A phrase, punctuation mark, grammatical form, or combination of hits cannot identify an author as human or AI.

Use the quality gate's [reader-understanding](prose-quality-gate.md#读者理解) and [copy-use](prose-quality-gate.md#正文用途) checks for unclear referents and drafting material in reader copy. Possible residues include drafting greetings, offers to continue, unfinished placeholders, opaque citation markers and descriptions of how the text was assembled. A quotation, a document about those items, or useful source/navigation guidance can legitimately contain them; decide from the reader's task.

## Diagnose the effect, not the token

| Possible defect | Inspect | Useful repair and valid exceptions |
|---|---|---|
| Unsupported authority | “研究表明”, “experts agree”, endorsements without a usable source | Check the source or narrow the claim; retain attribution that is actually supported |
| Inflated significance | “前所未有”, “revolutionary”, broad promises resting on a small observation | State what changed and its evidence ceiling; strong claims may remain when evidence earns them |
| Reply to the wrong reader | A reply repeats background the recipient supplied or agreed to and buries the answer | When the surrounding exchange is available, lead with the requested decision or change and keep the new fact needed to act; apply the gate's reader-understanding check to standalone documents |
| Performed certainty or emotion | Praise, mind reading, generic reassurance, ceremonial uplift | Respond to the actual event or request; preserve warranted warmth and the chosen voice |
| Missing progression | “因此”, “此外” or a new label carrying a connection the sentences never explain | Write the supported causal, explanatory or sequential relation; give a distinct idea its own paragraph when needed. Each sentence should advance the paragraph's point |
| Unnecessary modifiers | Intensifiers or hedges that add nothing | Remove only when meaning survives; timing, degree, probability, and real uncertainty remain |
| Translation-heavy Chinese | Long nominal chains, literal passive constructions, repeated “通过…来…” | Restore natural information order while preserving the technical relation and actor |

Frequency limits, abstraction, contrast, repetition, structure, emphasis, rhythm and endings belong to [prose-quality-gate.md](prose-quality-gate.md). Apply its selected settings and mandatory repair completion instead of maintaining a second checklist here. The families above add evidence, reader and language checks.

## Scene and voice

Chat can use fragments; documentation can use repeated terms and lists; research can need uncertainty; a letter can be warm. Use these as context for diagnosis, then follow the author's actual choices as described in [editing-engine.md](editing-engine.md#intentional-expression-and-quotation).

Do not invent a human actor to replace an accurate system subject. Do not add a personal anecdote to make a passage sound human. Structure needs rebuilding only when reader movement is broken and that change is authorized.

## Mechanical support

`scripts/audit_text.py` reports contextual signals and raw punctuation/phrase counts with locations. Code and URL destinations are masked; ordinary quotation marks do not hide their contents. A signal within a genuine quotation is for contextual review, not permission to alter it.

Apply the selected limits from [prose-quality-gate.md](prose-quality-gate.md) after identifying protected content. The script provides no style score, authorship verdict or semantic pass. No mechanical signals means only that this detector found none.
