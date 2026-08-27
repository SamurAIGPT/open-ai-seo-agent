# AI SEO Agent

Portable SEO skills for existing AI agents. The host agent supplies the reasoning,
planning, tool execution, and conversation; this repository supplies the SEO
workflows, Muapi tool map, decision rules, and report formats.

No custom agent runtime is required.

## What this enables

After the skills are installed and the host agent can reach Muapi, an existing
agent can perform:

- site and SEO project intake
- keyword discovery, metrics, clustering, and prioritization
- domain visibility and competitor analysis
- content-gap and relevant-page analysis
- ranking snapshots, comparisons, and trend reports
- backlink profile, page, and history analysis
- Lighthouse and Core Web Vitals reviews
- local search, listing, profile, review, Q&A, and update analysis
- AI-search visibility and answer testing
- YouTube search and video analysis

Every workflow is designed to produce an evidence-backed report rather than a
raw API dump or unsupported recommendation.

## How the package works

1. Install one or more skills from agents/ into the host agent's skill directory
   or load the skill file as task instructions.
2. Connect the host agent to Muapi through MCP or an equivalent API connector.
3. Give the agent a domain, business, keyword set, competitors, URL, or video.
4. The agent follows the selected workflow, calls only the required Muapi tools,
   and records the request parameters with the findings.
5. The agent writes a readable report and, when a comparison is requested, a
   dated raw snapshot in the user's workspace.

The external target is never edited by these skills. Local report and snapshot
files are allowed so a later run can compare results.

## Skills

| Skill | Purpose | Status |
|---|---|---|
| [SEO project setup](agents/seo-project-setup/SKILL.md) | Establish the domain, market, goals, competitors, and workspace context | Ready |
| [Keyword research](agents/keyword-research/SKILL.md) | Discover, validate, expand, cluster, and prioritize target terms | Ready |
| [Keyword clustering](agents/keyword-clustering/SKILL.md) | Group terms by intent and SERP evidence to prevent cannibalization | Ready |
| [SEO growth](agents/seo-growth/SKILL.md) | Find page-two wins and new growth opportunities | Ready |
| [Competitor SEO](agents/competitor-seo/SKILL.md) | Compare domains, rankings, SERPs, pages, and backlinks | Ready |
| [Content gap](agents/content-gap/SKILL.md) | Turn competitor and domain data into prioritized content briefs | Ready |
| [Rank tracking](agents/rank-tracking/SKILL.md) | Capture ranking snapshots and calculate changes between runs | Ready |
| [Technical SEO audit](agents/technical-seo-audit/SKILL.md) | Review Lighthouse scores, Core Web Vitals, and page-level risks | Ready |
| [Backlink intelligence](agents/backlink-intelligence/SKILL.md) | Analyze backlink sources, anchor patterns, pages, and history | Ready |
| [Local SEO](agents/local-seo/SKILL.md) | Analyze map results and business-profile health | Ready |
| [AI visibility](agents/ai-visibility/SKILL.md) | Measure brand mentions, citations, share of voice, and answer quality | Ready |
| [YouTube SEO](agents/youtube-seo/SKILL.md) | Research YouTube results and analyze videos, transcripts, and comments | Ready |

The skills are intentionally composable. For example, a content strategy run
can use project setup, keyword research, competitor SEO, content gap, and
technical audit in one host-agent session.

## Muapi connection

The host agent needs access to the Muapi MCP server or an equivalent connector.
Use the official Muapi connection instructions for the client being used:

- MCP endpoint: https://api.muapi.ai/mcp
- API reference: https://muapi.ai/docs/api-reference
- MCP setup: https://muapi.ai/docs/mcp

Never commit an API key. Prefer an environment variable or the host agent's
secret/connector storage. The skills use logical capability names such as
seo.google_serp; the endpoint catalog records the corresponding HTTP task name
and request fields.

For an HTTP-only connector, submit a POST request to the Muapi API task endpoint,
then poll the returned request ID until the result is ready. The connector
should preserve both the result and billing object in the report source record.

## Complete Muapi SEO coverage

The canonical mapping for all currently registered SEO tasks is in
[references/muapi-seo-tools.md](references/muapi-seo-tools.md). It covers:

- 11 core search, domain, backlink, audit, rank, and local tasks
- 7 keyword, page, backlink-history, and AI-visibility expansion tasks
- 4 local and account utility tasks
- 4 YouTube tasks
- 2 AI answer and mention tasks

The skills should consult the live Muapi schema when a field, limit, or enum is
not shown in the local reference. The live schema is authoritative.

Run the dependency-free package check with:

~~~sh
python3 scripts/validate_package.py
~~~

## Reports and snapshots

Use the conventions in
[references/reports-and-snapshots.md](references/reports-and-snapshots.md):

~~~text
.seo/
  project.md
  reports/YYYY-MM-DD/<run-slug>.md
  sources/YYYY-MM-DD/<run-slug>/<tool-name>.json
  snapshots/rankings/<market>/<YYYY-MM-DD>.json
  snapshots/backlinks/<YYYY-MM-DD>.json
  snapshots/ai-visibility/<YYYY-MM-DD>.json
~~~

Raw sources make every recommendation auditable. A later run must compare
snapshots only when the keyword, domain, location, language, device, depth, and
date window are compatible.

## Safety and quality rules

- Confirm the target domain, market, language, device, and comparison window
  before paid calls.
- Check seo-account-status when balance or provider availability is unknown.
- Ask before a large batch, deep SERP request, AI-response run, or repeated
  competitor scan.
- Do not claim a ranking, volume, sentiment, citation, or trend that is absent
  from a Muapi response.
- Distinguish observed data, calculated values, and hypotheses.
- Keep the exact request parameters and retrieval timestamp with every source.
- Treat a missing result as missing data, not as evidence of zero visibility.
- External operations are read-only. Report and snapshot writes require no
  external SEO permission.
- Stop and state the limitation when a requested capability is not exposed by
  Muapi; do not substitute guessed data.

## Limitations

Muapi currently supplies the SEO capabilities listed in the tool catalog. This
package does not claim native Google Search Console or Google Analytics support
unless a connected tool explicitly provides it. A Lighthouse result is a page
audit, not a complete site crawl.

## License

[MIT](LICENSE)
