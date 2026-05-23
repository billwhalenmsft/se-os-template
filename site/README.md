# SE OS Landing Site

This folder is the source for the **SE OS marketing/landing site** — the page that gets shared with leadership, partners, and prospective adopters who haven't installed SE OS yet.

It's distinct from `web_ui/` (which is the Command Center an SE actually *uses* day to day).

## Live URL

Once GitHub Pages is enabled on this repo, the site will live at:

**https://billwhalenmsft.github.io/se-os/**

## How it's deployed

`/.github/workflows/deploy-pages.yml` publishes this folder to GitHub Pages on every push to `main` that touches the site (or any of the linked content: MANIFESTO, agents/, docs/, web_ui/).

The workflow also copies `MANIFESTO.md`, `web_ui/`, `agents/`, and `docs/` into the published site so that deep-links from the landing page resolve.

## To enable Pages (one-time)

1. Go to repo Settings → Pages
2. Source: **GitHub Actions** (not "Deploy from a branch")
3. Save
4. Push any change to `site/` and the workflow takes over

## Structure

- `index.html` — the single-page landing site (self-contained, no build step)
- `assets/` — images and icons (none yet — favicon is inlined as data URI)

## Editing principles

- **One file** — keep it all in `index.html` until that becomes painful
- **No frameworks** — semantic HTML + vanilla CSS + minimal JS only
- **Dark theme matches** `web_ui/index.html` so links between the marketing and product sides feel native
- **Every section earns its place** — if it doesn't move someone from "what is this?" to "I want to try it," cut it
