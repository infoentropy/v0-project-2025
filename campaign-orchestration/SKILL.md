# Skill: Campaign Orchestration

**Folder:** `campaign-orchestration/`
**Depends on:** an approved campaign brief in `campaign-strategy/`
**Feeds into:** the sending platform / ESP (workflow definitions are exported or referenced here)

---

## What This Skill Does

Defines the end-to-end operational logic for running a campaign: entry triggers,
send sequence, wait steps, branching conditions, channel priority, suppression
rules, frequency capping, A/B test configuration, and integration touchpoints.
Output is a workflow definition document that an engineer or ESP operator can
implement directly.

---

## Inputs

| Input | Required | Description |
|---|---|---|
| Campaign brief path | Yes | Path to the approved `*-brief.md` in `campaign-strategy/` |
| ESP / sending platform | No | Name of the tool that will execute the workflow (e.g., Braze, Klaviyo, Iterable) |
| Suppression overrides | No | Any campaign-specific exceptions to global suppression rules |
| Integration dependencies | No | External systems this workflow must connect to (CRM, data warehouse, etc.) |

If the campaign brief is not yet approved (status ≠ `Approved`), stop and ask
the user to approve the brief before building the workflow.

---

## Context Documents — Read These First

Before building any workflow, read the following files in this folder in order:

1. `frequency-capping-rules.md` — global send limits per recipient per day/week.
   Every workflow must respect these unless the brief explicitly grants an
   override and a reason is documented.
2. `suppression-rules.md` — global suppression list logic (unsubscribes,
   bounces, complainers, recent purchasers). Apply all applicable rules.
3. `channel-priority-rules.md` — when email, SMS, and push overlap, defines
   which channel takes precedence and when fallbacks trigger.
4. `ab-test-standards.md` — required configuration format for A/B tests,
   sample size minimums, and winner-declaration criteria.

Then read from `campaign-strategy/`:
5. The active campaign brief — focus on Sections 4 (Target Audience and
   Suppression), 7 (Email Series Plan and Cadence Rules), 8 (Offer),
   12 (A/B Test Plan), and 13 (Tracking and Attribution).

---

## Process

### Step 1 · Map the send sequence
From brief Section 7, extract every email in the series:
- Entry trigger for Email 1 (date, behavioral event, or segment membership)
- Wait condition between each email (fixed delay, or behavioral branch)
- Exit conditions (purchase, unsubscribe, non-engagement threshold)

Draw the sequence as a text flow diagram before writing the formal document:
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

### Step 2 · Apply suppression and frequency rules
For every send node in the sequence:
- Apply all rules from `suppression-rules.md`.
- Apply frequency cap from `frequency-capping-rules.md`.
- If the brief requests an override, document the justification explicitly.

### Step 3 · Configure channel logic
If the campaign uses channels beyond email, apply `channel-priority-rules.md`
to define fallback conditions (e.g., if email bounces → SMS within 24 hours).

### Step 4 · Define A/B tests
For each test in brief Section 12:
- Map it to the correct send node.
- Apply sample size and split from `ab-test-standards.md`.
- Define winner-declaration date and fallback if no winner.

### Step 5 · Define tracking
Confirm UTM parameters from brief Section 13 are applied to every link at every
send node. Document the attribution window and reporting tool.

### Step 6 · Save the workflow document
Save as:
```
campaign-orchestration/<campaign-slug>-workflow.md
```

### Step 7 · Validate before handing off
- [ ] Every send node has an entry trigger (no floating sends)
- [ ] Exit conditions prevent infinite loops
- [ ] Suppression rules applied at every node
- [ ] Frequency cap not violated across any 7-day window
- [ ] A/B winner criteria defined for every test
- [ ] UTM parameters present on all links

---

## Output Spec

| Output | Location | Format |
|---|---|---|
| Workflow definition | `campaign-orchestration/<slug>-workflow.md` | Sequence diagram + node-by-node spec |

---

## Workflow Document Structure

Each `<slug>-workflow.md` file must contain these sections:

```
# Workflow: <Campaign Name>

## Overview
Brief | Audience | Series length | Entry trigger | Primary channel

## Sequence Diagram
[Text flow diagram of the full send sequence]

## Node Definitions
One sub-section per send node:
### Node N — <Email Name>
- Trigger / wait condition
- Audience at this node (after suppression)
- Suppression rules applied
- Channel
- A/B test (if any)
- UTM parameters
- Exit conditions

## Suppression Summary
List of all suppression rules applied and any overrides granted

## Frequency Cap Check
Confirmation that no recipient receives more than [N] sends in [window]

## A/B Test Summary
Test variable, split, winner criteria, decision date for each test

## Integration Touchpoints
External systems called at any node (CRM sync, data warehouse event, etc.)

## Approval
| Role | Name | Approved | Date |
```

---

## Rules

- Never build a workflow without reading `suppression-rules.md` and
  `frequency-capping-rules.md` first.
- Never leave a send node without a defined exit condition.
- If a brief calls for a frequency cap override, document the business reason
  in the workflow file — do not silently apply the override.
- Do not reference ESP-specific UI steps; keep workflow definitions
  platform-agnostic unless the user specifies a platform.
