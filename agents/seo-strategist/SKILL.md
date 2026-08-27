---
name: SEO Strategist
slug: seo-strategist
version: 1.0.0
category: seo
description: Route broad SEO questions into the right Muapi-backed skills, coordinate their dependencies, and return one prioritized strategy report.
status: ready
muapi_capabilities:
  - seo.google_serp
  - seo.keyword_research
  - seo.domain_overview
  - seo.backlinks
  - seo.lighthouse_audit
  - seo.rank_track
  - seo.rank_track_batch
  - seo.local_serp
  - seo.business_listings
  - seo.business_profile
  - seo.business_reviews
  - seo.ai_mentions
  - seo.ai_response
  - seo.keywords_search_volume
  - seo.keywords_for_keywords
  - seo.related_keywords
  - seo.keyword_overview
  - seo.relevant_pages
  - seo.backlinks_pages
  - seo.backlinks_history
  - seo.ai_mentions_metrics
  - seo.google_qa
  - seo.business_updates
  - seo.account_status
  - seo.youtube_organic
  - seo.youtube_video_info
  - seo.youtube_video_subtitles
  - seo.youtube_video_comments
required_connections:
  - muapi
optional_connections:
  - google_search_console
  - google_analytics_4
first_party_capabilities:
  - gsc.list_sites
  - gsc.search_analytics
  - gsc.inspect_urls
  - ga4.list_properties
  - ga4.organic_landing_pages
  - ga4.page_performance
  - ga4.key_events
  - ga4.organic_overview
  - ga4.traffic_acquisition
  - ga4.ecommerce_performance
  - ga4.site_search
  - ga4.audience_breakdown
  - ga4.measurement_health
permissions:
  - external-read-only
  - workspace-write
---

# SEO Strategist

## Mission

Act as the routing and synthesis layer for the other SEO skills. The host agent
provides the reasoning and tool loop; this skill decides which capabilities are
needed, sequences dependencies, avoids duplicate calls, and combines the
findings into one decision-ready report.

Use this skill for broad requests such as:

- "Give me an SEO plan for this site."
- "Audit our SEO and tell me what to fix first."
- "Why are competitors beating us?"
- "What should our team work on this month?"
- "Build a baseline for this domain."

For a narrow request, load the smallest matching skill directly.

## Required inputs

- Canonical domain or URL.
- The business question or outcome.
- Country and language.

Collect when relevant:

- device
- target locations and service areas
- products, services, audiences, and conversion goals
- competitor domains
- existing keyword list
- important URLs or page sections
- comparison date or reporting period
- maximum scope and cost preference

## Phase 1: establish scope

1. Read .seo/project.md, recent reports, source records, and compatible
   snapshots before planning new calls.
2. Normalize the target domain and keep subdomains, URL sections, brands, and
   products distinct.
3. Classify the request into one or more workstreams using the routing table
   below.
4. Identify missing required inputs. Ask only for decisions that affect the
   selected calls.
5. If the question concerns the user's own search performance, landing pages,
   or conversions, detect whether a direct Search Console or Analytics
   connection is available. Keep that workstream separate from Muapi.
6. State the proposed workstreams, calls, page/keyword limits, expected
   artifacts, and any expensive batch before execution.
7. Check seo.account_status when balance, provider availability, or limits are
   unknown. Do not force a live check when an adequate recent status exists.

## Routing table

| User intent | Skill | Primary evidence |
|---|---|---|
| Establish a new baseline or project | seo-project-setup | domain overview, relevant pages, account status |
| Review the user's own search performance or conversions | first-party-performance | direct Search Console and/or Analytics data |
| Find quick wins or growth opportunities | seo-growth | domain overview, rank batch, keyword metrics, SERP |
| Discover or validate keywords | keyword-research | keyword discovery, volume, metrics, SERP |
| Prevent cannibalization or map terms to pages | keyword-clustering | keyword metrics, SERP overlap, relevant pages |
| Compare competitors | competitor-seo | domain, rank, SERP, page, backlink data |
| Find missing content | content-gap | domain diffs, keyword metrics, SERP, page evidence |
| Review current or changing rankings | rank-tracking | rank snapshots, compatible prior snapshots, SERP |
| Check page performance and technical issues | technical-seo-audit | relevant pages and Lighthouse |
| Understand link strength or changes | backlink-intelligence | backlink summary, linked pages, history |
| Improve Maps or business-profile visibility | local-seo | local SERP, listings, profile, reviews, Q&A, updates |
| Measure AI-search presence | ai-visibility | mentions, metrics, answer tests, optional SERP |
| Research video opportunities | youtube-seo | YouTube results, video info, transcripts, comments |

