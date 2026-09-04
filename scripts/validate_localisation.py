#!/usr/bin/env python3
"""Validate localisation contract tests against the current baseline.

Run with: python3 scripts/validate_localisation.py

This script checks various localisation contract rules and prints a summary,
then writes the failing output to docs/localisation/validation/baseline-red.md.
"""

import csv
import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = REPO_ROOT / "plugin" / "skills"
DOCS = REPO_ROOT / "docs"
LOCALISATION = DOCS / "localisation"
INVENTORY_CSV = LOCALISATION / "01-us-specific-inventory.csv"
SOURCE_REGISTER_CSV = LOCALISATION / "02-source-register.csv"
REPLACEMENT_MATRIX_CSV = LOCALISATION / "03-replacement-matrix.csv"
SCHEMA_DIR = LOCALISATION / "schema"
VALIDATION_DIR = LOCALISATION / "validation"
ALLOWLIST = REPO_ROOT / "tests" / "localisation" / "allowlist.yml"

US_TERM_PATTERNS = [
    re.compile(r"\bK-12\b", re.IGNORECASE),
    re.compile(r"\bCCSS\b", re.IGNORECASE),
    re.compile(r"\bNGSS\b", re.IGNORECASE),
    re.compile(r"\bWIDA\b", re.IGNORECASE),
    re.compile(r"\bIEP\b", re.IGNORECASE),
    re.compile(r"\b504\b", re.IGNORECASE),
    re.compile(r"\bcommon core\b", re.IGNORECASE),
]


def load_allowlist():
    """Load US terms allowlist from YAML if available."""
    if not ALLOWLIST.exists():
        return set()
    terms = set()
    with open(ALLOWLIST, "r") as f:
        content = f.read()
    # Simple parsing: look for terms under a '-' bullet
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("- ") or line.startswith("*"):
            term = line[2:].strip().strip("'\"")
            if term:
                terms.add(term.lower())
    return terms


