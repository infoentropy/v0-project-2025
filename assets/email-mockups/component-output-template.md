# Component Output Template

Each component is a **folder** inside `02-components/`, named in `kebab-case`.
The folder contains exactly three files. Do not add or remove files.

Reference: `02-components/cta-button/` is a correctly formatted example.

---

## Folder Structure

```
02-components/
└── <component-name>/
    ├── <component-name>.md           # Purpose, schema table, usage notes
    ├── <component-name>.html         # Raw HTML with {{variable}} tokens
    └── <component-name>.schema.json  # JSON Schema (draft-07)
```

---

## File 1 · `<component-name>.md`

```markdown
# Component: <Component Name>

**Type:** <Structural | Interactive | Decorative | Layout>
**Phase:** 2 — Component
**Used in:** <list page or mockup names, or "All layouts" if universal>

---

## Purpose

<One paragraph. What this component does, when to use it, and any
critical rendering or accessibility notes.>

---

## Schema

| Variable | Type | Required | Default | Description |
|---|---|---|---|---|
| `variable_name` | <string \| hex \| px \| url \| boolean> | <Yes \| No> | <value or —> | <what it controls> |

See `<component-name>.schema.json` for the machine-readable schema.
See `<component-name>.html` for the HTML implementation.

---

## Usage Notes

- <Bullet points covering Outlook quirks, touch target rules,
  alt text requirements, or other constraints.>
- <One note per distinct concern.>
```

---

## File 2 · `<component-name>.html`

Raw HTML only — no markdown, no fences, no explanatory text.

```html
<!-- <Component Name> -->
<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
  <tr>
    <td style="<inline styles>">
      <!-- component markup using {{variable}} tokens -->
    </td>
  </tr>
</table>
<!-- /<Component Name> -->
```

---

## File 3 · `<component-name>.schema.json`

Pure JSON only — no markdown, no fences, no explanatory text.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "<Component Name>",
  "type": "object",
  "required": ["<required_variable>"],
  "properties": {
    "<variable_name>": {
      "type": "<string | number | boolean>",
      "description": "<what it controls>",
      "default": "<value — omit this key if no default>"
    }
  }
}
```

---

## Rules (apply to all three files)

- **All layout uses `<table>`** — no `<div>`, no flexbox, no grid.
- **All styles are inline** — no `<style>` blocks, no class attributes.
- **Variables use `{{double_curly_braces}}`** — snake_case names. Variable
  names must be identical across the `.md` table, `.html`, and `.schema.json`.
- **Images must have** explicit `width`, `height`, and `alt` attributes.
- **Outlook button compatibility:** use `bgcolor` attribute on `<td>` in
  addition to `background-color` in inline CSS.
- **HTML comments** wrap every component: `<!-- Component Name -->` open,
  `<!-- /Component Name -->` close.
- **Max content width: 600px.** Components must not exceed this.
