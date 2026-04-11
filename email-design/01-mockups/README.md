# Phase 1 · Mockups

This folder is a **skill workflow**, not a static library of layouts.

---

## What Happens Here

When a new email design arrives — as a PNG screenshot or a Figma file — the
mockup skill processes it and extracts reusable components from it.

```
[ PNG or Figma input ]
        │
        ▼
  Mockup Skill
  (parses design,
   identifies components)
        │
        ▼
[ New .md files → 02-components/ ]
        │
        ▼
[ Row appended → processed-log.md ]
```

---

## Files in This Folder

| File | Purpose |
|---|---|
| `parsing-guide.md` | Instructions the skill follows to analyze a design |
| `component-output-template.md` | Exact format every new component file must use |
| `processed-log.md` | Running record of every design processed and what was extracted |

---

## How to Trigger the Mockup Skill

Provide one of the following:
- A PNG/JPG image of an email design (upload directly to the skill)
- A public Figma share link (the skill will read frames from it)

The skill will read `parsing-guide.md`, analyze the input, and write new
component files to `02-components/` — one file per identified component.
