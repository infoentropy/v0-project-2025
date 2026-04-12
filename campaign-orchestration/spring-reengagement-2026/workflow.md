# Workflow: Spring Re-engagement 2026

**Campaign code:** CMP-2026-Q2-REEN
**Brief:** `campaign-strategy/spring-reengagement-2026-brief.md`
**Workflow built:** 2026-04-12
**Workflow status:** Draft — pending Legal sign-off (Sam Patel, due 2026-04-16)

---

## Overview

| Field | Value |
|---|---|
| Campaign name | Spring Re-engagement 2026 |
| Campaign code | CMP-2026-Q2-REEN |
| Brief status | Approved (2026-04-10, Robin Okafor) |
| Primary channel | Email |
| Series length | 3 emails |
| Entry segment | Lapsed purchasers — 90–180 day no-open (est. 12,400 contacts) |
| Entry trigger | Scheduled batch send, 2026-04-28 10 am local |
| Offer | 15% off one order, expires 2026-05-12 at 11:59 pm PT |
| First send date | 2026-04-28 |
| Last send date | 2026-05-12 (hard deadline — offer expires) |
| Copy JSON | `copywriting-archive/spring-reengagement-2026-copy.json` |
| ESP | TBD — workflow is platform-agnostic |

---

## Sequence Diagram

```
[Entry trigger: 2026-04-28, 10 am local]
│
│  Pre-send suppression:
│    — global opt-out list
│    — hard bounces and spam complainers
│    — purchased in last 30 days
│    — unengaged > 180 days → route to sunset flow (not this series)
│
▼
╔══════════════════════════════════════════╗
║  NODE 1 — The Check-In                  ║
║  2026-04-28 · est. ~12,000 recipients   ║
║  A/B test: subject line 50/50 split     ║
╚══════════════════════════════════════════╝
│
├── Purchased at any point ──────────────────────────────► EXIT SERIES
│
├── Opened · did NOT click (24-hr window)
│       │
│       └── trigger Node 2 within 24 hrs of open
│           (openers-no-click batch, ~2026-04-29)
│
└── Not opened after 72 hrs
        │
        └── trigger Node 2 on 2026-05-01
            (non-opener batch)


╔══════════════════════════════════════════╗
║  NODE 2 — The Offer                     ║
║  2026-04-29 (openers-no-click batch)    ║
║  2026-05-01 (non-opener batch)          ║
║  est. ~11,000 recipients                ║
║  Offer introduced: 15% off              ║
╚══════════════════════════════════════════╝
│
├── Purchased within 5 days ─────────────────────────────► EXIT SERIES
│
└── No purchase within 5 days
        │
        ├── 5 days after 2026-04-29 send → Node 3 on 2026-05-04
        └── 5 days after 2026-05-01 send → Node 3 on 2026-05-06


╔══════════════════════════════════════════╗
║  NODE 3 — Last Chance                   ║
║  2026-05-04 and 2026-05-06              ║
║  est. ~10,600 recipients                ║
║  ⚠ Hard deadline: all sends must        ║
║  complete by 2026-05-12 11:59 pm PT     ║
╚══════════════════════════════════════════╝
│
├── Purchased ───────────────────────────────────────────► EXIT SERIES (converted)
│
└── No action ───────────────────────────────────────────► EXIT SERIES (flag for sunset)
```

---

## Node Definitions

### Node 1 — The Check-In

| Field | Value |
|---|---|
| Send date | 2026-04-28 |
| Send time | 10 am contact's local timezone; default to PT if timezone unknown |
| Audience at entry | Full lapsed segment, est. 12,400 |
| Audience after suppression | Est. ~12,000 (see Suppression Summary) |
| Template | `email-design/03-pages/starter-single-column/` |
| Copy source | `copywriting-archive/spring-reengagement-2026-copy.json` → `"email": 1` |
| Rendered HTML | `rendered/spring-reengagement-2026/the-check-in.html` |
| Channel | Email |
| A/B test | Yes — Test 1 (see A/B Test Summary) |
| Offer in email | No — re-open only, no discount in this send |
| Legal copy required | No |

**Subject lines:**
- Variant A (50%): `{{first_name}}, it's been a while`
- Variant B (50%): `Something new is waiting for you`
- Winner declared: 2026-04-29 at 10 am PT on unique open rate at 24 hours

