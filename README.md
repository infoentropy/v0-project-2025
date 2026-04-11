# v0-project-2025

A shared document library for Claude skills. Each folder is scoped to a skill
domain and contains the source-of-truth documents that skills read to do their
work — strategy briefs, design templates, copy archives, and orchestration logic.

---

## Folders

| Folder | Skill | What lives here |
|---|---|---|
| `email-design/` | Email Design | Mockup parsing workflow, HTML components, assembled page templates |
| `campaign-strategy/` | Campaign Strategy | Audience personas, campaign briefs, messaging hierarchies |
| `copywriting-archive/` | Copywriting | Subject line swipes, body copy examples, brand voice guide |
| `campaign-orchestration/` | Campaign Orchestration | Send sequences, channel rules, suppression logic, A/B standards |

---

## email-design Structure

`email-design/` is the most developed folder and establishes the patterns
the other folders will follow as they are built out.

```
email-design/
├── 01-mockups/                       # Phase 1 — Design parsing workflow
│   ├── parsing-guide.md              # How the skill analyzes a PNG or Figma input
│   ├── component-output-template.md  # Exact format for generated component files
│   └── processed-log.md             # Log of every design processed
│
├── 02-components/                    # Phase 2 — Reusable HTML components
│   └── <component-name>/
│       ├── <component-name>.md       # Purpose, schema table, usage notes
│       ├── <component-name>.html     # Raw HTML with {{variable}} tokens
│       └── <component-name>.schema.json
│
└── 03-pages/                         # Phase 3 — Assembled email templates
    └── <page-name>/
        ├── <page-name>.md            # Metadata, component manifest, variable table
        ├── <page-name>.html          # Full send-ready HTML document
        └── <page-name>.schema.json
```

---

## How Skills Use This Repo

1. **Parse a design** — provide a PNG or Figma link to the Email Design skill.
   It reads `01-mockups/parsing-guide.md`, extracts components, and writes them
   to `02-components/`.

2. **Build a page** — assemble components from `02-components/` into a new
   folder under `03-pages/`. Check `03-pages/page-output-template.md` for the
   required structure.

3. **Write copy or strategy** — add documents to the relevant folder following
   the conventions in `CLAUDE.md`.

---

## Conventions

- All files use `kebab-case` names with `.md`, `.html`, or `.schema.json` extensions.
- One topic per file. Do not bundle unrelated content.
- Commit messages describe what changed and why (not just "update").
- Do not push to `main` directly — use a feature branch.

See `CLAUDE.md` for full conventions and AI assistant rules.
