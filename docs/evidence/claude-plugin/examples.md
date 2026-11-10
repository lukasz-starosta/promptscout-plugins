# Claude plugin: real runs of "How visible is my brand in AI answers?"

These runs used the real production model in native Claude cloud on 2026-11-09. Nothing is mocked.

- Claude Code 2.1.319, model `claude-opus-5-5`, headless session, empty working folder.
- **Without plugin:** a Claude Code config with no PromptScout marketplace and no plugin.
- **With plugin:** the same kind of config after `claude plugin marketplace add ./` and
  `claude plugin install promptscout@promptscout` from this branch. The `promptscout` server
  reports `needs-auth`, because nobody signed in to PromptScout. The task forbids that sign-in
  (see "Not yet covered").
- **Cost per run for PromptScout:** none. The plugin calls no model of its own. Claude's usage
  counts against the user's own Claude account, and the PromptScout MCP server does the data
  work.

## Example 1: not signed in to PromptScout

Command, run once per config:

```bash
claude -p "How visible is my brand in AI answers?" --output-format stream-json --verbose --max-turns 6 \
  --disallowedTools "Bash,ListConnectors,ListPlugins,ToolSearch,Read,Glob,Grep"   # without plugin
claude -p "How visible is my brand in AI answers?" --output-format stream-json --verbose --max-turns 4   # with plugin
```

On its first attempt, the no-plugin run ran out of turns while it inspected the session and
listed this account's connectors. That output is not reproduced here. It was rerun without
those account-inspection tools.

### Without the plugin (4 turns)

- **Date:** 2026-11-09, 12:11 UTC
- **Model:** `claude-opus-5-5` in Claude Code 2.1.319, headless, no PromptScout plugin installed
- **Exact question:** `How visible is my brand in AI answers?`
- **Source:** Claude's own tool calls in this run. It searched Anthropic's plugin directory
  (`SearchPlugins`) and the MCP registry (`SearchMcpRegistry`), then showed an install card
  (`SuggestPluginInstall`) for three third-party AI-visibility plugins. This records what Claude
  showed on that date. It is not PromptScout's claim about those products.

Claude then answered:

> I can't measure that yet. Nothing in this session can query ChatGPT, Perplexity, Gemini or Google AI Overviews and log which brands they mention. Each of the plugins above can, and if you install one I'll run a proper audit with it.
>
> If you'd like something sooner, I can do a rough check now:
>
> 1. **Tell me your brand and website.** Is it PromptScout (promptscout.app), or a different brand?
> 2. **Name 2–4 competitors** and the kinds of questions buyers ask, like "best tool for X." If you don't list any, I'll pick some.
> 3. **I'll run a quick check:**
>    - **What I know about you:** what I say about your brand when asked directly, and whether I mention you in answers to category questions without being prompted.
>    - **What the web says:** a web search for the sources AI tools tend to cite in your category, such as listicles, review sites and Reddit, to see whether you appear there.
>    - **Your site:** a look at whether AI crawlers can read it easily (robots.txt, llms.txt, structured data).
>
> This check gives you directional findings and a list of gaps, not scores. For share-of-voice numbers across several AI engines, use one of the plugins.

### With the plugin, before sign-in (1 turn, no tool calls)

2026-11-09, 12:11 UTC · `claude-opus-5-5` in Claude Code 2.1.319 · exact question:
`How visible is my brand in AI answers?`

> I can't check that yet. Your brand's AI visibility data comes from PromptScout, and its connection isn't authorized in this session, so I have no access to your mention rates, share of voice or cited sources.
>
> I can't sign in to it from here, so you'll need to authorize the PromptScout plugin outside this session. Once that's done, ask again and I'll pull:
>
> - **Visibility:** how often ChatGPT, Perplexity, Gemini and Claude mention your brand for the prompts you track.
> - **Share of voice:** how you compare with your competitors.
> - **Sources:** which pages and threads AI answers cite when they talk about your category.
>
> After that, I can also go through your PromptScout Opportunities (suggested actions to raise your visibility) or draft content briefs for pages that AI assistants are more likely to cite.

### What this shows

- Without the plugin, Claude has no data and points the user to competing AI-visibility plugins.
- With the plugin installed but not signed in, Claude routes the question to PromptScout and
  says what it will return. It does not invent numbers, and it does not suggest other vendors.
