#!/usr/bin/env python3
"""Detect bilingual writing-pattern signals without judging authorship."""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


SCHEMA_VERSION = 3
DISCLAIMER = (
    "These are contextual writing-quality signals, not proof of AI authorship. "
    "Review every finding against genre, source facts, and the writer's intended voice."
)
SEVERITY_ORDER = {"P0": 0, "P1": 1, "P2": 2}
CONTEXTS = (
    "general",
    "social",
    "blog",
    "technical",
    "high-trust-email",
    "docs",
    "casual",
)


@dataclass(frozen=True)
class Rule:
    rule_id: str
    severity: str
    family: str
    pattern: str
    message: str
    suggestion: str
    flags: int = re.IGNORECASE
    languages: tuple[str, ...] = ("en", "zh", "mixed")


RULES: tuple[Rule, ...] = (
    Rule(
        "chatbot-artifact",
        "P0",
        "credibility",
        r"\b(?:great question|i hope this helps|feel free to ask|let me know if you(?:'d| would) like)\b|"
        r"(?:很高兴(?:为你|能)|希望(?:这些|这)(?:能|会)帮到你|如果你愿意[，,]?我可以)",
        "Visible assistant or service-script language remains in reader-facing prose.",
        "Check whether this is intended reader-facing language; remove drafting residue only when it is out of place.",
    ),
    Rule(
        "cutoff-disclaimer",
        "P0",
        "credibility",
        r"\b(?:as of my last (?:update|knowledge)|my knowledge cutoff)\b|截至我的(?:知识|资料)",
        "A model-style knowledge disclaimer appears in the prose.",
        "Replace it with a sourced date boundary or remove it.",
    ),
    Rule(
        "vague-attribution",
        "P0",
        "source-boundary",
        r"\b(?:studies|research|experts|analysts|data) (?:show|shows|suggest|suggests|indicate|indicates|say|says)\b|"
        r"(?:研究表明|数据显示|专家(?:认为|表示)|业内人士(?:认为|表示)|有研究认为)",
        "The claim invokes authority without a named, checkable source.",
        "Name and verify the source, remove the authority wrapper, or mark a source gap.",
    ),
    Rule(
        "significance-inflation",
        "P0",
        "credibility",
        r"\b(?:game[- ]changer|groundbreaking|revolutionary|transformative|historic|pivotal)\b|"
        r"(?:颠覆性|革命性|历史性|里程碑式|意义重大|划时代)",
        "The wording inflates significance beyond the evidence shown.",
        "State the concrete change or consequence instead.",
    ),
    Rule(
        "reasoning-artifact",
        "P0",
        "model-artifact",
        r"(?:^|\n)\s*(?:analysis|chain of thought|reasoning)\s*:|(?:思考过程|内部推理|推理链)\s*[：:]",
        "Internal reasoning or workflow residue appears in output prose.",
        "Remove it and retain only the conclusion and necessary evidence.",
    ),
    Rule(
        "ai-citation-markup",
        "P0",
        "model-artifact",
        r"(?:turn\d+(?:search|view|fetch)\d+|\[source:\s*\d+\]|cite[^]+)",
        "Interface-specific citation markup leaked into the text.",
        "Replace it with a real reader-facing citation or remove it.",
        flags=re.IGNORECASE,
    ),
    Rule(
        "unfilled-placeholder",
        "P0",
        "model-artifact",
        r"\[(?:insert|add|todo|tbd|placeholder)[^\]]*\]|<(?:insert|add|todo|tbd)[^>]*>|(?:待补|待填写|占位符)",
        "An unresolved placeholder remains in the content.",
        "Fill it from a verified source or keep the gap outside final copy.",
    ),
    Rule(
        "ai-tool-url",
        "P0",
        "model-artifact",
        r"[?&]utm_source=(?:chatgpt|openai|claude|perplexity)(?:&|\b)",
        "An AI-tool tracking parameter remains in a URL.",
        "Remove the tracking parameter and preserve the destination.",
    ),
    Rule(
        "throat-clearing",
        "P1",
        "filler",
        r"\b(?:here(?:'s| is) (?:the thing|why|what|the problem)|let me be clear|the uncomfortable truth is)\b|"
        r"(?:值得注意的是|值得一提的是|结论先说|直接说结论|首先要说|让我来(?:解释|说明))",
        "The sentence announces a point before making it.",
        "Cut the announcement and lead with the claim or action.",
    ),
    Rule(
        "generic-conclusion",
        "P1",
        "conclusion",
        r"\b(?:in conclusion|overall|at the end of the day|the future (?:is|looks) bright)\b|"
        r"(?:综上所述|总的来说|归根结底|未来可期|让我们拭目以待)",
        "The ending summarizes or uplifts without adding information.",
        "End on the last supported consequence, decision, or action.",
    ),
    Rule(
        "business-jargon",
        "P1",
        "register",
        r"\b(?:leverage|unpack|lean into|game[- ]changer|double down|deep dive|circle back|moving forward)\b|"
        r"(?:赋能|抓手|闭环|对齐颗粒度|收窄问题|兜住需求|能力落盘)",
        "Jargon may be replacing the actual action.",
        "Use the concrete action unless the term is literal in this domain.",
    ),
    Rule(
        "sycophantic-tone",
        "P1",
        "stance",
        r"\b(?:you(?:'ve| have) (?:nailed|identified) (?:the|a)|excellent point|brilliant question)\b|"
        r"(?:你问到了.{0,12}核心|这个判断非常(?:精准|深刻)|顶刊作者的素养|方向完全是对的)",
        "Praise or certification substitutes for analysis.",
        "Respond to the evidence or request without awarding status.",
    ),
    Rule(
        "mind-reading",
        "P1",
        "stance",
        r"\byou(?:'re| are) not [^.?!]{1,50}[,;:]? you(?:'re| are) just\b|"
        r"(?:你不是.{0,30}你只是|稳稳接住|我完全理解你的感受|你内心其实)",
        "The prose claims access to a person's internal state without evidence.",
        "Use a bounded acknowledgment or describe the observable situation.",
    ),
    Rule(
        "binary-contrast",
        "P1",
        "structure",
        r"\bnot\s+[^.!?\n]{1,80}\s+but\s+[^.!?\n]{1,80}|"
        r"(?:不是.{1,50}而是|与其.{1,50}不如|并非.{1,50}而是)",
        "A mechanical contrast delays the positive claim.",
        "State the intended claim directly unless both sides carry facts.",
    ),
    Rule(
        "negative-listing",
        "P1",
        "structure",
        r"\bnot\s+[^.!?]{1,40}[.!]\s+not\s+[^.!?]{1,40}[.!]\s+(?:it (?:is|was)|but)\b|"
        r"(?:不是.{1,30}[。！!]\s*不是.{1,30}[。！!]\s*(?:而是|是))",
        "Repeated negation creates a staged reveal.",
        "Start with the positive definition.",
    ),
    Rule(
        "future-narrative",
        "P1",
        "conclusion",
        r"\b(?:will undoubtedly|will inevitably|may become one of the most|poised to reshape)\b|"
        r"(?:注定将|必将成为|未来必然|有望成为最)",
        "A generic prediction substitutes for evidence.",
        "State the current evidence and bounded implication.",
    ),
    Rule(
        "social-cta",
        "P1",
        "engagement",
        r"\b(?:agree\?|what do you think\?|share this|follow for more|thank me later)\b|"
        r"(?:你怎么看[？?]|评论区见|点赞收藏|转发给需要的人)",
        "The ending uses generic engagement bait.",
        "Use a task-specific action or end without a CTA.",
    ),
    Rule(
        "real-actual-inflation",
        "P2",
        "word-choice",
        r"\b(?:the )?(?:real|actual|true)\s+[a-z][a-z-]+\b|(?:真正的|本质上|真正意义上的)",
        "A real/actual phrase appears; check whether it names a meaningful distinction.",
        "Retain a literal distinction, or name the property if the label adds no meaning.",
    ),
    Rule(
        "transition-cluster-item",
        "P2",
        "transition",
        r"\b(?:moreover|furthermore|additionally|consequently|nevertheless)\b|(?:此外|与此同时|进一步来说|因此可以看出)",
        "A formal transition appears; inspect repetition and its relation to the surrounding ideas.",
        "Keep it only if it clarifies a real relationship.",
    ),
)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Report writing-pattern signals as JSON without judging authorship."
    )
    parser.add_argument("path", nargs="?", help="UTF-8 text or Markdown file to audit.")
    parser.add_argument("--text", help="Audit this literal text instead of a file or stdin.")
    parser.add_argument(
        "--language",
        choices=("auto", "en", "zh", "mixed"),
        default="auto",
        help="Language hint; default auto.",
    )
    parser.add_argument("--context", choices=CONTEXTS, default="general")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON.")
    return parser.parse_args(argv)


