# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repo is a collection of Claude Skills. Each top-level folder is one skill and contains a `SKILL.md` at its root. The skills work together to produce marketing email campaigns — a non-technical strategist writes a brief and copy, a designer produces HTML templates, and an orchestrator assembles send-ready artifacts.

## Skills

| Folder | Skill name (frontmatter) | Role |
|---|---|---|
| `infoentropy-strategy/` | `infoentropy-campaign-strategy` | Strategy briefs, audience, messaging, copywriting reference |
| `infoentropy-email-designer/` | `infoentropy-email-designer` | Parse mockups → HTML components → assembled page templates |
| `infoentropy-bulk-generator/` | `infoentropy-bulk-generator` | Build send sequence, A/B tests, render ESP-ready HTML |

Each `SKILL.md` begins with YAML frontmatter (`name`, `description`). The `description` is the trigger text Claude uses to decide when to invoke the skill — edit it carefully.

## The `projects/<slug>/` Pattern

Campaign-specific outputs from every skill land in a shared `projects/<slug>/` folder (gitignored artifacts live under `projects/<slug>/templates/rendered/`). Reference material that does **not** change per campaign stays in the skill's own folder. Never write campaign-specific output back into a skill's reference folder.

Standard layout:
```
projects/<slug>/
├── campaign-strategy-brief.md   ← infoentropy-strategy
├── copy.json                     ← copywriting output
├── orchestration.md              ← infoentropy-bulk-generator
└── templates/rendered/           ← render-email-html.py output (gitignored)
```

## Rendering ESP-Ready HTML

```bash
python infoentropy-bulk-generator/scripts/render-email-html.py projects/<slug>/copy.json
```

Substitutes `{{variables}}` in each email's template using values from `copy.json` and writes rendered HTML to `projects/<slug>/templates/rendered/`. Warns on unresolved URI fields.

## HTML Standards (enforced by `infoentropy-email-designer`)

- Table-based layout only — no `<div>`, flexbox, or grid.
- Max content width: 600 px.
- All styles inline; no external stylesheets or `<style>` blocks.
- Images require `alt` text and explicit `width` + `height` attributes.
- Variables: `{{snake_case}}` double-curly tokens.
- `role="presentation"` on layout tables.
- Test targets: Gmail, Apple Mail, Outlook 2019+.

## Component / Page Three-File Rule

Every component in `02-components/<name>/` and every page in `03-pages/<name>/` must contain exactly three files with matching basenames:
- `<name>.md` — purpose, schema table, usage notes
- `<name>.html` — raw HTML with `{{tokens}}`
- `<name>.schema.json` — JSON Schema draft-07 for the variables

Variable names must be identical across all three files. A folder with fewer than three files is invalid.

Before creating a new component or page, always scan existing ones and prefer updating over duplicating.

## Personalization Data

Every `{{variable}}` in a template and every `contact.*` condition in an orchestration file must map to a field in `infoentropy-strategy/reference/personalization-data-catalog.md`. If a needed field is missing, add a `# BLOCKER:` comment rather than inventing a field name.

## Conventions

- `kebab-case` filenames with `.md`, `.html`, or `.schema.json` extensions.
- One topic per file.
- Work on a feature branch; do not push to `main` directly.

## Known Inconsistency

The top-level `README.md` still describes an older folder layout (`email-design/`, `campaign-strategy/`, `copywriting-archive/`, `campaign-orchestration/`). The actual folders are the `infoentropy-*` directories listed above. The `SKILL.md` files also still reference the old folder names internally (e.g., `campaign-orchestration/personalization-data-catalog.md`, `email-design/02-components/`). Treat the folder names in this CLAUDE.md as authoritative when locating files; update skill docs as you encounter drift.
