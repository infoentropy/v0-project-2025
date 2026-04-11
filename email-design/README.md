# Email Design

This folder governs everything about how emails look and are built. It is
organized into three phases that mirror how UI is built for web pages —
from concept to component to full page.

---

## Three-Phase Structure

```
email-design/
├── 01-mockups/       # Phase 1 — Layout blueprints and visual structure
├── 02-components/    # Phase 2 — Individual HTML components with schemas
└── 03-pages/         # Phase 3 — Full email templates assembled from components
```

### Phase 1 · Mockups
High-level layout concepts defined in plain language and ASCII wireframes.
No code. Describes the spatial structure, content zones, and reading flow of
an email layout pattern. A mockup is a reusable blueprint — not a specific
campaign.

### Phase 2 · Components
The building blocks. Each file documents one discrete email element:
its purpose, its HTML code (table-based for email client compatibility),
and a schema listing every variable the component accepts.

### Phase 3 · Pages
Full email templates assembled by combining components from Phase 2.
Each page document names which components it uses, defines the composition
order, and includes the complete assembled HTML.

---

## How a Skill Uses This Folder

1. **Start in `01-mockups/`** to choose or reference a layout pattern.
2. **Pull components from `02-components/`** to fill the layout zones.
3. **Check `03-pages/`** for existing templates before building a new one.
4. **Save new templates back to `03-pages/`** so they join the shared library.

---

## Email HTML Rules

- All layout must use `<table>` elements — no `<div>` flexbox or grid.
- Max content width: **600px**.
- All styles must be **inline** — no external stylesheets, no `<style>` blocks
  (some clients strip them).
- Images must include `alt` text and explicit `width`/`height` attributes.
- Every component must be tested against: Gmail, Apple Mail, Outlook 2019+.
- Use `role="presentation"` on layout tables to suppress screen reader noise.
