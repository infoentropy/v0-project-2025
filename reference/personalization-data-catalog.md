# Personalization Data Catalog

This document is the authoritative reference for all data fields available to
the Campaign Orchestration skill. Use it when writing workflow branching logic
(`workflow.md`) and when resolving `{{variables}}` in HTML templates.

---

## User Properties

These fields are attributes of a contact record. They are available for both
HTML template substitution (`{{property_name}}`) and as conditions in workflow
`if/else` branching.

| Property | Type | Description | Example Values |
|---|---|---|---|
| `first_name` | string | Contact's given name | `"Maria"`, `"James"` |
| `country` | string | ISO 3166-1 alpha-2 country code | `"US"`, `"DE"`, `"BR"` |
| `language` | string | BCP 47 language tag | `"en"`, `"es"`, `"pt-BR"` |
| `subscription_expires_at` | ISO 8601 datetime | Timestamp when the contact's subscription lapses | `"2026-07-15T23:59:59Z"` |
| `favorite_content` | string | Category tag of the content the contact engages with most | `"sports"`, `"finance"`, `"cooking"` |
| `last_purchase_date` | ISO 8601 date | Date of most recent completed purchase | `"2026-01-22"` |

### Usage in HTML Templates

Reference user properties with double-curly-brace syntax:

```html
<p>Hi {{first_name}},</p>
<p>Your subscription expires on {{subscription_expires_at}}.</p>
```

The render script (`scripts/render-email-html.py`) substitutes these tokens at
build time. Any unresolved token surfaces as a warning in the render output —
treat all warnings as blockers before handoff.

### Usage in Workflow Logic

Reference user properties directly on the `contact` object:

```python
if contact.subscription_expires_at <= days_from_now(7):
    schedule(renewal_reminder_node, contact, delay="0h")

if contact.country == "DE":
    send(email="gdpr-variant", to=contact)

if contact.language == "es":
    send(email="es-variant", to=contact)
else:
    send(email="en-default", to=contact)
```

---

## Events

Events are timestamped records of actions a contact has taken. They drive
trigger conditions and branching logic in workflows. Events are **not** used
for HTML substitution — they are workflow-only signals.

### Email Events

| Event | Key Properties | Description |
|---|---|---|
| `email.sent` | `email_id`, `timestamp` | ESP confirmed the message was dispatched |
| `email.opened` | `email_id`, `timestamp`, `device_type` | Recipient opened the email |
| `email.clicked` | `email_id`, `link_url`, `timestamp` | Recipient clicked a tracked link |

### Commerce Events

| Event | Key Properties | Description |
|---|---|---|
| `purchase.completed` | `order_id`, `amount`, `currency`, `timestamp` | A transaction was finalized |

### App / Web Events

| Event | Key Properties | Description |
|---|---|---|
| `app.opened` | `platform`, `timestamp` | Contact launched the mobile or desktop app |
| `page.viewed` | `url`, `page_title`, `timestamp` | Contact loaded a tracked web page |

### Usage in Workflow Logic

Events are accessed via `contact.events` or as shorthand boolean/date helpers:

```python
# Shorthand helpers (preferred for common checks)
if contact.purchased:
    exit_series(contact)

if contact.opened and not contact.clicked:
    schedule(click_nudge_node, contact, delay="24h")

if not contact.opened:
    schedule(resend_node, contact, delay="3d")

# Event inspection for richer conditions
last_open = contact.events.last("email.opened")
if last_open and last_open.days_ago > 90:
    tag(contact, "lapsed")

if contact.events.count("purchase.completed", within="30d") >= 2:
    tag(contact, "repeat-buyer")

if contact.events.occurred("app.opened", within="7d"):
    # Contact is recently active — safe to send
    schedule(next_node, contact, delay="0h")

if contact.events.occurred("page.viewed", url_contains="/pricing"):
    schedule(pricing_follow_up_node, contact, delay="1h")
```

---

## Personalization Checklist

Before finalizing any `workflow.md` or rendered HTML, verify:

- [ ] Every `{{token}}` in HTML templates maps to a property listed above.
- [ ] Every workflow branch condition references a property or event listed above.
- [ ] Locale variants are gated on `contact.language` or `contact.country` where copy differs.
- [ ] Expiry-based sends check `contact.subscription_expires_at` with an appropriate lead time.
- [ ] Engagement branches use `contact.opened`, `contact.clicked`, and/or `contact.purchased` for exit logic.
- [ ] Any field not listed here is flagged with a `# BLOCKER:` comment and escalated to the data team.