**Preview text:** Take a look at what's new — we think you'll find something worth coming back for.

**Suppression applied:**
- Global opt-out list
- Hard bounces and spam complainers
- Purchased in last 30 days
- Unengaged > 180 days (diverted to sunset flow)
- Duplicates in segment export

**UTM parameters:**
| Parameter | Value |
|---|---|
| utm_source | email |
| utm_medium | lifecycle |
| utm_campaign | spring-reen-2026 |
| utm_content | email-1-cta |

**CTA destination:** `/new-arrivals?utm_source=email&utm_medium=lifecycle&utm_campaign=spring-reen-2026&utm_content=email-1-cta`

**Exit conditions:**
- Purchased before or on send date → remove from series
- Unsubscribed after send → remove from series; add to global opt-out
- Spam complaint after send → remove from series; add to complaint suppression

**Branch logic:**
| Behavior (24-hr window post-send) | Next action |
|---|---|
| Purchased | Exit series immediately |
| Opened, did not click | Trigger Node 2 within 24 hrs of open event |
| Opened and clicked (no purchase) | Trigger Node 2 within 24 hrs of open event |
| Not opened after 72 hrs | Trigger Node 2 on 2026-05-01 |

---

### Node 2 — The Offer

| Field | Value |
|---|---|
| Send date | 2026-04-29 (openers-no-click batch) / 2026-05-01 (non-opener batch) |
| Send time | 10 am contact's local timezone |
| Audience at entry | Openers-no-click + non-openers from Node 1; est. ~11,000 |
| Audience after suppression | Est. ~10,800 (Node 1 purchases and unsubs removed) |
| Template | `email-design/03-pages/starter-single-column/` |
| Copy source | `copywriting-archive/spring-reengagement-2026-copy.json` → `"email": 2` |
| Rendered HTML | `rendered/spring-reengagement-2026/the-offer.html` |
| Channel | Email |
| A/B test | None |
| Offer in email | Yes — 15% off next order, no code, applied at checkout, expires 2026-05-12 |
| Legal copy required | Yes |

**Subject line:** `Your exclusive 15% is ready, {{first_name}}`

**Preview text:** Your exclusive 15% discount is waiting — no code needed, applied at checkout.

**Legal copy (footer):** 15% off one order. Single use. Expires 2026-05-12. Exclusions apply.
[Link to full T&Cs required — URL to be confirmed by Sam Patel (Legal) by 2026-04-16]

> ⚠ **Blocker:** Legal sign-off from Sam Patel required before this node can be activated. Due 2026-04-16.

**Suppression applied:**
- All suppressions inherited from Node 1
- Contacts who purchased after Node 1 send
- Contacts who unsubscribed after Node 1 send

**UTM parameters:**
| Parameter | Value |
|---|---|
| utm_source | email |
| utm_medium | lifecycle |
| utm_campaign | spring-reen-2026 |
| utm_content | email-2-cta |

**CTA destination:** `/offers/reengagement-15?utm_source=email&utm_medium=lifecycle&utm_campaign=spring-reen-2026&utm_content=email-2-cta`

> ⚠ **Dependency:** Landing page at `/offers/reengagement-15` must be live before this node sends. Owner: Sam Patel (Web), due 2026-04-25.

**Exit conditions:**
- Purchased within 5 days of send → exit series
- Unsubscribed → exit series; add to global opt-out
- Spam complaint → exit series; add to complaint list

**Branch logic:**
| Behavior (5-day window post-send) | Next action |
|---|---|
| Purchased | Exit series immediately |
| No purchase within 5 days | Trigger Node 3 (5 days after this send date) |
| Unsubscribed | Exit series; no Node 3 |

---

### Node 3 — Last Chance

