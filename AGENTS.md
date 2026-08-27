# AI SEO capability instructions

This repository empowers an existing AI agent with SEO workflows and Muapi
tools. Use the host agent for reasoning, planning, approvals, and file
operations.

When this package is available in a project:

1. For a broad SEO request, read agents/seo-strategist/SKILL.md first. For a
   narrow request, read the smallest matching skill under agents/.
2. Read references/muapi-seo-tools.md before selecting Muapi tasks.
3. For a first-party Google request, read references/google-first-party-data.md
   and references/google-setup.md, then use the host's direct Google connector.
4. Check .seo/project.md and prior .seo/sources/ or .seo/snapshots/ when they
   exist.
5. Ask for missing domain, keyword, market, language, device, location,
   competitor, or date-window inputs.
6. Announce broad or potentially expensive calls before making them.
7. Use Muapi results as the source of truth for Muapi-backed capabilities and
   preserve source metadata.
8. Write only local reports and snapshots; do not modify external SEO assets.
9. Never invent metrics, rankings, citations, reviews, trends, or provider
   capabilities.
10. For the user's own search performance, clicks, impressions, CTR, position,
   landing pages, or conversions, prefer the directly connected Search Console
   or Google Analytics property. Do not route user-owned Google data through
   Muapi or substitute third-party estimates when first-party data is
   available.

Choose the smallest skill that answers the request. Compose skills when the
question requires multiple evidence types, and explain the dependency order in
the report.
