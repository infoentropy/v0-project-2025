# Skill: Campaign Orchestration

Produces the artifacts needed to launch a campaign. Run subtasks in whatever order fits your production state.

**Inputs:** an approved brief at `projects/<slug>/campaign-strategy-brief.md`, and a copy JSON in `copywriting-archive/` for subtask 4.
**Outputs:** land in `projects/<slug>/`.

**Required reference — read before any subtask:**
`campaign-orchestration/personalization-data-catalog.md` — the authoritative
list of user properties and events available for HTML template tokens and
workflow branching. Every `{{variable}}` in an HTML template and every
`contact.*` condition in a workflow **must** map to a field defined there. If a
needed field is absent, add a `# BLOCKER:` comment and flag it rather than
inventing a field name.

---

## Subtask 1 · Build Send Sequence

Read the brief (sections 4 and 7), `suppression-rules.md`, `frequency-capping-rules.md`, and `channel-priority-rules.md`. Map each email in the series to a send node: trigger, audience after suppression, branching logic, and exit conditions.

Write the result to `projects/<slug>/orchestration.md` as a single Python code block. Use `send()` calls for each node, `if/else` per contact for branching, `# BLOCKER:` comments above any send that has an unmet dependency, UTMs as inline `cta_url=` arguments, and `# comment sections` for suppression, frequency cap, attribution, and approvals. No tables. No ASCII diagrams.

```python
segment = crm.query(inclusion_criteria, exclude=[...])

# ── NODE 1: <Email Name>  ──────────────────────  <send date>
send(email=1, to=segment, cta_url="/<path>?utm_source=email&...")

for contact in segment:
    if contact.purchased:
        exit_series(contact)
    elif contact.opened and not contact.clicked:
        schedule(node_2, contact, delay="24h")
    elif not contact.opened:
        schedule(node_2, contact, delay="3d")
    if contact.unsubscribed or contact.spam_complaint:
        exit_series(contact); suppress_globally(contact)

# ── NODE 2: <Email Name>  ──────────────────────  <send date>
# BLOCKER: <dependency> — <owner>, due <date>
send(email=2, to=node_2_audience, cta_url="/<path>?utm_source=email&...")

for contact in node_2_audience:
    if contact.purchased:
        exit_series(contact)
    else:
        schedule(node_3, contact, delay="5d")
    if contact.unsubscribed or contact.spam_complaint:
        exit_series(contact); suppress_globally(contact)

# ── FREQUENCY CAP  ─────────────────────────────────────────
if contact.emails_in_last_7_days >= CAP:
    delay(next_node, days=1)

# ── ATTRIBUTION  ───────────────────────────────────────────
# model: last click  |  window: 7 days post-click

# ── BLOCKERS / DEPENDENCIES  ───────────────────────────────
# <date>  <owner>  — <what is needed>

# ── APPROVAL  ──────────────────────────────────────────────
# <role>  <name>  pending / approved <date>
```

---

## Subtask 2 · Configure A/B Tests

Read the brief (section 12) and `ab-test-standards.md`. For each test, confirm variant labels match options in the copy JSON. Record variable, split, winner criteria, decision date, and fallback. Append to the workflow as a `# ── A/B TEST` comment section.

---

## Subtask 3 · Define Tracking and Attribution

Read the brief (sections 8 and 13). Build UTM strings per email and confirm the attribution window. Append to the workflow as a `# ── ATTRIBUTION` comment section. UTM strings also go inline as `cta_url=` args on each `send()` call.

---

## Subtask 4 · Render ESP-Ready HTML

Run `python campaign-orchestration/scripts/render-email-html.py copywriting-archive/<slug>-copy.json`. The script reads each email's template and schema, substitutes `{{variables}}` with copy values, and warns on unresolved URI fields. Output goes to `projects/<slug>/templates/rendered/` (gitignored).

---

## Subtask 5 · Validate and Handoff

Confirm the brief is approved, every rendered HTML has no unresolved `{{tokens}}`, every send node has an exit condition, A/B tests have winner criteria, UTMs are on all links, and suppression is documented. Record sign-off in the workflow's `# ── APPROVAL` section.
