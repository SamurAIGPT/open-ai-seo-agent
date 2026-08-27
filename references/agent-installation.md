# Installation for existing agents

This repository is an SEO Agent Skill Pack: portable Markdown workflows that
an existing agent loads into its own planning and tool loop. It is not an agent
runtime or an MCP server.

## 1. Connect Muapi

Choose the transport supported by the host agent. Muapi's official
[MCP documentation](https://muapi.ai/docs/mcp) is authoritative for client
configuration.

For Claude Code or Claude Desktop, use Muapi's local stdio bridge:

~~~sh
claude mcp add muapi -e MUAPI_API_KEY=YOUR_MUAPI_API_KEY -- muapi mcp serve
~~~

For Cursor, Windsurf, or another hosted MCP client, configure:

- server URL: https://api.muapi.ai/mcp
- credential: a Muapi API key stored in the client's secret or environment
  store

For a REST-only host, use the submit-then-poll flow in the
[Muapi API reference](https://muapi.ai/docs/api-reference). For Codex,
Claude.ai, or another agent host, load this pack through that host's supported
project, skill, or custom-instruction mechanism and register Muapi through its
supported MCP or REST transport.

For HTTP clients, use secure header configuration when available. Do not put a
key in a checked-in file, prompt, report, source record, or shell history.

Verify the connection with seo.account_status before running a paid workflow.
Muapi also documents public Agent Skill recipe discovery at
https://api.muapi.ai/api/v1/agent-skills; use it only when the host supports
that discovery flow. The local `agents/` directory is the source of truth for
this pack.

## 2. Connect first-party Google data (optional)

Search Console and Google Analytics 4 should be connected directly through the
host agent's Google OAuth or native connector. They are user-specific sources,
not Muapi tasks.

Follow [Google first-party connector setup](google-setup.md) for the Google
Cloud APIs, OAuth scopes, property selection, capability mapping, and
verification checklist. This repository does not implement the OAuth callback
or token store.

1. Let the user authorize read-only access.
2. Let the user select the verified Search Console property and accessible GA4
   property.
3. Load agents/first-party-performance/SKILL.md for first-party questions.
4. Keep property, date range, timezone, dimensions, filters, and connector
   errors in the source record.
5. Never put OAuth credentials or tokens in .seo/ or the repository.

Use Search Console for the user's search queries, pages, clicks, impressions,
CTR, and average position. Use GA4 for the user's organic acquisition,
landing-page, engagement, and configured key-event data. Use Muapi for
third-party and market data.

## 3. Install skills

For a host with directory-based skill discovery, copy the required skill
directory so that SKILL.md remains at the skill root:

~~~text
<project>/.claude/skills/keyword-research/SKILL.md
<project>/.claude/skills/competitor-seo/SKILL.md
~~~

The same files can be loaded from agents/ by hosts that accept explicit
instruction files. Do not combine unrelated skills into one prompt if the host
supports selective loading.

For a broad request, load `agents/seo-strategist/SKILL.md` first. For a narrow
request, load only the matching skill. The host agent remains responsible for
reasoning, approvals, tool calls, and report persistence.

Typical loading patterns are:

| Host | Load this pack |
|---|---|
| Claude Code | Keep `AGENTS.md` in the project and copy selected `agents/<skill>/` directories into `.claude/skills/`. |
| Codex | Keep `AGENTS.md` at the project root and load the relevant `SKILL.md` as project context or task instructions. |
| Claude.ai | Attach or add `AGENTS.md`, the selected `SKILL.md`, and only the needed reference files to the project or conversation context. |
| Other Markdown-capable or MCP hosts | Load `AGENTS.md` plus the selected skill through the host's project-instruction mechanism, then register Muapi using its supported MCP/REST transport. |

Loading the Markdown does not create a Google connection. The host must expose
the direct Google OAuth/native connector and the Muapi connector separately.

## 4. Give the host agent a useful request

Include the target and measurement context:

~~~text
Analyze example.com for organic growth opportunities.
Market: United States
Language: English
Device: desktop
Priority: commercial pages and page-two keywords
Save the report and Muapi source records under .seo/.
~~~

For competitor, local, AI-visibility, and YouTube work, also provide the
competitor set, business location, target brand, platforms, or video IDs.

## 5. Connector contract

The Muapi connector should:

- expose all task names in references/muapi-seo-tools.md
- validate required fields against the live schema
- preserve request IDs and billing
- poll asynchronous tasks until completion
- return structured JSON instead of only a rendered URL
- surface provider errors without rewriting them as successful results

If the host already exposes Muapi tools, no adapter code belongs in this
repository. If it only supports HTTP, its connector must implement the POST
and result-polling flow described in muapi-seo-tools.md.

For direct Google connectors, additionally:

- expose property selection instead of accepting an unverified domain as
  authorization
- use read-only OAuth scopes
- return structured rows with metric definitions and metadata
- preserve the selected property, date range, timezone, dimensions, and
  filters
- keep Search Console and GA4 metrics in separate source records
- surface permission and quota errors without converting them to zero values

## 6. Host-agent behavior

Before calling tools, the host agent should:

1. identify the applicable skill
2. collect missing required inputs
3. state the planned calls and any expensive batch
4. check existing .seo/project.md and compatible sources
5. ask for approval when the run is broad or cost is uncertain

After calling tools, it should:

1. save source records
2. separate observations from calculations and hypotheses
3. produce the skill's output format
4. save the report only if requested or if the host convention permits it
5. state limitations and failed calls
