#!/usr/bin/env python3
"""
render-email-html.py

Orchestration Subtask 4: Render ESP-Ready HTML

Reads a copywriting JSON file, resolves the HTML template for each email in
the series, substitutes {{variable}} placeholders with copy values, and writes
rendered HTML files ready to upload to an ESP.

Usage:
    python campaign-orchestration/scripts/render-email-html.py <copy-json> [options]

Options:
    --output-dir DIR    Directory for rendered HTML files.
                        Default: rendered/<copy-json-stem>/
    --repo-root DIR     Path to repo root.
                        Default: auto-detected by walking up to CLAUDE.md.

Examples:
    python campaign-orchestration/scripts/render-email-html.py \\
        copywriting-archive/spring-reengagement-2026-copy.json

    python campaign-orchestration/scripts/render-email-html.py \\
        copywriting-archive/spring-reengagement-2026-copy.json \\
        --output-dir rendered/spring-reengagement-2026
"""

import argparse
import json
import re
import sys
from pathlib import Path


# Keys in copy JSON objects that are metadata, not HTML template variables.
METADATA_KEYS = {"email", "name", "template", "subject_line", "_meta"}


# ---------------------------------------------------------------------------
# Repo / path helpers
# ---------------------------------------------------------------------------


def find_repo_root(start: Path) -> Path:
    """Walk up directory tree until CLAUDE.md is found."""
    current = start.resolve()
    while current != current.parent:
        if (current / "CLAUDE.md").exists():
            return current
        current = current.parent
    raise RuntimeError(
        "Could not locate repo root (no CLAUDE.md found). "
        "Use --repo-root to specify the path explicitly."
    )


def resolve_template_html(template_ref: str, repo_root: Path) -> Path:
    """
    Given a template reference like 'email-design/03-pages/starter-single-column/',
    return the path to the matching .html file.

    The HTML file name matches the last component of the template path, e.g.:
        email-design/03-pages/starter-single-column/
        → email-design/03-pages/starter-single-column/starter-single-column.html
    """
    ref = template_ref.rstrip("/")
    name = Path(ref).name
    html_path = repo_root / ref / f"{name}.html"
    if not html_path.exists():
        raise FileNotFoundError(f"HTML template not found: {html_path}")
    return html_path


