# Mockup Parsing Guide

Instructions for the mockup skill when processing an uploaded PNG or Figma file.

---

## Step 1 · Orient to the Design

Before identifying anything, answer these questions:
- What is the overall email width? (Usually 600px — confirm from any visible ruler or frame dimensions.)
- Is this a single email or multiple variants? (Process each variant separately.)
- Is there an existing processed-log entry for this file? If yes, check whether
  it needs an update or can be skipped entirely.

---

## Step 2 · Identify Component Boundaries

Scan the design top to bottom. A discrete component is a self-contained visual
unit that:
- Has a clear visual boundary (background change, divider, whitespace gap ≥ 16px)
- Could appear in a different email without modification
- Contains a consistent internal structure (the same pattern of text, image, or button)

**Treat these as components:**
- Logo/header bar
- Hero image band (image + optional overlay text)
- Headline + subheadline block
- Body text block
- CTA button
- Image + caption pair
- Product card (image + name + price + CTA)
- Icon + text row (feature callout)
- Divider / spacer
- Social icon row
- Footer (legal + unsubscribe)

**Do NOT create a component for:**
- Page-level background color
- Padding/margin between components (document these in the page template instead)
- One-off decorative flourishes unique to a single campaign
- Text content itself (copy belongs in `copywriting-archive/`, not here)

---

## Step 3 · Define Each Component

For each identified component:

1. **Name it** using `kebab-case`. Be descriptive but concise.
   - Good: `product-card.md`, `icon-feature-row.md`, `social-icon-row.md`
   - Avoid: `section3.md`, `thing-with-image.md`

2. **Check `02-components/`** before creating.
   - If a file for this component already exists: compare it against the design.
     If the design shows a meaningful variation (different structure, new variable),
     update the existing file. Otherwise skip.
   - If no file exists: create it using `component-output-template.md`.

3. **Extract the schema.** For each visual property that varies (color, text,
   image URL, link), define a `{{variable}}`. Fixed structural elements
   (table wrappers, base padding) are hardcoded in the HTML.

4. **Write the HTML** using table-based layout. All styles inline. See
   `component-output-template.md` for the required structure.

---

## Step 4 · Write Output Files

For each new component:
- Write the file to `email-design/02-components/<component-name>.md`
- Follow `component-output-template.md` exactly

Then append a row to `processed-log.md`:
```
| YYYY-MM-DD | <filename or Figma URL> | <comma-separated component names> | <any notes> |
```

---

## Edge Cases

| Situation | Action |
|---|---|
| Component exists but design shows a new variant | Add a "Variants" section to the existing component file |
| Design has a section with freeform layout (no repeatable pattern) | Skip — document as a one-off in the page template (`03-pages/`) |
| Two very similar components (e.g. two button styles) | Create one component with a variable for the style difference |
| Figma uses auto-layout or components | Focus on the rendered visual output, not Figma's internal structure |
| Design is low-fidelity or incomplete | Extract what is defined; note gaps in the processed-log Notes column |
