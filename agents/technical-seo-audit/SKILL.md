---
name: Technical SEO Audit
slug: technical-seo-audit
version: 2.0.0
category: seo
description: Audit selected pages with Muapi Lighthouse data and turn observed issues into prioritized technical SEO actions.
status: ready
muapi_capabilities:
  - seo.lighthouse_audit
  - seo.relevant_pages
  - seo.account_status
required_connections:
  - muapi
permissions:
  - external-read-only
  - workspace-write
---

# Technical SEO Audit

## Mission

Produce a page-level technical SEO review from Lighthouse results. Make the
scope explicit: this skill audits supplied or selected pages; it does not claim
to crawl every URL on a site.

## Required inputs

- One or more complete page URLs, or a target domain.
- Device mode, if different from desktop.
- Optional: page types, business priority, and maximum page count.

## Workflow

1. Read .seo/project.md and confirm the canonical domain and device.
2. If URLs were not supplied, call seo.relevant_pages for the target and choose
   a representative set across the returned page types. Explain the selection.
3. Check seo.account_status when the page count or provider balance is unknown.
4. Ask before auditing a broad page set. Start with the homepage, one important
   commercial page, one content page, and one conversion page when available.
5. Call seo.lighthouse_audit for each selected URL. Use the same device for
   comparable results and save every source record.
6. Extract category scores, Core Web Vitals, and provider-reported issues.
   Preserve the provider's status, value, and unit. Do not infer crawl,
   indexing, canonical, schema, redirect, robots, or XML-sitemap behavior from
   a Lighthouse score.
7. Prioritize issues by observed severity, affected business page, repeated
   occurrence, and likely user impact. Label any prioritization formula as
   calculated.
8. Return one concrete remediation per finding and identify the evidence that
   should be rechecked after a fix.

## Decision rules

- A low Lighthouse score is a diagnostic signal, not a complete SEO diagnosis.
- Do not claim site-wide health from one page.
- Keep mobile and desktop results separate.
- Do not compare runs when URL, device, or provider result completeness differs.
- Prefer a small representative audit to an unapproved large batch.

## Output format

Return:

- scope and page-selection rationale
- score and Core Web Vitals table per URL
- observed issues grouped by category
- priority, owner, remediation, and verification check
- limitations and unaudited areas
- source links

## Failure and missing-data behavior

If a URL fails, preserve the failure and continue with independent URLs. If
Lighthouse returns no issue detail, report the available scores only and do not
invent fixes.