def resolve_template_schema(template_ref: str, repo_root: Path) -> dict:
    """Return the parsed JSON Schema for a template."""
    ref = template_ref.rstrip("/")
    name = Path(ref).name
    schema_path = repo_root / ref / f"{name}.schema.json"
    if not schema_path.exists():
        raise FileNotFoundError(f"Schema not found: {schema_path}")
    with schema_path.open(encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------


def load_copy_json(path: Path) -> list:
    """Load and validate the copywriting JSON file."""
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(
            f"Expected a JSON array in {path.name}, got {type(data).__name__}."
        )
    return data


# ---------------------------------------------------------------------------
# Variable extraction and rendering
# ---------------------------------------------------------------------------


def body_copy_to_html(text: str) -> str:
    """
    Convert plain-text body copy into HTML-safe inline content.

    Paragraphs are separated by blank lines (two or more newlines).
    Within a paragraph, single newlines become <br> tags.
    The result is suitable for direct injection into a <p>...</p> element.
    """
    paragraphs = re.split(r"\n{2,}", text.strip())
    html_paragraphs = [p.replace("\n", "<br>") for p in paragraphs]
    separator = '</p>\n<p style="margin: 0 0 16px 0;">'
    return separator.join(html_paragraphs)


def extract_variables(email_obj: dict) -> dict:
    """
    Extract HTML template variables from a copy JSON email object.

    - Skips metadata keys (email, template, subject_line, _meta).
    - Converts body_copy plain text to HTML paragraph content.
    - Skips non-string values (dicts, lists) — these are not template variables.
    """
    variables = {}
    for key, value in email_obj.items():
        if key in METADATA_KEYS:
            continue
        if not isinstance(value, str):
            continue
        if key == "body_copy":
            variables[key] = body_copy_to_html(value)
        else:
            variables[key] = value
    return variables


def substitute_variables(html: str, variables: dict) -> tuple:
    """
    Replace {{key}} tokens in html with values from the variables dict.

    Returns:
        (rendered_html, sorted list of unresolved variable names)
    """
    rendered = html
    for key, value in variables.items():
        rendered = rendered.replace("{{" + key + "}}", value)
    unresolved = sorted(set(re.findall(r"\{\{(\w+)\}\}", rendered)))
    return rendered, unresolved


def display_path(path: Path, base: Path) -> str:
    """Return path relative to base if possible, otherwise return absolute path."""
    try:
        return str(path.relative_to(base))
    except ValueError:
        return str(path)


def file_slug(email_obj: dict, index: int) -> str:
    """Produce a kebab-case filename slug from the email name."""
    name = email_obj.get("name") or email_obj.get("email") or f"email-{index + 1}"
    return re.sub(r"[^a-z0-9]+", "-", str(name).lower()).strip("-")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Render ESP-ready HTML by merging a copy JSON file with "
            "email design templates."
        )
    )
    parser.add_argument(
        "copy_json",
        help="Path to the copywriting JSON file (e.g., copywriting-archive/my-campaign-copy.json).",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Directory to write rendered HTML files. Default: rendered/<copy-json-stem>/",
    )
    parser.add_argument(
        "--repo-root",
        default=None,
        help="Path to repo root. Default: auto-detected by walking up to CLAUDE.md.",
    )
    args = parser.parse_args()

    # --- Resolve paths ---
    copy_path = Path(args.copy_json).resolve()
    if not copy_path.exists():
        print(f"ERROR: {copy_path} not found.", file=sys.stderr)
        sys.exit(1)

    repo_root = (
        Path(args.repo_root).resolve()
        if args.repo_root
        else find_repo_root(copy_path.parent)
    )

    output_dir = (
        Path(args.output_dir).resolve()
        if args.output_dir
        else repo_root / "rendered" / copy_path.stem
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    # --- Load copy data ---
    try:
        emails = load_copy_json(copy_path)
    except (json.JSONDecodeError, ValueError) as e:
        print(f"ERROR: Could not load copy JSON — {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Copy JSON:    {display_path(copy_path, repo_root)}")
    print(f"Repo root:    {repo_root}")
    print(f"Output dir:   {display_path(output_dir, repo_root)}")
    print(f"Emails found: {len(emails)}")
    print()

    # --- Render each email ---
    exit_code = 0

    for i, email_obj in enumerate(emails):
        label = email_obj.get("name") or email_obj.get("email") or f"Email {i + 1}"
        template_ref = email_obj.get("template", "").strip()

        print(f"[{i + 1}/{len(emails)}] {label}")

        if not template_ref:
            print("  ERROR: missing 'template' field — skipping.")
            exit_code = 1
            continue

        print(f"  Template: {template_ref}")

        try:
            html_path = resolve_template_html(template_ref, repo_root)
            schema = resolve_template_schema(template_ref, repo_root)  # noqa: F841
        except FileNotFoundError as e:
            print(f"  ERROR: {e} — skipping.")
            exit_code = 1
            continue

        template_html = html_path.read_text(encoding="utf-8")
        variables = extract_variables(email_obj)
        rendered, unresolved = substitute_variables(template_html, variables)

        if unresolved:
            tokens = ", ".join(f"{{{{{v}}}}}" for v in unresolved)
            print(f"  WARNING: {len(unresolved)} unresolved variable(s): {tokens}")

        slug = file_slug(email_obj, i)
        out_path = output_dir / f"{slug}.html"
        out_path.write_text(rendered, encoding="utf-8")
        print(f"  Written:  {display_path(out_path, repo_root)}")

    # --- Summary ---
    print()
    if exit_code == 0:
        print(f"Done. {len(emails)} file(s) written to {display_path(output_dir, repo_root)}/")
    else:
        print("Done with errors — review output above.")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
