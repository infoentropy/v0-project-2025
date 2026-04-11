# Component: CTA Button

**Type:** Interactive element  
**Phase:** 2 — Component  
**Used in:** All layout mockups

---

## Purpose

The primary call-to-action button. Designed as a bulletproof HTML button
(table-based, not `<a>` styled as a button) so it renders in Outlook.

---

## Schema

| Variable | Type | Required | Default | Description |
|---|---|---|---|---|
| `label` | string | Yes | — | Button text (e.g. "Shop Now") |
| `url` | string | Yes | — | Destination URL |
| `bg_color` | hex | No | `#000000` | Button background color |
| `text_color` | hex | No | `#ffffff` | Button label color |
| `width` | px or % | No | `200px` | Button width |
| `border_radius` | px | No | `4px` | Corner rounding |
| `font_size` | px | No | `16px` | Label font size |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "CTA Button",
  "type": "object",
  "required": ["label", "url"],
  "properties": {
    "label": {
      "type": "string",
      "description": "Button text (e.g. \"Shop Now\")"
    },
    "url": {
      "type": "string",
      "format": "uri",
      "description": "Destination URL"
    },
    "bg_color": {
      "type": "string",
      "pattern": "^#[0-9A-Fa-f]{6}$",
      "default": "#000000",
      "description": "Button background color"
    },
    "text_color": {
      "type": "string",
      "pattern": "^#[0-9A-Fa-f]{6}$",
      "default": "#ffffff",
      "description": "Button label color"
    },
    "width": {
      "type": "string",
      "default": "200px",
      "description": "Button width (px or %)"
    },
    "border_radius": {
      "type": "string",
      "default": "4px",
      "description": "Corner rounding"
    },
    "font_size": {
      "type": "string",
      "default": "16px",
      "description": "Label font size"
    }
  }
}
```

---

## HTML

```html
<!-- CTA Button -->
<table role="presentation" cellspacing="0" cellpadding="0" border="0"
       align="center" style="margin: 0 auto;">
  <tr>
    <td align="center" bgcolor="{{bg_color}}"
        style="border-radius: {{border_radius}};">
      <a href="{{url}}" target="_blank"
         style="display: inline-block;
                font-family: Arial, sans-serif;
                font-size: {{font_size}};
                font-weight: bold;
                color: {{text_color}};
                text-decoration: none;
                padding: 14px 28px;
                border-radius: {{border_radius}};
                background-color: {{bg_color}};
                width: {{width}};
                text-align: center;
                mso-padding-alt: 0;
                -webkit-text-size-adjust: none;">
        {{label}}
      </a>
    </td>
  </tr>
</table>
<!-- /CTA Button -->
```

---

## Usage Notes

- Always center-align the button table with `align="center"` and `margin: 0 auto`.
- One primary CTA per email. Do not stack two CTA buttons without a secondary
  style distinction (outlined vs. filled).
- Minimum touch target: 44px tall — the default padding (14px top + bottom)
  achieves this with any font size ≥ 16px.
- Test `bgcolor` attribute on `<td>` in addition to the inline CSS `background-color`
  — Outlook reads the attribute, not the CSS.
