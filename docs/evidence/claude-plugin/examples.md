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

Claude searched the plugin catalog and the MCP registry. It showed an install card for three
third-party AI-visibility plugins from Anthropic's directory (Searcherries, Rankability,
UnifAPI), then answered:

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
  answer omits the skill's exact sign-in path (`/mcp` → `plugin:promptscout:promptscout`). This
  is a headless run, where interactive OAuth is impossible anyway. The founder's run below
  should check whether the skill loads in an interactive session.

## Not yet covered: a run on live PromptScout data

A signed-in run needs an OAuth sign-in to a PromptScout account. The task's constraints rule
that out for this session ("Do not sign in to PromptScout … the founder does every manual
step"), so no answer on live data exists yet. To produce it, the founder (or a session given a
test account) runs:

1. `/plugin marketplace add lukasz-starosta/promptscout-plugins`, then
   `/plugin install promptscout@promptscout` and `/reload-plugins`.
2. `/mcp` → `plugin:promptscout:promptscout` → authenticate, and grant one brand.
3. Ask `How visible is my brand in AI answers?` and paste the answer here under "With the
   plugin, signed in".
4. `/plugin` → disable PromptScout, start a new session, ask the same question, and paste the
   answer under "Without the plugin, same account".

**Pass:** the signed-in answer leads with share of voice and rank for the stated period. It
lists competitors and cited sources with links. Each AI claim names the engine, the date and
the source link, with High/Medium/Low confidence, and the answer says what was not checked.
