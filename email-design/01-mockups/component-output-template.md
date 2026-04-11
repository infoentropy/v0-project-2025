# Component Output Template

Use this exact structure for every new `.md` file written to `02-components/`.
Replace all `<placeholder>` values. Do not add or remove sections.

Reference: `02-components/cta-button.md` is a correctly formatted example.

---

```markdown
# Component: <Component Name>

**Type:** <Structural | Interactive | Decorative | Layout>
**Phase:** 2 — Component
**Used in:** <list mockup or page names, or "All layouts" if universal>

---

## Purpose

<One paragraph. What this component does, when to use it, and any
critical rendering or accessibility notes.>

---

## Schema

| Variable | Type | Required | Default | Description |
|---|---|---|---|---|
| `{{variable_name}}` | <string \| hex \| px \| url \| boolean> | <Yes \| No> | <value or —> | <what it controls> |

---

## HTML

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
` ` `

---

## Usage Notes

- <Bullet points covering Outlook compatibility quirks, touch target rules,
  alt text requirements, or other constraints.>
- <One note per distinct concern.>
```

---

## Rules

- **All layout uses `<table>`** — no `<div>`, no flexbox, no grid.
- **All styles are inline** — no `<style>` blocks, no class attributes.
- **Variables use `{{double_curly_braces}}`** — snake_case names.
- **Images must have** explicit `width`, `height`, and `alt` attributes.
- **Outlook button compatibility:** use `bgcolor` attribute on `<td>` in
  addition to `background-color` in inline CSS.
- **Comments** wrap every component: `<!-- Component Name -->` open,
  `<!-- /Component Name -->` close. This allows skills to locate and
  extract components from assembled page HTML.
- **Max content width: 600px.** Components must not exceed this.
