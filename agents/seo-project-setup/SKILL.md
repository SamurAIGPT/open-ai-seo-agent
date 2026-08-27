---
name: SEO Project Setup
slug: seo-project-setup
version: 2.0.0
category: seo
description: Establish a reusable SEO project context so later research uses consistent targets, markets, competitors, and workspace artifacts.
status: ready
muapi_capabilities:
  - seo.account_status
  - seo.domain_overview
  - seo.relevant_pages
  - seo.keyword_research
required_connections:
  - muapi
permissions:
  - external-read-only
  - workspace-write
---

# SEO Project Setup

## Mission

Turn an unstructured SEO request into a small, explicit project brief that
other skills can reuse. Establish the canonical domain, market, audience,
business priorities, competitors, and reporting location before drawing
conclusions from search data.

## Use this skill when

- A domain is being analyzed for the first time.
- A team wants repeatable SEO reports rather than one-off answers.
- The user needs to establish competitors, locations, or priority products.
- Existing .seo/project.md is missing, stale, or contradictory.

## Required inputs

- Canonical domain or site URL.
- At least one business goal or SEO question.
- Target country and language, or permission to use Muapi defaults.

Collect these when relevant:

- product, service, or audience priorities
- physical locations or service areas
- two to five known competitors
- target devices
- seed topics or an existing keyword list
- preferred report cadence

## Workflow

1. Normalize the domain to a hostname. Preserve important subdomains and URL
   prefixes separately; do not silently analyze a different property.
2. Read .seo/project.md and prior .seo/reports/ if they exist. Ask about
   conflicting domain, market, or competitor values.
3. Check seo.account_status when provider availability, balance, or limits are
   unknown. Do not force a live check unless the user asks or the cached status
   is insufficient.
4. Call seo.domain_overview for the canonical domain using the confirmed
   location and language. Use the result to record observed competitors and
   ranked-keyword context, not to decide business relevance automatically.
5. Call seo.relevant_pages when page-level context is needed. Limit the result
   to the number of pages needed for the requested workflow.
6. If the user supplied a topic but no keyword list, call
   seo.keyword_research once per distinct seed topic, with a modest limit.
7. Present the proposed project context and ask the user to correct it before
   broad or repeated research.
8. Write .seo/project.md only after the context is confirmed. Record the
   retrieval date and links to the source records used to establish it.

## Decision rules

- A provider-listed competitor is a research lead, not a confirmed business
  competitor. Confirm relevance with the user.
- Keep domain, subdomain, brand, and product targets distinct.
- Use the same country, language, device, and date conventions in later runs.
- Never make a performance claim from setup data alone.
- Do not create a recurring schedule inside this skill. Record a suggested
  cadence for the host agent or an external scheduler.

## Output format

Return:

1. Confirmed project context.
2. Missing decisions, if any.
3. Initial observed domain facts with source links.
4. Proposed .seo/project.md contents.
5. Recommended next skill and the smallest useful Muapi run.

## Failure and missing-data behavior

If Muapi returns no domain data, keep the project file with an explicit
unknown-data note and offer keyword research for a supplied topic. Do not
replace missing provider data with estimates.
