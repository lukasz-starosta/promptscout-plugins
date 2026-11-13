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

The `promptscout` plugin adds five ready-made workflows (skills) to Claude. Two work without a
PromptScout account:

- **checking-website-readiness**: checks up to five public pages of any website you name for
  what AI assistants and search engines need: crawler rules, sitemap, redirects, page titles,
  headings and meta descriptions. It lists each problem with where it is, the fix and why it
  matters, plus the date of the check.
- **aeo-geo-evidence-guide**: answers questions such as "How can my website appear in ChatGPT
  search?" or "Do I need llms.txt?" from PromptScout's guide, with steps, a way to check the
  result and public sources.

Three work with your PromptScout account:

- **checking-ai-visibility**: lists the brands you granted, then reads share of voice, competitor
  rankings and cited sources. Answers name the AI engine, the date and the source link.
- **acting-on-opportunities**: reads your current Opportunities and the steps for one, then marks
  it done or dismisses it only after you confirm.
- **drafting-content-briefs**: lists and reads your content briefs, and creates a new one only
  after you confirm.

### Without a PromptScout account

The website check and the guide use PromptScout's public website audit server at
`https://check.promptscout.app/mcp`. It needs no account, no sign-in and no payment. Run, for
example, `/promptscout:checking-website-readiness example.com`. The check covers technical setup
only: it does not measure whether AI assistants cite or recommend your website.

### With a PromptScout account

The account skills connect to PromptScout's hosted MCP server at
`https://mcp.promptscout.app/mcp`, and you sign in to PromptScout the first time Claude uses it.
Any PromptScout account with a brand can connect, on any plan. Free gets part of the visibility
data, Starter gets all of it, and Growth and higher also get Opportunities and content briefs.
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

Then run `/reload-plugins` (or restart Claude Code). The website check works right away: ask
"Is example.com ready for AI search?" or run `/promptscout:checking-website-readiness example.com`.
To use your PromptScout account, run `/mcp`, select `plugin:promptscout:promptscout` and sign in
to PromptScout in the browser window that opens. Then ask, for example, "How visible is my brand
in AI answers?" or run `/promptscout:checking-ai-visibility`.

### Install on claude.ai or in the Claude desktop app

1. Open **Customize > Plugins**.
2. Select **Add > Add marketplace** and enter `lukasz-starosta/promptscout-plugins`.
3. Add the **PromptScout** plugin.
4. To use your PromptScout account, open the plugin's **Connectors** tab, connect PromptScout
   and sign in. The website check and the guide need no sign-in.

The plugin is then on your account in chat, Cowork and Claude Code.

## What the plugin reads and writes

The plugin itself stores nothing and runs nothing on your computer. Everything goes through
PromptScout's two MCP servers.

- **Website check, no account**: PromptScout's server reads up to five public pages of the
  website you name, plus its robots.txt and sitemap, and keeps the result for seven days so
  Claude can read it. The guide reads only PromptScout's own guide. Neither one reads or changes
  any account.
- **Reads**, with the access you grant when you sign in: the brands you granted, their setup status, share of voice, competitor rankings,
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
