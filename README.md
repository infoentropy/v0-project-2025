# v0-project-2025

A collection of Claude Skills for producing marketing email campaigns. Each
top-level folder is one skill and contains a `SKILL.md` at its root, plus
reference material the skill reads to do its work.

---

## Skills

| Folder | Skill name | What it does |
|---|---|---|
| `infoentropy-strategy/` | `infoentropy-campaign-strategy` | Strategy briefs, audience personas, messaging hierarchy, copywriting reference |
| `infoentropy-email-designer/` | `infoentropy-email-designer` | Parse mockups → HTML components → assembled page templates |
| `infoentropy-bulk-generator/` | `infoentropy-bulk-generator` | Build send sequence, A/B tests, render ESP-ready HTML |

Each `SKILL.md` begins with YAML frontmatter (`name`, `description`). The
`description` is the trigger text Claude uses to decide when to invoke the
skill.

---

## The `projects/<slug>/` Pattern

Campaign-specific outputs from every skill land in a shared `projects/<slug>/`
folder. Reference material that does not change per campaign stays in the
skill's own folder.

```
projects/<slug>/
├── campaign-strategy-brief.md   ← infoentropy-strategy
├── copy.json                     ← copywriting output
├── orchestration.md              ← infoentropy-bulk-generator
└── templates/
    └── rendered/                 ← render-email-html.py output (gitignored)
```

Use the campaign slug as the folder name (e.g. `spring-reengagement-2026`,
`q4-product-launch`).

---

## Typical Workflow

1. **Write the brief** — invoke `infoentropy-campaign-strategy` to produce
   `projects/<slug>/campaign-strategy-brief.md`.
2. **Design the email** — invoke `infoentropy-email-designer` with a PNG or
   Figma link. It extracts components into `infoentropy-email-designer/assets/`
   and assembles page templates. Templates are global, not project-specific.
3. **Write copy** — produce `projects/<slug>/copy.json` following the schema of
   the chosen page template.
4. **Orchestrate and render** — invoke `infoentropy-bulk-generator` to build
   `projects/<slug>/orchestration.md` and run the renderer:

   ```bash
   python infoentropy-bulk-generator/scripts/render-email-html.py projects/<slug>/copy.json
   ```

   Rendered HTML lands in `projects/<slug>/templates/rendered/` (gitignored).

---

## HTML Standards (enforced by `infoentropy-email-designer`)

- Table-based layout only — no `<div>`, flexbox, or grid.
- Max content width: 600 px.
- All styles inline; no external stylesheets or `<style>` blocks.
- Images require `alt` text and explicit `width` and `height` attributes.
- Variables: `{{snake_case}}` double-curly tokens.
- `role="presentation"` on layout tables.
- Test targets: Gmail, Apple Mail, Outlook 2019+.

### Component / Page Three-File Rule

Every component and every page must have exactly three files with matching
basenames:

- `<name>.md` — purpose, schema table, usage notes
- `<name>.html` — raw HTML with `{{tokens}}`
- `<name>.schema.json` — JSON Schema draft-07 for the variables

Variable names must be identical across all three files.

---

## Personalization Data

Every `{{variable}}` in a template and every `contact.*` condition in an
orchestration file must map to a field in
`infoentropy-strategy/reference/personalization-data-catalog.md`. If a field is
missing, add a `# BLOCKER:` comment rather than inventing one.

---

## Conventions

- `kebab-case` filenames with `.md`, `.html`, or `.schema.json` extensions.
- One topic per file.
- Commit messages describe what changed and why.
- Work on a feature branch; do not push to `main` directly.

See `CLAUDE.md` for guidance aimed at AI assistants working in this repo.
