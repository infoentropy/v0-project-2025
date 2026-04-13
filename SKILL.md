# Master Skills File

This is the root registry for all Claude skills in this repository. Use this
file as the entry point when you need to know which skill to invoke, what it
reads, and what it produces.

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

### Campaign Strategy

**Reference folder:** `campaign-strategy/`
**Skill instructions:** `campaign-strategy/SKILL.md`

**What this skill does:**
Produces a strategy brief that defines a campaign's business objective, target
audience, messaging hierarchy, success metrics, and send plan — including which
design template each email in the series uses. All downstream skills read the
brief this skill writes before doing any work.

**Reads from:**
- `campaign-strategy/email-strategy-brief-template.md` — canonical brief structure
- `campaign-strategy/` — audience persona and segmentation reference docs
- `email-design/03-pages/` — to assign a design template to each email in the series

**Writes to:**
- `projects/<slug>/campaign-strategy-brief.md` — one file per campaign

**Invoke when:**
- Starting a new campaign from scratch
- Revisiting goals or audience targeting mid-campaign
- Needing a messaging hierarchy before copy or design work begins

**Downstream skills unblocked after this runs:** Copywriting, Campaign Orchestration (once brief status = `Approved`)

---

### Email Design

**Reference folder:** `email-design/`
**Skill instructions:** `email-design/SKILL.md`

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

---

### Copywriting

**Reference folder:** `copywriting-archive/`
**Skill instructions:** `copywriting-archive/SKILL.md`

**What this skill does:**
Writes subject lines, preview text, body copy, and CTAs for every copy field
defined in the campaign's email template schema. References approved brand
guidelines and copy examples to keep output consistent across campaigns.

**Reads from:**
- `projects/<slug>/campaign-strategy-brief.md` — messaging hierarchy, tone, offer, CTA direction
- `email-design/03-pages/<template-name>/<template-name>.schema.json` — definitive list of copy fields
- `copywriting-archive/brand-voice-guide.md` — highest-authority tone and compliance rules
- `copywriting-archive/subject-line-swipes.md` — structural patterns for subject lines
- `copywriting-archive/copy-examples/` — approved copy by tone (if populated)

**Writes to:**
- `projects/<slug>/copy.json` — copy output for the campaign (one JSON object per email, accumulated in one file)
- `copywriting-archive/subject-line-swipes.md` — post-campaign archive of high-performing subject lines
- `copywriting-archive/copy-examples/` — post-campaign archive of notable body copy

**Invoke when:**
- Writing email copy for any email in the campaign series
- Checking whether a phrase or subject line is on-brand
- Archiving high-performing copy after a campaign completes

**Requires:** Brief at `projects/<slug>/campaign-strategy-brief.md` with status `Approved` and a design template assigned in Section 7.2

---

### Campaign Orchestration

**Reference folder:** `campaign-orchestration/`
**Skill instructions:** `campaign-orchestration/SKILL.md`

**What this skill does:**
Builds all artifacts needed to launch a campaign: send sequence logic, A/B test
configuration, UTM tracking, and ESP-ready rendered HTML. Runs as five subtasks
that can be executed in any order that fits the current production state.

**Reads from:**
- `projects/<slug>/campaign-strategy-brief.md` — timing, audience, channel, and A/B test plans
- `projects/<slug>/copy.json` — copy values for HTML rendering (Subtask 4)
- `campaign-orchestration/personalization-data-catalog.md` — authoritative list of contact fields and events
- `campaign-orchestration/suppression-rules.md`
- `campaign-orchestration/frequency-capping-rules.md`
- `campaign-orchestration/channel-priority-rules.md`
- `campaign-orchestration/ab-test-standards.md`

**Writes to:**
- `projects/<slug>/orchestration.md` — send sequence workflow, A/B config, UTMs, and approval sign-off
- `projects/<slug>/templates/rendered/` — ESP-ready HTML files (gitignored)

**Subtasks:**
1. Build Send Sequence → `projects/<slug>/orchestration.md`
2. Configure A/B Tests → appended to `projects/<slug>/orchestration.md`
3. Define Tracking and Attribution → appended to `projects/<slug>/orchestration.md`
4. Render ESP-Ready HTML → `projects/<slug>/templates/rendered/`
5. Validate and Handoff → sign-off recorded in `projects/<slug>/orchestration.md`

**Invoke when:**
- Setting up send logic, triggers, or branching conditions for a campaign
- Rendering copy into ESP-ready HTML
- Completing final pre-launch validation and approval

**Requires:** Brief with status `Approved`; copy JSON at `projects/<slug>/copy.json` for Subtask 4

---

## How Skills Work Together

A typical campaign flows through all four skills. The `projects/<slug>/` folder
is the shared hub — each skill deposits its output there for the next skill to
pick up.

```
[Campaign Strategy] ──────────────────────────────────┐
  writes: projects/<slug>/campaign-strategy-brief.md   │
                                                        ▼
                                              [projects/<slug>/]
                                                        │
         ┌──────────────────────────────────────────────┤
         ▼                                              ▼
   [Copywriting]                              [Email Design]
   reads:  brief + schemas                    reads:  mockups
   writes: copy.json                          writes: email-design/03-pages/
         │                                              │
         └──────────────────┬───────────────────────────┘
                            ▼
               [Campaign Orchestration]
               reads:  brief + copy.json + templates
               writes: orchestration.md + rendered HTML
```

**Execution order:**
1. **Campaign Strategy** — produces the brief; nothing else can start without it
2. **Email Design** — can run in parallel with step 1 if templates already exist;
   must complete before the brief can be fully approved (design template gate)
3. **Copywriting** — requires approved brief with template assigned in Section 7.2
4. **Campaign Orchestration** — Subtasks 1–3 require approved brief; Subtask 4
   additionally requires `copy.json`

No skill should begin without a strategy brief. No copy should be written without
an approved brief and an assigned design template.

---

## Adding a New Skill

1. Create a new top-level folder using `kebab-case` for global reference docs.
2. Add a `SKILL.md` inside it with full instructions (inputs, context documents,
   process steps, output spec, and rules).
3. Decide whether the skill produces **campaign-specific output**:
   - If yes: output goes to `projects/<slug>/` — add the file(s) to the
     `projects/<slug>/` structure in `CLAUDE.md` and document the path in the skill's Output Spec.
   - If no (global output like Email Design): output stays in the skill's own folder.
4. Register the skill in the **Skill Index** table and add a full
   **Skill Definition** section in this file.
5. Update the **How Skills Work Together** diagram if the new skill has
   dependencies on or feeds into existing skills.
6. Update `CLAUDE.md` — add the folder to the repository structure diagram,
   add a Folder Purposes entry, and update the skills table.
