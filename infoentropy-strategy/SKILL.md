---
name: infoentropy-campaign-strategy
description: Use this skill to start, define, and refine marketing campaign strategy including Briefs and Copywriting. This is primarily for non-technical people who want send an email.
---

# Infoentropy Campaign Strategist

## When to use this skill

---

## The Projects Pattern

Campaign-specific outputs from all skills land in a shared project folder:

```
projects/<slug>/
├── campaign-strategy-brief.md   ← Campaign Strategy skill
├── copy.json                     ← Copywriting skill
├── orchestration.md              ← Campaign Orchestration skill
└── templates/
    └── rendered/                 ← Campaign Orchestration skill (gitignored)
```

Each skill has a **reference folder** for global rules and templates that do not
change per campaign. Outputs that are campaign-specific always go to
`projects/<slug>/` — never back into the reference folder.

| Skill | Reference folder | Writes to |
|---|---|---|
| Campaign Strategy | `campaign-strategy/` | `projects/<slug>/campaign-strategy-brief.md` |
| Email Design | `email-design/` | `email-design/` (global — not project-specific) |
| Copywriting | `copywriting-archive/` | `projects/<slug>/copy.json` |
| Campaign Orchestration | `campaign-orchestration/` | `projects/<slug>/orchestration.md`, `projects/<slug>/templates/` |

---

## Skill Index

| Skill | Reference folder | One-line purpose |
|---|---|---|
| [Campaign Strategy](#campaign-strategy) | `campaign-strategy/` | Define the why, who, and what of a campaign |
| [Email Design](#email-design) | `email-design/` | Translate designs into reusable HTML components and full templates |
| [Copywriting](#copywriting) | `copywriting-archive/` | Write on-brand copy for every field in the email template |
| [Campaign Orchestration](#campaign-orchestration) | `campaign-orchestration/` | Build the send sequence, A/B tests, tracking, and rendered HTML |

---

## Skill Definitions

### infoentropy-strategy

**What this skill does:**
Produces a strategy brief that defines a campaign's business objective, target
audience, messaging hierarchy, success metrics, and send plan — including which
design template each email in the series uses. All downstream skills read the
brief this skill writes before doing any work.

**Reads from:**
- `reference/email-strategy-brief-template.md` — canonical brief structure
- `reference/` — audience persona and segmentation reference docs

**Writes to:**
- `projects/<slug>/campaign-strategy-brief.md` — one file per campaign

**Invoke when:**
- Starting a new campaign from scratch
- Revisiting goals or audience targeting mid-campaign
- Needing a messaging hierarchy before copy or design work begins

---

### infoentropy-email-designer
**What this skill does:**
Converts visual mockups (PNG, Figma) into documented HTML components, then
assembles those components into full email page templates. Templates produced
here are global — shared across campaigns, not tied to any single project.

**Sub-folder structure:**
```
email-design/
├── 01-mockups/     # Input: design files → triggers component extraction
├── 02-components/  # Output of Phase 1; input for Phase 3
└── 03-pages/       # Assembled full email templates (referenced by campaigns)
```

**Reads from:**
- Design files or screenshots provided as input
- Component `.md` files in `email-design/02-components/`
- `email-design/README.md` for layout rules and HTML standards

**Writes to:**
- `email-design/02-components/` — new component files
- `email-design/03-pages/` — new page templates

**HTML standards enforced:**
- Table-based layout only; max content width 600 px
- All styles inline; no external stylesheets
- Images must carry `alt` text and explicit dimensions
- Tested against Gmail, Apple Mail, Outlook 2019+

**Invoke when:**
- Parsing a new design mockup into components
- Building a new email template that multiple campaigns will use
- Checking what templates are available before starting a campaign brief