def read_input(args: argparse.Namespace) -> tuple[str, str]:
    if args.path and args.text is not None:
        raise ValueError("provide only one of path or --text")
    if args.text is not None:
        return args.text, "literal-text"
    if args.path:
        path = Path(args.path)
        if not path.is_file():
            raise ValueError(f"input file does not exist: {path}")
        return path.read_text(encoding="utf-8"), str(path)
    if sys.stdin.isatty():
        raise ValueError("provide a path, --text, or stdin")
    return sys.stdin.read(), "stdin"


def detect_language(text: str) -> str:
    cjk = len(re.findall(r"[\u3400-\u9fff]", text))
    latin = len(re.findall(r"[A-Za-z]", text))
    if cjk >= 4 and latin >= 12:
        return "mixed"
    if cjk >= 4:
        return "zh"
    return "en"


def protected_spans(text: str) -> list[tuple[int, int]]:
    patterns = (
        r"```[\s\S]*?```",
        r"`[^`\n]+`",
        r"https?://[^\s)\]}>]+",
    )
    spans: list[tuple[int, int]] = []
    for pattern in patterns:
        spans.extend(match.span() for match in re.finditer(pattern, text))
    return merge_spans(spans)


def merge_spans(spans: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    merged: list[list[int]] = []
    for start, end in sorted(spans):
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return [(start, end) for start, end in merged]


def mask_spans(text: str, spans: Sequence[tuple[int, int]]) -> str:
    chars = list(text)
    for start, end in spans:
        for index in range(start, end):
            if chars[index] != "\n":
                chars[index] = " "
    return "".join(chars)


def line_column(text: str, start: int) -> tuple[int, int]:
    line = text.count("\n", 0, start) + 1
    last_newline = text.rfind("\n", 0, start)
    column = start + 1 if last_newline < 0 else start - last_newline
    return line, column


def raw_style_counts(text: str, masked: str) -> dict[str, object]:
    """Locate candidates; the skill classifies quotations and applies its limits."""
    patterns = {
        "quote_pairs": r'"[^"\n]+"|“[^”\n]+”|「[^」\n]+」|『[^』\n]+』|‘[^’\n]+’',
        "dash_runs": r"—+|(?<!-)---+(?!-)",
        "colons": r"[:：]",
        "semicolons": r"[;；]",
        "er_shi": r"而是",
        "binary_contrast": r"(?:不是|并非)[^。！？!?\n]{0,80}?而是",
        "additive_frames": r"(?:不仅|不只|不但)[^。！？!?\n]{0,80}?(?:而且|还|也|更)",
        "stock_closers": r"换句话说|归根结底|本质上|真正重要的是",
    }
    # Markdown rules are layout; hyphens inside words are not dash runs.
    scan = re.sub(r"(?m)^ {0,3}(?:-{3,}|—{3,})[ \t]*$", lambda m: " " * len(m.group()), masked)
    metrics = {}
    for name, pattern in patterns.items():
        occurrences = []
        for match in re.finditer(pattern, scan):
            line, column = line_column(text, match.start())
            occurrences.append({"start": match.start(), "end": match.end(),
                                "line": line, "column": column,
                                "text": text[match.start():match.end()]})
        metrics[name] = {"count": len(occurrences), "occurrences": occurrences}
    return {"status": "context-review-required",
            "scope": "Raw candidates excluding code and URLs; genuine quotations, necessary structure and semantic defects require contextual review. Apply limits from prose-quality-gate.md.",
            "metrics": metrics}


def adjusted_severity(rule: Rule, context: str) -> str | None:
    severity = rule.severity
    if context == "casual" and severity == "P2":
        return None
    if context in {"technical", "docs"} and rule.rule_id in {
        "business-jargon",
        "transition-cluster-item",
    }:
        return None if severity == "P2" else "P2"
    if context == "high-trust-email" and severity == "P2":
        return "P1"
    if context == "social" and rule.rule_id in {"transition-cluster-item"}:
        return None
    return severity


def regex_findings(
    *, text: str, masked: str, language: str, context: str
) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    for rule in RULES:
        if language not in rule.languages:
            continue
        severity = adjusted_severity(rule, context)
        if severity is None:
            continue
        for match in re.finditer(rule.pattern, masked, rule.flags):
            start, end = match.span()
            evidence = re.sub(r"\s+", " ", text[start:end]).strip()
            if not evidence:
                continue
            line, column = line_column(text, start)
            findings.append(
                {
                    "rule_id": rule.rule_id,
                    "severity": severity,
                    "family": rule.family,
                    "evidence": evidence[:240],
                    "start": start,
                    "end": end,
                    "line": line,
                    "column": column,
                    "message": rule.message,
                    "suggestion": rule.suggestion,
                    "requires_context_review": True,
                }
            )
    return findings


def sentence_lengths(masked: str, language: str) -> list[int]:
    lengths: list[int] = []
    for match in re.finditer(r"[^.!?。！？\n]+[.!?。！？]?", masked):
        sentence = match.group(0).strip()
        if not sentence:
            continue
        if language == "en":
            length = len(re.findall(r"\b[\w'-]+\b", sentence))
        else:
            cjk = len(re.findall(r"[\u3400-\u9fff]", sentence))
            words = len(re.findall(r"\b[A-Za-z0-9][\w'-]*\b", sentence))
            length = cjk + words
        if length:
            lengths.append(length)
    return lengths


def document_findings(
    *, text: str, masked: str, language: str, context: str
) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    lengths = sentence_lengths(masked, language)
    if len(lengths) >= 4:
        mean = statistics.fmean(lengths)
        stdev = statistics.pstdev(lengths)
        coefficient = stdev / mean if mean else 0.0
        if coefficient < 0.25 and context not in {"docs", "casual"}:
            findings.append(
                {
                    "rule_id": "uniform-sentence-rhythm",
                    "severity": "P2",
                    "family": "rhythm",
                    "evidence": f"sentence length CV={coefficient:.2f} across {len(lengths)} sentences",
                    "start": 0,
                    "end": 0,
                    "line": 1,
                    "column": 1,
                    "message": "Sentence lengths are unusually uniform for this context.",
                    "suggestion": "Vary one or two sentence shapes after confirming the rhythm is not deliberate.",
                    "requires_context_review": True,
                }
            )

    hashtags = re.findall(r"(?<!\w)#[\w\u3400-\u9fff-]+", masked)
    if len(hashtags) >= 5 and context not in {"docs", "technical"}:
        findings.append(
            {
                "rule_id": "hashtag-stuffing",
                "severity": "P0" if context == "high-trust-email" else "P1",
                "family": "formatting",
                "evidence": " ".join(hashtags[:8]),
                "start": 0,
                "end": 0,
                "line": 1,
                "column": 1,
                "message": "The text contains a dense hashtag cluster.",
                "suggestion": "Keep only platform-relevant tags or remove them.",
                "requires_context_review": True,
            }
        )

    return findings


def stats_for(text: str, masked: str, language: str, protected: Sequence[tuple[int, int]]) -> dict[str, object]:
    lengths = sentence_lengths(masked, language)
    mean = statistics.fmean(lengths) if lengths else 0.0
    stdev = statistics.pstdev(lengths) if len(lengths) >= 2 else 0.0
    return {
        "characters": len(text),
        "latin_words": len(re.findall(r"\b[A-Za-z0-9][\w'-]*\b", text)),
        "cjk_characters": len(re.findall(r"[\u3400-\u9fff]", text)),
        "paragraphs": len([part for part in re.split(r"\n\s*\n", text) if part.strip()]),
        "sentences": len(lengths),
        "mean_sentence_length": round(mean, 2),
        "sentence_length_stdev": round(stdev, 2),
        "sentence_length_cv": round(stdev / mean, 3) if mean else 0.0,
        "protected_spans": len(protected),
    }


def deduplicate(findings: Iterable[dict[str, object]]) -> list[dict[str, object]]:
    unique: dict[tuple[object, object, object], dict[str, object]] = {}
    for finding in findings:
        key = (finding["rule_id"], finding["start"], finding["evidence"])
        unique[key] = finding
    return sorted(
        unique.values(),
        key=lambda item: (SEVERITY_ORDER[str(item["severity"])], int(item["start"]), str(item["rule_id"])),
    )


def summarize(findings: Sequence[dict[str, object]]) -> dict[str, object]:
    counts = {severity: 0 for severity in SEVERITY_ORDER}
    families: set[str] = set()
    for finding in findings:
        counts[str(finding["severity"])] += 1
        families.add(str(finding["family"]))
    recommendation = "review-signals-in-context" if findings else "no-mechanical-signals"
    return {
        "counts": counts,
        "distinct_families": len(families),
        "total": len(findings),
        "recommendation": recommendation,
    }


def audit(
    text: str,
    *,
    source: str = "literal-text",
    language_hint: str = "auto",
    context: str = "general",
) -> dict[str, object]:
    language = detect_language(text) if language_hint == "auto" else language_hint
    protected = protected_spans(text)
    masked = mask_spans(text, protected)
    findings = deduplicate(
        [
            *regex_findings(
                text=text,
                masked=masked,
                language=language,
                context=context,
            ),
            *document_findings(
                text=text,
                masked=masked,
                language=language,
                context=context,
            ),
        ]
    )
    return {
        "schema_version": SCHEMA_VERSION,
        "source": source,
        "language": language,
        "context": context,
        "authorship_verdict": None,
        "disclaimer": DISCLAIMER,
        "stats": stats_for(text, masked, language, protected),
        "raw_style_counts": raw_style_counts(text, masked),
        "findings": findings,
        "summary": summarize(findings),
    }


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        text, source = read_input(args)
        if not text.strip():
            raise ValueError("input text is empty")
        payload = audit(
            text,
            source=source,
            language_hint=args.language,
            context=args.context,
        )
    except (OSError, UnicodeError, ValueError) as error:
        print(f"audit configuration error: {error}", file=sys.stderr)
        return 2

    indent = 2 if args.pretty else None
    print(json.dumps(payload, ensure_ascii=False, indent=indent, sort_keys=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
