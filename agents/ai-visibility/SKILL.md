---
name: AI Visibility
slug: ai-visibility
version: 2.0.0
category: seo
description: Measure brand visibility in AI-search results and test specific AI answers using Muapi evidence.
status: ready
muapi_capabilities:
  - seo.ai_mentions
  - seo.ai_response
  - seo.ai_mentions_metrics
  - seo.google_serp
required_connections:
  - muapi
permissions:
  - external-read-only
  - workspace-write
---

# AI Visibility

## Mission

Measure whether a brand or product is mentioned and cited in supported
AI-search surfaces, then explain the result with individual mentions and
carefully selected answer tests.

## Required inputs

- Target brand, product, or domain.
- Target country when relevant.
- Optional: two to five competitor brands or domains, platforms, date window,
  intent prompts, and a report period.

## Workflow

1. Read .seo/project.md for the canonical brand, aliases, products, and
   competitors. Ask for disambiguation when a brand name is generic.
2. Check seo.account_status when the user requests multiple platforms,
   competitors, or prompts.
3. Call seo.ai_mentions_metrics for aggregate target and competitor metrics
   over the same platform and date window. Keep platform sets and windows
   identical before comparing share of voice.
4. Call seo.ai_mentions for individual target mentions and citation pages.
   Use those records to explain which queries, pages, or sources contributed to
   the aggregate result.
5. Build a small, explicit prompt set from the user's buying questions or
   product categories. Ask before running multiple live answer tests.
6. Call seo.ai_response for selected prompts with a specified model,
   web_search setting, country, and valid token limit. Record the exact prompt
   and settings.
7. Optionally call seo.google_serp for the equivalent web queries to compare
   conventional search context with AI visibility. Do not treat the two
   surfaces as interchangeable metrics.
8. Classify findings as observed mention, observed citation, calculated share,
   answer-quality observation, or hypothesis. Recommend improvements only when
   the evidence supports a specific gap.

## Decision rules

- Mention count, citation count, sentiment, and share of voice are provider
  outputs only when returned by Muapi.
- Do not claim that an AI answer is representative from one prompt.
- Do not call an unmentioned brand invisible; state the query, platform, and
  window tested.
- Keep AI-answer text separate from provider aggregate metrics.
- Do not infer causal ranking factors from an AI citation.
- Treat a citation as an observed source relationship, not an endorsement.

## Output format

Return:

- scope, platforms, models, prompts, and dates
- aggregate visibility table
- representative mentions and citation pages
- answer-test table with prompt, model, web-search setting, and observed result
- calculated share-of-voice formulas
- prioritized opportunities and limitations
- source links

## Failure and missing-data behavior

If a platform or model is unavailable, report the exact unsupported dimension
and continue only with independent supported calls. Never fill a missing
mention or citation with a web-search assumption.