| Field | Value |
|---|---|
| Send date | 2026-05-04 (for contacts who received Node 2 on 2026-04-29) / 2026-05-06 (for contacts who received Node 2 on 2026-05-01) |
| Send time | 10 am contact's local timezone |
| Hard deadline | All sends must complete before 2026-05-12 11:59 pm PT — do not send after offer expires |
| Audience at entry | Node 2 recipients who did not purchase; est. ~10,600 |
| Template | `email-design/03-pages/starter-single-column/` |
| Copy source | `copywriting-archive/spring-reengagement-2026-copy.json` → `"email": 3` |
| Rendered HTML | `rendered/spring-reengagement-2026/last-chance.html` |
| Channel | Email |
| A/B test | None |
| Offer in email | Yes — 15% off, expires tonight at 11:59 pm PT |
| Legal copy required | Yes — same terms as Node 2 |

**Subject line:** `{{first_name}}, your 15% expires tonight`

**Preview text:** Your 15% off expires at 11:59 pm PT tonight. Don't let it go — it won't come back.

**Legal copy (footer):** 15% off one order. Single use. Expires 2026-05-12. Exclusions apply.

> ⚠ **Copy dependency:** Subject line and body copy reference "tonight" and "11:59 pm PT tonight." This email must send on 2026-05-12. If the 5-day interval from Node 2 produces a send date after 2026-05-12, move send date to 2026-05-12 and review copy to confirm date references remain accurate.

**Suppression applied:**
- All suppressions inherited from Nodes 1 and 2
- Contacts who purchased after Node 2 send

**UTM parameters:**
| Parameter | Value |
|---|---|
| utm_source | email |
| utm_medium | lifecycle |
| utm_campaign | spring-reen-2026 |
| utm_content | email-3-cta |

**CTA destination:** `/offers/reengagement-15?utm_source=email&utm_medium=lifecycle&utm_campaign=spring-reen-2026&utm_content=email-3-cta`

**Exit conditions:**
- Purchased → exit series (converted)
- No action → exit series; flag contact for sunset evaluation
- Unsubscribed → exit series; add to global opt-out

---

## A/B Test Summary

| # | Node | Variable | Variant A | Variant B | Split | Winner criteria | Decision date | Fallback |
|---|---|---|---|---|---|---|---|---|
| 1 | Node 1 | Subject line angle | `{{first_name}}, it's been a while` | `Something new is waiting for you` | 50 / 50 | Higher unique open rate at 24 hrs post-send | 2026-04-29, 10 am PT | No statistically significant winner → send Variant A to any remainder (warm recognition is lower-risk for re-engagement; see brief Section 12) |

**Configuration requirements:**
- Variant assignment must be stable per contact. The same contact must always receive the same variant if reprocessed.
- Do not declare a winner before 24 hours, regardless of early data.
- Record winning variant in post-campaign notes (brief Section 17) to inform future re-engagement subject line strategy.
- Nodes 2 and 3 have fixed subject lines — A/B winner does not carry forward.

---

## Tracking and Attribution

| Field | Value |
|---|---|
| UTM source | `email` |
| UTM medium | `lifecycle` |
| UTM campaign | `spring-reen-2026` |
| UTM content convention | `email-{n}-{element}` (e.g. `email-1-cta`, `email-2-cta`) |
| Attribution window | 7 days post-click |
| Revenue attribution model | Last click |
| Reporting dashboard | Looker — CRM Campaign Performance dashboard |
| Reporting cadence | Daily during send window; weekly post-series close |

**Full UTM strings per node:**

| Node | CTA destination with UTM |
|---|---|
| 1 | `/new-arrivals?utm_source=email&utm_medium=lifecycle&utm_campaign=spring-reen-2026&utm_content=email-1-cta` |
| 2 | `/offers/reengagement-15?utm_source=email&utm_medium=lifecycle&utm_campaign=spring-reen-2026&utm_content=email-2-cta` |
| 3 | `/offers/reengagement-15?utm_source=email&utm_medium=lifecycle&utm_campaign=spring-reen-2026&utm_content=email-3-cta` |

**Metrics to track per email:**
- Unique open rate (primary engagement signal)
- Click-to-open rate (CTOR)
- Unique click rate
- Conversion rate (purchases ÷ recipients)
- Revenue per email (RPE)
- Unsubscribe rate
- Spam complaint rate

**Series-level metric:**
- Re-engagement rate: % of original segment (12,400) that opens or clicks at least one email in the series. Target: 12% (≥ 1,488 contacts).

---

## Suppression Summary

### Global suppressions (applied before every node)

