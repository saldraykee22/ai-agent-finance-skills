#!/usr/bin/env python3
"""Evaluate lexical separability of skill descriptions on routing prompts."""

from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r"[a-z0-9]+", re.IGNORECASE)
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---", re.DOTALL)
STOP = {
    "a", "an", "and", "as", "across", "for", "from", "how", "in", "into", "is", "it",
    "my", "of", "on", "or", "the", "this", "to", "use", "user", "when", "with",
    "analysis", "analyze", "finance", "financial", "market", "asks",
}


def tokens(text: str) -> list[str]:
    return [token.lower() for token in TOKEN.findall(text) if token.lower() not in STOP]


def descriptions() -> dict[str, str]:
    result = {}
    for folder in (ROOT / "skills").iterdir():
        if not folder.is_dir():
            continue
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
        match = FRONTMATTER.match(text)
        if not match:
            continue
        fields = {}
        for line in match.group(1).splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip()
        result[fields["name"]] = f"{fields['name'].replace('-', ' ')} {fields['description']}"
    return result


def rank(prompt: str, docs: dict[str, str]) -> list[tuple[str, float]]:
    doc_tokens = {name: tokens(text) for name, text in docs.items()}
    document_frequency = Counter()
    for values in doc_tokens.values():
        document_frequency.update(set(values))
    query = Counter(tokens(prompt))
    scores = {}
    for name, values in doc_tokens.items():
        counts = Counter(values)
        score = 0.0
        for term, query_count in query.items():
            if term not in counts:
                continue
            inverse_frequency = math.log((1 + len(docs)) / (1 + document_frequency[term])) + 1
            score += query_count * (1 + math.log(counts[term])) * inverse_frequency
        scores[name] = score
    return sorted(scores.items(), key=lambda item: (-item[1], item[0]))


def cosine(left: str, right: str) -> float:
    a, b = Counter(tokens(left)), Counter(tokens(right))
    numerator = sum(value * b[term] for term, value in a.items())
    denominator = math.sqrt(sum(value * value for value in a.values())) * math.sqrt(
        sum(value * value for value in b.values())
    )
    return numerator / denominator if denominator else 0.0


def main() -> int:
    docs = descriptions()
    cases = json.loads((ROOT / "evals" / "routing-cases.json").read_text(encoding="utf-8"))
    failures = []
    non_top1 = []
    top1 = top3 = 0
    for case in cases:
        ranking = rank(case["prompt"], docs)
        names = [name for name, _ in ranking]
        position = names.index(case["expected"]) + 1
        top1 += position == 1
        top3 += position <= 3
        if position > 1:
            non_top1.append(
                f"rank {position}: {case['expected']} <- {case['prompt']} "
                f"(top: {names[0]})"
            )
        if position > 3:
            failures.append(
                f"route rank {position}: {case['expected']} <- {case['prompt']} "
                f"(top3: {', '.join(names[:3])})"
            )

    overlaps = []
    names = sorted(docs)
    for index, left in enumerate(names):
        for right in names[index + 1 :]:
            similarity = cosine(docs[left], docs[right])
            if similarity >= 0.72:
                overlaps.append((similarity, left, right))
    if overlaps:
        failures.extend(
            f"description overlap {score:.2f}: {left} / {right}"
            for score, left, right in sorted(overlaps, reverse=True)
        )

    accuracy = top1 / len(cases)
    coverage = top3 / len(cases)
    print(f"Routing eval: top1={top1}/{len(cases)} ({accuracy:.1%}), top3={top3}/{len(cases)} ({coverage:.1%})")
    if non_top1:
        print("Non-top1 diagnostics:\n" + "\n".join(non_top1))
    if failures:
        print("\n".join(failures))
    if coverage < 0.95 or accuracy < 0.75 or overlaps:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
