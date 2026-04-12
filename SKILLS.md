# Master Skills File

This is the root registry for all Claude skills in this repository. Each skill
maps to a single folder. Use this file as the entry point when you need to know
which skill to invoke, what documents it reads, and what it is expected to
produce.

---

## Skill Index

| Skill | Folder | One-line purpose |
|---|---|---|
| [Campaign Strategy](#campaign-strategy) | `campaign-strategy/` | Define the why, who, and what of a campaign |
| [Email Design](#email-design) | `email-design/` | Translate designs into reusable HTML components and full templates |
| [Copywriting](#copywriting) | `copywriting-archive/` | Write on-brand copy for emails and campaigns |
| [Campaign Orchestration](#campaign-orchestration) | `campaign-orchestration/` | Define how campaigns run end-to-end across channels |

---

## Sub-Skill Definitions

### Campaign Strategy
**Folder:** `campaign-strategy/`

**What this skill does:**
Produces strategy briefs that define a campaign's business objective, target
audience, messaging hierarchy, success metrics, and send plan. All downstream
skills (copywriting, design, orchestration) pull from the brief this skill
writes.

**Reads from:**
- Audience persona and segmentation docs in `campaign-strategy/`
- Historical briefs for reference and continuity
- Competitive positioning notes in `campaign-strategy/`

**Writes to:**
- New campaign briefs in `campaign-strategy/`, named
  `<campaign-slug>-brief.md` (e.g., `q3-re-engagement-brief.md`)
- Updates to existing briefs as strategy evolves

**Key template:**
- `campaign-strategy/email-strategy-brief-template.md` — duplicate and fill
  in for every new campaign

**Invoke when:**
- Starting a new campaign from scratch
- Revisiting goals or audience targeting mid-campaign
- Needing a messaging hierarchy before copy or design work begins

---

### Email Design
**Folder:** `email-design/`

**What this skill does:**
Converts visual mockups (PNG, Figma) into documented HTML components, then
assembles those components into full email page templates. Works in three
sequential phases.

**Sub-folder structure:**
```
email-design/
├── 01-mockups/     # Input: design files → triggers component extraction
├── 02-components/  # Output of Phase 1; input for Phase 3
└── 03-pages/       # Assembled full email templates
```

**Reads from:**
- Design files or screenshots provided as input (Phase 1)
- Component `.md` files in `email-design/02-components/` (Phase 3)
- `email-design/README.md` for layout rules and HTML standards

**Writes to:**
- New component files in `email-design/02-components/`
- New page templates in `email-design/03-pages/`

**HTML rules enforced by this skill:**
- Table-based layout only; max content width 600 px
- All styles inline; no external stylesheets
- Images must carry `alt` text and explicit dimensions
- Tested against Gmail, Apple Mail, Outlook 2019+

**Invoke when:**
- Parsing a new design mockup into components
- Building a new email template
- Looking up an existing template before starting new design work

---

### Copywriting
**Folder:** `copywriting-archive/`

**What this skill does:**
Writes subject lines, preview text, body copy, and CTAs that match the brand
voice and the campaign's messaging hierarchy. References approved examples and
tone guidelines to keep output consistent across campaigns.

**Reads from:**
- Brand voice and tone guide in `copywriting-archive/`
- Subject line swipe files in `copywriting-archive/`
- Approved copy examples organized by tone and goal
- The active campaign brief in `campaign-strategy/` for messaging direction

**Writes to:**
- New copy blocks saved in `copywriting-archive/` for future reference
- Subject line additions to the relevant swipe file
- Tone or voice guide updates when brand guidance changes

**Invoke when:**
- Writing or reviewing email subject lines, preview text, or body copy
- Checking whether a phrase is on-brand or on the avoid list
- Adding high-performing copy to the archive after a campaign completes

---

### Campaign Orchestration
**Folder:** `campaign-orchestration/`

**What this skill does:**
Defines the end-to-end operational logic for running a campaign: trigger
conditions, send sequence, channel priority, suppression rules, A/B test
configuration, and integration touchpoints.

**Reads from:**
- Workflow and sequencing docs in `campaign-orchestration/`
- Channel priority and frequency capping rules in `campaign-orchestration/`
- The active campaign brief in `campaign-strategy/` for timing and audience

**Writes to:**
- New workflow definition files in `campaign-orchestration/`
- Updates to suppression and frequency capping rules
- A/B test configuration records

**Invoke when:**
- Setting up send logic, triggers, or branching conditions for a campaign
- Resolving channel conflicts or frequency cap questions
- Documenting integration touchpoints with external platforms

---

## How Skills Work Together

A typical campaign flows through all four skills in order:

```
Campaign Strategy  →  Copywriting
       ↓                   ↓
Campaign Orchestration  ←  Email Design
```

1. **Campaign Strategy** produces the brief — audience, goals, messaging
   hierarchy, and send plan.
2. **Copywriting** reads the brief and writes all copy assets.
3. **Email Design** reads the brief's design direction and assembles templates.
4. **Campaign Orchestration** reads the brief's timing and channel rules and
   builds the send workflow.

Skills may run in parallel once the brief is approved. No skill should begin
without a strategy brief.

---

## Adding a New Skill

1. Create a new top-level folder using `kebab-case`.
2. Add a `README.md` inside it explaining its purpose, folder structure, and
   HTML/format rules if applicable.
3. Register the skill in the **Skill Index** table and add a full
   **Sub-Skill Definition** section above.
4. Update `CLAUDE.md` to include the new folder in the repository structure
   and the skill-to-folder mapping table.