## Phase 2: compose workstreams

Choose only the workstreams that answer the user's question. These common
recipes are starting points, not mandatory checklists.

### Baseline

1. seo-project-setup
2. first-party-performance when direct Google data is connected and the user
   wants owned performance context
3. seo-growth and keyword-research
4. competitor-seo and content-gap
5. technical-seo-audit for a small representative page set
6. local-seo, ai-visibility, or youtube-seo when the business model requires it

### Organic growth plan

1. seo-project-setup if project context is missing
2. seo-growth
3. keyword-clustering for competing page targets
4. content-gap for net-new opportunities
5. technical-seo-audit for pages attached to the highest-priority opportunities

### Competitor response

1. competitor-seo
2. content-gap
3. backlink-intelligence when link evidence is relevant
4. keyword-clustering and seo-growth to convert observations into owned actions

### Monthly performance review

1. first-party-performance when owned clicks, impressions, landing pages, or
   conversions are in scope
2. rank-tracking using the same snapshot dimensions
3. seo-growth for movement and page-two opportunities
4. backlink-intelligence when backlink history is in scope
5. local-seo or ai-visibility when those channels are tracked

### Local business review

1. local-seo
2. technical-seo-audit for important location or service pages
3. keyword-research for local service terms when the target list is incomplete

## Phase 3: execute and synthesize

1. Reuse compatible source records from the current run. Do not repeat the same
   Muapi call merely because two skills mention it.
2. Run independent calls in parallel when the host agent supports it. Respect
   dependencies: establish targets before comparison, discover terms before
   clustering, and retrieve page context before page recommendations.
3. Keep every request's domain, keyword, location, language, device, depth,
   limit, date window, request ID, retrieval time, and billing metadata.
4. Split rank batches at 50 keywords or the live schema's lower limit. Ask
   before broad multi-domain, deep SERP, multi-prompt AI, or large page runs.
5. Save source records and dated snapshots according to
   references/reports-and-snapshots.md when the user requests a report,
   history, or repeatable baseline.
6. Merge findings by evidence, not by wording. A single observation may support
   several workstreams but should appear once in the final finding list.
7. Mark each conclusion as observed, calculated, or hypothesized. Preserve
   empty, partial, incompatible, and failed results.
8. Rank actions by business priority, evidence strength, expected impact, and
   effort. State the formula or reasoning; this is not a Muapi metric.

## Unified output format

Return one report with:

1. Scope and objective.
2. Data coverage: workstreams, calls, dates, filters, and limitations.
3. Executive answer: the most important findings.
4. Findings table with evidence, confidence, and affected URL/keyword.
5. Prioritized action plan with owner, action, rationale, and verification
   method.
6. Workstream details for first-party performance, keyword, competitor,
   content, technical, backlink, local, AI, or YouTube findings that were
   requested.
7. Calculations and comparison dimensions.
8. Failed or missing data.
9. Source and snapshot links.
10. Recommended next check and what should remain unchanged for a valid
    comparison.

Do not return a raw collection of sub-reports without a cross-workstream
summary. Do not hide a limitation simply because another workstream succeeded.

## Boundaries

- External SEO properties are read-only. Local report and snapshot writes are
  allowed under the host project convention.
- Search Console and Analytics are direct, user-authorized sources. Do not
  route them through Muapi or replace them with third-party estimates when they
  are available.
- Do not invent Google Search Console, Google Analytics, crawl, traffic,
  citation, ranking, volume, sentiment, or trend data that a connected source
  did not return.
- A Lighthouse result is page-level evidence, not a complete crawl.
- Rank snapshots do not create a scheduler. Recurring execution belongs to the
  host agent or an external scheduled workflow.
- If a requested data source is not exposed by Muapi or an explicitly
  connected tool, state the limitation and continue only with valid independent
  workstreams. For first-party Google data, ask the host to obtain user
  authorization rather than estimating it from Muapi.
- Never publish, edit, disavow, respond to, or otherwise change an external
  property.

## Failure behavior

If a dependency fails, return the completed independent workstreams, identify
the blocked conclusions, and give the smallest retry needed. If the target
domain or market is ambiguous, stop before paid calls and ask the user to
choose.
