# Skill: Campaign Orchestration

**Folder:** `campaign-orchestration/`
**Depends on:** an approved campaign brief in `campaign-strategy/`
**Feeds into:** the sending platform / ESP (workflow definitions, rendered HTML)

---

## What This Skill Does

Defines the end-to-end operational logic for running a campaign and produces
the artifacts needed to launch it. The skill is organized as a set of named
**subtasks** — each has defined inputs, a process, and an output.

Run subtasks in the order that fits your campaign's production state. Most
campaigns run them roughly in sequence; some can run in parallel.

---

## Inputs

| Input | Required | Description |
|---|---|---|
| Campaign brief path | Yes | Path to the approved `*-brief.md` in `campaign-strategy/` |
| Copy JSON path | Yes (for Subtask 4) | Path to `copywriting-archive/<slug>-copy.json` |
| ESP / sending platform | No | Name of the tool executing the workflow (e.g., Braze, Klaviyo) |
| Suppression overrides | No | Campaign-specific exceptions to global suppression rules |
| Integration dependencies | No | External systems this workflow must connect to |

If the campaign brief is not yet approved (status ≠ `Approved`), stop and ask
the user to approve the brief before proceeding.

---

## Context Documents — Read These First

Before running subtasks that involve send logic, read these files in this folder:

1. `frequency-capping-rules.md` — global send limits per recipient per day/week
2. `suppression-rules.md` — global suppression logic (unsubscribes, bounces, complainers)
3. `channel-priority-rules.md` — precedence rules when email, SMS, and push overlap
4. `ab-test-standards.md` — required config format, sample size minimums, winner criteria

Then from `campaign-strategy/`:

5. The active campaign brief — focus on Sections 4, 7, 8, 12, and 13

The **Render ESP-Ready HTML** subtask (Subtask 4) does not require these documents.

---

## Subtasks

### Subtask 1 · Build Send Sequence

**Purpose:** Map the email series from the campaign brief into a structured
workflow document.

**Inputs:** Campaign brief (Sections 4 and 7), `suppression-rules.md`,
`frequency-capping-rules.md`, `channel-priority-rules.md`

**Process:**
1. Extract every email in the series from brief Section 7: name, trigger,
   template, send date.
2. Define each as a send node with: entry trigger, wait condition, suppression
   rules, exit conditions.
3. Apply frequency capping and suppression rules to every node.
4. Define branching (e.g., opened → suppress from next email; purchased → exit).
5. Draw the sequence as a text flow diagram:

```
[Entry trigger]
  → Email 1 (Day 0)
      ├─ Opened → wait 3 days → Email 2
      └─ Not opened → wait 2 days → Email 2 (re-send with alt subject)
  → Email 2
      ├─ Clicked → exit (converted)
      └─ Not clicked → wait 5 days → Email 3
  → Email 3 → exit
```

**Output:** `campaign-orchestration/<campaign-slug>/workflow.md`

---

### Subtask 2 · Configure A/B Tests

**Purpose:** Translate the A/B test plan from the brief into a structured test
configuration.

**Inputs:** Campaign brief (Section 12), `ab-test-standards.md`

**Process:**
1. Read each test entry: variable, variants, split %, winner criteria, decision
   date.
2. Validate that variant labels match the options defined in the copy JSON.
3. Write test configuration into the A/B Test Summary section of the workflow
   document.

**Output:** A/B Test Summary section in
`campaign-orchestration/<campaign-slug>/workflow.md`

---

### Subtask 3 · Define Tracking and Attribution

**Purpose:** Set UTM parameters and attribution windows for all sends.

**Inputs:** Campaign brief (Sections 8 and 13)

**Process:**
1. Define UTM parameters per email (source, medium, campaign, content).
2. Set attribution window (default: 7-day click, 1-day open, unless brief
   overrides).
3. Confirm parameters are applied to all links in the template.
4. Document reporting cadence and dashboard.

**Output:** Tracking and Attribution section in
`campaign-orchestration/<campaign-slug>/workflow.md`

---

### Subtask 4 · Render ESP-Ready HTML

**Purpose:** Produce rendered, send-ready HTML files by merging copy values
into design templates. Output files are ready to upload directly to an ESP.

