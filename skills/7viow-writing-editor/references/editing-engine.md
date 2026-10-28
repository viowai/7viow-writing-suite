# Scene-Aware Editing

Use for diagnosis, revision, strict style cleanup, and authorized file edits. Select the social setting and the permitted change before diagnosing language.

## Scene and scope

| Scene | Editing aim |
|---|---|
| Chat or comments | Preserve the speaker's register; remove performative reassurance and unnecessary expansion |
| Status or incident note | Keep actors, sequence, result, remaining risk, and next action clear |
| Technical documentation | Preserve terms, commands, retrieval, prerequisites, and reproducible order |
| Public prose | Improve reader movement, evidence, voice, and useful specificity |

Use minimal edits for otherwise sound text. Rebuild structure only when the user permits it and a structural defect calls for it. An explicit word limit or edit budget is a ceiling, not a quota. If satisfying it would lose a material fact or qualifier, show the conflict or a faithful shorter alternative.

## Protect meaning

Before changing a passage, identify numbers, dates, units, names, quotations, terminology, commands, responsibility, causality, conditions, confidence, and deliberately preserved wording. Read the applicable sources when facts need verification.

For a prose-only file edit, keep code blocks, inline code, commands, paths, data, metadata, and link destinations unchanged. Write only the final text to the file, with any material notes beside the deliverable. Paragraphs may merge or split when the scope permits; required information, rankings, and whether events occur together must survive the change.

Make concrete wording carry the supported relation: who does what to which object, why or with what consequence, and for how long when duration matters. Replace nominal chains with actions where that reveals the relation; retain accurate product and service names. A sequence of near-synonymous nouns is not a concrete account of the work.

Compare source and output directly:

- Every required source proposition survives or has an authorized omission.
- Every added factual proposition has a supplied or verified basis.
- Pronouns refer to the same actors; negation, conditions, and comparison targets keep their scope.
- Dates, populations, ranges, exceptions, and non-commitment language retain their meaning.

Use a small mapping for a consequential merge or a long transformation when direct comparison is hard. Ordinary sentence edits do not need a record per clause.

When detail is missing, distinguish an explicitly undecided matter, information absent from the supplied material, and an established rule whose details are not supplied. Absence alone does not establish that a rule is unwritten or an activity has not occurred. Retain the supported meaning and apply the [copy-use check](prose-quality-gate.md#正文用途). Missing information limits what can be asserted; it does not automatically become copy or an appended note.

For example, “设备更换后的前三天，值班员每小时记录一次温度，以判断设备能否持续稳定运行” can become “更换设备后的前三天，值班员每小时记录温度，判断运行是否持续稳定。” “建立稳定性监测机制” loses the actor, action, duration and frequency; adding an alarm threshold would invent a fact.

## Intentional expression and quotation

Preserve an intentional phrase at the location the user identifies; review similar phrases elsewhere on their merits. Contextually valid technical language or ordinary punctuation needs no user-created exception record.

Apply an explicitly requested voice change; otherwise infer voice from the author's actual choices: directness, colloquial phrases, stance, rhythm and degree of warmth. Repair strained collocations, unclear subjects and awkward rhythm while keeping those choices recognizable. A candid commercial objective can remain candid; an abstract voice label is weaker evidence than the supplied prose.

For exact quotations, preserve the quoted words and attribution. If translating, shortening, or paraphrasing is requested, make that treatment clear and preserve the claim's scope. Missing attribution should be reported rather than invented.

## Diagnose, then revise

Prioritize misleading facts, false authority, and broken meaning before rhythm. A phrase is evidence to inspect, not an automatic substitution trigger. Use the appropriate family from pattern-catalog.md when the problem is unclear or repeated.

Choose local wording repair, relation repair, structural revision, or no-change according to the actual defect. Preserve clean passages. For audit-only work, give located findings and their implications without silently rewriting.

### Edit by layer

For explanatory prose, distinguish titles or headings, paragraph leads and supporting sentences where present. Start at the highest layer responsible for the defect: a heading orients the reader, a paragraph lead establishes the point or its relevance, and the body supplies explanation, evidence or action. A concise professional summary can remain in a heading or lead when the body explains it; expand an abstraction only where the reader lacks the needed meaning.

After repairing a heading or paragraph lead, reread the body in that context. Keep it when it now explains the point adequately. This pass is complete when the higher-level claim matches what the body delivers and no necessary explanation remains missing; changing every layer is not a completion requirement.

### Condense by sentence function

For a requested shift of emphasis within a fixed overall length, use [length allocation](composition-engine.md#2-structure) before cutting individual sentences.

Identify what a candidate deletion contributes using the gate's [copy-use check](prose-quality-gate.md#正文用途). Keep an example that explains the claim, a concrete action, a responsibility, a distinct service item or a condition that changes the decision. Combine repeated wording around these functions rather than replacing the functions with a generic summary.

For example, this source contains a removable introduction and useful explanation: “下面是门店活动方案的核心内容。说白了，我们想多卖货；但满减也有成本。比如，顾客原本就要买两件时，第二件降价可能只会少赚，所以先分清哪些订单是活动新增的。” Cut the first sentence; the remaining passage supplies the author's aim, tone, example and decision. “本方案旨在优化促销，实现商业价值” is shorter but removes that work.

Use the direct meaning comparison above to establish fidelity. Calculate a reduction ratio when the user requests one, and name its measure and denominator: character reduction measures text length, page reduction measures pages, and neither establishes semantic coverage.

### Put conditions where they matter

Keep a qualification beside the claim, action or decision it changes. State a shared condition once at the scope where it applies, repeating it only where separate reading would otherwise change the meaning. Verify a fact when the requested edit introduces a claim, exposes a conflict or depends on an unresolved source; an otherwise unrelated established fact does not trigger a fresh whole-document audit.

## Finish

Use [prose-quality-gate.md](prose-quality-gate.md) for the selected settings, every applicable check and mandatory repair/readback. Preserve the fidelity requirements above during every repair. An unchanged passage is valid when it satisfies the applicable gate and no other concrete defect remains. Report a conflict with protected wording rather than silently weakening the settings or discarding meaning.

## Deliver the result

For diagnosis, give located findings and why each affects the reader; a valid passage needs no invented problem. For rewriting, return the revised unit. For a file edit, identify the saved result. Apply the copy-use check to any accompanying text instead of automatically appending source gaps or author notes.

Apply substantive deletions when authorized. If ordinary polishing would require discarding a unique fact or changing a decision, identify that concrete choice first. Do not ask again for an omission already granted. Follow the user's requested comparison dimensions, sequence, and artifact format.
