"""Test source register: enforce authority identity/type/owner/evidence for all sources."""
import csv
import json
import os
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SOURCE_REGISTER = REPO_ROOT / "docs" / "localisation" / "02-source-register.csv"
SCHEMA_PATH = REPO_ROOT / "docs" / "localisation" / "schema" / "source-register.schema.json"

REQUIRED_AUTHORITY_FIELDS = [
    "authority_name",
    "authority_type",
    "authority_evidence_url",
    "publication_owner",
    "authority_verification_status",
    "jurisdiction",
    "school_phase",
    "learning_area_or_subject",
    "document_title",
    "version_or_effective_year",
    "url",
    "locator",
    "licence",
    "retrieval_date",
    "content_hash",
]

ALLOWED_AUTHORITY_NAMES = {"ACARA", "QCAA", "NCCD", "Queensland Department of Education"}
ALLOWED_AUTHORITY_TYPES = {
    "statutory curriculum authority",
    "government department/agency",
    "official national education program",
}
ALLOWED_JURISDICTIONS = {"Australia", "Queensland"}
ALLOWED_SCHOOL_PHASES = {"F-10", "Years 11-12", "F-12", "cross-phase"}
CONTENT_HASH_PATTERN = re.compile(r"^sha256:[a-f0-9]{64}$")


def load_source_register():
    with open(SOURCE_REGISTER, newline="") as f:
        return list(csv.DictReader(f))


def load_schema():
    with open(SCHEMA_PATH) as f:
        return json.load(f)


class TestSourceRegisterAuthority:
    """Validate that every source has verified authority identity/type/owner/evidence."""

    def test_required_authority_fields_present(self):
        """Every source row must have all required authority fields populated."""
        rows = load_source_register()
        failures = []
        for row in rows:
            src_id = row.get("source_id", "?")
            for field in REQUIRED_AUTHORITY_FIELDS:
                val = row.get(field, "").strip()
                if not val:
                    failures.append(f"{src_id}: missing required field '{field}'")
        assert not failures, (
            "Sources missing required authority fields:\n" + "\n".join(failures)
        )

    def test_authority_name_in_allowed_set(self):
        """authority_name must be one of ACARA, QCAA, NCCD, Queensland Department of Education."""
        rows = load_source_register()
        failures = []
        for row in rows:
            src_id = row.get("source_id", "?")
            name = row.get("authority_name", "").strip()
            if name not in ALLOWED_AUTHORITY_NAMES:
                failures.append(f"{src_id}: authority_name='{name}' not in allowed set")
        assert not failures, (
            "Invalid authority_name values:\n" + "\n".join(failures)
        )

    def test_authority_type_in_allowed_set(self):
        """authority_type must be statutory curriculum authority, government department/agency, or official national education program."""
        rows = load_source_register()
        failures = []
        for row in rows:
            src_id = row.get("source_id", "?")
            atype = row.get("authority_type", "").strip()
            if atype not in ALLOWED_AUTHORITY_TYPES:
                failures.append(f"{src_id}: authority_type='{atype}' not in allowed set")
        assert not failures, (
            "Invalid authority_type values:\n" + "\n".join(failures)
        )

    def test_jurisdiction_in_allowed_set(self):
        """jurisdiction must be Australia or Queensland."""
        rows = load_source_register()
        failures = []
        for row in rows:
            src_id = row.get("source_id", "?")
            jur = row.get("jurisdiction", "").strip()
            if jur not in ALLOWED_JURISDICTIONS:
                failures.append(f"{src_id}: jurisdiction='{jur}' not in allowed set")
        assert not failures, (
            "Invalid jurisdiction values:\n" + "\n".join(failures)
        )

    def test_school_phase_in_allowed_set(self):
        """school_phase must be F-10, Years 11-12, F-12, or cross-phase."""
        rows = load_source_register()
        failures = []
        for row in rows:
            src_id = row.get("source_id", "?")
            phase = row.get("school_phase", "").strip()
            if phase not in ALLOWED_SCHOOL_PHASES:
                failures.append(f"{src_id}: school_phase='{phase}' not in allowed set")
        assert not failures, (
            "Invalid school_phase values:\n" + "\n".join(failures)
        )

    def test_content_hash_matches_pattern(self):
        """content_hash must match sha256:[a-f0-9]{64}."""
        rows = load_source_register()
        failures = []
        for row in rows:
            src_id = row.get("source_id", "?")
            ch = row.get("content_hash", "").strip()
            if not CONTENT_HASH_PATTERN.match(ch):
                failures.append(f"{src_id}: content_hash='{ch}' does not match pattern")
        assert not failures, (
            "Invalid content_hash values:\n" + "\n".join(failures)
        )

    def test_authority_verification_status_is_verified(self):
        """authority_verification_status must be 'verified'."""
        rows = load_source_register()
        failures = []
        for row in rows:
            src_id = row.get("source_id", "?")
            status = row.get("authority_verification_status", "").strip()
            if status != "verified":
                failures.append(f"{src_id}: authority_verification_status='{status}' not 'verified'")
        assert not failures, (
            "Sources with non-verified authority:\n" + "\n".join(failures)
        )

    def test_source_register_conforms_to_schema(self):
        """Source register must conform to the JSON schema."""
        schema = load_schema()
        rows = load_source_register()
        required = schema.get("required", [])
        failures = []
        for row in rows:
            src_id = row.get("source_id", "?")
            for req in required:
                if req not in row or not row[req].strip():
                    failures.append(f"{src_id}: schema-required field '{req}' missing")
            # Check enum constraints from schema
            for prop_name, prop_def in schema.get("properties", {}).items():
                if "enum" in prop_def:
                    val = row.get(prop_name, "").strip()
                    if val and val not in prop_def["enum"]:
                        failures.append(
                            f"{src_id}: field '{prop_name}'='{val}' not in schema enum {prop_def['enum']}"
                        )
                if "pattern" in prop_def:
                    val = row.get(prop_name, "").strip()
                    if val and not re.match(prop_def["pattern"], val):
                        failures.append(
                            f"{src_id}: field '{prop_name}'='{val}' does not match pattern {prop_def['pattern']}"
                        )
        assert not failures, (
            "Source register schema violations:\n" + "\n".join(failures)
        )