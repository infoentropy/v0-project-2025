#!/usr/bin/env python3
"""
render-email-html.py

Orchestration Subtask 4: Render ESP-Ready HTML

For each email in a copywriting JSON file:
  1. Read the template reference to locate the .html and .schema.json files.
  2. Use the schema to classify variables as content fields (supplied by the
     copywriting skill) vs. URI fields (URLs filled in separately before send).
  3. Validate that all required content fields are present in the copy JSON.
  4. Substitute {{variable}} placeholders in the HTML with copy values.
  5. Write a rendered .html file ready to upload to an ESP.

Exit codes:
  0  All emails rendered; no missing content fields.
  1  One or more emails had errors (missing template, missing file, missing
     required content fields in --strict mode).

Usage:
    python campaign-orchestration/scripts/render-email-html.py <copy-json> [options]

Options:
    --output-dir DIR   Where to write rendered HTML files.
                       Default: rendered/<copy-json-stem>/
    --repo-root DIR    Repo root path. Default: auto-detected via CLAUDE.md.
    --strict           Exit 1 if any required content field is missing from
                       the copy JSON (default: warn only).

Examples:
    python campaign-orchestration/scripts/render-email-html.py \\
        copywriting-archive/spring-reengagement-2026-copy.json

    python campaign-orchestration/scripts/render-email-html.py \\
        copywriting-archive/spring-reengagement-2026-copy.json \\
        --output-dir rendered/spring-reengagement-2026 \\
        --strict
"""

import argparse
import json
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Top-level keys in a copy JSON email object that are never HTML variables.
METADATA_KEYS = frozenset({"email", "name", "template", "subject_line", "_meta"})


# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------


def find_repo_root(start: Path) -> Path:
    """Walk up the directory tree until a directory containing CLAUDE.md is found."""
    current = start.resolve()
    while current != current.parent:
        if (current / "CLAUDE.md").exists():
            return current
        current = current.parent
    raise RuntimeError(
        "Could not locate repo root (no CLAUDE.md found upstream). "
        "Pass --repo-root to specify the path explicitly."
    )


def display_path(path: Path, base: Path) -> str:
    """Return path relative to base when possible; fall back to absolute."""
    try:
        return str(path.relative_to(base))
    except ValueError:
        return str(path)


def template_name(template_ref: str) -> str:
    """Extract the stem name from a template reference path."""
    return Path(template_ref.rstrip("/")).name


def html_path_for(template_ref: str, repo_root: Path) -> Path:
    """Resolve the .html file path for a template reference."""
    ref = template_ref.rstrip("/")
    name = template_name(ref)
    return repo_root / ref / f"{name}.html"


def schema_path_for(template_ref: str, repo_root: Path) -> Path:
    """Resolve the .schema.json file path for a template reference."""
    ref = template_ref.rstrip("/")
    name = template_name(ref)
    return repo_root / ref / f"{name}.schema.json"


# ---------------------------------------------------------------------------
# Schema helpers
# ---------------------------------------------------------------------------


def load_schema(template_ref: str, repo_root: Path) -> dict:
    path = schema_path_for(template_ref, repo_root)
    if not path.exists():
        raise FileNotFoundError(f"Schema not found: {display_path(path, repo_root)}")
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def classify_fields(schema: dict) -> tuple:
    """
    Split schema properties into two sets:

    uri_fields     — properties with "format": "uri". These hold asset URLs and
                     ESP-specific links (logo, hero image, CTA, unsubscribe).
                     They are NOT written by the copywriting skill and will be
                     absent from the copy JSON; their absence is expected.

    content_fields — all other required properties. These are text values the
                     copywriting skill must supply. Their absence is a warning
                     (or error in --strict mode).

    Returns (uri_fields, content_fields) as sets of field name strings.
    """
    properties = schema.get("properties", {})
    required = set(schema.get("required", []))

    uri_fields = {
        name
        for name, defn in properties.items()
        if defn.get("format") == "uri"
    }
    content_fields = required - uri_fields

    return uri_fields, content_fields


# ---------------------------------------------------------------------------
# Copy extraction and rendering
# ---------------------------------------------------------------------------


def load_copy_json(path: Path) -> list:
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(
            f"Expected a JSON array in {path.name}, got {type(data).__name__}."
        )
    return data


def body_copy_to_html(text: str) -> str:
    """
    Convert plain-text body copy to inline HTML.

    Double newlines (blank lines) split paragraphs; each becomes a </p><p>
    boundary. Single newlines within a paragraph become <br> tags.
    The output is meant to be injected directly inside a <p>...</p> element.
    """
    paragraphs = re.split(r"\n{2,}", text.strip())
    parts = [p.replace("\n", "<br>") for p in paragraphs]
    return '</p>\n<p style="margin: 0 0 16px 0;">'.join(parts)


def extract_copy_variables(email_obj: dict) -> dict:
    """
    Pull HTML template variables out of a copy JSON email object.

    - Skips all keys in METADATA_KEYS.
    - Skips non-string values (nested objects, arrays, numbers).
    - Converts body_copy paragraphs to HTML.
    """
    variables = {}
    for key, value in email_obj.items():
        if key in METADATA_KEYS:
            continue
        if not isinstance(value, str):
            continue
        variables[key] = body_copy_to_html(value) if key == "body_copy" else value
    return variables


