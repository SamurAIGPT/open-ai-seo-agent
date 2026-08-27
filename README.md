# AI SEO Agent

> A free, open-source SEO alternative to Ahrefs and Semrush for the AI
> assistant you already use.

Give Claude, Claude Code, Codex, Cursor, Windsurf, Claude.ai, or another AI
assistant a complete SEO playbook. Add this repository to the assistant you
already use and ask it to research keywords, study competitors, find content
gaps, track rankings, audit pages, and build a practical SEO plan.

Connect an external SEO data source for market research, and connect Google
Search Console or Google Analytics directly for your own website data.

The repository is free to use and has no hosted subscription. Your external
data provider or Google account may still have its own pricing, quotas, and
limits.

## Why use it?

- Use the AI assistant you already know instead of learning another SEO
  dashboard.
- Start with a complete SEO plan or run one focused workflow at a time.
- Use your own Search Console and Analytics data alongside market research.
- Keep reports, decisions, and comparisons in your project folder.
- Read, adapt, and extend the workflows because the project is open source.

## What you can ask it to do

Use plain language. For example:

- “Create an SEO plan for my website and tell me what to fix first.”
- “Find keyword opportunities for my product in the United States.”
- “Show me which pages are close to page one.”
- “Compare my website with these competitors.”
- “Find content topics my competitors cover that I do not.”
- “Check my important pages for technical SEO problems.”
- “Use my Search Console and Analytics data to find pages that need attention.”
- “Check my local visibility, AI-search visibility, or YouTube opportunities.”

The assistant chooses the right workflow, uses the relevant data, and returns a
clear report with evidence, priorities, and next steps.

## Use it with your AI assistant

This repository works with the assistant you already use:

| Assistant | How to add the SEO playbook |
|---|---|
| Claude Code | Keep `AGENTS.md` in the project and add selected skill folders to `.claude/skills/`. |
| Codex | Keep `AGENTS.md` in the project and load the relevant `SKILL.md` with the task. |
| Cursor or Windsurf | Add `AGENTS.md` and the relevant skill as project instructions. |
| Claude.ai | Add the files to Project knowledge or the conversation, then connect the available data tools. |
| Other AI assistants | Load `AGENTS.md` and the relevant skill through the assistant's project-instruction or file-upload feature. |

See [installation for existing agents](references/agent-installation.md) for
setup patterns. Muapi's [Agent Skills documentation](https://muapi.ai/docs/agent-skills)
explains its compatible skill format.

## Quick start

1. Choose Claude, Claude Code, Codex, Cursor, Windsurf, Claude.ai, or another
   assistant that can read project files and use tools.
2. Add `AGENTS.md` and the skill you need from `agents/`.
3. Connect Muapi for external SEO research.
4. Connect your own Search Console and/or Analytics property when you want
   first-party performance and conversion data.
5. Ask for an SEO task using your website, market, language, competitors, and
   goals.

The assistant only reads external SEO data. Reports and comparison snapshots
are saved locally when you ask for them.

## SEO workflows

Start with **SEO Strategist** when you want an overall plan. For a focused task,
use the matching workflow directly.

| Workflow | What it helps with |
|---|---|
| [SEO Strategist](agents/seo-strategist/SKILL.md) | Build a complete SEO plan and prioritize the work |
| [SEO project setup](agents/seo-project-setup/SKILL.md) | Set up your website, goals, market, competitors, and workspace |
| [First-party performance](agents/first-party-performance/SKILL.md) | Understand your own Search Console and Analytics performance |
| [Keyword research](agents/keyword-research/SKILL.md) | Find and prioritize keywords for your products, services, or content |
| [Keyword clustering](agents/keyword-clustering/SKILL.md) | Group keywords and map them to the right pages |
| [SEO growth](agents/seo-growth/SKILL.md) | Find quick wins and new organic growth opportunities |
| [Competitor SEO](agents/competitor-seo/SKILL.md) | See where competitors are stronger and how to respond |
| [Content gap](agents/content-gap/SKILL.md) | Find useful topics and pages your website is missing |
| [Rank tracking](agents/rank-tracking/SKILL.md) | Track rankings and see what changed over time |
| [Technical SEO audit](agents/technical-seo-audit/SKILL.md) | Check page speed, Core Web Vitals, and page-level issues |
| [Backlink intelligence](agents/backlink-intelligence/SKILL.md) | Understand links pointing to your website or competitors |
| [Local SEO](agents/local-seo/SKILL.md) | Improve local search, Maps, listings, reviews, and profiles |
| [AI visibility](agents/ai-visibility/SKILL.md) | Check how your brand appears in AI-search answers |
| [YouTube SEO](agents/youtube-seo/SKILL.md) | Research YouTube topics, videos, transcripts, and comments |

