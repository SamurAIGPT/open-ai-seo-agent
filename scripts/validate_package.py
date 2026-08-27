#!/usr/bin/env python3
"""Validate the portable SEO skill package without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TASKS = (
    "seo-google-serp",
    "seo-keyword-research",
    "seo-domain-overview",
    "seo-backlinks",
    "seo-lighthouse-audit",
    "seo-rank-track",
    "seo-rank-track-batch",
    "seo-local-serp",
    "seo-business-listings",
    "seo-business-profile",
    "seo-business-reviews",
    "seo-ai-mentions",
    "seo-ai-response",
    "seo-keywords-search-volume",
    "seo-keywords-for-keywords",
    "seo-related-keywords",
    "seo-keyword-overview",
    "seo-relevant-pages",
    "seo-backlinks-pages",
    "seo-backlinks-history",
    "seo-ai-mentions-metrics",
    "seo-google-qa",
    "seo-business-updates",
    "seo-account-status",
    "seo-youtube-organic",
    "seo-youtube-video-info",
    "seo-youtube-video-subtitles",
    "seo-youtube-video-comments",
)

CAPABILITIES = {
    task.removeprefix("seo-").replace("-", "_"): task for task in TASKS
}


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter start")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("missing frontmatter end")
    return text[4:end]


def main() -> int:
    errors: list[str] = []
    catalog = (ROOT / "references" / "muapi-seo-tools.md").read_text()

    for task in TASKS:
        if task not in catalog:
            errors.append(f"catalog is missing {task}")

    skills = sorted((ROOT / "agents").glob("*/SKILL.md"))
    if len(skills) != 12:
        errors.append(f"expected 12 skills, found {len(skills)}")

    readme = (ROOT / "README.md").read_text()
    for skill_file in skills:
        try:
            metadata = frontmatter(skill_file.read_text())
        except ValueError as exc:
            errors.append(f"{skill_file}: {exc}")
            continue

        for field in ("name:", "slug:", "version:", "status:", "permissions:"):
            if field not in metadata:
                errors.append(f"{skill_file}: missing {field}")

        capability_names = re.findall(r"^\s+-\s+(seo\.[a-z0-9_]+)\s*$", metadata, re.MULTILINE)
        for capability in capability_names:
            task = CAPABILITIES.get(capability.removeprefix("seo."))
            if task is None:
                errors.append(f"{skill_file}: unknown capability {capability}")

        slug_match = re.search(r"^slug:\s*([a-z0-9-]+)\s*$", metadata, re.MULTILINE)
        if slug_match:
            link = f"agents/{slug_match.group(1)}/SKILL.md"
            if link not in readme:
                errors.append(f"{skill_file}: README does not link {link}")

    for required_file in (
        "AGENTS.md",
        "references/agent-installation.md",
        "references/reports-and-snapshots.md",
    ):
        if not (ROOT / required_file).exists():
            errors.append(f"missing {required_file}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(skills)} skills and {len(TASKS)} Muapi SEO tasks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