def render(template_html: str, variables: dict) -> tuple:
    """
    Replace {{key}} tokens in template_html with values from variables.

    Returns:
        rendered   — the substituted HTML string
        unresolved — sorted list of variable names that had no matching key
    """
    html = template_html
    for key, value in variables.items():
        html = html.replace("{{" + key + "}}", value)
    unresolved = sorted(set(re.findall(r"\{\{(\w+)\}\}", html)))
    return html, unresolved


def email_slug(email_obj: dict, index: int) -> str:
    """Produce a kebab-case filename slug from the email name."""
    raw = email_obj.get("name") or email_obj.get("email") or f"email-{index + 1}"
    return re.sub(r"[^a-z0-9]+", "-", str(raw).lower()).strip("-")


# ---------------------------------------------------------------------------
# Per-email processing
# ---------------------------------------------------------------------------


def process_email(
    index: int,
    total: int,
    email_obj: dict,
    repo_root: Path,
    output_dir: Path,
    strict: bool,
) -> bool:
    """
    Render a single email. Prints progress and warnings to stdout.

    Returns True on success (file written), False on fatal error.
    """
    label = email_obj.get("name") or email_obj.get("email") or f"Email {index + 1}"
    template_ref = email_obj.get("template", "").strip()

    print(f"[{index + 1}/{total}] {label}")

    if not template_ref:
        print("  ERROR  — missing 'template' field, skipping.")
        return False

    # Locate template files.
    h_path = html_path_for(template_ref, repo_root)
    if not h_path.exists():
        print(f"  ERROR  — HTML template not found: {display_path(h_path, repo_root)}")
        return False

    try:
        schema = load_schema(template_ref, repo_root)
    except FileNotFoundError as exc:
        print(f"  ERROR  — {exc}")
        return False

    print(f"  Schema:   {display_path(schema_path_for(template_ref, repo_root), repo_root)}")
    print(f"  Template: {display_path(h_path, repo_root)}")

    # Classify schema fields and validate copy coverage.
    uri_fields, content_fields = classify_fields(schema)
    copy_vars = extract_copy_variables(email_obj)

    missing_content = sorted(content_fields - set(copy_vars.keys()))
    if missing_content:
        tag = "ERROR  " if strict else "WARNING"
        print(f"  {tag} — missing required content field(s): {', '.join(missing_content)}")
        if strict:
            return False

    # Render.
    template_html = h_path.read_text(encoding="utf-8")
    rendered, unresolved = render(template_html, copy_vars)

    # Report unresolved tokens, split by expected (URI) vs. unexpected.
    uri_unresolved = [v for v in unresolved if v in uri_fields]
    unexpected_unresolved = [v for v in unresolved if v not in uri_fields]

    if uri_unresolved:
        print(f"  URI gaps  — fill before sending: {', '.join(uri_unresolved)}")
    if unexpected_unresolved:
        print(f"  WARNING  — unexpected unresolved token(s): {', '.join(unexpected_unresolved)}")

    # Write output file.
    slug = email_slug(email_obj, index)
    out_path = output_dir / f"{slug}.html"
    out_path.write_text(rendered, encoding="utf-8")
    print(f"  Written  → {display_path(out_path, repo_root)}")

    return True


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render ESP-ready HTML by merging copy JSON values into email design templates.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "copy_json",
        help="Path to the copywriting JSON file.",
    )
    parser.add_argument(
        "--output-dir",
        metavar="DIR",
        default=None,
        help="Output directory for rendered HTML. Default: rendered/<copy-json-stem>/",
    )
    parser.add_argument(
        "--repo-root",
        metavar="DIR",
        default=None,
        help="Repo root path. Default: auto-detected by walking up to CLAUDE.md.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 if any required content field is missing from the copy JSON.",
    )
    args = parser.parse_args()

    # Resolve paths.
    copy_path = Path(args.copy_json).resolve()
    if not copy_path.exists():
        print(f"ERROR: copy JSON not found: {copy_path}", file=sys.stderr)
        sys.exit(1)

    try:
        repo_root = (
            Path(args.repo_root).resolve()
            if args.repo_root
            else find_repo_root(copy_path.parent)
        )
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    output_dir = (
        Path(args.output_dir).resolve()
        if args.output_dir
        else repo_root / "rendered" / copy_path.stem
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load copy data.
    try:
        emails = load_copy_json(copy_path)
    except (json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Copy JSON:  {display_path(copy_path, repo_root)}")
    print(f"Output dir: {display_path(output_dir, repo_root)}")
    print(f"Emails:     {len(emails)}")
    if args.strict:
        print("Mode:       strict (missing content fields are errors)")
    print()

    # Process each email.
    results = [
        process_email(i, len(emails), obj, repo_root, output_dir, args.strict)
        for i, obj in enumerate(emails)
    ]
    print()

    success = sum(results)
    failed = len(results) - success

    if failed == 0:
        print(f"Done. {success} file(s) written.")
    else:
        print(f"Done. {success} written, {failed} failed — review output above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
