# Website check evidence (SL-1468)

This folder is evidence for the founder's decision and is not part of the plugin.

- [transcript.md](transcript.md): four recorded Claude Code runs on this branch with no
  PromptScout account. `/promptscout:checking-website-readiness` on example.com and iana.org
  returns a full report with no sign-in prompt.
- [existing-skills.md](existing-skills.md): the three account skills are byte-identical to main,
  and `/promptscout:checking-ai-visibility` without an account gives the same sign-in steps on
  main and on this branch.
- README on GitHub, full-page captures of github.com taken on 2026-11-11. Before is `main`,
  after is branch `feat/SL-1468-S3Y72zMXbh`:
  - [before-readme-1440.png](before-readme-1440.png), [before-readme-390.png](before-readme-390.png)
  - [after-readme-1440.png](after-readme-1440.png), [after-readme-390.png](after-readme-390.png)
- [pages.json](pages.json): the page each screenshot shows.