- **Gap:** this run did not load the `checking-ai-visibility` skill (no Skill call), so the
  answer omits the skill's exact sign-in path. Example 2 fixes this with a change to the skill's
  description.

## Example 2: skill description, before and after (signed out)

**Question:** does the `checking-ai-visibility` skill load for "How visible is my brand in AI
answers?" when PromptScout is not signed in?

**Method:** 3 runs per version. Each run uses the with-plugin config above (plugin loaded in
place from the checkout, server `needs-auth`), Claude Code 2.1.319, `claude-opus-5-5`:

```bash
claude -p "How visible is my brand in AI answers?" --output-format stream-json --verbose --max-turns 4
```

A run counts as loaded when the stream has a `Skill` tool call for
`promptscout:checking-ai-visibility`.

| Description | Skill loaded | Answer gives the exact Claude Code sign-in path |
| :- | :- | :- |
| Before (commit c073715) | 0 of 3 (no tool calls, 1 turn) | 1 of 3. The others say "authorize the PromptScout plugin outside this session" or "open your claude.ai connector settings" |
| After (this commit) | 3 of 3 (`Skill` → `promptscout:checking-ai-visibility`, 3 turns) | 3 of 3 (`/mcp` → `plugin:promptscout:promptscout`, plus the claude.ai Connectors tab) |

**Before:**

```yaml
description: Check how visible a brand is in AI answers with PromptScout. Use when the user asks how often AI assistants such as ChatGPT, Perplexity, Gemini or Claude mention their brand, how they compare with competitors, what their share of voice is, or which sources and threads AI answers cite.
```

**After:**

```yaml
description: Check how visible a brand is in AI answers with PromptScout. Use for questions like "How visible is my brand in AI answers?", how often ChatGPT, Perplexity, Gemini or Claude mention the user's brand, how it compares with competitors, its share of voice, or which sources and threads AI answers cite. Load it before answering even when the PromptScout server is not connected or needs sign-in, because it gives the exact sign-in steps.
```

### Before (run 2 of 3; in a Claude Code session, it points to the wrong place)

2026-11-09, 13:08 UTC · `claude-opus-5-5` in Claude Code 2.1.319 · exact question:
`How visible is my brand in AI answers?`

> I can't check that yet. Your brand's AI visibility data comes from PromptScout, and its connection in this session isn't authorized, so I can't read your mention rates, share of voice or cited sources.
>
> To fix it, open your claude.ai connector settings and authorize the **PromptScout** connector (I can't start the sign-in from here). Then ask again and I'll pull:
>
> - **Mention rate:** how often ChatGPT, Perplexity, Gemini and Claude mention your brand for the prompts you track
> - **Share of voice:** how you compare with your competitors
> - **Sources:** which pages and threads AI answers cite when they bring you up
> - **Opportunities:** specific actions that would raise your visibility

### After (run 1 of 3; the skill loaded)

2026-11-09, 13:08 UTC · `claude-opus-5-5` in Claude Code 2.1.319 · exact question:
`How visible is my brand in AI answers?`

> I can't check this yet because PromptScout isn't signed in for this session, so I can't read any of your brand's visibility data.
>
> **To connect it:**
> - **Claude Code:** run `/mcp`, select `plugin:promptscout:promptscout`, and follow the sign-in steps.
> - **claude.ai:** go to **Customize → Plugins**, open the PromptScout plugin, and connect it on its **Connectors** tab.
>
> When you're signed in, ask me again and I'll get:
> - **Share of voice:** how often ChatGPT, Perplexity, Gemini and Claude mention your brand, and for what period.
> - **Competitor rankings:** a table of your brand next to competitors, with changes since the previous period.
> - **Cited sources:** the pages AI answers link to most, and whether each one mentions your brand.
>
> I'll also say how confident the numbers are and what PromptScout doesn't track for your brand.

## Signed-in runs: the founder's test after merge

Decision by the founder (2026-11-09, answered through Symphony): "I will do the manual stuff
myself." The signed-in steps happen after merge, and this session does not sign in to
PromptScout or claude.ai. Two signed-in checks remain. Their exact steps and pass conditions are
in the PR's "Founder's test after merge" section:

1. A live-data run of "How visible is my brand in AI answers?" in Claude Code.
2. The claude.ai **Customize > Plugins** view, showing the PromptScout entry with its icon.
