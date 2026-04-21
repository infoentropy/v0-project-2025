---
name: infoentropy-campaign-strategy
description: Use this skill to start, define, and refine marketing campaign strategy — including the campaign brief and on-brand copywriting for every email in the series. Aimed at non-technical strategists who need to send an email.
---

# Infoentropy Campaign Strategist

## When to use this skill

Invoke this skill when the user wants to:

- Start a new campaign from scratch (produce a strategy brief).
- Revisit goals, audience, or messaging on an existing campaign.
- Write subject lines, preview text, and body copy for an email whose brief is
  already `Approved`.
- Archive high-performing copy after a send.

Do **not** invoke this skill to build HTML templates (that is
`infoentropy-email-designer`) or to configure sends, A/B tests, and rendered
output (that is `infoentropy-bulk-generator`).

---

## The Projects Pattern

Campaign-specific outputs from every skill land in a shared project folder.
This skill writes two of those files:

```
projects/<slug>/
├── campaign-strategy-brief.md   ← this skill (brief)
├── copy.json                     ← this skill (copywriting)
├── orchestration.md              ← infoentropy-bulk-generator
└── templates/
    └── rendered/                 ← infoentropy-bulk-generator (gitignored)
```

Reference material that does **not** change per campaign stays in this skill's
own folder (`infoentropy-strategy/reference/` and `infoentropy-strategy/assets/`).
Never write campaign-specific output back into a reference folder.

---

## Skill Folder Layout

| Path | Contents |
|---|---|
| `infoentropy-strategy/SKILL.md` | This file |
| `infoentropy-strategy/assets/email-strategy-brief-template.md` | Canonical 17-section brief template |
| `infoentropy-strategy/reference/REFERENCE.md` | Index of the reference docs below |
| `infoentropy-strategy/reference/campaign-strategy.md` | Full process guide for writing a brief |
| `infoentropy-strategy/reference/copywriting.md` | Full process guide for writing copy against a page schema |
| `infoentropy-strategy/reference/brand-voice-guide.md` | Highest-authority tone and wording rules |
| `infoentropy-strategy/reference/personalization-data-catalog.md` | Allowed `{{tokens}}` and `contact.*` fields |

Read the specific reference file the subtask calls for — do not load all of
them by default.

---

## Subtask 1 · Produce a Campaign Strategy Brief

**When:** the user is starting a new campaign, or an existing brief needs to
be revisited (goals, audience, messaging, send plan).

**Inputs required from the user:**

| Input | Required | Description |
|---|---|---|
| Campaign goal | Yes | What the campaign is trying to achieve |
| Audience description | Yes | Segment name, size, known behaviors |
| Send window | Yes | Approximate first and last send dates |
| Offer or incentive | No | Discount, free shipping, early access, or "no offer" |
| Channel constraints | No | Email only, or email + SMS + push |
| Design or tone references | No | Links to past campaigns, brand notes |

If any required input is missing, ask before proceeding.

**Read first:**

1. `infoentropy-strategy/assets/email-strategy-brief-template.md` — the
   canonical brief structure. Every output must follow this template exactly.
2. `infoentropy-strategy/reference/campaign-strategy.md` — full process guide,
   including the design-template gate (Section 7.2) and validation checklist.
3. Any existing `projects/*/campaign-strategy-brief.md` (if the `projects/`
   folder exists) — scan for reusable audience segments and messaging patterns.

**Output:** `projects/<slug>/campaign-strategy-brief.md` — one file per campaign.

**Key gates (enforced by `campaign-strategy.md`):**

- Brief status must be `Draft`, `In Review`, or `Approved`.
- A brief cannot be `Approved` while any email in Section 7.2 shows
  `Copy unblocked? = No`.
- One primary goal only (Section 5.1).
- A/B tests list a single variable per test (Section 12).
- Design template paths in Section 7 point into
  `infoentropy-email-designer/assets/email-pages/<template-name>/`.

---

## Subtask 2 · Write Copy for an Email

**When:** the brief at `projects/<slug>/campaign-strategy-brief.md` has status
`Approved` and the user asks for copy for a specific email in the series.

If the brief is not yet `Approved`, stop and ask the user to approve it first.

**Read first (in this order):**

1. `projects/<slug>/campaign-strategy-brief.md` — locate the design template
   path for this email in Section 7.2. If the row shows `Copy unblocked? = No`,
   stop and ask the user to resolve the template before continuing.
2. `infoentropy-email-designer/assets/email-pages/<template-name>/<template-name>.schema.json`
   — the definitive field list. Every copy field you write must correspond to
   a property in this schema.
3. `infoentropy-email-designer/assets/email-pages/<template-name>/<template-name>.md`
   — the page manifest; confirms the purpose of each variable.
4. `infoentropy-strategy/reference/copywriting.md` — full process guide
   (classification rules, per-field writing steps, self-review checklist).
5. `infoentropy-strategy/reference/brand-voice-guide.md` — highest-authority
   document for tone and approved vs. avoided language.

**Classification rule (copy vs. skip):**

- **Write copy for** properties that are `"type": "string"` **and** have no
  `"format": "uri"` key.
- **Skip** properties whose format is `"uri"` — those are asset or link URLs
  (owned by design/engineering).
- Always write `subject_line` (3–5 options) and `preview_text`, even though
  they are not in the page schema.

**Output:** `projects/<slug>/copy.json` — one JSON object per email, merged
into any existing file (never overwritten). Property names must match the
schema exactly.

---

## Subtask 3 · Archive Strong Copy (Post-Campaign)

After a campaign completes and results are known, save high-performing
subject lines and body copy back into the reference folder so future
campaigns can reuse the patterns. See the Step 6 note in
`infoentropy-strategy/reference/copywriting.md`. Do not archive copy that
was not actually sent or was rejected by the team.

---

## Writing Standards

- **Plain language first.** Write at a 9th-grade reading level. Short
  sentences, active voice, direct statements.
- **Never invent numbers.** If a metric, audience size, conversion rate, or
  any numeric value is unknown, either ask the user or insert a clearly
  marked `[INSERT: …]` placeholder. Do not estimate or fabricate figures.
- **Never invent people.** Leave stakeholder, approver, and owner fields
  blank (`—`) rather than filling with placeholder names.
- **Brand voice is authoritative.** If the brief and the brand voice guide
  conflict on tone or language, flag it — do not silently choose one over
  the other.

---

## Rules

- One brief per campaign. Do not bundle two campaigns into one file.
- Update an existing brief in place rather than creating a duplicate.
- Completed post-campaign briefs (Section 17 filled in) move to
  `projects/<slug>/_archive/` rather than being deleted.
- Never write copy before reading the page schema — field names in the
  output must exactly match property names in the schema.
- Never write copy for URI fields.
- Never introduce product claims, pricing, or legal terms not present in
  the brief.
- If a needed personalization field is not in
  `infoentropy-strategy/reference/personalization-data-catalog.md`, add a
  `# BLOCKER:` comment rather than inventing a field name.
