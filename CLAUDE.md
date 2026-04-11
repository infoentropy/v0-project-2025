# CLAUDE.md

This file provides guidance to AI assistants (Claude and others) working in this repository.

---

## Project Overview

**Repository:** `infoentropy/v0-project-2025`
**Stack:** Next.js 15 (App Router) · TypeScript · Tailwind CSS · shadcn/ui

This project was bootstrapped with [v0.dev](https://v0.dev), Vercel's AI-powered UI generation tool. It follows the conventions of a modern Next.js App Router application with server components, server actions, and the shadcn/ui component library.

---

## Repository Structure

```
.
├── app/                    # Next.js App Router pages and layouts
│   ├── layout.tsx          # Root layout (fonts, global providers)
│   ├── page.tsx            # Home page (route: /)
│   ├── globals.css         # Global styles and Tailwind base/theme tokens
│   └── (routes)/           # Additional route segments
├── components/             # Reusable React components
│   └── ui/                 # shadcn/ui primitives (auto-generated, do not edit manually)
├── lib/                    # Shared utilities and helpers
│   └── utils.ts            # cn() helper and other utilities
├── hooks/                  # Custom React hooks
├── public/                 # Static assets
├── .env.local              # Local environment variables (never commit)
├── .env.example            # Template for required env vars (commit this)
├── components.json         # shadcn/ui configuration
├── next.config.ts          # Next.js configuration
├── tailwind.config.ts      # Tailwind CSS configuration
├── tsconfig.json           # TypeScript configuration
└── package.json            # Dependencies and scripts
```

> Note: This structure reflects the expected layout once files are added. Adapt this section as the project grows.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Next.js 15 (App Router) |
| Language | TypeScript (strict mode) |
| Styling | Tailwind CSS v3/v4 |
| UI Components | shadcn/ui |
| Icons | lucide-react |
| Fonts | Geist (via `next/font`) |
| Package Manager | npm (or pnpm if `pnpm-lock.yaml` is present) |
| Linting | ESLint (Next.js config) |
| Formatting | Prettier (if `.prettierrc` exists) |

---

## Development Workflows

### Install dependencies

```bash
npm install
# or
pnpm install
```

### Start dev server

```bash
npm run dev
```

The app runs at `http://localhost:3000`.

### Build for production

```bash
npm run build
npm run start
```

### Lint

```bash
npm run lint
```

### Type-check

```bash
npx tsc --noEmit
```

---

## Adding shadcn/ui Components

Use the CLI — never copy-paste components manually into `components/ui/`:

```bash
npx shadcn@latest add <component-name>
# examples:
npx shadcn@latest add button
npx shadcn@latest add dialog
npx shadcn@latest add form
```

This respects `components.json` and places files correctly.

---

## Key Conventions

### TypeScript

- Strict mode is enabled (`"strict": true` in `tsconfig.json`).
- Prefer `interface` over `type` for object shapes.
- Use explicit return types on exported functions.
- Avoid `any`; use `unknown` with narrowing if the type is truly unknown.
- Path aliases: `@/` maps to the project root (e.g., `import { cn } from "@/lib/utils"`).

### React / Next.js

- **Server Components by default.** Only add `"use client"` at the top of a file when the component needs browser APIs, event handlers, or React state/effects.
- **Server Actions** live in `app/actions/` or colocated in route segments, marked with `"use server"`.
- Fetch data in Server Components using `async/await` directly — no useEffect data fetching.
- Use `next/image` for all images (`<Image>` not `<img>`).
- Use `next/link` for all internal navigation (`<Link>` not `<a>`).
- Prefer `loading.tsx` and `error.tsx` files for route-level loading and error states.

### Styling

- Use Tailwind utility classes exclusively. Avoid inline `style` props unless absolutely necessary.
- Use the `cn()` helper from `@/lib/utils` to merge conditional classes:
  ```ts
  import { cn } from "@/lib/utils"
  // cn("base-class", isActive && "active-class", className)
  ```
- CSS variables for design tokens are defined in `app/globals.css` (shadcn/ui convention).
- Do not modify files in `components/ui/` directly — regenerate them with the shadcn CLI.

### File Naming

| Artifact | Convention |
|---|---|
| Components | `PascalCase.tsx` |
| Pages / layouts | `page.tsx`, `layout.tsx` (Next.js required names) |
| Hooks | `use-kebab-case.ts` |
| Utilities | `kebab-case.ts` |
| Server actions | `actions.ts` or `<feature>-actions.ts` |

### Component Structure

```tsx
// 1. Imports
import { type FC } from "react"
import { cn } from "@/lib/utils"

// 2. Types
interface MyComponentProps {
  title: string
  className?: string
}

// 3. Component
const MyComponent: FC<MyComponentProps> = ({ title, className }) => {
  return (
    <div className={cn("base-styles", className)}>
      {title}
    </div>
  )
}

// 4. Export
export default MyComponent
// or: export { MyComponent }
```

---

## Environment Variables

- Secrets and environment-specific values go in `.env.local` (gitignored).
- Document every required variable in `.env.example` with placeholder values.
- Client-side variables must be prefixed with `NEXT_PUBLIC_`.
- Never commit real credentials — check `.gitignore` before staging files.

---

## Git Workflow

- The default branch is `main`.
- Feature branches: `feature/<short-description>` or `fix/<short-description>`.
- AI-generated branches use the prefix `claude/`.
- Write clear, imperative commit messages: `Add hero section`, `Fix mobile nav overflow`, `Update shadcn button variant`.
- Do not amend published commits; create new ones.

---

## What AI Assistants Should NOT Do

- Do not add comments or JSDoc unless the logic is genuinely non-obvious.
- Do not add `"use client"` to components that don't need it.
- Do not edit files under `components/ui/` — use the shadcn CLI to regenerate.
- Do not commit `.env.local` or any file containing real secrets.
- Do not introduce `any` types to silence TypeScript errors — fix the root cause.
- Do not add abstractions or utilities for one-off use cases.
- Do not create new files when modifying an existing file is sufficient.
- Do not use `<img>` or `<a>` — use `next/image` and `next/link`.
- Do not add `eslint-disable` comments without a clear explanation of why the rule must be bypassed.
- Do not push to `main` directly — always work on a feature branch.

---

## Common Patterns

### Data fetching in a Server Component

```tsx
// app/posts/page.tsx
async function PostsPage() {
  const posts = await fetch("https://api.example.com/posts").then(r => r.json())
  return <PostList posts={posts} />
}
```

### Server Action for form submission

```ts
// app/actions.ts
"use server"

import { revalidatePath } from "next/cache"

export async function createPost(formData: FormData) {
  const title = formData.get("title") as string
  // ... persist to DB
  revalidatePath("/posts")
}
```

### Client component with state

```tsx
"use client"

import { useState } from "react"

export function Counter() {
  const [count, setCount] = useState(0)
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>
}
```

---

## References

- [Next.js App Router docs](https://nextjs.org/docs/app)
- [shadcn/ui docs](https://ui.shadcn.com)
- [Tailwind CSS docs](https://tailwindcss.com/docs)
- [v0.dev](https://v0.dev)
