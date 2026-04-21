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
- See [the reference guide](references/REFERENCE.md) for details.

**Writes to:**
- `projects/<slug>/campaign-strategy-brief.md` — one file per campaign

**Invoke when:**
- Starting a new campaign from scratch
- Revisiting goals or audience targeting mid-campaign
- Needing a messaging hierarchy before copy or design work begins
