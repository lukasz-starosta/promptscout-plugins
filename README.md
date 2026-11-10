# PromptScout plugins

PromptScout shows how often AI assistants such as ChatGPT, Perplexity, Gemini and Claude mention
your brand, which sources they cite, and what you can do to appear more often. This repository
holds PromptScout's plugins for AI assistants, one folder per plugin target:

| Folder | Target | Status |
| :- | :- | :- |
| [`claude/promptscout`](claude/promptscout) | Claude (Claude Code, claude.ai, Cowork) | Available |

The repository root is also a Claude plugin marketplace named `promptscout`
([`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json)).

## The Claude plugin

The `promptscout` plugin connects Claude to your PromptScout account and adds three ready-made
workflows (skills):

- **checking-ai-visibility**: lists the brands you granted, then reads share of voice, competitor
  rankings and cited sources. Answers name the AI engine, the date and the source link.
- **acting-on-opportunities**: reads your current Opportunities and the steps for one, then marks
  it done or dismisses it only after you confirm.
- **drafting-content-briefs**: lists and reads your content briefs, and creates a new one only
  after you confirm.

You need a PromptScout account. The plugin connects to PromptScout's hosted MCP server at
`https://mcp.promptscout.app/mcp`, and you sign in to PromptScout the first time Claude uses it.
PromptScout MCP is in beta; if your sign-in shows no brand to approve, [contact us](https://www.promptscout.app/contact?utm_source=claude-plugin&utm_medium=github-readme&utm_campaign=claude-plugin).

### Install in Claude Code

Run these in a Claude Code session:

```text
/plugin marketplace add lukasz-starosta/promptscout-plugins
/plugin install promptscout@promptscout
```

On Claude Code 2.1.275 or later, one line does both:

```text
/plugin install promptscout --marketplace lukasz-starosta/promptscout-plugins
```

Then run `/reload-plugins` (or restart Claude Code), run `/mcp`, select
`plugin:promptscout:promptscout` and sign in to PromptScout in the browser window that opens.
Ask, for example, "How visible is my brand in AI answers?" or run
`/promptscout:checking-ai-visibility`.

### Install on claude.ai or in the Claude desktop app

1. Open **Customize > Plugins**.
2. Select **Add > Add marketplace** and enter `lukasz-starosta/promptscout-plugins`.
3. Add the **PromptScout** plugin.
4. Open the plugin's **Connectors** tab, connect PromptScout and sign in.

The plugin is then on your account in chat, Cowork and Claude Code.

## What the plugin reads and writes

The plugin itself stores nothing and runs nothing on your computer. Everything goes through
PromptScout's MCP server with the access you grant when you sign in.

- **Reads**: the brands you granted, their setup status, share of voice, competitor rankings,
  cited sources and threads, tracked AI engines and prompts, search performance, AI traffic to
  your site, Opportunities with their steps and evidence, and content briefs.
- **Writes**, each only after you confirm it in the conversation: marking an Opportunity done,
  dismissing an Opportunity, asking PromptScout to create new Opportunities, and creating a
  content brief.

PromptScout handles your data under its privacy policy: https://www.promptscout.app/privacy.

## Support

Visit [www.promptscout.app](https://www.promptscout.app/?utm_source=claude-plugin&utm_medium=github-readme&utm_campaign=claude-plugin) or use the [contact form](https://www.promptscout.app/contact?utm_source=claude-plugin&utm_medium=github-readme&utm_campaign=claude-plugin).

## For maintainers

Validate the plugin and the marketplace (needs Claude Code 2.1.281 or later and Python 3):

```bash
./scripts/validate.sh
```

It runs `claude plugin validate --strict` on `claude/promptscout` and on the repository root,
then the static checks in `tests/`.

## License

The code and manifests are under the MIT License; see [LICENSE](LICENSE). The PromptScout name
and logo are not licensed.
