# Skill: Campaign Orchestration

```python
# inputs
brief   = "campaign-strategy/<slug>-brief.md"   # must be status: Approved
copy    = "copywriting-archive/<slug>-copy.json" # required for subtask 4
# outputs land in campaign-orchestration/<slug>/


def subtask_1_build_send_sequence(brief):
    read(brief, sections=[4, 7])          # audience, email series
    read("suppression-rules.md")
    read("frequency-capping-rules.md")
    read("channel-priority-rules.md")

    for email in brief.series:
        node = {
            trigger,        # date, event, or delay from previous node
            audience,       # segment size after suppression
            suppression,    # rules applied at this node
            branches,       # opened/clicked/purchased → next node or exit
            exit_conditions # purchase, unsub, end of series
        }

    # workflow.md is a single python code block — no tables, no ASCII diagrams
    # nodes as send() calls with inline args
    # branching as if/else per contact
    # blockers as # BLOCKER: comments above the send they gate
    # UTMs as cta_url= args on send()
    # suppression, freq cap, attribution, approvals as # comment sections
    write("campaign-orchestration/<slug>/workflow.md")


def subtask_2_configure_ab_tests(brief, copy):
    read(brief, section=12)           # test variable, variants, split, winner criteria
    read("ab-test-standards.md")

    for test in brief.ab_tests:
        assert test.variant_labels in copy.subject_line.options
        record(variable, split, winner_criteria, decision_date, fallback)

    append_to("campaign-orchestration/<slug>/workflow.md", section="A/B Test Summary")


def subtask_3_define_tracking(brief):
    read(brief, sections=[8, 13])     # offer/CTA destinations, UTM, attribution

    for email in brief.series:
        utm = build_utm(source, medium, campaign, content=f"email-{n}-cta")
        attribution_window = brief.attribution_window or "7-day click, 1-day open"

    append_to("campaign-orchestration/<slug>/workflow.md", section="Tracking and Attribution")


def subtask_4_render_html(copy):
    # runs: python campaign-orchestration/scripts/render-email-html.py <copy>
    for email in copy:
        schema = read(email.template + ".schema.json")
        html   = read(email.template + ".html")
        vars   = {k: v for k, v in email.items() if k not in METADATA_KEYS}
        rendered = substitute(html, vars)          # {{var}} → value
        warn_if_unresolved(rendered, uri_fields)   # logo_url, cta_url, etc. — fill manually
        write(f"campaign-orchestration/<slug>/rendered/<email-slug>.html")
    # rendered/ is gitignored


def subtask_5_validate_and_handoff(slug):
    assert brief.status == "Approved"

    for html in glob(f"campaign-orchestration/{slug}/rendered/*.html"):
        assert no_unresolved_tokens(html)   # no remaining {{var}}

    workflow = read(f"campaign-orchestration/{slug}/workflow.md")
    assert all_nodes_have_exit_conditions(workflow)
    assert ab_tests_have_winner_criteria(workflow)
    assert utms_on_all_links(workflow)
    assert suppression_documented(workflow)
    assert frequency_cap_not_violated(workflow)

    append_to(workflow, section="Approval", sign_off=True)
```
