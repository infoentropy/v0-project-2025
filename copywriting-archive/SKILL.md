# Skill: Copywriting

**Folder:** `copywriting-archive/`
**Depends on:** an approved campaign brief in `campaign-strategy/` with a design
template reference (brief Section 10)
**Feeds into:** `email-design/` — copy values are inserted into the page template's
`{{variables}}`

---

## What This Skill Does

Writes on-brand email copy for every copy field defined in the email design's
JSON schema. The brief identifies which page template the campaign uses; the
schema for that template is the authoritative list of fields that need copy.
No field is guessed or invented — every piece of copy maps directly to a named
schema variable.

---

## Inputs

| Input | Required | Description |
|---|---|---|
| Campaign brief path | Yes | Path to the approved `*-brief.md` in `campaign-strategy/` |
| Email number in series | Yes | Which email in the send sequence this copy is for |

If the campaign brief status is not `Approved`, stop and ask the user to approve
the brief first.

---

## Context Documents — Read These First

Read in this order before writing a single word:

1. **The campaign brief** (`campaign-strategy/<slug>-brief.md`)
   Locate the template path for this email in Section 7.2 (Design template
   status). If the row for this email shows Copy unblocked? = No, stop and
   ask the user to resolve the template before continuing.

2. **The page schema** (`email-design/03-pages/<template-name>/<template-name>.schema.json`)
   This is the definitive field list. Every copy field you write must correspond
   to a property in this schema.

3. **The page manifest** (`email-design/03-pages/<template-name>/<template-name>.md`)
   Scan the Variables Required table to understand the purpose of each field and
   confirm which are copy vs. asset fields.

4. **`brand-voice-guide.md`** (this folder)
   Defines tone, words to use, words to avoid, and required compliance copy.
   This is the highest-authority document — never deviate from it without
   explicit user instruction.

5. **`subject-line-swipes.md`** (this folder)
   Reference structural patterns for subject line options. Do not copy verbatim.

6. **`copy-examples/`** (this folder, if populated)
   Approved body copy examples by tone. Read the file(s) matching the tone in
   brief Section 6.4.

---

## Identifying Copy Fields in the Schema

Not every schema property needs copy. Use these rules to classify each property:

**Write copy for** properties that are:
- `"type": "string"` **and** have no `"format": "uri"` key
- Descriptions that reference text, label, headline, copy, alt text, or name

**Skip** properties that are:
- `"format": "uri"` — these are asset or link URLs (owned by design/engineering)
- Descriptions that reference color, size, radius, padding, or dimensions

Example classification using `starter-single-column.schema.json`:

| Property | Classify as | Reason |
|---|---|---|
| `headline` | **Copy** | string, no uri format, "Main headline text" |
| `body_copy` | **Copy** | string, no uri format, "Body paragraph(s)" |
| `cta_label` | **Copy** | string, no uri format, "Button label" |
| `logo_alt` | **Copy** | string, no uri format, "Alt text for the logo" |
| `hero_alt` | **Copy** | string, no uri format, "Alt text for the hero image" |
| `company_name` | **Copy** | string, no uri format — confirm value with user |
| `company_address` | **Copy** | string, no uri format — confirm value with user |
| `logo_url` | Skip | `"format": "uri"` |
| `hero_image_url` | Skip | `"format": "uri"` |
| `cta_url` | Skip | `"format": "uri"` |
| `unsubscribe_url` | Skip | `"format": "uri"` |

> **Note:** `subject_line` and `preview_text` are never in a page schema because
> they are set at the ESP send level, not in the HTML. Always write them — they
> are always required regardless of what the schema contains.

---

## Process

### Step 1 · Resolve the template
From brief Section 7.2, find the Design template path for this email. Navigate to:
```
email-design/03-pages/<template-name>/<template-name>.schema.json
```
Read the schema. List every property and classify each as **copy** or **skip**
using the rules above.

### Step 2 · Map the message to schema fields
From the brief extract:
- **Section 6.1** (Primary Message) → drives `headline` and subject line
- **Section 6.2** (Secondary Messages) → drives `body_copy` proof points
- **Section 8** (Offer and CTA) → drives `cta_label` and urgency language
- **Section 6.4** (Tone) → filters every word choice
- **Section 9** (Subject Line Direction) → drives subject line angle and tokens

### Step 3 · Write subject line and preview text
These are always required. Write 3–5 options:
- Match the angle from brief Section 9
- Check every option against the avoid list in `brand-voice-guide.md`
- Verify character counts: subject ≤ 50 chars, preview text ≤ 90 chars
- Mark the recommended option

### Step 4 · Write copy for each schema field
For each **copy** field identified in Step 1, write the value:
- Ground every field in the messaging hierarchy from the brief (Section 6)
- Do not introduce claims, statistics, or product details not in the brief
- Keep field values self-contained — each value will be dropped directly into
  the template `{{variable}}` without surrounding context

Output a single JSON object. Property names must exactly match the schema
property names. Subject line is the only field with multiple options — represent
it as an object with an `options` array and a `recommended` string. All other
copy fields are plain strings.

```json
{
  "email": 1,
  "template": "email-design/03-pages/<template-name>/",
  "subject_line": {
    "options": [
      "Option A — [subject line]",
      "Option B — [subject line]",
      "Option C — [subject line]"
    ],
    "recommended": "Option A — [subject line]"
  },
  "preview_text": "[preview text, ≤ 90 chars]",
  "headline": "[headline copy]",
  "body_copy": "[body copy]",
  "cta_label": "[CTA label]",
  "logo_alt": "[alt text]",
  "hero_alt": "[alt text]",
  "company_name": "[legal entity name]",
  "company_address": "[mailing address]"
}
```

Include only the copy fields identified in Step 1 plus `email`, `template`,
`subject_line`, and `preview_text`. Do not include URI fields or design fields.

### Step 5 · Self-review checklist
- [ ] Every required schema field (per `"required"` array) has a value
- [ ] No words from the avoid list in `brand-voice-guide.md`
- [ ] Subject line ≤ 50 characters
- [ ] Preview text ≤ 90 characters
- [ ] One CTA label — no competing calls to action
- [ ] Legal or compliance copy included if required by brief Section 14
- [ ] Alt text written for every image field (never left blank)

### Step 6 · Archive strong copy
After the campaign completes and results are known, save high-performing
subject lines to `subject-line-swipes.md` and notable body copy to the
appropriate file in `copy-examples/`. Note the metric result alongside each
archived piece.

---

## Output Spec

| Output | Delivered as | Saved to |
|---|---|---|
| JSON copy object (one per email) | Inline in response | — |
| Post-campaign archive entry | — | `subject-line-swipes.md` or `copy-examples/` |

Copy is delivered as a JSON object so values can be applied programmatically or
pasted directly into the template by field name. It is only saved to this folder
after the campaign completes.

---

## Rules

- Never write copy without first reading the page schema — field names in your
  output must exactly match property names in the schema.
- Never write copy for URI fields (`format: uri`).
- Never invent product claims, pricing, or legal terms not present in the brief.
- If the brief's Section 7.2 has no template path for this email, ask before proceeding.
- If the brand voice guide and the brief conflict on tone or language, flag it —
  do not silently choose one over the other.
- Do not archive copy that was not actually sent or was rejected by the team.
