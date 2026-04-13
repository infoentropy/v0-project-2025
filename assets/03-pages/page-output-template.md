# Page Output Template

Each page is a **folder** inside `03-pages/`, named in `kebab-case`.
The folder contains exactly three files. Do not add or remove files.

Reference: `03-pages/starter-single-column/` is a correctly formatted example.

---

## Folder Structure

```
03-pages/
└── <page-name>/
    ├── <page-name>.md           # Metadata, component manifest, variable table
    ├── <page-name>.html         # Full assembled email HTML
    └── <page-name>.schema.json  # JSON Schema for all page variables (draft-07)
```

---

## File 1 · `<page-name>.md`

```markdown
# Page: <Page Name>

**Mockup:** <mockup name>
**Status:** <Template | Draft | Approved>

---

## Components Used

| Order | Component | Folder |
|---|---|---|
| 1 | <Component Name> | `02-components/<component-name>/` |

---

## Variables Required

| Variable | Type | Required | Description |
|---|---|---|---|
| `{{variable_name}}` | <string \| url> | <Yes \| No> | <what it holds> |

See `<page-name>.schema.json` for the machine-readable schema.
See `<page-name>.html` for the full assembled HTML.
```

---

## File 2 · `<page-name>.html`

Complete, send-ready HTML — full `<!DOCTYPE html>` document.
Raw HTML only — no markdown, no fences, no explanatory text.
Component sections are wrapped in `<!-- Component Name -->` / `<!-- /Component Name -->` comments.

---

## File 3 · `<page-name>.schema.json`

JSON Schema covering every `{{variable}}` present in the `.html` file.
Pure JSON only — no markdown, no fences, no explanatory text.
All page-level variables are `required` unless they have a documented default.
