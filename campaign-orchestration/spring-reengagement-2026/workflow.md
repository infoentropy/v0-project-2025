# Workflow: Spring Re-engagement 2026

# campaign:  CMP-2026-Q2-REEN
# brief:     campaign-strategy/spring-reengagement-2026-brief.md  (Approved 2026-04-10)
# copy:      copywriting-archive/spring-reengagement-2026-copy.json
# status:    Draft — legal sign-off pending (Sam Patel, due 2026-04-16)

```python
segment = crm.query(
    subscribed_gte_6_months=True,
    prior_purchases_gte=1,
    last_open_days_between=(90, 180),
    exclude=["opted_out", "hard_bounce", "spam_complaint",
             "purchased_last_30_days", "unengaged_gt_180_days"]
)
# est. 12,400 → ~12,000 after suppression
# unengaged_gt_180_days → route to sunset flow instead


# ── NODE 1: The Check-In  ──────────────────────────  2026-04-28, 10 am local
ab_test(
    variant_A = "{{first_name}}, it's been a while",   # 50%
    variant_B = "Something new is waiting for you",     # 50%
    winner_by = "unique_open_rate",
    decide_at  = "2026-04-29 10:00 PT",
    fallback   = variant_A
)
send(email=1, to=segment,
     cta_url="/new-arrivals?utm_source=email&utm_medium=lifecycle"
             "&utm_campaign=spring-reen-2026&utm_content=email-1-cta")

for contact in segment:
    if contact.purchased:
        exit_series(contact)
    elif contact.opened and not contact.clicked:
        schedule(node_2, contact, delay="24h")   # openers-no-click batch
    elif not contact.opened:
        schedule(node_2, contact, date="2026-05-01")  # non-opener batch
    if contact.unsubscribed or contact.spam_complaint:
        exit_series(contact); suppress_globally(contact)


# ── NODE 2: The Offer  ────────────────────────────  2026-04-29 / 2026-05-01
# BLOCKER: legal sign-off required before activating (Sam Patel, 2026-04-16)
# BLOCKER: /offers/reengagement-15 must be live (Sam Patel, 2026-04-25)
send(email=2, to=node_2_audience,   # est. ~11,000
     legal_footer="15% off one order. Single use. Expires 2026-05-12. Exclusions apply.",
     cta_url="/offers/reengagement-15?utm_source=email&utm_medium=lifecycle"
             "&utm_campaign=spring-reen-2026&utm_content=email-2-cta")

for contact in node_2_audience:
    if contact.purchased:
        exit_series(contact)
    else:
        schedule(node_3, contact, delay="5d")
    if contact.unsubscribed or contact.spam_complaint:
        exit_series(contact); suppress_globally(contact)


# ── NODE 3: Last Chance  ──────────────────────────  2026-05-04 / 2026-05-06
# NOTE: copy says "expires tonight" — send date must be 2026-05-12 at latest
# NOTE: hard deadline 2026-05-12 11:59 pm PT; do not send after offer expires
send(email=3, to=node_3_audience,   # est. ~10,600
     legal_footer="15% off one order. Single use. Expires 2026-05-12. Exclusions apply.",
     cta_url="/offers/reengagement-15?utm_source=email&utm_medium=lifecycle"
             "&utm_campaign=spring-reen-2026&utm_content=email-3-cta")

for contact in node_3_audience:
    if contact.purchased:
        exit_series(contact)
    else:
        exit_series(contact); flag_for_sunset(contact)
    if contact.unsubscribed or contact.spam_complaint:
        exit_series(contact); suppress_globally(contact)


# ── FREQUENCY CAP  ────────────────────────────────────────────────────────────
# global cap: 5 emails / 7-day window
# this series max: 3 emails over ~8 days → no violation within series alone
# cross-campaign risk: verify combined 7-day count in ESP before each node
if contact.emails_in_last_7_days >= 5:
    delay(node_next, days=1)   # do not suppress — just push by 1 day


# ── A/B TEST  ──────────────────────────────────────────────────────────────────
# node_1 only; nodes 2 and 3 have fixed subject lines
# variant assignment is stable per contact (hash-based, not random at send time)
# winner declared 2026-04-29 10:00 PT on unique open rate; no early calls


# ── ATTRIBUTION  ───────────────────────────────────────────────────────────────
# model:   last click
# window:  7 days post-click
# report:  Looker / CRM Campaign Performance dashboard
# target:  12% re-engagement rate (≥ 1,488 of 12,400 open or click ≥ 1 email)


# ── BLOCKERS / DEPENDENCIES  ───────────────────────────────────────────────────
# 2026-04-16  Sam Patel (Legal)   — sign off on offer copy + T&Cs URL
# 2026-04-20  Maya Chen (CRM)     — validate segment export count
# 2026-04-25  Sam Patel (Web)     — discount configured + landing page live
# 2026-04-25  operator            — A/B test configured in ESP
# 2026-05-14  Maya Chen (CRM)     — flag non-openers for sunset


# ── APPROVAL  ──────────────────────────────────────────────────────────────────
# Maya Chen (orchestration)  pending
# Sam Patel (legal)          pending — due 2026-04-16
# Robin Okafor (marketing)   pending
```
