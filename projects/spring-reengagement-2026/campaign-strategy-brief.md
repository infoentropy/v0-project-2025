# Email Strategy Brief

---

## 1. Campaign Overview

| Field | Value |
|---|---|
| Campaign name | Spring Re-engagement 2026 |
| Campaign code / ID | CMP-2026-Q2-REEN |
| Campaign type | Re-engagement / win-back |
| Primary channel | Email |
| Supporting channels | Email only |
| Brief owner | Maya Chen, CRM Manager |
| Stakeholders | Jordan Lee (Brand), Sam Patel (Legal), Robin Okafor (Marketing Lead) |
| Brief status | Approved |
| Brief approved by | Robin Okafor |
| Brief approved date | 2026-04-10 |

---

## 2. Campaign Dates

| Milestone | Date |
|---|---|
| Brief approved | 2026-04-10 |
| Copy due | 2026-04-17 |
| Design due | 2026-04-17 |
| Build / QA due | 2026-04-22 |
| First send date | 2026-04-28 |
| Last send date | 2026-05-12 |
| Post-campaign analysis due | 2026-05-26 |

---

## 3. Business Objective

**Objective:** Reactivate subscribers who have not opened or clicked any email in the past 90–180 days and convert at least a portion back to active purchasers before removing them from the main list.

**Why now:** Q2 historically outperforms Q1 for re-engagement due to the seasonal mindset shift in spring. List hygiene is also due — unresponsive subscribers are hurting deliverability scores. Acting now recovers revenue before the larger summer promotional calendar begins.

---

## 4. Target Audience

### 4.1 Primary Segment

| Field | Value |
|---|---|
| Segment name | Lapsed purchasers — 90-180 day no-open |
| Segment size (est.) | 12,400 contacts |
| List source | CRM — behavioral engagement data, last-open timestamp |
| Inclusion criteria | Subscribed ≥ 6 months; at least one prior purchase; no email open or click in 90–180 days |
| Exclusion criteria | Opened or clicked anything in the last 89 days; never purchased; suppressed for complaints or hard bounces |
| Suppression rules | Suppress if purchased in last 30 days; suppress unengaged > 180 days (move to sunset flow instead); suppress on global opt-out list |

### 4.2 Secondary Segment _(if applicable)_

| Field | Value |
|---|---|
| Segment name | N/A — single-segment campaign |
| Segment size (est.) | — |
| Inclusion criteria | — |
| Exclusion criteria | — |

### 4.3 Audience Insights

- **Pain points:** Inbox is noisy; previous emails may have felt irrelevant or too frequent. Price sensitivity is likely elevated for those who haven't purchased recently.
- **Motivations:** They bought once, which means the brand resonated. A relevant offer or a moment of recognition ("we noticed you've been away") can reactivate goodwill.
- **Where they are in the funnel:** Past the awareness and consideration stages — these are lapsed customers, not prospects. Message should skip re-introduction and focus on re-incentivising.
- **Past campaign behavior:** This segment's last known open rate was 18% before lapse. The last re-engagement attempt (Q4 2025) achieved a 9% re-open rate and 2.1% conversion among openers. That campaign used a 20% discount — this campaign will test a smaller offer (15%) to protect margin.

---

## 5. Goals and Success Metrics

### 5.1 Primary Goal

**Primary goal:** Reactivate lapsed subscribers — defined as achieving at least one open or click across the three-email series.

**Primary metric:** Re-engagement rate (% of segment that opens or clicks at least one email in the series)

**Target:** 12% re-engagement rate (≥ 1,488 contacts reactivated)

### 5.2 Secondary Metrics

| Metric | Baseline | Target |
|---|---|---|
| Open rate | 9% (Q4 2025 re-engagement) | 14% on Email 1 |
| Click-to-open rate (CTOR) | 11% | 16% |
| Click rate | 1.0% | 2.2% |
| Conversion rate | 2.1% among openers | 2.8% among openers |
| Revenue per email (RPE) | $0.38 | $0.55 |
| Unsubscribe rate | 0.6% | ≤ 0.5% |
| Spam complaint rate | 0.04% | ≤ 0.03% |

### 5.3 What "success" looks like

A successful outcome means roughly 1,500 previously silent customers have re-engaged with the brand, with ~400 of them making a purchase. Equally important: the remaining non-openers are cleanly flagged for sunset, which improves deliverability for the active list going into the summer promotional window.

---

## 6. Messaging Hierarchy

### 6.1 Primary Message
We noticed you've been away — here's a reason to come back.

### 6.2 Secondary Messages

