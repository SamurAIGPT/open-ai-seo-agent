# AI SEO Agent

An AI agent for SEO and organic-growth work — rank/opportunity tracking, competitor SEO analysis, content gap discovery, SEO/PR news monitoring, and app store optimization — backed by real search and analytics APIs.

Part of [Agency Agents OS](https://github.com/Anil-matcha/agency-agents-os), an open ecosystem of specialized AI agents for real business work.

## What this covers

This repo is the umbrella for anything an agency or in-house team would call "the AI SEO agent": finding ranking opportunities, watching what competitors are doing in search, spotting content gaps, monitoring SEO/PR news that affects strategy, and optimizing app store listings — without a human manually pulling reports from five different tools.

## Sub-agents

| Agent | Does | Status |
|---|---|---|
| [SEO Growth](agents/seo-growth/SKILL.md) | Finds ranking and traffic-growth opportunities from search performance data | Coming Soon |
| [Competitor SEO](agents/competitor-seo/SKILL.md) | Tracks competitor rankings, content, and backlink moves over time | Coming Soon |
| [Content Gap](agents/content-gap/SKILL.md) | Identifies keywords and topics competitors rank for that a site doesn't cover | Coming Soon |
| [News Monitoring](agents/news-monitoring/SKILL.md) | Monitors SEO/PR/search-engine news for changes that affect strategy | Coming Soon |
| [ASO](agents/aso/SKILL.md) | Optimizes app store listings for discoverability and conversion | Coming Soon |

## Required Muapi APIs

- `seo.search_performance` — search-console-style clicks, impressions, CTR, and average position by query/page.
- `seo.keyword_research` — keyword search volume, difficulty, and related-term expansion.
- `seo.serp_analysis` — search engine results page composition, ranking positions, and SERP feature presence for a query.
- `seo.backlink_analysis` — referring domains, link velocity, and anchor text for a site or URL.
- `analytics.ga4_report` — GA4-style traffic, conversion, and engagement metrics by page/channel.

These are planned capability names, not live yet — see the Status section below.

## Setup

1. Create a Muapi account and API key at [muapi.ai](https://muapi.ai).
2. Review the [Muapi API quickstart](https://muapi.ai) and [OpenAPI schema](https://api.muapi.ai/openapi.json).
3. Load the `SKILL.md` for the sub-agent you need into your agent runtime, or follow it manually.

## Read-only vs. write actions

All sub-agents here are `read-only` / `draft-only` — they analyze and report, never publish or change live SEO settings.

## Status and limitations

**All sub-agents in this repo are Coming Soon.** They depend on non-media API surfaces (search performance, keyword research, SERP data, backlink data) that are not yet live on Muapi. The workflows and instructions are fully drafted so they're ready to test the moment those APIs ship.

## Contributing

See [Agency Agents OS CONTRIBUTING.md](https://github.com/Anil-matcha/agency-agents-os/blob/main/CONTRIBUTING.md).

## License

[MIT](LICENSE)
