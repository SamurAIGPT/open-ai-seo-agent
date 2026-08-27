---
name: Rank Tracking
slug: rank-tracking
version: 2.0.0
category: seo
description: Capture comparable ranking snapshots and explain changes between runs using Muapi rank and SERP data.
status: ready
muapi_capabilities:
  - seo.rank_track
  - seo.rank_track_batch
  - seo.google_serp
  - seo.account_status
required_connections:
  - muapi
permissions:
  - external-read-only
  - workspace-write
---

# Rank Tracking

## Mission

Measure search visibility consistently across repeated runs. A ranking trend is
valid only when the query set and search context are comparable.

## Required inputs

- Target domain.
- Keyword list, or a confirmed list from .seo/project.md.
- Country, language, device, and result depth.
- Optional: previous snapshot, comparison date, competitor domains, and
  priority URL groups.

## Workflow

1. Read .seo/project.md and locate the most recent compatible ranking snapshot.
2. Normalize and deduplicate the keyword list. Keep the exact query text used
   for the provider.
3. Check seo.account_status when balance or limits are unknown.
4. Use seo.rank_track_batch for up to 50 comparable keywords per call. Split a
   larger list into chunks with identical target domain, location, language,
   device, and depth. Ask before a broad or repeated run.
5. Use seo.rank_track for a single diagnostic term or when a batch result needs
   verification.
6. Use seo.google_serp for high-priority terms where the user needs the live
   result composition, SERP features, or competing URLs—not as a replacement
   for the complete tracked set.
7. Save the raw request and response as a dated snapshot before calculating
   changes.
8. Compare only compatible snapshots. Calculate position change as previous
   position minus current position; positive means improvement. Keep found,
   not-found, and provider-error states distinct.
9. Summarize winners, losers, stable terms, new terms, lost terms, and URL
   changes. Recommend investigation, not causation, unless other evidence
   supports it.

## Decision rules

- Never compare different markets, devices, depths, or keyword spellings as if
  they were a trend.
- A single keyword movement is a signal, not proof of a site-wide change.
- Do not convert an unranked result into an arbitrary numeric position.
- Do not call a change an algorithm event without a broader dataset and
  independent evidence.
- Rank trackers are snapshots here. Recurring execution belongs to the host
  agent, a scheduled task, or the user's workflow.

## Output format

Return:

- run scope and retrieval timestamp
- visibility rate and top-10 rate, with formulas and denominators
- keyword, previous position, current position, delta, ranking URL, and status
- grouped movement summary
- URL changes and live SERP observations
- source and snapshot links
- next-check recommendation

## Failure and missing-data behavior

Preserve partial batch results and identify missing chunks. If a previous
snapshot is incompatible, report the current run without fabricating deltas.