| Rule | Action |
|---|---|
| Global opt-out / unsubscribe list | Exclude entirely — do not send |
| Hard bounce list | Exclude entirely — do not send |
| Spam complaint list | Exclude entirely — do not send |

### Campaign entry suppressions (applied at segment build before Node 1)

| Rule | Reason |
|---|---|
| Purchased in last 30 days | Active customers don't need re-engagement; offer is irrelevant |
| Unengaged > 180 days | Beyond re-engagement window — route to sunset flow instead |
| No prior purchase | Inclusion criterion requires ≥ 1 purchase; these contacts don't qualify |
| Opened or clicked in last 89 days | Not lapsed; inclusion criterion requires 90+ day no-open |

### Mid-series suppression (checked before each subsequent node)

| Trigger | Action |
|---|---|
| Purchase event after any node | Remove from all remaining nodes immediately |
| Unsubscribe after any node | Remove from remaining nodes; add to global opt-out list |
| Spam complaint after any node | Remove from remaining nodes; add to complaint suppression list |
| Hard bounce on any send | Remove from remaining nodes; update bounce record in CRM |

### Overrides

None. No overrides to global suppression or campaign-entry suppression rules have been granted for this campaign.

---

## Frequency Cap Check

**Global cap (brief Section 7.1):** Maximum 5 emails per 7-day rolling window per contact.
**Cap override rule (brief Section 7.1):** If a contact is at cap, delay their next send in this series by 1 day.

| Scenario | Max emails in any 7-day window | Within cap? |
|---|---|---|
| Contact receives Nodes 1 + 2 only (Days 0 and 3) | 2 | Yes |
| Contact receives Nodes 1, 2, 3 (Days 0, 3, 8) | 2 in first 7 days; 1 in second | Yes |
| Contact receives Nodes 2 + 3 via openers-no-click path (Days 1 and 6) | 2 | Yes |
| Contact is simultaneously in another active campaign | Unknown — must verify at send time | Check in ESP |

**Cross-campaign risk:** The global cap of 5/7 days is unlikely to be reached within this series alone (maximum 3 emails over ~8 days). The risk is contacts who are simultaneously active in a transactional campaign (order confirmation, shipping updates). Verify combined 7-day send count in the ESP before activating each node. Per the brief, delay by 1 day if at cap — do not suppress entirely.

---

## Integration Touchpoints

| System | Node | Required action | Owner | Due |
|---|---|---|---|---|
| CRM — segment export | Before Node 1 | Export lapsed segment; validate final count against 12,400 estimate; exclude GDPR contacts without current consent | Maya Chen (CRM) | 2026-04-20 |
| E-commerce — discount | Before Node 2 | Configure 15% auto-apply discount; confirm it expires 2026-05-12 at 11:59 pm PT; test at checkout | Sam Patel (Web) | 2026-04-25 |
| Web — landing page | Before Node 2 | `/offers/reengagement-15` must be live and linked to correct discount; mobile-optimised | Sam Patel (Web) | 2026-04-25 |
| Legal — T&Cs copy | Before Node 2 | Sign off on "15% off one order. Single use. Expires 2026-05-12. Exclusions apply." and full T&Cs page URL | Sam Patel (Legal) | 2026-04-16 |
| ESP — A/B test config | Before Node 1 | Configure 50/50 subject line split; set winner-declaration trigger at 24 hrs on unique open rate | Orchestration operator | 2026-04-25 |
| ESP — suppression sync | Before each node | Confirm purchase events and unsubscribes sync from e-commerce to ESP suppression list with < 1 hr lag | Orchestration operator | Before each send |
| Looker — dashboard | After Node 1 | Verify UTM data is flowing into CRM Campaign Performance dashboard; confirm unique open rate metrics are tracking by variant | Reporting team | 2026-04-29 |
| CRM — post-series flag | After Node 3 | Flag non-openers across all 3 sends for sunset evaluation | Maya Chen (CRM) | 2026-05-14 |

---

## Approval

| Role | Name | Approved | Date |
|---|---|---|---|
| Orchestration owner | Maya Chen | — | — |
| Legal / Compliance | Sam Patel | No — pending review of Nodes 2 and 3 offer copy | Due 2026-04-16 |
| Marketing lead | Robin Okafor | — | — |