def check_us_terms_in_skills():
    """Check for unapproved US-specific terms in skill SKILL.md files."""
    failures = []
    allowlist = load_allowlist()
    for skill_dir in sorted(SKILL_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        text = skill_md.read_text(errors="replace")
        for pattern in US_TERM_PATTERNS:
            matches = pattern.findall(text)
            if matches:
                for m in matches:
                    if m.lower() not in allowlist:
                        failures.append(
                            f"{skill_md}: US term '{m}' found (unapproved)"
                        )
    return failures


def check_replacement_matrix_source_claims():
    """Check that every mapped curriculum claim in replacement-matrix has source_id/url/version/locator."""
    failures = []
    with open(REPLACEMENT_MATRIX_CSV, "r", newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        src_ids = row.get("source_ids", "").strip()
        if not src_ids:
            # skip rows without mapping
            continue
        # Row has a mapping, so it should have source_id/url/version/locator context
        # Check source-register for referenced sources
        src_list = [s.strip() for s in src_ids.split(",")]
        for src in src_list:
            # Look up in source register
            sr_path = SOURCE_REGISTER_CSV
            found = False
            with open(sr_path, "r", newline="") as sf:
                for sr in csv.DictReader(sf):
                    if sr["source_id"] == src:
                        found = True
                        # Verify it has url, version_or_effective_year, locator, content_hash
                        missing = []
                        if not sr.get("url", "").strip():
                            missing.append("url")
                        if not sr.get("version_or_effective_year", "").strip():
                            missing.append("version_or_effective_year")
                        if not sr.get("locator", "").strip():
                            missing.append("locator")
                        if not sr.get("content_hash", "").strip():
                            missing.append("content_hash")
                        if missing:
                            failures.append(
                                f"Replacement matrix row {row['inventory_id']} references {src} missing fields: {missing}"
                            )
                        break
            if not found:
                failures.append(
                    f"Replacement matrix row {row['inventory_id']} references {src} not found in source register"
                )
    return failures


def check_source_register_schema():
    """Validate source-register rows against the schema; require authority fields."""
    failures = []
    schema_path = SCHEMA_DIR / "source-register.schema.json"
    if not schema_path.exists():
        failures.append(f"Schema file not found: {schema_path}")
        return failures
    # Load schema manually (simplified) - check required fields and enums
    with open(schema_path, "r") as f:
        schema = json.load(f)
    required = schema.get("required", [])
    allowed_enums = {}
    for prop_name, prop_def in schema.get("properties", {}).items():
        if "enum" in prop_def:
            allowed_enums[prop_name] = prop_def["enum"]
        if "pattern" in prop_def:
            # store pattern for later
            allowed_enums[f"_pattern_{prop_name}"] = prop_def["pattern"]

    with open(SOURCE_REGISTER_CSV, "r", newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        for req in required:
            if req not in row or not row[req].strip():
                failures.append(
                    f"Source register row {row.get('source_id','?')}: missing required field '{req}'"
                )
        # Check enum constraints
        for prop_name, allowed in allowed_enums.items():
            if prop_name in row:
                val = row[prop_name]
                if allowed and val not in allowed:
                    failures.append(
                        f"Source register row {row.get('source_id','?')}: field '{prop_name}'='{val}' not in allowed enum {allowed}"
                    )
    return failures


def check_us_inventory_schema():
    """Validate US-specific-inventory CSV against its schema."""
    failures = []
    schema_path = SCHEMA_DIR / "us-specific-inventory.schema.json"
    if not schema_path.exists():
        failures.append(f"Schema file not found: {schema_path}")
        return failures
    with open(schema_path, "r") as f:
        schema = json.load(f)
    required = schema.get("required", [])
    allowed_enums = {}
    for prop_name, prop_def in schema.get("properties", {}).items():
        if "enum" in prop_def:
            allowed_enums[prop_name] = prop_def["enum"]
        if "pattern" in prop_def:
            allowed_enums[f"_pattern_{prop_name}"] = prop_def["pattern"]

    with open(INVENTORY_CSV, "r", newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        for req in required:
            if req not in row or not row[req].strip():
                failures.append(
                    f"Inventory row {row.get('inventory_id','?')}: missing required field '{req}'"
                )
        for prop_name, allowed in allowed_enums.items():
            if prop_name in row:
                val = row[prop_name]
                if allowed and val not in allowed:
                    failures.append(
                        f"Inventory row {row.get('inventory_id','?')}: field '{prop_name}'='{val}' not in allowed enum {allowed}"
                    )
    return failures


def check_skill_links():
    """Check that every file linked from each plugin/skills/**/SKILL.md exists."""
    failures = []
    for skill_dir in sorted(SKILL_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        text = skill_md.read_text(errors="replace")
        refs = []
        # Match backtick-quoted paths that have a path separator (/)
        # These are actual file references like `references/output.md` or `scripts/render.sh`
        for m in re.finditer(r"`[a-zA-Z0-9_/\.\-]+/[a-zA-Z0-9_/\.\-]+\.(?:md|json|sh|py|css|yml|yaml)`", text):
            refs.append(m.group(0).strip("`"))
        # Match actual Markdown links [text](path) with file extensions
        for m in re.finditer(r"\[([^\]]+)\]\(([^)]+\.(?:md|json|sh|py|css|yml|yaml))\)", text):
            refs.append(m.group(2))
        for ref in refs:
            ref_clean = ref.strip()
            parts = ref_clean.split("/")
            # Skip absolute or parent-relative paths
            if parts[0].startswith("/") or parts[0] in {".", ".."}:
                continue
            # Build path relative to the skill directory (where SKILL.md lives)
            p = skill_md.parent / ref_clean
            if not p.exists():
                failures.append(f"Skill link {skill_md}: referenced file '{ref}' does not exist")
    return failures


def check_duplicate_scripts():
    """Check for duplicate/shared rendering scripts under multiple skills."""
    failures = []
    script_patterns = set()
    for skill_dir in sorted(SKILL_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        scripts_dir = skill_dir / "scripts"
        if not scripts_dir.exists():
            continue
        for sp in scripts_dir.rglob("*.py"):
            rel = sp.relative_to(REPO_ROOT)
            # Check if same script name appears under multiple skills
            name_key = str(rel)
            if name_key in script_patterns:
                failures.append(
                    f"Duplicate script found: {name_key} appears under multiple skills"
                )
            else:
                script_patterns.add(name_key)
    return failures


def main():
    """Run all validation checks and produce baseline-red.md."""
    VALIDATION_DIR.mkdir(parents=True, exist_ok=True)

    all_failures = []

    # 1. US terms in skills
    all_failures.append(("US Terms in Skills", check_us_terms_in_skills()))

    # 2. Replacement matrix source claims
    all_failures.append(("Replacement Matrix Source Claims", check_replacement_matrix_source_claims()))

    # 3. Source register schema validation
    all_failures.append(("Source Register Schema", check_source_register_schema()))

    # 4. US inventory schema validation
    all_failures.append(("US Inventory Schema", check_us_inventory_schema()))

    # 5. Skill links
    all_failures.append(("Skill Links", check_skill_links()))

    # 6. Duplicate scripts
    all_failures.append(("Duplicate Scripts", check_duplicate_scripts()))

    # Print summary
    print("=" * 60)
    print("LOCALISATION CONTRACT VALIDATION SUMMARY")
    print("=" * 60)
    total = 0
    for category, failures in all_failures:
        print(f"\n[{category}]")
        if not failures:
            print("  (no failures)")
        for f in failures:
            print(f"  FAIL: {f}")
            total += 1
    print(f"\nTotal failing checks: {total}")
    print("=" * 60)

    # Write baseline-red.md
    baseline_path = VALIDATION_DIR / "baseline-red.md"
    with open(baseline_path, "w") as out:
        out.write("## Localisation Contract Validation Baseline (RED - US-only baseline)\n\n")
        out.write("_This file captures the expected failures when running the contract tests against the current (US-only) baseline._\n\n")
        out.write("=" * 60 + "\n")
        out.write("LOCALISATION CONTRACT VALIDATION SUMMARY\n")
        out.write("=" * 60 + "\n")
        for category, failures in all_failures:
            out.write(f"\n[{category}]\n")
            if not failures:
                out.write("  (no failures)\n")
            for f in failures:
                out.write(f"  FAIL: {f}\n")
        out.write(f"\nTotal failing checks: {total}\n")
        out.write("=" * 60 + "\n")
        out.write(
            "NOTE: These failures are EXPECTED for the US-only baseline. "
            "After implementing Australian localisation (renaming skills, replacing US terminology, updating source registers), these tests should pass.\n"
        )

    print(f"\nBaseline written to: {baseline_path}")


if __name__ == "__main__":
    main()