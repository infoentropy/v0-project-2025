# Skill: Campaign Strategy

**Folder:** `campaign-strategy/`
**Depends on:** nothing — this skill runs first
**Feeds into:** `copywriting-archive/`, `email-design/`, `campaign-orchestration/`

---

## What This Skill Does

Produces a complete campaign strategy brief. The brief is the single source of
truth that every other skill reads before starting work. No copy should be
written, no template built, and no workflow configured without an approved brief
from this skill.

---

## Inputs

The user provides one or more of the following:

| Input | Required | Description |
|---|---|---|
| Campaign goal | Yes | What the campaign is trying to achieve (e.g., re-engagement, product launch, seasonal promo) |
| Audience description | Yes | Who the campaign targets — segment name, size, known behaviors |
| Send window | Yes | Approximate first and last send dates |
| Offer or incentive | No | Discount, free shipping, early access, or "no offer" |
| Channel constraints | No | Email only, or email + SMS + push |
| Design or tone references | No | Links to past campaigns, brand notes, or mood direction |

If any required input is missing, ask for it before proceeding.

---

## Context Documents — Read These First

Before producing any output, read the following files in this folder:

1. `email-strategy-brief-template.md` — the canonical brief structure; every
   output must follow this template exactly.
2. Any existing `*-brief.md` files in this folder — scan for audience segments,
   messaging patterns, and prior goals that may inform the current brief.

Do not invent audience segments, brand rules, or channel logic that are not
documented here or provided by the user. Flag the gap instead.

---

## Process

### Step 1 · Clarify scope
Confirm with the user: single email or a series? Promotional or lifecycle?
Any hard constraints (legal copy, suppression rules, budget)?

### Step 2 · Populate the brief
Duplicate `email-strategy-brief-template.md` and fill in every section.
- Write "TBD — Owner: [name], Due: [date]" for any unknown field.
- Do not leave any field blank.
- Sections 6 (Messaging Hierarchy) and 7 (Email Series Plan) are the highest-
  value sections — spend the most effort here.

### Step 3 · Select designs for the email sequence
For each email in the series (Section 7), assign a design template before the
brief can be approved for copywriting. This is a required gate — copywriting
cannot start without it.

1. List the available templates by scanning `email-design/03-pages/`.
2. For each email in Section 7, pick the template whose layout best fits the
   email's goal and content type (hero-led, product grid, plain text, etc.).
3. Fill in the **Design template** column in the Section 7 series plan table
   with the full path: `email-design/03-pages/<template-name>/`
4. Fill in Section 7.2 (Design template status):
   - Set **Template status** to `Ready` if the template folder contains all
     three required files (`.md`, `.html`, `.schema.json`).
   - Set **Template status** to `Draft` if the template is incomplete.
   - Set **Copy unblocked?** to `Yes` only when Template status is `Ready`.
5. If no suitable template exists for an email, set Template status to `Draft`
   and trigger the Email Design skill to build one before proceeding.

> A brief must not be moved to `Approved` while any email in the sequence has
> **Copy unblocked? = No**.

### Step 4 · Validate the brief
Before saving, confirm:
- [ ] One primary goal only (Section 5.1)
- [ ] Inclusion and exclusion criteria are both defined (Section 4.1)
- [ ] Every email in the series has a send trigger, not just a date (Section 7)
- [ ] Every email in the series has a Design template path in Section 7
- [ ] Every email in the series has Template status = `Ready` in Section 7.2
- [ ] Every email shows Copy unblocked? = `Yes` in Section 7.2
- [ ] A/B test plan has a single variable per test (Section 12)
- [ ] Legal review flag is set if promotional terms or discounts are present (Section 14)

### Step 5 · Save the output
Save the completed brief as:
```
campaign-strategy/<campaign-slug>-brief.md
```

Use a descriptive slug: `q3-re-engagement-brief.md`, `summer-launch-brief.md`.
Do not use dates in the file name unless maintaining versioned snapshots.

### Step 6 · Notify downstream skills
After saving, summarize for the user:
- Brief file path
- Primary goal and primary metric
- Audience segment name and estimated size
- Number of emails in the series
- Design template assigned to each email
- Which downstream skills are now unblocked (copy, orchestration)

---

## Output Spec

| Output | Location | Format |
|---|---|---|
| Campaign brief | `campaign-strategy/<slug>-brief.md` | Filled-in copy of `email-strategy-brief-template.md` |

---

## Rules

- One brief per campaign. Do not bundle two campaigns into one file.
- Brief status must be set to `Draft`, `In Review`, or `Approved` before any
  downstream skill begins work.
- If a brief already exists for the campaign, update it in place rather than
  creating a duplicate.
- Completed post-campaign briefs (Section 17 filled in) must be moved to
  `campaign-strategy/_archive/` rather than deleted.
