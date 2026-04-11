# Mockup: Single Column

**Type:** Layout blueprint  
**Use when:** Announcements, transactional emails, simple promotions, re-engagement

---

## Overview

The workhorse layout. One content column, full width, top-to-bottom reading
flow. Renders cleanly on mobile without any media query tricks because there
is nothing to restack.

---

## Wireframe

```
┌─────────────────────────────┐
│           HEADER            │  logo + optional nav link(s)
│         (600px wide)        │
├─────────────────────────────┤
│                             │
│          HERO ZONE          │  image or solid color band + headline
│                             │
├─────────────────────────────┤
│                             │
│         BODY COPY           │  1–3 short paragraphs
│                             │
├─────────────────────────────┤
│          [ CTA ]            │  single primary button, centered
├─────────────────────────────┤
│      SUPPORTING TEXT        │  optional: secondary message or fine print
├─────────────────────────────┤
│           FOOTER            │  legal, unsubscribe, social icons
└─────────────────────────────┘
```

---

## Zones

| Zone | Required | Notes |
|---|---|---|
| Header | Yes | Always first. Max height 80px. |
| Hero | Recommended | Can be image-based or text-on-color. |
| Body Copy | Yes | Keep to 3 paragraphs max. |
| CTA | Yes | One primary CTA per email. |
| Supporting Text | No | Use for secondary offers or disclaimers. |
| Footer | Yes | Always last. Must include unsubscribe. |

---

## Design Notes

- Total content width: **600px**
- Background: white content column on a light gray (`#f4f4f4`) page background
- Left/right padding inside the content column: **24px**
- Vertical rhythm: **24px** of space between each zone
- Body font: 16px / 24px line-height minimum for readability

---

## Components to Use

Pull these from `02-components/` to assemble this layout:

1. `header.md`
2. `hero-banner.md`
3. `text-block.md`
4. `cta-button.md`
5. `footer.md`
