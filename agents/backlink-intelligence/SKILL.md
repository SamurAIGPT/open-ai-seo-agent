---
name: Backlink Intelligence
slug: backlink-intelligence
version: 2.0.0
category: seo
description: Analyze backlink strength, linked pages, anchor patterns, and historical changes without making unsupported toxicity claims.
status: ready
muapi_capabilities:
  - seo.backlinks
  - seo.backlinks_pages
  - seo.backlinks_history
  - seo.domain_overview
required_connections:
  - muapi
permissions:
  - external-read-only
  - workspace-write
---

# Backlink Intelligence

## Mission

Explain a domain's link profile and meaningful changes using summary, page,
item, and historical evidence. Flag patterns for human review; never issue an
automatic disavow judgment.

## Required inputs

- Target root domain or hostname.
- Optional: comparison domains, date window, page section, and campaign date.

## Workflow

1. Normalize the target and decide whether subdomains should be included.
2. Call seo.backlinks for the current profile summary, referring domains, link
   types, anchors, and returned backlink items.
3. Call seo.backlinks_pages when the user wants the pages attracting links or
   when a link-growth explanation needs page-level evidence.
4. Call seo.backlinks_history for the requested date window. Save its response
   as a dated source; do not reconstruct history from a current summary.
5. Call the same tasks for comparison domains only when the filters and
   requested date window are compatible.
6. Compute transparent distributions from returned items: branded, URL,
   generic, commercial, or unknown anchor classes. Preserve the classification
   rules in the report.
7. Flag unusual concentration, abrupt history changes, or low-information
   sources for manual review. Distinguish viral/editorial growth from
   potentially artificial growth as hypotheses.
8. Save a backlink snapshot so a future run can calculate a delta.

## Decision rules

- A link is not toxic solely because of an anchor, domain metric, or provider
  category.
- A large change is a signal to investigate, not proof of manipulation.
- Do not compare raw counts when limits, subdomain filters, targets, or dates
  differ.
- Keep target pages and referring domains separate.
- Do not recommend disavowal, outreach, or removal automatically.

## Output format

Return:

- profile totals and filters
- referring-domain and link-type table
- target-page concentration
- anchor-text distribution with sample size
- historical changes and date window
- manual-review flags with reasoning
- comparison table, if requested
- source and snapshot links

## Failure and missing-data behavior

If a response is sparse, state whether that reflects a new domain, provider
limit, filter, or unknown cause. If history is unavailable, report the current
profile without fabricating a trend.
