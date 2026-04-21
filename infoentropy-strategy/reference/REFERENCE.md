---
name: reference info for infoentropy-strategy
description: Use this reference to add context for fulfilling requests.
---

# Strategy Reference Index

This folder contains the source-of-truth documents the `infoentropy-strategy`
skill reads before producing campaign work. Read the specific files called out
by the subtask — do not load all of them by default.

---

## Files

### `brand-voice-guide.md`

**What it is:** The Hearthstone Home Co. brand voice guide. Highest-authority
document for tone — never deviate without explicit user instruction.

**Read when:** writing subject lines, preview text, body copy, CTAs, or any
customer-facing language; filling in a brief's Section 6.4 (Tone and Voice);
reviewing copy for compliance with brand rules.

**Covers:** brand personality; four voice dimensions (warm / direct / confident
/ respectful) with on-brand vs. off-brand examples; tone-by-context matrix;
approved words and phrases; words and phrases to avoid (weakening language,
hollow superlatives, manipulative phrasing, sycophantic phrases); grammar and
style conventions (Oxford comma, em dash, numbers, date/time format); subject
line rules (≤ 50 chars, sentence case, no exclamations); CTA button rules
(2–4 words, action verb first); mandatory legal and compliance copy
(unsubscribe footer, promotional offer disclaimer).

---

### `email-strategy-brief-template.md`

**What it is:** The canonical 17-section brief template. Every campaign
duplicates this file and fills in every section.

**Read when:** starting a new campaign brief; validating that an existing brief
is complete; understanding which fields downstream skills (copy, design,
orchestration) expect to find.

**Sections:** 1 Campaign Overview · 2 Campaign Dates · 3 Business Objective ·
4 Target Audience (inclusion, exclusion, suppression, insights) · 5 Goals and
Success Metrics · 6 Messaging Hierarchy (primary, secondary, tertiary, tone) ·
7 Email Series Plan + 7.1 Cadence + 7.2 Design template status ·
8 Offer and CTA Strategy · 9 Subject Line and Preview Text Direction ·
10 Design Direction · 11 Personalization and Dynamic Content · 12 A/B Test
Plan · 13 Tracking and Attribution · 14 Legal and Compliance · 15 Dependencies
and Risks · 16 Approvals · 17 Post-Campaign Notes.

**Key gates:**
- Brief status must be `Draft`, `In Review`, or `Approved`.
- A brief cannot be `Approved` while any email in Section 7.2 shows
  Copy unblocked? = `No`.
- One primary goal only (Section 5.1) — multi-goal briefs underperform.
- A/B tests: one variable per test (Section 12).

---

### `campaign-strategy.md`

**What it is:** Full process guide for producing a campaign strategy brief.
Defines the sequence of steps that populate the brief template above.

**Read when:** the user asks to start, draft, or refine a campaign brief.

**Process (summary):**
1. Clarify scope (single email vs. series, constraints).
2. Populate the brief from `email-strategy-brief-template.md` — never leave a
   field blank; write `TBD — Owner, Due` for unknowns.
3. Select a design template for every email in the series (Section 7.2 gate).
4. Validate the brief against the checklist.
5. Save to `projects/<slug>/campaign-strategy-brief.md`.
6. Summarize for the user and flag which downstream skills are unblocked.

**Writing standards:** plain language (9th-grade reading level); never invent
numbers — use `[INSERT: …]` placeholders; never invent people — leave owner
fields as `—`.

---

### `copywriting.md`

**What it is:** Full process guide for writing on-brand email copy against a
page template's JSON schema.

**Read when:** the brief at `projects/<slug>/campaign-strategy-brief.md` is
`Approved` and the user asks for copy for a specific email in the series.

**Core rule:** every copy field must map to a named property in the page
template's `.schema.json`. Never invent fields.

**Classification rule (copy vs. skip):**
- **Write copy for** `"type": "string"` properties with no `"format": "uri"`.
- **Skip** properties with `"format": "uri"` (design/engineering owns those).
- Always write `subject_line` (3–5 options) and `preview_text`, even though
  they are not in the page schema.

**Output:** a JSON object per email, saved to `projects/<slug>/copy.json`
(merged, not overwritten, when the file already exists). Property names must
match the schema exactly.

**Links out:** heavily references `brand-voice-guide.md` — that file is the
final authority on wording choices.

---

### `personalization-data-catalog.md`

**What it is:** Authoritative list of contact properties and events available
for template substitution (`{{token}}`) and workflow branching logic
(`contact.*`).

**Read when:** writing `{{variables}}` into an HTML template; writing `if/else`
branching in `orchestration.md`; reviewing a template or workflow for
unresolved fields.

**User properties (HTML-substitutable and branching-safe):** `first_name`,
`country`, `language`, `subscription_expires_at`, `favorite_content`,
`last_purchase_date`.

**Events (workflow-only, not HTML-substitutable):**
- Email: `email.sent`, `email.opened`, `email.clicked`
- Commerce: `purchase.completed`
- App / Web: `app.opened`, `page.viewed`

**Shorthand helpers available on `contact`:** `.purchased`, `.opened`,
`.clicked`, `.unsubscribed`, `.spam_complaint`, plus
`contact.events.last(...)`, `.count(...)`, `.occurred(...)` for richer checks.

**Blocker rule:** if a needed field is not listed here, do not invent one —
add a `# BLOCKER:` comment and flag it to the data team.

---

## How to Use This Index

- The skill's `SKILL.md` names specific files to read for each subtask. Follow
  those instructions first.
- Use this index to orient when a request does not clearly map to a subtask, or
  to confirm the right file before loading a large document.
- Do not bundle these files together in one read unless the task genuinely
  spans voice, strategy, and data — it rarely does.
