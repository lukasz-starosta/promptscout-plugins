# The three account skills are unchanged

Recorded on 2026-11-11 with Claude Code 2.1.322 in the same cloud container as
[transcript.md](transcript.md), which has never signed in to PromptScout.

## The files are identical to main

`git diff --stat main -- claude/promptscout/skills/checking-ai-visibility claude/promptscout/skills/acting-on-opportunities claude/promptscout/skills/drafting-content-briefs`
prints 0 lines. SHA-256 of each file on this branch and on main:

```text
4178d7e945dc15be76cb6b02071be3646ed50e9f3438e66f513643969b7a47b0  claude/promptscout/skills/checking-ai-visibility/SKILL.md
2ac9a77a8021f43e17886546091bdf1258cd47daa7be8ce8a0a2d0f384612566  claude/promptscout/skills/acting-on-opportunities/SKILL.md
8083b3449ef2a25095799f613a22d4afcc7c305f6c4de6bc769fb0af2f47ded5  claude/promptscout/skills/drafting-content-briefs/SKILL.md
4178d7e945dc15be76cb6b02071be3646ed50e9f3438e66f513643969b7a47b0  claude/promptscout/skills/checking-ai-visibility/SKILL.md (main)
2ac9a77a8021f43e17886546091bdf1258cd47daa7be8ce8a0a2d0f384612566  claude/promptscout/skills/acting-on-opportunities/SKILL.md (main)
8083b3449ef2a25095799f613a22d4afcc7c305f6c4de6bc769fb0af2f47ded5  claude/promptscout/skills/drafting-content-briefs/SKILL.md (main)
```

## Same request, main and this branch, no account

Command: `claude -p "/promptscout:checking-ai-visibility" --plugin-dir <main or branch copy of claude/promptscout>`, no tools pre-approved.

On both, Claude called no PromptScout tool (tool calls: main none, branch none) and gave the
skill's sign-in steps. The only difference is in Claude's wording: on this branch it also
mentions the two skills that work without signing in, because it can now see them in the
plugin. The skill's own text and steps did not change.

### main

> I can't check your brand's AI visibility yet because the PromptScout tools need you to sign in first.
>
> **To connect PromptScout:**
> - **Claude Code:** run `/mcp`, select `plugin:promptscout:promptscout` and follow the sign-in.
> - **claude.ai or Cowork:** go to **Customize > Plugins**, open the PromptScout plugin and connect it on its **Connectors** tab.
>
> Because this is a cloud session, the `/mcp` sign-in may not work here. If it doesn't, connect the plugin on claude.ai and start a new session.
>
> Once you're signed in, run this again and I'll get:
> - your brand's share of voice and its rank against competitors, with the period it covers
> - a competitor table showing changes since the previous period
> - the sources AI answers cite most, and whether each one mentions your brand
> - a confidence rating based on how many prompts and AI engines are tracked
>
> If you have more than one brand in PromptScout, tell me which one to check.

### This branch

> I can't check your brand's AI visibility yet because the PromptScout server (`plugin:promptscout:promptscout`) isn't signed in, so none of its tools work in this session.
>
> You can't sign in to it from this cloud session, and I can't start the sign-in for you. To connect it, do one of these:
>
> - **Claude Code on your own machine:** run `/mcp`, select `plugin:promptscout:promptscout` and follow the sign-in.
> - **claude.ai or Cowork:** go to **Customize > Plugins**, open the PromptScout plugin, and connect it on its **Connectors** tab.
>
> Once you're signed in, run `/promptscout:checking-ai-visibility` again. The report will cover your share of voice and rank, how you compare with competitors, which sources AI answers cite, and how confident the numbers are.
>
> Two things work without signing in, if they help in the meantime:
> - `/promptscout:checking-website-readiness` checks whether your public website is technically ready for AI assistants to read and cite.
> - `/promptscout:aeo-geo-evidence-guide` answers general questions about how to get cited in AI answers.
