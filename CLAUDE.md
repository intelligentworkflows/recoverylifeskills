# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**recoverylifeskills.com** is a static informational website about 12-step recovery from alcoholism and substance abuse, written from the author's personal first-hand perspective (9+ years sobriety). The site targets people who cannot commit to traditional 90-day rehab programs and need practical, low-commitment entry points into recovery.

## Development

This is a **zero-build static site** — plain HTML5 and CSS3, no JavaScript, no dependencies, no package manager. There are no build, lint, or test commands.

To preview locally, open any HTML file directly in a browser, or serve with any static file server:
```
python -m http.server 8080
```

Deployment is manual: copy HTML/CSS files to the web host.

## Architecture

All pages share a single stylesheet (`style.css`) and follow an identical structural template:

1. `.disclaimer` block (repeated on every page — legal/privacy notice)
2. Site header with navigation back to home
3. `<main>` content
4. Footer

### CSS Design System

All theming uses CSS custom properties defined in `:root` in `style.css`:
- Colors: `--bg`, `--surface`, `--border`, `--text`, `--muted`, `--accent`, `--accent-light`, `--border-blue`
- Layout: `--max-w` (680px content width), `--radius` (6px)
- Font: system stack (SF Pro Display → Segoe UI → sans-serif)

Reusable component classes: `.note-box` (highlighted info block), `.prayer-card` (card layout), `.items-list` / `.step-list` / `.podcast-list` (custom list styles). Collapsible sections use native `<details>`/`<summary>` with CSS-only +/- toggle animation.

### Site Map

| Directory | Page purpose |
|-----------|-------------|
| `index.html` | Home — author intro + collapsible navigation hub |
| `aup/` | Acceptable Use Policy / legal disclaimers |
| `starting/` | Getting started guide with sample schedules |
| `basics-to-try/` | 11 core recovery approaches to explore |
| `upon-awakening/` | Daily morning routine (Big Book + sponsor + meeting) |
| `oxford-group/` | Historical context: The Four Absolutes |
| `step-prayers/` | Three key prayers from AA literature |
| `faq/` | ~20 detailed Q&A pairs (longest page, most content) |
| `family-recommendations/` | Social situations, family dynamics, sponsor relationships |

### External Dependencies

Apple Podcasts iframes embed Joe & Charlie's "Big Book Comes Alive" series across multiple pages. No other third-party resources — no analytics, no tracking, no cookies (by design).

## UI Business Rules

These are non-negotiable constraints for all pages and any future changes:

- **No cookies** — no tracking, no session storage, no localStorage, no analytics scripts.
- **No images** — convey all information through text and typography alone.
- **Mobile-first** — design for small screens first; desktop legibility is required but secondary.
- **FAQ pattern** — content is presented as questions that expand to reveal answers. Use native `<details>`/`<summary>` for all expandable Q&A. Avoid decorative chrome or sidebars that distract from the content.
- **Readable typography** — large base font size, generous line height, short line length (`--max-w: 680px`). Audience is non-technical and may be in crisis; clarity always beats cleverness.
- **Minimal visual noise** — no hero sections, no cards for decoration, no icons, no animations beyond the expand/collapse toggle.

## Content Guidelines

- The site is anonymous — no author identity, no contact form, no user accounts.
- All content reflects the AA Big Book and 12-step tradition; maintain that voice when editing.
- The disclaimer block at the top of every page is legally significant — do not remove or alter it without explicit instruction.
- New pages must follow the existing structural template and link back from `index.html`.