1. We've added new products since you last visited — there's something worth seeing.
2. As a returning customer, you're getting an exclusive offer not available to the general list.
3. The offer expires — this isn't a permanent discount, so now is the time.
4. Your account and past order history are still here — picking up is easy.
5. If our emails aren't right for you anymore, you're in control of that too.

### 6.3 Tertiary Messages
- Brief mention of any new collections or bestsellers launched since the subscriber's last visit.
- Reminder of free shipping threshold if relevant to the offer email.

### 6.4 Tone and Voice

- **Overall tone:** Warm and direct. Acknowledges the gap without guilt-tripping. Confident that there's value on offer, not desperate.
- **Tone to avoid:** Pushy, apologetic, overly casual ("Hey!!"), or corporate-formal.
- **Words / phrases to use:** "We noticed," "welcome back," "exclusive," "still here," "picked this for you"
- **Words / phrases to avoid:** "You haven't opened our emails" (accusatory), "FINAL WARNING" (aggressive), "just" (weakens the offer), "amazing deal" (generic)

---

## 7. Email Series Plan

_The **Design template** column must be filled in before this brief is approved
for copywriting. Each value must be a path to an existing folder under
`email-design/03-pages/`._

| # | Email name | Send trigger / timing | Audience | Subject line direction | Primary CTA | Goal | Design template |
|---|---|---|---|---|---|---|---|
| 1 | The Check-In | 2026-04-28, batch send at 10 am local | Full lapsed segment (12,400) | Warm recognition — no offer yet. Curiosity hook. | View new arrivals | Re-open the relationship; measure who re-engages | `email-design/03-pages/starter-single-column/` |
| 2 | The Offer | 3 days after Email 1 non-openers; immediate for openers who did not click | Non-openers from Email 1 + openers who did not click (~11,000 est.) | Exclusive offer reveal. Urgency starts here. | Claim your 15% off | Drive first click and conversion with the offer | `email-design/03-pages/starter-single-column/` |
| 3 | Last Chance | 5 days after Email 2; send only to non-converters | Anyone who received Email 2 and did not purchase (~10,600 est.) | Offer expiry. Final nudge. | Use your discount — expires tonight | Convert remaining fence-sitters before offer expires | `email-design/03-pages/starter-single-column/` |

### 7.1 Cadence rules
- Minimum days between sends to same recipient: 3 days
- Maximum emails in this series: 3
- Global frequency cap interaction: This series respects the global cap of 5 emails per 7-day window. If a contact is already at cap, delay their next send in this series by 1 day.

### 7.2 Design template status

| # | Design template path | Template status | Copy unblocked? |
|---|---|---|---|
| 1 | `email-design/03-pages/starter-single-column/` | Ready | Yes |
| 2 | `email-design/03-pages/starter-single-column/` | Ready | Yes |
| 3 | `email-design/03-pages/starter-single-column/` | Ready | Yes |

---

## 8. Offer and CTA Strategy

| Field | Value |
|---|---|
| Offer / incentive | 15% off next purchase — exclusive to this re-engagement segment |
| Offer expiry | 2026-05-12 at 11:59 pm PT (Email 1 has no offer; offer introduced in Email 2) |
| Primary CTA label | Email 1: "See what's new" / Email 2: "Claim your 15% off" / Email 3: "Use your discount" |
| Primary CTA destination URL | Email 1: /new-arrivals?utm_campaign=spring-reen-2026&utm_content=email-1-cta / Emails 2–3: /offers/reengagement-15?utm_campaign=spring-reen-2026 |
| Secondary CTA label _(if any)_ | None |
| Secondary CTA destination URL | None |
| Post-click landing page owner | Sam Patel (Web team) — landing page must be live by 2026-04-25 |

---

## 9. Subject Line and Preview Text Direction

- **Angle / hook:** Email 1 — soft recognition (curiosity, warmth). Email 2 — exclusive offer reveal (value, mild urgency). Email 3 — expiry deadline (scarcity, urgency).
- **Personalization tokens to use:** First name in subject line for Emails 1 and 3; not required for Email 2 where offer framing carries more weight.
- **Character target:** Subject ≤ 50 chars; preview text ≤ 90 chars
- **Emojis:** Brand discretion — one emoji max per subject line if it reinforces the message; none in preview text
- **Examples of the right tone:**
  1. "{{first_name}}, it's been a while" (Email 1 — warm, not accusatory)
  2. "Something new is waiting for you" (Email 1 — curiosity)
  3. "Your exclusive 15% off — just for you" (Email 2 — offer)
  4. "This offer was made for you, {{first_name}}" (Email 2 — personalised)
  5. "Last day: your 15% discount expires tonight" (Email 3 — deadline)

