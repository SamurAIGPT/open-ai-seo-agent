# AI SEO Agent

An AI agent for SEO and organic-growth work — rank/opportunity tracking, competitor SEO analysis, content gap discovery, local SEO, backlink intelligence, SEO/PR news monitoring, and app store optimization — backed by real search and analytics APIs.

Part of [Agency Agents OS](https://github.com/Anil-matcha/agency-agents-os), an open ecosystem of specialized AI agents for real business work.

## What this covers

This repo is the umbrella for anything an agency or in-house team would call "the AI SEO agent": finding ranking opportunities, watching what competitors are doing in search, spotting content gaps, tracking local/map rankings, auditing backlink profiles, monitoring SEO/PR news that affects strategy, and optimizing app store listings — without a human manually pulling reports from five different tools.

## Sub-agents

| Agent | Does | Status |
|---|---|---|
| [SEO Growth](agents/seo-growth/SKILL.md) | Finds ranking and traffic-growth opportunities from keyword and domain data | Blueprint |
| [Competitor SEO](agents/competitor-seo/SKILL.md) | Tracks a competitor's organic rankings, top pages, and backlink profile | Blueprint |
| [Content Gap](agents/content-gap/SKILL.md) | Identifies keywords a competitor ranks for that a site doesn't cover | Blueprint |
| [Local SEO](agents/local-seo/SKILL.md) | Tracks local/map-pack rankings and Google Business Profile health | Blueprint |
| [Backlink Intelligence](agents/backlink-intelligence/SKILL.md) | Audits a site's backlink profile and referring-domain quality | Blueprint |
| [News Monitoring](agents/news-monitoring/SKILL.md) | Monitors SEO/PR/search-engine news for changes that affect strategy | Coming Soon |
| [ASO](agents/aso/SKILL.md) | Optimizes app store listings for discoverability and conversion | Coming Soon |

## Required Muapi APIs

Live today:

- `seo.google_serp` — location/device-specific Google organic SERP snapshot for a keyword.
- `seo.keyword_research` — keyword overview: search volume, difficulty, and related-term suggestions.
- `seo.domain_overview` — domain organic visibility, ranked keywords, and top competitors.
- `seo.backlinks` — backlink profile: referring domains, link types, and anchor text.
- `seo.rank_track` / `seo.rank_track_batch` — organic ranking position for one or many keywords against a target domain, tracked over time.
- `seo.local_serp` — Google Maps / Local Finder rankings for a keyword and location.
- `seo.business_listings` / `seo.business_profile` / `seo.business_reviews` — local business listing, Google Business Profile, and review data.
- `seo.lighthouse_audit` — on-page performance, accessibility, SEO, and Core Web Vitals audit for a URL.

Not yet live (needed by News Monitoring and ASO):

- `seo.news_monitoring` — SEO/search-engine/PR news tracking.
- `aso.listing_optimization` — app store listing search-rank and conversion data.

## Setup

1. Create a Muapi account and API key at [muapi.ai](https://muapi.ai).
2. Review the [Muapi API quickstart](https://muapi.ai) and [OpenAPI schema](https://api.muapi.ai/openapi.json) — the live endpoints are `/api/v1/seo-google-serp`, `/seo-keyword-research`, `/seo-domain-overview`, `/seo-backlinks`, `/seo-lighthouse-audit`, `/seo-rank-track`, `/seo-rank-track-batch`, `/seo-local-serp`, `/seo-business-listings`, `/seo-business-profile`, and `/seo-business-reviews`.
3. Load the `SKILL.md` for the sub-agent you need into your agent runtime, or follow it manually.


## Using with an AI agent

Every sub-agent's `SKILL.md` is model- and runtime-agnostic — it's plain Markdown, so it works with any LLM agent, not just Claude. Two integration paths:

**As an MCP connection (the agent gets live Muapi tools):**

Muapi runs an MCP server at `https://api.muapi.ai/mcp` that any MCP-compatible client can connect to — Cursor, Windsurf, Claude, or your own custom agent.

- **Cursor / Windsurf / other clients with a header field:** connect to `https://api.muapi.ai/mcp` with an `Authorization: Bearer YOUR_MUAPI_KEY` header.
- **claude.ai / Claude Cowork / other connector UIs with no header field:** use the URL-embedded key form instead, `https://api.muapi.ai/mcp/YOUR_MUAPI_KEY`, via Settings → Connectors → Add custom connector.
- **Claude Code / Claude Desktop:** `claude mcp add muapi -e MUAPI_API_KEY=YOUR_MUAPI_KEY -- muapi mcp serve` (uses the muapi CLI's stdio transport — Claude Code's HTTP MCP client doesn't reliably inject tools).

Full setup details for every client: [muapi.ai/docs/mcp](https://muapi.ai/docs/mcp).

**As agent instructions (any LLM follows the workflow directly):**

Drop a sub-agent's `SKILL.md` into a Claude Code project's `.claude/skills/` directory, paste it into a custom-GPT/Project's system instructions, hand it to an autonomous agent framework as a tool spec, or attach it directly in a chat conversation — then ask the agent to follow it.

## Read-only vs. write actions

Every sub-agent here is `read-only` — they analyze and report, never publish or change live SEO settings.

## Status and limitations

Five of the seven sub-agents (SEO Growth, Competitor SEO, Content Gap, Local SEO, Backlink Intelligence) are **Blueprint**: they're built entirely on Muapi SEO endpoints that are live today, but haven't yet been verified end-to-end from inside this repo. News Monitoring and ASO are **Coming Soon** — they depend on capabilities (news tracking, app-store data) that Muapi doesn't expose yet.

## Contributing

See [Agency Agents OS CONTRIBUTING.md](https://github.com/Anil-matcha/agency-agents-os/blob/main/CONTRIBUTING.md).

## License

[MIT](LICENSE)
