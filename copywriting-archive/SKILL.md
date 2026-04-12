# Skill: Copywriting

**Folder:** `copywriting-archive/`
**Depends on:** an approved campaign brief in `campaign-strategy/`
**Feeds into:** `email-design/` (copy is inserted into HTML templates)

---

## What This Skill Does

Writes on-brand email copy — subject lines, preview text, body copy, and CTAs —
guided by the campaign brief and the brand voice documents in this folder.
Also archives high-performing copy so future campaigns can reference it.

---

## Inputs

| Input | Required | Description |
|---|---|---|
| Campaign brief path | Yes | Path to the approved `*-brief.md` in `campaign-strategy/` |
| Email number in series | Yes | Which email in the send sequence this copy is for |
| Tone direction | No | Any campaign-specific tone override from brief Section 6.4 |
| Copy length target | No | Short (≤ 100 words body), standard (100–200 words), long-form (200+) |

If the campaign brief is not yet approved (status ≠ `Approved`), stop and ask
the user to approve the brief before writing copy.

---

## Context Documents — Read These First

Before writing any copy, read the following files in this folder in order:

1. `brand-voice-guide.md` — defines tone, personality, words to use, words to
   avoid, and mandatory compliance copy. This is the highest-authority document.
   Do not deviate from it without explicit user instruction.
2. `subject-line-swipes.md` — approved subject line examples organized by goal.
   Reference these for structural patterns; do not copy verbatim.
3. `copy-examples/` — approved body copy examples by tone. Read the file(s)
   that match the tone specified in the campaign brief.

Then read from `campaign-strategy/`:
4. The active campaign brief — focus on Sections 6 (Messaging Hierarchy),
   7 (Email Series Plan), 8 (Offer and CTA Strategy), and 9 (Subject Line
   and Preview Text Direction).

---

## Process

### Step 1 · Map the message
From the brief, extract:
- Primary message (Section 6.1) → drives the subject line and hero copy
- Secondary messages (Section 6.2) → drive body proof points
- Offer and CTA (Section 8) → drives the button label and urgency language
- Tone (Section 6.4) → filters every word choice

### Step 2 · Write subject line and preview text
- Write 3–5 subject line options matching the angle from brief Section 9.
- Write matching preview text for each (≤ 90 characters).
- Check every option against the avoid list in `brand-voice-guide.md`.
- Select the strongest option and flag it as the recommended variant.

### Step 3 · Write body copy
- Open with the primary message — make it the first sentence or headline.
- Support with 2–3 secondary message proof points.
- Close with a transition into the CTA.
- Match the word count target (if specified) or use the brief's tone as a guide.
- Do not introduce claims, statistics, or product details not in the brief.

### Step 4 · Write the CTA
- Use the label direction from brief Section 8.
- Keep to 2–4 words. Action verb first.
- Confirm the destination URL matches the brief.

### Step 5 · Self-review
Before delivering, check:
- [ ] No words from the avoid list in `brand-voice-guide.md`
- [ ] Subject line ≤ 50 characters (or justified if longer)
- [ ] Preview text ≤ 90 characters
- [ ] One primary CTA — no competing calls to action in the body
- [ ] Legal or compliance copy included if required by brief Section 14

### Step 6 · Archive strong copy
After the campaign completes, save high-performing subject lines to
`subject-line-swipes.md` and notable body copy blocks to the appropriate
file in `copy-examples/`. Note open rate or conversion result if available.

---

## Output Spec

| Output | Delivered as | Saved to |
|---|---|---|
| Subject line options (3–5) | Inline in response | — |
| Recommended subject + preview text | Inline in response | — |
| Body copy | Inline in response | — |
| CTA label | Inline in response | — |
| Post-campaign archive entry | — | `subject-line-swipes.md` or `copy-examples/` |

Copy is delivered inline for the designer/builder to paste into the template.
It is only saved to this folder after the campaign completes.

---

## Rules

- Never write copy without reading `brand-voice-guide.md` first.
- Never invent product claims, pricing, or legal terms not in the brief.
- Never write more than one primary CTA per email.
- If the brand voice guide and the brief conflict, flag it — do not silently
  choose one over the other.
- Do not archive copy that was not actually sent or was rejected by the team.