---

## 10. Design Direction

_Per-email template assignments live in Section 7.2. Use this section for campaign-wide mood and layout guidance only._

- **Layout:** Single column throughout the series for maximum mobile readability and rendering consistency across the lapsed segment's likely varied email clients.
- **Hero image / visual:** Email 1 — lifestyle image from new arrivals collection. Email 2 — offer-focused graphic with the 15% figure prominent. Email 3 — same offer graphic with an urgency treatment (e.g. countdown or bold expiry date).
- **Brand mood:** Clean and confident. Spring palette — light backgrounds, warm accent color for CTA buttons. Not cluttered.
- **Mobile priority notes:** CTA button must be at least 44px tall and full-width on mobile. Hero image must be swapped for a mobile-optimised crop on screens < 480px.

---

## 11. Personalization and Dynamic Content

| Element | Personalization type | Fallback if data missing |
|---|---|---|
| Subject line | First name token (`{{first_name}}`) | Omit token — subject line reads without it |
| Hero image | Static (no personalisation for this series) | N/A |
| Body copy block | Static | N/A |
| Product recommendations | None in this series — category-level only | N/A |
| CTA | Static per email | N/A |

---

## 12. A/B Test Plan

| Test # | Email # | Variable | Variant A | Variant B | Split | Winner criteria | Decision date |
|---|---|---|---|---|---|---|---|
| 1 | 1 | Subject line angle | Warm recognition ("{{first_name}}, it's been a while") | Curiosity / product hook ("Something new is waiting for you") | 50/50 | Higher unique open rate at 24 hours post-send | 2026-04-29 |

---

## 13. Tracking and Attribution

| Field | Value |
|---|---|
| UTM source | email |
| UTM medium | lifecycle |
| UTM campaign | spring-reen-2026 |
| UTM content convention | `email-{n}-{element}` e.g. `email-1-hero-cta`, `email-2-hero-cta` |
| Attribution window | 7 days post-click |
| Revenue attribution model | Last click |
| Reporting dashboard / tool | Looker — CRM Campaign Performance dashboard |

---

## 14. Legal and Compliance

- **CAN-SPAM / CASL / GDPR applicable:** Yes — all three may apply depending on subscriber country. GDPR contacts require a valid prior consent record; confirm with Legal before send.
- **Unsubscribe mechanism:** Standard footer with one-click unsubscribe link
- **Required legal copy:** Standard unsubscribe footer; company name and physical address required per CAN-SPAM.
- **Promotional terms and conditions link:** Required on Emails 2 and 3 — "15% off one order. Single use. Expires 2026-05-12. Exclusions apply." Link to full T&Cs page.
- **Legal review required:** Yes — Owner: Sam Patel — Due: 2026-04-16

---

## 15. Dependencies and Risks

| Item | Owner | Due date | Status |
|---|---|---|---|
| Offer landing page live at /offers/reengagement-15 | Sam Patel (Web) | 2026-04-25 | In progress |
| Discount code configured and tested in e-commerce platform | Sam Patel (Web) | 2026-04-25 | Not started |
| Legal review of T&Cs copy and footer | Sam Patel (Legal) | 2026-04-16 | Not started |
| Hero images sourced and approved by brand | Jordan Lee (Brand) | 2026-04-17 | In progress |
| Segment query validated in CRM against 12,400 estimate | Maya Chen (CRM) | 2026-04-20 | Not started |

**Known risks:**
- Segment size may be smaller than 12,400 once GDPR contacts without current consent are excluded. Targets may need to be revised downward.
- If the landing page is delayed past 2026-04-25, Email 1 send must also be pushed to protect user experience.

**Contingency plan if first send is delayed:** Push entire series by the same number of days, preserving the 3-day and 5-day intervals. Notify Robin Okafor immediately if delay exceeds 3 days, as the series would then conflict with the May promotional calendar.

---

## 16. Approvals

| Role | Name | Approved | Date |
|---|---|---|---|
| Campaign strategist | Maya Chen | Yes | 2026-04-10 |
| Copywriter | TBD — Owner: Maya Chen | No | Due: 2026-04-17 |
| Designer | TBD — Owner: Jordan Lee | No | Due: 2026-04-17 |
| Legal / Compliance | Sam Patel | No | Due: 2026-04-16 |
| Marketing lead | Robin Okafor | Yes | 2026-04-10 |

---

## 17. Post-Campaign Notes

_Fill in after the campaign completes. Archive this completed brief in `campaign-strategy/_archive/` once the post-mortem is done._

- **What worked:**
- **What didn't:**
- **Recommendations for next time:**
- **Data / assets to carry forward:**
