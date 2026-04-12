# CLAUDE.md

This file explains the purpose, structure, and conventions of this repository
to any Claude skill or AI assistant that reads from it.

---

## Purpose

This repository is a **shared document library** for Claude skills. Each folder
corresponds to a distinct skill domain. Documents stored here are the source of
truth that skills pull from to do their work — brand voice, templates,
strategies, copy examples, and orchestration logic all live here.

Add, update, or retire documents in the appropriate folder as the team's
thinking evolves. Skills always reflect whatever is currently in this repo.

---

## Repository Structure

```
.
├── projects/                # One folder per campaign — all per-project outputs land here
│   └── (slug)/
│       ├── campaign-strategy-brief.md
│       ├── orchestration.md
│       └── templates/
├── campaign-strategy/       # Global templates and reference docs for the strategy skill
├── email-design/            # Global layout templates, design guidelines, component patterns
├── copywriting-archive/     # Approved copy examples, tone guides, swipe files
├── campaign-orchestration/  # Global scripts and reference docs for the orchestration skill
└── CLAUDE.md                # This file
```

---

## Folder Purposes

### `projects/`
One folder per campaign. All skill outputs that are specific to a campaign land
here so every artifact for a given project is in one place.

```
projects/<slug>/
├── campaign-strategy-brief.md   ← produced by Campaign Strategy skill
├── orchestration.md              ← produced by Campaign Orchestration skill
└── templates/
    └── rendered/                 ← rendered ESP-ready HTML (gitignored)
```

Use the campaign slug as the folder name: `spring-reengagement-2026`,
`q4-product-launch`. When a campaign is complete, move the whole folder to
`projects/_archive/<slug>/`.

### `campaign-strategy/`
Global templates and reference documents used by the Campaign Strategy skill.

- `email-strategy-brief-template.md` — canonical brief structure (do not edit output here)
- Audience personas and segmentation reference docs
- Competitive positioning notes

### `email-design/`
Documents that govern the *look and feel* of emails.

- Master layout templates (single column, two column, hero + text, etc.)
- Brand color palette, typography, and spacing rules
- Header and footer standards
- CTA button styles and placement guidelines
- Mobile responsiveness rules
- Dark mode considerations

### `copywriting-archive/`
A reference library of approved, high-performing copy.

- Subject line swipe files (organized by goal: open rate, re-engagement, etc.)
- Body copy examples by tone (urgent, educational, conversational, etc.)
- Brand voice and tone guidelines
- Words/phrases to avoid
- Legal or compliance copy requirements

### `campaign-orchestration/`
Global scripts and reference documents used by the Campaign Orchestration skill.

- `scripts/` — rendering and utility scripts
- `personalization-data-catalog.md` — authoritative list of contact fields and events
- Channel priority rules, suppression rules, frequency capping rules, A/B test standards

Per-campaign workflow output (`orchestration.md`, rendered HTML) goes to
`projects/<slug>/`, not here.

---

## File Conventions

- **Format:** Prefer Markdown (`.md`) for all documents. Use plain text (`.txt`)
  only when importing raw copy that must stay unformatted.
- **Naming:** Use `kebab-case` for all file names.
  - Good: `welcome-series-strategy.md`, `q4-subject-line-swipes.md`
  - Avoid: `Welcome Series Strategy.docx`, `copy v3 FINAL.txt`
- **One topic per file.** Don't bundle unrelated content into a single document.
- **Dates in names only when version matters:** `brand-voice-guide.md` is
  preferred over `brand-voice-guide-2025.md` unless you intentionally maintain
  versioned snapshots.

---

## How Skills Use This Repo

Each Claude skill is scoped to one or more folders:

| Skill | Reads from | Writes to |
|---|---|---|
| Campaign Strategy | `campaign-strategy/` (templates, personas) | `projects/<slug>/campaign-strategy-brief.md` |
| Email Design | `email-design/` | `email-design/` (global — not project-specific) |
| Copywriting | `copywriting-archive/` | `copywriting-archive/` |
| Campaign Orchestration | `campaign-orchestration/` (scripts, rules), `projects/<slug>/campaign-strategy-brief.md` | `projects/<slug>/orchestration.md`, `projects/<slug>/templates/` |

Skills read their reference folder(s) for global rules and templates. Campaign-
specific outputs always land in `projects/<slug>/` so every artifact for a
project is co-located.

---

## Updating Documents

- Edit documents directly in the appropriate folder.
- Write clear, descriptive commit messages that say what changed and why:
  - `Add Q3 re-engagement campaign brief`
  - `Update brand voice guide — remove formal tone section`
  - `Archive 2024 holiday subject line swipes`
- Do not delete documents without confirming they are no longer referenced by
  any active skill or campaign.
- If a document is outdated but worth keeping for reference, move it to an
  `_archive/` subfolder within the relevant folder rather than deleting it.

---

## What AI Assistants Should NOT Do

- Do not invent facts about audience segments, brand rules, or channel logic
  that are not documented here — flag the gap instead.
- Do not merge unrelated documents together.
- Do not rename files arbitrarily — naming changes break skill references.
- Do not commit files containing PII, real customer data, or credentials.
- Do not push to `main` directly — use a feature branch and get a review.
