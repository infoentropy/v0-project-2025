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
├── campaign-strategy/       # Strategic briefs, audience frameworks, goals
├── email-design/            # Layout templates, design guidelines, component patterns
├── copywriting-archive/     # Approved copy examples, tone guides, swipe files
├── campaign-orchestration/  # Workflow definitions, sequencing rules, channel logic
└── CLAUDE.md                # This file
```

---

## Folder Purposes

### `campaign-strategy/`
Documents that define the *why* and *what* of campaigns.

- Target audience personas and segmentation rules
- Campaign goals and success metrics
- Messaging hierarchies (primary, secondary, tertiary messages)
- Seasonal or product-launch strategy briefs
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
Documents that define *how* campaigns run end-to-end.

- Send sequence logic (triggers, delays, branching conditions)
- Channel priority rules (email vs. SMS vs. push)
- Suppression and frequency capping rules
- A/B test configuration standards
- Integration touchpoints with other tools or platforms

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

| Skill | Primary Folder(s) |
|---|---|
| Campaign Strategy | `campaign-strategy/` |
| Email Design | `email-design/` |
| Copywriting | `copywriting-archive/` |
| Campaign Orchestration | `campaign-orchestration/` |

Skills read the documents in their folder(s) to inform their outputs. When a
skill produces something new (a strategy brief, a copy block, a workflow), the
result should be saved back into the appropriate folder so it becomes part of
the shared knowledge base.

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