**Inputs:**
- Copy JSON: `copywriting-archive/<campaign-slug>-copy.json`
- HTML templates referenced by the copy JSON:
  `email-design/03-pages/<template-name>/<template-name>.html`
- Schema files for variable validation:
  `email-design/03-pages/<template-name>/<template-name>.schema.json`

**Process:**

Run the rendering script from the repo root:

```bash
python campaign-orchestration/scripts/render-email-html.py \
    copywriting-archive/<campaign-slug>-copy.json
```

The script auto-derives the campaign slug from the copy JSON filename and
writes output to `campaign-orchestration/<campaign-slug>/rendered/` by
default. Override with `--output-dir` if needed.

The script:
1. Reads the copy JSON array (one object per email in the series).
2. For each email entry, reads the `template` field and resolves the `.html`
   file path.
3. Reads the paired `.schema.json` to understand all expected variables.
4. Substitutes every `{{variable}}` placeholder in the template with the
   matching value from the copy object.
5. Converts plain-text `body_copy` newlines into HTML paragraph breaks.
6. Logs a warning for any unresolved variables (e.g., URI fields like
   `{{cta_url}}` that the copy JSON doesn't supply).
7. Writes one rendered `.html` file per email to the output directory.

**Output:** `campaign-orchestration/<campaign-slug>/rendered/<email-slug>.html`

**Notes:**
- URI fields (`logo_url`, `hero_image_url`, `cta_url`, `unsubscribe_url`) are
  not written by the copywriting skill. Add them to the copy JSON before
  rendering, or fill them in the rendered file manually afterwards.
- Rendered files are build artifacts — do not commit them. The
  `campaign-orchestration/*/rendered/` pattern is in `.gitignore`.

---

### Subtask 5 · Validate and Handoff

**Purpose:** Final pre-launch checks before handing off to the ESP operator.

**Inputs:** Rendered HTML files, workflow document, campaign brief

**Checklist:**
- [ ] Campaign brief status is `Approved`
- [ ] One rendered HTML file exists per email in the series
- [ ] No unresolved `{{variable}}` tokens remain in any rendered file
- [ ] Workflow document covers all send nodes with defined exit conditions
- [ ] A/B test configuration complete with winner criteria and decision dates
- [ ] UTM parameters set on all links at every send node
- [ ] Suppression rules documented in workflow
- [ ] Frequency cap not violated across any 7-day window
- [ ] Sign-off recorded in the Approval section of the workflow document

**Output:** Approval section completed in
`campaign-orchestration/<campaign-slug>/workflow.md`

---

## Workflow Document Structure

Each `campaign-orchestration/<slug>/workflow.md` produced by Subtask 1 must
contain these sections:

```
# Workflow: <Campaign Name>

## Overview
Brief | Audience | Series length | Entry trigger | Primary channel

## Sequence Diagram
[Text flow diagram from Subtask 1]

## Node Definitions
### Node N — <Email Name>
- Trigger / wait condition
- Audience at this node (after suppression)
- Suppression rules applied
- Channel
- A/B test (if any)
- UTM parameters
- Exit conditions

## A/B Test Summary
[From Subtask 2]

## Tracking and Attribution
[From Subtask 3]

## Suppression Summary
List of all suppression rules applied, plus any overrides with business justification

## Frequency Cap Check
Confirmation no recipient receives more than [N] sends in any [window]

## Integration Touchpoints
External systems called at any node (CRM sync, data warehouse event, etc.)

## Approval
| Role | Name | Approved | Date |
```

---

## Rules

- Never run Subtask 1 without reading `suppression-rules.md` and
  `frequency-capping-rules.md` first.
- Never leave a send node without a defined exit condition.
- Never run Subtask 4 before the campaign brief is `Approved` and the copy
  JSON exists.
- Do not commit rendered HTML files — they belong in
  `campaign-orchestration/<slug>/rendered/`, which is gitignored.
- If a required context document is missing, flag the gap and do not proceed
  with the affected subtask.
- Frequency cap or suppression overrides must be documented in the workflow
  file with a business justification — do not silently apply them.
- Keep workflow definitions platform-agnostic unless the user specifies a
  platform.