Workflows can be used separately or combined. For example, a content strategy
can combine project setup, keyword research, competitor SEO, content gaps, and
technical review.

## Connect external SEO data

The workflows use Muapi for research about search markets, competitors,
rankings, backlinks, local results, AI-search visibility, and YouTube. The
repository tells the assistant which research to use and how to turn it into
useful advice.

Choose the connection that matches your assistant:

| Assistant or setup | Muapi connection |
|---|---|
| Claude Code or Claude Desktop | Use Muapi's local connection with `muapi mcp serve`. |
| Cursor, Windsurf, or another hosted MCP assistant | Use `https://api.muapi.ai/mcp`. |
| Codex, Claude.ai, or a REST-only setup | Add Muapi through the assistant's supported MCP or REST connection method. |

Follow the official [Muapi MCP instructions](https://muapi.ai/docs/mcp) or
[API reference](https://muapi.ai/docs/api-reference) for the connection method
you use. Keep the API key in the assistant's secure settings or an environment
variable. Never paste it into a prompt, report, or committed file.

## Connect your own Google data (optional)

Search Console and Google Analytics 4 show what is happening on your own
website. They connect directly to the assistant as separate first-party data
sources.
Use [First-party Performance](agents/first-party-performance/SKILL.md) when you
want to use this data.

- Search Console supplies the user's queries, pages, clicks, impressions, CTR,
  average position, and optional URL inspection data.
- Analytics supplies the user's organic landing-page, acquisition, engagement,
  ecommerce, site-search, audience, and configured key-event data.

To connect them:

1. Follow [Google first-party connector setup](references/google-setup.md).
2. Let the user authorize read-only access and choose the correct Search
   Console and/or Analytics property.
3. Load the First-party Performance workflow for questions about your own
   search traffic, pages, engagement, or conversions.

Use Google for your own performance and the external SEO connection for
competitors, market metrics, live search results, backlinks, local results, AI
visibility, and YouTube data. Google permissions and quotas still apply. See
[references/google-first-party-data.md](references/google-first-party-data.md)
for the data rules and reconciliation guidance.

## Costs

The repository itself is free and open source. External SEO research follows
the pricing and limits of the data connection you configure. Google data uses
Google's own permissions and quotas. Check the provider documentation before
running large or repeated research jobs.

## External SEO coverage

The external SEO connection currently supports:

- keyword ideas, search volume, intent, and keyword expansion
- live search results and ranking checks
- domain visibility, competitor research, and content gaps
- backlinks and backlink history
- Lighthouse page reviews and Core Web Vitals
- local search, business listings, profiles, reviews, Q&A, and updates
- AI-search mentions and answer testing
- YouTube search, video details, subtitles, and comments

See the complete [external SEO task list](references/muapi-seo-tools.md) for
the available research actions. If a field or option changes, the live data
source schema is the final source of truth.

Run the dependency-free package check with:

~~~sh
python3 scripts/validate_package.py
~~~

## Reports and saved work

When you ask the assistant to save its work, it can keep the project context,
reports, supporting data, and comparison snapshots in a `.seo/` folder. A
typical project looks like this:

~~~text
.seo/
  project.md
  reports/YYYY-MM-DD/<run-slug>.md
  sources/YYYY-MM-DD/<run-slug>/<tool-name>.json
  snapshots/rankings/<market>/<YYYY-MM-DD>.json
  snapshots/backlinks/<YYYY-MM-DD>.json
  snapshots/ai-visibility/<YYYY-MM-DD>.json
~~~

This makes later conversations more useful and lets the assistant compare
changes over time. See [reports and snapshots](references/reports-and-snapshots.md)
for the format. Google credentials and API keys are never saved there.

## Quality and privacy

- Confirm the website, market, language, device, and date range before paid
  research.
- Ask before large keyword lists, deep search-result checks, AI-answer runs, or
  repeated competitor scans.
- Report only what the connected data actually shows. Never invent rankings,
  traffic, volume, sentiment, citations, reviews, or trends.
- Clearly separate observed facts, calculations, and recommendations.
- Treat missing data as unknown—not as zero.
- External websites and properties are read-only. Only local reports and
  snapshots may be written.
- Keep API keys, OAuth credentials, and access tokens out of prompts, reports,
  source files, and the repository.
- If a requested data source is unavailable, say so clearly instead of guessing.

## Limitations

Your assistant must be able to read the files and connect to the data sources.
Search Console and Analytics are optional and require the user's authorization.
External SEO capabilities depend on the configured data connection and its
current task catalog. A Lighthouse result reviews selected pages; it is not a
complete site crawl.

## Contributing

Improvements are welcome. Keep new workflows focused, evidence-based, and
usable by more than one AI assistant. Before opening a change, run:

~~~sh
python3 scripts/validate_package.py
~~~

## License

[MIT](LICENSE)
