# Claude plugin evidence (SL-1428)

These screenshots show what the public sees once PR #2 merges, plus the PromptScout sign-in page a plugin user meets. Each image links to its PNG file.
The full-size files sit in this folder. See also [examples.md](examples.md) (real Claude
answers) and [pages.json](pages.json).

## README on GitHub

Before is `main` (the public repository today). After is branch `feat/SL-1428-N_38Tzo6XS`. Both
are full-page captures of github.com taken on 2026-11-09.

### Before (main)

| 1440 px | 390 px |
| - | - |
| [![before-readme-1440.png](before-readme-1440.png)](before-readme-1440.png) | [![before-readme-390.png](before-readme-390.png)](before-readme-390.png) |

### After (branch)

| 1440 px | 390 px |
| - | - |
| [![after-readme-1440.png](after-readme-1440.png)](after-readme-1440.png) | [![after-readme-390.png](after-readme-390.png)](after-readme-390.png) |

## Claude Code `/plugin` panel

These are real interactive Claude Code 2.1.319 sessions, captured from the terminal on
2026-11-09.

### Before (main)

`/plugin marketplace add lukasz-starosta/promptscout-plugins` against the public repository
fails with `Marketplace file not found …/.claude-plugin/marketplace.json`.

| 1440 px | 390 px |
| - | - |
| [![before-plugin-panel-1440.png](before-plugin-panel-1440.png)](before-plugin-panel-1440.png) | [![before-plugin-panel-390.png](before-plugin-panel-390.png)](before-plugin-panel-390.png) |

### After: PromptScout details (branch)

`/plugin > Installed > PromptScout` shows the description, author, version, the 3 skills and the
`promptscout` server.

| 1440 px | 390 px |
| - | - |
| [![after-plugin-panel-1440.png](after-plugin-panel-1440.png)](after-plugin-panel-1440.png) | [![after-plugin-panel-390.png](after-plugin-panel-390.png)](after-plugin-panel-390.png) |

### After: installed list (branch)

The list shows PromptScout with 3 skills, and the `promptscout` server marked "Enter to auth".

| 1440 px | 390 px |
| - | - |
| [![after-plugin-list-1440.png](after-plugin-list-1440.png)](after-plugin-list-1440.png) | [![after-plugin-list-390.png](after-plugin-list-390.png)](after-plugin-list-390.png) |

## Sign-in page for a visitor with no PromptScout account

When the plugin's server needs sign-in, PromptScout's OAuth server sends the browser to the
PromptScout sign-in page. I checked on 2026-11-09 using GET requests only: no account, no OAuth
client registration and no form submission.

- **Sign-in page:** `www.promptscout.app/auth/login`. It offers "Continue with Google", email
  login, and **"Don't have an account? Sign up"**, which links to `/auth/sign-up`. The top bar
  also has "Start for free".
- **Following "Sign up"** opens `/auth/sign-up` (HTTP 200), "Create a free account to run your
  AI Visibility Check". The page was opened only; nothing was submitted.
- **Not verified:** the exact consent URL inside a real plugin sign-in, and whether signing up
  from there returns the visitor to the consent screen. Both need a registered OAuth client.
  Creating one is a production write, so they are part of the founder's step A.

| Sign-in, 1440 px | Sign-in, 390 px | Sign-up (after clicking "Sign up"), 1440 px |
| - | - | - |
| [![signin-page-1440.png](signin-page-1440.png)](signin-page-1440.png) | [![signin-page-390.png](signin-page-390.png)](signin-page-390.png) | [![signup-page-1440.png](signup-page-1440.png)](signup-page-1440.png) |

This folder is evidence for the founder's decision and is not part of the plugin. It can be
deleted before or after merge without affecting the plugin.
