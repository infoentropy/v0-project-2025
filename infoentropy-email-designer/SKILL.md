---
name: infoentropy-email-designer
description: Use this skill to build bulk-generator-compatible emails filled by the strategist. This is a technical skill to define Data Fields, and produce HTML. This is an operations/technical skill.
---

# Skill: Email Design

**Folder:** `email-design/`
**Depends on:** a campaign brief in `campaign-strategy/` (for design direction)
**Feeds into:** `campaign-orchestration/` (final HTML is referenced in send config)

---

## What This Skill Does

Converts visual designs into send-ready HTML email templates. Work happens in
three sequential sub-skills. Each sub-skill can be invoked independently once
its inputs exist.

| Sub-skill | Folder | Purpose |
|---|---|---|
| [Mockup Parser](#sub-skill-1--mockup-parser) | `01-mockups/` | Extract components from a PNG or Figma design |
| [Component Builder](#sub-skill-2--component-builder) | `02-components/` | Create or update a single HTML component |
| [Page Assembler](#sub-skill-3--page-assembler) | `03-pages/` | Assemble components into a full email template |

Run them in order for a new design. Run any one independently when inputs
for that phase are already available.

---

## HTML Rules (apply to all three sub-skills)

- All layout must use `<table>` elements — no `<div>`, flexbox, or grid.
- Max content width: **600 px**.
- All styles must be **inline** — no external stylesheets, no `<style>` blocks.
- Images must include `alt` text and explicit `width` and `height` attributes.
- Variables use `{{double_curly_braces}}` with `snake_case` names.
- Test against: Gmail, Apple Mail, Outlook 2019+.
- Use `role="presentation"` on layout tables.

---

## Sub-skill 1 · Mockup Parser

**Invoke when:** a PNG screenshot or Figma URL is provided as input.

### Inputs
- A PNG file or Figma link showing the email design.
- Optionally: the name of the campaign this design belongs to.

### Context documents — read these first
1. `01-mockups/parsing-guide.md` — full instructions for identifying and
   extracting components from a design.
2. `01-mockups/component-output-template.md` — exact file format for component
   output; every generated component must match this format.
3. `01-mockups/processed-log.md` — check before processing; skip if this design
   was already parsed and no structural changes are present.
4. `02-components/` — scan existing components before creating new ones;
   update rather than duplicate.

### Process
Follow the four steps in `01-mockups/parsing-guide.md`:
1. Orient to the design (width, variants, log check).
2. Identify discrete component boundaries.
3. Define each component (name, schema, HTML).
4. Write output files and append the processed-log row.

### Output
- One folder per new component in `02-components/<component-name>/`
  containing: `<name>.md`, `<name>.html`, `<name>.schema.json`
- One new row appended to `01-mockups/processed-log.md`

---

## Sub-skill 2 · Component Builder

**Invoke when:** a specific component needs to be created or updated without
a full design file — e.g., adding a new button variant or fixing an Outlook bug.

### Inputs
- Component name and description, or a reference to an existing component to update.
- Variable list (what the component should accept as inputs).
- Any design specs (dimensions, colors, font sizes).

### Context documents — read these first
1. `01-mockups/component-output-template.md` — the required three-file folder
   structure; every component must match this exactly.
2. `02-components/<existing-component>/` — read any related existing component
   before creating a new one to reuse patterns.

### Process
1. Check `02-components/` for an existing component to update or reference.
2. Create the folder `02-components/<component-name>/`.
3. Write `<name>.md` — purpose, schema table, usage notes.
4. Write `<name>.html` — raw table-based HTML with `{{variable}}` tokens.
5. Write `<name>.schema.json` — JSON Schema draft-07 for all variables.
6. Verify that variable names are identical across all three files.

### Output
- `02-components/<component-name>/<name>.md`
- `02-components/<component-name>/<name>.html`
- `02-components/<component-name>/<name>.schema.json`

---

## Sub-skill 3 · Page Assembler

**Invoke when:** components are available in `02-components/` and a full email
template needs to be built.

### Inputs
- List of components to include (or a design mockup identifying which components to use).
- Variable values for all `{{tokens}}` required by those components, or
  confirmation that a schema-only template (no filled values) is the goal.
- Campaign brief reference (for Section 10 design direction).

### Context documents — read these first
1. `03-pages/page-output-template.md` — required three-file folder structure
   for pages; every assembled page must match this.
2. `03-pages/` — check for an existing template before building a new one.
3. Each component folder in `02-components/` that will be included.

### Process
1. Check `03-pages/` for an existing template that matches the required layout.
   Reuse and adapt rather than building from scratch when possible.
2. Create the folder `03-pages/<page-name>/`.
3. Write `<page-name>.md` — component manifest and variable table.
4. Write `<page-name>.html` — full `<!DOCTYPE html>` document assembled from
   component HTML, wrapped in `<!-- Component Name -->` comments.
5. Write `<page-name>.schema.json` — combined JSON Schema for all page variables.
6. Validate: inline styles only, no external CSS, all images have `alt` + dimensions.

### Output
- `03-pages/<page-name>/<name>.md`
- `03-pages/<page-name>/<name>.html`
- `03-pages/<page-name>/<name>.schema.json`

---

## Rules

- Never skip the processed-log entry (Sub-skill 1).
- Never create a component that duplicates an existing one — update instead.
- Never build a page before checking `03-pages/` for an existing template.
- All three files (`.md`, `.html`, `.schema.json`) must be created together;
  a component or page folder is not valid with fewer than three files.
